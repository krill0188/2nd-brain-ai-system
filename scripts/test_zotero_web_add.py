#!/usr/bin/env python3
"""
test_zotero_web_add.py — zotero-web-add.py 단위 테스트.

이 저장소에는 테스트 프레임워크(pytest 등)가 없다 — 새 의존성을 추가하지
않고 기존 스크립트들과 같은 스타일(assert 기반, 표준 라이브러리만)로 작성.
네트워크 호출 없이 api_request()를 monkeypatch해서 전부 검증한다.

실행:
  python3 scripts/test_zotero_web_add.py
성공 시 종료코드 0, 실패 시 AssertionError와 함께 종료코드 1.
"""
import importlib.util
import io
import json
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parent / "zotero-web-add.py"
spec = importlib.util.spec_from_file_location("zotero_web_add", MODULE_PATH)
zwa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(zwa)


def with_tmp_state(fn):
    orig_state = zwa.STATE_PATH
    orig_key, orig_uid = zwa.API_KEY, zwa.USER_ID
    with tempfile.TemporaryDirectory() as td:
        zwa.STATE_PATH = Path(td) / "zotero-pushed.txt"
        zwa.API_KEY, zwa.USER_ID = "test-key", "12345"
        try:
            fn()
        finally:
            zwa.STATE_PATH = orig_state
            zwa.API_KEY, zwa.USER_ID = orig_key, orig_uid


def test_build_creators_splits_first_last():
    creators = zwa.build_creators(["Linghui Miao", "Shijian Gao"])
    assert creators == [
        {"creatorType": "author", "firstName": "Linghui", "lastName": "Miao"},
        {"creatorType": "author", "firstName": "Shijian", "lastName": "Gao"},
    ]
    print("PASS test_build_creators_splits_first_last")


def test_build_creators_single_word_name_falls_back_to_lastname_only():
    creators = zwa.build_creators(["Cher"])
    assert creators == [{"creatorType": "author", "firstName": "", "lastName": "Cher"}]
    print("PASS test_build_creators_single_word_name_falls_back_to_lastname_only")


def test_find_existing_by_title_matches_case_insensitively():
    def run():
        def fake_api_request(method, path, **kwargs):
            assert method == "GET"
            assert "q=" in path
            return 200, json.dumps([
                {"key": "JF9I6VDL", "data": {"title": "UAV Swarming for Air-Ground ISAC via Cross-Region Cooperation"}},
            ]).encode()

        orig = zwa.api_request
        zwa.api_request = fake_api_request
        try:
            found = zwa.find_existing_by_title("uav swarming for air-ground isac via cross-region cooperation")
        finally:
            zwa.api_request = orig
        assert found == "JF9I6VDL"

    with_tmp_state(run)
    print("PASS test_find_existing_by_title_matches_case_insensitively")


def test_find_existing_by_title_no_match_returns_none():
    def run():
        def fake_api_request(method, path, **kwargs):
            return 200, json.dumps([
                {"key": "OTHER01", "data": {"title": "Completely Different Paper"}},
            ]).encode()

        orig = zwa.api_request
        zwa.api_request = fake_api_request
        try:
            found = zwa.find_existing_by_title("A Paper Not In The Library")
        finally:
            zwa.api_request = orig
        assert found is None

    with_tmp_state(run)
    print("PASS test_find_existing_by_title_no_match_returns_none")


def test_main_skips_when_server_already_has_matching_title():
    # 2026-08-10 실측 발견: 로컬 state 파일만 믿으면, 브라우저로 이미 수동 추가한
    # 논문을 자동수집이 다시 push해서 Zotero에 중복 아이템을 만든다. 이 테스트는
    # 그 정확한 시나리오(로컬 state엔 없음, 서버엔 이미 있음)를 재현한다.
    def run():
        create_called = []

        def fake_api_request(method, path, **kwargs):
            if method == "GET" and "/items?q=" in path:
                return 200, json.dumps([
                    {"key": "EXIST01", "data": {"title": "Duplicate Test Paper"}},
                ]).encode()
            create_called.append((method, path))
            return 200, b"{}"

        orig = zwa.api_request
        zwa.api_request = fake_api_request
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(json.dumps({
            "title": "Duplicate Test Paper", "authors": ["A B"], "abstract": "x",
            "arxiv_id": "1111.11111", "url": "https://arxiv.org/abs/1111.11111",
            "pdf_url": "https://arxiv.org/pdf/1111.11111", "date": "2026-08-10",
        }))
        out = io.StringIO()
        try:
            with redirect_stdout(out):
                zwa.main()
        finally:
            zwa.api_request = orig
            sys.stdin = stdin_backup

        assert not create_called, "서버에 이미 있으면 아이템 생성 API를 호출하면 안 됨"
        assert "이미 존재" in out.getvalue()
        assert "1111.11111" in zwa.load_pushed() or "https://arxiv.org/abs/1111.11111" in zwa.load_pushed(), \
            "다음부터 서버 재조회 없이 스킵하도록 로컬 state에도 기록해야 함"

    with_tmp_state(run)
    print("PASS test_main_skips_when_server_already_has_matching_title")


def test_main_skips_when_already_in_local_state():
    def run():
        zwa.mark_pushed("https://arxiv.org/abs/2222.22222")
        called = []

        def fake_api_request(method, path, **kwargs):
            called.append((method, path))
            return 200, b"{}"

        orig = zwa.api_request
        zwa.api_request = fake_api_request
        stdin_backup = sys.stdin
        sys.stdin = io.StringIO(json.dumps({
            "title": "Already Pushed Paper", "authors": [], "abstract": "",
            "arxiv_id": "2222.22222", "url": "https://arxiv.org/abs/2222.22222",
        }))
        out = io.StringIO()
        try:
            with redirect_stdout(out):
                zwa.main()
        finally:
            zwa.api_request = orig
            sys.stdin = stdin_backup

        assert not called, "로컬 state에 이미 있으면 서버 조회조차 하면 안 됨(불필요한 API 호출 절약)"
        assert "이미 push됨" in out.getvalue()

    with_tmp_state(run)
    print("PASS test_main_skips_when_already_in_local_state")


if __name__ == "__main__":
    tests = [v for k, v in list(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
    print(f"\n전체 {len(tests)}개 테스트 통과")
