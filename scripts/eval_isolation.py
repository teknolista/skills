"""Linux mount and process isolation for one synthetic evaluation workspace."""

import os
from pathlib import Path
import shutil
import subprocess


WORKSPACE = "/workspace"


def command(workspace, tools, argv):
    """Build a fresh sandbox with a private home and explicitly selected tools."""
    bwrap = shutil.which("bwrap")
    if not bwrap or not Path("/usr/bin/python3").is_file():
        raise RuntimeError("isolated evaluations require Linux Bubblewrap and /usr/bin/python3")
    args = [
        bwrap, "--unshare-user", "--unshare-pid", "--unshare-ipc", "--unshare-uts",
        "--die-with-parent", "--new-session", "--clearenv", "--proc", "/proc",
        "--dev", "/dev", "--tmpfs", "/tmp", "--dir", "/home/eval/.codex",
        "--setenv", "HOME", "/home/eval", "--setenv", "CODEX_HOME", "/home/eval/.codex",
        "--setenv", "PATH", "/tools:/usr/bin:/bin", "--setenv", "LANG", "C.UTF-8",
        "--setenv", "SHELL", "/bin/bash",
        "--setenv", "OPENSPEC_TELEMETRY", "0", "--setenv", "GIT_CONFIG_NOSYSTEM", "1",
    ]
    for path in ("/usr/bin", "/usr/lib", "/usr/lib64", "/bin", "/lib", "/lib64",
                 "/etc/ssl/certs", "/etc/hosts", "/etc/resolv.conf", "/etc/nsswitch.conf"):
        if Path(path).is_symlink() and path in ("/bin", "/lib", "/lib64"):
            args.extend(("--symlink", os.readlink(path), path))
        elif Path(path).exists():
            args.extend(("--ro-bind", path, path))
    for name, path in tools.items():
        args.extend(("--ro-bind", str(path), f"/tools/{name}"))
    return [*args, "--bind", str(workspace), WORKSPACE, "--chdir", WORKSPACE, "--", *argv]


def probe(workspace, tools, protected_paths):
    """Check mount exclusion with real files and a positive workspace control."""
    source = """
from pathlib import Path
import sys

assert Path.cwd() == Path('/workspace')
assert Path('AGENTS.md').is_file() or Path('.git').is_dir()
for name in sys.argv[1:]:
    path = Path(name)
    if path.exists():
        raise SystemExit(f'host path visible: {path}')
    for operation in (lambda: path.open('rb'), lambda: path.open('r+b')):
        try:
            handle = operation()
        except OSError:
            continue
        handle.close()
        raise SystemExit(f'host path accessible: {path}')
probe = Path('/tmp/workspace-probe')
probe.write_text('ok')
assert probe.read_text() == 'ok'
"""
    for path in protected_paths:
        if not path.is_file():
            raise RuntimeError(f"missing isolation control: {path}")
    subprocess.run(
        command(workspace, tools, ["/usr/bin/python3", "-I", "-c", source,
                                   *(str(path) for path in protected_paths)]),
        stdin=subprocess.DEVNULL, check=True, timeout=15,
    )
