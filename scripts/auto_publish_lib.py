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
APPROVAL_TTL_SECONDS = 20 * 3600

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
    if req.get('status') in ('approved', 'rejected') and now - req.get('decided_at', req['created']) > APPROVAL_TTL_SECONDS:
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
