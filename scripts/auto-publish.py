#!/usr/bin/env python3
"""Daily unattended publication: rebaseline -> gate -> judge -> approve -> manifest -> derived -> web -> deploy.

Run from launchd under the shared pipeline lock (default is a dry-run that changes nothing):
    python3 scripts/with-pipeline-lock.py -- .venv/bin/python scripts/auto-publish.py --apply

Exceptions (sensitive pattern, unexpected path, oversized batch, gate block) never publish: they create a
hash-pinned approval request under .ua/auto-publish/approvals/ and notify via Telegram. Approval is a
separate human action:  auto-publish.py --approve <id> --by <who>   (--reject <id>, --list).
A failed step restores the web snapshot and the live alias; the previous site stays up.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))
import auto_publish_lib as lib  # noqa: E402
from pipeline_lock import inherited_lock_fd  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
WEB = Path.home() / 'projectm/drone-wiki-web'
CANDIDATES = Path.home() / 'projectm/drone-wiki-publication-candidates'
NOTIFY = Path.home() / 'claudeclaw/scripts/notify.sh'
STATE = ROOT / '.ua/auto-publish'
APPROVALS = STATE / 'approvals'
POLICY = ROOT / 'publication/policy.json'
MANIFEST = ROOT / 'publication/publication-manifest.json'
PY = str(ROOT / '.venv/bin/python')
SITE = 'https://drone-wiki-web.vercel.app'
ALIAS = 'drone-wiki-web.vercel.app'
DEPLOY_URL = re.compile(r'https://drone-wiki-[a-z0-9]+-jon-kkm-s-projects\.vercel\.app')


class Abort(Exception):
    def __init__(self, stage: str, detail: str, code: int = 3):
        super().__init__(f'{stage}: {detail}')
        self.stage, self.detail, self.code = stage, detail, code


def default_run(cmd, cwd=None, timeout=1800):
    """Run a child process without allowing locale bytes to crash the publisher.

    rsync on macOS 13 may emit non-UTF-8 filename bytes in itemized output.
    Preserve file bytes on disk; only decode process diagnostics loss-tolerantly.
    C locale makes rsync's control/status output deterministic while the
    replacement decoder keeps the sync decision usable for unusual filenames.
    """
    fd = inherited_lock_fd()
    env = dict(os.environ)
    env.update({'LC_ALL': 'C', 'LANG': 'C'})
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=False, timeout=timeout,
                            env=env, pass_fds=(() if fd is None else (fd,)))
    return subprocess.CompletedProcess(
        result.args,
        result.returncode,
        (result.stdout or b'').decode('utf-8', errors='replace'),
        (result.stderr or b'').decode('utf-8', errors='replace'),
    )


def default_fetch(url: str, timeout: int = 30):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        return exc.code, b''
    except Exception:
        return 0, b''


def telegram_safe(text: str) -> str:
    return text.translate({ord('<'): '(', ord('>'): ')', ord('&'): '+', ord('%'): 'pct'})


@dataclass
class Ctx:
    apply: bool = False
    push: bool = True
    root: Path = ROOT
    web: Path = WEB
    candidates: Path = CANDIDATES
    state: Path = STATE
    run: Callable = default_run
    fetch: Callable = default_fetch
    notify: Callable[[str], None] = lambda msg: None
    now: Callable[[], float] = time.time
    sleep: Callable[[float], None] = time.sleep
    log: list = field(default_factory=list)

    def say(self, msg: str):
        line = f'[{datetime.now().strftime("%H:%M:%S")}] {msg}'
        self.log.append(line)
        print(line, flush=True)

    def git(self, *args, cwd=None, check=True):
        result = self.run(['git', '-C', str(cwd or self.root), *args], timeout=300)
        if check and result.returncode:
            raise Abort('git', f'{args[0]} failed: {result.stderr.strip()[:200]}')
        return result.stdout.strip()

    def script(self, name: str, *args, timeout=1800, ok=(0,)):
        result = self.run([PY, str(self.root / 'scripts' / name), *args], cwd=self.root, timeout=timeout)
        if result.returncode not in ok:
            raise Abort(name, (result.stderr or result.stdout).strip()[-300:])
        return result


# ---------------------------------------------------------------- approvals
def load_requests(state: Path) -> list[dict]:
    out = []
    for path in sorted((state / 'approvals').glob('*.json')) if (state / 'approvals').is_dir() else []:
        try:
            out.append(json.loads(path.read_text()))
        except (OSError, ValueError):
            continue
    return out


def save_request(state: Path, req: dict):
    (state / 'approvals').mkdir(parents=True, exist_ok=True)
    (state / 'approvals' / f"{req['id']}.json").write_text(json.dumps(req, ensure_ascii=False, indent=2) + '\n')


def decide(state: Path, req_id: str, verdict: str, by: str, now: float | None = None) -> str:
    if not re.fullmatch(r'[0-9a-f]{12}', req_id):
        return 'invalid-id'
    path = state / 'approvals' / f'{req_id}.json'
    if not path.is_file():
        return 'not-found'
    req = json.loads(path.read_text())
    if lib.request_state(req, now) != 'pending':
        return f'not-pending:{lib.request_state(req, now)}'
    req.update(status=verdict, decided_by=by, decided_at=now or time.time())
    save_request(state, req)
    return verdict


# ---------------------------------------------------------------- steps
def precommit_raw(ctx: Ctx):
    """Commit any untracked raw/ files before the publish pipeline starts.

    New raw files added by extract-knowledge-graph.py or ingest scripts
    sit untracked until this step.  If left untracked they leak into
    commit_paths' staged-set check and cause a mismatch abort.
    This step is idempotent: nothing to commit → no-op.
    """
    # Only auto-commit raw/ paths that are NOT in HARD_DENY_PREFIXES
    raw_untracked = [
        line[3:].strip().strip('"')
        for line in ctx.git('status', '--porcelain', '-u', '--', 'raw/').splitlines()
        if line.startswith('?? ')
    ]
    if not raw_untracked:
        return
    ctx.say(f'precommit_raw: {len(raw_untracked)} untracked raw file(s) → auto-commit')
    ctx.git('add', '--', 'raw/')
    ctx.git('commit', '-q', '-m',
            f'raw: auto-commit {len(raw_untracked)} untracked file(s) before publish\n\n'
            'Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>')


def preflight(ctx: Ctx):
    if ctx.git('status', '--porcelain', '--', 'publication/'):
        raise Abort('preflight', 'publication/ has uncommitted edits')
    if ctx.git('diff', '--cached', '--name-only'):
        raise Abort('preflight', 'something is staged in 2nd')
    if ctx.git('status', '--porcelain', '--', 'data/wiki', cwd=ctx.web):
        raise Abort('preflight', 'web data/wiki is dirty')
    ctx.git('fetch', 'origin', 'main', cwd=ctx.web)
    if ctx.git('rev-parse', 'HEAD', cwd=ctx.web) != ctx.git('rev-parse', 'origin/main', cwd=ctx.web):
        raise Abort('preflight', 'web HEAD differs from origin/main')


def snapshot_hashes(web: Path) -> dict:
    base = web / 'data/wiki'
    return {p.relative_to(base).as_posix(): lib.sha256_text(p.read_bytes())
            for p in sorted(base.rglob('*')) if p.is_file() and not p.is_symlink()}


def commit_paths(ctx: Ctx, paths: list[str], message: str):
    ctx.git('add', '--', *paths)
    staged = set(ctx.git('diff', '--cached', '--name-only').splitlines())
    unexpected = staged - set(paths)
    if unexpected or not staged:
        ctx.git('reset', '-q', '--', *paths, check=False)
        raise Abort('commit', f'staged set mismatch: unexpected={sorted(unexpected)[:3]} empty={not staged}')
    ctx.git('commit', '-q', '-m', f'{message}\n\nCo-Authored-By: Claude Code <noreply@anthropic.com>\n'
            'Claude-Session: https://claude.ai/code/session_01MdPu3bEdp9FFS6bUGvSFNG')


def gate_report(ctx: Ctx, policy_path: Path | None = None) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        report = Path(tmp) / 'r.json'
        args = ['--report', str(report)] + (['--policy', str(policy_path)] if policy_path else [])
        ctx.script('publication-gate.py', *args, ok=(0, 2))
        if not report.exists():
            raise Abort('gate', 'no report produced')
        return json.loads(report.read_text())


def rebaseline(ctx: Ctx) -> Path | None:
    """Apply (or in dry-run, simulate in a temp policy) the baseline re-pin; returns temp policy for dry-run."""
    if ctx.apply:
        ctx.script('rebaseline-publication.py', '--apply')
        if ctx.git('status', '--porcelain', '--', 'publication/'):
            commit_paths(ctx, ['publication/policy.json', 'publication/publication-manifest.json'],
                         'publication: rebaseline to web snapshot')
        return None
    ctx.script('rebaseline-publication.py')
    policy = json.loads((ctx.root / 'publication/policy.json').read_text())
    policy['baseline']['files'] = snapshot_hashes(ctx.web)
    tmp = Path(tempfile.mkdtemp()) / 'policy.json'
    tmp.write_text(json.dumps(policy))
    return tmp


def judge_holds(ctx: Ctx, report: dict) -> list[dict]:
    blocks = [r for r in report['files'] if r['action'] == 'block']
    if blocks:
        top = ', '.join(sorted({f"{r['reason']}" for r in blocks})[:4])
        raise Abort('gate', f'{len(blocks)} blocked rows ({top})', code=4)
    holds = [r for r in report['files'] if r['action'] == 'hold']
    requests = load_requests(ctx.state)
    pairs = lib.approved_pairs(requests, ctx.now())
    auto_ok, exceptions, lines = lib.decide_hold_rows(
        holds,
        lambda p: (ctx.root / p).read_bytes(),
        lambda p: (ctx.web / 'data/wiki' / p).read_bytes() if (ctx.web / 'data/wiki' / p).is_file() else None,
        pairs,
    )
    batch_reasons = lib.judge_batch(len(holds), lines)
    ctx.say(f'holds={len(holds)} lines={lines} exceptions={len(exceptions)} batch={batch_reasons}')
    if batch_reasons and lib.request_id([{'path': r['path'], 'sha256': r['source_sha256']} for r in holds]) \
            not in lib.approved_batch_ids(requests, ctx.now()):
        exceptions = [{'path': r['path'], 'sha256': r['source_sha256'], 'reasons': ['batch']} for r in holds]
    elif batch_reasons:
        batch_reasons = []
    if exceptions:
        raise_exception_request(ctx, exceptions, batch_reasons, requests)
    return auto_ok


def raise_exception_request(ctx: Ctx, items: list[dict], batch_reasons: list[str], requests: list[dict]):
    req = lib.new_request(items, batch_reasons, ctx.now())
    prior = next((r for r in requests if r['id'] == req['id']), None)
    state = lib.request_state(prior, ctx.now()) if prior else None
    if state in ('pending', 'rejected'):
        raise Abort('exception', f"request {req['id']} is {state}; keeping the live site", code=5)
    if ctx.apply:
        save_request(ctx.state, req)
        sample = '; '.join(f"{i['path']} [{','.join(i['reasons'])}]" for i in items[:5])
        ctx.notify(f"[2nd 자동발행] 예외 승인 필요 id={req['id']}\n{len(items)}건 {batch_reasons or ''}\n{sample}\n"
                   f"승인: /publish approve {req['id']}  거부: /publish reject {req['id']}\n20시간 내 무응답이면 오늘은 건너뜁니다.")
    raise Abort('exception', f"{len(items)} files need human approval (id {req['id']})", code=5)


def approve_and_commit(ctx: Ctx, rows: list[dict]):
    if not rows:
        return
    policy = json.loads((ctx.root / 'publication/policy.json').read_text())
    for row in rows:
        current = lib.sha256_text((ctx.root / row['path']).read_bytes())
        if current != row['source_sha256']:
            raise Abort('approve', f"{row['path']} changed after judgement (tampering or race)")
        policy['approved_files'][row['path']] = row['source_sha256']
    (ctx.root / 'publication/policy.json').write_text(json.dumps(policy, ensure_ascii=False, indent=2) + '\n')
    after = gate_report(ctx)
    if not after['ready']:
        ctx.git('checkout', '--', 'publication/policy.json')
        raise Abort('approve', f"gate not ready after approval: {after['counts']}")
    paths = [r['path'] for r in rows] + ['publication/policy.json']
    try:
        commit_paths(ctx, paths, f'publication: auto-approve {len(rows)} canonical files')
    except Abort:
        ctx.git('checkout', '--', 'publication/policy.json', check=False)
        raise


def approve_manifest(ctx: Ctx):
    ctx.script('approve-version-manifest.py', '--apply')
    if ctx.git('status', '--porcelain', '--', 'publication/publication-manifest.json'):
        commit_paths(ctx, ['publication/publication-manifest.json'], 'publication: register approved sources in the version manifest')


def refresh_derived(ctx: Ctx) -> Path:
    before = {p.name for p in ctx.candidates.iterdir()} if ctx.candidates.is_dir() else set()
    ctx.script('knowledge-pipeline.py', '--refresh-derived', '--candidate-root', str(ctx.candidates), timeout=3600)
    fresh = sorted(p for p in ctx.candidates.iterdir() if p.name not in before and p.is_dir())
    if not fresh:
        raise Abort('derived', 'no new candidate produced')
    candidate = fresh[-1]
    ctx.script('build-derived-candidate.py', '--candidate', str(candidate), '--verify-only')
    return candidate


def sync_web(ctx: Ctx, candidate: Path) -> int:
    target = f'{ctx.web}/data/wiki/'
    dry = ctx.run(['rsync', '-rcn', '--delete', '--itemize-changes', f'{candidate}/', target], timeout=600)
    if dry.returncode:
        raise Abort('sync', dry.stderr.strip()[:200])
    lines = [ln for ln in dry.stdout.splitlines() if ln.strip()]
    deleted = sum(1 for ln in lines if ln.startswith('*deleting'))
    changed = sum(1 for ln in lines if ln.startswith('>f'))
    problems = lib.web_sync_ok(deleted, changed)
    if problems == ['no-change']:
        raise Abort('sync', 'candidate identical to live snapshot; nothing to deploy', code=0)
    if problems:
        raise Abort('sync', ', '.join(problems))
    real = ctx.run(['rsync', '-rc', '--delete', f'{candidate}/', target], timeout=600)
    if real.returncode:
        raise Abort('sync', real.stderr.strip()[:200])
    return changed + deleted


def restore_web(ctx: Ctx):
    """Return the web working tree and HEAD to origin/main; only touches data/wiki and our own unpushed commit."""
    ctx.git('reset', '-q', '--soft', 'origin/main', cwd=ctx.web, check=False)
    ctx.git('restore', '--source=origin/main', '--staged', '--worktree', '--', 'data/wiki', cwd=ctx.web, check=False)
    ctx.git('clean', '-fdq', '--', 'data/wiki', cwd=ctx.web, check=False)


def alias_source(ctx: Ctx) -> str | None:
    out = ctx.run(['vercel', 'alias', 'ls'], cwd=ctx.web, timeout=120).stdout
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[1] == ALIAS and parts[0].endswith('.vercel.app'):
            return parts[0]
    return None


def live_verify(ctx: Ctx, prev_pages: int | None) -> tuple[list[str], int | None]:
    statuses = {}
    for path in ('/', '/wiki', '/news'):
        for attempt in range(4):
            code, _ = ctx.fetch(SITE + path)
            if code == 200:
                break
            ctx.sleep(15)
        statuses[path] = code
    code, body = ctx.fetch(SITE + '/api/pages')
    pages = None
    try:
        data = json.loads(body)
        pages = len(data) if isinstance(data, list) else None
    except (ValueError, TypeError):
        pass
    return lib.live_check_ok(statuses, pages, prev_pages), pages


def live_page_count(ctx: Ctx) -> int | None:
    _, body = ctx.fetch(SITE + '/api/pages')
    try:
        data = json.loads(body)
        return len(data) if isinstance(data, list) else None
    except (ValueError, TypeError):
        return None


def build_and_deploy(ctx: Ctx, changed: int) -> dict:
    prev_alias = alias_source(ctx)
    if not prev_alias:
        raise Abort('deploy', 'cannot determine current alias target; refusing to deploy without rollback')
    prev_pages = live_page_count(ctx)
    build = ctx.run(['npx', 'next', 'build'], cwd=ctx.web, timeout=2400)
    if build.returncode:
        raise Abort('build', (build.stderr or build.stdout).strip()[-300:])
    ctx.git('add', '-A', '--', 'data/wiki', cwd=ctx.web)
    ctx.git('commit', '-q', '-m', f'data: publish {datetime.now().date()} auto-publish ({changed} files)\n\n'
            'Co-Authored-By: Claude Code <noreply@anthropic.com>\n'
            'Claude-Session: https://claude.ai/code/session_01MdPu3bEdp9FFS6bUGvSFNG', cwd=ctx.web)
    deploy = ctx.run(['vercel', '--prod', '--yes'], cwd=ctx.web, timeout=2400)
    match = DEPLOY_URL.search(deploy.stdout + deploy.stderr)
    if deploy.returncode or not match:
        raise Abort('deploy', (deploy.stderr or deploy.stdout).strip()[-300:])
    new_url = match.group(0).removeprefix('https://')
    if alias_source(ctx) != new_url:
        ctx.run(['vercel', 'alias', 'set', new_url, ALIAS], cwd=ctx.web, timeout=300)
    problems, pages = live_verify(ctx, prev_pages)
    if problems:
        ctx.run(['vercel', 'alias', 'set', prev_alias, ALIAS], cwd=ctx.web, timeout=300)
        raise Abort('live-check', f"rolled alias back to {prev_alias}: {'; '.join(problems)}", code=6)
    return {'deployment': new_url, 'pages': pages, 'previous_pages': prev_pages, 'previous_alias': prev_alias}


def finish(ctx: Ctx, result: dict):
    if ctx.push:
        ctx.git('push', 'origin', 'main', cwd=ctx.web)
    if ctx.push:
        rebaseline(ctx)
        try:
            ctx.git('push', 'origin', ctx.git('branch', '--show-current') or 'master')
        except Abort as exc:
            result['warning'] = f'2nd push failed: {exc.detail}'


# ---------------------------------------------------------------- driver
def execute(ctx: Ctx) -> int:
    started = ctx.now()
    stage = 'start'
    web_dirty = False
    try:
        stage = 'preflight'
        precommit_raw(ctx)   # untracked raw/ 파일 먼저 커밋 (staged-set mismatch 방지)
        preflight(ctx)
        stage = 'rebaseline'
        temp_policy = rebaseline(ctx)
        stage = 'gate'
        report = gate_report(ctx, temp_policy)
        rows = judge_holds(ctx, report)
        ctx.say(f'auto-approvable holds: {len(rows)}')
        if not ctx.apply:
            ctx.say('dry-run complete: no files, commits, pushes or deploys were made')
            return 0
        stage = 'approve'
        approve_and_commit(ctx, rows)
        stage = 'manifest'
        approve_manifest(ctx)
        stage = 'derived'
        candidate = refresh_derived(ctx)
        stage = 'sync'
        web_dirty = True
        changed = sync_web(ctx, candidate)
        stage = 'deploy'
        result = build_and_deploy(ctx, changed)
        stage = 'finish'
        web_dirty = False
        finish(ctx, result)
        record(ctx, 'ok', result, started)
        ctx.notify(f"[2nd 자동발행] 배포 완료 {result['deployment']}\n페이지 {result['previous_pages']} -> {result['pages']}, 변경 {changed}건"
                   + (f"\n경고: {result['warning']}" if result.get('warning') else ''))
        return 0
    except Abort as exc:
        if web_dirty and exc.stage != 'finish':
            restore_web(ctx)
        status = 'noop' if exc.code == 0 else 'skipped' if exc.code == 5 else 'failed'
        record(ctx, status, {'stage': exc.stage, 'detail': exc.detail}, started)
        if status == 'failed' and ctx.apply:
            ctx.notify(f'[2nd 자동발행] 실패 단계={exc.stage}\n{exc.detail[:300]}\n기존 사이트는 유지됩니다.')
        ctx.say(f'{status}: {exc}')
        return exc.code
    except Exception as exc:  # noqa: BLE001
        if web_dirty:
            restore_web(ctx)
        record(ctx, 'crashed', {'stage': stage, 'detail': repr(exc)[:300]}, started)
        if ctx.apply:
            ctx.notify(f'[2nd 자동발행] 예기치 못한 오류 단계={stage}\n{repr(exc)[:300]}')
        raise


def record(ctx: Ctx, status: str, detail: dict, started: float):
    if not ctx.apply:
        return
    ctx.state.mkdir(parents=True, exist_ok=True)
    payload = {'status': status, 'started': started, 'finished': ctx.now(), **detail, 'log': ctx.log[-40:]}
    (ctx.state / 'last-run.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')


def deliver(message: str, runner=subprocess.run, notify_path: Path = NOTIFY, log_path: Path | None = None,
            attempts: int = 2, pause=time.sleep) -> bool:
    """Send via notify.sh, retry on failure, and record each attempt; never raises."""
    log_path = log_path or STATE / 'notify.log'
    if not notify_path.is_file():
        outcomes = ['notify.sh missing']
    else:
        outcomes = []
        for attempt in range(1, attempts + 1):
            try:
                done = runner(['bash', str(notify_path), telegram_safe(message)], capture_output=True, text=True, timeout=60)
                outcomes.append(f'attempt {attempt} rc={done.returncode} {(done.stderr or "").strip()[:200]}'.strip())
                if done.returncode == 0:
                    break
            except Exception as exc:
                outcomes.append(f'attempt {attempt} {type(exc).__name__}')
            if attempt < attempts:
                pause(5)
    sent = bool(outcomes) and outcomes[-1].startswith('attempt') and ' rc=0' in outcomes[-1]
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open('a', encoding='utf-8') as handle:
            handle.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {'SENT' if sent else 'FAILED'} "
                         f"{message.splitlines()[0][:80]!r} | {'; '.join(outcomes)}\n")
    except OSError:
        pass
    return sent


def telegram_notify(message: str):
    deliver(message)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--no-push', action='store_true')
    ap.add_argument('--approve')
    ap.add_argument('--reject')
    ap.add_argument('--by', default='cli')
    ap.add_argument('--list', action='store_true')
    args = ap.parse_args()

    if args.list:
        for req in load_requests(STATE):
            print(req['id'], lib.request_state(req), len(req['items']), req.get('batch_reasons'))
        return 0
    if args.approve or args.reject:
        verdict = decide(STATE, args.approve or args.reject, 'approved' if args.approve else 'rejected', args.by)
        print(verdict)
        return 0 if verdict in ('approved', 'rejected') else 1

    from pipeline_lock import run_locked
    ctx = Ctx(apply=args.apply, push=not args.no_push, notify=telegram_notify)
    return run_locked(lambda: execute(ctx))


if __name__ == '__main__':
    raise SystemExit(main())
