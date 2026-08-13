#!/usr/bin/env python3
"""test_lint_knowledge.py — lint-knowledge.py(갭 A: daily-ingest 게이트) 단위 테스트.

이 저장소에는 테스트 프레임워크(pytest 등)가 없다 — 새 의존성을 추가하지
않고 기존 스크립트들(test_research_promote.py 등)과 같은 스타일(assert
기반, 표준 라이브러리만)로 작성.

실행:
  python3 scripts/test_lint_knowledge.py
"""
import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

spec = importlib.util.spec_from_file_location(
    "lint_knowledge", Path(__file__).resolve().parent / "lint-knowledge.py"
)
lint_knowledge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint_knowledge)

VALID_FM = """---
title: Test Page
created: 2026-08-13
updated: 2026-08-13
type: concept
tags: [drone-sw]
sources: [raw/articles/example.md]
confidence: medium
contested: false
contradictions: []
---

본문. [[px4-architecture-deep]] 그리고 [[ros2-drone-deep]] 참고.
"""


def _write(tmp_path: Path, name: str, content: str) -> Path:
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return p


def test_parse_frontmatter_extracts_all_9_fields():
    fm = lint_knowledge.parse_frontmatter(VALID_FM)
    for field in lint_knowledge.REQUIRED_FIELDS:
        assert field in fm, f"필드 누락: {field}"
    print("PASS: frontmatter 파서가 9필드 전부 추출")


def test_valid_page_has_no_errors(tmp_path=Path("/tmp/lint_knowledge_test")):
    tmp_path.mkdir(exist_ok=True)
    path = _write(tmp_path, "concept-ok.md", VALID_FM)
    path.parent.name  # noqa (디렉토리명이 concepts가 아니므로 type 체크는 스킵됨 — 별도 테스트에서 검증)
    errs = lint_knowledge.lint_file(path, slugs={"px4-architecture-deep", "ros2-drone-deep"})
    # type 불일치(임시 디렉토리명 mismatch)만 제외하고 나머지 필드는 전부 통과해야 함
    non_type_errs = [e for e in errs if not e.startswith("type 불일치")]
    assert non_type_errs == [], non_type_errs
    print("PASS: 정상 페이지는 type 외 위반 없음")


def test_missing_required_field_detected(tmp_path=Path("/tmp/lint_knowledge_test")):
    tmp_path.mkdir(exist_ok=True)
    broken = VALID_FM.replace("confidence: medium\n", "")
    path = _write(tmp_path, "concept-missing.md", broken)
    errs = lint_knowledge.lint_file(path, slugs={"px4-architecture-deep", "ros2-drone-deep"})
    assert any("confidence" in e for e in errs), errs
    print("PASS: 필수 필드 누락(confidence) 탐지")


def test_invalid_confidence_value_detected(tmp_path=Path("/tmp/lint_knowledge_test")):
    tmp_path.mkdir(exist_ok=True)
    broken = VALID_FM.replace("confidence: medium", "confidence: very-high")
    path = _write(tmp_path, "concept-badconf.md", broken)
    errs = lint_knowledge.lint_file(path, slugs={"px4-architecture-deep", "ros2-drone-deep"})
    assert any("confidence 값 무효" in e for e in errs), errs
    print("PASS: confidence 값 무효(very-high) 탐지")


def test_insufficient_wikilinks_detected(tmp_path=Path("/tmp/lint_knowledge_test")):
    tmp_path.mkdir(exist_ok=True)
    broken = VALID_FM.replace("[[px4-architecture-deep]] 그리고 [[ros2-drone-deep]] 참고.", "관련 문서 없음.")
    path = _write(tmp_path, "concept-nolinks.md", broken)
    errs = lint_knowledge.lint_file(path, slugs={"px4-architecture-deep", "ros2-drone-deep"})
    assert any("wikilink 2개 미만" in e for e in errs), errs
    print("PASS: wikilink 2개 미만 탐지")


def test_self_link_not_counted(tmp_path=Path("/tmp/lint_knowledge_test")):
    tmp_path.mkdir(exist_ok=True)
    content = VALID_FM.replace(
        "[[px4-architecture-deep]] 그리고 [[ros2-drone-deep]] 참고.",
        "[[concept-selflink]] 자기참조는 안 셈. [[px4-architecture-deep]] 하나뿐.",
    )
    path = _write(tmp_path, "concept-selflink.md", content)
    errs = lint_knowledge.lint_file(path, slugs={"px4-architecture-deep", "ros2-drone-deep", "concept-selflink"})
    assert any("wikilink 2개 미만" in e for e in errs), errs
    print("PASS: 자기참조 wikilink는 카운트에서 제외됨")


def test_type_directory_mismatch_detected(tmp_path=Path("/tmp/lint_knowledge_test/entities")):
    tmp_path.mkdir(parents=True, exist_ok=True)
    path = _write(tmp_path, "wrong-type.md", VALID_FM)  # type: concept, 디렉토리: entities
    errs = lint_knowledge.lint_file(path, slugs={"px4-architecture-deep", "ros2-drone-deep"})
    assert any("type 불일치" in e for e in errs), errs
    print("PASS: type/디렉토리 불일치 탐지")


def test_no_frontmatter_detected():
    path = Path("/tmp/lint_knowledge_test/concept-nofm.md")
    path.parent.mkdir(exist_ok=True)
    path.write_text("# 제목만 있고 frontmatter 없음\n", encoding="utf-8")
    errs = lint_knowledge.lint_file(path, slugs=set())
    assert any("frontmatter 없음" in e for e in errs), errs
    print("PASS: frontmatter 없는 파일 탐지")


def test_recent_files_respects_hours_cutoff():
    """워치독 모드(--recent-hours) — git과 무관하게 mtime만으로 선별하는지 확인."""
    import os
    import time as _time

    d = lint_knowledge.ROOT / "concepts"
    d.mkdir(parents=True, exist_ok=True)
    fresh = d / "_lint_test_fresh.md"
    stale = d / "_lint_test_stale.md"
    try:
        fresh.write_text(VALID_FM, encoding="utf-8")
        stale.write_text(VALID_FM, encoding="utf-8")
        old_time = _time.time() - 10 * 3600  # 10시간 전
        os.utime(stale, (old_time, old_time))

        found = {p.name for p in lint_knowledge.recent_files(hours=2)}
        assert "_lint_test_fresh.md" in found, found
        assert "_lint_test_stale.md" not in found, found
        print("PASS: recent_files가 mtime 기준으로 최신 파일만 선별(오래된 파일 제외)")
    finally:
        fresh.unlink(missing_ok=True)
        stale.unlink(missing_ok=True)


def test_quiet_mode_suppresses_clean_output_via_subprocess():
    """hermes --no-agent 워치독 규약: 위반 0건이면 stdout이 완전히 비어야 함."""
    import subprocess

    result = subprocess.run(
        [sys.executable, str(lint_knowledge.ROOT / "scripts" / "lint-knowledge.py"),
         "--recent-hours", "0.0000001", "--quiet"],
        capture_output=True, text=True,
    )
    assert result.stdout == "", repr(result.stdout)
    assert result.returncode == 0
    print("PASS: --quiet + 대상 없음(0시간 윈도)일 때 stdout 완전히 비어있음")


if __name__ == "__main__":
    tests = [
        test_parse_frontmatter_extracts_all_9_fields,
        test_valid_page_has_no_errors,
        test_missing_required_field_detected,
        test_invalid_confidence_value_detected,
        test_insufficient_wikilinks_detected,
        test_self_link_not_counted,
        test_type_directory_mismatch_detected,
        test_no_frontmatter_detected,
        test_recent_files_respects_hours_cutoff,
        test_quiet_mode_suppresses_clean_output_via_subprocess,
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
