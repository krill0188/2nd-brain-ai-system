#!/usr/bin/env python3
"""
test_graph_lib.py — update-graph.sh G0(그래프 파일 분리)/G1(관계타입 세분화)
리팩터링에 대한 단위 테스트. 표준 라이브러리만 사용(이 저장소 관례).

실행: python3 scripts/test_graph_lib.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_lib


def test_parse_frontmatter_basic():
    text = '---\ntitle: "테스트"\ndomain: ai-agent\ntags: [a, b]\n---\n본문'
    fm = graph_lib.parse_frontmatter(text)
    assert fm["title"] == "테스트"
    assert fm["domain"] == "ai-agent"
    assert fm["tags"] == ["a", "b"]
    print("PASS: frontmatter 파싱 기본 동작(무회귀)")


def test_extract_links_by_section_evidence_heading():
    text = (
        "본문 서두에 [[prose-mention]] 언급.\n\n"
        "## 근거\n\n- [[evidence-source-a]]\n- [[evidence-source-b]]\n\n"
        "## 관련 개념\n\n[[related-x]] [[related-y]]\n"
    )
    results = graph_lib.extract_links_by_section(text)
    by_slug = dict(results)
    assert by_slug["prose-mention"] == "wikilink", "헤딩 밖 산문 언급은 wikilink 유지"
    assert by_slug["evidence-source-a"] == "evidences", "## 근거 아래 링크는 evidences"
    assert by_slug["evidence-source-b"] == "evidences"
    assert by_slug["related-x"] == "related", "## 관련 개념 아래 링크는 related"
    assert by_slug["related-y"] == "related"
    print("PASS: 섹션 맥락 기반 관계타입 분류(근거/관련/산문 3분류) 정상")


def test_extract_links_by_section_unrecognized_heading_stays_generic():
    """'## 핵심 기능'처럼 근거/관련 어느 쪽도 아닌 헤딩은 관계를 지어내지
    않고 기존과 같은 wikilink로 남아야 한다(과잉 분류 방지 회귀 확인)."""
    text = "## 핵심 기능\n\n[[some-feature]]\n"
    results = graph_lib.extract_links_by_section(text)
    assert results == [("some-feature", "wikilink")]
    print("PASS: 미인식 헤딩은 관계를 지어내지 않고 wikilink 유지(과잉분류 방지)")


def test_extract_links_by_section_reference_and_seealso_english():
    text = "## References\n\n[[paper-a]]\n\n## See Also\n\n[[topic-b]]\n"
    results = dict(graph_lib.extract_links_by_section(text))
    assert results["paper-a"] == "evidences"
    assert results["topic-b"] == "related"
    print("PASS: 영문 헤딩(References/See Also)도 동일하게 분류")


def test_ontology_class_for_domain_known_and_unknown():
    assert graph_lib.ontology_class_for_domain("ai-agent") == "AIModel"
    assert graph_lib.ontology_class_for_domain("flight-control") == "Technology"
    assert graph_lib.ontology_class_for_domain("no-such-domain") is None, \
        "매핑 안 되는 domain은 억지로 분류하지 않고 None"
    print("PASS: ontologyClass 매핑 — 알려진 도메인/미지 도메인 모두 정상")


def test_ontology_class_map_covers_registered_schema_tags():
    """SCHEMA.md 등록 드론 도메인 태그(2026-08-02 커버리지 보완분 포함) 전부
    ontologyClass 매핑을 갖는지 확인 — Phase O1 당시 15개 None이었던 갭
    보완 회귀 테스트."""
    registered = ["drone", "datalink", "swarm", "voice-control",
                  "drone-hw", "drone-sw", "drone-ai", "ai-agent"]
    missing = [d for d in registered if graph_lib.ontology_class_for_domain(d) is None]
    assert not missing, f"SCHEMA.md 등록 태그인데 ontologyClass 매핑 누락: {missing}"
    print("PASS: SCHEMA.md 등록 드론 도메인 태그 전부 ontologyClass 매핑 보유")


if __name__ == "__main__":
    tests = [
        test_parse_frontmatter_basic,
        test_extract_links_by_section_evidence_heading,
        test_extract_links_by_section_unrecognized_heading_stays_generic,
        test_extract_links_by_section_reference_and_seealso_english,
        test_ontology_class_for_domain_known_and_unknown,
        test_ontology_class_map_covers_registered_schema_tags,
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
