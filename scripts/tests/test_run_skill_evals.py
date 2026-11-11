"""Offline execution-lifetime checks; no Codex, credentials, or network required."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

spec = importlib.util.spec_from_file_location(
    "skill_eval_runner", Path(__file__).resolve().parents[1] / "run_skill_evals.py"
)
sys.path.insert(0, str(Path(spec.origin).parent))
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
sys.path.pop(0)


@unittest.skipUnless(os.name == "posix", "POSIX process groups")
class ProcessLifetimeTests(unittest.TestCase):
    def run_command(self, source, timeout=5):
        return runner.run_bounded(
            [sys.executable, "-c", source], stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL, timeout=timeout,
        )

    def test_success_preserves_effect(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "output"
            result = self.run_command(f"from pathlib import Path; Path({str(output)!r}).write_text('ok')")
            self.assertEqual(result, 0)
            self.assertEqual(output.read_text(), "ok")

    def test_nonzero_exit_is_not_success(self):
        self.assertEqual(self.run_command("raise SystemExit(7)"), 7)

    def test_timeout_stops_descendant_effect(self):
        with tempfile.TemporaryDirectory() as folder:
            ready = Path(folder) / "ready"
            late = Path(folder) / "late"
            child = (
                "import time; from pathlib import Path; "
                f"Path({str(ready)!r}).write_text('ready'); "
                f"time.sleep(1.2); Path({str(late)!r}).write_text('escaped')"
            )
            parent = (
                "import subprocess,sys,time; "
                f"subprocess.Popen([sys.executable, '-c', {child!r}]); time.sleep(10)"
            )
            result = self.run_command(parent, timeout=0.7)
            self.assertIsNone(result)
            self.assertTrue(ready.exists(), "child must start before timeout to exercise cleanup")
            time.sleep(0.8)
            self.assertFalse(late.exists(), "descendant wrote after the run timed out")


class PilotControlTests(unittest.TestCase):
    def test_candidate_exports_only_distribution_paths(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "source"
            package = source / "sample"
            package.mkdir(parents=True)
            runner.git("init", "-q", cwd=source)
            (source / ".gitignore").write_text("sample/private.txt\n")
            (package / "SKILL.md").write_text("staged version")
            (package / "removed.md").touch()
            runner.git("add", "--", "sample", cwd=source)
            (package / "SKILL.md").write_text("candidate version")
            (package / "removed.md").unlink()
            (package / "new.md").touch()
            (package / "private.txt").write_text("ignored control")
            destination = root / "candidate"
            runner.copy_candidate(source, destination)
            self.assertEqual(runner.inventory(destination), ["sample"])
            files = {path.name: path.read_text() for path in (destination / "sample").iterdir()}
            self.assertEqual(files, {"SKILL.md": "candidate version", "new.md": ""})

    def test_candidate_rejects_external_symbolic_link(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder)
            runner.git("init", "-q", cwd=source)
            package = source / "sample"
            package.mkdir()
            (package / "SKILL.md").touch()
            (package / "link").symlink_to("/path/outside/fixture")
            with self.assertRaisesRegex(ValueError, "symbolic link"):
                runner.copy_candidate(source, source / "candidate")

    def test_receipt_grader_distinguishes_fixture_from_clean_control(self):
        fixture = runner.EVALS / "fixtures" / "receipts"
        checker = runner.EVALS / "check_receipts.py"
        command = [sys.executable, "-I", "-B", str(checker)]
        bad = subprocess.run([*command, str(fixture), "-v"], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1, bad.stderr)
        self.assertIn("FAIL: test_independent_tenants", bad.stderr)
        self.assertIn("FAIL: test_conflict_does_not_change_receipt_or_state", bad.stderr)
        self.assertIn("test_rejected_calls_do_not_write (__main__.ReceiptAcceptance.test_rejected_calls_do_not_write) ... ok",
                      bad.stderr)
        good = subprocess.run([*command, str(runner.EVALS / "overlays" / "review-clean")],
                              capture_output=True, text=True)
        self.assertEqual(good.returncode, 0, good.stderr)

    @unittest.skipUnless(shutil.which("openspec"), "optional OpenSpec CLI")
    def test_real_openspec_fixture_validates_with_unfinished_tasks(self):
        source = runner.EVALS / "overlays" / "openspec"
        with tempfile.TemporaryDirectory() as temp:
            fixture = Path(temp) / "fixture"
            shutil.copytree(source, fixture)
            env = os.environ | {"OPENSPEC_TELEMETRY": "0"}
            commands = [
                ("validate", "--all", "--strict", "--json"),
                ("status", "--change", "tenant-receipts", "--json"),
                ("instructions", "apply", "--change", "tenant-receipts", "--json"),
            ]
            reports = [json.loads(subprocess.check_output(
                ["openspec", *args], cwd=fixture, env=env, text=True, timeout=15
            )) for args in commands]
            self.assertEqual(reports[0]["summary"]["totals"]["passed"], 2)
            self.assertTrue(reports[1]["isComplete"])
            self.assertEqual(reports[2]["progress"], {"total": 2, "complete": 0, "remaining": 2})
            delta = fixture / "openspec/changes/tenant-receipts/specs/receipts/spec.md"
            delta.write_text(delta.read_text().replace("Scenario: Request ID is replayed", "Scenario: Exact replay"))
            missing = subprocess.run(["openspec", *commands[0]], cwd=fixture, env=env,
                                     capture_output=True, text=True, timeout=15)
            self.assertEqual(missing.returncode, 1, missing.stdout)
            self.assertIn("Request ID is replayed", missing.stdout)

    def test_gateway_rejects_embedded_credentials(self):
        for url in ("https://token@example.test/v1", "https://example.test/?token=private",
                    "http://example.test/v1"):
            with self.subTest(url=url), self.assertRaises(argparse.ArgumentTypeError):
                runner.gateway_url(url)
        self.assertEqual(runner.gateway_url("http://127.0.0.1:8080/v1"), "http://127.0.0.1:8080/v1")


if __name__ == "__main__":
    unittest.main()
