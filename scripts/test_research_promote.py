#!/usr/bin/env python3
"""
test_research_promote.py — research-promote.py의 Phase O2 변경(claim_type
frontmatter 필드 추가)에 대한 단위 테스트.

이 저장소에는 테스트 프레임워크(pytest 등)가 없다 — 새 의존성을 추가하지
않고 기존 스크립트들과 같은 스타일(assert 기반, 표준 라이브러리만)로 작성.

실행:
  python3 scripts/test_research_promote.py
성공 시 종료코드 0, 실패 시 AssertionError와 함께 종료코드 1.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import importlib.util

spec = importlib.util.spec_from_file_location(
    "research_promote", Path(__file__).resolve().parent / "research-promote.py"
)
research_promote = importlib.util.module_from_spec(spec)
spec.loader.exec_module(research_promote)


def make_claim(claim_type: str, claim_text: str = "테스트 클레임"):
    return {"id": "C1", "claim": claim_text, "claim_type": claim_type, "evidence": []}


def make_resolved():
    return {
        "canon": ["swarm-coordination"],
        "raw": ["raw/articles/example.md"],
        "wikilinks": ["swarm-coordination", "px4-architecture-deep"],
        "review": {"opposing_sources": "없음", "limitations": "없음"},
    }


REQUIRED_9_FIELDS = [
    "title", "created", "updated", "type", "tags",
    "sources", "confidence", "contested", "contradictions",
]


def parse_simple_frontmatter(text: str) -> dict:
    """SCHEMA.md와 동일한 최소 파서 — 이 테스트 전용, 값 형태만 확인."""
    assert text.startswith("---\n"), "frontmatter는 byte 0에서 --- 로 시작해야 한다"
    end = text.find("\n---\n", 4)
    assert end != -1, "닫는 --- 를 찾을 수 없음"
    fm_block = text[4:end]
    fields = {}
    for line in fm_block.split("\n"):
        m = re.match(r"^([a-zA-Z_]+):", line)
        if m:
            fields[m.group(1)] = True
    return fields


def test_inference_claim_has_claim_type():
    claim = make_claim("inference")
    page = research_promote.build_page(claim, make_resolved(), "test-session", "2026-08-02")
    fields = parse_simple_frontmatter(page)
    assert "claim_type" in fields, "claim_type 필드가 frontmatter에 없음"
    assert "claim_type: inference" in page, "claim_type 값이 올바르게 기록되지 않음"
    print("PASS: inference 클레임에 claim_type 필드 존재")


def test_hypothesis_claim_confidence_low():
    claim = make_claim("hypothesis")
    page = research_promote.build_page(claim, make_resolved(), "test-session", "2026-08-02")
    assert "confidence: low" in page, "hypothesis는 confidence: low 여야 함(기존 규칙, 회귀 확인)"
    assert "claim_type: hypothesis" in page
    print("PASS: hypothesis 클레임 confidence/claim_type 정상")


def test_required_9_fields_unchanged():
    """SCHEMA.md 9개 필수 필드 계약이 claim_type 추가로 깨지지 않았는지 확인
    (Rollback 조건: 이 테스트가 실패하면 즉시 되돌려야 함)."""
    claim = make_claim("inference")
    page = research_promote.build_page(claim, make_resolved(), "test-session", "2026-08-02")
    fields = parse_simple_frontmatter(page)
    missing = [f for f in REQUIRED_9_FIELDS if f not in fields]
    assert not missing, f"필수 9필드 중 누락: {missing}"
    print("PASS: 기존 9개 필수 필드 전부 유지됨(무회귀)")


def test_yaml_quote_escaping_regression():
    """이전 실사용 테스트에서 발견했던 버그(제목에 큰따옴표 있으면 YAML
    깨짐)가 재발하지 않는지 확인."""
    claim = make_claim("inference", claim_text='이것은 "인용부호"가 포함된 클레임이다')
    page = research_promote.build_page(claim, make_resolved(), "test-session", "2026-08-02")
    title_line = [l for l in page.split("\n") if l.startswith("title:")][0]
    assert title_line.count('\\"') == 2, "내부 인용부호가 이스케이프되지 않음(회귀)"
    print("PASS: YAML 인용부호 이스케이프 무회귀")


def test_fact_claim_type_rejected_by_validation():
    """validate_item()이 fact 클레임을 여전히 거부하는지 확인(Phase O2가
    다른 검증 로직을 건드리지 않았는지 회귀 확인)."""
    claims = {"C1": {"id": "C1", "claim": "x", "claim_type": "fact", "evidence": []}}
    reviews = {"C1": {"verification_status": "grounded"}}
    ok, reason, _ = research_promote.validate_item("C1", claims, reviews)
    assert not ok, "fact 클레임이 거부되지 않음(회귀)"
    assert "fact" in reason
    print("PASS: fact 클레임 거부 로직 무회귀")


if __name__ == "__main__":
    tests = [
        test_inference_claim_has_claim_type,
        test_hypothesis_claim_confidence_low,
        test_required_9_fields_unchanged,
        test_yaml_quote_escaping_regression,
        test_fact_claim_type_rejected_by_validation,
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
