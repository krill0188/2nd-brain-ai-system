"""paper_fulltext_lib 시험(T2·T3 일부). 실행: ~/2nd/.venv/bin/python -W ignore scripts/test_paper_fulltext_lib.py
모델 호출 없음. PDF 추출 시험은 시험 중에 fitz로 작은 PDF를 직접 만들어 쓴다.
"""
import os, sys, tempfile, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paper_fulltext_lib as F
import paper_claims_lib as L


class Parse(unittest.TestCase):
    def test_plain_array(self):
        self.assertEqual(len(F.parse_candidates('[{"quote": "a"}, {"quote": "b"}]')), 2)

    def test_array_inside_prose_and_codefence(self):
        raw = '결과입니다:\n```json\n[{"subject": "x", "quote": "q"}]\n```\n끝.'
        self.assertEqual(F.parse_candidates(raw)[0]["subject"], "x")

    def test_empty_array(self):
        self.assertEqual(F.parse_candidates("[]"), [])

    def test_no_array_raises(self):
        for raw in ("", None, "죄송합니다. 찾지 못했습니다.", "{}"):
            with self.assertRaises(ValueError):
                F.parse_candidates(raw)

    def test_broken_json_raises(self):
        with self.assertRaises(ValueError):          # json.JSONDecodeError는 ValueError의 하위 클래스
            F.parse_candidates('[{"quote": "unterminated]')

    def test_truncated_array_salvages_complete_items(self):
        """실측 결함(2026-10-27): 모델 응답이 중간에 잘려 ']'가 없으면 전부 버리던 문제. 완결된 항목은 살린다."""
        raw = '```json\n[\n {"subject":"a","quote":"first quote here"},\n {"subject":"b","quote":"second {braces} in string"},\n {"subject":"c","quote":"cut off im'
        items, truncated = F.parse_candidates_ex(raw)
        self.assertEqual([x["subject"] for x in items], ["a", "b"])
        self.assertTrue(truncated)
        self.assertEqual(len(F.parse_candidates(raw)), 2)

    def test_truncated_with_no_complete_item_raises(self):
        with self.assertRaises(ValueError):
            F.parse_candidates('[{"subject":"a","quote":"cut off')

    def test_complete_array_not_flagged_truncated(self):
        items, truncated = F.parse_candidates_ex('[{"quote":"x"}]')
        self.assertEqual((len(items), truncated), (1, False))

    def test_non_dict_items_dropped(self):
        self.assertEqual(F.parse_candidates('[1, "x", {"quote": "ok"}]'), [{"quote": "ok"}])


class Sentences(unittest.TestCase):
    def test_keeps_number_with_unit_only(self):
        pages = ["The measured hover endurance reached 28 min with a 2.5 kg payload on the bench. "
                 "We then discuss the related work in the field of aerial robotics in detail here. "
                 "Section 3 describes the 12 experiments that were carried out in the lab."]
        s = F.numeric_sentences(pages)
        self.assertEqual(len(s), 1)
        self.assertIn("28 min", s[0][1])

    def test_page_numbers_are_one_based(self):
        pages = ["no numbers here at all in this long sentence about nothing in particular, really.",
                 "The peak thrust measured on the bench was 4.2 kg at full throttle in the test."]
        self.assertEqual(F.numeric_sentences(pages)[0][0], 2)

    def test_hyphen_linebreak_restored(self):
        pages = ["The maximum veloc-\nity of the airframe was measured at 17 m/s during the outdoor flight test."]
        self.assertIn("velocity", F.numeric_sentences(pages)[0][1])

    def test_length_bounds(self):
        self.assertEqual(F.numeric_sentences(["It is 5 m."]), [])                       # 너무 짧음
        self.assertEqual(F.numeric_sentences(["x" * 700 + " is 5 m long."]), [])        # 너무 김


class References(unittest.TestCase):
    def test_cut_at_references_heading(self):
        pages = ["intro"] * 6 + ["body 5 kg", "text\nReferences\n[1] A. Author, 2020."] + ["[2] ref 99 kg"]
        out = F.strip_references(pages)
        self.assertNotIn("[1] A. Author", "".join(out))
        self.assertNotIn("[2] ref", "".join(out))
        self.assertIn("body 5 kg", "".join(out))

    def test_no_heading_keeps_all(self):
        pages = ["a", "b", "c"]
        self.assertEqual(F.strip_references(pages), pages)

    def test_heading_in_front_half_is_ignored(self):
        pages = ["References\nrelated work discussion"] + ["x"] * 9
        self.assertEqual(len(F.strip_references(pages)), 10)


class Chunks(unittest.TestCase):
    def sents(self, n, size=100):
        return [(i // 10 + 1, ("s%03d " % i) + "x" * size) for i in range(n)]

    def test_max_chars_respected(self):
        for ch in F.make_chunks(self.sents(200), max_chars=1000, max_chunks=99):
            self.assertLessEqual(sum(len(s) for _, s in ch), 1000 + 110)  # 마지막 문장 1개 초과분 허용

    def test_max_chunks_even_selection(self):
        ch = F.make_chunks(self.sents(400), max_chars=1000, max_chunks=4)
        self.assertEqual(len(ch), 4)
        firsts = [c[0][1][:4] for c in ch]
        self.assertEqual(len(set(firsts)), 4)
        self.assertGreater(int(firsts[-1][1:]), int(firsts[0][1:]) + 100)             # 앞쪽에만 몰리지 않음

    def test_front_skipped(self):
        ch = F.make_chunks(self.sents(100), max_chars=10**6, max_chunks=4, skip_front=0.1)
        self.assertEqual(ch[0][0][1][:4], "s010")

    def test_empty(self):
        self.assertEqual(F.make_chunks([]), [])


class Locate(unittest.TestCase):
    CH = [(3, "Alpha result was 5 kg."), (4, "Beta   result  was 7  kg in flight.")]

    def test_finds_page_ignoring_whitespace(self):
        self.assertEqual(F.locate(self.CH, "beta result was 7 kg"), "p.4")

    def test_fallback_first_page(self):
        self.assertEqual(F.locate(self.CH, "not present anywhere"), "p.3")


class PromptContract(unittest.TestCase):
    def test_prompt_contains_chunk_and_json_instruction(self):
        p = F.chunk_prompt([(1, "Sentence A 5 kg."), (2, "Sentence B 7 m/s.")])
        self.assertIn("Sentence A 5 kg.", p)
        self.assertIn("JSON 배열", p)

    def test_end_to_end_with_judge(self):
        """후보 → locate → 코드 판정까지의 흐름(모델 없이 고정 응답으로)."""
        chunk = [(2, "The measured hover power was 42 W at 1.5 kg payload in the indoor test.")]
        raw = '[{"subject":"hover power","attribute":"power","value":"42","unit":"W","conditions":"1.5 kg payload, indoor","quote":"measured hover power was 42 W at 1.5 kg payload"}]'
        cands = F.parse_candidates(raw)
        for c in cands:
            c["locator"] = F.locate(chunk, c["quote"])
        good, bad = L.judge(cands, chunk[0][1])
        self.assertEqual((len(good), len(bad)), (1, 0))
        self.assertEqual(good[0]["locator"], "p.2")


class Canonical(unittest.TestCase):
    def test_soft_hyphen_break_joined(self):
        self.assertEqual(F.canonicalize("our pro-\nposed method, Com-\npared with"), "our proposed method, Compared with")

    def test_uppercase_continuation_and_real_dash_kept(self):
        self.assertEqual(F.canonicalize("RT-\nDETR and 5-\n10 m"), "RT-\nDETR and 5-\n10 m")

    def test_quote_matches_after_canonicalization(self):
        """실측 결함 재현: 줄 끝 분절이 있는 원문 + 청크에서 복원된 모델 인용문."""
        raw = "Con- trast: the pro-\nposed method achieves 1.9% improvement in AP over baseline."
        quote = "the proposed method achieves 1.9% improvement in AP"
        c = {"subject": "m", "attribute": "AP", "value": "1.9", "conditions": "baseline", "locator": "p.1", "quote": quote}
        self.assertEqual(len(L.judge([c], raw)[0]), 0)                       # 정본화 전: 거짓 탈락
        self.assertEqual(len(L.judge([c], F.canonicalize(raw))[0]), 1)       # 정본화 후: 통과

    def test_clean_candidate_unicode_hyphen(self):
        c = F.clean_candidate({"quote": "links U\u2011G and U\u2010E at\u00a010 dB", "value": "10"})
        self.assertEqual(c["quote"], "links U-G and U-E at 10 dB")
        self.assertEqual(c["value"], "10")                                    # 다른 필드는 그대로

    def test_clean_candidate_without_quote(self):
        self.assertEqual(F.clean_candidate({"value": "1"}), {"value": "1"})


class PdfExtract(unittest.TestCase):
    def test_extract_pages_roundtrip(self):
        import fitz
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "t.pdf")
            doc = fitz.open()
            for txt in ("The measured endurance was 31 min on page one.", "Second page reports 4.5 kg of thrust."):
                doc.new_page().insert_text((72, 72), txt)
            doc.save(p); doc.close()
            pages = F.extract_pages(p)
            self.assertEqual(len(pages), 2)
            self.assertIn("31 min", pages[0])
            self.assertIn("4.5 kg", pages[1])


if __name__ == "__main__":
    unittest.main(verbosity=1)
