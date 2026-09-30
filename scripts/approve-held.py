#!/usr/bin/env python3
"""List publication-gate held files; with --apply approve exactly those by current sha256.

Run from ~/2nd:  .venv/bin/python scripts/approve-held.py [--apply]
Default is dry-run and prints every held path. Never deploys, never touches Git.
"""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POLICY = ROOT / 'publication/policy.json'


def audit() -> dict:
    with tempfile.NamedTemporaryFile(suffix='.json') as tmp:
        subprocess.run(
            [sys.executable, str(ROOT / 'scripts/publication-gate.py'), '--report', tmp.name],
            check=False, capture_output=True,
        )
        return json.load(open(tmp.name))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    report = audit()
    held = [f for f in report['files'] if f['action'] == 'hold']
    print(f"before: {report['counts']}")
    for f in held:
        print('  hold', f['path'])
    if not args.apply:
        print(f'dry-run: {len(held)} files; pass --apply to write publication/policy.json')
        return 0

    policy = json.loads(POLICY.read_text())
    for f in held:
        policy['approved_files'][f['path']] = f['source_sha256']
    POLICY.write_text(json.dumps(policy, ensure_ascii=False, indent=2) + '\n')
    print(f"approved {len(held)}; after: {audit()['counts']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
