#!/usr/bin/env bash
# ko-summarize.sh — news-feed 영문 항목에 한글 요약(summary_ko) 부가
# 원문(title/summary)은 절대 수정하지 않음 — sha256으로 무결성 보존
# fetch-inbox.sh 말미에서 호출. claude CLI 없으면 스킵.
set -uo pipefail
export PATH="$HOME/.npm-global/bin:$HOME/.local/bin:/usr/local/bin:$PATH"

FEED="$HOME/2nd/.ua/news-feed.json"
command -v claude >/dev/null || { echo "  ko-summarize: claude CLI 없음 — 스킵"; exit 0; }
[[ -f "$FEED" ]] || exit 0

for BATCH in 1 2 3; do
  # 요약 대상 추출 (영문 항목 & summary_ko 없음, 최신순 25개)
  PROMPT=$(python3 - "$FEED" <<'PYEOF'
import json, sys, re
feed = sys.argv[1]
items = json.load(open(feed))

def is_english(t):
    letters = re.findall(r"[A-Za-z]", t)
    hangul = re.findall(r"[가-힣]", t)
    return len(letters) > 10 and len(letters) > len(hangul) * 3

todo = [(i, it) for i, it in enumerate(items)
        if not it.get("summary_ko") and is_english(it.get("title", "") + " " + it.get("summary", ""))][:25]
if not todo:
    sys.exit(3)

lines = []
for idx, it in todo:
    lines.append(f'{idx}| [{it.get("type","news")}] {it["title"][:150]} — {it.get("summary","")[:250]}')

print(f"""아래 드론 분야 영문 자료 목록입니다. 각 항목을 한국어 1~2문장(60자 내외)으로 초보자도 이해하게 요약하세요.
전문용어는 한글(영문) 병기. 반드시 아래 JSON만 출력:
{{"요약": {{"인덱스번호": "한글요약", ...}}}}

{chr(10).join(lines)}""")
PYEOF
  ) || break  # 대상 없으면 종료

  TMP=$(mktemp)
  echo "$PROMPT" | claude -p > "$TMP" 2>/dev/null || { rm -f "$TMP"; echo "  ko-summarize: claude 호출 실패"; exit 0; }

  python3 - "$FEED" "$TMP" <<'PYEOF'
import json, sys, re
feed, tmp = sys.argv[1:]
raw = re.sub(r'```(?:json)?', '', open(tmp).read()).strip()
s, e = raw.find('{'), raw.rfind('}')
try:
    d = json.loads(raw[s:e+1])
    mapping = d.get("요약", d)
    items = json.load(open(feed))
    n = 0
    for k, v in mapping.items():
        try:
            idx = int(k)
            if 0 <= idx < len(items) and isinstance(v, str) and v.strip():
                items[idx]["summary_ko"] = v.strip()[:200]
                n += 1
        except (ValueError, TypeError):
            continue
    json.dump(items, open(feed, "w"), ensure_ascii=False, indent=1)
    print(f"  ✅ ko-summarize: 한글 요약 {n}건 부가")
except Exception as ex:
    print(f"  ko-summarize: 파싱 실패 — {ex}")
PYEOF
  rm -f "$TMP"
done
exit 0
