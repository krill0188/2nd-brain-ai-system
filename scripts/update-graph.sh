#!/usr/bin/env bash
# update-graph.sh — concepts/ entities/ frontmatter를 파싱해 drone-knowledge-graph.json 갱신
# 실행: ~/2nd/scripts/update-graph.sh
# 의존: python3
#
# G0(2026-08-02): 파일명을 knowledge-graph.json → drone-knowledge-graph.json으로
# 분리했다. 실측 결과 ~/2nd에 설치된 서드파티 플러그인 "understand-anything"의
# /understand 명령도 정확히 같은 경로($HOME/2nd/.ua/knowledge-graph.json)에
# 코드베이스 구조 그래프(calls/imports/contains 엣지, article:/topic: 노드)를
# 쓴다는 걸 발견했다 — 두 서로 무관한 도구가 같은 파일을 공유하던 우연한
# 충돌이었다. understand-anything의 기존 파일은 절대 건드리지 않고(그 플러그인
# 기능을 깨뜨리면 안 됨), 우리 드론 지식그래프만 별도 파일로 분리한다.
set -euo pipefail
export PATH="$HOME/.local/bin:/usr/local/bin:$PATH"

WIKI="$HOME/2nd"
GRAPH_JSON="$HOME/2nd/.ua/drone-knowledge-graph.json"
LEGACY_SHARED_JSON="$HOME/2nd/.ua/knowledge-graph.json"

mkdir -p "$(dirname "$GRAPH_JSON")"

echo "🔄 drone-knowledge-graph.json 갱신 시작..."

python3 - "$GRAPH_JSON" "$LEGACY_SHARED_JSON" <<'PYEOF'
import json, os, re, glob, sys

sys.path.insert(0, os.path.expanduser("~/2nd/scripts"))
from graph_lib import (
    parse_frontmatter, extract_links_by_section, ontology_class_for_domain,
)

wiki = os.path.expanduser("~/2nd")
graph_path, legacy_path = sys.argv[1], sys.argv[2]

# ── G0 마이그레이션(최초 1회) ────────────────────────────────────
# 신규 전용 파일이 아직 없고, understand-anything이 공유하던 구 파일에
# 우리 canonical 데이터(ontologyClass 필드 보유 노드)가 있으면 그것만
# 걸러서 시드한다. understand-anything 전용 노드(article:/topic:, 코드
# 구조 엣지)는 가져오지 않는다 — 그 도구의 데이터를 우리 파일로 복제할
# 이유가 없다(각자 다른 목적의 그래프).
if not os.path.exists(graph_path) and os.path.exists(legacy_path):
    with open(legacy_path) as f:
        legacy = json.load(f)
    canonical_ids = {n["id"] for n in legacy.get("nodes", []) if "ontologyClass" in n}
    seed_nodes = [n for n in legacy.get("nodes", []) if n["id"] in canonical_ids]
    seed_edges = [e for e in legacy.get("edges", [])
                  if e.get("source") in canonical_ids and e.get("target") in canonical_ids]
    with open(graph_path, "w") as f:
        json.dump({"nodes": seed_nodes, "edges": seed_edges}, f, ensure_ascii=False, indent=2)
    print(f"🌱 G0 마이그레이션: understand-anything 공유 파일에서 canonical "
          f"노드 {len(seed_nodes)}개 + 엣지 {len(seed_edges)}개만 분리 시드")

# ── 기존 그래프 로드 ──────────────────────────────────────────
if os.path.exists(graph_path):
    with open(graph_path) as f:
        graph = json.load(f)
else:
    graph = {"nodes": [], "edges": []}

existing_ids = {n["id"] for n in graph.get("nodes", [])}
existing_edge_keys = {(e["source"], e["target"], e.get("type", "wikilink")) for e in graph.get("edges", [])}

# frontmatter 파서 / 섹션 맥락 관계타입 분류(G1)는 graph_lib.py에서 import함
# (테스트 가능하도록 분리, 2026-08-02 — 동작은 이전과 동일)

# ── 파일 스캔 ─────────────────────────────────────────────────
added_nodes = 0
added_edges = 0

scan_dirs = ["concepts", "entities", "comparisons", "queries"]
all_files = []
for d in scan_dirs:
    all_files.extend(glob.glob(f"{wiki}/{d}/**/*.md", recursive=True))
    all_files.extend(glob.glob(f"{wiki}/{d}/*.md"))

for fpath in sorted(set(all_files)):
    try:
        with open(fpath) as f:
            content = f.read()
    except:
        continue

    fm = parse_frontmatter(content)
    if not fm.get("title"):
        continue

    # 노드 ID: 파일명 (확장자 제외)
    slug = os.path.splitext(os.path.basename(fpath))[0]
    layer = os.path.basename(os.path.dirname(fpath)).capitalize()
    # layer 정규화
    layer_map = {"Concepts": "Concepts", "Entities": "Entities",
                 "Comparisons": "Comparisons", "Queries": "Queries"}
    layer = layer_map.get(layer, "Concepts")

    confidence = fm.get("confidence", "") if fm.get("confidence") in ("high", "medium", "low") else ""
    sources = fm.get("sources", []) if isinstance(fm.get("sources"), list) else []

    # ── 온톨로지 클래스 라벨 (Phase O1, ONTOLOGY_IMPLEMENTATION_ROADMAP.md) ──
    # ONTOLOGY_SPEC.md §5 매핑표를 문서 분류 목적에 맞게 단순화했다(원안은
    # domain 하나에 여러 런타임 클래스를 나열했으나, 위키 문서 자체를 그
    # 런타임 객체의 인스턴스로 볼 수는 없다 — 예: "PX4 아키텍처" 문서는
    # FlightController라는 하드웨어의 인스턴스가 아니라 그 기술에 대한
    # 설명이므로 Technology로 분류하는 게 맞다). 매핑 안 되면 null로 두고
    # 억지로 분류하지 않는다(SCHEMA.md 원칙과 동일).
    ontology_class = ontology_class_for_domain(fm.get("domain", ""))

    node = {
        "id":     slug,
        "name":   fm.get("title", slug),
        "layer":  layer,
        "domain": fm.get("domain", ""),
        "tags":   fm.get("tags", []) if isinstance(fm.get("tags"), list) else [],
        "updated": fm.get("updated", fm.get("created", "")),
        "confidence": confidence,
        "status": "canonical",
        "ontologyClass": ontology_class,
    }

    if slug not in existing_ids:
        graph["nodes"].append(node)
        existing_ids.add(slug)
        added_nodes += 1
    else:
        # 기존 노드 domain/updated/confidence/ontologyClass 갱신
        for n in graph["nodes"]:
            if n["id"] == slug:
                if fm.get("domain"):
                    n["domain"] = fm["domain"]
                if fm.get("updated"):
                    n["updated"] = fm["updated"]
                if confidence:
                    n["confidence"] = confidence
                n.setdefault("status", "canonical")
                n["ontologyClass"] = ontology_class
                break

    # 엣지: 본문 wikilink — G1부터 섹션 맥락에 따라 evidences/related/wikilink로 분화
    for target_slug, rel_type in extract_links_by_section(content):
        if not target_slug:
            continue
        key = (slug, target_slug, rel_type)
        if key not in existing_edge_keys:
            graph["edges"].append({
                "source": slug, "target": target_slug, "type": rel_type,
                "evidence": sources[:1], "confidence": confidence,
            })
            existing_edge_keys.add(key)
            added_edges += 1
        else:
            for e in graph["edges"]:
                if e["source"] == slug and e["target"] == target_slug and e.get("type") == rel_type:
                    e.setdefault("evidence", sources[:1])
                    e.setdefault("confidence", confidence)
                    break

    # 엣지: frontmatter contradictions → 명시적 contradicts 관계
    contradictions = fm.get("contradictions", [])
    if isinstance(contradictions, list):
        for target_slug in contradictions:
            target_slug = target_slug.strip()
            if not target_slug:
                continue
            key = (slug, target_slug, "contradicts")
            if key not in existing_edge_keys:
                graph["edges"].append({
                    "source": slug, "target": target_slug, "type": "contradicts",
                    "evidence": sources[:1], "confidence": confidence,
                })
                existing_edge_keys.add(key)
                added_edges += 1

# ── 노드 ID 정규화 (Phase 2, G0 이후에도 유지) ──────────────────
# 우리 전용 파일로 분리했지만, 과거 legacy 공유 파일 시절 섞여 들어온
# article:<slug> 잔재가 있으면 계속 병합한다(무해, 하위호환).
bare_slugs = existing_ids
redirect = {}
for n in graph["nodes"]:
    nid = n["id"]
    if nid.startswith("article:"):
        candidate = nid.split(":", 1)[1].rsplit("/", 1)[-1]
        if candidate in bare_slugs:
            redirect[nid] = candidate

if redirect:
    graph["nodes"] = [n for n in graph["nodes"] if n["id"] not in redirect]
    for e in graph["edges"]:
        if e["source"] in redirect:
            e["source"] = redirect[e["source"]]
        if e["target"] in redirect:
            e["target"] = redirect[e["target"]]
    seen = set()
    deduped = []
    for e in graph["edges"]:
        k = (e["source"], e["target"], e.get("type", "wikilink"))
        if k not in seen:
            seen.add(k)
            deduped.append(e)
    graph["edges"] = deduped
    print(f"🔗 노드 ID 정규화: article: prefix {len(redirect)}개 → bare slug 병합")

# ── 저장 ──────────────────────────────────────────────────────
with open(graph_path, "w") as f:
    json.dump(graph, f, ensure_ascii=False, indent=2)

rel_counts = {}
for e in graph["edges"]:
    t = e.get("type", "wikilink")
    rel_counts[t] = rel_counts.get(t, 0) + 1

print(f"✅ 노드 +{added_nodes}개, 엣지 +{added_edges}개 추가")
print(f"   총 노드: {len(graph['nodes'])}개, 총 엣지: {len(graph['edges'])}개")
print(f"   관계타입 분포: {rel_counts}")
print(f"   저장: {graph_path}")
PYEOF
