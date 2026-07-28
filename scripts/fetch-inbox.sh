#!/usr/bin/env bash
# fetch-inbox.sh — 드론 도메인 지식을 외부 소스에서 수집해 inbox/에 저장
# 실행: ~/2nd/scripts/fetch-inbox.sh [--force]
# 의존: curl, python3

set -euo pipefail
export PATH="$HOME/.local/bin:/usr/local/bin:$PATH"

INBOX="$HOME/2nd/inbox"
TODAY=$(date +%Y-%m-%d)
FORCE="${1:-}"

already_fetched() {
  local cnt
  cnt=$(ls "$INBOX"/fetch-"$TODAY"-*.md 2>/dev/null | wc -l | tr -d ' ')
  [[ "$cnt" -gt 0 ]]
}

[[ -z "$FORCE" ]] && already_fetched && { echo "✅ 오늘 이미 수집됨 ($TODAY)"; exit 0; }

echo "🔍 드론 도메인 지식 수집 시작 ($TODAY)..."

# ── GitHub 최신 릴리즈 노트 수집 ─────────────────────────────────
fetch_github_release() {
  local repo="$1" slug="$2"
  local out="$INBOX/fetch-${TODAY}-${slug}.md"
  local data tag body published slug_lower safe_tag

  data=$(curl -sf --max-time 15 "https://api.github.com/repos/${repo}/releases/latest" 2>/dev/null) || return 0

  tag=$(echo "$data"       | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('tag_name',''))" 2>/dev/null)
  published=$(echo "$data" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('published_at','')[:10])" 2>/dev/null)
  body=$(echo "$data"      | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('body','')[:3000])" 2>/dev/null)

  [[ -z "$tag" || -z "$body" ]] && return 0

  safe_tag="${tag//\//-}"
  if ls "$INBOX/processed/fetch-"*"-${slug}-${safe_tag}.md" 2>/dev/null | grep -q .; then
    echo "  skip $slug $tag (already processed)"
    return 0
  fi

  slug_lower=$(echo "$slug" | tr '[:upper:]' '[:lower:]')
  local source_url="https://github.com/${repo}/releases/tag/${tag}"

  python3 - "$out" "$slug" "$tag" "$TODAY" "$published" "$slug_lower" "$source_url" "$body" <<'PYEOF'
import sys
out_path, slug, tag, today, published, slug_lower, source_url, body = sys.argv[1:]
content = (
    "---\n"
    f'title: "{slug} {tag} Release Notes"\n'
    f"created: {today}\n"
    f"captured: {today}\n"
    "type: release-note\n"
    f"source: {source_url}\n"
    f"tags: [drone, {slug_lower}]\n"
    "---\n\n"
    f"# {slug} {tag} Release Notes ({published})\n\n"
    f"{body}\n"
)
with open(out_path, 'w') as f:
    f.write(content)
PYEOF

  echo "  ✅ $slug $tag → inbox/"
}

fetch_github_release "PX4/PX4-Autopilot"  "px4"
fetch_github_release "ArduPilot/ardupilot" "ardupilot"
fetch_github_release "mavlink/mavlink"     "mavlink"
fetch_github_release "dronecan/libcanard"  "dronecan"

COUNT=$(ls "$INBOX"/fetch-"$TODAY"-*.md 2>/dev/null | wc -l | tr -d ' ')
if [[ "$COUNT" -gt 0 ]]; then
  echo "✅ ${COUNT}개 파일 수집 완료 → inbox/ 에 저장됨 (다음 cron에서 처리)"
else
  echo "ℹ️  새 릴리즈 없음 (이미 처리됐거나 변경 없음)"
fi
