#!/usr/bin/env python3
"""
research-search.py — 연구 루프의 기계적(비-LLM) 검색 단계 (Retriever).

canonical(entities/concepts/comparisons/queries) + raw/ + news-feed.json +
knowledge-graph.json 이웃 확장을 검색해 마크다운으로 출력한다. LLM을
호출하지 않는다 — 순수 로컬 검색(+ 로컬 임베딩 모델 subprocess 호출).

lib/rag.ts의 키워드 스코어링 로직(hit count + 제목 가중치×2)을 기본값으로
재사용하고, Phase 2부터 `.ua/embeddings.json`(scripts/embed-docs.py 산출)이
있으면 코사인 유사도를 결합한 하이브리드 점수로 전환한다. embeddings.json이
없거나 venv가 없으면 기존 키워드 전용 방식으로 자동 폴백한다(무회귀 보장).

사용법:
  python3 scripts/research-search.py --questions research/<id>/01-questions.md
  python3 scripts/research-search.py --query "군집 비행 위치 정밀도"
"""
from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIRS = ["concepts", "entities", "comparisons", "queries"]
RAW_DIRS = ["raw/articles", "raw/notebooklm", "raw/papers", "raw/transcripts", "raw/web", "raw/youtube"]
VENV_PYTHON = WIKI_ROOT / ".venv" / "bin" / "python"
EMBEDDINGS_PATH = WIKI_ROOT / ".ua" / "embeddings.json"
EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
HYBRID_VECTOR_WEIGHT = 0.6
HYBRID_KEYWORD_WEIGHT = 0.4
MIN_COSINE_INCLUDE = 0.35  # 키워드 겹침이 0이어도 이 이상이면 결과에 포함 (교차언어 검색 목적)

TOKEN_RE = re.compile(r"[\s\n\r.,;:!?()\[\]{}\"'`/\\-]+")
STOPWORDS = {
    "이", "가", "을", "를", "은", "는", "의", "에", "와", "과", "도", "로",
    "에서", "그", "및", "등", "왜", "필요한가", "예상", "근거", "유형",
    "the", "a", "an", "of", "to", "in", "on", "for", "and", "or", "is", "are",
}


def tokenize(text: str) -> set[str]:
    toks = {t.lower() for t in TOKEN_RE.split(text) if len(t) > 1}
    return toks - STOPWORDS


_EMBEDDINGS_CACHE: dict[str, list[float]] | None = None


def load_embeddings() -> dict[str, list[float]]:
    """path -> vector 매핑. embed-docs.py 산출물이 없으면 빈 dict(=키워드 폴백)."""
    global _EMBEDDINGS_CACHE
    if _EMBEDDINGS_CACHE is not None:
        return _EMBEDDINGS_CACHE
    if not EMBEDDINGS_PATH.exists():
        _EMBEDDINGS_CACHE = {}
        return _EMBEDDINGS_CACHE
    try:
        data = json.loads(EMBEDDINGS_PATH.read_text(encoding="utf-8"))
        _EMBEDDINGS_CACHE = {d["path"]: d["vector"] for d in data.get("docs", [])}
    except Exception:
        _EMBEDDINGS_CACHE = {}
    return _EMBEDDINGS_CACHE


def cosine(a: list[float], b: list[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def embed_queries(queries: list[str]) -> list[list[float] | None]:
    """~/2nd/.venv (fastembed 설치됨)를 subprocess로 호출해 질의 임베딩을
    일괄 생성한다. venv가 없거나 실패하면 전부 None — 호출측은 키워드
    전용으로 폴백해야 한다. 절대 예외를 상위로 전파하지 않는다."""
    if not VENV_PYTHON.exists():
        return [None] * len(queries)
    script = (
        "import sys, json\n"
        "from fastembed import TextEmbedding\n"
        "queries = json.load(sys.stdin)\n"
        f"m = TextEmbedding({EMBED_MODEL!r})\n"
        "vecs = list(m.embed(queries))\n"
        "print(json.dumps([[float(x) for x in v] for v in vecs]))\n"
    )
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), "-c", script],
            input=json.dumps(queries), capture_output=True, text=True, timeout=90,
        )
        if result.returncode != 0 or not result.stdout.strip():
            return [None] * len(queries)
        # fastembed가 stderr가 아닌 stdout에 경고를 섞을 수 있어 마지막 줄만 파싱
        return json.loads(result.stdout.strip().splitlines()[-1])
    except Exception:
        return [None] * len(queries)


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


def keyword_score(query_tokens: set[str], title: str, tags: list[str], content: str) -> int:
    body_tokens = tokenize(f"{title} {' '.join(tags)} {content}")
    title_tokens = tokenize(title)
    hits = len(query_tokens & body_tokens)
    title_hits = len(query_tokens & title_tokens)
    return hits + title_hits * 2


def hybrid_score(kw_score: int, query_tokens: set[str], query_vec: list[float] | None,
                  doc_path: str, embeddings: dict[str, list[float]]) -> tuple[float, float]:
    """반환: (정렬용 최종 점수, 표시용 코사인 유사도 0이면 임베딩 미사용)"""
    kw_norm = kw_score / max(len(query_tokens), 1)
    if query_vec is None or doc_path not in embeddings:
        return float(kw_score), 0.0  # 폴백: 기존 정수 키워드 점수 그대로 (하위호환)
    cos = cosine(query_vec, embeddings[doc_path])
    return HYBRID_VECTOR_WEIGHT * cos + HYBRID_KEYWORD_WEIGHT * kw_norm, cos


def search_canonical(query_tokens: set[str], top_k: int = 5,
                      query_vec: list[float] | None = None) -> list[dict]:
    docs = load_canonical_docs()
    embeddings = load_embeddings()
    scored = []
    for d in docs:
        kw = keyword_score(query_tokens, d["title"], d["tags"], d["content"])
        final, cos = hybrid_score(kw, query_tokens, query_vec, d["path"], embeddings)
        # 키워드 0건이어도 의미 유사도가 충분하면 포함 — 교차언어("군집 비행" ↔
        # swarm-coordination) 검색 실패를 고치는 것이 Phase 2의 핵심 목적.
        if kw > 0 or cos >= MIN_COSINE_INCLUDE:
            scored.append((final, cos, d))
    scored.sort(key=lambda x: -x[0])
    results = []
    for final, cos, d in scored[:top_k]:
        # 제목만 보여주면 LLM이 제목 재진술 이상의 클레임을 만들 근거가 없다
        # (실사용 테스트에서 canonical 클레임이 title 패러프레이즈 수준에
        # 그치는 문제를 발견 — 본문 발췌를 추가해 실제 내용을 근거로 삼게 함).
        excerpt = re.sub(r"^#[^\n]*\n", "", d["content"].lstrip(), count=1).strip()[:900]
        results.append({"score": round(final, 3), "cosine": round(cos, 3), "excerpt": excerpt, **d})
    return results


def search_raw(query_tokens: set[str], top_k: int = 5,
                query_vec: list[float] | None = None) -> list[dict]:
    embeddings = load_embeddings()
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
            kw = len(query_tokens & toks)
            rel_path = str(f.relative_to(WIKI_ROOT))
            final, cos = hybrid_score(kw, query_tokens, query_vec, rel_path, embeddings)
            if kw > 0 or cos >= MIN_COSINE_INCLUDE:
                # 400자는 frontmatter만 보여주고 본문은 잘려나가는 경우가 실사용
                # 테스트에서 확인됨(예: 파일 56번째 줄의 관련 내용을 LLM이 못 봄).
                # 900자로 확장 — 여전히 전체 문서 검증을 대체하지 못하는 절단임을
                # 인지할 것.
                snippet = text[:900].replace("\n", " ").strip()
                hits.append({"score": round(final, 3), "cosine": round(cos, 3), "path": rel_path, "snippet": snippet})
    hits.sort(key=lambda x: -x["score"])
    return hits[:top_k]


def search_news(query_tokens: set[str], top_k: int = 4,
                 query_vec: list[float] | None = None) -> list[dict]:
    feed_path = WIKI_ROOT / ".ua" / "news-feed.json"
    if not feed_path.exists():
        return []
    try:
        items = json.loads(feed_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    embeddings = load_embeddings()
    scored = []
    for it in items[:300]:
        text = f"{it.get('title', '')} {it.get('summary', '')}"
        kw = len(query_tokens & tokenize(text))
        url = it.get("url", "")  # embed-docs.py는 news 문서의 path로 url을 사용
        final, cos = hybrid_score(kw, query_tokens, query_vec, url, embeddings)
        if kw > 0 or cos >= MIN_COSINE_INCLUDE:
            scored.append((final, it))
    scored.sort(key=lambda x: -x[0])
    return [{"score": round(s, 3), "title": it.get("title"), "url": it.get("url"), "summary": it.get("summary", "")[:200]}
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
            cos_note = f", cos={h['cosine']}" if h.get("cosine") else ""
            lines.append(f"- [{h['score']}{cos_note}] `{h['path']}` — {h['title']} (slug: `{h['slug']}`, layer: {h['layer']})")
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

    # 질의 임베딩을 세션당 1회 배치로 생성 (venv 모델 로드 비용을 질문 수만큼
    # 반복하지 않기 위함). embeddings.json이나 venv가 없으면 전부 None —
    # 이후 검색 함수들이 자동으로 키워드 전용 방식으로 폴백한다.
    hybrid_enabled = EMBEDDINGS_PATH.exists() and VENV_PYTHON.exists()
    query_vecs = embed_queries(queries) if hybrid_enabled else [None] * len(queries)
    if hybrid_enabled and all(v is None for v in query_vecs):
        print("# (참고: 임베딩 모델 호출 실패 — 키워드 전용 검색으로 폴백)\n", file=sys.stderr)

    print("# 기계 검색 결과 (Retriever — LLM 미사용, 하이브리드: "
          f"{'ON' if hybrid_enabled else 'OFF(키워드 전용)'})\n")
    for q, qvec in zip(queries, query_vecs):
        q_tokens = tokenize(q)
        canonical_hits = search_canonical(q_tokens, args.top_k, qvec)
        raw_hits = search_raw(q_tokens, args.top_k, qvec)
        news_hits = search_news(q_tokens, 4, qvec)
        seed_slugs = [h["slug"] for h in canonical_hits]
        neighbors = expand_neighbors(seed_slugs) if seed_slugs else []
        print(format_report(q, canonical_hits, raw_hits, news_hits, neighbors))

    return 0


if __name__ == "__main__":
    sys.exit(main())
