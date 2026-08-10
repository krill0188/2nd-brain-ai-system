#!/usr/bin/env python3
"""news-feed-append.py — stdin으로 뉴스 아이템 JSON 배열을 받아 news-feed.json에 병합.

아이템 스키마: {title, url, source, domain, type(news|release), summary, published}
- URL 기준 중복 제거 (기존 항목 유지)
- fetched(수집 시각) 자동 부여, 최신순 정렬, 최대 500개 유지
사용: echo '[{...}]' | python3 news-feed-append.py
"""
import hashlib
import json
import sys
import os
from datetime import datetime, timezone

FEED_PATH = os.path.expanduser("~/2nd/.ua/news-feed.json")
MAX_ITEMS = 500


def _title_key(title: str) -> str:
    return title.strip().lower()


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
    # Google News RSS는 같은 기사를 재수집할 때마다 다른 리다이렉트 URL을 발급한다
    # (다른 언론사가 같은 통신사 기사를 그대로 실은 경우도 제목이 동일) — URL만으로
    # 중복 제거하면 같은 기사가 여러 항목으로 쌓인다. 제목 기준 중복 제거를 추가한다
    # (2026-08-10: entities/sol-one.md 등 9개 canonical 문서에서 중복 삽입 발견).
    seen_titles = {_title_key(it.get("title", "")) for it in existing if it.get("title")}
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    added = 0
    for it in incoming:
        url = it.get("url", "").strip()
        title_key = _title_key(it.get("title", ""))
        if not url or url in seen:
            continue
        if title_key and title_key in seen_titles:
            continue
        it.setdefault("fetched", now)
        it.setdefault("type", "news")
        # 원문 무결성 해시 — 수집 시점의 제목+요약 원문 SHA-256 (변조 검증용)
        it.setdefault("sha256", hashlib.sha256(
            (it.get("title", "") + it.get("summary", "") + url).encode()).hexdigest())
        existing.append(it)
        seen.add(url)
        if title_key:
            seen_titles.add(title_key)
        added += 1

    existing.sort(key=lambda x: x.get("fetched", ""), reverse=True)
    existing = existing[:MAX_ITEMS]

    os.makedirs(os.path.dirname(FEED_PATH), exist_ok=True)
    with open(FEED_PATH, "w") as f:
        json.dump(existing, f, ensure_ascii=False, indent=1)
    print(f"news-feed: +{added}개 (총 {len(existing)}개)")

if __name__ == "__main__":
    main()
