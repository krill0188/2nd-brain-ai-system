#!/usr/bin/env bash
# fetch-inbox.sh — 드론 7개 도메인 지식을 외부 소스에서 수집해 inbox/에 저장
# 도메인: flight-control | comms-protocol | hardware | gcs-software | ops-mission | regulations | ai-autonomy
# 실행: ~/2nd/scripts/fetch-inbox.sh [--force]
# 의존: curl, python3 (RSS는 feedparser 있으면 사용, 없으면 stdlib 폴백)

set -euo pipefail
export PATH="$HOME/.local/bin:/usr/local/bin:$PATH"

INBOX="$HOME/2nd/inbox"
PROCESSED="$INBOX/processed"
SEEN_RSS="$PROCESSED/.rss-seen.txt"
TODAY=$(date +%Y-%m-%d)
FORCE="${1:-}"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) 2ndBrainFetcher/2.0"

mkdir -p "$PROCESSED"
touch "$SEEN_RSS"

already_fetched() {
  local cnt
  cnt=$(ls "$INBOX"/fetch-"$TODAY"-*.md 2>/dev/null | wc -l | tr -d ' ')
  [[ "$cnt" -gt 3 ]]
}

[[ -z "$FORCE" ]] && already_fetched && { echo "✅ 오늘 이미 수집됨 ($TODAY)"; exit 0; }

# 맥이 Power Nap(짧은 유지보수 웨이크업)으로 깼을 때 cron이 곧바로 실행되면
# 네트워크(DNS)가 아직 준비되기 전이라 이 스크립트의 모든 fetch가 통째로
# "nodename nor servname provided"로 실패한다(2026-08-11 03:30 실측 확인 —
# GitHub/arXiv/YouTube/Crossref/Federal Register/텔레그램 전송까지 전부 동시
# 실패). DNS 해석이 될 때까지 최대 60초 대기 후 진행 — 그래도 안 되면 그냥
# 진행한다(개별 fetch 함수들은 이미 실패를 흡수하고 다음으로 넘어가게 돼 있음).
wait_for_network() {
  local tries=0
  while (( tries < 12 )); do
    if curl -sf --max-time 4 -o /dev/null "https://export.arxiv.org"; then
      return 0
    fi
    tries=$((tries + 1))
    sleep 5
  done
  echo "⚠️  60초 대기했지만 네트워크 미준비 — 그대로 진행(개별 fetch는 각자 실패 처리됨)"
  return 1
}
wait_for_network || true  # set -e 보호: 네트워크 끝내 안 되도 스크립트는 계속 진행

echo "🔍 드론 7개 도메인 지식 수집 시작 ($TODAY)..."

# ── GitHub 최신 릴리즈 노트 수집 ─────────────────────────────────
fetch_github_release() {
  local repo="$1" slug="$2" domain="$3"
  local out="$INBOX/fetch-${TODAY}-${slug}.md"
  local data tag body published slug_lower safe_tag

  data=$(curl -sf --max-time 15 "https://api.github.com/repos/${repo}/releases/latest" 2>/dev/null) || return 0

  tag=$(echo "$data"       | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('tag_name',''))" 2>/dev/null)
  published=$(echo "$data" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('published_at','')[:10])" 2>/dev/null)
  body=$(echo "$data"      | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('body','')[:3000])" 2>/dev/null)

  [[ -z "$tag" || -z "$body" ]] && return 0

  safe_tag="${tag//\//-}"
  if ls "$PROCESSED/fetch-"*"-${slug}-${safe_tag}.md" 2>/dev/null | grep -q . || \
     ls "$PROCESSED/fetch-"*"-${slug}.md" 2>/dev/null | xargs grep -l "tag: ${tag}$" 2>/dev/null | grep -q .; then
    echo "  skip $slug $tag (already processed)"
    return 0
  fi

  slug_lower=$(echo "$slug" | tr '[:upper:]' '[:lower:]')
  local source_url="https://github.com/${repo}/releases/tag/${tag}"

  python3 - "$out" "$slug" "$tag" "$TODAY" "$published" "$slug_lower" "$source_url" "$domain" "$body" <<'PYEOF'
import sys
out_path, slug, tag, today, published, slug_lower, source_url, domain, body = sys.argv[1:]
content = (
    "---\n"
    f'title: "{slug} {tag} Release Notes"\n'
    f"created: {today}\n"
    f"captured: {today}\n"
    "type: release-note\n"
    f"tag: {tag}\n"
    f"domain: {domain}\n"
    f"source: {source_url}\n"
    f"tags: [drone, {domain}, {slug_lower}]\n"
    "---\n\n"
    f"# {slug} {tag} Release Notes ({published})\n\n"
    f"{body}\n"
)
with open(out_path, 'w') as f:
    f.write(content)

import json, subprocess
item = json.dumps([{
    "title": f"{slug} {tag} 릴리즈",
    "url": source_url,
    "source": "github.com",
    "domain": domain,
    "type": "release",
    "summary": body.strip().replace("\r", " ").replace("\n", " ")[:200],
    "published": published,
}], ensure_ascii=False)
subprocess.run(["python3", __import__('os').path.expanduser("~/2nd/scripts/news-feed-append.py")],
               input=item, text=True, capture_output=True)
PYEOF

  echo "  ✅ [$domain] $slug $tag → inbox/"
}

# ── RSS 피드 수집 (도메인별 뉴스/기사) ───────────────────────────
fetch_rss() {
  local url="$1" slug="$2" domain="$3" max_items="${4:-5}"
  local out="$INBOX/fetch-${TODAY}-rss-${slug}.md"

  python3 - "$url" "$slug" "$domain" "$max_items" "$out" "$TODAY" "$SEEN_RSS" "$UA" <<'PYEOF'
import sys, html, re
url, slug, domain, max_items, out_path, today, seen_path, ua = sys.argv[1:]
max_items = int(max_items)

entries = []
try:
    import feedparser
    d = feedparser.parse(url, agent=ua)
    for e in d.entries[:20]:
        summary = re.sub(r'<[^>]+>', '', e.get('summary', ''))[:600]
        entries.append({
            'title': e.get('title', '').strip(),
            'link': e.get('link', '').strip(),
            'date': (e.get('published', '') or e.get('updated', ''))[:32],
            'summary': html.unescape(summary).strip(),
        })
except ImportError:
    import urllib.request, xml.etree.ElementTree as ET
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    raw = urllib.request.urlopen(req, timeout=15).read()
    root = ET.fromstring(raw)
    for item in root.iter('item'):
        g = lambda t: (item.findtext(t) or '').strip()
        summary = re.sub(r'<[^>]+>', '', g('description'))[:600]
        entries.append({'title': g('title'), 'link': g('link'),
                        'date': g('pubDate')[:32],
                        'summary': html.unescape(summary).strip()})
except Exception as ex:
    print(f"  ⚠️  {slug} RSS 실패: {ex}", file=sys.stderr)
    sys.exit(0)

seen = set(open(seen_path).read().splitlines())
fresh = [e for e in entries if e['link'] and e['link'] not in seen][:max_items]
if not fresh:
    print(f"  skip {slug} (새 항목 없음)")
    sys.exit(0)

lines = [
    "---",
    f'title: "{slug} 최신 동향 ({today})"',
    f"created: {today}",
    f"captured: {today}",
    "type: news-digest",
    f"domain: {domain}",
    f"source: {url}",
    f"tags: [drone, {domain}, news]",
    "---",
    "",
    f"# {slug} 최신 동향 ({today})",
    "",
]
for e in fresh:
    lines.append(f"## {e['title']}")
    lines.append(f"- 링크: {e['link']}")
    if e['date']:
        lines.append(f"- 날짜: {e['date']}")
    if e['summary']:
        lines.append(f"\n{e['summary']}")
    lines.append("")

with open(out_path, 'w') as f:
    f.write("\n".join(lines))
with open(seen_path, 'a') as f:
    for e in fresh:
        f.write(e['link'] + "\n")

import subprocess, os, json
from urllib.parse import urlparse
items = json.dumps([{
    "title": e['title'],
    "url": e['link'],
    "source": urlparse(e['link']).hostname or slug,
    "domain": domain,
    "type": "news",
    "summary": e['summary'][:200],
    "published": e['date'],
} for e in fresh], ensure_ascii=False)
subprocess.run(["python3", os.path.expanduser("~/2nd/scripts/news-feed-append.py")],
               input=items, text=True, capture_output=True)
print(f"  ✅ [{domain}] {slug} 기사 {len(fresh)}건 → inbox/")
PYEOF
}

# ── flight-control ──────────────────────────────────────────────
fetch_github_release "PX4/PX4-Autopilot"       "px4"        "flight-control"
fetch_github_release "ArduPilot/ardupilot"     "ardupilot"  "flight-control"
fetch_github_release "betaflight/betaflight"   "betaflight" "flight-control"

# ── comms-protocol ──────────────────────────────────────────────
fetch_github_release "mavlink/mavlink"         "mavlink"    "comms-protocol"
fetch_github_release "dronecan/libcanard"      "dronecan"   "comms-protocol"
fetch_github_release "mavlink/MAVSDK"          "mavsdk"     "comms-protocol"
fetch_github_release "ArduPilot/pymavlink"     "pymavlink"  "comms-protocol"

# ── gcs-software ────────────────────────────────────────────────
fetch_github_release "mavlink/qgroundcontrol"  "qgroundcontrol" "gcs-software"
fetch_github_release "ArduPilot/MissionPlanner" "missionplanner" "gcs-software"
fetch_github_release "ros2/ros2"               "ros2"       "gcs-software"

# ── ai-autonomy ─────────────────────────────────────────────────
fetch_github_release "ultralytics/ultralytics" "yolo"       "ai-autonomy"
fetch_github_release "opencv/opencv"           "opencv"     "ai-autonomy"
fetch_github_release "PX4/PX4-Avoidance"       "px4-avoidance" "ai-autonomy"

# ── patents: USPTO 특허 데이터(PatentsView) — 무료 키 필요 ────────
# 키 발급: https://patentsview.org/apis/keyrequest (data.uspto.gov로 이관됨,
# 2026-08-02 curl로 리다이렉트 200 확인). .env에 USPTO_API_KEY=<키> 추가 시
# 활성화, 없으면 아래에서 자동 스킵. INNOVATION_ENGINE.md의 "Patent
# Candidate" 판정에 실제 근거 데이터를 처음으로 공급한다.
# ⚠️ search.patentsview.org/api/v1/patent/ 엔드포인트는 공개 문서 기준
# 구현이며, 이 세션에서는 키가 없어 실호출 검증을 못 했다 — 키 등록 후
# 1회 실행 결과를 확인해야 한다(마스터에게 보고 필수).
USPTO_KEY=$(grep '^USPTO_API_KEY=' "$HOME/2nd/.env" 2>/dev/null | cut -d= -f2 || true)
fetch_patents() {
  local key="$1" query="$2" domain="$3" max_items="${4:-5}"
  [[ -z "$key" ]] && { echo "  patents: USPTO_API_KEY 없음 — 스킵(발급: https://patentsview.org/apis/keyrequest)"; return 0; }

  python3 - "$key" "$query" "$domain" "$max_items" "$INBOX" "$TODAY" "$SEEN_RSS" <<'PYEOF'
import sys, json, os, re
import urllib.request, urllib.parse

key, query, domain, max_items, inbox, today, seen_path = sys.argv[1:]
max_items = int(max_items)

params = urllib.parse.urlencode({
    "q": json.dumps({"_text_any": {"patent_title": query}}),
    "f": json.dumps(["patent_id", "patent_title", "patent_date", "patent_abstract"]),
    "o": json.dumps({"size": max_items}),
    "s": json.dumps([{"patent_date": "desc"}]),
})
url = f"https://search.patentsview.org/api/v1/patent/?{params}"

try:
    req = urllib.request.Request(url, headers={"X-Api-Key": key})
    data = json.load(urllib.request.urlopen(req, timeout=20))
except Exception as ex:
    print(f"  ⚠️  uspto patents 실패(엔드포인트 1회 실검증 필요): {ex}", file=sys.stderr)
    sys.exit(0)

seen = set(open(seen_path).read().splitlines())
feed_items, new_links, written = [], [], 0

for it in data.get("patents", []) or []:
    pid = it.get("patent_id", "")
    link = f"https://patents.google.com/patent/US{pid}" if pid else ""
    title = (it.get("patent_title") or "").strip()
    if not link or not title or link in seen:
        continue
    abstract = (it.get("patent_abstract") or "").strip()
    published = it.get("patent_date", "")

    fslug = re.sub(r"[^\w\s-]", "", title.lower())
    fslug = re.sub(r"[\s_]+", "-", fslug)[:60]
    out = os.path.join(inbox, f"fetch-{today}-patent-{fslug}.md")
    with open(out, "w") as f:
        f.write(f"""---
title: {json.dumps(title)}
created: {today}
captured: {today}
type: patent
domain: {domain}
source: {link}
patent_id: {pid}
published: "{published}"
tags: [drone, {domain}, patent]
---

# {title}

**특허번호**: US{pid}
**공개일**: {published}
**원문(1차 소스)**: {link}

## 초록(Abstract)

{abstract or "(초록 미제공 — 원문 참조)"}
""")
    feed_items.append({"title": title, "url": link, "source": "patentsview.org",
                       "domain": domain, "type": "patent", "region": "US",
                       "summary": abstract[:200], "published": published})
    seen.add(link); new_links.append(link); written += 1

if written:
    import subprocess
    subprocess.run(["python3", os.path.expanduser("~/2nd/scripts/news-feed-append.py")],
                   input=json.dumps(feed_items, ensure_ascii=False), text=True, capture_output=True)
    with open(seen_path, "a") as f:
        for l in new_links:
            f.write(l + "\n")
    print(f"  ✅ [{domain}] USPTO 특허 {written}건 → inbox/")
else:
    print("  skip uspto patents (새 항목 없음 또는 응답 파싱 0건)")
PYEOF
}

fetch_patents "$USPTO_KEY" "drone" "ai-autonomy" 5
fetch_patents "$USPTO_KEY" "unmanned aerial vehicle" "hardware" 5

# ── hardware (RSS) ──────────────────────────────────────────────
fetch_rss "https://oscarliang.com/feed/"  "oscarliang-fpv" "hardware" 5
fetch_rss "https://dronedj.com/feed/"     "dronedj"        "hardware" 5

# ── hardware: 제조사 공식 발표(직접 RSS 미제공 확인됨 → Google News로
# 대체, 2026-08-02 검증: enterprise-insights.dji.com/feed, skydio.com/
# blog/rss.xml 등 표준 경로 전부 404 — 실제 RSS 없음을 curl로 직접 확인
# 후 결정한 대안). fetch_rss()는 재사용, 새 함수 없음(최소 변경).
fetch_rss "https://news.google.com/rss/search?q=%22DJI+Enterprise%22&hl=en-US&gl=US&ceid=US:en" "dji-enterprise" "hardware" 4
fetch_rss "https://news.google.com/rss/search?q=Skydio&hl=en-US&gl=US&ceid=US:en"                "skydio"        "hardware" 4
fetch_rss "https://news.google.com/rss/search?q=%22Parrot+Drone%22&hl=en-US&gl=US&ceid=US:en"    "parrot"        "hardware" 4

# ── ops-mission (RSS) ───────────────────────────────────────────
fetch_rss "https://www.suasnews.com/feed/" "suasnews"      "ops-mission" 5
fetch_rss "https://dronelife.com/feed/"    "dronelife"     "ops-mission" 5

# ── regulations (RSS) ───────────────────────────────────────────
fetch_rss "https://www.suasnews.com/category/regulation/feed/" "suasnews-regulation" "regulations" 5

# ── regulations 1차 소스: 미 연방 규정공보(Federal Register, FAA) ──
# 무료·키 불필요(federalregister.gov 공식 API). 뉴스 재가공이 아닌
# FAA 규정/고시 원문을 직접 수집 — "틀린 말을 하지 않는다" 목표에
# 직결되는 1차 소스 보강(2026-08-02, 마스터 요청).
fetch_federal_register() {
  local term="$1" slug="$2" domain="$3" max_items="${4:-5}"
  local out_prefix="$INBOX/fetch-${TODAY}-fedreg-${slug}"

  python3 - "$term" "$slug" "$domain" "$max_items" "$out_prefix" "$TODAY" "$SEEN_RSS" "$UA" <<'PYEOF'
import sys, json, os
import urllib.request, urllib.parse

term, slug, domain, max_items, out_prefix, today, seen_path, ua = sys.argv[1:]
max_items = int(max_items)

fields = ["title", "abstract", "html_url", "publication_date", "document_number", "type"]
qs = urllib.parse.urlencode({
    "conditions[term]": term,
    "conditions[agencies][]": "federal-aviation-administration",
    "order": "newest",
    "per_page": max_items,
}) + "".join(f"&fields[]={f}" for f in fields)
url = f"https://www.federalregister.gov/api/v1/articles.json?{qs}"

try:
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    data = json.load(urllib.request.urlopen(req, timeout=20))
except Exception as ex:
    print(f"  ⚠️  federalregister {slug} 실패: {ex}", file=sys.stderr)
    sys.exit(0)

seen = set(open(seen_path).read().splitlines())
feed_items, new_links, written = [], [], 0

for it in data.get("results", []):
    link = it.get("html_url", "")
    title = (it.get("title") or "").strip()
    if not link or not title or link in seen:
        continue
    abstract = (it.get("abstract") or "").strip()
    published = it.get("publication_date", "")
    doc_type = it.get("type", "")
    doc_no = it.get("document_number", "")

    out = f"{out_prefix}-{doc_no}.md"
    with open(out, "w") as f:
        f.write(f"""---
title: {json.dumps(title)}
created: {today}
captured: {today}
type: regulation-notice
domain: {domain}
source: {link}
doc_type: {json.dumps(doc_type)}
document_number: {doc_no}
published: "{published}"
tags: [drone, {domain}, faa, regulation]
---

# {title}

**문서 유형**: {doc_type}
**공표일**: {published}
**Federal Register 문서번호**: {doc_no}
**원문(1차 소스)**: {link}

## 요약(Abstract)

{abstract or "(요약 미제공 — 원문 참조)"}
""")
    feed_items.append({"title": title, "url": link, "source": "federalregister.gov",
                       "domain": domain, "type": "regulation", "region": "US",
                       "summary": abstract[:200], "published": published})
    seen.add(link); new_links.append(link); written += 1

if written:
    import subprocess
    subprocess.run(["python3", os.path.expanduser("~/2nd/scripts/news-feed-append.py")],
                   input=json.dumps(feed_items, ensure_ascii=False), text=True, capture_output=True)
    with open(seen_path, "a") as f:
        for l in new_links:
            f.write(l + "\n")
    print(f"  ✅ [{domain}] Federal Register(FAA) {written}건 → inbox/")
else:
    print(f"  skip federalregister {slug} (새 항목 없음)")
PYEOF
}

fetch_federal_register "drone" "faa" "regulations" 5

# ── arXiv 논문 자동 수집 (inbox → 위키 컴파일 + news-feed) ──────
fetch_arxiv() {
  local query="$1" slug="$2" domain="$3" max_items="${4:-3}"
  python3 - "$query" "$slug" "$domain" "$max_items" "$INBOX" "$TODAY" "$SEEN_RSS" <<'PYEOF'
import sys, json, os, re, subprocess
import urllib.request, urllib.parse
import xml.etree.ElementTree as ET

query, slug, domain, max_items, inbox, today, seen_path = sys.argv[1:]
max_items = int(max_items)
ns = {'a': 'http://www.w3.org/2005/Atom'}

url = ("https://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(query)
       + "&sortBy=submittedDate&sortOrder=descending&max_results=15")
try:
    req = urllib.request.Request(url, headers={'User-Agent': '2ndBrainFetcher/2.0'})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=20).read())
except Exception as ex:
    print(f"  ⚠️  arxiv {slug} 실패: {ex}", file=sys.stderr)
    sys.exit(0)

seen = set(open(seen_path).read().splitlines())
feed_items, new_links, written = [], [], 0

for e in root.findall('a:entry', ns):
    if written >= max_items:
        break
    link = (e.findtext('a:id', namespaces=ns) or '').strip()
    title = re.sub(r'\s+', ' ', (e.findtext('a:title', namespaces=ns) or '')).strip()
    if not link or link in seen or not title:
        continue
    abstract = re.sub(r'\s+', ' ', (e.findtext('a:summary', namespaces=ns) or '')).strip()
    published = (e.findtext('a:published', namespaces=ns) or '')[:10]
    author_list = [a.findtext('a:name', namespaces=ns) or '' for a in e.findall('a:author', ns)]
    authors = ", ".join(author_list)[:200]

    fslug = re.sub(r'[^\w\s-]', '', title.lower())
    fslug = re.sub(r'[\s_]+', '-', fslug)[:60]
    out = os.path.join(inbox, f"fetch-{today}-arxiv-{fslug}.md")
    with open(out, 'w') as f:
        f.write(f"""---
title: {json.dumps(title)}
created: {today}
captured: {today}
type: paper
domain: {domain}
source: {link}
authors: {json.dumps(authors)}
published: "{published}"
tags: [drone, {domain}, paper, arxiv]
---

# {title}

**Authors**: {authors}
**Published**: {published}
**arXiv**: {link}

## Abstract

{abstract}
""")
    feed_items.append({"title": title, "url": link, "source": "arxiv.org",
                       "domain": domain, "type": "paper", "region": "global",
                       "summary": abstract[:200], "published": published})
    seen.add(link); new_links.append(link); written += 1

    # Zotero에도 밀어넣어 원문(PDF) 보존 — 실패해도 inbox 파이프라인은 계속 진행한다
    # (Zotero 계정/키 미설정인 다른 머신에서도 이 스크립트가 죽으면 안 됨).
    try:
        arxiv_id = link.rsplit('/abs/', 1)[-1].split('v')[0]
        push_payload = json.dumps({
            "title": title, "authors": author_list, "abstract": abstract,
            "arxiv_id": arxiv_id, "url": link,
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}", "date": published,
        }, ensure_ascii=False)
        subprocess.run(["python3", os.path.expanduser("~/2nd/scripts/zotero-web-add.py")],
                       input=push_payload, text=True, capture_output=True, timeout=60)
    except Exception:
        pass

if written:
    subprocess.run(["python3", os.path.expanduser("~/2nd/scripts/news-feed-append.py")],
                   input=json.dumps(feed_items, ensure_ascii=False), text=True, capture_output=True)
    with open(seen_path, 'a') as f:
        for l in new_links:
            f.write(l + "\n")
    print(f"  ✅ [{domain}] arXiv {slug} 논문 {written}편 → inbox/ (+Zotero PDF 보존 시도)")
else:
    print(f"  skip arxiv {slug} (새 논문 없음)")
PYEOF
}

fetch_arxiv 'all:"UAV flight control" OR all:"quadrotor control"' "flight"  "flight-control" 3
fetch_arxiv 'all:"drone swarm" OR all:"autonomous UAV"'          "swarm"   "ai-autonomy"    3
fetch_arxiv 'all:"UAV communication" OR all:"drone network"'     "comms"   "comms-protocol" 3

# 2026-08-19 확장: 자동수집이 커버 못 하던 도메인(perception/hardware/LLM-agent/
# security/GCS software) 5종 추가. 기존 3쿼리는 flight-control·swarm(ai-autonomy)·
# comms-protocol만 다뤄 drone-ai(perception)·drone-hw·voice-control/ai-agent는
# 사실상 마스터의 수동 정밀재검색에만 의존하고 있었음. domain 값은 drone-wiki-web
# lib/types.ts의 DOMAIN_META 키와 반드시 일치시킬 것.
fetch_arxiv 'all:"UAV object detection" OR all:"drone visual navigation" OR all:"UAV SLAM"'          "perception"    "ai-autonomy"   3
fetch_arxiv 'all:"UAV battery management" OR all:"drone hardware design" OR all:"quadrotor actuator"' "hardware"      "hardware"      3
fetch_arxiv 'all:"UAV language model" OR all:"drone LLM agent" OR all:"UAV vision-language model"'    "llm-agent"     "ai-autonomy"   3
fetch_arxiv 'all:"UAV jamming detection" OR all:"drone GPS spoofing" OR all:"UAV secure communication"' "security"    "comms-protocol" 3
fetch_arxiv 'all:"ground control station" OR all:"UAV mission planning software"'                     "gcs"           "gcs-software"  3

# ── Crossref 저널논문 + KCI 국내논문 수집 (inbox + news-feed) ───
KCI_KEY=$(grep '^KCI_API_KEY=' "$HOME/2nd/.env" 2>/dev/null | cut -d= -f2 || true)
python3 - "$INBOX" "$TODAY" "$SEEN_RSS" "${KCI_KEY:-}" <<'PYEOF'
import sys, json, os, re, subprocess
import urllib.request, urllib.parse
import xml.etree.ElementTree as ET
from datetime import date, timedelta

inbox, today, seen_path, kci_key = sys.argv[1:]
seen = set(open(seen_path).read().splitlines())
feed_items, new_links = [], []

DOMAIN_RULES = [
    ("ai-autonomy",    ["swarm", "autonomous", "vision", "learning", "ai ", "neural", "detection", "slam"]),
    ("comms-protocol", ["communication", "network", "link", "relay", "spectrum", "통신"]),
    ("flight-control", ["control", "flight", "attitude", "trajectory", "path planning", "제어", "비행"]),
    ("regulations",    ["regulation", "law", "policy", "법", "규제"]),
    ("ops-mission",    ["delivery", "inspection", "mission", "survey", "배송", "임무"]),
]
def classify(text):
    t = text.lower()
    for dom, kws in DOMAIN_RULES:
        if any(k in t for k in kws):
            return dom
    return "ops-mission"

def slugify(t):
    t = re.sub(r"[^\w\s-]", "", t.lower())
    return re.sub(r"[\s_]+", "-", t)[:60]

def write_paper(title, url, domain, region, authors, journal, published, abstract, src_tag):
    fslug = slugify(title)
    out = os.path.join(inbox, f"fetch-{today}-{src_tag}-{fslug}.md")
    with open(out, "w") as f:
        f.write(f"""---
title: {json.dumps(title)}
created: {today}
captured: {today}
type: paper
domain: {domain}
source: {url}
authors: {json.dumps(authors[:200])}
journal: {json.dumps(journal[:120])}
published: "{published}"
tags: [drone, {domain}, paper, {src_tag}]
---

# {title}

**Authors**: {authors[:200]}
**Journal**: {journal}
**Published**: {published}
**Link**: {url}

## Abstract

{abstract or "(초록 미제공 — 링크 참조)"}
""")
    feed_items.append({"title": title, "url": url, "source": "doi.org" if "doi.org" in url else "kci.go.kr",
                       "domain": domain, "type": "paper", "region": region,
                       "summary": (abstract or journal)[:200], "published": published})
    seen.add(url); new_links.append(url)

# 1) Crossref — 최근 60일 드론/UAV 저널논문
try:
    since = (date.today() - timedelta(days=60)).isoformat()
    url = ("https://api.crossref.org/works?query=drone+UAV"
           f"&filter=type:journal-article,from-pub-date:{since}"
           "&sort=published&order=desc&rows=15&mailto=krill0188@gmail.com")
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': '2ndBrain/1.0'}), timeout=20))
    cnt = 0
    for it in d["message"]["items"]:
        if cnt >= 4: break
        doi = it.get("DOI", "")
        link = f"https://doi.org/{doi}"
        title = (it.get("title") or [""])[0].strip()
        if not doi or not title or link in seen: continue
        authors = ", ".join(f"{a.get('family','')} {a.get('given','')}".strip() for a in it.get("author", [])[:5])
        journal = (it.get("container-title") or [""])[0]
        pub = "-".join(str(x) for x in (it.get("published", {}).get("date-parts") or [[""]])[0])
        abstract = re.sub(r"<[^>]+>", "", it.get("abstract", ""))[:800]
        write_paper(title, link, classify(title + " " + abstract), "global", authors, journal, pub, abstract, "crossref")
        cnt += 1
    if cnt: print(f"  ✅ [paper] Crossref 저널논문 {cnt}편 → inbox/")
    else: print("  skip crossref (새 논문 없음)")
except Exception as ex:
    print(f"  ⚠️  crossref 실패: {ex}", file=sys.stderr)

# 2) KCI — 국내 등재논문 (키 설정 시 활성화)
# 2026-08-19: 실제 응답 스키마 실측 확인 결과 article-id는 <articleInfo> 태그의
# "속성"이지 하위 태그가 아니라 findtext(".//article-id")로는 항상 빈 문자열이
# 나와, 모든 레코드의 link가 동일값(...artiId=)으로 생성되어 dedup(seen)에 걸려
# 사실상 1건만 저장되던 버그. articleInfo.attrib에서 직접 가져오도록 수정.
# 키워드도 "드론" 단일어라 UAV/무인기/무인비행체 동의어를 OR로 추가해 커버리지 확대.
# regDateFrom/regDateTo(등록일 범위, 공식 활용가이드 확인)로 최근 7일 등록분만
# 요청 — 검색결과 상위가 항상 오래된 인기논문이라 새 논문을 놓치는 걸 방지.
if kci_key:
    try:
        kci_keywords = ["드론", "UAV", "무인기", "무인비행체"]
        reg_from = (date.today() - timedelta(days=7)).strftime("%Y%m%d")
        reg_to = date.today().strftime("%Y%m%d")
        cnt = 0
        for kw in kci_keywords:
            if cnt >= 4:
                break
            url = ("https://open.kci.go.kr/po/openapi/openApiSearch.kci?apiCode=articleSearch"
                   f"&key={kci_key}&title={urllib.parse.quote(kw)}"
                   f"&regDateFrom={reg_from}&regDateTo={reg_to}&displayCount=10")
            root = ET.fromstring(urllib.request.urlopen(url, timeout=20).read())
            for rec in root.iter("record"):
                if cnt >= 4:
                    break
                def ft(*names):
                    for n in names:
                        v = rec.findtext(f".//{n}")
                        if v: return v.strip()
                    return ""
                article_info = rec.find(".//articleInfo")
                art_id = (article_info.attrib.get("article-id", "") if article_info is not None else "")
                title = ft("article-title", "articleTitle", "title")
                if not title or not art_id: continue
                link = f"https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId={art_id}"
                if link in seen: continue
                authors = ft("author", "authors", "author-group")
                journal = ft("journal-name", "journalName", "journal-title")
                pub = ft("pub-year", "pubYear", "publication-date")
                abstract = ft("abstract", "abstract-ko")[:800]
                write_paper(title, link, classify(title + " " + abstract), "KR", authors, journal, pub, abstract, "kci")
                cnt += 1
        if cnt: print(f"  ✅ [paper] KCI 국내논문 {cnt}편 → inbox/")
        else: print("  ⚠️  kci: 응답 파싱 0건 — 키/스펙 확인 필요", file=sys.stderr)
    except Exception as ex:
        print(f"  ⚠️  kci 실패: {ex}", file=sys.stderr)

if feed_items:
    subprocess.run(["python3", os.path.expanduser("~/2nd/scripts/news-feed-append.py")],
                   input=json.dumps(feed_items, ensure_ascii=False), text=True, capture_output=True)
    with open(seen_path, "a") as f:
        for l in new_links:
            f.write(l + "\n")
PYEOF

# ── YouTube 채널 화이트리스트 영상 수집 (inbox + news-feed) ─────
YT_KEY=$(grep '^YOUTUBE_API_KEY=' "$HOME/2nd/.env" 2>/dev/null | cut -d= -f2 || true)
YT_CONF="$HOME/2nd/config/youtube-channels.txt"
if [[ -n "${YT_KEY:-}" && -f "$YT_CONF" ]]; then
  python3 - "$YT_KEY" "$YT_CONF" "$INBOX" "$TODAY" "$SEEN_RSS" <<'PYEOF'
import sys, json, os, re
import urllib.request

key, conf, inbox, today, seen_path = sys.argv[1:]
CACHE = os.path.expanduser("~/2nd/.ua/youtube-channels-cache.json")
API = "https://www.googleapis.com/youtube/v3"

def get(url):
    with urllib.request.urlopen(url, timeout=15) as r:
        return json.load(r)

cache = {}
if os.path.exists(CACHE):
    try: cache = json.load(open(CACHE))
    except Exception: cache = {}

seen = set(open(seen_path).read().splitlines())
feed_items, new_links, total = [], [], 0

for line in open(conf):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = line.split("|")
    handle = parts[0].lstrip("@")
    domain = parts[1] if len(parts) > 1 else ""
    region = parts[2] if len(parts) > 2 else "global"

    # 핸들 → 업로드 재생목록 (캐시)
    if handle not in cache:
        try:
            d = get(f"{API}/channels?part=snippet,contentDetails&forHandle={handle}&key={key}")
            items = d.get("items") or []
            if not items:
                print(f"  ⚠️  youtube @{handle}: 채널 없음", file=sys.stderr); continue
            cache[handle] = {
                "title": items[0]["snippet"]["title"],
                "uploads": items[0]["contentDetails"]["relatedPlaylists"]["uploads"],
            }
        except Exception as ex:
            print(f"  ⚠️  youtube @{handle}: {ex}", file=sys.stderr); continue

    ch = cache[handle]
    try:
        d = get(f"{API}/playlistItems?part=snippet&playlistId={ch['uploads']}&maxResults=5&key={key}")
    except Exception as ex:
        print(f"  ⚠️  youtube @{handle} 업로드 조회 실패: {ex}", file=sys.stderr); continue

    from datetime import date, timedelta
    cutoff = (date.today() - timedelta(days=45)).isoformat()
    written = 0
    for it in d.get("items", []):
        if written >= 2:
            break
        sn = it["snippet"]
        vid = sn.get("resourceId", {}).get("videoId", "")
        url = f"https://www.youtube.com/watch?v={vid}"
        if not vid or url in seen:
            continue
        title = sn.get("title", "").strip()
        desc = re.sub(r"\s+", " ", sn.get("description", ""))[:500]
        published = sn.get("publishedAt", "")[:10]
        if published and published < cutoff:
            continue  # 오래된 백로그 영상 제외 (최근 45일만)

        fslug = re.sub(r"[^\w\s-]", "", title.lower())
        fslug = re.sub(r"[\s_]+", "-", fslug)[:60]
        out = os.path.join(inbox, f"fetch-{today}-yt-{fslug}.md")
        with open(out, "w") as f:
            f.write(f"""---
title: {json.dumps(title)}
created: {today}
captured: {today}
type: video
domain: {domain}
source: {url}
channel: {json.dumps(ch['title'])}
published: "{published}"
tags: [drone, {domain}, video, youtube]
---

# {title}

**채널**: {ch['title']} (공신력 화이트리스트)
**게시**: {published}
**영상**: {url}

## 설명 요약

{desc}
""")
        feed_items.append({"title": f"[{ch['title']}] {title}", "url": url,
                           "source": "youtube.com", "domain": domain, "type": "video",
                           "region": region, "summary": desc[:200], "published": published})
        seen.add(url); new_links.append(url); written += 1; total += 1
    if written:
        print(f"  ✅ [{domain}] YouTube @{handle} 영상 {written}건 → inbox/")

json.dump(cache, open(CACHE, "w"), ensure_ascii=False)
if feed_items:
    import subprocess
    subprocess.run(["python3", os.path.expanduser("~/2nd/scripts/news-feed-append.py")],
                   input=json.dumps(feed_items, ensure_ascii=False), text=True, capture_output=True)
    with open(seen_path, "a") as f:
        for l in new_links:
            f.write(l + "\n")
if total == 0:
    print("  youtube: 새 영상 없음")
PYEOF
else
  echo "  youtube: API키 또는 채널설정 없음 — 스킵"
fi

# ── ops-mission 1차 소스: 조달청 나라장터 입찰공고정보 — 무료 키 필요 ──
# 키 발급: https://www.data.go.kr/data/15129394/openapi.do (활용신청).
# .env에 NARA_API_KEY=<키> 추가 시 활성화, 없으면 자동 스킵. 기존
# "정부사업" 구글뉴스 검색(간접 재가공)을 대체하지 않고 1차 소스로 보강한다.
# ⚠️ 엔드포인트(apis.data.go.kr/1230000/ad/BidPublicInfoService/...)는
# 공공데이터포털에 공개된 표준 서비스ID/오퍼레이션명 기준 구현이며, 이
# 세션에서는 키가 없어 실호출 검증을 못 했다 — 키 등록 후 1회 실행
# 결과를 확인해야 한다(마스터에게 보고 필수).
NARA_KEY=$(grep '^NARA_API_KEY=' "$HOME/2nd/.env" 2>/dev/null | cut -d= -f2 || true)
fetch_procurement() {
  local key="$1" domain="$2" max_items="${3:-5}"
  [[ -z "$key" ]] && { echo "  procurement: NARA_API_KEY 없음 — 스킵(발급: https://www.data.go.kr/data/15129394/openapi.do)"; return 0; }

  python3 - "$key" "$domain" "$max_items" "$INBOX" "$TODAY" "$SEEN_RSS" <<'PYEOF'
import sys, json, os, re
import urllib.request, urllib.parse
from datetime import date, timedelta

key, domain, max_items, inbox, today, seen_path = sys.argv[1:]
max_items = int(max_items)

begin = (date.today() - timedelta(days=14)).strftime("%Y%m%d0000")
end = date.today().strftime("%Y%m%d2359")
params = urllib.parse.urlencode({
    "serviceKey": key, "pageNo": 1, "numOfRows": max_items,
    "inqryDiv": 1, "inqryBgnDt": begin, "inqryEndDt": end,
    "bidNtceNm": "드론", "type": "json",
})
url = f"http://apis.data.go.kr/1230000/ad/BidPublicInfoService/getBidPblancListInfoServcPPSSrch?{params}"

try:
    data = json.load(urllib.request.urlopen(url, timeout=20))
    items = data.get("response", {}).get("body", {}).get("items", []) or []
    if isinstance(items, dict):
        items = [items]
except Exception as ex:
    print(f"  ⚠️  나라장터 실패(엔드포인트 1회 실검증 필요): {ex}", file=sys.stderr)
    sys.exit(0)

seen = set(open(seen_path).read().splitlines())
feed_items, new_links, written = [], [], 0

for it in items[:max_items]:
    link = it.get("bidNtceUrl") or it.get("bidNtceDtlUrl") or ""
    title = (it.get("bidNtceNm") or "").strip()
    if not link or not title or link in seen:
        continue
    agency = it.get("ntceInsttNm", "")
    deadline = it.get("bidClseDt", "")
    budget = it.get("presmptPrce", "")

    fslug = re.sub(r"[^\w\s-]", "", title.lower())
    fslug = re.sub(r"[\s_]+", "-", fslug)[:60]
    out = os.path.join(inbox, f"fetch-{today}-procurement-{fslug}.md")
    with open(out, "w") as f:
        f.write(f"""---
title: {json.dumps(title)}
created: {today}
captured: {today}
type: procurement-notice
domain: {domain}
source: {link}
agency: {json.dumps(agency)}
deadline: "{deadline}"
tags: [drone, {domain}, procurement, government]
---

# {title}

**발주기관**: {agency}
**마감**: {deadline}
**추정가격**: {budget}
**원문(1차 소스)**: {link}
""")
    feed_items.append({"title": title, "url": link, "source": "data.go.kr",
                       "domain": domain, "type": "procurement", "region": "KR",
                       "summary": agency[:200], "published": deadline})
    seen.add(link); new_links.append(link); written += 1

if written:
    import subprocess
    subprocess.run(["python3", os.path.expanduser("~/2nd/scripts/news-feed-append.py")],
                   input=json.dumps(feed_items, ensure_ascii=False), text=True, capture_output=True)
    with open(seen_path, "a") as f:
        for l in new_links:
            f.write(l + "\n")
    print(f"  ✅ [{domain}] 나라장터 입찰 {written}건 → inbox/")
else:
    print("  skip 나라장터 (새 항목 없음 또는 응답 파싱 0건)")
PYEOF
}

fetch_procurement "$NARA_KEY" "ops-mission" 5

# ── Zotero 수동 수집분 인제스트 (앱 실행 중일 때만) ─────────────
if curl -sf --max-time 3 "http://localhost:23119/connector/ping" >/dev/null 2>&1; then
  python3 "$HOME/2nd/scripts/zotero-ingest.py" 2>/dev/null || true
else
  echo "  zotero: 앱 미실행 — 스킵"
fi

# ── feed-only 수집: 국내뉴스·채용·정부사업 (위키 컴파일 제외) ────
python3 - "$SEEN_RSS" "$UA" <<'PYEOF'
import sys, json, re, html, os, subprocess
import urllib.request
from urllib.parse import urlparse

seen_path, ua = sys.argv[1:]
seen = set(open(seen_path).read().splitlines())
new_links = []
items_out = []

def rss_items(url, limit=30):
    try:
        import feedparser
        d = feedparser.parse(url, agent=ua)
        return [{'title': e.get('title', '').strip(),
                 'link': e.get('link', '').strip(),
                 'date': (e.get('published', '') or e.get('updated', ''))[:32],
                 'summary': html.unescape(re.sub(r'<[^>]+>', '', e.get('summary', '')))[:200].strip()}
                for e in d.entries[:limit]]
    except Exception as ex:
        print(f"  ⚠️  rss 실패 {url[:50]}: {ex}", file=sys.stderr)
        return []

def add(entries, typ, region, label, max_items, source_from_title=False):
    fresh = [e for e in entries if e['link'] and e['link'] not in seen][:max_items]
    for e in fresh:
        title, source = e['title'], urlparse(e['link']).hostname or ''
        if source_from_title and ' - ' in title:
            title, source = title.rsplit(' - ', 1)
        items_out.append({'title': title, 'url': e['link'], 'source': source,
                          'domain': '', 'type': typ, 'region': region,
                          'summary': e['summary'], 'published': e['date']})
        seen.add(e['link']); new_links.append(e['link'])
    if fresh:
        print(f"  ✅ [{label}] {len(fresh)}건 → news-feed")

GN = "https://news.google.com/rss/search?q={q}&hl=ko&gl=KR&ceid=KR:ko"
# 1) 국내 드론 뉴스
add(rss_items(GN.format(q="%EB%93%9C%EB%A1%A0")), 'news', 'KR', '국내뉴스', 8, source_from_title=True)
# 2) 정부사업 (지원사업·실증·공모)
add(rss_items(GN.format(q="%EB%93%9C%EB%A1%A0+%EC%A7%80%EC%9B%90%EC%82%AC%EC%97%85+OR+%EB%93%9C%EB%A1%A0+%EC%8B%A4%EC%A6%9D+OR+%EB%93%9C%EB%A1%A0+%EA%B3%B5%EB%AA%A8")), 'gov', 'KR', '정부사업', 5, source_from_title=True)
# 3) 방산 — 국내(무인기·드론 방산) + 해외(military drone)
add(rss_items(GN.format(q="%EB%B0%A9%EC%82%B0+%EB%93%9C%EB%A1%A0+OR+%EB%AC%B4%EC%9D%B8%EA%B8%B0+%EB%B0%A9%EC%82%B0+OR+%EA%B5%B0%EC%9A%A9+%EB%93%9C%EB%A1%A0")), 'defense', 'KR', '방산KR', 5, source_from_title=True)
add(rss_items("https://news.google.com/rss/search?q=military+drone+OR+defense+UAS+program&hl=en-US&gl=US&ceid=US:en"), 'defense', 'global', '방산글로벌', 5, source_from_title=True)
# 4) 해외 채용 (sUAS News jobs)
add(rss_items("https://www.suasnews.com/category/jobs/feed/"), 'job', 'global', '해외채용', 5)
# 5) 국내 채용 (Wanted API)
try:
    req = urllib.request.Request(
        "https://www.wanted.co.kr/api/v4/jobs?query=%EB%93%9C%EB%A1%A0&country=kr&limit=10",
        headers={'User-Agent': ua})
    data = json.load(urllib.request.urlopen(req, timeout=15))
    entries = [{'title': f"{j.get('position','')} — {j.get('company',{}).get('name','')}",
                'link': f"https://www.wanted.co.kr/wd/{j['id']}",
                'date': '', 'summary': j.get('company', {}).get('industry_name', '')}
               for j in data.get('data', []) if j.get('id')]
    add(entries, 'job', 'KR', '국내채용', 10)
except Exception as ex:
    print(f"  ⚠️  Wanted API 실패: {ex}", file=sys.stderr)

if items_out:
    r = subprocess.run(["python3", os.path.expanduser("~/2nd/scripts/news-feed-append.py")],
                       input=json.dumps(items_out, ensure_ascii=False), text=True, capture_output=True)
    print("  " + (r.stdout.strip() or r.stderr.strip()))
    with open(seen_path, 'a') as f:
        for l in new_links:
            f.write(l + "\n")
else:
    print("  feed-only: 새 항목 없음")
PYEOF

# 신규 펌웨어 릴리즈 감지 시 파라미터 diff 페이지 자동 생성
python3 "$HOME/2nd/scripts/param-diff.py" --auto 2>&1 | grep -v "^$" || true

# 영문 항목 한글 요약 부가 (원문+sha256 보존, claude CLI)
chmod +x "$HOME/2nd/scripts/ko-summarize.sh" 2>/dev/null
bash "$HOME/2nd/scripts/ko-summarize.sh" || true

# 오늘의 뉴스 2장 브리핑 생성 (claude CLI, 실패해도 계속)
bash "$HOME/2nd/scripts/daily-briefing.sh" || true

COUNT=$(ls "$INBOX"/fetch-"$TODAY"-*.md 2>/dev/null | wc -l | tr -d ' ')
if [[ "$COUNT" -gt 0 ]]; then
  echo "✅ ${COUNT}개 파일 수집 완료 → inbox/ 에 저장됨 (다음 cron에서 처리)"
else
  echo "ℹ️  새 자료 없음 (이미 처리됐거나 변경 없음)"
fi
