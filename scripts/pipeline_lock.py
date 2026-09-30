"""Shared nonblocking writer lock; inherited descriptors support nested entry points."""
import contextlib
import fcntl
import os
from pathlib import Path

LOCK_PATH = Path(__file__).resolve().parent.parent / '.ua/knowledge-pipeline.lock'
FD_ENV = 'KNOWLEDGE_PIPELINE_LOCK_FD'


def inherited_lock_fd():
    try:
        fd = int(os.environ.get(FD_ENV, '-1'))
        actual, expected = os.fstat(fd), LOCK_PATH.stat()
        if (actual.st_dev, actual.st_ino) != (expected.st_dev, expected.st_ino):
            return None
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return fd
    except (OSError, ValueError):
        return None


@contextlib.contextmanager
def shared_lock():
    inherited = inherited_lock_fd()
    if inherited is not None:
        yield inherited
        return
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    low = os.open(LOCK_PATH, os.O_CREAT | os.O_RDWR, 0o600)
    # Keep the lock above fd 3, which node children use for IPC.
    fd = fcntl.fcntl(low, fcntl.F_DUPFD, 10)
    os.close(low)
    previous = os.environ.get(FD_ENV)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        os.set_inheritable(fd, True)
        os.environ[FD_ENV] = str(fd)
        yield fd
    finally:
        if previous is None:
            os.environ.pop(FD_ENV, None)
        else:
            os.environ[FD_ENV] = previous
        os.close(fd)


def run_locked(main):
    try:
        with shared_lock():
            return main()
    except BlockingIOError:
        print('BLOCKED: another knowledge writer is running')
        return 75
