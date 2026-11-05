"""fetch-law-kskill.py 시험(네트워크 없음). 실행: python3 -I test_fetch_law_kskill.py
2026-11-06 정비 전 결함(빈 본문 저장·MST를 ID로 사용·응답 키 불일치·유니코드 이스케이프 제목·무관 법령·매일 중복·SSL 검증 해제)을 고정한다."""
import importlib.util, json, os, re, tempfile, unittest
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("kl", os.path.join(HERE, "fetch-law-kskill.py"))
kl = importlib.util.module_from_spec(spec); spec.loader.exec_module(kl)

ORD = {"LawService": {"자치법규기본정보": {"자치법규명": "가평군 드론산업 육성 및 지원 조례", "시행일자": "20201223"},
       "조문": {"조": [{"조제목": "목적", "조내용": "제1조(목적) 이 조례는 가평군 드론산업의 육성 및 지원에 필요한 사항을 규정함으로써 관련 산업 발전에 이바지함을 목적으로 한다."}, {"조내용": "제2조(정의) 이 조례에서 사용하는 용어의 뜻은 다음과 같다."}]},
       "부칙": {"부칙내용": "부칙 <제정 2020.12.23.> 이 조례는 공포한 날부터 시행한다."}}}
EXP = {"ExpcService": {"안건명": "드론 비행승인 관련", "해석일자": "20240101", "질의요지": "드론 비행승인 대상은 무엇인지 문의합니다 그리고 범위는 어디까지인지도 문의합니다.", "회답": "해당 조문에 따라 대상이 정해집니다.", "이유": ""}}


class Parse(unittest.TestCase):
    def test_relevance_title_filter(self):
        for t in ["가평군 드론산업 육성 및 지원 조례", "초경량비행장치 비행승인 업무처리 기준", "119항공대 운영 규정", "무인비행장치 특별비행승인 지침"]: self.assertTrue(kl.relevant(t), t)
        for t in ["2015년 하이브리드자동차 구매보조금 대상차종", "항공보안법 시행규칙", "항공운송사업 면허 기준", "감사원 - 외국회사 소유의 지방세", ""]: self.assertFalse(kl.relevant(t), t)

    def test_extract_ordin_uses_real_response_keys(self):
        body, eff = kl.extract("ordin", ORD)
        self.assertIn("제1조(목적)", body); self.assertIn("제2조(정의)", body); self.assertIn("공포한 날부터 시행", body); self.assertEqual(eff, "20201223")

    def test_extract_expc_and_admrul_and_unknown(self):
        body, eff = kl.extract("expc", EXP); self.assertIn("### 질의요지", body); self.assertIn("### 회답", body); self.assertNotIn("### 이유", body); self.assertEqual(eff, "20240101")
        b2, e2 = kl.extract("admrul", {"AdmRulService": {"행정규칙기본정보": {"시행일자": "20260920"}, "조문내용": ["제1조(목적) 이 규정은 항공대 운영에 필요한 사항을 정한다.", ["제2조 정의"]]}})
        self.assertIn("제2조 정의", b2); self.assertEqual(e2, "20260920")
        self.assertEqual(kl.extract("ordin", {"Law": "일치하는 법령이 없습니다."}), ("", ""))  # 옛 구현이 빈 본문으로 저장하던 응답
        self.assertEqual(kl.extract("law", ORD), ("", ""))

    def test_front_matter_has_readable_korean_and_no_secrets(self):
        doc = kl.build_doc("ordin", '가평군 "드론" 조례', "2203991", "본문 " * 20, "20201223", "2026-11-06")
        self.assertIn('title: "가평군 \\"드론\\" 조례"', doc); self.assertNotIn("\\ud", doc); self.assertIn("verified: false", doc); self.assertIn("effective: 2020-12-23", doc)
        self.assertNotIn("OC=", doc); self.assertNotIn("법령상세링크", doc); self.assertIn("미검증 사본", doc)
        self.assertTrue(doc.startswith("---\n") and "\n---\n" in doc)
        fm = doc.split("---")[1]; self.assertEqual(len(re.findall(r"^title:", fm, re.M)), 1)

    def test_long_body_is_cut_and_says_so(self):
        doc = kl.build_doc("admrul", "항공대 규정", "1", "가" * (kl.MAX_BODY + 500), "", "2026-11-06")
        self.assertIn("이하 생략", doc); self.assertLess(len(doc), kl.MAX_BODY + 1200)

    def test_no_ssl_verification_bypass_in_source(self):
        src = open(os.path.join(HERE, "fetch-law-kskill.py"), encoding="utf-8").read()
        self.assertNotIn("CERT_NONE", src); self.assertNotIn("check_hostname = False", src)


class Run(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.inbox = Path(self.tmp.name) / "inbox"; self.proc = self.inbox / "processed"; self.calls = []

    def tearDown(self): self.tmp.cleanup()

    def fake(self, items_by_target, details):
        def search(t, q): self.calls.append(("s", t, q)); return items_by_target.get(t, [])
        def detail(t, i): self.calls.append(("d", t, i)); return details[(t, i)]
        return search, detail

    def go(self, search, detail, targets=("ordin",), **kw):
        return kl.run(targets, self.inbox, self.proc, "2026-11-06", kw.pop("max_items", 5), search=search, detail=detail, sleep=lambda s: None, **kw)

    def test_writes_relevant_with_id_not_mst_and_skips_irrelevant(self):
        items = [{"자치법규ID": "2203991", "자치법규일련번호": "1556259", "자치법규명": "가평군 드론산업 육성 및 지원 조례"}, {"자치법규ID": "9", "자치법규명": "하이브리드 구매보조금 조례"}]
        s, d = self.fake({"ordin": items}, {("ordin", "2203991"): ORD})
        st = self.go(s, d)
        self.assertEqual(st["written"], 1); self.assertIn(("d", "ordin", "2203991"), self.calls); self.assertNotIn(("d", "ordin", "1556259"), self.calls)  # 상세 ID 는 법령 ID 계열
        self.assertEqual([c for c in self.calls if c[0] == "d"], [("d", "ordin", "2203991")])  # 무관 항목은 상세 조회조차 안 함
        f = list(self.inbox.glob("fetch-2026-11-06-law-ordin-2203991-20201223.md")); self.assertEqual(len(f), 1)

    def test_empty_body_is_not_saved(self):
        s, d = self.fake({"ordin": [{"자치법규ID": "1", "자치법규명": "드론 조례"}]}, {("ordin", "1"): {"Law": "일치하는 법령이 없습니다."}})
        st = self.go(s, d); self.assertEqual((st["written"], st["skipped_empty"]), (0, 1)); self.assertFalse(self.inbox.exists() and any(self.inbox.glob("*.md")))

    def test_no_daily_duplicates_and_processed_counts(self):
        s, d = self.fake({"ordin": [{"자치법규ID": "2203991", "자치법규명": "가평군 드론산업 육성 및 지원 조례"}]}, {("ordin", "2203991"): ORD})
        self.assertEqual(self.go(s, d)["written"], 1)
        st2 = kl.run(("ordin",), self.inbox, self.proc, "2026-11-07", 5, search=s, detail=d, sleep=lambda x: None)  # 다음 날
        self.assertEqual((st2["written"], st2["skipped_seen"]), (0, 1))
        (self.proc).mkdir(parents=True, exist_ok=True); next(self.inbox.glob("fetch-*.md")).rename(self.proc / "fetch-2026-11-06-law-ordin-2203991-20201223.md")
        self.assertEqual(kl.run(("ordin",), self.inbox, self.proc, "2026-11-08", 5, search=s, detail=d, sleep=lambda x: None)["skipped_seen"], 1)  # 정리(processed)된 것도 재수집 안 함

    def test_dry_run_writes_nothing_and_max_items(self):
        items = [{"자치법규ID": str(i), "자치법규명": f"드론 조례 {i}"} for i in range(1, 6)]
        s, d = self.fake({"ordin": items}, {("ordin", str(i)): ORD for i in range(1, 6)})
        st = self.go(s, d, dry_run=True, max_items=2); self.assertEqual(st["written"], 2); self.assertFalse(self.inbox.exists())

    def test_errors_counted_and_exit_code_only_when_all_fail(self):
        def boom(t, q): raise OSError("http://x?OC=SECRET")
        st = kl.run(("ordin",), self.inbox, self.proc, "2026-11-06", 5, search=boom, detail=None, sleep=lambda x: None)
        self.assertEqual((st["errors"], st["calls"]), (len(kl.QUERIES), len(kl.QUERIES)))
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf): kl.run(("ordin",), self.inbox, self.proc, "2026-11-06", 5, search=boom, detail=None, sleep=lambda x: None)
        self.assertNotIn("SECRET", buf.getvalue())  # 오류 메시지의 URL·키는 출력하지 않는다

    def test_single_result_dict_is_handled(self):
        orig = kl._get
        try:
            kl._get = lambda url, timeout=30: {"OrdinSearch": {"law": {"자치법규ID": "5", "자치법규명": "드론 조례"}}}
            self.assertEqual(len(kl.kskill_search("ordin", "드론")), 1)  # 1건이면 목록이 아니라 딕셔너리
            kl._get = lambda url, timeout=30: {"OrdinSearch": {}}
            self.assertEqual(kl.kskill_search("ordin", "드론"), [])
        finally: kl._get = orig


if __name__ == "__main__": unittest.main()
