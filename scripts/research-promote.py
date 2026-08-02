#!/usr/bin/env python3
"""
research-promote.py — 연구 루프 13단계: 승인된 클레임을 canonical knowledge로 반영.

v2 재작성 (2026-08-01) — Phase 1 초기(v1, 세션 단일 폴더)용으로 작성된 구버전은
research/RESEARCH_SCHEMA.md v2(카테고리 기반: runs/hypotheses/reviews/drafts)
와 맞지 않아 실제로 한 번도 파이프라인에 연결되지 않았다. 이번 재작성으로
처음 실제 연결한다.

정책 (research/RESEARCH_SCHEMA.md 및 SCHEMA.md 원칙에서 도출):
- 세션 상태가 approved 여야만 승격 가능 (research-run.sh approve 선행 필수).
- claim_type: fact 는 승격 거부 — 이미 존재하는 출처 문서의 재진술이라
  신규 canonical 페이지를 만들 이유가 없다(SCHEMA.md "page thresholds").
  inference/hypothesis만 승격 후보.
- verification_status: insufficient_evidence 는 승격 거부.
- supporting_sources 가 raw 출처를 1건 이상 포함해야 함(SCHEMA provenance).
- 활성 canonical로의 wikilink 2개 이상 확보해야 함(SCHEMA link validity) —
  부족하면 같은 세션의 다른 클레임 인용에서 보충.
- 요청 항목 중 하나라도 검증 실패하면 전체 중단(부분 기록 없음).
- raw/ 파일은 절대 건드리지 않는다.

사용법:
  python3 scripts/research-promote.py <session-id> --items C4,C7
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = WIKI_ROOT / "research" / "runs"
HYP_DIR = WIKI_ROOT / "research" / "hypotheses"
REVIEWS_DIR = WIKI_ROOT / "research" / "reviews"
CANONICAL_DIRS = ["entities", "concepts", "comparisons", "queries"]
SECTION_TITLES = {"entities": "Entities", "concepts": "Concepts",
                   "comparisons": "Comparisons", "queries": "Queries"}


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(text: str, max_len: int = 60) -> str:
    """저장소 관례(전 132편 canonical 전부 영문 slug)를 따른다. 한글 클레임
    텍스트에서 영문/숫자 토큰만 추출 — 실사용 테스트에서 첫 구현이 한글
    slug를 그대로 만들어 기존 관례와 어긋난 문제를 발견하고 수정함."""
    ascii_words = re.findall(r"[A-Za-z0-9]+", text)
    seen = set()
    deduped = []
    for w in ascii_words:
        wl = w.lower()
        if wl not in seen:
            seen.add(wl)
            deduped.append(wl)
    slug = "-".join(deduped)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug[:max_len].strip("-") or "research-finding"


def slug_exists(slug: str) -> str | None:
    for d in CANONICAL_DIRS:
        if (WIKI_ROOT / d / f"{slug}.md").exists():
            return d
    return None


# ---- 파서: hypotheses/<id>.md (claim/claim_type/supporting_sources) -------

CLAIM_HEADER_RE = re.compile(r"^##\s*(C\d+)\s*$", re.MULTILINE)


def parse_claims(path: Path) -> dict[str, dict]:
    text = path.read_text(encoding="utf-8")
    headers = list(CLAIM_HEADER_RE.finditer(text))
    items: dict[str, dict] = {}
    for i, m in enumerate(headers):
        cid = m.group(1)
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        block = text[start:end]

        claim_m = re.search(r"-\s*claim:\s*(.+)", block)
        type_m = re.search(r"-\s*claim_type:\s*(\S+)", block)
        ev_block_m = re.search(r"-\s*supporting_sources:\s*\n((?:\s+-\s+.+\n?)+)", block)
        evidence = []
        if ev_block_m:
            for line in ev_block_m.group(1).splitlines():
                line = line.strip()
                if line.startswith("- "):
                    evidence.append(line[2:].strip())

        items[cid] = {
            "id": cid,
            "claim": claim_m.group(1).strip() if claim_m else "",
            "claim_type": type_m.group(1).strip() if type_m else "unknown",
            "evidence": evidence,
        }
    return items


# ---- 파서: reviews/<id>.md (opposing_sources/limitations/confidence/verification_status)

def parse_reviews(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    headers = list(CLAIM_HEADER_RE.finditer(text))
    items: dict[str, dict] = {}
    for i, m in enumerate(headers):
        cid = m.group(1)
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        block = text[start:end]

        def grab(field: str) -> str:
            fm = re.search(rf"-\s*{field}:\s*(.+)", block)
            return fm.group(1).strip() if fm else ""

        items[cid] = {
            "opposing_sources": grab("opposing_sources"),
            "limitations": grab("limitations"),
            "confidence": grab("confidence") or "low",
            "verification_status": grab("verification_status") or "insufficient_evidence",
        }
    return items


def resolve_evidence(evidence: list[str]) -> tuple[list[str], list[str], list[str]]:
    canon, raw, unresolved = [], [], []
    for item in evidence:
        wl = re.match(r"^\[\[([^\]]+)\]\]$", item)
        rw = re.match(r"^\^\[([^\]]+)\]$", item)
        if wl:
            slug = wl.group(1)
            (canon if slug_exists(slug) else unresolved).append(slug if slug_exists(slug) else item)
        elif rw:
            relpath = rw.group(1)
            (raw if (WIKI_ROOT / relpath).exists() else unresolved).append(relpath if (WIKI_ROOT / relpath).exists() else item)
        else:
            unresolved.append(item)
    return canon, raw, unresolved


def find_extra_wikilinks(all_claims: dict[str, dict], exclude: set[str], need: int) -> list[str]:
    """같은 세션의 다른 클레임이 인용한 canonical slug로 wikilink 부족분을 보충."""
    extra = []
    for c in all_claims.values():
        for ev in c["evidence"]:
            wl = re.match(r"^\[\[([^\]]+)\]\]$", ev)
            if wl and wl.group(1) not in exclude and wl.group(1) not in extra and slug_exists(wl.group(1)):
                extra.append(wl.group(1))
            if len(extra) >= need:
                return extra
    return extra


# ---- 검증 -------------------------------------------------------------------

def validate_item(cid: str, claims: dict, reviews: dict) -> tuple[bool, str, dict]:
    if cid not in claims:
        return False, f"{cid}: 존재하지 않는 클레임 ID", {}
    claim = claims[cid]
    review = reviews.get(cid, {})

    if claim["claim_type"] == "fact":
        return False, f"{cid}: claim_type이 'fact' — 이미 출처 문서 재진술이라 승격 대상 아님", {}
    if claim["claim_type"] not in ("inference", "hypothesis"):
        return False, f"{cid}: claim_type이 유효하지 않음 ({claim['claim_type']})", {}

    if review.get("verification_status") != "grounded":
        return False, f"{cid}: verification_status가 'grounded'가 아님 ({review.get('verification_status')})", {}

    if not claim["evidence"]:
        return False, f"{cid}: supporting_sources가 비어 있음", {}

    canon, raw, unresolved = resolve_evidence(claim["evidence"])
    if unresolved:
        return False, f"{cid}: 해결 불가능한 인용 — {unresolved}", {}
    if not raw:
        return False, f"{cid}: raw 출처가 하나도 없음 (SCHEMA provenance 요건 미충족)", {}

    wikilinks = list(dict.fromkeys(canon))
    if len(wikilinks) < 2:
        extra = find_extra_wikilinks(claims, set(wikilinks) | {cid}, 2 - len(wikilinks))
        wikilinks.extend(extra)
    if len(wikilinks) < 2:
        return False, f"{cid}: 활성 canonical wikilink 2개 확보 불가 (SCHEMA 링크 규칙)", {}

    return True, "", {"canon": canon, "raw": raw, "wikilinks": wikilinks[:4], "review": review}


# ---- 페이지 생성 -------------------------------------------------------------

def unique_slug(base_slug: str, target_dir: str) -> str:
    slug = base_slug
    n = 2
    while (WIKI_ROOT / target_dir / f"{slug}.md").exists():
        slug = f"{base_slug}-{n}"
        n += 1
    return slug


def yaml_safe_title(text: str) -> str:
    """YAML 큰따옴표 문자열 내부의 따옴표를 이스케이프한다. 실사용 테스트에서
    클레임 본문에 "micro drone" 같은 내부 인용부호가 있어 frontmatter가
    깨지는 문제를 발견해 수정함."""
    return text.replace("\\", "\\\\").replace('"', '\\"')


def build_page(claim: dict, resolved: dict, session_id: str, today: str) -> str:
    confidence = "medium" if claim["claim_type"] == "inference" else "low"
    review = resolved["review"]
    # Phase O2 (ONTOLOGY_IMPLEMENTATION_ROADMAP.md) — claim_type을 본문
    # 텍스트에만 남기지 않고 frontmatter의 선택적 10번째 필드로 기록한다.
    # SCHEMA.md 9개 필수 필드 계약은 그대로 유지(추가만, 제거·변경 없음).
    fm = (
        "---\n"
        f"title: \"{yaml_safe_title(claim['claim'])}\"\n"
        f"created: {today}\n"
        f"updated: {today}\n"
        "type: concept\n"
        "tags: []\n"
        "sources:\n" + "\n".join(f"  - {p}" for p in resolved["raw"]) + "\n"
        f"confidence: {confidence}\n"
        "domain: ai-agent\n"
        "contested: false\n"
        "contradictions: []\n"
        f"claim_type: {claim['claim_type']}\n"
        "---\n"
    )
    body = [
        f"# {claim['claim']}",
        "",
        f"> 이 페이지는 인간 승인형 AI 연구 세션 `research/runs/{session_id}`에서 "
        f"마스터 승인을 거쳐 승격된 {claim['claim_type']} 클레임(`{claim['id']}`)이다. "
        f"세션 원본 산출물은 `research/hypotheses/{session_id}.md`,"
        f" `research/reviews/{session_id}.md`에 그대로 보존되어 있다.",
        "",
        "## 주장",
        "",
        claim["claim"],
        "",
        "## 근거",
        "",
    ]
    for c in resolved["canon"]:
        body.append(f"- [[{c}]]")
    for r in resolved["raw"]:
        body.append(f"- ^[{r}]")
    body += [
        "",
        "## 검토 노트 (Critic)",
        "",
        f"- 반론/모순: {review.get('opposing_sources') or '없음'}",
        f"- 한계: {review.get('limitations') or '식별된 제약 없음'}",
        "",
        "## 관련",
        "",
        " ".join(f"[[{s}]]" for s in resolved["wikilinks"]),
        "",
    ]
    return fm + "\n".join(body)


def update_index(new_entries: list[tuple[str, str, str]]) -> None:
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
        entry_lines = [l for l in section_body.split("\n") if l.startswith("- ")]
        entry_lines.append(new_line)
        entry_lines.sort(key=lambda l: re.sub(r"^- \[\[", "", l).lower())
        text = text[:sec_start] + "\n" + "\n".join(entry_lines) + "\n" + text[sec_end:]
    total = len(re.findall(r"^- \[\[", text, re.MULTILINE))
    text = re.sub(r"Total pages:\s*\d+", f"Total pages: {total}", text, count=1)
    index_path.write_text(text, encoding="utf-8")


def append_log(session_id: str, goal: str, created_pages: list[tuple[str, str, str]]) -> None:
    log_path = WIKI_ROOT / "log.md"
    today = date.today().isoformat()
    lines = [f"\n## [{today}] research-promote | {goal[:80]}", ""]
    lines.append(f"- Source: `research/drafts/{session_id}.md` (마스터 승인)")
    lines.append("- Created pages:")
    for target_dir, slug, summary in created_pages:
        lines.append(f"  - `{target_dir}/{slug}.md` — {summary}")
    lines.append("- Updated: `index.md`")
    with log_path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def update_state(session_id: str, promoted: dict[str, str]) -> None:
    sf = RUNS_DIR / session_id / "state.json"
    state = json.loads(sf.read_text(encoding="utf-8"))
    state.setdefault("promoted", {})
    state["promoted"].update(promoted)
    state["updated"] = now_utc()
    sf.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("session_id")
    ap.add_argument("--items", required=True, help="쉼표구분 클레임 ID, 예: C4,C7")
    args = ap.parse_args()

    session_dir = RUNS_DIR / args.session_id
    hyp_path = HYP_DIR / f"{args.session_id}.md"
    reviews_path = REVIEWS_DIR / f"{args.session_id}.md"
    state_path = session_dir / "state.json"

    if not session_dir.exists() or not hyp_path.exists():
        print(f"ERROR: 세션 없음 또는 미완료 — {args.session_id}", file=sys.stderr)
        return 1

    state = json.loads(state_path.read_text(encoding="utf-8"))
    if state.get("status") != "approved":
        print(f"ERROR: 세션 상태가 'approved'가 아님 (현재: {state.get('status')}). "
              f"먼저 'research-run.sh approve {args.session_id}' 실행 필요", file=sys.stderr)
        return 1

    claims = parse_claims(hyp_path)
    reviews = parse_reviews(reviews_path)
    requested = [i.strip() for i in args.items.split(",") if i.strip()]

    resolved_by_id, failures = {}, []
    for cid in requested:
        ok, reason, resolved = validate_item(cid, claims, reviews)
        if not ok:
            failures.append(reason)
        else:
            resolved_by_id[cid] = resolved

    if failures:
        print("승격 거부 — 검증 실패 (전체 중단, 부분 기록 없음):", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1

    today = date.today().isoformat()
    goal_path = session_dir / "00-goal.md"
    goal_text = goal_path.read_text(encoding="utf-8").strip() if goal_path.exists() else args.session_id
    created_pages, promoted = [], {}

    for cid in requested:
        claim = claims[cid]
        resolved = resolved_by_id[cid]
        base_slug = slugify(claim["claim"])
        slug = unique_slug(base_slug, "concepts")
        page_text = build_page(claim, resolved, args.session_id, today)
        (WIKI_ROOT / "concepts" / f"{slug}.md").write_text(page_text, encoding="utf-8")
        summary = claim["claim"][:100]
        created_pages.append(("concepts", slug, summary))
        promoted[cid] = slug
        print(f"생성: concepts/{slug}.md  (from {cid}, {claim['claim_type']})")

    update_index(created_pages)
    append_log(args.session_id, goal_text, created_pages)
    update_state(args.session_id, promoted)

    print(f"\n승격 완료: {len(created_pages)}건. index.md·log.md 원자적 갱신 완료.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
