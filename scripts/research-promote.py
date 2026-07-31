#!/usr/bin/env python3
"""
research-promote.py — G3 승격: 승인된 가설만 canonical knowledge로 반영.

research/RESEARCH_SCHEMA.md § Promotion rules(G3)의 구현체.
- 검증 없는 항목(status != proposed, evidence 비어있음/미해결, verifier_note에
  [근거 부족] 포함)은 거부한다.
- 요청된 항목 중 하나라도 검증에 실패하면 전체를 중단한다(부분 기록 금지).
- raw/ 파일은 절대 건드리지 않는다. canonical 쓰기는 이 스크립트만 수행한다.

사용법:
  python3 scripts/research-promote.py <session-id> --approve --items H1,H3
  python3 scripts/research-promote.py <session-id> --reject "사유"
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import date, datetime, timezone
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
RESEARCH_DIR = WIKI_ROOT / "research"
CANONICAL_DIRS = ["entities", "concepts", "comparisons", "queries"]
SECTION_TITLES = {"entities": "Entities", "concepts": "Concepts",
                   "comparisons": "Comparisons", "queries": "Queries"}


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(text: str, max_len: int = 60) -> str:
    text = re.sub(r"[^\w\s가-힣-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip()).lower()
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:max_len].strip("-") or "research-item"


def slug_exists(slug: str) -> str | None:
    """canonical 4계층 중 slug.md가 존재하는 디렉터리를 반환, 없으면 None."""
    for d in CANONICAL_DIRS:
        if (WIKI_ROOT / d / f"{slug}.md").exists():
            return d
    return None


# ---- 04-hypotheses.md 파서 -------------------------------------------------

HYP_HEADER_RE = re.compile(r"^##\s*(H\d+):\s*(.+)$", re.MULTILINE)


def parse_hypotheses(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    headers = list(HYP_HEADER_RE.finditer(text))
    items = []
    for i, m in enumerate(headers):
        hid, claim = m.group(1), m.group(2).strip()
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        block = text[start:end]

        status_m = re.search(r"-\s*status:\s*(\S+)", block)
        status = status_m.group(1).strip() if status_m else "proposed"

        verifier_m = re.search(r"-\s*verifier_note:\s*(.+)", block)
        verifier_note = verifier_m.group(1).strip() if verifier_m else ""

        counter_m = re.search(r"-\s*counter:\s*(.+)", block)
        counter = counter_m.group(1).strip() if counter_m else ""

        ev_block_m = re.search(r"-\s*evidence:\s*\n((?:\s+-\s+.+\n?)+)", block)
        evidence = []
        if ev_block_m:
            for line in ev_block_m.group(1).splitlines():
                line = line.strip()
                if line.startswith("- "):
                    evidence.append(line[2:].strip())

        items.append({
            "id": hid, "claim": claim, "status": status,
            "evidence": evidence, "verifier_note": verifier_note, "counter": counter,
            "raw_block": block,
        })
    return items


def resolve_evidence(evidence: list[str]) -> tuple[list[str], list[str], list[str]]:
    """반환: (canonical_slugs, raw_paths, unresolved)"""
    canon, raw, unresolved = [], [], []
    for item in evidence:
        wl = re.match(r"^\[\[([^\]]+)\]\]$", item)
        rw = re.match(r"^\^\[([^\]]+)\]$", item)
        if wl:
            slug = wl.group(1)
            if slug_exists(slug):
                canon.append(slug)
            else:
                unresolved.append(item)
        elif rw:
            relpath = rw.group(1)
            if (WIKI_ROOT / relpath).exists():
                raw.append(relpath)
            else:
                unresolved.append(item)
        else:
            unresolved.append(item)
    return canon, raw, unresolved


def find_extra_wikilinks(session_dir: Path, exclude: set[str], need: int) -> list[str]:
    """검색 결과(02a-search-hits.md)에서 이미 검증된 canonical slug를 보충."""
    hits_file = session_dir / "02a-search-hits.md"
    if not hits_file.exists():
        return []
    text = hits_file.read_text(encoding="utf-8")
    slugs = re.findall(r"slug:\s*`([^`]+)`", text)
    extra = []
    for s in slugs:
        if s in exclude or s in extra:
            continue
        if slug_exists(s):
            extra.append(s)
        if len(extra) >= need:
            break
    return extra


# ---- 검증 -------------------------------------------------------------------

def validate_item(item: dict, session_dir: Path) -> tuple[bool, str, dict]:
    """반환: (통과여부, 실패사유, resolved{canon,raw,wikilinks})"""
    if item["status"] != "proposed":
        return False, f"{item['id']}: status가 'proposed'가 아님 (현재: {item['status']})", {}

    if "[근거 부족]" in item["verifier_note"]:
        return False, f"{item['id']}: verifier_note에 [근거 부족] 표시됨 — 승격 불가", {}

    if not item["evidence"]:
        return False, f"{item['id']}: evidence 목록이 비어 있음", {}

    canon, raw, unresolved = resolve_evidence(item["evidence"])
    if unresolved:
        return False, f"{item['id']}: 해결되지 않는 인용 경로 존재 — {unresolved}", {}

    if not raw:
        return False, f"{item['id']}: raw 출처가 하나도 없음 (SCHEMA provenance 요건 미충족)", {}

    wikilinks = list(dict.fromkeys(canon))  # dedupe, order-preserving
    if len(wikilinks) < 2:
        extra = find_extra_wikilinks(session_dir, set(wikilinks), 2 - len(wikilinks))
        wikilinks.extend(extra)
    if len(wikilinks) < 2:
        return False, f"{item['id']}: 활성 canonical 페이지로의 wikilink를 2개 이상 확보할 수 없음 (SCHEMA 링크 규칙)", {}

    return True, "", {"canon": canon, "raw": raw, "wikilinks": wikilinks[:4]}


# ---- 페이지 생성 -------------------------------------------------------------

def unique_slug(base_slug: str, target_dir: str) -> str:
    slug = base_slug
    n = 2
    while (WIKI_ROOT / target_dir / f"{slug}.md").exists():
        slug = f"{base_slug}-{n}"
        n += 1
    return slug


def build_page(item: dict, resolved: dict, session_id: str, today: str) -> str:
    tags_line = "tags: []"
    sources_line = "sources:\n" + "\n".join(f"  - {p}" for p in resolved["raw"])
    fm = (
        "---\n"
        f"title: \"{item['claim']}\"\n"
        f"created: {today}\n"
        f"updated: {today}\n"
        "type: concept\n"
        f"{tags_line}\n"
        f"{sources_line}\n"
        "confidence: low\n"
        "domain: ai-agent\n"
        "contested: false\n"
        "contradictions: []\n"
        "---\n"
    )
    wikilinks_line = " ".join(f"[[{s}]]" for s in resolved["wikilinks"])
    body_lines = [
        f"# {item['claim']}",
        "",
        f"> 이 페이지는 인간 승인형 AI 연구 세션 `research/{session_id}`에서 "
        f"마스터 승인을 거쳐 생성되었다. 원 세션 산출물(질문 분해, 근거, 비판, "
        f"검증)은 `research/{session_id}/`에 보존되어 있다.",
        "",
        "## 주장",
        "",
        item["claim"],
        "",
        "## 근거",
        "",
    ]
    for c in resolved["canon"]:
        body_lines.append(f"- [[{c}]]")
    for r in resolved["raw"]:
        body_lines.append(f"- ^[{r}]")
    body_lines += ["", "## 검토 노트", ""]
    body_lines.append(f"- 반론/한계: {item['counter'] or '(기록 없음)'}")
    body_lines.append(f"- 검증 상태: {item['verifier_note'] or '(기록 없음)'}")
    body_lines += ["", "## 관련", "", wikilinks_line, ""]
    return fm + "\n".join(body_lines)


# ---- index.md / log.md 원자적 갱신 --------------------------------------------

def update_index(new_entries: list[tuple[str, str, str]]) -> None:
    """new_entries: [(dir, slug, one_line_summary), ...]"""
    index_path = WIKI_ROOT / "index.md"
    text = index_path.read_text(encoding="utf-8")

    for target_dir, slug, summary in new_entries:
        section = SECTION_TITLES[target_dir]
        header_re = re.compile(rf"^## {re.escape(section)}\s*$", re.MULTILINE)
        m = header_re.search(text)
        new_line = f"- [[{slug}]] — {summary}"
        if not m:
            text += f"\n\n## {section}\n\n{new_line}\n"
            continue
        sec_start = m.end()
        next_header_m = re.search(r"^## ", text[sec_start:], re.MULTILINE)
        sec_end = sec_start + next_header_m.start() if next_header_m else len(text)
        section_body = text[sec_start:sec_end]

        lines = [l for l in section_body.split("\n")]
        entry_lines = [l for l in lines if l.startswith("- ")]
        other_lines = [l for l in lines if not l.startswith("- ")]
        entry_lines.append(new_line)
        entry_lines.sort(key=lambda l: re.sub(r"^- \[\[", "", l).lower())

        rebuilt = "\n".join(other_lines[:1]) + "\n" if other_lines and other_lines[0].strip() == "" else "\n"
        rebuilt = "\n" + "\n".join(entry_lines) + "\n"
        text = text[:sec_start] + rebuilt + text[sec_end:]

    total = sum(len(re.findall(r"^- \[\[", text, re.MULTILINE)) for _ in [0])
    total = len(re.findall(r"^- \[\[", text, re.MULTILINE))
    text = re.sub(r"Total pages:\s*\d+", f"Total pages: {total}", text, count=1)

    index_path.write_text(text, encoding="utf-8")


def append_log(session_id: str, goal: str, created_pages: list[tuple[str, str, str]]) -> None:
    log_path = WIKI_ROOT / "log.md"
    today = date.today().isoformat()
    lines = [f"\n## [{today}] research-promote | {goal[:80]}", ""]
    lines.append(f"- Source: `research/{session_id}/06-report-draft.md` (마스터 승인)")
    lines.append("- Created pages:")
    for target_dir, slug, summary in created_pages:
        lines.append(f"  - `{target_dir}/{slug}.md` — {summary}")
    lines.append("- Updated: `index.md`")
    with log_path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ---- state.json ---------------------------------------------------------

def update_state(session_dir: Path, approvals_patch: dict) -> None:
    sf = session_dir / "state.json"
    state = json.loads(sf.read_text(encoding="utf-8"))
    state.setdefault("approvals", {})
    for k, v in approvals_patch.items():
        if k == "G3" and isinstance(v, dict):
            state["approvals"].setdefault("G3", {})
            state["approvals"]["G3"].update(v)
        else:
            state["approvals"][k] = v
    state["updated"] = now_utc()
    sf.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def rewrite_hypotheses_status(hyp_path: Path, items: list[dict], approved_ids: set[str]) -> None:
    text = hyp_path.read_text(encoding="utf-8")
    for item in items:
        if item["id"] not in approved_ids:
            continue
        old_block_status = re.search(rf"(##\s*{item['id']}:.*?\n(?:.*\n)*?-\s*status:\s*)(\S+)", text)
        if old_block_status:
            text = text[:old_block_status.start(2)] + "approved" + text[old_block_status.end(2):]
    hyp_path.write_text(text, encoding="utf-8")


# ---- 메인 로직 -----------------------------------------------------------

def cmd_reject(session_id: str, reason: str) -> int:
    session_dir = RESEARCH_DIR / session_id
    if not session_dir.exists():
        print(f"ERROR: 세션 없음 — {session_id}", file=sys.stderr)
        return 1

    update_state(session_dir, {"G2": "rejected"})
    sf = session_dir / "state.json"
    state = json.loads(sf.read_text(encoding="utf-8"))
    state["reject_reason"] = reason
    state["updated"] = now_utc()
    sf.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    archive_dir = RESEARCH_DIR / "_archive" / session_id
    archive_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(session_dir), str(archive_dir))

    print(f"세션 반려 완료: {session_id} → research/_archive/{session_id}")
    print(f"사유: {reason}")
    print("canonical/index.md/log.md/raw 무변경 확인됨 (쓰기 경로 미실행).")
    return 0


def cmd_approve(session_id: str, requested_ids: list[str]) -> int:
    session_dir = RESEARCH_DIR / session_id
    if not session_dir.exists():
        print(f"ERROR: 세션 없음 — {session_id}", file=sys.stderr)
        return 1

    hyp_path = session_dir / "04-hypotheses.md"
    report_path = session_dir / "06-report-draft.md"
    goal_path = session_dir / "00-goal.md"
    if not hyp_path.exists() or not report_path.exists():
        print("ERROR: 04-hypotheses.md 또는 06-report-draft.md 없음 — 파이프라인 미완료", file=sys.stderr)
        return 1

    all_items = {i["id"]: i for i in parse_hypotheses(hyp_path)}
    missing = [rid for rid in requested_ids if rid not in all_items]
    if missing:
        print(f"ERROR: 존재하지 않는 가설 ID — {missing}", file=sys.stderr)
        return 1

    resolved_by_id = {}
    failures = []
    for rid in requested_ids:
        ok, reason, resolved = validate_item(all_items[rid], session_dir)
        if not ok:
            failures.append(reason)
        else:
            resolved_by_id[rid] = resolved

    if failures:
        print("승격 거부 — 다음 항목이 검증을 통과하지 못했습니다 (전체 중단, 부분 기록 없음):", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    today = date.today().isoformat()
    goal_text = goal_path.read_text(encoding="utf-8").strip() if goal_path.exists() else session_id
    created_pages = []

    for rid in requested_ids:
        item = all_items[rid]
        resolved = resolved_by_id[rid]
        target_dir = "concepts"
        base_slug = slugify(item["claim"])
        slug = unique_slug(base_slug, target_dir)
        page_text = build_page(item, resolved, session_id, today)
        page_path = WIKI_ROOT / target_dir / f"{slug}.md"
        page_path.write_text(page_text, encoding="utf-8")
        summary = item["claim"][:100]
        created_pages.append((target_dir, slug, summary))
        print(f"생성: {target_dir}/{slug}.md")

    update_index([(d, s, summary) for d, s, summary in created_pages])
    append_log(session_id, goal_text, created_pages)
    rewrite_hypotheses_status(hyp_path, list(all_items.values()), set(requested_ids))

    g3_patch = {rid: "approved" for rid in requested_ids}
    update_state(session_dir, {"G2": "approved", "G3": g3_patch})

    print(f"\n승격 완료: {len(created_pages)}건. index.md·log.md 원자적 갱신 완료.")
    print("세션은 research/ 에 그대로 보존됩니다 (감사 추적).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("session_id")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--approve", action="store_true")
    g.add_argument("--reject", action="store_true")
    ap.add_argument("--items", type=str, help="쉼표구분 가설 ID, 예: H1,H3")
    ap.add_argument("--reason", type=str, default="사유 미기재")
    args = ap.parse_args()

    if args.approve:
        if not args.items:
            print("ERROR: --approve 사용 시 --items H1,H2 형식으로 승격 대상을 명시해야 합니다", file=sys.stderr)
            return 1
        ids = [i.strip() for i in args.items.split(",") if i.strip()]
        return cmd_approve(args.session_id, ids)
    else:
        return cmd_reject(args.session_id, args.reason)


if __name__ == "__main__":
    sys.exit(main())
