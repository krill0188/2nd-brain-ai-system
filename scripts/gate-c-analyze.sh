#!/usr/bin/env bash
# Gate C v2 — AI 구조 분석 + 공백 탐지
# Usage:
#   ./scripts/gate-c-analyze.sh           # 분석 + stdout 출력
#   ./scripts/gate-c-analyze.sh --deliver  # 분석 + Hermes Telegram 전달

set -euo pipefail

GRAPH="$HOME/2nd/.ua/knowledge-graph.json"
REPORT="$HOME/2nd/.ua/gap-report.md"
DELIVER=false

for arg in "$@"; do
  [[ "$arg" == "--deliver" ]] && DELIVER=true
done

if [[ ! -f "$GRAPH" ]]; then
  echo "❌ knowledge-graph.json 없음. Gate C 먼저 실행 필요:"
  echo "   hermes run --skill understand-knowledge --workdir ~/2nd"
  exit 1
fi

echo "🔍 Gate C v2 분석 시작..." >&2

# ── 1. Python으로 구조 데이터 추출 ────────────────────────────
STATS=$(python3 - "$GRAPH" <<'PYEOF'
import json, sys
from collections import Counter, defaultdict

with open(sys.argv[1]) as f:
    d = json.load(f)

nodes = d.get('nodes', [])
edges = d.get('edges', [])
layers_raw = d.get('layers', [])

# 레이어 → 노드ID 매핑
layer_of = {}
layer_info = {}
for layer in layers_raw:
    lname = layer['name']
    layer_info[lname] = {'nodeIds': layer.get('nodeIds', []), 'count': len(layer.get('nodeIds', []))}
    for nid in layer.get('nodeIds', []):
        layer_of[nid] = lname

# 노드 맵
node_map = {n['id']: n for n in nodes}

# 연결도 계산
degree = Counter()
for e in edges:
    degree[e.get('source', '')] += 1
    degree[e.get('target', '')] += 1

# 지식 레이어만 (Other/templates 제외)
KNOW_LAYERS = ['Concepts', 'Comparisons', 'Queries', 'Entities']

# 레이어별 article 수
layer_articles = defaultdict(list)
for n in nodes:
    nid = n['id']
    lyr = layer_of.get(nid, 'Other')
    if n.get('type') == 'article':
        layer_articles[lyr].append(n.get('name', nid))

# 고립 노드 (지식 레이어 내)
isolated = []
for n in nodes:
    nid = n['id']
    lyr = layer_of.get(nid, 'Other')
    if lyr in KNOW_LAYERS and degree.get(nid, 0) == 0:
        isolated.append(n.get('name', nid))

# 과부하 허브 (연결 8+)
high_deg = sorted(
    [(node_map.get(nid, {}).get('name', nid), cnt)
     for nid, cnt in degree.items() if cnt >= 8],
    key=lambda x: -x[1]
)

# 비어있는 지식 레이어 (article 0개)
empty_layers = [l for l in KNOW_LAYERS if len(layer_articles.get(l, [])) == 0]

# 얇은 지식 레이어 (article 1~2개)
thin_layers = [l for l in KNOW_LAYERS if 0 < len(layer_articles.get(l, [])) <= 2]

# 클러스터 간 연결 분석 (지식 레이어 간 cross-edge 수)
cross_edges = defaultdict(int)
for e in edges:
    if e.get('type') == 'related':
        sl = layer_of.get(e.get('source', ''), 'Other')
        tl = layer_of.get(e.get('target', ''), 'Other')
        if sl in KNOW_LAYERS and tl in KNOW_LAYERS and sl != tl:
            pair = tuple(sorted([sl, tl]))
            cross_edges[pair] += 1

# 연결 없는 레이어 쌍
all_pairs = [(a, b) for i, a in enumerate(KNOW_LAYERS) for b in KNOW_LAYERS[i+1:]]
disconnected_pairs = [f"{a}↔{b}" for a, b in all_pairs if cross_edges.get(tuple(sorted([a, b])), 0) == 0]

# 강점: 연결이 풍부한 레이어
strong_layers = [l for l in KNOW_LAYERS if len(layer_articles.get(l, [])) >= 3]

# 출력
print(f"TOTAL_NODES={len(nodes)}")
print(f"TOTAL_EDGES={len(edges)}")
print(f"ISOLATED={' | '.join(isolated) if isolated else '없음'}")
print(f"HIGH_DEG={' | '.join(f'{n}({c}개)' for n, c in high_deg) if high_deg else '없음'}")
print(f"EMPTY_LAYERS={', '.join(empty_layers) if empty_layers else '없음'}")
print(f"THIN_LAYERS={', '.join(thin_layers) if thin_layers else '없음'}")
print(f"DISCONNECTED_PAIRS={', '.join(disconnected_pairs) if disconnected_pairs else '없음'}")
print(f"STRONG_LAYERS={', '.join(strong_layers) if strong_layers else '없음'}")
for l in KNOW_LAYERS:
    cnt = len(layer_articles.get(l, []))
    names = ', '.join(layer_articles.get(l, [])[:3])
    print(f"LAYER_{l.upper()}={cnt}개 ({names})")
PYEOF
)

# ── 2. 값 추출 ───────────────────────────────────────────────
extract() { echo "$STATS" | grep "^$1=" | cut -d= -f2-; }

TOTAL_NODES=$(extract TOTAL_NODES)
TOTAL_EDGES=$(extract TOTAL_EDGES)
ISOLATED=$(extract ISOLATED)
HIGH_DEG=$(extract HIGH_DEG)
EMPTY=$(extract EMPTY_LAYERS)
THIN=$(extract THIN_LAYERS)
DISCONNECTED=$(extract DISCONNECTED_PAIRS)
STRONG=$(extract STRONG_LAYERS)
LAYER_CONCEPTS=$(extract LAYER_CONCEPTS)
LAYER_COMPARISONS=$(extract LAYER_COMPARISONS)
LAYER_QUERIES=$(extract LAYER_QUERIES)
LAYER_ENTITIES=$(extract LAYER_ENTITIES)

echo "📊 추출 완료: ${TOTAL_NODES}노드 · ${TOTAL_EDGES}엣지" >&2

# ── 3. Claude -p 분석 ────────────────────────────────────────
PROMPT="당신은 개인 지식관리 시스템(PKM) 전문가다. 아래는 ~/2nd 드론 도메인 지식그래프 구조 분석 데이터다. 이를 해석해서 실용적인 보고서를 작성해줘.

== 구조 데이터 ($(date '+%Y-%m-%d')) ==
- 전체: ${TOTAL_NODES}노드 · ${TOTAL_EDGES}엣지
- 고립 노드: ${ISOLATED}
- 과부하 허브 (연결 8+): ${HIGH_DEG}
- 비어있는 지식 레이어: ${EMPTY}
- 얇은 레이어 (2개 이하): ${THIN}
- 레이어 간 단절 쌍: ${DISCONNECTED}
- 강한 레이어 (3개 이상): ${STRONG}
- 레이어 상세:
  · Concepts: ${LAYER_CONCEPTS}
  · Comparisons: ${LAYER_COMPARISONS}
  · Queries: ${LAYER_QUERIES}
  · Entities: ${LAYER_ENTITIES}

== 시스템 컨텍스트 ==
- 드론 기술 도메인 PKM (drone/datalink/swarm/drone-hw/drone-sw/drone-ai/ai-agent)
- inbox/에 19개 드론 파일 대기 중 (PX4·ArduPilot 공식문서 + 개인 노트)
- Hermes Cron이 04:00 daily-ingest 실행 예정

== 출력 형식 (Telegram 마크다운, 한글) ==
🔍 *Gate C v2 — 지식구조 분석*
📅 $(date '+%Y-%m-%d %H:%M')
📊 ${TOTAL_NODES}노드 · ${TOTAL_EDGES}엣지

⚠️ *공백 탐지*
(각 문제를 1줄씩, 왜 문제인지 포함)

✅ *강점*
(잘 구성된 부분, 1~2줄)

🎯 *다음 수집 우선순위*
1. (구체적 액션: '~를 inbox에 추가')
2. (구체적 액션)
3. (구체적 액션)

💡 *(1줄 핵심 인사이트)*

간결하고 실용적으로. 드론 도메인 맥락 반영 필수."

echo "🤖 Claude 분석 중..." >&2
ANALYSIS=$(claude -p "$PROMPT" 2>/dev/null) || {
  ANALYSIS="❌ claude -p 분석 실패. claude CLI 로그인 상태 확인 필요."
}

# ── 4. 파일 저장 ─────────────────────────────────────────────
{
  echo "# Gate C Gap Analysis"
  echo "**분석일시**: $(date '+%Y-%m-%d %H:%M')"
  echo ""
  echo "## 구조 요약"
  echo "| 항목 | 값 |"
  echo "|---|---|"
  echo "| 총 노드 | ${TOTAL_NODES} |"
  echo "| 총 엣지 | ${TOTAL_EDGES} |"
  echo "| 비어있는 레이어 | ${EMPTY} |"
  echo "| 얇은 레이어 | ${THIN} |"
  echo "| 고립 노드 | ${ISOLATED} |"
  echo "| 과부하 허브 | ${HIGH_DEG} |"
  echo ""
  echo "## AI 분석"
  echo ""
  echo "$ANALYSIS"
} > "$REPORT"

# ── 5. 출력 ──────────────────────────────────────────────────
echo ""
echo "$ANALYSIS"
echo ""
echo "---" >&2
echo "📄 저장됨: $REPORT" >&2

# ── 6. Telegram 전달 (--deliver 옵션) ────────────────────────
if [[ "$DELIVER" == true ]]; then
  if command -v hermes &>/dev/null; then
    echo "$ANALYSIS" | hermes send -t telegram 2>/dev/null && \
      echo "📨 Telegram 전달 완료" >&2 || \
      echo "⚠️  Telegram 전달 실패 — 수동 복사 필요" >&2
  else
    echo "⚠️  hermes 명령어 없음 — Telegram 수동 전달 필요" >&2
  fi
fi
