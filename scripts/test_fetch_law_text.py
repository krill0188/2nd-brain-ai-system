"""fetch-law-text.py 시험(네트워크 없음). 실행: python3 -I test_fetch_law_text.py"""
import importlib.util, json, os, tempfile, unittest

spec = importlib.util.spec_from_file_location("flt", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fetch-law-text.py"))
flt = importlib.util.module_from_spec(spec); spec.loader.exec_module(flt)

LAW = {"id": "law:t", "name": "시험법"}
GOOD = {"법령": {"기본정보": {"법령명_한글": "시험법"}, "조문": {"조문단위": [{"조문번호": "1"}]}}}


def put_record(rec_dir, mst, day="2026-11-01"):
    d = os.path.join(rec_dir, "law_t"); os.makedirs(d, exist_ok=True)
    json.dump({"법령일련번호": mst}, open(os.path.join(d, f"{day}-abc.json"), "w", encoding="utf-8"))


class T(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.rec = os.path.join(self.tmp.name, "rec"); self.st = os.path.join(self.tmp.name, "st")
        self.calls = []

    def tearDown(self): self.tmp.cleanup()

    def fetch(self, payload):
        def f(oc, mst): self.calls.append(mst); return payload
        return f

    def test_latest_mst_uses_newest_file(self):
        put_record(self.rec, "100", "2026-10-30"); put_record(self.rec, "200", "2026-11-01")
        self.assertEqual(flt.latest_mst(self.rec, "law:t"), "200")

    def test_skip_when_no_record(self):
        r = flt.run([LAW], self.st, self.rec, "k", self.fetch(GOOD))
        self.assertEqual(r["skipped"], ["시험법"]); self.assertEqual(self.calls, [])

    def test_new_then_unchanged_without_second_call(self):
        put_record(self.rec, "200")
        r1 = flt.run([LAW], self.st, self.rec, "k", self.fetch(GOOD))
        r2 = flt.run([LAW], self.st, self.rec, "k", self.fetch(GOOD))
        self.assertEqual((r1["new"], r2["unchanged"], self.calls), (["시험법"], ["시험법"], ["200"]))
        files = os.listdir(os.path.join(self.st, "law_t")); self.assertEqual(len(files), 1)
        self.assertRegex(files[0], r"^200-[0-9a-f]{12}\.json$")

    def test_validation_rejects_wrong_name_and_empty(self):
        put_record(self.rec, "200")
        bad = {"법령": {"기본정보": {"법령명_한글": "다른법"}, "조문": {"조문단위": [{"x": 1}]}}}
        r = flt.run([LAW], self.st, self.rec, "k", self.fetch(bad))
        self.assertEqual(r["failed"][0][0], "시험법"); self.assertIn("불일치", r["failed"][0][1]); self.assertFalse(os.path.exists(self.st))
        self.assertIn("조문 없음", flt.validate({"법령": {"기본정보": {"법령명_한글": "시험법"}, "조문": {}}}, "시험법"))

    def test_fetch_error_recorded_without_message(self):
        put_record(self.rec, "200")
        def boom(oc, mst): raise OSError("http://x?OC=SECRET")
        r = flt.run([LAW], self.st, self.rec, "k", boom)
        self.assertEqual(r["failed"], [("시험법", "OSError")])

    def test_dry_run_makes_no_call_or_file(self):
        put_record(self.rec, "200")
        r = flt.run([LAW], self.st, self.rec, "", self.fetch(GOOD), dry_run=True)
        self.assertEqual((r["new"], self.calls, os.path.exists(self.st)), (["시험법"], [], False))

if __name__ == "__main__": unittest.main()
