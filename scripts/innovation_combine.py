"""innovation_combine.py — Innovation Engine의 Cross-Domain Scan(§3.1 Novel
Combination) 기계 파트. INNOVATION_ENGINE.md §7 결정사항 3에 대한 답:
"의도적으로 먼 조합"을 두 가지 기계적 필터로 정의한다(무작위 방지) —
(1) ontologyClass가 서로 다름, (2) 그래프에 기존 엣지로 이미 연결돼
있지 않음(이미 알려진 관계면 "새 조합"이 아니다).

LLM을 호출하지 않는다 — 순수 그래프 순회. 실제 창의적 결합 문구는
innovations/prompts/combination.md 단계(LLM)의 몫이다.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

GRAPH_PATH = Path(__file__).resolve().parent.parent / ".ua" / "drone-knowledge-graph.json"


def load_graph(path: Path = GRAPH_PATH) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"nodes": [], "edges": []}


def _connected_pairs(graph: dict) -> set[tuple[str, str]]:
    pairs = set()
    for e in graph.get("edges", []):
        a, b = e.get("source"), e.get("target")
        if a and b:
            pairs.add(tuple(sorted((a, b))))
    return pairs


def pick_cross_domain_pair(
    graph: dict, avoid_pairs: set[tuple[str, str]] | None = None, rng: random.Random | None = None
) -> tuple[dict, dict] | None:
    """ontologyClass가 다르고, 그래프에서 직접 연결돼 있지 않은 노드 쌍을
    하나 고른다. 후보가 없으면 None(호출자가 라운드를 건너뛰거나 필터를
    완화할지 결정)."""
    rng = rng or random.Random()
    avoid_pairs = avoid_pairs or set()
    connected = _connected_pairs(graph)

    nodes = [n for n in graph.get("nodes", []) if n.get("ontologyClass")]
    candidates = []
    for i, a in enumerate(nodes):
        for b in nodes[i + 1:]:
            if a["ontologyClass"] == b["ontologyClass"]:
                continue
            key = tuple(sorted((a["id"], b["id"])))
            if key in connected or key in avoid_pairs:
                continue
            candidates.append((a, b))

    if not candidates:
        return None
    return rng.choice(candidates)


def format_pair_brief(pair: tuple[dict, dict]) -> str:
    a, b = pair
    return (
        f"- A: [{a.get('ontologyClass')}] {a.get('name')} (`{a['id']}`, domain={a.get('domain','')})\n"
        f"- B: [{b.get('ontologyClass')}] {b.get('name')} (`{b['id']}`, domain={b.get('domain','')})"
    )
