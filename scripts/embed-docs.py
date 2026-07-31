#!/usr/bin/env python3
"""
embed-docs.py — Phase 2: canonical/raw/뉴스 문서를 다국어 임베딩으로 사전계산.

배경: TECHNOLOGY_DECISION_RECORD.md는 "BGE-M3" 채택을 권고했으나, 실제
채택 라이브러리(fastembed)의 내장 모델 목록에 BGE-M3가 없음을 실사용
검증 중 발견했다. 대체로 검증한
sentence-transformers/paraphrase-multilingual-mpnet-base-v2
(768차원, ~50개 언어)를 사용한다 — 한/영 교차 언어 유사도 실측 0.78 확인.

실행 환경: 시스템 Python(3.14)은 onnxruntime 미지원(휠 없음) → 격리된
~/2nd/.venv (Python 3.11)에서만 실행한다. 반드시 아래처럼 실행:

    ~/2nd/.venv/bin/python scripts/embed-docs.py

이 스크립트는 raw/canonical을 읽기만 한다 — 절대 쓰지 않는다.
출력은 .ua/embeddings.json 1개 파일뿐이며, 이는 knowledge-graph.json과
동일하게 "파생 상태"로 취급한다(.gitignore의 .ua/ 규칙과 정합).
"""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIRS = ["entities", "concepts", "comparisons", "queries"]
RAW_DIRS = ["raw/articles", "raw/notebooklm", "raw/papers", "raw/transcripts", "raw/web", "raw/youtube"]
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
MAX_CHARS = 2000  # 문서당 임베딩 입력 상한 (청킹 없이 전체 문서를 대표하는 앞부분만 사용 — Phase 2 범위 결정)
OUT_PATH = WIKI_ROOT / ".ua" / "embeddings.json"


def parse_frontmatter(raw: str) -> tuple[dict, str]:
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
        m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", lines[i])
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [v.strip() for v in inner.split(",") if v.strip()]
            i += 1
        elif val == "":
            items, j = [], i + 1
            while j < len(lines) and re.match(r"^\s*-\s+", lines[j]):
                items.append(re.sub(r"^\s*-\s+", "", lines[j]).strip())
                j += 1
            data[key] = items if items else ""
            i = j if items else i + 1
        else:
            data[key] = val.strip('"')
            i += 1
    return data, body


def collect_canonical() -> list[dict]:
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
            tags = fm.get("tags", [])
            tags = tags if isinstance(tags, list) else []
            text = f"{fm['title']}\n{' '.join(tags)}\n{body}"[:MAX_CHARS]
            docs.append({
                "kind": "canonical", "layer": d, "slug": f.stem,
                "path": str(f.relative_to(WIKI_ROOT)), "title": fm["title"], "text": text,
            })
    return docs


def collect_raw() -> list[dict]:
    docs = []
    for d in RAW_DIRS:
        dirpath = WIKI_ROOT / d
        if not dirpath.exists():
            continue
        for f in sorted(dirpath.rglob("*.md")):
            try:
                raw = f.read_text(encoding="utf-8")
            except Exception:
                continue
            fm, body = parse_frontmatter(raw)
            title = fm.get("title", f.stem) if isinstance(fm.get("title", f.stem), str) else f.stem
            text = f"{title}\n{body}"[:MAX_CHARS]
            docs.append({
                "kind": "raw", "layer": d, "slug": f.stem,
                "path": str(f.relative_to(WIKI_ROOT)), "title": title, "text": text,
            })
    return docs


def collect_news() -> list[dict]:
    feed_path = WIKI_ROOT / ".ua" / "news-feed.json"
    if not feed_path.exists():
        return []
    try:
        items = json.loads(feed_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    docs = []
    for i, it in enumerate(items[:300]):
        text = f"{it.get('title', '')}\n{it.get('summary', '')}"[:MAX_CHARS]
        if not text.strip():
            continue
        docs.append({
            "kind": "news", "layer": "news", "slug": f"news-{i}",
            "path": it.get("url", ""), "title": it.get("title", ""), "text": text,
        })
    return docs


def main() -> int:
    try:
        from fastembed import TextEmbedding
    except ImportError:
        print("ERROR: fastembed 미설치. ~/2nd/.venv/bin/python으로 실행했는지 확인하십시오.", file=sys.stderr)
        return 1

    t0 = time.time()
    canonical = collect_canonical()
    raw = collect_raw()
    news = collect_news()
    all_docs = canonical + raw + news
    print(f"수집: canonical {len(canonical)} / raw {len(raw)} / news {len(news)} = 총 {len(all_docs)}건")

    if not all_docs:
        print("임베딩할 문서 없음 — 종료")
        return 0

    model = TextEmbedding(MODEL_NAME)
    print(f"모델 로드: {round(time.time() - t0, 1)}초")

    t1 = time.time()
    texts = [d["text"] for d in all_docs]
    vectors = list(model.embed(texts))
    print(f"임베딩 생성: {round(time.time() - t1, 1)}초 ({len(vectors)}건)")

    out_docs = []
    for d, v in zip(all_docs, vectors):
        out_docs.append({
            "kind": d["kind"], "layer": d["layer"], "slug": d["slug"],
            "path": d["path"], "title": d["title"],
            "vector": [round(float(x), 6) for x in v],
        })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": 1,
        "model": MODEL_NAME,
        "dim": len(out_docs[0]["vector"]) if out_docs else 0,
        "created": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "doc_count": len(out_docs),
        "docs": out_docs,
    }
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    size_mb = OUT_PATH.stat().st_size / 1024 / 1024
    print(f"저장 완료: {OUT_PATH} ({round(size_mb, 2)}MB, {len(out_docs)}건)")
    print(f"총 소요: {round(time.time() - t0, 1)}초")
    return 0


if __name__ == "__main__":
    sys.exit(main())
