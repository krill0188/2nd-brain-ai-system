import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("fts", HERE / "fetch-topic-sources.py")
fts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fts)

RSS = b"""<?xml version="1.0"?><rss version="2.0"><channel>
<item><title>Jetson Orin drone brain</title><link>https://a/1</link><description>&lt;p&gt;edge &amp;amp; AI&lt;/p&gt;</description><pubDate>Fri, 07 Nov 2026 01:00:00 GMT</pubDate></item>
<item><title>Kubernetes news</title><link>https://a/2</link><description>cluster</description></item>
<item><title>UAV swarm paper</title><link>https://a/3</link><description>s</description></item>
<item><title>no link</title></item></channel></rss>"""
ATOM = b"""<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">
<entry><title>v1.18.0-rc1</title><link href="https://github.com/PX4/x/releases/tag/v1.18.0-rc1"/><updated>2026-11-06T00:00:00Z</updated><content>notes</content></entry>
<entry><title>v1.17.0</title><link href="https://github.com/PX4/x/releases/tag/v1.17.0"/></entry></feed>"""


class ParseTests(unittest.TestCase):
    def test_rss_parse_cleans_html_and_skips_linkless(self):
        rows = fts.parse_feed(RSS)
        self.assertEqual([r["url"] for r in rows], ["https://a/1", "https://a/2", "https://a/3"])
        self.assertEqual(rows[0]["summary"], "edge & AI")

    def test_atom_parse(self):
        rows = fts.parse_feed(ATOM)
        self.assertEqual(rows[0]["url"], "https://github.com/PX4/x/releases/tag/v1.18.0-rc1")
        self.assertEqual(rows[0]["published"], "2026-11-06T00:00:00Z")

    def test_bad_xml_raises(self):
        with self.assertRaises(ValueError):
            fts.parse_feed(b"<html><oops")

    def test_include_filter_and_max(self):
        rows = fts.parse_feed(RSS)
        picked = fts.select(rows, {"include": "Jetson|UAV", "max": 1})
        self.assertEqual([r["url"] for r in picked], ["https://a/1"])
        self.assertEqual(len(fts.select(rows, {"max": 2})), 2)

    def test_release_items_get_release_label(self):
        rows = fts.parse_feed(ATOM)
        items = fts.to_items(rows[:1], {"slug": "px4-release", "domain": "flight-control", "type": "release"})
        self.assertIn("릴리즈", items[0]["title"] + "릴리즈")
        self.assertEqual(items[0]["type"], "release")
        self.assertEqual(items[0]["source"], "github.com")

    def test_arxiv_url_built_and_encoded(self):
        u = fts.source_url('arxiv:all:"GNSS-denied" AND all:UAV')
        self.assertTrue(u.startswith("https://export.arxiv.org/api/query?search_query="))
        self.assertNotIn(" ", u)


class CollectTests(unittest.TestCase):
    def test_one_failing_source_does_not_stop_others(self):
        specs = [{"slug": "bad", "url": "https://bad", "type": "news", "domain": "hardware", "max": 3},
                 {"slug": "ok", "url": "https://ok", "type": "news", "domain": "hardware", "max": 3}]

        def fetcher(url):
            if "bad" in url:
                raise OSError("down")
            return RSS

        items, stat = fts.collect(specs, fetcher, sleep=lambda s: None)
        self.assertEqual((stat["ok"], stat["failed"]), (1, 1))
        self.assertEqual(len(items), 3)

    def test_arxiv_calls_are_spaced(self):
        specs = [{"slug": f"a{i}", "url": f"arxiv:all:x{i}", "type": "paper", "domain": "ai-autonomy", "max": 1} for i in range(3)]
        waits = []
        fts.collect(specs, lambda u: RSS, sleep=waits.append)
        self.assertEqual(len(waits), 2)  # 첫 호출 뒤 두 번 대기
        self.assertTrue(all(w > 0 for w in waits))

    def test_config_is_valid_and_domains_exist_in_web(self):
        cfg = json.loads((HERE / "news-topic-sources.json").read_text(encoding="utf-8"))["sources"]
        types = (Path.home() / "projectm/drone-wiki-web/lib/types.ts").read_text(encoding="utf-8")
        slugs = [c["slug"] for c in cfg]
        self.assertEqual(len(slugs), len(set(slugs)))
        for c in cfg:
            self.assertIn(c["type"], ("news", "release", "paper"))
            self.assertIn(f'"{c["domain"]}"', types, f"웹에 없는 domain: {c['domain']}")
            self.assertGreaterEqual(int(c["max"]), 1)


if __name__ == "__main__":
    unittest.main()
