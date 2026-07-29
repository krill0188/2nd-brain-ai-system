#!/usr/bin/env python3
"""
zotero-ingest.py — Zotero → raw/papers/<topic>/ 인제스트 스크립트
사용: python3 scripts/zotero-ingest.py [--topic <tag>] [--dry-run]

Zotero 로컬 API(http://localhost:23119)에서 신규 항목을 가져와
~/2nd/raw/papers/<topic>/ 에 Markdown 레코드를 생성한다.

요구사항:
  - Zotero 앱 실행 중
  - Zotero Settings → Advanced → "Allow other applications" 켜기
"""

import argparse
import datetime
import hashlib
import json
import re
import shutil
import sys
import urllib.request
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
RAW_PAPERS = WIKI_ROOT / "raw" / "papers"
ZOTERO_API = "http://localhost:23119/api"
ZOTERO_USER = "users/0"  # 로컬 모드 기본값

# SCHEMA.md 등록 드론 태그 → raw/papers/<topic>/ 매핑
TAG_MAP = {
    "drone-sw":      "drone-sw",
    "drone-ai":      "drone-ai",
    "datalink":      "datalink",
    "swarm":         "swarm",
    "drone-hw":      "drone-hw",
    "voice-control": "voice-control",
    "ai-agent":      "ai-agent",
    "drone":         "drone-sw",   # 일반 drone → drone-sw 기본
}


def zotero_get(path: str) -> dict | list:
    url = f"{ZOTERO_API}/{ZOTERO_USER}/{path}?format=json&limit=100"
    req = urllib.request.Request(url, headers={"Zotero-API-Version": "3"})
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.loads(r.read())


def resolve_topic(item_data: dict) -> str:
    """Zotero 태그에서 드론 토픽 결정. 매핑 없으면 _unclassified."""
    tags = [t.get("tag", "").lower() for t in item_data.get("tags", [])]
    for tag in tags:
        if tag in TAG_MAP:
            return TAG_MAP[tag]
    return "_unclassified"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80]


def sha256_str(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def build_markdown(item: dict) -> str:
    d = item.get("data", {})
    title = d.get("title", "Untitled")
    authors = "; ".join(
        f"{c.get('lastName', '')}, {c.get('firstName', '')}"
        for c in d.get("creators", [])
        if c.get("creatorType") == "author"
    ) or "Unknown"
    year = d.get("date", "")[:4] if d.get("date") else ""
    doi = d.get("DOI", "")
    url = d.get("url", "")
    abstract = d.get("abstractNote", "").strip()
    item_type = d.get("itemType", "journalArticle")
    tags_raw = [t.get("tag", "") for t in d.get("tags", [])]
    today = datetime.date.today().isoformat()
    zotero_key = item.get("key", "")

    lines = [
        "---",
        f"title: {json.dumps(title)}",
        f"created: {today}",
        f"updated: {today}",
        f"type: paper",
        f"item_type: {item_type}",
        f"authors: {json.dumps(authors)}",
        f"year: \"{year}\"",
        f"doi: \"{doi}\"",
        f"url: \"{url}\"",
        f"zotero_key: {zotero_key}",
        f"tags: {json.dumps(tags_raw)}",
        f"sha256: {sha256_str(title + authors + year)}",
        "---",
        "",
        f"# {title}",
        "",
        f"**Authors**: {authors}  ",
        f"**Year**: {year}  ",
        *([ f"**DOI**: {doi}  "] if doi else []),
        *([ f"**URL**: {url}"] if url else []),
        "",
    ]
    if abstract:
        lines += ["## Abstract", "", abstract, ""]
    lines += [
        "## Notes",
        "",
        "<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->",
        "",
    ]
    return "\n".join(lines)


def ingest(dry_run: bool = False, topic_filter: str | None = None) -> None:
    # Zotero 연결 확인
    try:
        items = zotero_get("items?itemType=-attachment")
    except Exception as e:
        print(f"[ERROR] Zotero 로컬 API 연결 실패: {e}")
        print("  → Zotero 앱을 실행하고 Settings → Advanced → 'Allow other applications' 활성화 필요")
        sys.exit(1)

    if not isinstance(items, list):
        items = items.get("items", [])

    new_count = 0
    skip_count = 0

    for item in items:
        d = item.get("data", {})
        if d.get("itemType") == "attachment":
            continue

        topic = resolve_topic(d)
        if topic_filter and topic != topic_filter:
            continue

        title = d.get("title", "Untitled")
        slug = slugify(title)
        out_dir = RAW_PAPERS / topic
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{slug}.md"

        if out_file.exists():
            skip_count += 1
            continue

        md = build_markdown(item)

        if dry_run:
            print(f"[DRY-RUN] → {out_file.relative_to(WIKI_ROOT)}")
        else:
            out_file.write_text(md, encoding="utf-8")
            # inbox에도 복사 → 다음 04:00 cron이 위키 canonical로 컴파일
            inbox_file = WIKI_ROOT / "inbox" / f"zotero-{slug}.md"
            if not inbox_file.exists() and not (WIKI_ROOT / "inbox" / "processed" / f"zotero-{slug}.md").exists():
                inbox_file.write_text(md, encoding="utf-8")
            print(f"[OK] → {out_file.relative_to(WIKI_ROOT)} (+inbox)")
        new_count += 1

    print(f"\n수집 완료: 신규 {new_count}개 | 기존 스킵 {skip_count}개")
    if topic_filter:
        print(f"필터: {topic_filter}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zotero → raw/papers/<topic>/ 인제스트")
    parser.add_argument("--topic", help="특정 토픽만 수집 (예: drone-sw)")
    parser.add_argument("--dry-run", action="store_true", help="파일 쓰기 없이 미리보기")
    args = parser.parse_args()
    ingest(dry_run=args.dry_run, topic_filter=args.topic)
