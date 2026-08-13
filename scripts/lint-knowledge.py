#!/usr/bin/env python3
"""lint-knowledge.py — SCHEMA.md 9필드 계약 + wikilink 최소 2개 규칙을
canonical 페이지 생성 경로 전부(research-promote.py 뿐 아니라 daily-ingest도)에
코드로 강제한다.

배경(CURRENT_STATE_AUDIT.md 2026-08-01 발견 + SHAPES.md 체크리스트 3항):
research-promote.py::validate_item()은 research/ 경로로 승격되는 페이지만
검증한다. daily-ingest(hermes llm-wiki skill)가 직접 쓰는 페이지는 어떤
자동 검증도 거치지 않는다 — README가 주장하는 승인 게이트와 실제 동작이
어긋나는 근본 원인이었다. 이 스크립트는 새 규칙을 만들지 않는다 —
SCHEMA.md/SHAPES.md가 이미 문서로 정의했지만 "강제 방식: 수동 검토"였던
규칙만 코드로 옮긴다.

실행:
  scripts/lint-knowledge.py                    # 변경분만 검사 (수동 ai-control.sh 게이트용)
  scripts/lint-knowledge.py --full              # 전체 코퍼스 검사 (읽기 전용 리포트,
                                                 # 기존 페이지를 무효화하지 않음 — 게이트 아님)
  scripts/lint-knowledge.py --recent-hours 2    # 최근 N시간 내 mtime 변경 파일만 검사
                                                 # (hermes cron 자동 daily-ingest 워치독용 —
                                                 # 이 잡은 ai-control.sh를 거치지 않고 별도
                                                 # 스킬이 직접 파일을 쓰므로, git 커밋 타이밍에
                                                 # 의존하는 changed_files() 대신 mtime 기준으로
                                                 # 감지해야 커밋 여부/시점과 무관하게 정확하다)
  scripts/lint-knowledge.py --recent-hours 2 --quiet   # 워치독 모드: 위반 없으면 완전 침묵
                                                 # (hermes --no-agent 잡의 "빈 stdout=조용히
                                                 # 넘어감" 규약에 맞춤 — 매일 정상 텔레그램
                                                 # 알림이 오는 소음을 피함)

종료코드: 0 = 위반 없음, 1 = 위반 있음.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR_TYPE = {
    "concepts": "concept",
    "entities": "entity",
    "comparisons": "comparison",
    "queries": "query",
}
REQUIRED_FIELDS = [
    "title", "created", "updated", "type", "tags",
    "sources", "confidence", "contested", "contradictions",
]
VALID_CONFIDENCE = {"high", "medium", "low"}
WIKILINK_RE = re.compile(r"\[\[([a-z0-9-]+)\]\]")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """정규식 기반 경량 frontmatter 파서 (research-promote.py 등 기존 스크립트와
    같은 스타일 — PyYAML 등 새 의존성 추가 안 함). `key: value` 한 줄 형식과
    YAML 블록 리스트(`key:\\n  - item`) 두 형식을 모두 값 유무 판정 목적으로
    지원한다 — 실제 실사용 canonical 파일 다수가 후자를 쓰기 때문에 지원이
    필수다(값 파싱 정확도가 아니라 "필드가 비어있는가"만 판정하면 되므로
    리스트 항목은 콤마로 이어붙인 문자열로만 보관한다)."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    lines = text[4:end].splitlines()
    fm: dict[str, str] = {}
    i = 0
    while i < len(lines):
        m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", lines[i])
        if not m:
            i += 1
            continue
        key, value = m.group(1), m.group(2).strip()
        if value:
            fm[key] = value
            i += 1
            continue
        # 값이 같은 줄에 없음 — 다음 줄들이 "  - item" 블록 리스트인지 확인
        items = []
        j = i + 1
        while j < len(lines) and re.match(r"^\s+-\s*(.*)$", lines[j]):
            items.append(re.match(r"^\s+-\s*(.*)$", lines[j]).group(1).strip())
            j += 1
        fm[key] = ", ".join(items) if items else ""
        i = j if items else i + 1
    return fm


def all_slugs() -> set[str]:
    slugs = set()
    for d in DIR_TYPE:
        for p in (ROOT / d).glob("*.md"):
            slugs.add(p.stem)
    return slugs


def changed_files() -> list[Path]:
    """git 기준 아직 커밋 안 된 변경/신규 canonical 파일만 (daily-ingest 게이트용)."""
    dirs = list(DIR_TYPE)
    try:
        modified = subprocess.run(
            ["git", "-C", str(ROOT), "diff", "--name-only", "--diff-filter=ACM", "HEAD", "--", *dirs],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
        untracked = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "--others", "--exclude-standard", "--", *dirs],
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
    except subprocess.CalledProcessError:
        return []
    names = set(modified) | set(untracked)
    result = []
    for name in names:
        if name.endswith(".md") and not name.endswith(".gitkeep"):
            p = ROOT / name
            if p.exists():
                result.append(p)
    return result


def recent_files(hours: float) -> list[Path]:
    """git 상태와 무관하게 최근 `hours`시간 내 mtime이 갱신된 canonical 파일만
    (hermes 자동 daily-ingest 워치독용 — 이 잡은 git 커밋을 거치지 않고 파일을
    직접 쓸 수도 있어 changed_files()의 git diff 기반 감지가 못 미더울 수 있다)."""
    cutoff = time.time() - hours * 3600
    files: list[Path] = []
    for d in DIR_TYPE:
        for p in (ROOT / d).glob("*.md"):
            if p.name != ".gitkeep" and p.stat().st_mtime >= cutoff:
                files.append(p)
    return sorted(files)


def target_files(full: bool, recent_hours: float | None) -> list[Path]:
    if full:
        files: list[Path] = []
        for d in DIR_TYPE:
            files.extend(sorted((ROOT / d).glob("*.md")))
        return [f for f in files if f.name != ".gitkeep"]
    if recent_hours is not None:
        return recent_files(recent_hours)
    return changed_files()


def lint_file(path: Path, slugs: set[str]) -> list[str]:
    errors: list[str] = []
    expected_type = DIR_TYPE.get(path.parent.name)
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        return ["frontmatter 없음 또는 형식 오류 (--- 블록을 찾을 수 없음)"]

    for field in REQUIRED_FIELDS:
        if field not in fm or fm[field] == "":
            errors.append(f"필수 필드 누락: {field} (SCHEMA.md 9필드 계약)")

    if expected_type and fm.get("type") != expected_type:
        errors.append(f"type 불일치: frontmatter='{fm.get('type')}' vs 디렉토리='{expected_type}'")

    if "confidence" in fm and fm["confidence"] not in VALID_CONFIDENCE:
        errors.append(f"confidence 값 무효: {fm['confidence']!r} (허용: high/medium/low)")

    if "contested" in fm and fm["contested"] not in ("true", "false"):
        errors.append(f"contested 값 무효: {fm['contested']!r} (허용: true/false)")

    found = set(WIKILINK_RE.findall(text)) - {path.stem}
    resolvable = found & slugs
    if len(resolvable) < 2:
        errors.append(
            f"활성 canonical wikilink 2개 미만 (해석됨: {len(resolvable)}개 {sorted(resolvable)}) "
            "— SCHEMA.md §Canonical link validity"
        )

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--full", action="store_true", help="전체 코퍼스 검사(읽기 전용 리포트)")
    ap.add_argument("--recent-hours", type=float, default=None,
                     help="최근 N시간 내 mtime 변경 파일만 검사(hermes 자동잡 워치독용)")
    ap.add_argument("--quiet", action="store_true",
                     help="위반 0건이면 아무 출력도 안 함(hermes --no-agent 워치독의 '빈 출력=조용히 통과' 규약용)")
    args = ap.parse_args()

    slugs = all_slugs()
    files = target_files(full=args.full, recent_hours=args.recent_hours)
    mode = "전체" if args.full else (f"최근{args.recent_hours}시간" if args.recent_hours is not None else "변경분")

    if not files:
        if not args.quiet:
            print(f"lint-knowledge ({mode}): 검사 대상 없음")
        return 0

    total_errors = 0
    report_lines = []
    for path in files:
        errs = lint_file(path, slugs)
        if errs:
            total_errors += len(errs)
            report_lines.append(f"FAIL {path.relative_to(ROOT)}")
            for e in errs:
                report_lines.append(f"  - {e}")

    if total_errors == 0 and args.quiet:
        return 0

    for line in report_lines:
        print(line)
    print(f"lint-knowledge ({mode}): {len(files)}개 파일 검사, 위반 {total_errors}건")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
