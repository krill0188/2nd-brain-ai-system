#!/usr/bin/env python3
"""Re-pin publication baselines to the live drone-wiki-web snapshot after a snapshot replacement.

Run from ~/2nd:  .venv/bin/python scripts/rebaseline-publication.py [--apply]

Updates publication/policy.json (baseline.files/web_head, drops candidate_retirements whose path is
already gone from the live snapshot) and publication/publication-manifest.json (baseline.commit).
Refuses unless data/wiki is clean, equals the last commit touching it, and that commit is pushed.
Default is dry-run. Never deploys, never touches Git.
"""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POLICY = ROOT / 'publication/policy.json'
MANIFEST = ROOT / 'publication/publication-manifest.json'
WEB = Path.home() / 'projectm/drone-wiki-web'
SNAP = WEB / 'data/wiki'


def git(*args):
    r = subprocess.run(['git', '-C', str(WEB), *args], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f'git {args[0]} failed: {r.stderr.strip()}')
    return r.stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    if git('status', '--porcelain', '--', 'data/wiki'):
        raise SystemExit('data/wiki has uncommitted changes; refusing')
    commit = git('log', '-1', '--format=%H', '--', 'data/wiki')
    if subprocess.run(['git', '-C', str(WEB), 'merge-base', '--is-ancestor', commit, 'origin/main']).returncode:
        raise SystemExit(f'{commit[:7]} is not pushed to origin/main; refusing')

    files = {}
    for p in sorted(SNAP.rglob('*')):
        if p.is_symlink():
            raise SystemExit(f'symlink in snapshot: {p}')
        if p.is_file():
            files[p.relative_to(SNAP).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()

    policy = json.loads(POLICY.read_text())
    manifest = json.loads(MANIFEST.read_text())
    old = policy['baseline']['files']
    retired_done = [n for n in policy.get('candidate_retirements', {}) if n not in files]
    retired_live = [n for n in policy.get('candidate_retirements', {}) if n in files]

    print(f'snapshot commit : {commit}')
    print(f'baseline files  : {len(old)} -> {len(files)}')
    print(f'new/changed/gone: {len([n for n in files if n not in old])}/'
          f'{len([n for n in files if n in old and files[n] != old[n]])}/{len([n for n in old if n not in files])}')
    print(f'retirements     : drop {retired_done} (already gone), keep {retired_live}')
    if not args.apply:
        print('dry-run; pass --apply to write policy.json and publication-manifest.json')
        return 0

    policy['baseline']['files'] = files
    policy['baseline']['web_head'] = commit[:7]
    policy['candidate_retirements'] = {n: r for n, r in policy['candidate_retirements'].items() if n in files}
    manifest['baseline']['commit'] = commit
    POLICY.write_text(json.dumps(policy, ensure_ascii=False, indent=2) + '\n')
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print('rebaselined')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
