#!/usr/bin/env bash
# test_fetch_inbox.sh — fetch-inbox.sh 확장(특허/규제/조달/제조사) 단위 테스트
#
# 실제 daily 파이프라인(already_fetched 게이트, 실제 inbox/, 실제 .rss-seen.txt)을
# 건드리지 않고, 격리된 임시 디렉터리에서 신규 함수만 추출해 검증한다.
#
# 실행: bash scripts/test_fetch_inbox.sh
set -uo pipefail

SCRIPT="$HOME/2nd/scripts/fetch-inbox.sh"
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

PASS=0; FAIL=0
ok()  { PASS=$((PASS+1)); echo "PASS: $1"; }
bad() { FAIL=$((FAIL+1)); echo "FAIL: $1"; }

# 0) 문법 검증 — 전체 스크립트가 여전히 파싱 가능한지(회귀 확인)
if bash -n "$SCRIPT" 2>"$TMPDIR/synerr"; then
  ok "fetch-inbox.sh 문법 검증 통과(bash -n)"
else
  bad "fetch-inbox.sh 문법 오류: $(cat "$TMPDIR/synerr")"
fi

# 신규 함수만 추출해 격리 실행 (실제 daily 파이프라인은 실행하지 않음)
extract_fn() { sed -n "/^${1}() {/,/^}\$/p" "$SCRIPT"; }

INBOX="$TMPDIR/inbox"; PROCESSED="$INBOX/processed"; SEEN_RSS="$PROCESSED/.rss-seen.txt"
mkdir -p "$PROCESSED"; touch "$SEEN_RSS"
TODAY=$(date +%Y-%m-%d)
UA="test-agent/1.0"

# 1) fetch_federal_register — 키 불필요, 실제 라이브 호출로 정상 산출물 검증
eval "$(extract_fn fetch_federal_register)"
fetch_federal_register "drone" "faa-test" "regulations" 2 >"$TMPDIR/fedreg.out" 2>&1
found=$(ls "$INBOX"/fetch-*-fedreg-faa-test-*.md 2>/dev/null | wc -l | tr -d ' ')
if [[ "$found" -ge 1 ]]; then
  f=$(ls "$INBOX"/fetch-*-fedreg-faa-test-*.md | head -1)
  if grep -q "^type: regulation-notice$" "$f" && grep -q "^domain: regulations$" "$f" \
     && grep -q "^source: https://www.federalregister.gov" "$f"; then
    ok "fetch_federal_register: FAA 규제 1차 소스 수집 + frontmatter 정상"
  else
    bad "fetch_federal_register: frontmatter 필드 누락 — $f"
  fi
else
  bad "fetch_federal_register: 산출물 없음(네트워크 문제 또는 로직 오류) — $(cat "$TMPDIR/fedreg.out")"
fi

# 2) fetch_patents — USPTO_API_KEY 없을 때 그레이스풀 스킵(회귀: 파일 생성 0건)
eval "$(extract_fn fetch_patents)"
before=$(ls "$INBOX"/fetch-*-patent-*.md 2>/dev/null | wc -l | tr -d ' ')
out=$(fetch_patents "" "drone" "hardware" 3 2>&1)
after=$(ls "$INBOX"/fetch-*-patent-*.md 2>/dev/null | wc -l | tr -d ' ')
if [[ "$before" == "$after" ]] && echo "$out" | grep -q "USPTO_API_KEY 없음"; then
  ok "fetch_patents: 키 없을 때 그레이스풀 스킵(파일 0건 생성, 경고 메시지 출력)"
else
  bad "fetch_patents: 키 없음 처리 회귀 — before=$before after=$after out=$out"
fi

# 3) fetch_procurement — NARA_API_KEY 없을 때 그레이스풀 스킵
eval "$(extract_fn fetch_procurement)"
before=$(ls "$INBOX"/fetch-*-procurement-*.md 2>/dev/null | wc -l | tr -d ' ')
out=$(fetch_procurement "" "ops-mission" 3 2>&1)
after=$(ls "$INBOX"/fetch-*-procurement-*.md 2>/dev/null | wc -l | tr -d ' ')
if [[ "$before" == "$after" ]] && echo "$out" | grep -q "NARA_API_KEY 없음"; then
  ok "fetch_procurement: 키 없을 때 그레이스풀 스킵(파일 0건 생성, 경고 메시지 출력)"
else
  bad "fetch_procurement: 키 없음 처리 회귀 — before=$before after=$after out=$out"
fi

# 4) 기존 호출부 무회귀 — 신규 코드 삽입으로 기존 라인이 지워지지 않았는지 확인
for sig in \
  'fetch_github_release "PX4/PX4-Autopilot"' \
  'fetch_rss "https://oscarliang.com/feed/"' \
  'fetch_rss "https://www.suasnews.com/feed/"' \
  "fetch_arxiv 'all:\"UAV flight control\""
do
  if grep -qF "$sig" "$SCRIPT"; then
    ok "기존 호출부 무회귀: ${sig:0:40}"
  else
    bad "기존 호출부 누락(회귀 의심): ${sig:0:40}"
  fi
done

echo ""
echo "${PASS}/$((PASS+FAIL)) 통과"
[[ "$FAIL" -eq 0 ]]
