"""paper_claims_lib 시험. 실행: ~/2nd/.venv/bin/python -W ignore scripts/test_paper_claims_lib.py
T1(회귀): 기존 수동 파이프라인이 남긴 후보 claim 파일을 이전한 판정으로 다시 판정해 저장된 통과/탈락 결과와 100% 일치해야 한다.
T3(단위): 판정 규칙의 경계(길이 14/15/400/401, 필수 필드, 숫자 불일치, 합자·대시 정규화).
"""
import glob, json, os, sys, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paper_claims_lib as L

PAPERS = os.path.expanduser("~/projectm/hw-collection/20261019/papers-ontology")
BASE = {"subject": "S", "attribute": "A", "value": "42", "unit": "", "conditions": "C", "locator": "II-A"}


def cand(quote, **kw):
    return {**BASE, "quote": quote, **kw}


class Boundaries(unittest.TestCase):
    TEXT = "The measured hover power was 42 W at 1.5 kg payload in the indoor test. " + "x" * 600

    def test_pass(self):
        q = "measured hover power was 42 W at 1.5 kg"
        self.assertIsNone(L.check(cand(q), L.norm(self.TEXT)))

    def test_length_bounds(self):
        nt = L.norm("a" * 500 + " 42 ")
        for n, ok in ((14, False), (15, True), (400, True), (401, False)):
            q = "a" * (n - 3) + " 42"           # 길이 n, 숫자 42를 인용문 안에 포함
            self.assertEqual(len(q), n)
            r = L.check(cand(q), nt)
            self.assertEqual(r is None, ok, f"len={n}: {r}")

    def test_required_fields(self):
        nt = L.norm(self.TEXT)
        q = "measured hover power was 42 W at 1.5 kg"
        for k in ("subject", "attribute", "conditions", "locator", "value"):
            self.assertIn("비어 있음", L.check(cand(q, **{k: "  "}), nt) or "")

    def test_quote_missing(self):
        self.assertEqual(L.check(cand("this sentence is not in the paper at all"), L.norm(self.TEXT)), "quote가 원문에 없음")

    def test_number_not_in_quote(self):
        q = "measured hover power was 42 W at 1.5 kg"
        r = L.check(cand(q, value="99"), L.norm(self.TEXT))
        self.assertTrue(r and "숫자" in r, r)

    def test_ligature_dash_normalization(self):
        text = "The ﬁnal efﬁciency reached 85 % — a new best for the 2–4 kg class."
        q = "The final efficiency reached 85 % - a new best for the 2-4 kg class."
        self.assertIsNone(L.check(cand(q, value="85"), L.norm(text)))

    def test_judge_preserves_order_and_reasons(self):
        good, bad = L.judge([cand("measured hover power was 42 W at 1.5 kg"), cand("nope nope nope nope nope"), cand("measured hover power was 42 W at 1.5 kg", value="7")], self.TEXT)
        self.assertEqual(len(good), 1)
        self.assertEqual([b["_why"] for b in bad][0], "quote가 원문에 없음")
        self.assertEqual(len(bad), 2)

    def test_evidence_kind(self):
        self.assertEqual(L.evidence_kind({"quote": "values reported by Li et al. were used", "conditions": "", "attribute": ""}), "cited-secondary")
        self.assertEqual(L.evidence_kind({"quote": "we assume a drag coefficient", "conditions": "", "attribute": ""}), "model-assumption")
        self.assertEqual(L.evidence_kind({"quote": "Gazebo results", "conditions": "", "attribute": ""}), "simulation")
        self.assertEqual(L.evidence_kind({"quote": "measured thrust", "conditions": "bench", "attribute": "thrust"}), "reported")


@unittest.skipUnless(os.path.isdir(os.path.join(PAPERS, "claims")), "기존 수동 파이프라인 폴더 없음")
class Regression(unittest.TestCase):
    def test_rejudge_all_existing_candidate_files(self):
        cl, txt = os.path.join(PAPERS, "claims"), os.path.join(PAPERS, "txt")
        checked = claims = 0
        diffs = []
        for f in sorted(glob.glob(os.path.join(cl, "*.json"))):
            b = os.path.basename(f)
            if b.endswith(".verified.json") or b.endswith(".rejected.json"):
                continue
            aid = b[:-5]
            tp = os.path.join(txt, aid + ".txt")
            vp, rp = os.path.join(cl, aid + ".verified.json"), os.path.join(cl, aid + ".rejected.json")
            if not (os.path.exists(tp) and os.path.exists(vp) and os.path.exists(rp)):
                continue
            good, bad = L.judge(json.load(open(f)), open(tp).read())
            if good != json.load(open(vp)) or bad != json.load(open(rp)):
                diffs.append(aid)
            checked += 1
            claims += len(good) + len(bad)
        self.assertGreater(checked, 100, f"재판정한 논문 {checked}편 — 기대보다 적음")
        self.assertEqual(diffs, [], f"기존 결과와 다른 논문 {len(diffs)}/{checked}편: {diffs[:5]}")
        print(f"\n  T1 회귀: {checked}편 / 후보 {claims}건 재판정, 기존 결과와 불일치 0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
