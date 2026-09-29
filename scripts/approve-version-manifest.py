#!/usr/bin/env python3
"""Register policy-approved source files in the version-gate manifest.

Run from ~/2nd:  .venv/bin/python scripts/approve-version-manifest.py [--apply]

Approves exactly what the policy gate approves (non-derived sources) at the current HEAD commit
and revokes exactly the policy gate's retire-from-candidate paths. Dry-run (default) verifies the
whole chain -- policy candidate, version candidate, reconcile -- in a temp dir without touching the
repo. Requires the approved files to be committed and unchanged. Never deploys, never pushes.
"""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'publication/publication-manifest.json'
WEB = Path.home() / 'projectm/drone-wiki-web'
PY = sys.executable


def run(*cmd, cwd=ROOT):
    return subprocess.run(list(cmd), cwd=cwd, capture_output=True, text=True)


def git(*args):
    result = run('git', *args)
    if result.returncode:
        raise SystemExit(f'git {args[0]} failed')
    return result.stdout.strip()


def audit(tmp: Path) -> dict:
    report = tmp / 'audit.json'
    run(PY, str(ROOT / 'scripts/publication-gate.py'), '--report', str(report))
    if not report.exists():
        raise SystemExit('audit failed')
    return json.loads(report.read_text())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    manifest = json.loads(MANIFEST.read_text())
    derived = set(manifest['derived_artifacts'])
    head = git('rev-parse', 'HEAD')

    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        report = audit(tmp)
        if not report['ready']:
            raise SystemExit(f"policy gate not ready: {report['counts']}")

        approved = sorted(r['path'] for r in report['files'] if r['action'] == 'approve')
        revoked = sorted(r['path'] for r in report['files'] if r['action'] == 'retire-from-candidate')
        if any(p in derived for p in approved):
            raise SystemExit('derived artifact in approvals; update publication-gate first')

        dirty = git('status', '--porcelain', '--', *approved).splitlines() if approved else []
        if dirty:
            raise SystemExit(f'{len(dirty)} approved files are uncommitted or modified; commit first')
        for path in approved:
            committed = git('rev-parse', f'HEAD:{path}')
            working = git('hash-object', '--', path)
            if committed != working:
                raise SystemExit(f'working bytes differ from HEAD: {path}')

        manifest['approved_source_versions'] = [{'path': p, 'source_commit': head} for p in approved]
        manifest['revoked_paths'] = revoked
        proposed = tmp / 'manifest.json'
        proposed.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

        stage = run(PY, str(ROOT / 'scripts/publication-gate.py'), '--stage', str(tmp / 'policy'))
        build = run(PY, str(ROOT / 'scripts/build-publication-snapshot.py'),
                    '--source-root', str(ROOT), '--baseline-repo', str(WEB), '--manifest', str(proposed),
                    '--output', str(tmp / 'version'), '--report', str(tmp / 'version-report.json'))
        if stage.returncode or build.returncode:
            raise SystemExit('candidate build failed; nothing written')
        final = run(PY, str(ROOT / 'scripts/reconcile-publication-candidates.py'),
                    '--policy-candidate', str(tmp / 'policy'), '--version-candidate', str(tmp / 'version'),
                    '--output', str(tmp / 'final'))
        print(f'approve {len(approved)} sources @ {head[:7]}, revoke {len(revoked)}')
        print('reconcile:', final.stdout.strip() or final.stderr.strip())
        if final.returncode:
            raise SystemExit('gates do not agree; manifest NOT written')

    if not args.apply:
        print('dry-run OK; pass --apply to write publication/publication-manifest.json')
        return 0
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print('manifest written; commit it, then run knowledge-pipeline.py --validate-existing')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
