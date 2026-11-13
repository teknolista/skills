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
import stat
import subprocess
import tarfile
import tempfile
import time
from urllib.parse import urlsplit

import eval_isolation
import eval_outcomes


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd)


def inventory(directory):
    return sorted(path.parent.name for path in directory.glob("*/SKILL.md"))


def copy_candidate(source, destination):
    """Copy the working-tree files eligible for distribution as skill packages."""
    source = source.resolve()
    listed = git("ls-files", "--cached", "--others", "--exclude-standard", "-z", cwd=source)
    paths = {Path(os.fsdecode(raw)) for raw in listed.split(b"\0") if raw}
    packages = {path.parts[0] for path in paths
                if len(path.parts) == 2 and path.name == "SKILL.md" and (source / path).exists()}
    if not packages:
        raise ValueError("candidate has no skill packages")
    for path in sorted(paths):
        if len(path.parts) < 2 or path.parts[0] not in packages:
            continue
        entry = source / path
        if entry.is_symlink() or entry.resolve() != entry:
            raise ValueError(f"candidate package path contains a symbolic link: {path}")
        if not entry.exists():
            continue
        if not entry.is_file():
            raise ValueError(f"candidate package path is not a regular file: {path}")
        target = destination / path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(entry, target)


def snapshot(directory):
    if not eval_isolation.has_direct_path(directory) or (directory.exists() and not directory.is_dir()):
        return {"": {"unsafe_root": "symbolic link or substituted parent"}}
    files = {}
    for path in sorted(directory.rglob("*")):
        relative = path.relative_to(directory)
        if any(part in {".git", ".agents", "__pycache__"} for part in relative.parts):
            continue
        if path.is_symlink():
            files[str(relative)] = {"symlink": str(path.readlink())}
            continue
        info = path.lstat()
        if stat.S_ISREG(info.st_mode):
            if info.st_size > 32 * 1024 * 1024:
                files[str(relative)] = {"unhashed_size": info.st_size}
                continue
            with path.open("rb") as source:
                files[str(relative)] = hashlib.file_digest(source, "sha256").hexdigest()
        elif not stat.S_ISDIR(info.st_mode):
            files[str(relative)] = {"special_file_mode": info.st_mode}
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


def trial_command(options, work, tools, prompt):
    codex = "/tools/codex" if options.isolated else options.codex
    cwd = eval_isolation.WORKSPACE if options.isolated else str(work)
    command = [codex, "exec", "--ignore-user-config", "--ephemeral", "--cd", cwd,
               "--model", options.model, "-c", f"model_reasoning_effort={json.dumps(options.effort)}",
               "-c", f"projects.{json.dumps(cwd)}.trust_level=\"trusted\"", "--json"]
    if options.isolated:
        command.extend([
            "--dangerously-bypass-approvals-and-sandbox",
            "-c", 'model_provider="eval_gateway"',
            "-c", 'model_providers.eval_gateway.name="Evaluation gateway"',
            "-c", f"model_providers.eval_gateway.base_url={json.dumps(options.gateway)}",
            "-c", 'model_providers.eval_gateway.wire_api="responses"',
        ])
        return eval_isolation.command(work, tools, [*command, prompt])
    return [options.codex, "-a", "never", *command[1:], "--sandbox", "workspace-write", prompt]


def inspect_git(work, options, *args):
    command = ["git", "-c", "core.fsmonitor=false", "-c", "core.hooksPath=/dev/null", *args]
    if options.grade or options.isolated:
        if not eval_isolation.has_direct_path(work) or not work.is_dir():
            raise RuntimeError("evaluation workspace was replaced")
    if options.grade:
        with eval_isolation.offline_command(work, command) as (sandbox, fds):
            return subprocess.check_output(sandbox, pass_fds=fds, cwd=work, timeout=20)
    if options.isolated:
        command = eval_isolation.command(work, {}, command)
    return subprocess.check_output(command, cwd=work, timeout=20)


def run_case(job, cases, options, output, sources, tools):
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
    initial_head = git("rev-parse", "HEAD", cwd=work).decode().strip()
    before = snapshot(work)
    installed = work / ".agents/skills"
    if arm in sources:
        source = sources[arm]
        for name in inventory(source):
            shutil.copytree(source / name, installed / name)

    prompt = case["prompt"]
    explicitly_invoked = bool(options.explicit and arm in sources and case["owner"])
    if explicitly_invoked:
        owner = case["owner"]
        prompt = f"Use ${owner} at .agents/skills/{owner}/SKILL.md.\n\n{prompt}"
    if options.isolated:
        eval_isolation.probe(work, tools, (EVALS / "check_receipts.py", output / "settings.json"))
    command = trial_command(options, work, tools, prompt)
    started = time.monotonic()
    with (run / "events.jsonl").open("w") as events, (run / "stderr.txt").open("w") as errors:
        exit_code = run_bounded(command, stdout=events, stderr=errors, timeout=options.timeout)
    elapsed = round(time.monotonic() - started, 2)
    events = list(read_events(run / "events.jsonl"))
    items = [event["item"] for event in events if event.get("type") == "item.completed"]
    messages = [item["text"] for item in items if item["type"] == "agent_message"]
    (run / "answer.txt").write_text(messages[-1] + "\n" if messages else "")
    commands = [item.get("command", "") for item in items if item["type"] == "command_execution"]
    after = snapshot(work)
    installed_after = snapshot(installed)
    installed_names = inventory(installed) if "" not in installed_after else []
    inspection_error = None
    revision = state = b""
    try:
        revision = inspect_git(work, options, "rev-parse", "HEAD")
        state = inspect_git(work, options, "--no-optional-locks", "status", "--porcelain=v1")
        diff = inspect_git(work, options, "diff", "--no-ext-diff", "--no-textconv", "HEAD", "--")
        (run / "diff.patch").write_bytes(diff)
    except (RuntimeError, OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        inspection_error = str(exc)
    installed_before = snapshot(sources[arm]) if arm in sources else {}
    result = {
        "case": case_id, "arm": arm, "attempt": attempt, "run": run.name,
        "prompt_mode": "explicit" if explicitly_invoked else "unhinted",
        "exit_code": exit_code, "seconds": elapsed,
        "execution_status": execution_status(exit_code, events, messages, inspection_error),
        "git_inspection_error": inspection_error,
        "thread_id": next((event["thread_id"] for event in events if event.get("type") == "thread.started"), None),
        "usage": next((event["usage"] for event in reversed(events) if event.get("type") == "turn.completed"), None),
        "reported_errors": sum(item["type"] == "error" for item in items),
        "tool_events": sum(item["type"] in {"command_execution", "mcp_tool_call", "web_search", "file_change"}
                           for item in items),
        "skill_paths_mentioned_in_commands": [name for name in installed_names
                                             if any(f"{name}/SKILL.md" in cmd for cmd in commands)],
        "changed_paths": changes(before, after), "fixture_sha256": before,
        "installed_skill_changes": changes(installed_before, installed_after),
        "initial_head": initial_head, "fixture_head": revision.decode().strip(),
        "fixture_status": state.decode(errors="replace").splitlines(),
    }
    result["grade"] = (eval_outcomes.score(EVALS, case, work, result, options.seed + attempt - 1)
                       if options.grade else {"status": "not-run"})
    return result


def execution_status(exit_code, events, messages, inspection_error):
    if exit_code is None:
        return "timeout"
    if exit_code:
        return "cli-error"
    if inspection_error:
        return "inspection-error"
    turn_events = [event["type"] for event in events if event.get("type") in {"turn.completed", "turn.failed"}]
    if not messages or not turn_events or turn_events[-1] != "turn.completed":
        return "incomplete-turn"
    return "complete"


def native_tool(executable):
    path = shutil.which(executable)
    if path:
        resolved = Path(path).resolve()
        with resolved.open("rb") as binary:
            if binary.read(4) == b"\x7fELF":
                return resolved
    raise ValueError(f"{executable} must resolve to a standalone Linux executable for isolation")


def gateway_url(value):
    url = urlsplit(value)
    if (not url.hostname or url.username or url.password or url.query or url.fragment
            or (url.scheme != "https" and not (url.scheme == "http" and url.hostname in
                                               {"localhost", "127.0.0.1", "::1"}))):
        raise argparse.ArgumentTypeError("use an HTTPS or loopback HTTP gateway URL without credentials")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    try:
        cases = eval_outcomes.load_cases(EVALS, inventory(ROOT))
    except (OSError, ValueError) as exc:
        parser.error(f"case manifest: {exc}")
    parser.add_argument("--baseline", help="Git revision to install as the baseline arm")
    parser.add_argument("--arms", nargs="+", choices=("none", "baseline", "candidate"),
                        default=["none", "baseline"])
    parser.add_argument("--cases", nargs="+", choices=tuple(cases),
                        default=[name for name, case in cases.items() if not case.get("requires")])
    parser.add_argument("--explicit", action="store_true", help="Explicitly invoke the fixture's owner in skill arms")
    parser.add_argument("--model", help="Model exposed by the selected host or gateway")
    parser.add_argument("--effort", default="low")
    parser.add_argument("--codex", default="codex")
    parser.add_argument("--isolated", action="store_true", help="Use Linux mount and process isolation")
    parser.add_argument("--gateway", type=gateway_url, help="Responses API gateway for isolated model runs")
    parser.add_argument("--openspec", help="Standalone OpenSpec executable to mount for isolated runs")
    parser.add_argument("--check-isolation", action="store_true", help="Run offline isolation probes and exit")
    parser.add_argument("--check-cases", action="store_true", help="Validate the case inventory and exit")
    parser.add_argument("--grade", action="store_true", help="Run independent offline artifact checks (Linux)")
    parser.add_argument("--seed", type=int, default=20261113, help="First evaluator-only receipt input seed")
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
    if options.check_cases:
        print(f"Validated {len(cases)} evaluation cases.")
        return
    if options.check_isolation or options.grade:
        with tempfile.TemporaryDirectory(prefix="skill-eval-probe-") as scratch:
            root = Path(scratch)
            workspace = root / "workspace"
            workspace.mkdir()
            (workspace / "AGENTS.md").touch()
            sibling = root / "other-run"
            sibling.write_text("other run control")
            try:
                eval_isolation.probe(workspace, {}, (EVALS / "check_receipts.py", sibling))
                if options.grade:
                    eval_isolation.probe_offline(workspace, sibling, "AGENTS.md")
            except (RuntimeError, OSError, subprocess.SubprocessError) as exc:
                parser.error(f"selected isolation boundary is unavailable: {exc}")
        print("Mount isolation passed. Offline grading mount, socket and resource checks passed."
              if options.grade else "Mount isolation passed.")
    if options.check_isolation:
        return
    if options.isolated and not (options.gateway and options.model):
        parser.error("--isolated model runs require --gateway and an explicit tool-capable --model")
    options.model = options.model or "gpt-6.1-sol"
    if not options.isolated and (options.gateway or options.openspec):
        parser.error("--gateway and --openspec are for isolated runs")
    if "baseline" in options.arms and not options.baseline:
        parser.error("--baseline is required when selecting the baseline arm")
    if options.explicit and "none" in options.arms:
        parser.error("explicit invocation compares installed arms; use an unhinted run for the none arm")
    tools = {}
    if options.isolated:
        try:
            tools["codex"] = native_tool(options.codex)
            sidecar = tools["codex"].with_name("codex-code-mode-host")
            if sidecar.is_file():
                tools[sidecar.name] = native_tool(str(sidecar))
            if options.openspec:
                tools["openspec"] = native_tool(options.openspec)
        except ValueError as exc:
            parser.error(str(exc))
    needs_openspec = any("openspec" in cases[name].get("requires", ()) for name in options.cases)
    if needs_openspec and not (tools.get("openspec") if options.isolated else shutil.which("openspec")):
        parser.error("selected case requires OpenSpec; provide --openspec for isolated runs or install it on PATH")
    revision = (git("rev-parse", "--verify", "--end-of-options", f"{options.baseline}^{{commit}}")
                .decode().strip() if options.baseline else None)
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
            try:
                copy_candidate(ROOT, candidate)
            except ValueError as exc:
                parser.error(str(exc))
        sources = {"baseline": baseline, "candidate": candidate}
        source_hashes = {}
        owners = {cases[case]["owner"] for case in options.cases} - {None}
        for arm in options.arms:
            if arm in sources:
                names = inventory(sources[arm])
                if options.explicit and owners - set(names):
                    parser.error(f"{arm} has no owner skill(s): {', '.join(sorted(owners - set(names)))}")
                source_hashes[arm] = {name: snapshot(sources[arm] / name) for name in names}
        metadata = vars(options) | {
            "baseline": revision, "codex_version": subprocess.check_output([options.codex, "--version"],
                                                                           text=True).strip(),
            "candidate_base": git("rev-parse", "HEAD").decode().strip() if "candidate" in options.arms else None,
            "execution_boundary": "mount-and-process; shared network" if options.isolated else "workspace-write",
            "openspec_version": subprocess.check_output(
                [tools.get("openspec", "openspec"), "--version"], text=True, timeout=15
            ).strip() if needs_openspec else None,
            "case_definitions": {case: cases[case] for case in options.cases},
            "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "grader_sha256": {
                path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                for path in (Path(eval_outcomes.__file__), Path(eval_isolation.__file__), EVALS / "check_receipts.py")
            } if options.grade else {},
            "skill_sha256": source_hashes,
        }
        (output / "settings.json").write_text(json.dumps(metadata, indent=2) + "\n")
        jobs = []
        for attempt in range(1, options.repetitions + 1):
            for index, case in enumerate(options.cases):
                arms = options.arms if (attempt + index) % 2 else list(reversed(options.arms))
                jobs.extend((case, arm, attempt) for arm in arms)
        summary = {}
        with ThreadPoolExecutor(max_workers=options.workers) as pool, (output / "results.jsonl").open("w") as report:
            for result in pool.map(lambda job: run_case(job, cases, options, output, sources, tools), jobs):
                eval_outcomes.count_result(summary, result)
                report.write(json.dumps(result) + "\n")
                report.flush()
                print(f"{result['run']} exit={result['exit_code']} seconds={result['seconds']} "
                      f"execution={result['execution_status']} grade={result['grade']['status']}", flush=True)
        (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")


if __name__ == "__main__":
    main()
