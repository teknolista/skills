"""Run synthetic skill evaluations in fresh Codex CLI workspaces."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tarfile
import tempfile
import time


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd)


def inventory(directory):
    return sorted(path.parent.name for path in directory.glob("*/SKILL.md"))


def snapshot(directory):
    files = {}
    for path in sorted(directory.rglob("*")):
        relative = path.relative_to(directory)
        if any(part in {".git", ".agents", "__pycache__"} for part in relative.parts):
            continue
        if path.is_symlink():
            files[str(relative)] = {"symlink": str(path.readlink())}
        elif path.is_file():
            files[str(relative)] = hashlib.sha256(path.read_bytes()).hexdigest()
    return files


def changes(before, after):
    return sorted(path for path in before.keys() | after.keys() if before.get(path) != after.get(path))


def read_events(path):
    for line in path.read_text().splitlines():
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            continue


def run_bounded(command, *, stdout, stderr, timeout):
    """Stop the POSIX process group on timeout, including ordinary descendants.

    This is lifecycle cleanup, not isolation against processes that escape the group.
    """
    if os.name != "posix":
        raise RuntimeError("Evaluation process-group cleanup requires a POSIX host")
    with subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr,
                          start_new_session=True) as process:
        try:
            return process.wait(timeout=timeout)
        except BaseException as exc:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            process.wait()
            if isinstance(exc, subprocess.TimeoutExpired):
                return None
            raise


def run_case(job, cases, options, output, sources):
    case_id, arm, attempt = job
    case = cases[case_id]
    run = output / f"{case_id}-{arm}-{attempt}"
    work = run / "workspace"
    shutil.copytree(EVALS / "fixtures" / case["fixture"], work)
    if "overlay" in case:
        shutil.copytree(EVALS / "overlays" / case["overlay"], work, dirs_exist_ok=True)
    git("init", "--quiet", "--template=", cwd=work)
    (work / ".git/info").mkdir(exist_ok=True)
    (work / ".git/info/exclude").write_text(".agents/\n__pycache__/\n")
    git("add", "--all", cwd=work)
    git("-c", "user.name=Skill Eval", "-c", "user.email=eval@example.invalid",
        "-c", "commit.gpgSign=false", "-c", "core.hooksPath=/dev/null",
        "commit", "--quiet", "-m", "Synthetic starting state", cwd=work)
    before = snapshot(work)
    installed = work / ".agents/skills"
    if arm in sources:
        source = sources[arm]
        for name in inventory(source):
            shutil.copytree(source / name, installed / name)

    prompt = case["prompt"]
    if options.explicit and arm in sources and case["owner"]:
        owner = case["owner"]
        prompt = f"Use ${owner} at .agents/skills/{owner}/SKILL.md.\n\n{prompt}"
    command = [
        options.codex, "-a", "never", "exec", "--ignore-user-config", "--ephemeral",
        "--sandbox", "workspace-write", "--cd", str(work), "--model", options.model,
        "-c", f"model_reasoning_effort={json.dumps(options.effort)}",
        "-c", f"projects.{json.dumps(str(work))}.trust_level=\"trusted\"", "--json", prompt,
    ]
    started = time.monotonic()
    with (run / "events.jsonl").open("w") as events, (run / "stderr.txt").open("w") as errors:
        exit_code = run_bounded(command, stdout=events, stderr=errors, timeout=options.timeout)
    events = list(read_events(run / "events.jsonl"))
    items = [event["item"] for event in events if event.get("type") == "item.completed"]
    messages = [item["text"] for item in items if item["type"] == "agent_message"]
    (run / "answer.txt").write_text(messages[-1] + "\n" if messages else "")
    commands = [item.get("command", "") for item in items if item["type"] == "command_execution"]
    after = snapshot(work)
    revision = git("rev-parse", "HEAD", cwd=work)
    state = git("status", "--porcelain=v1", cwd=work)
    (run / "diff.patch").write_bytes(git("diff", "--no-ext-diff", "HEAD", "--", cwd=work))
    installed_before = snapshot(sources[arm]) if arm in sources else {}
    return {
        "case": case_id, "arm": arm, "attempt": attempt, "run": run.name,
        "exit_code": exit_code, "seconds": round(time.monotonic() - started, 2),
        "thread_id": next((event["thread_id"] for event in events if event.get("type") == "thread.started"), None),
        "usage": next((event["usage"] for event in reversed(events) if event.get("type") == "turn.completed"), None),
        "tool_events": sum(item["type"] in {"command_execution", "mcp_tool_call", "web_search", "file_change"}
                           for item in items),
        "skill_paths_mentioned_in_commands": [name for name in inventory(installed)
                                             if any(f"{name}/SKILL.md" in cmd for cmd in commands)],
        "changed_paths": changes(before, after), "fixture_sha256": before,
        "installed_skill_changes": changes(installed_before, snapshot(installed)),
        "fixture_head": revision.decode().strip(), "fixture_status": state.decode().splitlines(),
    }


def main():
    cases = json.loads((EVALS / "cases.json").read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, help="Git revision to install as the baseline arm")
    parser.add_argument("--arms", nargs="+", choices=("none", "baseline", "candidate"),
                        default=["none", "baseline"])
    parser.add_argument("--cases", nargs="+", choices=tuple(cases), default=list(cases))
    parser.add_argument("--explicit", action="store_true", help="Explicitly invoke the fixture's owner in skill arms")
    parser.add_argument("--model", default="gpt-6.1-sol")
    parser.add_argument("--effort", default="low")
    parser.add_argument("--codex", default="codex")
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--repetitions", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=180, help="Per-run wall timeout in seconds")
    options = parser.parse_args()
    if os.name != "posix":
        parser.error("the evaluation runner requires a POSIX host for process-group cleanup")
    if min(options.workers, options.repetitions, options.timeout) < 1:
        parser.error("workers, repetitions and timeout must be positive")
    if len(set(options.arms)) != len(options.arms) or len(set(options.cases)) != len(options.cases):
        parser.error("select each arm and case only once")
    revision = git("rev-parse", "--verify", "--end-of-options", f"{options.baseline}^{{commit}}").decode().strip()
    output = Path(tempfile.mkdtemp(prefix="skill-eval-"))
    print(output, flush=True)
    with tempfile.TemporaryDirectory(prefix="skill-eval-sources-") as source_dir:
        baseline = Path(source_dir) / "baseline"
        candidate = Path(source_dir) / "candidate"
        if "baseline" in options.arms:
            paths = git("ls-tree", "-rz", "--name-only", revision).decode().split("\0")
            packages = [path.split("/")[0] for path in paths if path.count("/") == 1 and path.endswith("/SKILL.md")]
            if not packages:
                parser.error("baseline has no skill packages")
            with tarfile.open(fileobj=io.BytesIO(git("archive", revision, "--", *packages))) as archive:
                archive.extractall(baseline, filter="data")
        if "candidate" in options.arms:
            for name in inventory(ROOT):
                package = ROOT / name
                if package.is_symlink() or any(path.is_symlink() for path in package.rglob("*")):
                    parser.error(f"candidate package {name} contains a symbolic link")
                shutil.copytree(package, candidate / name)
        sources = {"baseline": baseline, "candidate": candidate}
        source_hashes = {}
        for arm in options.arms:
            if arm in sources:
                source_hashes[arm] = {name: snapshot(sources[arm] / name) for name in inventory(sources[arm])}
        metadata = vars(options) | {
            "baseline": revision, "codex_version": subprocess.check_output([options.codex, "--version"],
                                                                           text=True).strip(),
            "case_definitions": {case: cases[case] for case in options.cases},
            "skill_sha256": source_hashes,
        }
        (output / "settings.json").write_text(json.dumps(metadata, indent=2) + "\n")
        jobs = []
        for attempt in range(1, options.repetitions + 1):
            for index, case in enumerate(options.cases):
                arms = options.arms if (attempt + index) % 2 else list(reversed(options.arms))
                jobs.extend((case, arm, attempt) for arm in arms)
        with ThreadPoolExecutor(max_workers=options.workers) as pool, (output / "results.jsonl").open("w") as report:
            for result in pool.map(lambda job: run_case(job, cases, options, output, sources), jobs):
                report.write(json.dumps(result) + "\n")
                report.flush()
                print(f"{result['run']} exit={result['exit_code']} seconds={result['seconds']}", flush=True)


if __name__ == "__main__":
    main()
