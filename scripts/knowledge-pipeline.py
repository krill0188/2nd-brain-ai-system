#!/usr/bin/env python3
"""Sequential local pipeline candidate. Default is plan-only; never deploys.

Install schedule only after retiring overlapping legacy calendar triggers together.
--run-local invokes existing generation tools and therefore is intentionally opt-in.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import uuid
from pipeline_lock import shared_lock, inherited_lock_fd
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = Path.home() / 'projectm/drone-wiki-web'


def source_fingerprint() -> str:
    h = hashlib.sha256()
    for layer in ('concepts', 'entities', 'comparisons', 'queries', 'raw', 'ontology'):
        for p in sorted((ROOT / layer).rglob('*')):
            if p.is_file() and not p.is_symlink() and p.suffix in ('.md', '.json'):
                h.update(str(p.relative_to(ROOT)).encode())
                h.update(p.read_bytes())
    for name in (
        '.ua/news-feed.json',
        'publication/policy.json',
        'publication/publication-manifest.json',
    ):
        p = ROOT / name
        if p.exists():
            h.update(name.encode())
            h.update(p.read_bytes())
    return h.hexdigest()


def publication_paths(candidate: Path) -> tuple[Path, Path, Path]:
    return (
        candidate.with_name(candidate.name + '.policy'),
        candidate.with_name(candidate.name + '.version'),
        candidate.with_name(candidate.name + '.version-report.json'),
    )


def steps(candidate: Path) -> list[tuple[str, list[str]]]:
    py = str(ROOT / '.venv/bin/python')
    policy_candidate, version_candidate, version_report = publication_paths(candidate)
    return [
        ('Generate:fetch', ['bash', str(ROOT / 'scripts/fetch-inbox.sh')]),
        ('Generate:ingest', ['bash', str(ROOT / 'scripts/daily-ingest-claude.sh')]),
        ('Generate:self-update-canonical', [str(WEB / 'node_modules/.bin/tsx'), str(WEB / 'scripts/self-update-pipeline.ts'), '--apply']),
        ('Generate:kinetic-apply', [py, str(ROOT / 'scripts/apply-kinetic-rules.py'), '--no-notify']),
        ('Validate:canonical-lint-before-generation', ['python3', str(ROOT / 'scripts/lint-knowledge.py'), '--full']),
        ('Generate:embeddings', [py, str(ROOT / 'scripts/embed-docs.py'), '--if-stale']),
        ('Generate:discovery', ['bash', str(ROOT / 'scripts/extract-knowledge-graph.sh'), '--limit', '15']),
        ('Generate:canonical-graph', ['bash', str(ROOT / 'scripts/update-graph.sh')]),
        ('Validate:all', ['python3', str(ROOT / 'scripts/publication-preflight.py')]),
        ('Publish:policy-candidate', [
            py,
            str(ROOT / 'scripts/publication-gate.py'),
            '--stage',
            str(policy_candidate),
        ]),
        ('Publish:version-candidate', [
            py,
            str(ROOT / 'scripts/build-publication-snapshot.py'),
            '--source-root',
            str(ROOT),
            '--baseline-repo',
            str(WEB),
            '--output',
            str(version_candidate),
            '--report',
            str(version_report),
        ]),
        ('Publish:reconcile-candidates', [
            py,
            str(ROOT / 'scripts/reconcile-publication-candidates.py'),
            '--policy-candidate',
            str(policy_candidate),
            '--version-candidate',
            str(version_candidate),
            '--output',
            str(candidate),
        ]),
    ]


def select_steps(plan, names):
    wanted = set(names)
    selected = [item for item in plan if item[0] in wanted]
    found = {name for name, _ in selected}
    missing = wanted - found
    if missing:
        raise ValueError(f'missing pipeline steps: {sorted(missing)}')
    return selected


def run_steps(items, execute=subprocess.run) -> list[dict]:
    results = []
    for name, command in items:
        fd = inherited_lock_fd()
        result = execute(
            command,
            cwd=WEB,
            capture_output=True,
            timeout=7200,
            pass_fds=(() if fd is None else (fd,)),
        )

        record = {'step': name, 'exit_code': result.returncode}

        if result.returncode:
            # Persist only fixed diagnostics; never source/provider output.
            output = (
                (getattr(result, 'stdout', b'') or b'')
                + (getattr(result, 'stderr', b'') or b'')
            )
            if isinstance(output, bytes):
                output = output.decode('utf-8', errors='replace')

            known = (
                'MODEL_LOAD_FAILED',
                'MODEL_CACHE_UNAVAILABLE',
                'MODEL_COMPUTE_FAILED',
                'INPUT_CHANGED',
                'INVALID_VECTORS',
                'MISSING_VECTORS',
            )
            record['diagnostic'] = next(
                (code for code in known if code in output),
                'STEP_FAILED',
            )

            if name == 'Validate:all':
                try:
                    validation = json.loads(output)
                    allowed = {
                        'canonical-lint',
                        'kinetic-static-check',
                        'embeddings-freshness',
                        'graph-coverage',
                        'publication-policy',
                    }
                    failed = [
                        row['step']
                        for row in validation['steps']
                        if row['step'] in allowed and row['exit_code'] != 0
                    ]
                    record['failed_checks'] = failed
                    if failed == ['publication-policy']:
                        record['diagnostic'] = 'PUBLICATION_REVIEW_REQUIRED'
                except (ValueError, KeyError, TypeError):
                    pass

        results.append(record)
        if result.returncode:
            break

    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-local', action='store_true')
    parser.add_argument('--validate-existing', action='store_true', help='Validate current source and stage only; no generation or messages')
    parser.add_argument('--refresh-derived', action='store_true', help='Refresh derived artifacts from current source; skip fetch/ingest/self-update and notifications')

    target = parser.add_mutually_exclusive_group()
    target.add_argument('--candidate', type=Path)
    target.add_argument('--candidate-root', type=Path, help='Create a unique child for each run; retain previous final candidates')

    args = parser.parse_args()

    candidate = args.candidate or (
        args.candidate_root
        / (
            datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ-')
            + uuid.uuid4().hex[:12]
        )
        if args.candidate_root
        else Path('/tmp/dronewiki-reviewed-candidate')
    )

    plan = steps(candidate)

    if sum((args.run_local, args.validate_existing, args.refresh_derived)) > 1:
        parser.error('choose one execution mode')

    if not args.run_local and not args.validate_existing and not args.refresh_derived:
        print(json.dumps({'steps': [name for name, _ in plan], 'Deploy': 'manual approval required',
                          'Report': 'local .ua/pipeline-result.json; no messages',
                          'activation': 'NOT ACTIVE; replace overlapping launchd triggers before running'}, indent=2))
        return 0
    # Fail closed while legacy independent generators are installed. A new lock alone
    # cannot coordinate old jobs that do not share that lock.
    labels = ('daily-fetch', 'daily-ingest', 'dronewiki-self-update', 'lint-knowledge',
              'extract-knowledge-graph', 'update-knowledge-graph', 'apply-kinetic-rules', 'sync-dronewiki')
    for label in labels:
        state = subprocess.run(['launchctl', 'list', 'ai.2nd.' + label], capture_output=True, text=True)
        if state.returncode == 0 and (not args.validate_existing or re.search(r'"PID"\s*=\s*\d+', state.stdout)):
            print('BLOCKED: overlapping legacy launchd jobs remain loaded; schedule migration required')
            return 2
    if not (args.candidate or args.candidate_root) or candidate.exists() or any(
        candidate.resolve().is_relative_to(p.resolve())
        or p.resolve().is_relative_to(candidate.resolve())
        for p in (ROOT, WEB)
    ):
        print('BLOCKED: provide a new isolated --candidate directory')
        return 2

    policy_candidate, version_candidate, version_report = publication_paths(candidate)
    if any(path.exists() for path in (policy_candidate, version_candidate, version_report)):
        print('BLOCKED: publication intermediate path already exists')
        return 2
    (ROOT / '.ua').mkdir(exist_ok=True)
    with shared_lock():
        results = []
        try:
            # Freeze publication-relevant source after the initial canonical lint.
            if args.validate_existing:
                initial = []
            elif args.refresh_derived:
                initial = select_steps(
                    plan,
                    ['Validate:canonical-lint-before-generation'],
                )
            else:
                initial = select_steps(
                    plan,
                    [
                        'Generate:fetch',
                        'Generate:ingest',
                        'Generate:self-update-canonical',
                        'Generate:kinetic-apply',
                        'Validate:canonical-lint-before-generation',
                    ],
                )

            results = run_steps(initial) if initial else []
            before = source_fingerprint()

            if all(r['exit_code'] == 0 for r in results):
                if args.validate_existing:
                    middle = select_steps(plan, ['Validate:all'])
                else:
                    middle = select_steps(
                        plan,
                        [
                            'Generate:embeddings',
                            'Generate:discovery',
                            'Generate:canonical-graph',
                            'Validate:all',
                        ],
                    )
                results += run_steps(middle)

            if source_fingerprint() != before:
                results.append({
                    'step': 'Validate:source-stability',
                    'exit_code': 2,
                })

            if all(r['exit_code'] == 0 for r in results):
                publication = select_steps(
                    plan,
                    [
                        'Publish:policy-candidate',
                        'Publish:version-candidate',
                        'Publish:reconcile-candidates',
                    ],
                )
                results += run_steps(publication)

                if source_fingerprint() != before:
                    results.append({
                        'step': 'Validate:source-stability-after-stage',
                        'exit_code': 2,
                    })
                    if candidate.exists():
                        shutil.rmtree(candidate)
        except (OSError, subprocess.TimeoutExpired):
            results.append({'step': 'execution-error', 'exit_code': 124})
        finally:
            for path in (policy_candidate, version_candidate):
                if path.exists():
                    shutil.rmtree(path)
            if version_report.exists():
                version_report.unlink()

        report = {'at': datetime.now(timezone.utc).isoformat(), 'steps': results,
                  'mode': 'validate-existing' if args.validate_existing else 'generate-local',
                  'schedule_activation': 'NOT PERFORMED',
                  'deploy': 'NOT EXECUTED: approval required'}
        fd, tmp = tempfile.mkstemp(prefix='.pipeline-result-', dir=ROOT / '.ua')
        try:
            with os.fdopen(fd, 'w') as handle:
                json.dump(report, handle, indent=2)
            os.replace(tmp, ROOT / '.ua/pipeline-result.json')
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)
        print(json.dumps(report))
        return 0 if results and all(r['exit_code'] == 0 for r in results) else 2


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except BlockingIOError:
        print('BLOCKED: another knowledge writer is running')
        raise SystemExit(75)
