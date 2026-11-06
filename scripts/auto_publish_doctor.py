"""auto-publish --doctor: 배포 없이 발행 사전 조건을 읽기 전용으로 점검한다(2026-11-06).

10/31 이후 뉴스 정지 때 한 번에 하나씩 겪은 막힘(미커밋 승인 파일, 레거시 launchd 겹침, 락·고아 프로세스, 웹 저장소 불일치, 대기 문서)을
실행 전에 한꺼번에 찾는다. 어떤 파일도 쓰지 않고 커밋·푸시·배포·알림도 하지 않는다. 각 항목은 (이름, 상태, 설명, 조치) 로 돌려준다.
상태: OK / WARN(발행은 가능) / FAIL(발행이 막힘).
"""
from __future__ import annotations
import json
import re
import subprocess
from pathlib import Path

OK, WARN, FAIL = 'OK', 'WARN', 'FAIL'
BUSY_PATTERN = re.compile(r'scripts/(auto-publish|knowledge-pipeline|extract-knowledge-graph|embed-docs)\.py')


def _git(args, cwd, run=subprocess.run) -> str:
    r = run(['git', *args], cwd=cwd, capture_output=True, text=True, timeout=60)
    return (r.stdout or '').strip()


def check_busy_processes(ps_output: str, own_pid: int | None = None) -> tuple:
    """실행 중인 발행·파이프라인·추출·임베딩 프로세스(고아 포함)."""
    rows = [l for l in ps_output.splitlines() if BUSY_PATTERN.search(l) and '--doctor' not in l and (own_pid is None or not l.strip().startswith(f'{own_pid} '))]
    if rows:
        return ('busy-processes', FAIL, f'{len(rows)}개 실행 중', 'ps 로 확인 후 정상 실행이면 끝날 때까지 대기, 고아(PPID 1)면 종료')
    return ('busy-processes', OK, '없음', '')


def check_git_clean(root: Path, web: Path, run=subprocess.run) -> list:
    out = []
    pub = _git(['status', '--porcelain', '--', 'publication/'], root, run)
    out.append(('publication-clean', FAIL if pub else OK, f'미커밋 {len(pub.splitlines())}건' if pub else '깨끗함', 'publication/ 변경을 커밋(또는 되돌림)' if pub else ''))
    staged = _git(['diff', '--cached', '--name-only'], root, run)
    out.append(('nothing-staged', FAIL if staged else OK, f'스테이징 {len(staged.splitlines())}건' if staged else '없음', 'git restore --staged 로 해제' if staged else ''))
    dirty = _git(['status', '--porcelain', '--', 'data/wiki'], web, run)
    out.append(('web-data-clean', FAIL if dirty else OK, f'수정 {len(dirty.splitlines())}건' if dirty else '깨끗함', '웹 data/wiki 변경 확인(git status)' if dirty else ''))
    return out


def check_approved_committed(root: Path, policy: dict, run=subprocess.run) -> tuple:
    """정책에 고정된 승인 파일이 커밋되지 않았으면 매니페스트 단계가 실패한다."""
    paths = list((policy.get('approved_files') or {}).keys())
    dirty = []
    for i in range(0, len(paths), 200):
        dirty += _git(['status', '--porcelain', '--', *paths[i:i + 200]], root, run).splitlines()
    if dirty:
        return ('approved-files-committed', FAIL, f'미커밋·수정 {len(dirty)}건', '승인 파일을 커밋한 뒤 실행')
    return ('approved-files-committed', OK, f'{len(paths)}건 모두 커밋됨', '')


def check_web_sync(web: Path, run=subprocess.run) -> tuple:
    """웹 저장소가 원격보다 앞서거나 갈라졌으면 막힌다(뒤처지기만 하면 발행이 자동으로 따라잡는다). 마지막으로 fetch 한 시점 기준."""
    head = _git(['rev-parse', 'HEAD'], web, run)
    remote = _git(['rev-parse', 'origin/main'], web, run)
    if head == remote:
        return ('web-sync', OK, 'origin/main 과 일치', '')
    ahead = _git(['rev-list', '--count', f'{remote}..{head}'], web, run) or '0'
    behind = _git(['rev-list', '--count', f'{head}..{remote}'], web, run) or '0'
    if ahead == '0':
        return ('web-sync', WARN, f'원격보다 {behind}커밋 뒤처짐(발행이 자동 fast-forward)', '')
    return ('web-sync', FAIL, f'앞선 {ahead} / 뒤처진 {behind} 커밋', '웹 저장소에서 푸시 또는 정리 후 실행')


def check_legacy_launchd(labels, loaded, shares_lock) -> tuple:
    """loaded(label)->bool 이 로드된 작업, shares_lock(label)->bool 이 락 공유 여부. 겹침=로드돼 있고 락을 공유하지 않는 것."""
    overlap = [l for l in labels if loaded(l) and not shares_lock(l)]
    if overlap:
        return ('legacy-launchd', FAIL, '락 없는 옛 작업 로드됨: ' + ', '.join(overlap), 'launchctl 로 해당 작업 이전·해제')
    return ('legacy-launchd', OK, '겹치는 작업 없음', '')


def check_pending_documents(status_stdout: str) -> tuple:
    try:
        d = json.loads(status_stdout[status_stdout.index('{'):])
    except (ValueError, TypeError):
        return ('discovery-pending', WARN, 'artifact-status 출력 해석 실패', 'scripts/artifact-status.py 직접 실행')
    n = d.get('discovery_pending_documents', 0)
    bad = [k for k in ('duplicate_slugs', 'missing_nodes', 'extra_nodes') if d.get(k)]
    if bad or d.get('canonical_node_source_fresh') is False:
        return ('graph-integrity', FAIL, '정합성 오류: ' + ', '.join(bad or ['canonical_node_source_fresh']), 'update-graph.sh 후 artifact-status 재확인')
    if n:
        return ('discovery-pending', WARN, f'추출 대기 {n}건(소진 루프가 처리)', '')
    return ('discovery-pending', OK, '대기 0건', '')


def check_site(fetch, url: str) -> tuple:
    try:
        code = fetch(url)
    except Exception as exc:  # noqa: BLE001
        return ('site-alive', WARN, f'대표 주소 확인 실패({type(exc).__name__})', '네트워크 확인')
    return ('site-alive', OK if code == 200 else WARN, f'{url} → {code}', '' if code == 200 else '사이트 상태 확인')


def format_report(rows: list) -> str:
    mark = {OK: '✅', WARN: '⚠️ ', FAIL: '❌'}
    lines = [f"{mark[s]} {n}: {d}" + (f"\n     → {a}" if a else '') for n, s, d, a in rows]
    verdict = 'FAIL' if any(r[1] == FAIL for r in rows) else 'WARN' if any(r[1] == WARN for r in rows) else 'OK'
    lines.append(f'\n종합: {verdict}' + (' — 발행 전에 ❌ 항목을 해결하세요' if verdict == 'FAIL' else ' — 발행 가능'))
    return '\n'.join(lines)


def exit_code(rows: list) -> int:
    return 2 if any(r[1] == FAIL for r in rows) else 0
