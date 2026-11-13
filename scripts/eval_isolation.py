"""Linux mount and process isolation for one synthetic evaluation workspace."""

from contextlib import contextmanager
import ctypes
import errno
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


WORKSPACE = "/workspace"
SCRATCH_BYTES = 8 * 1024 * 1024
ADDRESS_SPACE_BYTES = 256 * 1024 * 1024
OFFLINE_BOOTSTRAP = """
import os
import resource
import sys

for kind, ceiling in (
    (resource.RLIMIT_AS, int(sys.argv[1])),
    (resource.RLIMIT_FSIZE, 65536),
    (resource.RLIMIT_CPU, 8),
    (resource.RLIMIT_CORE, 0),
    (resource.RLIMIT_NOFILE, 128),
):
    soft, hard = resource.getrlimit(kind)
    hard = ceiling if hard == resource.RLIM_INFINITY else min(hard, ceiling)
    soft = hard if soft == resource.RLIM_INFINITY else min(soft, hard)
    resource.setrlimit(kind, (soft, hard))
os.execvp(sys.argv[2], sys.argv[2:])
"""


def has_direct_path(path):
    """Reject symlinks anywhere in a candidate path, including loops."""
    try:
        return not path.is_symlink() and path.resolve() == path
    except (OSError, RuntimeError):
        return False


def command(workspace, tools, argv, *, read_only=False, seccomp_fd=None):
    """Build a fresh sandbox with a private home and explicitly selected tools."""
    bwrap = shutil.which("bwrap")
    if not bwrap or not Path("/usr/bin/python3").is_file():
        raise RuntimeError("isolated evaluations require Linux Bubblewrap and /usr/bin/python3")
    args = [
        bwrap, "--unshare-user", "--unshare-pid", "--unshare-ipc", "--unshare-uts",
        "--die-with-parent", "--new-session", "--clearenv", "--proc", "/proc",
        "--dir", "/home/eval/.codex",
        "--setenv", "HOME", "/home/eval", "--setenv", "CODEX_HOME", "/home/eval/.codex",
        "--setenv", "PATH", "/tools:/usr/bin:/bin", "--setenv", "LANG", "C.UTF-8",
        "--setenv", "SHELL", "/bin/bash",
        "--setenv", "OPENSPEC_TELEMETRY", "0", "--setenv", "GIT_CONFIG_NOSYSTEM", "1",
    ]
    if seccomp_fd is None:
        args.extend(("--dev", "/dev"))
    else:
        args.extend(("--dir", "/dev"))
        for device in ("/dev/null", "/dev/zero", "/dev/random", "/dev/urandom"):
            args.extend(("--dev-bind", device, device))
        args.extend(("--size", str(SCRATCH_BYTES)))
    args.extend(("--tmpfs", "/tmp"))
    for path in ("/usr/bin", "/usr/lib", "/usr/lib64", "/bin", "/lib", "/lib64",
                 "/etc/ssl/certs", "/etc/hosts", "/etc/resolv.conf", "/etc/nsswitch.conf"):
        if Path(path).is_symlink() and path in ("/bin", "/lib", "/lib64"):
            args.extend(("--symlink", os.readlink(path), path))
        elif Path(path).exists():
            args.extend(("--ro-bind", path, path))
    for name, path in tools.items():
        args.extend(("--ro-bind", str(path), f"/tools/{name}"))
    bind = "--ro-bind" if read_only else "--bind"
    args.extend((bind, str(workspace), WORKSPACE))
    if seccomp_fd is not None:
        args.extend(("--remount-ro", "/", "--remount-ro", "/proc",
                     "--seccomp", str(seccomp_fd)))
    return [*args, "--chdir", WORKSPACE, "--", *argv]


@contextmanager
def offline_command(workspace, argv):
    """Apply the limits before executing fixture code or inspecting its Git state."""
    try:
        library = ctypes.CDLL("libseccomp.so.2")
    except OSError as exc:
        raise RuntimeError("offline grading requires libseccomp.so.2") from exc
    library.seccomp_init.argtypes = [ctypes.c_uint32]
    library.seccomp_init.restype = ctypes.c_void_p
    library.seccomp_syscall_resolve_name.argtypes = [ctypes.c_char_p]
    library.seccomp_syscall_resolve_name.restype = ctypes.c_int
    library.seccomp_rule_add.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.c_uint]
    library.seccomp_export_bpf.argtypes = [ctypes.c_void_p, ctypes.c_int]
    library.seccomp_release.argtypes = [ctypes.c_void_p]

    allow = 0x7FFF0000
    deny = 0x00050000 | errno.EPERM
    policy = library.seccomp_init(allow)
    if not policy:
        raise RuntimeError("could not initialize the offline grading policy")
    try:
        for name in (b"socket", b"socketpair", b"io_uring_setup",
                     b"clone", b"clone3", b"fork", b"vfork",
                     b"memfd_create", b"shmget", b"semget", b"msgget"):
            call = library.seccomp_syscall_resolve_name(name)
            # Some architectures have no separate fork or vfork syscall.
            if call < 0 and name in (b"fork", b"vfork"):
                continue
            if call < 0 or library.seccomp_rule_add(policy, deny, call, 0) != 0:
                raise RuntimeError(f"could not deny {name.decode()} in offline grading")
        with tempfile.TemporaryFile() as rules:
            fd = rules.fileno()
            if library.seccomp_export_bpf(policy, fd) != 0:
                raise RuntimeError("could not export the offline grading policy")
            rules.seek(0)
            limited = ["/usr/bin/python3", "-I", "-B", "-c", OFFLINE_BOOTSTRAP,
                       str(ADDRESS_SPACE_BYTES), *argv]
            yield command(workspace, {}, limited, read_only=True, seccomp_fd=fd), (fd,)
    finally:
        library.seccomp_release(policy)


def probe_offline(workspace, protected_path, positive_file):
    """Verify file, network and resource controls without stressing the host."""
    source = """
import errno
import mmap
import os
from pathlib import Path
import resource
import socket
import sys

assert (Path('/workspace') / sys.argv[2]).is_file()
assert not Path(sys.argv[1]).exists()
try:
    Path('/workspace/should-not-exist').write_text('failed')
except OSError as exc:
    assert exc.errno == errno.EROFS
else:
    raise AssertionError('grader workspace was writable')
for family in (socket.AF_INET, socket.AF_INET6, socket.AF_UNIX):
    try:
        socket.socket(family, socket.SOCK_STREAM).close()
    except PermissionError:
        pass
    else:
        raise AssertionError(f'socket creation succeeded for {family}')
try:
    child = os.fork()
except PermissionError:
    pass
else:
    if child == 0:
        os._exit(0)
    os.waitpid(child, 0)
    raise AssertionError('grader created a child process')
ceiling = int(sys.argv[3])
assert 0 < resource.getrlimit(resource.RLIMIT_AS)[1] <= ceiling
try:
    mmap.mmap(-1, ceiling + 4096).close()
except OSError as exc:
    assert exc.errno == errno.ENOMEM
else:
    raise AssertionError('grader exceeded its address-space limit')
scratch = os.statvfs('/tmp')
assert 0 < scratch.f_frsize * scratch.f_blocks <= int(sys.argv[4])
for mount in ('/', '/dev', '/proc', '/workspace'):
    assert os.statvfs(mount).f_flag & os.ST_RDONLY, mount
Path('/tmp/grader-probe').write_text('ok')
assert Path('/tmp/grader-probe').read_text() == 'ok'
"""
    if not protected_path.is_file():
        raise RuntimeError(f"missing offline isolation control: {protected_path}")
    argv = ["/usr/bin/python3", "-I", "-c", source, str(protected_path), positive_file,
            str(ADDRESS_SPACE_BYTES), str(SCRATCH_BYTES)]
    with offline_command(workspace, argv) as (sandbox, fds):
        subprocess.run(sandbox, pass_fds=fds, stdin=subprocess.DEVNULL, check=True, timeout=15)


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
