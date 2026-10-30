"""fetch-law.py 시험 — 네트워크·.env 없이 합성 fixture로만 돈다(tests/fixtures/law/).

주의: fixture는 실제 API 응답이 아니라 합성 자료다. 이 시험이 통과해도 '실제 응답 형식과 일치'는 증명되지 않는다.
"""
import copy
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parent
FIXTURES = SCRIPTS.parent / "tests" / "fixtures" / "law"
spec = importlib.util.spec_from_file_location("fetch_law", SCRIPTS / "fetch-law.py")
fl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fl)

NAME = "항공안전법"
LAW_ID = "law:aviation-safety-act"


def payload():
    return json.loads((FIXTURES / "law_aviation-safety-act.json").read_text(encoding="utf-8"))


class Workspace:
    """임시 laws.json·fixture·보존 디렉터리."""

    def __init__(self, tmp, pl=None):
        self.tmp = Path(tmp)
        self.fix = self.tmp / "fix"
        self.fix.mkdir()
        self.store = self.tmp / "store"
        self.laws = self.tmp / "laws.json"
        self.laws.write_text(json.dumps({"confirmed": True, "laws": [{"id": LAW_ID, "name": NAME}]}, ensure_ascii=False), encoding="utf-8")
        self.set_payload(pl or payload())

    def set_payload(self, pl):
        (self.fix / "law_aviation-safety-act.json").write_text(json.dumps(pl, ensure_ascii=False), encoding="utf-8")

    def run(self, *extra):
        sent = []
        with patch.object(fl, "append_to_feed", side_effect=lambda items: sent.extend(items)):
            code = fl.main(["--laws", str(self.laws), "--store-dir", str(self.store), "--fixture-dir", str(self.fix), *extra])
        return code, sent


class Units(unittest.TestCase):
    def test_iso_day(self):
        self.assertEqual(fl.iso_day("20260401"), "2026-04-01")
        for bad in ("", None, "2026-04-01", "20260231", "2026", "abcdefgh"):
            self.assertIsNone(fl.iso_day(bad), bad)

    def test_pick_exact_ignores_similar_names(self):
        self.assertEqual(fl.pick_exact(payload(), NAME)["법령일련번호"], "900001")
        self.assertEqual(fl.pick_exact(payload(), "항공안전법 시행령")["법령일련번호"], "900002")
        self.assertIsNone(fl.pick_exact(payload(), "항공법"))

    def test_pick_exact_single_object_result(self):
        pl = {"LawSearch": {"law": payload()["LawSearch"]["law"][0]}}  # 1건이면 리스트가 아니라 객체
        self.assertEqual(fl.pick_exact(pl, NAME)["법령일련번호"], "900001")

    def test_pick_exact_prefers_current(self):
        old = copy.deepcopy(payload()["LawSearch"]["law"][0])
        old.update({"현행연혁코드": "연혁", "법령일련번호": "111"})
        pl = {"LawSearch": {"law": [old, payload()["LawSearch"]["law"][0]]}}
        self.assertEqual(fl.pick_exact(pl, NAME)["법령일련번호"], "900001")

    def test_pick_exact_empty(self):
        for pl in ({}, None, {"LawSearch": {}}, {"LawSearch": {"law": []}}):
            self.assertIsNone(fl.pick_exact(pl, NAME))

    def test_clean_record_drops_key_bearing_link(self):
        rec = fl.clean_record(fl.pick_exact(payload(), NAME))
        self.assertNotIn("법령상세링크", rec)
        self.assertNotIn("FAKEKEY123", json.dumps(rec, ensure_ascii=False))

    def test_feed_item_shape_and_no_secret(self):
        item = fl.to_feed_item(NAME, fl.clean_record(fl.pick_exact(payload(), NAME)))
        self.assertEqual(item["title"], "[법령] 항공안전법 · 일부개정 · 시행 2026-04-01")
        self.assertEqual((item["type"], item["region"], item["source"], item["summary"]), ("regulation", "KR", "law.go.kr", ""))
        self.assertEqual(item["published"], "2025-10-01")
        self.assertTrue(item["url"].startswith("https://www.law.go.kr/법령/") and item["url"].endswith("#rev-900001"))
        self.assertNotIn("OC=", json.dumps(item, ensure_ascii=False))

    def test_feed_item_refuses_invented_dates(self):
        rec = fl.clean_record(fl.pick_exact(payload(), NAME))
        for field in ("공포일자", "시행일자", "법령일련번호"):
            bad = {k: v for k, v in rec.items() if k != field}
            self.assertIsNone(fl.to_feed_item(NAME, bad), field)
        self.assertIsNone(fl.to_feed_item(NAME, {**rec, "시행일자": "20261301"}))

    def test_revision_gets_distinct_url_and_title(self):
        a = fl.to_feed_item(NAME, fl.clean_record(fl.pick_exact(payload(), NAME)))
        pl = payload()
        pl["LawSearch"]["law"][0].update({"법령일련번호": "900009", "시행일자": "20270101"})
        b = fl.to_feed_item(NAME, fl.clean_record(fl.pick_exact(pl, NAME)))
        self.assertNotEqual(a["url"], b["url"])
        self.assertNotEqual(a["title"], b["title"])


class Main(unittest.TestCase):
    def test_first_run_emits_and_stores_second_run_is_quiet(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp)
            code, sent = ws.run()
            self.assertEqual((code, len(sent)), (0, 1))
            stored = list((ws.store / "law_aviation-safety-act").glob("*.json"))
            self.assertEqual(len(stored), 1)
            body = stored[0].read_text(encoding="utf-8")
            self.assertNotIn("FAKEKEY123", body)
            self.assertNotIn("OC=", body)
            code, sent = ws.run()
            self.assertEqual((code, len(sent)), (0, 0))  # 같은 내용이면 피드에 다시 넣지 않는다

    def test_amendment_emits_new_event(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp)
            ws.run()
            pl = payload()
            pl["LawSearch"]["law"][0].update({"법령일련번호": "900009", "시행일자": "20270101", "공포일자": "20260701"})
            ws.set_payload(pl)
            code, sent = ws.run()
            self.assertEqual((code, len(sent)), (0, 1))
            self.assertIn("시행 2027-01-01", sent[0]["title"])

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp)
            code, sent = ws.run("--dry-run")
            self.assertEqual((code, sent), (0, []))
            self.assertFalse(ws.store.exists())

    def test_missing_law_is_failure_exit_2(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp, {"LawSearch": {"law": []}})
            code, sent = ws.run()
            self.assertEqual((code, sent), (2, []))

    def test_feed_failure_keeps_store_empty_so_next_run_retries(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp)
            with patch.object(fl, "append_to_feed", side_effect=RuntimeError("boom")):
                code = fl.main(["--laws", str(ws.laws), "--store-dir", str(ws.store), "--fixture-dir", str(ws.fix)])
            self.assertEqual(code, 2)
            self.assertEqual(list(ws.store.glob("law_*")), [])  # 보존 파일은 없다(실행 기록 runs.jsonl 만 남음)
            code, sent = ws.run()
            self.assertEqual((code, len(sent)), (0, 1))

    def test_no_key_skips_without_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp)
            with patch.object(fl, "load_oc", return_value=""), patch.object(fl, "fetch_remote", side_effect=AssertionError("네트워크 호출 금지")):
                code = fl.main(["--laws", str(ws.laws), "--store-dir", str(ws.store)])
            self.assertEqual(code, 0)

    def test_run_log_records_outcomes_without_secrets(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp)
            ws.run()                          # ok(신규 1)
            ws.run()                          # ok(변경없음 1)
            ws.run("--dry-run")               # dry-run 은 기록하지 않는다
            ws.set_payload({"LawSearch": {"law": []}})
            ws.run()                          # failed
            rows = [json.loads(x) for x in (ws.store / "runs.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual([r["status"] for r in rows], ["ok", "ok", "failed"])
            self.assertEqual((rows[0]["new"], rows[1]["unchanged"], len(rows[2]["failed"])), (1, 1, 1))
            self.assertNotIn("OC=", json.dumps(rows, ensure_ascii=False))

    def test_no_key_run_is_logged_as_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp)
            with patch.object(fl, "load_oc", return_value=""):
                fl.main(["--laws", str(ws.laws), "--store-dir", str(ws.store)])
            rows = [json.loads(x) for x in (ws.store / "runs.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual([r["status"] for r in rows], ["skipped-no-key"])

    def test_bad_config_is_exit_1(self):
        self.assertEqual(fl.main(["--laws", "/nonexistent/laws.json"]), 1)

    def test_remote_error_message_does_not_leak_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            ws = Workspace(tmp)
            import io
            import urllib.error
            from contextlib import redirect_stderr, redirect_stdout
            url = "https://www.law.go.kr/DRF/lawSearch.do?OC=SECRETKEY&query=x"
            # 실제 네트워크 예외(URLError·HTTPError)는 메시지·속성에 URL 이 들어갈 수 있다
            for err in (RuntimeError(url), urllib.error.URLError(f"failed: {url}"), urllib.error.HTTPError(url, 500, "server error", {}, None)):
                with self.subTest(type(err).__name__):
                    out, errbuf = io.StringIO(), io.StringIO()
                    with patch.object(fl, "load_oc", return_value="SECRETKEY"), patch.object(fl, "fetch_remote", side_effect=err), redirect_stdout(out), redirect_stderr(errbuf):
                        code = fl.main(["--laws", str(ws.laws), "--store-dir", str(ws.store)])
                    self.assertEqual(code, 2)
                    self.assertNotIn("SECRETKEY", out.getvalue() + errbuf.getvalue())


if __name__ == "__main__":
    unittest.main()
