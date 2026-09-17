#!/usr/bin/env python3
"""Execute a command under the shared writer lock, preserving its descriptor."""
import os
import sys
from pipeline_lock import inherited_lock_fd, run_locked

def main():
    args = sys.argv[1:]
    if args == ['--check-inherited']:
        return 0 if inherited_lock_fd() is not None else 1
    if args and args[0] == '--':
        args = args[1:]
    if not args:
        return 64
    def execute():
        os.execvp(args[0], args)
    return run_locked(execute)

if __name__ == '__main__':
    raise SystemExit(main())
