"""Check the real OpenSpec delta and its consolidated capability."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
CHANGE = "tenant-receipts"


@unittest.skipUnless(shutil.which("openspec"), "optional OpenSpec CLI")
class OpenSpecArchiveTests(unittest.TestCase):
    def test_active_delta_and_archived_capability_validate(self):
        source = ROOT / "evals/overlays/openspec"
        with tempfile.TemporaryDirectory() as temp:
            fixture = Path(temp) / "fixture"
            shutil.copytree(source, fixture)
            env = os.environ | {"OPENSPEC_TELEMETRY": "0", "OPENSPEC_NO_UPDATE_CHECK": "1"}
            commands = [
                ("validate", "--all", "--strict"),
                ("archive", CHANGE, "--yes"),
                ("validate", "receipts", "--type", "spec", "--strict"),
            ]
            change = fixture / "openspec/changes" / CHANGE
            delta = change / "specs/receipts/spec.md"
            tasks = change / "tasks.md"
            tasks.write_text(tasks.read_text().replace("- [ ] ", "- [x] "))
            scenarios = [line for line in delta.read_text().splitlines() if line.startswith("#### Scenario:")]
            self.assertIn("#### Scenario: Request ID is replayed", scenarios)
            for args in commands:
                result = subprocess.run(["openspec", *args], cwd=fixture, env=env,
                                        capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertFalse(change.exists())
            archives = list((change.parent / "archive").glob(f"*-{CHANGE}"))
            self.assertEqual(len(archives), 1)
            self.assertTrue((archives[0] / "specs/receipts/spec.md").is_file())
            consolidated = (fixture / "openspec/specs/receipts/spec.md").read_text().splitlines()
            self.assertEqual([line for line in consolidated if line.startswith("#### Scenario:")], scenarios)
