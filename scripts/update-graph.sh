#!/usr/bin/env bash
# update-graph.sh — concepts/ entities/ frontmatter를 파싱해 knowledge-graph.json 갱신
# 실행: ~/2nd/scripts/update-graph.sh
# 의존: python3

set -euo pipefail
export PATH="$HOME/.local/bin:/usr/local/bin:$PATH"

WIKI="$HOME/2nd"
GRAPH_JSON="$HOME/2nd/.ua/knowledge-graph.json"

mkdir -p "$(dirname "$GRAPH_JSON")"

echo "🔄 knowledge-graph.json 갱신 시작..."

python3 - <<'PYEOF'
import json, os, re, glob

wiki   = os.path.expanduser("~/2nd")
graph_path = os.path.expanduser("~/2nd/.ua/knowledge-graph.json")

# ── 기존 그래프 로드 ──────────────────────────────────────────
if os.path.exists(graph_path):
    with open(graph_path) as f:
        graph = json.load(f)
else:
    graph = {"nodes": [], "edges": []}

existing_ids = {n["id"] for n in graph.get("nodes", [])}
existing_edge_keys = {(e["source"], e["target"]) for e in graph.get("edges", [])}

# ── frontmatter 파서 ──────────────────────────────────────────
def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm_text = text[4:end]
    fm = {}
    for line in fm_text.splitlines():
        m = re.match(r'^(\w+):\s*(.+)', line.strip())
        if m:
            key, val = m.group(1), m.group(2).strip()
            # 리스트 처리: [a, b, c]
            if val.startswith('[') and val.endswith(']'):
                items = [x.strip().strip('"').strip("'") for x in val[1:-1].split(',') if x.strip()]
                fm[key] = items
            else:
                fm[key] = val.strip('"').strip("'")
    return fm

# ── wikilink 추출 ─────────────────────────────────────────────
def extract_links(text):
    return re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', text)

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

    node = {
        "id":     slug,
        "name":   fm.get("title", slug),
        "layer":  layer,
        "domain": fm.get("domain", ""),
        "tags":   fm.get("tags", []) if isinstance(fm.get("tags"), list) else [],
        "updated": fm.get("updated", fm.get("created", "")),
    }

    if slug not in existing_ids:
        graph["nodes"].append(node)
        existing_ids.add(slug)
        added_nodes += 1
    else:
        # 기존 노드 domain/updated 갱신
        for n in graph["nodes"]:
            if n["id"] == slug:
                if fm.get("domain"):
                    n["domain"] = fm["domain"]
                if fm.get("updated"):
                    n["updated"] = fm["updated"]
                break

    # 엣지: wikilink
    links = extract_links(content)
    for target_slug in links:
        target_slug = target_slug.strip()
        key = (slug, target_slug)
        if key not in existing_edge_keys:
            graph["edges"].append({"source": slug, "target": target_slug, "type": "wikilink"})
            existing_edge_keys.add(key)
            added_edges += 1

# ── 저장 ──────────────────────────────────────────────────────
with open(graph_path, "w") as f:
    json.dump(graph, f, ensure_ascii=False, indent=2)

print(f"✅ 노드 +{added_nodes}개, 엣지 +{added_edges}개 추가")
print(f"   총 노드: {len(graph['nodes'])}개, 총 엣지: {len(graph['edges'])}개")
print(f"   저장: {graph_path}")
PYEOF
