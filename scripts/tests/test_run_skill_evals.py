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
from unittest.mock import patch

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
        seed = 53
        bad = runner.eval_outcomes.check_receipts(runner.EVALS, fixture, seed)
        if bad["status"] == "incomplete":
            self.skipTest(bad["reason"])
        self.assertEqual(bad["status"], "fail")
        self.assertEqual(sum(bad["checks"].values()), 6)
        self.assertFalse(bad["checks"]["independent_tenants_0"])
        self.assertFalse(bad["checks"]["conflicting_replay_0"])
        self.assertTrue(bad["checks"]["rejected_calls_0"])
        good = runner.eval_outcomes.check_receipts(runner.EVALS, runner.EVALS / "overlays" / "review-clean", seed)
        self.assertEqual(good["status"], "pass")
        self.assertEqual(sum(good["checks"].values()), 12)

    def test_hard_coded_fixture_solution_and_false_success_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            workspace = Path(folder)
            source = workspace / "receipts.py"
            fixed = (runner.EVALS / "overlays" / "review-clean" / "receipts.py").read_text()
            source.write_text(fixed.replace("key = (tenant, request_id)",
                                            "key = (tenant, request_id) if request_id == '123' else request_id"))
            hard_coded = runner.eval_outcomes.check_receipts(runner.EVALS, workspace, 53)
            if hard_coded["status"] == "incomplete":
                self.skipTest(hard_coded["reason"])
            self.assertEqual(hard_coded["status"], "fail")
            self.assertFalse(hard_coded["checks"]["independent_tenants_0"])
            source.write_text("import os\nprint('{\"status\":\"pass\"}', flush=True)\nos._exit(0)\n")
            forged = runner.eval_outcomes.check_receipts(runner.EVALS, workspace, 53)
            self.assertEqual(forged["status"], "fail")

    def test_candidate_has_no_access_to_evaluator_workspace_or_sockets(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            workspace = root / "workspace"
            workspace.mkdir()
            sentinel = root / "outside"
            sentinel.write_text("trusted")
            fixed = (runner.EVALS / "overlays" / "review-clean" / "receipts.py").read_text()
            controls = f"""
from pathlib import Path
import socket

assert not Path({str(sentinel)!r}).exists()
for target in (Path({str(sentinel)!r}), Path('/workspace/receipt-leak')):
    try:
        target.write_text('unexpected write')
    except OSError:
        pass
    else:
        raise AssertionError('write escaped the boundary')
try:
    socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
except PermissionError:
    pass
else:
    raise AssertionError('socket escaped the boundary')
"""
            (workspace / "receipts.py").write_text(fixed + controls)
            result = runner.eval_outcomes.check_receipts(runner.EVALS, workspace, 53)
            if result["status"] == "incomplete":
                self.skipTest(result["reason"])
            self.assertEqual(result["status"], "pass")
            self.assertEqual(sentinel.read_text(), "trusted")
            self.assertFalse((workspace / "receipt-leak").exists())

    def test_execution_success_and_fixture_success_are_distinct(self):
        completed = [{"type": "turn.completed"}]
        self.assertEqual(runner.execution_status(0, completed, [], None), "incomplete-turn")
        self.assertEqual(runner.execution_status(0, completed, ["Done"], None), "complete")
        with tempfile.TemporaryDirectory() as folder:
            workspace = Path(folder)
            fixture = runner.EVALS / "fixtures" / "copy" / "README.md"
            (workspace / "README.md").write_bytes(fixture.read_bytes().replace(b"Recepit", b"Receipt"))
            cases = runner.eval_outcomes.load_cases(runner.EVALS, runner.inventory(runner.ROOT))
            result = {
                "execution_status": "complete",
                "changed_paths": ["README.md"],
                "installed_skill_changes": [],
                "fixture_head": "initial",
                "initial_head": "initial",
            }
            case = cases["copy-near-miss"]
            grade = runner.eval_outcomes.score(runner.EVALS, case, workspace, result, 53)
            self.assertEqual(grade["status"], "pass")
            result["changed_paths"].append("unrelated.txt")
            grade = runner.eval_outcomes.score(runner.EVALS, case, workspace, result, 53)
            self.assertEqual(grade["status"], "fail")
            result["execution_status"] = "timeout"
            grade = runner.eval_outcomes.score(runner.EVALS, case, workspace, result, 53)
            self.assertEqual(grade["status"], "incomplete")

    def test_case_manifest_rejects_an_unknown_owner(self):
        with tempfile.TemporaryDirectory() as folder:
            evals = Path(folder)
            (evals / "fixtures" / "copy").mkdir(parents=True)
            case = {"owner": "absent", "fixture": "copy", "prompt": "fix the heading"}
            (evals / "cases.json").write_text(json.dumps({"copy": case}))
            with self.assertRaisesRegex(ValueError, "invalid skill owner"):
                runner.eval_outcomes.load_cases(evals, ["http-api"])

    def test_openspec_task_grading_accepts_evidence_but_preserves_work_items(self):
        with tempfile.TemporaryDirectory() as folder:
            workspace = Path(folder)
            tasks = runner.eval_outcomes.TASKS
            task_file = workspace / tasks
            task_file.parent.mkdir(parents=True)
            original = (runner.EVALS / "overlays/openspec" / tasks).read_bytes()
            checked = original.replace(b"- [ ]", b"- [x]")
            result = {
                "execution_status": "complete",
                "changed_paths": ["receipts.py", "test_receipts.py", tasks],
                "installed_skill_changes": [],
                "fixture_head": "initial",
                "initial_head": "initial",
            }
            case = {"grader": "openspec-receipts", "overlay": "openspec"}
            with patch.object(runner.eval_outcomes, "check_receipts", return_value={"status": "pass"}):
                task_file.write_bytes(checked + b"\nEvidence: focused tests passed.\n")
                grade = runner.eval_outcomes.score(runner.EVALS, case, workspace, result, 53)
                self.assertEqual(grade["status"], "manual")
                for changed in (
                    checked.replace(b"1.1 Implement", b"1.1 Skip"),
                    checked.replace(b"- [x] 1.2", b"- [ ] 1.2"),
                ):
                    task_file.write_bytes(changed)
                    grade = runner.eval_outcomes.score(runner.EVALS, case, workspace, result, 53)
                    self.assertEqual(grade["status"], "fail")

    def test_authored_regression_must_detect_unauthorized_side_effect(self):
        test_body = """import unittest
from service import queue_export

class QueueContract(unittest.TestCase):
    def test_known_document_rejects_non_owner(self):
        jobs = [('other', 'already-queued')]
        self.assertEqual(queue_export('attacker', 'private', {'private': 'owner'}, jobs), 403)
"""
        with tempfile.TemporaryDirectory() as folder:
            workspace = Path(folder)
            test_file = workspace / "test_service.py"
            test_file.write_text(test_body)
            case = {"fixture": "test-effect"}
            weak = runner.eval_outcomes.check_authored_tests(runner.EVALS, case, workspace)
            if weak["status"] == "incomplete":
                self.skipTest(weak["reason"])
            self.assertEqual(weak, {
                "status": "fail", "checks": {"clean_tests_passed": True, "seeded_effect_detected": False},
            })
            test_file.write_text(test_body + "        self.assertEqual(jobs, [('other', 'already-queued')])\n")
            strong = runner.eval_outcomes.check_authored_tests(runner.EVALS, case, workspace)
            self.assertEqual(strong, {
                "status": "pass", "checks": {"clean_tests_passed": True, "seeded_effect_detected": True},
            })

    def test_grading_does_not_read_through_symlink_parents(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            outside = root / "outside"
            outside.mkdir()
            (outside / "notes.md").write_text("external")
            workspace = root / "workspace"
            workspace.mkdir()
            (workspace / "docs").symlink_to(outside, target_is_directory=True)
            self.assertEqual(runner.eval_outcomes.bounded_bytes(workspace / "docs/notes.md"), b"")
            self.assertEqual(runner.snapshot(workspace), {"docs": {"symlink": str(outside)}})
            (workspace / "loop").symlink_to("loop")
            self.assertEqual(runner.eval_outcomes.bounded_bytes(workspace / "loop/notes.md"), b"")
            self.assertEqual(runner.snapshot(workspace / "loop"), {"": {"unsafe_root": "symbolic link or substituted parent"}})

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
