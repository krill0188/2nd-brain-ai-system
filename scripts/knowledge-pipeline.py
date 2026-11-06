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
import time
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
        ('Generate:self-update-canonical', [shutil.which('node') or '/usr/local/bin/node', '--import', 'tsx', str(WEB / 'scripts/self-update-pipeline.ts'), '--apply']),
        ('Generate:kinetic-apply', [py, str(ROOT / 'scripts/apply-kinetic-rules.py'), '--no-notify']),
        ('Validate:canonical-lint-before-generation', ['python3', str(ROOT / 'scripts/lint-knowledge.py'), '--full']),
        ('Generate:embeddings', [py, str(ROOT / 'scripts/embed-docs.py'), '--if-stale']),
        ('Generate:discovery', ['bash', str(ROOT / 'scripts/extract-knowledge-graph.sh'), '--limit', '10']),
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
        ('Publish:derived-projection', [
            py,
            str(ROOT / 'scripts/build-derived-candidate.py'),
            '--candidate',
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


NOTIFY = Path.home() / 'claudeclaw/scripts/notify.sh'


def notify_telegram(message: str) -> None:
    if NOTIFY.is_file():
        try:
            subprocess.run(['bash', str(NOTIFY), message], capture_output=True, timeout=60)
        except (OSError, subprocess.TimeoutExpired):
            pass


def ensure_web_dependencies(execute=subprocess.run, notify=notify_telegram) -> list[dict]:
    # A lost node_modules once surfaced as a masked exit 124 for ten days.
    if (WEB / 'node_modules/tsx/package.json').exists():
        return []
    dir_present = (WEB / 'node_modules').is_dir()
    npm = shutil.which('npm') or '/usr/local/bin/npm'
    try:
        result = execute(
            [npm, 'ci', '--no-audit', '--no-fund'],
            cwd=WEB,
            capture_output=True,
            timeout=900,
        )
        code = result.returncode
    except (OSError, subprocess.TimeoutExpired):
        code = 127
    ok = code == 0
    record = {'step': 'Prepare:web-dependencies', 'exit_code': code,
              'diagnostic': 'DEPENDENCIES_RESTORED' if ok else 'DEPENDENCY_RESTORE_FAILED',
              'node_modules_dir_present': dir_present}
    notify('[2nd 파이프라인] drone-wiki-web 의존성(tsx) 유실 감지 - '
           + ('npm ci로 자동 복구했습니다.' if ok else '자동 복구 실패, 확인이 필요합니다.')
           + f' node_modules 폴더 {"있었음(일부 유실)" if dir_present else "없었음(전체 유실)"}')
    return [record]


def output_text(result) -> str:
    out = getattr(result, 'stdout', b'') or b''
    return out.decode('utf-8', errors='replace') if isinstance(out, bytes) else str(out)


DISCOVERY_STEP = 'Generate:discovery'
DISCOVERY_DRAIN_BUDGET_SEC = 20 * 60  # 추출 소진 루프 전용 벽시계 예산(파생물 갱신 전체 3600초와 별개)
PENDING_RE = re.compile(r'남은 미처리 (\d+)개')


def remaining_pending(output: str) -> int | None:
    """extract-knowledge-graph.py 출력에서 남은 미처리 문서 수. 알 수 없으면 None."""
    if '처리할 것이 없습니다' in output:
        return 0
    m = PENDING_RE.search(output)
    return int(m.group(1)) if m else None


def drain_discovery(run, first_output: str, budget_sec: float = DISCOVERY_DRAIN_BUDGET_SEC, clock=time.monotonic) -> dict:
    """대기 문서가 0이 될 때까지 추출을 반복한다. run() -> (exit_code, output).

    한 번에 --limit 건만 처리하므로 신규 문서가 많으면 대기가 남는다. 예산 소진·실패·진척 없음이면 멈추고 남은 건수를 돌려준다.
    """
    started = clock()
    pending = remaining_pending(first_output)
    rounds = 1
    stopped = 'DONE'
    while pending:
        if clock() - started >= budget_sec:
            stopped = 'BUDGET_EXHAUSTED'
            break
        code, output = run()
        rounds += 1
        now = remaining_pending(output)
        if code != 0 or now is None:
            stopped = 'EXTRACTION_FAILED'
            break
        if now >= pending:
            stopped = 'NO_PROGRESS'
            pending = now
            break
        pending = now
    return {'rounds': rounds, 'remaining': pending if pending is not None else -1, 'stopped': stopped}


def run_steps(items, execute=subprocess.run) -> list[dict]:
    results = []
    for name, command in items:
        fd = inherited_lock_fd()
        try:
            result = execute(
                command,
                cwd=WEB,
                capture_output=True,
                timeout=7200,
                pass_fds=(() if fd is None else (fd,)),
            )
        except subprocess.TimeoutExpired:
            results.append({'step': name, 'exit_code': 124, 'diagnostic': 'STEP_TIMEOUT'})
            break
        except OSError as exc:
            results.append({
                'step': name,
                'exit_code': 127,
                'diagnostic': 'EXECUTABLE_MISSING' if isinstance(exc, FileNotFoundError) else 'STEP_LAUNCH_FAILED',
            })
            break

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
        if name == DISCOVERY_STEP and not result.returncode:
            def run_again(command=command, fd=fd):
                r = execute(command, cwd=WEB, capture_output=True, timeout=1800, pass_fds=(() if fd is None else (fd,)))
                return r.returncode, output_text(r)
            first = output_text(result)
            drained = drain_discovery(run_again, first)
            record.update(drain_rounds=drained['rounds'], drain_remaining=drained['remaining'], drain_stopped=drained['stopped'])
            if drained['remaining']:
                record['diagnostic'] = 'DISCOVERY_BACKLOG_REMAINING'
        if result.returncode:
            # 문서 추출은 일부 문서가 실패해도 성공분이 저장되고 다음 밤에 재시도되므로 후속 단계(그래프·검증)를 막지 않는다.
            if name == 'Generate:discovery':
                record['diagnostic'] = 'PARTIAL_EXTRACTION_CONTINUE'
                continue
            break

    return results


LEGACY_LABELS = ('daily-fetch', 'daily-ingest', 'dronewiki-self-update', 'lint-knowledge',
                 'extract-knowledge-graph', 'update-knowledge-graph', 'apply-kinetic-rules', 'sync-dronewiki')


def shares_pipeline_lock(label: str, launch_agents: Path | None = None) -> bool:
    """launchd 작업의 plist 가 with-pipeline-lock.py 래퍼로 실행하는가(=이 파이프라인과 같은 락을 공유).

    아래 가드는 '락을 쓰지 않는 옛 독립 생성기'를 막으려는 것이다(새 락만으로는 그 작업들을 조율할 수 없다). 11/5 부터 daily-fetch·daily-ingest 가
    락 래퍼로 실행되도록 바뀌어 이 조건이 해소됐으므로, 래퍼를 쓰는 작업은 겹침으로 보지 않는다(daily-fetch 는 hermes-wrap.sh 의 명령 문자열 안에 래퍼가 있다). plist 를 읽을 수 없거나 형식이 이상하면 False(막는 쪽).
    """
    import plistlib
    path = (launch_agents or Path.home() / 'Library/LaunchAgents') / f'ai.2nd.{label}.plist'
    try:
        with path.open('rb') as fh:
            args = plistlib.load(fh).get('ProgramArguments') or []
    except (OSError, ValueError, plistlib.InvalidFileException):
        return False
    # 인자 자체가 래퍼이거나(…/with-pipeline-lock.py), hermes-wrap.sh 처럼 명령 문자열을 bash -c 로 넘기는 형태("python3 …/with-pipeline-lock.py -- bash …")
    return any(isinstance(a, str) and re.search(r'(^|[\s/])with-pipeline-lock\.py(\s|$)', a) is not None for a in args)


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
    for label in LEGACY_LABELS:
        state = subprocess.run(['launchctl', 'list', 'ai.2nd.' + label], capture_output=True, text=True)
        if state.returncode == 0 and (not args.validate_existing or re.search(r'"PID"\s*=\s*\d+', state.stdout)):
            if shares_pipeline_lock(label):
                continue  # 이 파이프라인과 같은 락(with-pipeline-lock.py)으로 직렬화되는 작업은 동시 쓰기 충돌이 없다
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

            prepared = ensure_web_dependencies() if initial else []
            if any(r['exit_code'] for r in prepared):
                initial = []
            results = prepared + (run_steps(initial) if initial else [])
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
                        'Publish:derived-projection',
                    ],
                )
                results += run_steps(publication)

                if any(r['step'] == 'Publish:derived-projection' and r['exit_code'] for r in results) and candidate.exists():
                    shutil.rmtree(candidate)

                if source_fingerprint() != before:
                    results.append({
                        'step': 'Validate:source-stability-after-stage',
                        'exit_code': 2,
                    })
                    if candidate.exists():
                        shutil.rmtree(candidate)
        except (OSError, subprocess.TimeoutExpired) as exc:
            results.append({
                'step': 'execution-error',
                'exit_code': 124,
                'diagnostic': type(exc).__name__,
                'errno': getattr(exc, 'errno', None),
                'path': Path(str(getattr(exc, 'filename', '') or '')).name or None,
            })
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
