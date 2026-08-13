#!/usr/bin/env python3
"""test_build_owl.py — build-owl.py 단위 테스트.

이 저장소 컨벤션(assert 기반, 표준 라이브러리만)을 따르되, rdflib/owlready2는
이번 작업으로 .venv에 신규 설치된 의존성이라 임포트 실패 시 스킵한다(다른
스크립트들처럼 "새 의존성 추가 안 함" 원칙과 다른 예외 케이스임을 명시).

실행:
  source .venv/bin/activate && python3 scripts/test_build_owl.py
"""
import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    import owlready2  # noqa: F401
except ImportError:
    print("SKIP: owlready2 미설치 — .venv 활성화 후 재실행 필요")
    sys.exit(0)

spec = importlib.util.spec_from_file_location(
    "build_owl", Path(__file__).resolve().parent / "build-owl.py"
)
build_owl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_owl)


def test_object_properties_have_unique_inverse_names():
    """ONTOLOGY_SPEC.md 원본의 mountedOn 중복 버그(hasSensor/hasActuator가 같은
    역관계 이름 재사용) 재발 방지 회귀 테스트."""
    inverses = [inv for _, _, _, inv in build_owl.OBJECT_PROPERTIES if inv]
    dupes = {x for x in inverses if inverses.count(x) > 1}
    assert not dupes, f"역관계 이름 중복(OWL inverseOf는 1:1 필요): {dupes}"
    print("PASS: object property 역관계 이름 전부 유일함")


def test_build_produces_consistent_ontology():
    stats = build_owl.build(reason=True)
    assert stats["classes"] == 53, stats["classes"]
    assert stats["object_properties"] == 20, stats["object_properties"]
    assert stats["pages"] == 195, stats["pages"]
    assert stats["reasoner_result"] and "일관성 검사 통과" in stats["reasoner_result"], stats["reasoner_result"]
    print("PASS: 빌드 + HermiT 추론 결과 일관됨(모순 없음)")


def test_technology_class_mismatch_flagged_not_silently_dropped():
    """O1 매핑이 만든 'Technology' ontologyClass가 class-hierarchy.json 53개
    클래스에 없다는 걸 조용히 무시하지 않고 명시적으로 보고하는지 확인
    (SCHEMA.md '억지로 분류하지 않는다' 원칙과 동일하게, 억지로 숨기지도 않음)."""
    stats = build_owl.build(reason=False)
    assert stats["skipped_class_mismatch"].get("Technology", 0) > 0, (
        "Technology 미스매치가 사라짐 — class-hierarchy.json이 갱신됐거나 로직이 바뀐 것, 재확인 필요"
    )
    print(f"PASS: 'Technology'(class-hierarchy.json에 없는 값) {stats['skipped_class_mismatch']['Technology']}건 명시적으로 보고됨")


if __name__ == "__main__":
    tests = [
        test_object_properties_have_unique_inverse_names,
        test_build_produces_consistent_ontology,
        test_technology_class_mismatch_flagged_not_silently_dropped,
    ]
    failed = 0
    for t in tests:
        try:
            t()
        except AssertionError as e:
            print(f"FAIL: {t.__name__} — {e}")
            failed += 1
    print(f"\n{len(tests) - failed}/{len(tests)} 통과")
    sys.exit(1 if failed else 0)
