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

# 이미 오늘 브리핑이 있으면 스킵 (--force로 재생성)
if [[ "${1:-}" != "--force" ]] && [[ -f "$OUT" ]] && python3 -c "import json,sys; sys.exit(0 if json.load(open('$OUT')).get('date')=='$TODAY' else 1)" 2>/dev/null; then
  echo "  briefing: 오늘 분 이미 생성됨"
  exit 0
fi

PROMPT=$(python3 - "$FEED" "$TODAY" <<'PYEOF'
import json, sys
feed, today = sys.argv[1:]
items = [it for it in json.load(open(feed)) if it.get("fetched","").startswith(today)][:40]
if len(items) < 3:
    items = json.load(open(feed))[:40]

TYPE_LABEL = {"news":"뉴스", "release":"릴리즈", "defense":"방산", "gov":"정부사업",
              "job":"채용", "paper":"논문", "video":"영상"}
by_type = {}
for it in items:
    by_type.setdefault(TYPE_LABEL.get(it["type"], "뉴스"), []).append(it)

blocks = []
for label, its in by_type.items():
    lines = [f"- [{it.get('region','global')}] {it['title'][:120]}"
             + (f" — {(it.get('summary_ko') or it.get('summary',''))[:80]}" if (it.get('summary_ko') or it.get('summary')) else "")
             for it in its[:8]]
    blocks.append(f"[{label}]\n" + "\n".join(lines))

print(f"""오늘({today}) 수집된 드론 분야 자료를 분야별로 정리한 목록입니다. 분야별 브리핑 카드를 작성하세요.

{chr(10).join(blocks)}

규칙:
- 첫 카드: title "오늘의 종합" — 가장 중요한 흐름 2~3문장
- 이후 카드: 자료가 있는 분야만, 분야당 1카드 (title은 분야명 그대로: 뉴스/방산/정부사업/릴리즈/논문/영상/채용)
- 각 카드 body는 2~3문장, 핵심만. 초보자도 이해하게 한국어로
- 반드시 아래 JSON만 출력 (다른 텍스트 금지):
{{"cards":[{{"title":"오늘의 종합","body":"..."}},{{"title":"방산","body":"..."}}, ...]}}""")
PYEOF
)

TMP=$(mktemp)
ERR=$(mktemp)
trap 'rm -f "$TMP" "$ERR"' EXIT
if ! echo "$PROMPT" | claude -p --tools "" --safe-mode > "$TMP" 2> "$ERR"; then
  echo "  briefing: claude 호출 실패 — $(tail -c 200 "$ERR" | tr '\n' ' ')"
  exit 0
fi
if [[ ! -s "$TMP" ]]; then
  echo "  briefing: claude 빈 응답 — $(tail -c 200 "$ERR" | tr '\n' ' ')"
  exit 0
fi

python3 - "$OUT" "$TODAY" "$TMP" <<'PYEOF'
import json, sys, re
out, today, tmp = sys.argv[1:]
raw = open(tmp).read()
raw = re.sub(r'```(?:json)?', '', raw).strip()
s, e = raw.find('{'), raw.rfind('}')
try:
    d = json.loads(raw[s:e+1])
    cards = [c for c in d.get("cards", []) if c.get("title") and c.get("body")][:9]
    assert cards
    json.dump({"date": today, "cards": cards}, open(out, "w"), ensure_ascii=False, indent=1)
    print(f"  ✅ briefing: {today} 2장 생성 완료")
except Exception as ex:
    print(f"  briefing: 파싱 실패 — {ex}")
PYEOF
