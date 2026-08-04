#!/usr/bin/env python3
"""extract-knowledge-graph.py — raw/ 원시 문서에서 LangChain LLMGraphTransformer로
개념(Entity)과 관계(Relation)를 자동 추출해 지식그래프를 빌드한다.

중요(레이어 분리): 여기서 추출된 그래프는 사람이 검토하지 않은 "Discovery" 레이어다
(README의 Evidence → Canonical Memory → Discovery → Human Decision 4계층 원칙,
연구 파이프라인의 research-promote.py와 동일한 정신). concepts/entities/ 문서를
스캔하는 update-graph.sh의 canonical drone-knowledge-graph.json(RAG·그래프 뷰어가
소비하는 파일)과는 완전히 분리된 discovery-knowledge-graph.json에만 저장하며,
canonical 그래프에는 자동 병합하지 않는다. 승격은 사람이 discovery 그래프를 보고
concepts/entities/*.md로 직접 옮겨 적는 방식으로 이뤄진다.

출력:
  - 기본: .ua/discovery-knowledge-graph.json (항상 동작, 인메모리 → JSON 스냅샷)
  - 선택: Neo4j (NEO4J_PASSWORD 환경변수가 있을 때만 시도, 없으면 조용히 스킵.
    이미 실행 중인 로컬 Neo4j에 다른 프로젝트 데이터가 섞여 있을 수 있으므로
    모든 노드에 source2nd="2nd-brain-discovery" 프로퍼티를 붙여 구분 가능하게 한다)

사용:
  .venv/bin/python scripts/extract-knowledge-graph.py [--limit N] [--source raw/papers] [--dry-run]
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(os.path.expanduser("~/2nd"))
RAW_SOURCES = ["raw/papers", "raw/articles", "raw/web", "raw/youtube", "raw/notebooklm", "raw/transcripts"]
STATE_PATH = WIKI_ROOT / ".ua" / "extract-graph-state.json"
DISCOVERY_GRAPH_PATH = WIKI_ROOT / ".ua" / "discovery-knowledge-graph.json"

# graph_lib.py의 ONTOLOGY_CLASS_MAP과 어휘를 맞춰 canonical 그래프와 스키마 정합성을 유지한다.
ALLOWED_NODES = [
    "Technology", "Hardware", "Protocol", "Organization",
    "Regulation", "Mission", "Concept", "Person",
]

MAX_CHARS_PER_DOC = 6000
MODEL_ID = "anthropic/claude-haiku-4.5"


def sha256_of(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_state() -> dict:
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text())
        except Exception:
            return {}
    return {}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2))


def strip_frontmatter(text: str) -> tuple[str, str]:
    title = ""
    body = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[3:end]
            body = text[end + 4:]
            m = re.search(r'^title:\s*"?(.+?)"?\s*$', fm, re.MULTILINE)
            if m:
                title = m.group(1)
    return title, body.strip()


def discover_files(limit_dir: str | None) -> list[Path]:
    dirs = [limit_dir] if limit_dir else RAW_SOURCES
    files: list[Path] = []
    for d in dirs:
        base = WIKI_ROOT / d
        if not base.exists():
            continue
        files.extend(Path(p) for p in glob.glob(str(base / "**" / "*.md"), recursive=True))
    return sorted(set(files))


def pending_files(files: list[Path], state: dict) -> list[tuple[Path, str, str]]:
    pending = []
    for f in files:
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue
        digest = sha256_of(content)
        rel = str(f.relative_to(WIKI_ROOT))
        if state.get(rel) == digest:
            continue
        pending.append((f, content, digest))
    return pending


def build_transformer():
    from langchain_openai import ChatOpenAI
    from langchain_experimental.graph_transformers import LLMGraphTransformer

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ OPENROUTER_API_KEY 미설정 — LLM 추출을 진행할 수 없습니다.", file=sys.stderr)
        sys.exit(1)

    llm = ChatOpenAI(
        model=MODEL_ID,
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        temperature=0,
    )
    return LLMGraphTransformer(
        llm=llm,
        allowed_nodes=ALLOWED_NODES,
        node_properties=False,
        relationship_properties=False,
        additional_instructions=(
            "드론(UAV)·AI·로보틱스 도메인 논문/기사다. 구체적 기술명·프로토콜명·"
            "하드웨어명·기관명·규정명 위주로 추출하고, 일반명사나 모호한 개념은 "
            "제외해라. 노드 이름은 문서에서 실제 쓰인 고유명사/기술명을 그대로 "
            "사용해라 (예: PX4, MAVLink, ArduPilot, Pixhawk 6X)."
        ),
    )


def to_discovery_nodes_edges(graph_documents, source_map) -> tuple[list[dict], list[dict]]:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    for gd in graph_documents:
        src_rel = source_map.get(id(gd), "")
        for n in gd.nodes:
            node_id = str(n.id).strip()
            if not node_id:
                continue
            if node_id not in nodes:
                nodes[node_id] = {
                    "id": node_id,
                    "name": node_id,
                    "layer": "Discovery",
                    "domain": "",
                    "tags": [],
                    "status": "auto-extracted",
                    "ontologyClass": n.type,
                    "sources": [src_rel] if src_rel else [],
                }
            elif src_rel and src_rel not in nodes[node_id]["sources"]:
                nodes[node_id]["sources"].append(src_rel)
        for r in gd.relationships:
            edges.append({
                "source": str(r.source.id).strip(),
                "target": str(r.target.id).strip(),
                "type": r.type,
                "evidence": [src_rel] if src_rel else [],
                "confidence": "unverified",
            })
    return list(nodes.values()), edges


def merge_into_discovery_graph(new_nodes: list[dict], new_edges: list[dict]) -> dict:
    if DISCOVERY_GRAPH_PATH.exists():
        graph = json.loads(DISCOVERY_GRAPH_PATH.read_text())
    else:
        graph = {"nodes": [], "edges": []}

    existing_by_id = {n["id"]: n for n in graph["nodes"]}
    for n in new_nodes:
        if n["id"] in existing_by_id:
            ex = existing_by_id[n["id"]]
            for s in n["sources"]:
                if s not in ex.setdefault("sources", []):
                    ex["sources"].append(s)
        else:
            graph["nodes"].append(n)
            existing_by_id[n["id"]] = n

    existing_edge_keys = {(e["source"], e["target"], e["type"]) for e in graph["edges"]}
    for e in new_edges:
        key = (e["source"], e["target"], e["type"])
        if key not in existing_edge_keys:
            graph["edges"].append(e)
            existing_edge_keys.add(key)

    return graph


def sync_to_neo4j(graph_documents) -> int:
    password = os.environ.get("NEO4J_PASSWORD")
    if not password:
        print("ℹ️  NEO4J_PASSWORD 미설정 — Neo4j 동기화는 건너뜁니다(discovery JSON에만 저장됨).")
        return 0

    from langchain_neo4j import Neo4jGraph
    from langchain_neo4j.graphs.graph_document import (
        GraphDocument as Neo4jGraphDocument,
        Node as Neo4jNode,
        Relationship as Neo4jRelationship,
    )

    url = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
    username = os.environ.get("NEO4J_USERNAME", "neo4j")

    try:
        graph = Neo4jGraph(url=url, username=username, password=password)
    except Exception as e:
        print(f"⚠️  Neo4j 연결 실패({e}) — discovery JSON만 저장됨.", file=sys.stderr)
        return 0

    converted = []
    for gd in graph_documents:
        nodes = [
            Neo4jNode(id=n.id, type=n.type, properties={**n.properties, "source2nd": "2nd-brain-discovery"})
            for n in gd.nodes
        ]
        rels = [
            Neo4jRelationship(
                source=Neo4jNode(id=r.source.id, type=r.source.type),
                target=Neo4jNode(id=r.target.id, type=r.target.type),
                type=r.type,
                properties=r.properties,
            )
            for r in gd.relationships
        ]
        converted.append(Neo4jGraphDocument(nodes=nodes, relationships=rels, source=gd.source))

    graph.add_graph_documents(converted, baseEntityLabel=True)
    return sum(len(gd.nodes) for gd in converted)


def main() -> None:
    parser = argparse.ArgumentParser(description="raw/ 문서에서 LLM 기반 개념/관계 자동 추출 → 지식그래프 빌드")
    parser.add_argument("--limit", type=int, default=8, help="이번 실행에서 처리할 신규 문서 최대 개수 (기본 8, 비용 안전장치)")
    parser.add_argument("--source", type=str, default=None, help="특정 raw 하위 디렉토리만 처리 (예: raw/papers)")
    parser.add_argument("--dry-run", action="store_true", help="추출만 하고 파일/Neo4j에 저장하지 않음")
    args = parser.parse_args()

    state = load_state()
    files = discover_files(args.source)
    pending = pending_files(files, state)

    if not pending:
        print("✅ 신규/변경된 raw 문서가 없습니다. 처리할 것이 없습니다.")
        return

    batch = pending[: args.limit]
    print(f"📄 신규 문서 {len(pending)}개 발견 (이번 실행 {len(batch)}개 처리, --limit {args.limit})")

    transformer = build_transformer()

    from langchain_core.documents import Document

    documents = []
    doc_meta = []
    for path, content, digest in batch:
        title, body = strip_frontmatter(content)
        rel = str(path.relative_to(WIKI_ROOT))
        doc = Document(page_content=body[:MAX_CHARS_PER_DOC], metadata={"source": rel, "title": title})
        documents.append(doc)
        doc_meta.append((path, digest, rel))

    print("🧠 LLM 추출 실행 중 (문서당 1회 호출)...")
    graph_documents = []
    source_map: dict[int, str] = {}
    for doc, (path, digest, rel) in zip(documents, doc_meta):
        try:
            gd_list = transformer.convert_to_graph_documents([doc])
        except Exception as e:
            print(f"  ⚠️  {rel} 추출 실패: {e}", file=sys.stderr)
            continue
        for gd in gd_list:
            graph_documents.append(gd)
            source_map[id(gd)] = rel
        n_nodes = len(gd_list[0].nodes) if gd_list else 0
        n_rels = len(gd_list[0].relationships) if gd_list else 0
        print(f"  ✓ {rel} → 노드 {n_nodes}개, 관계 {n_rels}개")

    new_nodes, new_edges = to_discovery_nodes_edges(graph_documents, source_map)
    print(f"\n📊 추출 결과: 노드 {len(new_nodes)}개, 관계 {len(new_edges)}개 (문서 {len(graph_documents)}개 처리)")

    if args.dry_run:
        print("🔍 --dry-run: discovery JSON/Neo4j에 저장하지 않음")
        return

    merged = merge_into_discovery_graph(new_nodes, new_edges)
    DISCOVERY_GRAPH_PATH.parent.mkdir(parents=True, exist_ok=True)
    DISCOVERY_GRAPH_PATH.write_text(json.dumps(merged, ensure_ascii=False, indent=2))
    print(f"💾 저장: {DISCOVERY_GRAPH_PATH} (총 노드 {len(merged['nodes'])}개, 총 엣지 {len(merged['edges'])}개)")

    neo4j_count = sync_to_neo4j(graph_documents)
    if neo4j_count:
        print(f"🔗 Neo4j 동기화: 노드 {neo4j_count}개 반영")

    for path, digest, rel in doc_meta:
        state[rel] = digest
    save_state(state)
    print(f"✅ 처리 완료. 남은 미처리 문서: {len(pending) - len(batch)}개")


if __name__ == "__main__":
    main()
