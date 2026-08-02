#!/usr/bin/env python3
"""test_ontology_lib.py — G2(클래스 계층 조회 테이블) 단위 테스트."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ontology_lib


def test_hierarchy_loads_and_has_expected_size():
    h = ontology_lib.load_hierarchy()
    assert len(h) > 30, f"클래스 수가 예상보다 적음: {len(h)}"
    assert h["PX4"] == "FlightStack"
    assert h["Thing"] is None
    print("PASS: 클래스 계층 로드 정상")


def test_get_ancestors_px4():
    ancestors = ontology_lib.get_ancestors("PX4")
    assert ancestors == ["FlightStack", "SoftwareSystem", "Thing"], ancestors
    print("PASS: PX4 조상 체인 정확(FlightStack→SoftwareSystem→Thing)")


def test_get_descendants_flightstack():
    descendants = set(ontology_lib.get_descendants("FlightStack"))
    assert descendants == {"PX4", "ArduPilot"}, descendants
    print("PASS: FlightStack 자손 = {PX4, ArduPilot} 정확")


def test_get_descendants_sensor_multi_level():
    descendants = set(ontology_lib.get_descendants("Sensor"))
    assert "IMU" in descendants and "GNSS" in descendants and "Camera" in descendants
    print("PASS: Sensor 자손에 IMU/GNSS/Camera 전부 포함")


def test_get_ancestors_no_cycle_infinite_loop():
    """순환 참조가 없는지 확인 — 있으면 get_ancestors가 무한루프 대신
    seen 가드로 멈춰야 한다(방어 로직 회귀 확인)."""
    for cls in ontology_lib.load_hierarchy():
        ancestors = ontology_lib.get_ancestors(cls)
        assert len(ancestors) < 20, f"{cls}: 비정상적으로 긴 조상 체인 — 순환 의심"
    print("PASS: 전체 클래스 순환 참조 없음")


def test_expand_query_class_terms_match():
    terms = ontology_lib.expand_query_class_terms("FlightStack 비교해줘")
    assert set(terms) == {"PX4", "ArduPilot"}, terms
    print("PASS: 'FlightStack' 질의 → PX4/ArduPilot 확장")


def test_expand_query_class_terms_no_match_returns_empty():
    terms = ontology_lib.expand_query_class_terms("오늘 날씨 어때")
    assert terms == [], terms
    print("PASS: 매칭 없는 질의는 빈 리스트(억지 확장 없음)")


if __name__ == "__main__":
    tests = [
        test_hierarchy_loads_and_has_expected_size,
        test_get_ancestors_px4,
        test_get_descendants_flightstack,
        test_get_descendants_sensor_multi_level,
        test_get_ancestors_no_cycle_infinite_loop,
        test_expand_query_class_terms_match,
        test_expand_query_class_terms_no_match_returns_empty,
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
