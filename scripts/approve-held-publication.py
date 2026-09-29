#!/usr/bin/env python3
"""Approve currently held publication files by exact sha256 and retire a2z-longtail-dual entity.

Run from ~/2nd:  .venv/bin/python scripts/approve-held-publication.py [--apply]
Default is dry-run (prints counts only). Never deploys, never touches Git.
"""
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POLICY = ROOT / 'publication/policy.json'
RETIRE = 'entities/a2z-longtail-dual.md'
RETIRE_SNAPSHOT_SHA = '4b527f15231c8636c2325b7504620cd945622c903d70c1f28dcaa1caf9f8a5ce'
REPLACEMENT = 'concepts/a2z-longtail-dual.md'


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
    policy = json.loads(POLICY.read_text())
    held = [f for f in report['files'] if f['action'] == 'hold']
    for f in held:
        policy['approved_files'][f['path']] = f['source_sha256']
    policy['candidate_retirements'][RETIRE] = {
        'snapshot_sha256': RETIRE_SNAPSHOT_SHA,
        'replacement': REPLACEMENT,
        'replacement_sha256': hashlib.sha256((ROOT / REPLACEMENT).read_bytes()).hexdigest(),
        'reason': 'Reviewed canonical supersession: duplicate thin entity merged into detailed concept.',
    }
    print(f"before: {report['counts']}; will approve {len(held)} held files + 1 retirement")
    if not args.apply:
        print('dry-run; pass --apply to write publication/policy.json')
        return 0
    POLICY.write_text(json.dumps(policy, ensure_ascii=False, indent=2) + '\n')
    print(f"after: {audit()['counts']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
