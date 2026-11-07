#!/usr/bin/env python3
"""fetch-topic-sources.py — 주제 메뉴를 채우기 위한 추가 뉴스 수집기(2026-11-07). 설정: scripts/news-topic-sources.json.

· 표준 라이브러리만 사용(RSS 2.0·Atom). 소스별 최대 건수·include 정규식 필터. 한 소스가 실패해도 나머지는 계속(fail-open).
· 항목은 news-feed-append.py 로 병합한다(URL·제목 중복 제거, 주제 분류 포함). inbox(위키 컴파일)에는 쓰지 않는다.
· arXiv API 는 호출 간 3.1초 간격(공식 권고). GitHub 릴리즈는 atom 피드를 쓴다.
사용: python3 scripts/fetch-topic-sources.py [--dry-run] [--only slug,slug]
"""
from __future__ import annotations
import argparse
import html
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONFIG = HERE / "news-topic-sources.json"
APPEND = HERE / "news-feed-append.py"
UA = "Mozilla/5.0 (compatible; 2ndBrainTopicFetcher/1.0)"
ARXIV_DELAY = 3.1


def source_url(spec_url: str) -> str:
    """`arxiv:<검색식>` → arXiv API URL, 그 밖에는 그대로."""
    if spec_url.startswith("arxiv:"):
        q = spec_url[len("arxiv:"):]
        return "https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(q) + "&sortBy=submittedDate&sortOrder=descending&max_results=10"
    return spec_url


def _tag(e) -> str:
    return e.tag.split("}")[-1]


def _clean(s: str, n: int) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()[:n]


def parse_feed(data: bytes) -> list[dict]:
    """RSS 2.0 / Atom → [{title, url, summary, published}]. 해석할 수 없으면 ValueError."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise ValueError("BAD_XML") from exc
    out = []
    for e in root.iter():
        if _tag(e) not in ("item", "entry"):
            continue
        row = {"title": "", "url": "", "summary": "", "published": ""}
        for c in e:
            t = _tag(c)
            if t == "title":
                row["title"] = _clean(c.text or "", 200)
            elif t == "link":
                row["url"] = (c.attrib.get("href") or c.text or "").strip() or row["url"]
            elif t in ("description", "summary", "content") and not row["summary"]:
                row["summary"] = _clean(c.text or "", 200)
            elif t in ("pubDate", "published", "updated") and not row["published"]:
                row["published"] = _clean(c.text or "", 40)
        if row["title"] and row["url"]:
            out.append(row)
    return out


def select(entries: list[dict], spec: dict) -> list[dict]:
    rx = re.compile(spec["include"], re.I) if spec.get("include") else None
    picked = []
    for en in entries:
        if rx and not rx.search(en["title"] + " " + en["summary"]):
            continue
        picked.append(en)
        if len(picked) >= int(spec.get("max", 3)):
            break
    return picked


def to_items(picked: list[dict], spec: dict) -> list[dict]:
    items = []
    for en in picked:
        host = urllib.parse.urlparse(en["url"]).netloc or spec["slug"]
        title = en["title"]
        if spec["type"] == "release" and not re.search(r"릴리즈|release", title, re.I):
            title = f"{spec['slug'].replace('-release', '')} {title} 릴리즈"
        items.append({"title": title, "url": en["url"], "source": host, "domain": spec["domain"], "type": spec["type"],
                      "region": "global", "summary": en["summary"], "published": en["published"]})
    return items


def fetch(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # 인증서 검증 유지
        return r.read()


def collect(specs: list[dict], fetcher=fetch, sleep=time.sleep) -> tuple[list[dict], dict]:
    items, stat = [], {"ok": 0, "failed": 0, "items": 0}
    last_arxiv = 0.0
    for spec in specs:
        if spec["url"].startswith("arxiv:"):
            wait = ARXIV_DELAY - (time.monotonic() - last_arxiv)
            if last_arxiv and wait > 0:
                sleep(wait)
            last_arxiv = time.monotonic()
        try:
            got = to_items(select(parse_feed(fetcher(source_url(spec["url"]))), spec), spec)
        except Exception as exc:  # noqa: BLE001 — 소스 하나의 실패가 전체를 막지 않는다
            stat["failed"] += 1
            print(f"  ⚠️  {spec['slug']}: {type(exc).__name__}", file=sys.stderr)
            continue
        stat["ok"] += 1
        stat["items"] += len(got)
        items.extend(got)
    return items, stat


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true", help="병합하지 않고 수집 결과만 표시")
    ap.add_argument("--only", help="쉼표로 구분한 slug 만")
    a = ap.parse_args(argv)
    specs = json.loads(CONFIG.read_text(encoding="utf-8"))["sources"]
    if a.only:
        want = set(a.only.split(","))
        specs = [s for s in specs if s["slug"] in want]
    items, stat = collect(specs)
    print(f"topic-sources: 소스 {stat['ok']}개 성공 · {stat['failed']}개 실패 · 항목 {stat['items']}건")
    if a.dry_run:
        for it in items[:12]:
            print(f"  [{it['type']}/{it['domain']}] {it['title'][:70]}")
        return 0
    if items:
        r = subprocess.run([sys.executable, str(APPEND)], input=json.dumps(items, ensure_ascii=False), text=True, capture_output=True)
        print((r.stdout or "").strip() or (r.stderr or "").strip()[:200])
        return r.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
