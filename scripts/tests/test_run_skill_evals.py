"""Offline execution-lifetime checks; no Codex, credentials, or network required."""
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

spec = importlib.util.spec_from_file_location(
    "skill_eval_runner", Path(__file__).resolve().parents[1] / "run_skill_evals.py"
)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


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


if __name__ == "__main__":
    unittest.main()
