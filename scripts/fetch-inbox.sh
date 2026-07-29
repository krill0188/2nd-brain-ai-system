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

# ── hardware (RSS) ──────────────────────────────────────────────
fetch_rss "https://oscarliang.com/feed/"  "oscarliang-fpv" "hardware" 5
fetch_rss "https://dronedj.com/feed/"     "dronedj"        "hardware" 5

# ── ops-mission (RSS) ───────────────────────────────────────────
fetch_rss "https://www.suasnews.com/feed/" "suasnews"      "ops-mission" 5
fetch_rss "https://dronelife.com/feed/"    "dronelife"     "ops-mission" 5

# ── regulations (RSS) ───────────────────────────────────────────
fetch_rss "https://www.suasnews.com/category/regulation/feed/" "suasnews-regulation" "regulations" 5

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

# 오늘의 뉴스 2장 브리핑 생성 (claude CLI, 실패해도 계속)
bash "$HOME/2nd/scripts/daily-briefing.sh" || true

COUNT=$(ls "$INBOX"/fetch-"$TODAY"-*.md 2>/dev/null | wc -l | tr -d ' ')
if [[ "$COUNT" -gt 0 ]]; then
  echo "✅ ${COUNT}개 파일 수집 완료 → inbox/ 에 저장됨 (다음 cron에서 처리)"
else
  echo "ℹ️  새 자료 없음 (이미 처리됐거나 변경 없음)"
fi
