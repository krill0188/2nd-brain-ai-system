#!/usr/bin/env bash
# daily-briefing.sh — 오늘 수집된 뉴스를 claude -p로 2장 브리핑 요약 → .ua/daily-briefing.json
# fetch-inbox.sh 말미에서 호출. claude CLI 없으면 조용히 스킵 (이전 브리핑 유지).
set -uo pipefail
export PATH="$HOME/.npm-global/bin:$HOME/.local/bin:/usr/local/bin:$PATH"

FEED="$HOME/2nd/.ua/news-feed.json"
OUT="$HOME/2nd/.ua/daily-briefing.json"
TODAY=$(date +%Y-%m-%d)

command -v claude >/dev/null || { echo "  briefing: claude CLI 없음 — 스킵"; exit 0; }
[[ -f "$FEED" ]] || { echo "  briefing: news-feed 없음 — 스킵"; exit 0; }

# 이미 오늘 브리핑이 있으면 스킵
if [[ -f "$OUT" ]] && python3 -c "import json,sys; sys.exit(0 if json.load(open('$OUT')).get('date')=='$TODAY' else 1)" 2>/dev/null; then
  echo "  briefing: 오늘 분 이미 생성됨"
  exit 0
fi

PROMPT=$(python3 - "$FEED" "$TODAY" <<'PYEOF'
import json, sys
feed, today = sys.argv[1:]
items = [it for it in json.load(open(feed)) if it.get("fetched","").startswith(today)][:20]
if len(items) < 3:
    items = json.load(open(feed))[:20]
lines = [f"- [{it['type']}/{it.get('region','global')}] {it['title']}" + (f" — {it['summary'][:100]}" if it.get('summary') else "") for it in items]
print(f"""오늘({today}) 수집된 드론 분야 뉴스 목록입니다. 이를 종합해 2장짜리 브리핑으로 요약하세요.

{chr(10).join(lines)}

규칙:
- 1장: 오늘의 핵심 이슈 종합 (가장 중요한 흐름 3~4문장)
- 2장: 기술·산업 동향과 시사점 (3~4문장)
- 한국어, 명확하고 간결하게
- 반드시 아래 JSON만 출력 (다른 텍스트 금지):
{{"cards":[{{"title":"1장 제목","body":"..."}},{{"title":"2장 제목","body":"..."}}]}}""")
PYEOF
)

TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT
echo "$PROMPT" | claude -p > "$TMP" 2>/dev/null || { echo "  briefing: claude 호출 실패"; exit 0; }

python3 - "$OUT" "$TODAY" "$TMP" <<'PYEOF'
import json, sys, re
out, today, tmp = sys.argv[1:]
raw = open(tmp).read()
raw = re.sub(r'```(?:json)?', '', raw).strip()
s, e = raw.find('{'), raw.rfind('}')
try:
    d = json.loads(raw[s:e+1])
    cards = [c for c in d.get("cards", []) if c.get("title") and c.get("body")][:2]
    assert cards
    json.dump({"date": today, "cards": cards}, open(out, "w"), ensure_ascii=False, indent=1)
    print(f"  ✅ briefing: {today} 2장 생성 완료")
except Exception as ex:
    print(f"  briefing: 파싱 실패 — {ex}")
PYEOF
