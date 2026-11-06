"""Pure decision logic for auto-publish.py: file judging, batch caps, hash-pinned exception approvals.

No subprocess, network or Git here, so every rule is unit-testable.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path

ALLOWED_PREFIXES = ('concepts/', 'entities/', 'raw/', 'comparisons/', 'queries/')
HARD_DENY_PREFIXES = ('research/', 'inbox/', 'innovations/', 'raw/career-quiz/', 'raw/papers/files/')
MAX_FILES = 100
MAX_CHANGED_LINES = 1500
MAX_FILE_BYTES = 200_000
MAX_WEB_DELETIONS = 5
APPROVAL_TTL_SECONDS = 20 * 3600     # 승인 대기 요청이 응답을 기다리는 시간(이후 만료, 다음 실행이 새 요청을 만든다)
DECISION_TTL_SECONDS = 48 * 3600     # 승인·거부 결정이 유효한 시간. 요청은 10:30 실행에서 생기고 다음 실행은 24시간 뒤라서, 결정 유효 시간이 20시간이면
                                     # 요청 직후 4시간 안에 승인한 건이 다음 실행 전에 만료되어 헛수고가 됐다(2026-11-06). 승인은 파일 해시에 고정되어 있어 길게 둬도 안전하다.

SENSITIVE_PATTERNS = {
    'local-path': re.compile(r'(?:/Users/[A-Za-z0-9._-]+|/home/[A-Za-z0-9._-]+|[A-Za-z]:\\Users\\)'),
    'api-key': re.compile(r'\b(?:sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|xox[abp]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_-]{30,})'),
    'bearer-token': re.compile(r'(?i)\bbearer\s+[A-Za-z0-9._-]{20,}'),
    'secret-assignment': re.compile(r'(?im)^\s*(?:api[_-]?key|secret|token|password|passwd)\s*[:=]\s*\S{8,}'),
    'private-key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
    'telegram-token': re.compile(r'\b\d{8,10}:[A-Za-z0-9_-]{35}\b'),
}
EMAIL_ALLOW = re.compile(r'@(?:example\.com|example\.org|users\.noreply\.github\.com)$', re.I)
DENY_META = {'private', 'internal', 'restricted', 'false', 'no', 'deny', 'draft'}
META_KEYS = ('visibility', 'publish', 'public', 'status')


def sha256_text(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def frontmatter(text: str) -> dict | None:
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---', 4)
    if end < 0:
        return None
    meta = {}
    for line in text[4:end].splitlines():
        if ':' in line and not line.startswith((' ', '\t', '-')):
            key, _, value = line.partition(':')
            meta[key.strip().lower()] = value.strip().strip('"\'')
    return meta


def judge_file(path: str, data: bytes) -> list[str]:
    """Return reasons the file must NOT be auto-approved (empty list = acceptable)."""
    reasons = []
    if '..' in Path(path).parts or path.startswith('/'):
        return ['path-escape']
    if path.startswith(HARD_DENY_PREFIXES):
        return ['hard-deny-dir']
    if not path.startswith(ALLOWED_PREFIXES):
        reasons.append('path-not-allowed')
    if not path.endswith('.md'):
        reasons.append('not-markdown')
    if len(data) > MAX_FILE_BYTES:
        reasons.append('file-too-large')
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        return reasons + ['not-utf8']
    meta = frontmatter(text)
    if meta is None:
        reasons.append('no-frontmatter')
    else:
        if not meta.get('title'):
            reasons.append('no-title')
        for key in META_KEYS:
            if meta.get(key, '').lower() in DENY_META:
                reasons.append(f'metadata-{key}-{meta[key].lower()}')
    for name, pattern in SENSITIVE_PATTERNS.items():
        for match in pattern.finditer(text):
            if name == 'email' and EMAIL_ALLOW.search(match.group(0)):
                continue
            reasons.append(f'sensitive-{name}')
            break
    return reasons


def count_changed_lines(old: bytes | None, new: bytes) -> int:
    new_lines = new.decode('utf-8', 'replace').splitlines()
    if old is None:
        return len(new_lines)
    old_lines = old.decode('utf-8', 'replace').splitlines()
    old_set = {}
    for line in old_lines:
        old_set[line] = old_set.get(line, 0) + 1
    added = 0
    for line in new_lines:
        if old_set.get(line, 0):
            old_set[line] -= 1
        else:
            added += 1
    removed = sum(old_set.values())
    return added + removed


def judge_batch(file_count: int, changed_lines: int) -> list[str]:
    reasons = []
    if file_count > MAX_FILES:
        reasons.append(f'batch-files>{MAX_FILES}')
    if changed_lines > MAX_CHANGED_LINES:
        reasons.append(f'batch-lines>{MAX_CHANGED_LINES}')
    return reasons


def request_id(items: list[dict]) -> str:
    """Stable id over (path, sha256) pairs: any content change yields a different request."""
    blob = json.dumps(sorted((i['path'], i['sha256']) for i in items))
    return sha256_text(blob.encode())[:12]


def new_request(items: list[dict], batch_reasons: list[str], now: float | None = None) -> dict:
    return {'id': request_id(items), 'status': 'pending', 'created': now or time.time(),
            'batch_reasons': batch_reasons, 'items': items, 'decided_by': None}


def request_state(req: dict, now: float | None = None) -> str:
    now = now or time.time()
    if req.get('status') in ('approved', 'rejected') and now - req.get('decided_at', req['created']) > DECISION_TTL_SECONDS:
        return 'expired'
    if req['status'] == 'pending' and now - req['created'] > APPROVAL_TTL_SECONDS:
        return 'expired'
    return req['status']


def approved_pairs(requests: list[dict], now: float | None = None) -> set[tuple[str, str]]:
    """(path, sha256) pairs a human approved; a later edit of the file invalidates its approval."""
    pairs = set()
    for req in requests:
        if request_state(req, now) == 'approved' and req.get('decided_by'):
            pairs.update((i['path'], i['sha256']) for i in req['items'])
    return pairs


def approved_batch_ids(requests: list[dict], now: float | None = None) -> set[str]:
    return {r['id'] for r in requests if request_state(r, now) == 'approved' and r.get('decided_by')}


def decide_hold_rows(rows: list[dict], read_bytes, baseline_bytes, pairs: set[tuple[str, str]]):
    """Judge every hold row. Returns (auto_ok, exceptions, total_changed_lines).

    exceptions: [{'path', 'sha256', 'reasons'}] for rows that failed a file rule and lack a human approval.
    """
    auto_ok, exceptions, lines = [], [], 0
    for row in rows:
        path, sha = row['path'], row['source_sha256']
        data = read_bytes(path)
        lines += count_changed_lines(baseline_bytes(path), data)
        if (path, sha) in pairs:
            auto_ok.append(row)
            continue
        reasons = judge_file(path, data)
        if sha256_text(data) != sha:
            reasons.append('hash-mismatch')
        if reasons:
            exceptions.append({'path': path, 'sha256': sha, 'reasons': reasons})
        else:
            auto_ok.append(row)
    return auto_ok, exceptions, lines


def web_sync_ok(deleted: int, added_or_changed: int) -> list[str]:
    reasons = []
    if deleted > MAX_WEB_DELETIONS:
        reasons.append(f'web-deletions>{MAX_WEB_DELETIONS}')
    if added_or_changed == 0 and deleted == 0:
        reasons.append('no-change')
    return reasons


def live_check_ok(statuses: dict[str, int], pages: int | None, prev_pages: int | None, slack: int = 5) -> list[str]:
    problems = [f'{path} -> {code}' for path, code in statuses.items() if code != 200]
    if pages is None:
        problems.append('/api/pages unreadable')
    elif prev_pages is not None and pages < prev_pages - slack:
        problems.append(f'/api/pages {pages} < previous {prev_pages} - {slack}')
    return problems


RERUN_COMMAND = 'cd ~/2nd && python3 scripts/with-pipeline-lock.py -- .venv/bin/python scripts/auto-publish.py --apply'

# (상세에 포함된 표지, 원인, 조치) — 위에서부터 먼저 맞는 것을 쓴다.
FAILURE_HINTS = (
    ('TimeoutExpired', '파생물 갱신이 시간 제한을 넘겼습니다(대개 지식그래프 추출 지연)', '~/projectm/scripts/ai_router_log.jsonl 의 2nd-extract-knowledge-graph 소요 시간과 남은 고아 프로세스(ps) 확인'),
    ('overlapping legacy launchd', '락을 쓰지 않는 옛 launchd 작업이 아직 로드돼 있습니다', 'launchctl list | grep ai.2nd 로 겹치는 작업 확인 후 이전 또는 해제'),
    ('uncommitted', '승인 파일이 커밋되지 않았거나 수정된 상태입니다', '~/2nd 에서 git status 로 확인 후 승인 파일 커밋'),
    ('graph-coverage', '그래프 정합성 검증이 실패했습니다', '~/2nd/.venv/bin/python scripts/artifact-status.py 출력 확인'),
    ('another knowledge writer', '다른 작업이 지식 락을 잡고 있습니다', 'ps 로 pipeline·extract·embed 프로세스 확인'),
    ('differs from origin', '웹 저장소가 원격과 다릅니다', '~/projectm/drone-wiki-web 에서 git status / fetch 확인'),
    ('needs human approval', '사람 승인이 필요한 파일이 있습니다', '텔레그램 승인 버튼 또는 auto-publish.py --approve <id>'),
)


def explain_failure(stage: str, detail: str, progress: dict | None = None) -> str:
    """실패 알림 본문: 원인·조치·재실행 명령을 덧붙인다(고정 문구만; 자식 출력은 그대로 옮기지 않는다)."""
    spent = ''
    if progress:
        done = [f"{r['step']} {r['seconds']:.0f}초" for r in (progress.get('done') or []) if r.get('seconds') is not None]
        if progress.get('current'):
            done.append(f"{progress['current']} 진행 중 끊김")
        if done:
            spent = '\n단계별 소요: ' + ', '.join(done)
    for marker, cause, action in FAILURE_HINTS:
        if marker in (detail or ''):
            return f"원인: {cause}{spent}\n조치: {action}\n재실행: {RERUN_COMMAND}"
    return f"{spent.lstrip(chr(10))}\n재실행: {RERUN_COMMAND}".lstrip('\n')
