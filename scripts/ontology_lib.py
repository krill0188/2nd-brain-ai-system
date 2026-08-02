"""ontology_lib.py — ONTOLOGY_SPEC.md 클래스 계층의 경량 조회 헬퍼 (G2/G3, 2026-08-02).

정식 OWL/DL 추론기를 쓰지 않는다(GRAPH_SCHEMA.md/현재 규모 판단과 동일 원칙 —
139노드 규모에서 정식 추론기는 과설계). parent 포인터 딕셔너리 하나로 조상/
자손 조회만 지원하는 게 이 모듈의 전체 범위다.

이 모듈은 "전 캐노니컬 페이지를 세밀 클래스로 재분류"하지 않는다 — 그건 이번
범위 밖이다(139페이지 각각을 근거 없이 세분류하면 새로운 오분류 리스크를
만든다). 대신 "질의 확장 사전"으로만 쓴다: 사용자가 상위 개념(예: FlightStack)
을 물으면 하위 클래스 이름(PX4/ArduPilot)을 검색어에 추가해, 이미 존재하는
제목/태그 기반 매칭이 그 하위 개념을 다루는 페이지를 더 잘 찾게 돕는다.
"""
from __future__ import annotations

import json
from pathlib import Path

_HIERARCHY_PATH = Path(__file__).resolve().parent.parent / "ontology" / "class-hierarchy.json"


def load_hierarchy(path: Path = _HIERARCHY_PATH) -> dict[str, str | None]:
    """{class_name: parent_name_or_None} 형태로 로드한다."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return {name: info.get("parent") for name, info in data.get("classes", {}).items()}


def get_ancestors(class_name: str, hierarchy: dict[str, str | None] | None = None) -> list[str]:
    hierarchy = hierarchy if hierarchy is not None else load_hierarchy()
    ancestors = []
    current = hierarchy.get(class_name)
    seen = set()
    while current and current not in seen:
        ancestors.append(current)
        seen.add(current)
        current = hierarchy.get(current)
    return ancestors


def get_descendants(class_name: str, hierarchy: dict[str, str | None] | None = None) -> list[str]:
    hierarchy = hierarchy if hierarchy is not None else load_hierarchy()
    children_map: dict[str, list[str]] = {}
    for name, parent in hierarchy.items():
        if parent:
            children_map.setdefault(parent, []).append(name)

    descendants: list[str] = []
    stack = list(children_map.get(class_name, []))
    seen = set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        descendants.append(node)
        stack.extend(children_map.get(node, []))
    return descendants


def expand_query_class_terms(query: str, hierarchy: dict[str, str | None] | None = None) -> list[str]:
    """질의 문자열에 클래스명이 (대소문자 무관) 포함돼 있으면 그 하위
    클래스명들을 반환한다 — 검색어에 추가로 섞어 넣을 후보. 매칭되는 게
    없으면 빈 리스트(억지로 확장하지 않음)."""
    hierarchy = hierarchy if hierarchy is not None else load_hierarchy()
    q_lower = query.lower()
    extra: list[str] = []
    for class_name in hierarchy:
        if class_name.lower() in q_lower:
            for d in get_descendants(class_name, hierarchy):
                if d not in extra:
                    extra.append(d)
    return extra
