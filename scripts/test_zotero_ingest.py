#!/usr/bin/env python3
"""
test_zotero_ingest.py — zotero-ingest.py 첨부 파일 저장 기능(2026-08-10 추가)
단위 테스트: sha256_file, copy_attachment, find_pdf_attachment, parse_frontmatter,
build_markdown의 attachment_path/attachment_sha256 프론트매터 삽입, backfill_attachments.

이 저장소에는 테스트 프레임워크(pytest 등)가 없다 — 새 의존성을 추가하지
않고 기존 스크립트들과 같은 스타일(assert 기반, 표준 라이브러리만)로 작성.
네트워크·실제 Zotero 앱 없이 전부 tmp 디렉토리 + 모듈 전역 monkeypatch로 동작.

실행:
  python3 scripts/test_zotero_ingest.py
성공 시 종료코드 0, 실패 시 AssertionError와 함께 종료코드 1.
"""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parent / "zotero-ingest.py"
spec = importlib.util.spec_from_file_location("zotero_ingest", MODULE_PATH)
zi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(zi)


def with_tmp_repo(fn):
    """WIKI_ROOT/RAW_PAPERS/ATTACHMENT_ROOT/ZOTERO_DATA_DIR을 tmp로 바꿔 실제
    ~/2nd 레포를 절대 건드리지 않고 테스트한다. 끝나면 원상복구."""
    orig = (zi.WIKI_ROOT, zi.RAW_PAPERS, zi.ATTACHMENT_ROOT, zi.ZOTERO_DATA_DIR)
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        zi.WIKI_ROOT = root
        zi.RAW_PAPERS = root / "raw" / "papers"
        zi.ATTACHMENT_ROOT = zi.RAW_PAPERS / "files"
        zi.ZOTERO_DATA_DIR = root / "zotero-data"
        (zi.RAW_PAPERS / "swarm").mkdir(parents=True)
        (zi.ZOTERO_DATA_DIR / "storage" / "ABCD1234").mkdir(parents=True)
        try:
            fn(root)
        finally:
            zi.WIKI_ROOT, zi.RAW_PAPERS, zi.ATTACHMENT_ROOT, zi.ZOTERO_DATA_DIR = orig


def test_sha256_file():
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "sample.txt"
        f.write_bytes(b"hello world")
        import hashlib
        expected = hashlib.sha256(b"hello world").hexdigest()
        assert zi.sha256_file(f) == expected
    print("PASS test_sha256_file")


def test_copy_attachment_and_idempotency():
    def run(root):
        src = zi.ZOTERO_DATA_DIR / "storage" / "ABCD1234" / "paper.pdf"
        src.write_bytes(b"%PDF-1.4 fake pdf bytes")
        attachment = {"path": src, "filename": "paper.pdf", "content_type": "application/pdf"}

        meta1 = zi.copy_attachment(attachment, "swarm", "example-paper", dry_run=False)
        dest = zi.ATTACHMENT_ROOT / "swarm" / "example-paper.pdf"
        assert dest.exists(), "첨부가 raw/papers/files/<topic>/<slug>.pdf로 복사돼야 함"
        assert meta1["attachment_path"] == str(dest.relative_to(zi.WIKI_ROOT))
        assert meta1["attachment_sha256"] == zi.sha256_file(dest)

        # 두 번째 호출은 재복사 없이 기존 파일 기준으로 동일 결과를 반환해야 함(멱등)
        mtime_before = dest.stat().st_mtime_ns
        meta2 = zi.copy_attachment(attachment, "swarm", "example-paper", dry_run=False)
        assert dest.stat().st_mtime_ns == mtime_before, "이미 존재하는 첨부를 재복사하면 안 됨"
        assert meta2 == meta1

    with_tmp_repo(run)
    print("PASS test_copy_attachment_and_idempotency")


def test_copy_attachment_dry_run_does_not_write():
    def run(root):
        src = zi.ZOTERO_DATA_DIR / "storage" / "ABCD1234" / "paper.pdf"
        src.write_bytes(b"%PDF-1.4 fake pdf bytes")
        attachment = {"path": src, "filename": "paper.pdf", "content_type": "application/pdf"}

        meta = zi.copy_attachment(attachment, "swarm", "example-paper", dry_run=True)
        dest = zi.ATTACHMENT_ROOT / "swarm" / "example-paper.pdf"
        assert not dest.exists(), "dry-run은 실제 파일을 쓰면 안 됨"
        assert meta["attachment_sha256"] == "(dry-run)"

    with_tmp_repo(run)
    print("PASS test_copy_attachment_dry_run_does_not_write")


def test_find_pdf_attachment_prefers_imported_local_file():
    def run(root):
        # 로컬에 실제로 존재하는 imported_file 첨부만 채택해야 함
        stored = zi.ZOTERO_DATA_DIR / "storage" / "ABCD1234" / "paper.pdf"
        stored.write_bytes(b"%PDF-1.4")

        def fake_zotero_get(path):
            assert path == "items/PARENT01/children"
            return [
                {"key": "LINKED1", "data": {"itemType": "attachment", "linkMode": "linked_url",
                                             "filename": "", "contentType": "text/html"}},
                {"key": "ABCD1234", "data": {"itemType": "attachment", "linkMode": "imported_file",
                                             "filename": "paper.pdf", "contentType": "application/pdf"}},
            ]

        orig_get = zi.zotero_get
        zi.zotero_get = fake_zotero_get
        try:
            found = zi.find_pdf_attachment("PARENT01")
        finally:
            zi.zotero_get = orig_get

        assert found is not None
        assert found["path"] == stored
        assert found["filename"] == "paper.pdf"

    with_tmp_repo(run)
    print("PASS test_find_pdf_attachment_prefers_imported_local_file")


def test_find_pdf_attachment_missing_zotero_dir_returns_none():
    def run(root):
        shutil.rmtree(zi.ZOTERO_DATA_DIR)  # Zotero 미설치/다른 경로 상황 시뮬레이션
        zi._warned_missing_zotero_dir = False
        found = zi.find_pdf_attachment("PARENT01")
        assert found is None

    with_tmp_repo(run)
    print("PASS test_find_pdf_attachment_missing_zotero_dir_returns_none")


def test_build_markdown_includes_attachment_fields_when_present():
    item = {
        "key": "ZKEY01",
        "data": {
            "title": "Example Paper",
            "creators": [{"creatorType": "author", "lastName": "Kim", "firstName": "J"}],
            "date": "2026-01-01",
            "DOI": "10.1/example",
            "url": "https://example.com",
            "abstractNote": "abstract text",
            "itemType": "journalArticle",
            "tags": [{"tag": "swarm"}],
        },
    }
    md_with = zi.build_markdown(item, {"attachment_path": "raw/papers/files/swarm/x.pdf",
                                        "attachment_sha256": "deadbeef"})
    assert "attachment_path: raw/papers/files/swarm/x.pdf" in md_with
    assert "attachment_sha256: deadbeef" in md_with
    # attachment 필드는 sha256 필드보다 앞에 위치해야 함(레코드 본문 삽입 지점과 일관성)
    assert md_with.index("attachment_path:") < md_with.index("sha256:")

    md_without = zi.build_markdown(item, None)
    assert "attachment_path:" not in md_without
    print("PASS test_build_markdown_includes_attachment_fields_when_present")


def test_parse_frontmatter():
    text = '---\ntitle: "Example"\nzotero_key: ZKEY01\nsha256: abc123\n---\n\nbody\n'
    fm = zi.parse_frontmatter(text)
    assert fm["title"] == "Example"
    assert fm["zotero_key"] == "ZKEY01"
    assert fm["sha256"] == "abc123"
    print("PASS test_parse_frontmatter")


def test_backfill_patches_frontmatter_without_touching_body():
    def run(root):
        record = zi.RAW_PAPERS / "swarm" / "existing.md"
        original_text = (
            '---\n'
            'title: "Existing Paper"\n'
            'zotero_key: PARENT01\n'
            'tags: []\n'
            'sha256: keepme\n'
            '---\n\n'
            '# Existing Paper\n\nbody text unchanged\n'
        )
        record.write_text(original_text, encoding="utf-8")

        stored = zi.ZOTERO_DATA_DIR / "storage" / "ABCD1234" / "paper.pdf"
        stored.write_bytes(b"%PDF-1.4")

        def fake_zotero_get(path):
            return [{"key": "ABCD1234", "data": {"itemType": "attachment", "linkMode": "imported_file",
                                                   "filename": "paper.pdf", "contentType": "application/pdf"}}]

        orig_get = zi.zotero_get
        zi.zotero_get = fake_zotero_get
        try:
            zi.backfill_attachments(dry_run=False)
        finally:
            zi.zotero_get = orig_get

        patched = record.read_text(encoding="utf-8")
        assert "attachment_path: raw/papers/files/swarm/existing.pdf" in patched
        assert "attachment_sha256:" in patched
        assert "sha256: keepme" in patched, "기존 sha256 값은 절대 바뀌면 안 됨(SCHEMA.md 불변성 계약)"
        assert patched.endswith("# Existing Paper\n\nbody text unchanged\n"), \
            "'---' 이후 본문 바이트는 한 글자도 바뀌면 안 됨"

        # 재실행 시 이미 attachment_path가 있으므로 재패치하지 않아야 함(멱등)
        zi.zotero_get = fake_zotero_get
        try:
            zi.backfill_attachments(dry_run=False)
        finally:
            zi.zotero_get = orig_get
        assert record.read_text(encoding="utf-8") == patched

    with_tmp_repo(run)
    print("PASS test_backfill_patches_frontmatter_without_touching_body")


if __name__ == "__main__":
    tests = [v for k, v in list(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
    print(f"\n전체 {len(tests)}개 테스트 통과")
