#!/usr/bin/env python3
"""build-owl.py — ONTOLOGY_SPEC.md의 설계(클래스 계층·object/data property·
Track A 규칙)를 실제 OWL 온톨로지로 빌드한다.

성격: 실험적, 격리된 산출물. 이 스크립트는 daily-ingest/update-graph.sh 등
기존 프로덕션 파이프라인에서 자동 호출되지 않는다 — 수동 실행 전용이다.
자동 배선하지 않는 이유(마스터에게 이미 보고한 내용): OWL을 자동 파이프라인에
넣으면 canonical Markdown+JSON 그래프와 OWL 트리플이라는 두 표현을 매번
동기화해야 하는 새 기술부채가 생긴다(CURRENT_STATE_AUDIT.md가 지적한
"하이브리드 검색 로직 2중 구현"과 같은 패턴). 지금은 온디맨드 산출물로만
둔다.

카테고리 오류 방지(G1의 전례를 따름 — ONTOLOGY_GUIDED_GRAPHRAG_PLAN.md):
ONTOLOGY_SPEC.md §2의 20개 object property(hasSensor, dependsOn 등)는
실제 드론/미션 "인스턴스" 간 관계용이다. 위키 문서(canonical page)는
그 인스턴스 자체가 아니라 "그 개념을 설명하는 문서"이므로, 문서를 곧바로
:AIModel 같은 도메인 클래스의 인스턴스로 선언하지 않는다. 대신:
  - `:CanonicalPage` — 위키 문서 195개 전부가 속하는 별도 클래스(북키핑용)
  - `:aboutClass` — CanonicalPage → owl:Class, "이 문서가 설명하는 온톨로지
    클래스"를 가리키는 메타 링크 (문서 ≠ 인스턴스라는 구분을 지킴)
  - `:docRelated`/`:docWikilink`/`:docEvidences` — 문서 간 관계 전용 어휘
    (Track A/B 도메인 relation과 다른 네임스페이스, G1과 동일 원칙)
ONTOLOGY_SPEC.md §2/§3의 도메인 object/data property는 TBox(스키마)로만
선언한다 — Track B(실시간 드론 인스턴스)가 없어 ABox 인스턴스화는 안 한다
(ONTOLOGY_IMPLEMENTATION_ROADMAP.md의 Track A/B 분리 결정을 그대로 따름).

실행:
  source .venv/bin/activate
  python3 scripts/build-owl.py            # .ua/ontology.owl 생성 + 리포트
  python3 scripts/build-owl.py --reason   # 생성 후 HermiT 추론기로 일관성 검사

출력: .ua/ontology.owl (RDF/XML), stdout에 빌드 통계 + (옵션) 추론 결과.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = ROOT / ".ua" / "ontology.owl"

# ONTOLOGY_SPEC.md §2 — Object Properties (Domain, Range, inverse)
# 전부 TBox 선언만 함 (Track B 인스턴스 없음 — ABox 미생성)
OBJECT_PROPERTIES = [
    # ONTOLOGY_SPEC.md 원본은 hasSensor/hasActuator 둘 다 역관계로 "mountedOn"을
    # 재사용하는데, OWL의 inverseOf는 1:1이라 같은 이름을 두 속성에 동시에 못 쓴다
    # (실제 빌드하며 발견 — 마스터에게 별도 보고). sensorMountedOn/actuatorMountedOn으로
    # 분리해 원 설계의 의도(무엇에 무엇이 장착됐는지)는 그대로 유지.
    ("hasSensor", "Drone", "Sensor", "sensorMountedOn"),
    ("hasActuator", "Drone", "Actuator", "actuatorMountedOn"),
    ("hasComputeUnit", "Drone", "ComputeUnit", "installedIn"),
    ("runsOnFC", "FlightStack", "FlightController", "hostsFC"),
    ("runsOnCC", "ROS2", "CompanionComputer", "hostsCC"),  # AIModel도 domain이나 단순화(OR-도메인 미지원)
    ("controls", "FlightController", "Actuator", "controlledBy"),
    ("publishesTo", "ROS2Node", "ROS2Topic", None),
    ("subscribesTo", "ROS2Node", "ROS2Topic", None),
    ("partOfMission", "Task", "Mission", "hasTask"),
    ("dependsOn", "Task", "Task", "blocks"),
    ("performedBy", "Task", "Drone", "executesTask"),
    ("triggeredBy", "Task", "VoiceCommand", "triggers"),
    ("interpretedBy", "VoiceCommand", "VoiceRecognitionModule", "interprets"),
    ("reasonedBy", "VoiceCommand", "AIModel", "reasonsAbout"),
    ("delegatesTo", "LLM", "SLM", "delegatedFrom"),
    ("consumes", "AIModel", "SensorReading", "consumedBy"),
    ("produces", "Task", "Telemetry", "producedBy"),
    ("coordinates", "SwarmCoordinator", "Drone", "coordinatedBy"),
    ("justifiedBy", "Mission", "KnowledgeClaim", "justifies"),
    ("approvedBy", "KnowledgeClaim", "HumanOperator", "approves"),
]

# ONTOLOGY_SPEC.md §3 — Data Properties (class, property, xsd type)
DATA_PROPERTIES = [
    ("Drone", "droneId", "string"), ("Drone", "model", "string"),
    ("Drone", "weightKg", "float"), ("Drone", "maxPayloadKg", "float"),
    ("Sensor", "sensorType", "string"), ("Sensor", "updateRateHz", "float"),
    ("Task", "taskId", "string"), ("Task", "status", "string"), ("Task", "priority", "string"),
    ("Mission", "missionId", "string"), ("Mission", "status", "string"),
    ("VoiceCommand", "transcript", "string"), ("VoiceCommand", "asrConfidence", "float"),
    ("AIModel", "modelName", "string"), ("AIModel", "parameterCount", "int"),
    ("AIModel", "deploymentLocation", "string"),
    ("KnowledgeClaim", "claimType", "string"), ("KnowledgeClaim", "verificationStatus", "string"),
]

# 문서 그래프(drone-knowledge-graph.json)의 실제 엣지 type -> 문서 전용 predicate
DOC_RELATIONS = {"related": "docRelated", "wikilink": "docWikilink", "evidences": "docEvidences"}


def load_class_hierarchy() -> dict[str, str | None]:
    return json.loads((ROOT / "ontology" / "class-hierarchy.json").read_text())["classes"]


def load_graph() -> dict:
    return json.loads((ROOT / ".ua" / "drone-knowledge-graph.json").read_text())


def safe_id(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]", "_", s)


def build(reason: bool) -> dict:
    from owlready2 import (
        get_ontology, Thing, ObjectProperty, DataProperty,
        AnnotationProperty, sync_reasoner,
    )

    onto = get_ontology("https://amaster.local/2nd-brain-ontology#")
    hierarchy = load_class_hierarchy()
    graph = load_graph()

    stats = {"classes": 0, "object_properties": 0, "data_properties": 0,
             "pages": 0, "typed_pages": 0, "doc_edges": 0, "skipped_class_mismatch": Counter()}

    with onto:
        # --- TBox: 클래스 계층 (ONTOLOGY_SPEC.md §1, class-hierarchy.json 그대로) ---
        owl_classes: dict[str, type] = {}

        def get_or_create_class(name: str) -> type:
            if name in owl_classes:
                return owl_classes[name]
            parent_name = hierarchy.get(name, {}).get("parent")  # class-hierarchy.json: {"parent": "X"|null}
            parent_cls = get_or_create_class(parent_name) if parent_name else Thing
            cls = type(name, (parent_cls,), {})
            owl_classes[name] = cls
            return cls

        for cname in hierarchy:
            get_or_create_class(cname)
        stats["classes"] = len(owl_classes)

        # 문서 북키핑 전용 클래스 (도메인 클래스와 분리 — 카테고리 오류 방지)
        class CanonicalPage(Thing):
            pass

        # --- TBox: object properties (ONTOLOGY_SPEC.md §2, ABox 없음 — Track B 미구현) ---
        owl_obj_props = {}
        for name, dom, rng, inv in OBJECT_PROPERTIES:
            if dom not in owl_classes or rng not in owl_classes:
                continue
            prop = type(name, (ObjectProperty,), {
                "domain": [owl_classes[dom]], "range": [owl_classes[rng]],
            })
            owl_obj_props[name] = prop
            stats["object_properties"] += 1
            if inv:
                inv_prop = type(inv, (ObjectProperty,), {"inverse_property": prop})
                owl_obj_props[inv] = inv_prop

        # --- TBox: data properties (ONTOLOGY_SPEC.md §3) ---
        for cls_name, prop_name, _xsd in DATA_PROPERTIES:
            if cls_name not in owl_classes:
                continue
            type(prop_name, (DataProperty,), {"domain": [owl_classes[cls_name]]})
            stats["data_properties"] += 1

        # --- 문서 관계 전용 object property (G1 원칙: 도메인 relation과 별도 어휘) ---
        doc_props = {}
        for edge_type, prop_name in DOC_RELATIONS.items():
            doc_props[edge_type] = type(prop_name, (ObjectProperty,), {
                "domain": [CanonicalPage], "range": [CanonicalPage],
            })
        about_class_prop = type("aboutClass", (AnnotationProperty,), {})

        # --- ABox: 195개 canonical 문서를 CanonicalPage 인스턴스로 (도메인 클래스로 직접
        # 타이핑하지 않음 — "문서"와 "인스턴스"는 다른 존재론적 층위, 대신 aboutClass로 연결) ---
        individuals: dict[str, object] = {}
        for node in graph["nodes"]:
            nid = safe_id(node["id"])
            ind = CanonicalPage(nid)
            individuals[node["id"]] = ind
            stats["pages"] += 1
            oclass = node.get("ontologyClass")
            if oclass and oclass in owl_classes:
                setattr(ind, "aboutClass", owl_classes[oclass].iri)
                stats["typed_pages"] += 1
            elif oclass:
                stats["skipped_class_mismatch"][oclass] += 1

        for edge in graph["edges"]:
            etype = edge.get("type")
            prop = doc_props.get(etype)
            src = individuals.get(edge.get("source"))
            dst = individuals.get(edge.get("target"))
            if prop and src is not None and dst is not None:
                getattr(src, prop.python_name).append(dst)
                stats["doc_edges"] += 1

    OUT_PATH.parent.mkdir(exist_ok=True)
    onto.save(file=str(OUT_PATH), format="rdfxml")

    reasoner_result = None
    if reason:
        try:
            with onto:
                sync_reasoner(infer_property_values=True)
            reasoner_result = "일관성 검사 통과 — 모순(inconsistent class) 없음"
        except Exception as e:  # owlready2가 비일관 시 OwlReadyInconsistentOntologyError 발생
            reasoner_result = f"비일관 발견 또는 추론기 오류: {e}"

    stats["reasoner_result"] = reasoner_result
    return stats


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--reason", action="store_true", help="빌드 후 HermiT 추론기로 일관성 검사")
    args = ap.parse_args()

    stats = build(reason=args.reason)

    print(f"OWL 빌드 완료: {OUT_PATH.relative_to(ROOT)}")
    print(f"  클래스: {stats['classes']}개 (class-hierarchy.json 그대로 전사)")
    print(f"  object property: {stats['object_properties']}개 (TBox만, ABox 없음 — Track B 미구현)")
    print(f"  data property: {stats['data_properties']}개 (TBox만)")
    print(f"  문서 인스턴스(CanonicalPage): {stats['pages']}개")
    print(f"  aboutClass 연결됨: {stats['typed_pages']}개 / {stats['pages']}개")
    if stats["skipped_class_mismatch"]:
        print(f"  ⚠ class-hierarchy.json에 없는 ontologyClass 값(연결 안 함): "
              f"{dict(stats['skipped_class_mismatch'])}")
    print(f"  문서 관계 엣지(docRelated/docWikilink/docEvidences): {stats['doc_edges']}개")
    if stats["reasoner_result"]:
        print(f"  추론기 결과: {stats['reasoner_result']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
