import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import news_topics as nt


def item(i, **kw):
    return {"title": f"기사 {i}", "url": f"https://x/{i}", "summary": "s", "source": "t", **kw}


class ParseTests(unittest.TestCase):
    def test_closed_list_enforced_and_max_two(self):
        out = nt.parse_answer('앞말 {"1":["security","hacking","swarm-multiagent","ros-middleware"],"2":[]} 뒷말', 2)
        self.assertEqual(out[1], ["security", "swarm-multiagent"])
        self.assertEqual(out[2], [])

    def test_out_of_range_and_bad_shapes_ignored(self):
        out = nt.parse_answer('{"0":["security"],"9":["security"],"x":["security"],"1":"security","2":["security","security"]}', 2)
        self.assertEqual(out, {2: ["security"]})  # 중복 제거, 범위 밖·잘못된 형태 무시

    def test_no_json_raises(self):
        with self.assertRaises(ValueError):
            nt.parse_answer("분류 불가", 3)

    def test_topics_match_web_menu_keys(self):
        ts = (Path.home() / "projectm/drone-wiki-web/lib/types.ts").read_text(encoding="utf-8")
        for key in nt.TOPICS:
            self.assertIn(f'"{key}"', ts, f"웹 DOMAIN_META 에 없는 주제: {key}")
        self.assertNotIn("knowledge-management", nt.TOPICS)  # PKM 은 뉴스 대상 아님


class ApplyTests(unittest.TestCase):
    def test_classifies_missing_only_and_is_idempotent(self):
        feed = [item(1), item(2, topics=["security"]), item(3)]
        calls = []

        def caller(prompt):
            calls.append(prompt)
            return '{"1":["ros-middleware"],"2":[]}'

        st = nt.apply_topics(feed, caller)
        self.assertEqual((st["todo"], st["classified"], st["empty"]), (2, 1, 1))
        self.assertEqual(feed[1]["topics"], ["security"])  # 이미 분류된 항목은 건드리지 않는다
        self.assertEqual(feed[0]["topics"], ["ros-middleware"])
        self.assertEqual(feed[2]["topics"], [])
        before = json.dumps(feed, sort_keys=True)
        nt.apply_topics(feed, lambda p: self.fail("두 번째 실행은 호출하지 않는다"))
        self.assertEqual(before, json.dumps(feed, sort_keys=True))

    def test_fail_open_counts_tries_then_gives_up(self):
        feed = [item(1)]

        def boom(prompt):
            raise RuntimeError("SECRET-TOKEN")  # 오류 내용은 어디에도 남지 않는다

        for n in range(1, nt.MAX_TRIES):
            st = nt.apply_topics(feed, boom)
            self.assertEqual(st["failed"], 1)
            self.assertNotIn("topics", feed[0])
            self.assertEqual(feed[0]["topics_tried"], n)
        nt.apply_topics(feed, boom)
        self.assertEqual(feed[0]["topics"], [])  # 상한 도달 → 빈 배열로 확정
        nt.apply_topics(feed, lambda p: self.fail("확정된 항목은 다시 호출하지 않는다"))

    def test_missing_number_stays_retryable(self):
        feed = [item(1), item(2)]
        nt.apply_topics(feed, lambda p: '{"1":["security"]}')
        self.assertEqual(feed[0]["topics"], ["security"])
        self.assertNotIn("topics", feed[1])
        self.assertEqual(feed[1]["topics_tried"], 1)

    def test_batches_and_per_run_limit(self):
        feed = [item(i) for i in range(45)]
        sizes = []

        def caller(prompt):
            n = prompt.count("\n") and sum(1 for ln in prompt.splitlines() if ln[:1].isdigit() and ". 기사" in ln)
            sizes.append(n)
            return json.dumps({str(i): [] for i in range(1, n + 1)})

        nt.apply_topics(feed, caller, limit=45)
        self.assertEqual(sizes, [20, 20, 5])
        feed2 = [item(i) for i in range(100)]
        st = nt.apply_topics(feed2, lambda p: json.dumps({str(i): [] for i in range(1, 21)}), limit=40)
        self.assertEqual(st["todo"], 40)

    def test_prompt_contains_all_topics_and_no_secrets_fields(self):
        p = nt.build_prompt([item(1, sha256="abcd")])
        for key in nt.TOPICS:
            self.assertIn(key, p)
        self.assertNotIn("abcd", p)


class AppendIntegrationTests(unittest.TestCase):
    def run_append(self, items, env_topics):
        home = tempfile.mkdtemp()
        (Path(home) / "2nd/.ua").mkdir(parents=True)
        env = {**os.environ, "HOME": home, "NEWS_TOPICS": env_topics}
        r = subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "news-feed-append.py")],
                           input=json.dumps(items), text=True, capture_output=True, env=env)
        feed = json.loads((Path(home) / "2nd/.ua/news-feed.json").read_text())
        return r, feed

    def test_disabled_switch_skips_classification(self):
        r, feed = self.run_append([item(1)], "0")
        self.assertEqual(r.returncode, 0)
        self.assertNotIn("topics", feed[0])

    def test_classifier_error_never_blocks_append(self):
        r, feed = self.run_append([item(1), item(2)], "1")  # 이 환경엔 라우터가 없어 분류가 실패한다
        self.assertEqual(r.returncode, 0)
        self.assertEqual(len(feed), 2)  # fail-open: 항목은 그대로 병합


if __name__ == "__main__":
    unittest.main()
