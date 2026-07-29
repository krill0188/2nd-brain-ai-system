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

COUNT=$(ls "$INBOX"/fetch-"$TODAY"-*.md 2>/dev/null | wc -l | tr -d ' ')
if [[ "$COUNT" -gt 0 ]]; then
  echo "✅ ${COUNT}개 파일 수집 완료 → inbox/ 에 저장됨 (다음 cron에서 처리)"
else
  echo "ℹ️  새 자료 없음 (이미 처리됐거나 변경 없음)"
fi
