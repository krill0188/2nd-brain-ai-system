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

    ~/2nd/.venv/bin/python scripts/embed-docs.py --if-stale
    python3 scripts/embed-docs.py --check  # 0=fresh, 2=stale; no model required

기본 모델 로드는 기존 로컬 캐시만 사용한다. 최초 무료 모델 다운로드는
명시적인 --allow-download 옵션으로만 허용한다.
캐시가 없거나 생성이 실패하면 기존 산출물을 보존하고 비정상 종료한다.

이 스크립트는 raw/canonical을 읽기만 한다 — 절대 쓰지 않는다.
산출물은 .ua/embeddings.json이며, 동시 실행 제어용 .ua/embeddings.lock을 사용한다.
산출물은 knowledge-graph.json과
동일하게 "파생 상태"로 취급한다(.gitignore의 .ua/ 규칙과 정합).
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import math
import os
import tempfile
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


def input_fingerprint(docs: list[dict]) -> str:
    """Hash exact model inputs and identities; no source text is written to output."""
    data = {"model": MODEL_NAME, "max_chars": MAX_CHARS, "docs": docs}
    return hashlib.sha256(json.dumps(data, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def generation_contract() -> dict:
    """Inspect installed metadata without importing/loading the embedding model."""
    version = 'unavailable'
    for metadata in sorted((WIKI_ROOT / '.venv/lib').glob('python*/site-packages/fastembed-*.dist-info/METADATA')):
        match = re.search(r'^Version: (.+)$', metadata.read_text(), re.MULTILINE)
        if match:
            version = match.group(1)
    return {'model': MODEL_NAME, 'fastembed': version, 'max_chars': MAX_CHARS, 'input_format': 1}


def document_fingerprint(doc: dict) -> str:
    # News list positions can change without changing its embedding input.
    value = {key: val for key, val in doc.items() if key != 'slug'}
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def reusable_vectors() -> dict:
    try:
        old = json.loads(OUT_PATH.read_text())
        if old.get('generation_contract') != generation_contract():
            return {}
        return {row['input_hash']: row['vector'] for row in old['docs']
                if 'input_hash' in row and len(row['vector']) == 768
                and all(isinstance(v, (float, int)) and math.isfinite(v) for v in row['vector'])}
    except (OSError, ValueError, KeyError, TypeError):
        return {}


def artifact_is_fresh(docs: list[dict], fingerprint: str) -> bool:
    """Reject incomplete, corrupt or stale output before skipping generation."""
    try:
        data = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        rows = data["docs"]
        return (data.get("input_fingerprint") == fingerprint
                and data.get('generation_contract') == generation_contract()
                and data["model"] == MODEL_NAME and data["dim"] == 768
                and data["doc_count"] == len(docs) == len(rows)
                and [r["path"] for r in rows] == [d["path"] for d in docs]
                and all(len(r["vector"]) == 768
                        and all(isinstance(v, (int, float)) and math.isfinite(v) for v in r["vector"])
                        for r in rows))
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return False


def atomic_write(payload: dict) -> None:
    """Only replace the last good artifact after a complete JSON write."""
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".embeddings-", suffix=".json", dir=OUT_PATH.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, allow_nan=False)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, OUT_PATH)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="read-only freshness check; stale exits 2")
    mode.add_argument("--if-stale", action="store_true", help="skip model loading when inputs are unchanged")
    parser.add_argument("--allow-download", action="store_true", help="explicit one-off free model download; default is cached-only")
    args = parser.parse_args()
    if args.check:
        return generate(args)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.with_suffix('.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('BLOCKED: 임베딩 생성 실행 중 — 기존 산출물 보존')
            return 2
        return generate(args)


def generate(args) -> int:
    """Collect a stable input set and atomically replace the derived vectors."""
    t0 = time.time()
    canonical = collect_canonical()
    raw = collect_raw()
    news = collect_news()
    all_docs = canonical + raw + news
    print(f"수집: canonical {len(canonical)} / raw {len(raw)} / news {len(news)} = 총 {len(all_docs)}건")

    fingerprint = input_fingerprint(all_docs)
    fresh = artifact_is_fresh(all_docs, fingerprint)
    if args.check:
        print("FRESH" if fresh else "STALE")
        return 0 if fresh else 2
    if args.if_stale and fresh:
        print("FRESH — 모델 실행 생략")
        return 0

    if not all_docs:
        print("임베딩할 문서 없음 — 종료")
        return 0

    cached = reusable_vectors()
    pending = [d for d in all_docs if document_fingerprint(d) not in cached]
    print(f'재사용 {len(all_docs) - len(pending)} / 재계산 {len(pending)}')
    t1 = time.time()
    if pending:
        try:
            from fastembed import TextEmbedding
            model = TextEmbedding(MODEL_NAME, local_files_only=not args.allow_download, threads=2)
            for i, (doc, vector) in enumerate(zip(pending, model.embed([d['text'] for d in pending], batch_size=8))):
                cached[document_fingerprint(doc)] = vector
                if (i + 1) % 40 == 0:
                    print(f'계산 진행 {i + 1}/{len(pending)}', flush=True)
        except Exception:
            print('ERROR: 모델 계산 실패 — 기존 임베딩 보존', file=sys.stderr)
            return 1
    if any(document_fingerprint(doc) not in cached for doc in all_docs):
        print('ERROR: 누락된 벡터 — 기존 파일 보존', file=sys.stderr)
        return 1
    vectors = [cached[document_fingerprint(d)] for d in all_docs]
    print(f"임베딩 생성: {round(time.time() - t1, 1)}초 ({len(vectors)}건)")

    if len(vectors) != len(all_docs) or any(
        len(v) != 768 or not all(math.isfinite(float(x)) for x in v) for v in vectors
    ):
        print("ERROR: 임베딩 개수/차원/수치 검증 실패 — 기존 파일 보존", file=sys.stderr)
        return 1
    # Concurrent knowledge edits must not be stamped as a fresh snapshot.
    if input_fingerprint(collect_canonical() + collect_raw() + collect_news()) != fingerprint:
        print("ERROR: 생성 중 입력 변경 — 기존 임베딩 보존", file=sys.stderr)
        return 1

    out_docs = []
    for d, v in zip(all_docs, vectors):
        out_docs.append({
            "kind": d["kind"], "layer": d["layer"], "slug": d["slug"],
            "path": d["path"], "title": d["title"],
            "input_hash": document_fingerprint(d),
            "vector": [round(float(x), 6) for x in v],
        })

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": 1,
        "input_fingerprint": fingerprint,
        "generation_contract": generation_contract(),
        "model": MODEL_NAME,
        "dim": len(out_docs[0]["vector"]) if out_docs else 0,
        "created": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "doc_count": len(out_docs),
        "docs": out_docs,
    }
    atomic_write(payload)
    size_mb = OUT_PATH.stat().st_size / 1024 / 1024
    print(f"저장 완료: {OUT_PATH} ({round(size_mb, 2)}MB, {len(out_docs)}건)")
    print(f"총 소요: {round(time.time() - t0, 1)}초")
    return 0


if __name__ == "__main__":
    sys.exit(main())
