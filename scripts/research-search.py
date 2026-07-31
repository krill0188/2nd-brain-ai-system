#!/usr/bin/env python3
"""
research-search.py — 연구 루프의 기계적(비-LLM) 검색 단계 (Retriever).

canonical(entities/concepts/comparisons/queries) + raw/ + news-feed.json +
knowledge-graph.json 이웃 확장을 키워드 매칭으로 검색해 마크다운으로 출력한다.
LLM을 호출하지 않는다 — 순수 로컬 검색.

lib/rag.ts의 토큰 매칭 로직을 그대로 재사용한다 (hit count + 제목 가중치×2,
IDF 없음 — Phase 2에서 임베딩 하이브리드로 대체 예정).

사용법:
  python3 scripts/research-search.py --questions research/<id>/01-questions.md
  python3 scripts/research-search.py --query "군집 비행 위치 정밀도"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIRS = ["concepts", "entities", "comparisons", "queries"]
RAW_DIRS = ["raw/articles", "raw/notebooklm", "raw/papers", "raw/transcripts", "raw/web", "raw/youtube"]

TOKEN_RE = re.compile(r"[\s\n\r.,;:!?()\[\]{}\"'`/\\-]+")
STOPWORDS = {
    "이", "가", "을", "를", "은", "는", "의", "에", "와", "과", "도", "로",
    "에서", "그", "및", "등", "왜", "필요한가", "예상", "근거", "유형",
    "the", "a", "an", "of", "to", "in", "on", "for", "and", "or", "is", "are",
}


def tokenize(text: str) -> set[str]:
    toks = {t.lower() for t in TOKEN_RE.split(text) if len(t) > 1}
    return toks - STOPWORDS


def parse_frontmatter(raw: str) -> tuple[dict, str]:
    """Minimal frontmatter parser — no pyyaml dependency (matches repo convention
    in scripts/add-domain-tags.py). Handles scalar, flow-list [a, b], and
    block-list (- item) forms."""
    if not raw.startswith("---"):
        return {}, raw
    end = raw.find("\n---", 3)
    if end == -1:
        return {}, raw
    fm_block = raw[3:end].strip("\n")
    body = raw[end + 4:].lstrip("\n")

    data: dict = {}
    lines = fm_block.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [v.strip() for v in inner.split(",") if v.strip()] if inner else []
            i += 1
        elif val == "":
            items = []
            j = i + 1
            while j < len(lines) and re.match(r"^\s*-\s+", lines[j]):
                items.append(re.sub(r"^\s*-\s+", "", lines[j]).strip())
                j += 1
            if items:
                data[key] = items
                i = j
            else:
                data[key] = ""
                i += 1
        else:
            data[key] = val.strip('"')
            i += 1
    return data, body


def load_canonical_docs() -> list[dict]:
    docs = []
    for d in CANONICAL_DIRS:
        dirpath = WIKI_ROOT / d
        if not dirpath.exists():
            continue
        for f in sorted(dirpath.glob("*.md")):
            try:
                raw = f.read_text(encoding="utf-8")
            except Exception:
                continue
            fm, body = parse_frontmatter(raw)
            if not fm.get("title"):
                continue
            docs.append({
                "slug": f.stem,
                "path": str(f.relative_to(WIKI_ROOT)),
                "title": fm.get("title", f.stem),
                "tags": fm.get("tags", []) if isinstance(fm.get("tags", []), list) else [],
                "layer": d,
                "content": body,
            })
    return docs


def score_doc(query_tokens: set[str], doc: dict) -> int:
    body_tokens = tokenize(f"{doc['title']} {' '.join(doc['tags'])} {doc['content']}")
    title_tokens = tokenize(doc["title"])
    hits = len(query_tokens & body_tokens)
    title_hits = len(query_tokens & title_tokens)
    return hits + title_hits * 2


def search_canonical(query_tokens: set[str], top_k: int = 5) -> list[dict]:
    docs = load_canonical_docs()
    scored = [(score_doc(query_tokens, d), d) for d in docs]
    scored = [s for s in scored if s[0] > 0]
    scored.sort(key=lambda x: -x[0])
    results = []
    for s, d in scored[:top_k]:
        # 제목만 보여주면 LLM이 제목 재진술 이상의 클레임을 만들 근거가 없다
        # (실사용 테스트에서 canonical 클레임이 title 패러프레이즈 수준에
        # 그치는 문제를 발견 — 본문 발췌를 추가해 실제 내용을 근거로 삼게 함).
        excerpt = re.sub(r"^#[^\n]*\n", "", d["content"].lstrip(), count=1).strip()[:900]
        results.append({"score": s, "excerpt": excerpt, **d})
    return results


def search_raw(query_tokens: set[str], top_k: int = 5) -> list[dict]:
    hits = []
    for d in RAW_DIRS:
        dirpath = WIKI_ROOT / d
        if not dirpath.exists():
            continue
        for f in sorted(dirpath.rglob("*.md")):
            try:
                text = f.read_text(encoding="utf-8")
            except Exception:
                continue
            toks = tokenize(text)
            score = len(query_tokens & toks)
            if score > 0:
                # 400자는 frontmatter만 보여주고 본문은 잘려나가는 경우가 실사용
                # 테스트에서 확인됨(예: 파일 56번째 줄의 관련 내용을 LLM이 못 봄).
                # 900자로 확장 — 여전히 전체 문서 검증을 대체하지 못하는 절단임을
                # 인지할 것 (Phase 2 임베딩 검색 전까지의 임시 완화).
                snippet = text[:900].replace("\n", " ").strip()
                hits.append({"score": score, "path": str(f.relative_to(WIKI_ROOT)), "snippet": snippet})
    hits.sort(key=lambda x: -x["score"])
    return hits[:top_k]


def search_news(query_tokens: set[str], top_k: int = 4) -> list[dict]:
    feed_path = WIKI_ROOT / ".ua" / "news-feed.json"
    if not feed_path.exists():
        return []
    try:
        items = json.loads(feed_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    scored = []
    for it in items[:300]:
        text = f"{it.get('title', '')} {it.get('summary', '')}"
        score = len(query_tokens & tokenize(text))
        if score > 0:
            scored.append((score, it))
    scored.sort(key=lambda x: -x[0])
    return [{"score": s, "title": it.get("title"), "url": it.get("url"), "summary": it.get("summary", "")[:200]}
            for s, it in scored[:top_k]]


def load_graph() -> dict:
    for p in [WIKI_ROOT / ".ua" / "knowledge-graph.json", WIKI_ROOT / "knowledge-graph.json"]:
        if p.exists():
            try:
                return json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                continue
    return {"nodes": [], "edges": []}


def expand_neighbors(seed_slugs: list[str], limit: int = 6) -> list[str]:
    graph = load_graph()
    edges = graph.get("edges", graph.get("links", []))
    seed_set = set(seed_slugs)
    neighbors = set()
    for e in edges:
        src, tgt = str(e.get("source", "")), str(e.get("target", ""))
        if src in seed_set and tgt not in seed_set:
            neighbors.add(tgt)
        if tgt in seed_set and src not in seed_set:
            neighbors.add(src)
    return sorted(neighbors)[:limit]


def extract_questions(questions_md: Path) -> list[str]:
    text = questions_md.read_text(encoding="utf-8")
    qs = re.findall(r"^##\s*Q\d+:\s*(.+)$", text, re.MULTILINE)
    return qs if qs else [text]


def format_report(query_label: str, canonical_hits: list[dict], raw_hits: list[dict],
                   news_hits: list[dict], neighbors: list[str]) -> str:
    lines = [f"### 검색: {query_label}", ""]
    lines.append("**canonical 검색 결과**")
    if canonical_hits:
        for h in canonical_hits:
            lines.append(f"- [{h['score']}] `{h['path']}` — {h['title']} (slug: `{h['slug']}`, layer: {h['layer']})")
            lines.append(f"  발췌: {h['excerpt']}")
    else:
        lines.append("- (매칭 없음)")
    lines.append("")
    lines.append("**raw 검색 결과**")
    if raw_hits:
        for h in raw_hits:
            lines.append(f"- [{h['score']}] `{h['path']}` — {h['snippet']}")
    else:
        lines.append("- (매칭 없음)")
    lines.append("")
    lines.append("**뉴스 검색 결과**")
    if news_hits:
        for h in news_hits:
            lines.append(f"- [{h['score']}] {h['title']} — {h['url']}")
    else:
        lines.append("- (매칭 없음)")
    lines.append("")
    if neighbors:
        lines.append("**그래프 인접 슬러그** (1-hop): " + ", ".join(f"`{n}`" for n in neighbors))
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", type=Path, help="01-questions.md 경로 — Q1/Q2... 단위로 개별 검색")
    ap.add_argument("--query", type=str, help="단일 질의 문자열")
    ap.add_argument("--top-k", type=int, default=5)
    args = ap.parse_args()

    if not args.questions and not args.query:
        print("ERROR: --questions 또는 --query 중 하나는 필수", file=sys.stderr)
        return 1

    queries = extract_questions(args.questions) if args.questions else [args.query]

    print("# 기계 검색 결과 (Retriever — LLM 미사용)\n")
    for q in queries:
        q_tokens = tokenize(q)
        canonical_hits = search_canonical(q_tokens, args.top_k)
        raw_hits = search_raw(q_tokens, args.top_k)
        news_hits = search_news(q_tokens, 4)
        seed_slugs = [h["slug"] for h in canonical_hits]
        neighbors = expand_neighbors(seed_slugs) if seed_slugs else []
        print(format_report(q, canonical_hits, raw_hits, news_hits, neighbors))

    return 0


if __name__ == "__main__":
    sys.exit(main())
