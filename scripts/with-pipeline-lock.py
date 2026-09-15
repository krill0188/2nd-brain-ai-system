#!/usr/bin/env python3
"""Acquire the shared knowledge-pipeline lock, then exec the given command.

Uses the same lock file and fcntl.flock() mechanism as knowledge-pipeline.py
so that legacy independent entry points (fetch-inbox.sh, daily-ingest-claude.sh,
dronewiki-self-update.sh, apply-kinetic-rules.py, extract-knowledge-graph.sh,
update-graph.sh, ai-control.sh run-ingest) cannot run concurrently with each
other or with a knowledge-pipeline.py run. Non-blocking: refuses immediately
rather than queuing, matching knowledge-pipeline.py's own behavior.

Usage: with-pipeline-lock.py -- <command> [args...]
Exit 75 (EX_TEMPFAIL) if the lock is held elsewhere; the wrapped command's own
exit code otherwise. The lock is held for the wrapped command's entire
lifetime because exec() preserves open file descriptors (O_CLOEXEC is
explicitly cleared below) - a child this command spawns inherits the same
locked fd.
"""
import fcntl
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK_PATH = ROOT / '.ua/knowledge-pipeline.lock'


def main() -> int:
    argv = sys.argv[1:]
    if argv and argv[0] == '--':
        argv = argv[1:]
    if not argv:
        print('usage: with-pipeline-lock.py -- <command> [args...]', file=sys.stderr)
        return 64

    LOCK_PATH.parent.mkdir(exist_ok=True)
    lock_fd = os.open(str(LOCK_PATH), os.O_CREAT | os.O_RDWR)
    # Ensure the fd survives exec() so the lock stays held for the child's lifetime.
    flags = fcntl.fcntl(lock_fd, fcntl.F_GETFD)
    fcntl.fcntl(lock_fd, fcntl.F_SETFD, flags & ~fcntl.FD_CLOEXEC)

    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print(f'BLOCKED: another pipeline entry point holds {LOCK_PATH}', file=sys.stderr)
        return 75

    os.execvp(argv[0], argv)  # replaces this process; lock fd stays open


if __name__ == '__main__':
    raise SystemExit(main())
