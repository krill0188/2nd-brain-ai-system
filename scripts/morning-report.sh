#!/usr/bin/env bash
# 2nd-morning-report.sh — 새벽 자동 체인 검증 + 오늘의 드론 소식 → 텔레그램
# Hermes cron: 매일 07:30, no-agent (stdout이 그대로 텔레그램 전송)
set -uo pipefail

TODAY=$(date +%Y-%m-%d)
FEED="$HOME/2nd/.ua/news-feed.json"
BRIEF="$HOME/2nd/.ua/daily-briefing.json"
INBOX_CNT=$(ls "$HOME/2nd/inbox"/*.md 2>/dev/null | wc -l | tr -d ' ')

# 오늘 수집된 뉴스 수
NEWS_CNT=$(python3 -c "
import json
try:
    items = json.load(open('$FEED'))
    print(sum(1 for it in items if it.get('fetched','').startswith('$TODAY')))
except Exception:
    print(0)" 2>/dev/null)

# 브리핑 생성 여부
BRIEF_OK=$(python3 -c "
import json
try:
    d = json.load(open('$BRIEF'))
    print('yes' if d.get('date')=='$TODAY' and d.get('cards') else 'no')
except Exception:
    print('no')" 2>/dev/null)

# 웹 배포 확인 (사이트에 오늘 브리핑 게시됐는지)
SITE_DATE=$(curl -sf --max-time 20 "https://drone-wiki-web.vercel.app/" 2>/dev/null | grep -oE "오늘의 드론 소식 \([0-9-]+\)" | grep -oE "[0-9-]+" | head -1)

echo "🌅 DroneWiki 아침 점검 ($TODAY)"
echo ""
if [[ "$NEWS_CNT" -gt 0 ]]; then echo "✅ 새벽 수집: 오늘 뉴스 ${NEWS_CNT}건"; else echo "⚠️ 새벽 수집: 오늘 수집분 없음 — fetch 확인 필요"; fi
if [[ "$BRIEF_OK" == "yes" ]]; then echo "✅ AI 브리핑: 오늘 2장 생성됨"; else echo "⚠️ AI 브리핑: 오늘 분 없음 — daily-briefing 확인 필요"; fi
if [[ "$INBOX_CNT" -eq 0 ]]; then echo "✅ 위키 컴파일: inbox 전부 처리됨"; else echo "⚠️ 위키 컴파일: inbox ${INBOX_CNT}건 잔여 — ingest 확인 필요"; fi
if [[ "$SITE_DATE" == "$TODAY" ]]; then echo "✅ 웹 배포: 사이트에 오늘 브리핑 게시됨"; else echo "⚠️ 웹 배포: 사이트 브리핑 날짜=${SITE_DATE:-없음} — sync/deploy 확인 필요"; fi
echo ""

# 오늘의 드론 소식 본문
# 오늘 새로 생성된 canonical 페이지 목록 (daily-ingest는 사전 승인 없이
# 자동 컴파일한다 — README.md 정정 이후 실제 동작에 맞춰, 최소한 사후
# 가시성을 매일 확보하기 위해 추가. research-promote는 이미 사람이
# approve한 것이므로 구분 표시한다.)
python3 - "$HOME/2nd/log.md" "$TODAY" <<'PYEOF'
import re, sys
log_path, today = sys.argv[1], sys.argv[2]
text = open(log_path, encoding="utf-8").read()
headers = list(re.finditer(r"^## \[(\d{4}-\d{2}-\d{2})\] (\S+) \| (.+)$", text, re.MULTILINE))
created = []
for i, m in enumerate(headers):
    date, action, subject = m.groups()
    if date != today:
        continue
    start = m.end()
    end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
    block = text[start:end]
    pages = re.findall(r"^\s*- `((?:concepts|entities|comparisons|queries)/[^`]+\.md)` — (.+)$", block, re.MULTILINE)
    for path, desc in pages:
        approved = action == "research-promote"
        created.append((path, desc.strip(), approved))

if created:
    print("📄 오늘 신규 canonical 페이지")
    print("")
    for path, desc, approved in created:
        tag = "✅승인됨(연구루프)" if approved else "🤖자동생성(사전승인 없음)"
        print(f"- [{tag}] `{path}` — {desc}")
    print("")
PYEOF

if [[ "$BRIEF_OK" == "yes" ]]; then
  python3 - "$BRIEF" <<'PYEOF'
import json, sys
d = json.load(open(sys.argv[1]))
print("🗞️ 오늘의 드론 소식")
print("")
for c in d.get("cards", []):
    print(f"▎{c['title']}")
    print(c["body"])
    print("")
PYEOF
fi

echo "🔗 https://drone-wiki-web.vercel.app"
