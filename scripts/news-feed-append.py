#!/usr/bin/env python3
"""news-feed-append.py — stdin으로 뉴스 아이템 JSON 배열을 받아 news-feed.json에 병합.

아이템 스키마: {title, url, source, domain, type(news|release), summary, published}
- URL 기준 중복 제거 (기존 항목 유지)
- fetched(수집 시각) 자동 부여, 최신순 정렬, 최대 500개 유지
사용: echo '[{...}]' | python3 news-feed-append.py
"""
import json
import sys
import os
from datetime import datetime, timezone

FEED_PATH = os.path.expanduser("~/2nd/.ua/news-feed.json")
MAX_ITEMS = 500

def main():
    try:
        incoming = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"news-feed-append: 잘못된 JSON 입력 — {e}", file=sys.stderr)
        sys.exit(1)
    if not isinstance(incoming, list):
        incoming = [incoming]

    existing = []
    if os.path.exists(FEED_PATH):
        try:
            existing = json.load(open(FEED_PATH))
        except (json.JSONDecodeError, OSError):
            existing = []

    seen = {it.get("url") for it in existing}
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    added = 0
    for it in incoming:
        url = it.get("url", "").strip()
        if not url or url in seen:
            continue
        it.setdefault("fetched", now)
        it.setdefault("type", "news")
        existing.append(it)
        seen.add(url)
        added += 1

    existing.sort(key=lambda x: x.get("fetched", ""), reverse=True)
    existing = existing[:MAX_ITEMS]

    os.makedirs(os.path.dirname(FEED_PATH), exist_ok=True)
    with open(FEED_PATH, "w") as f:
        json.dump(existing, f, ensure_ascii=False, indent=1)
    print(f"news-feed: +{added}개 (총 {len(existing)}개)")

if __name__ == "__main__":
    main()
