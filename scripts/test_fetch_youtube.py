"""Regression checks for fetch-inbox.sh embedded Python blocks and YouTube transcript collection."""

import ast
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parent
FETCH = SCRIPTS / "fetch-inbox.sh"
sys.path.insert(0, str(SCRIPTS))

import yt_transcript  # noqa: E402

WATCHED_MODULES = {"subprocess", "json", "os", "re", "sys", "time", "urllib", "datetime"}


def embedded_blocks() -> list[tuple[int, str]]:
    text = FETCH.read_text(encoding="utf-8")
    blocks = []
    for match in re.finditer(r"<<'PYEOF'\n(.*?)\nPYEOF", text, re.S):
        blocks.append((text.count("\n", 0, match.start()) + 1, match.group(1)))
    return blocks


def imported_names(tree: ast.AST) -> set[str]:
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(a.asname or a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return names


def used_modules(tree: ast.AST) -> set[str]:
    return {n.value.id for n in ast.walk(tree)
            if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name)
            and n.value.id in WATCHED_MODULES}


class EmbeddedPythonTests(unittest.TestCase):

    def test_shell_syntax(self):
        self.assertEqual(subprocess.run(["bash", "-n", str(FETCH)]).returncode, 0)

    def test_every_embedded_block_compiles_and_imports_what_it_uses(self):
        blocks = embedded_blocks()
        self.assertGreaterEqual(len(blocks), 9)
        for line, source in blocks:
            tree = ast.parse(source, filename=f"fetch-inbox.sh:{line}")
            missing = used_modules(tree) - imported_names(tree)
            self.assertFalse(missing, f"block at line {line} uses unimported modules: {sorted(missing)}")


class TranscriptHelperTests(unittest.TestCase):

    def test_vtt_to_text_strips_markup_and_repeats(self):
        raw = ("WEBVTT\nKind: captions\n\n00:00:00.000 --> 00:00:02.000\nHello <c>world</c>\n\n"
               "00:00:02.000 --> 00:00:04.000\nHello world\nsecond line\n")
        self.assertEqual(yt_transcript.vtt_to_text(raw), "Hello world second line")

    def _fetch(self, writes_vtt: bool, stderr: str = ""):
        def run(command, **kwargs):
            if writes_vtt:
                out = Path(command[command.index("-o") + 1]).parent
                (out / "abc123.en.vtt").write_text(
                    "WEBVTT\n\n00:00:00.000 --> 00:00:02.000\n" + ("word " * 80), encoding="utf-8")
            return SimpleNamespace(returncode=0, stderr=stderr, stdout="")

        with patch.object(yt_transcript, "find_ytdlp", return_value="/bin/true"):
            return yt_transcript.fetch("abc123xyz", run=run)

    def test_status_ok_empty_rate_limited_unavailable(self):
        text, status = self._fetch(True, "ERROR: Unable to download subtitles for 'ko': HTTP Error 429")
        self.assertEqual(status, "ok")
        self.assertGreater(len(text), 200)
        self.assertEqual(self._fetch(False), ("", "empty"))
        self.assertEqual(self._fetch(False, "HTTP Error 429: Too Many Requests"), ("", "rate_limited"))
        with patch.object(yt_transcript, "find_ytdlp", return_value=None):
            self.assertEqual(yt_transcript.fetch("abc123xyz"), ("", "unavailable"))

    def test_text_is_capped(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "v.en.vtt").write_text(
                "WEBVTT\n\n00:00:00.000 --> 00:00:01.000\n" + " ".join(f"w{i}" for i in range(5000)),
                encoding="utf-8")
            self.assertEqual(len(yt_transcript.pick_text(tmp)), yt_transcript.MAX_CHARS)


class YouTubeBlockTests(unittest.TestCase):
    """Run the real YouTube block in a fake HOME with stubbed API and transcript helper."""

    def block_source(self) -> str:
        text = FETCH.read_text(encoding="utf-8")
        start = text.index("python3 - \"$YT_KEY\"")
        start = text.index("\n", start) + 1
        source = text[start:text.index("\nPYEOF", start)]
        fake_get = (
            "def get(url):\n"
            "    from datetime import date\n"
            "    if 'channels' in url:\n"
            "        h = url.split('forHandle=')[1].split('&')[0]\n"
            "        return {'items': [{'snippet': {'title': h}, 'contentDetails': {'relatedPlaylists': {'uploads': h}}}]}\n"
            "    h = url.split('playlistId=')[1].split('&')[0]\n"
            "    return {'items': [{'snippet': {'title': f'{h} video {i}', 'description': 'd',\n"
            "            'publishedAt': date.today().isoformat() + 'T00:00:00Z',\n"
            "            'resourceId': {'videoId': f'{h}{today[5:].replace(\"-\", \"\")}v{i}'}}} for i in range(3)]}\n")
        patched, count = re.subn(
            r"def get\(url\):\n    with urllib\.request\.urlopen\(url, timeout=15\) as r:\n        return json\.load\(r\)\n",
            lambda _m: fake_get, source)
        self.assertEqual(count, 1, "YouTube block API helper changed shape; update this test")
        return patched.replace("time.sleep(1.5)", "pass")

    def _setup_home(self, helper_body: str) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        home = Path(tmp.name)
        (home / "2nd/scripts").mkdir(parents=True)
        (home / "2nd/.ua").mkdir()
        (home / "claudeclaw/scripts").mkdir(parents=True)
        (home / "2nd/scripts/yt_transcript.py").write_text(helper_body, encoding="utf-8")
        (home / "claudeclaw/scripts/notify.sh").write_text(
            f'#!/bin/bash\necho "$1" >> "{home}/alerts.txt"\n', encoding="utf-8")
        conf, inbox = home / "channels.txt", home / "inbox"
        inbox.mkdir()
        conf.write_text("@ChanA|hardware|global\n@ChanB|flight-control|global\n@ChanC|ops-mission|global\n")
        (home / "seen.txt").write_text("")
        (home / "block.py").write_text(self.block_source(), encoding="utf-8")
        return home

    def _run(self, home: Path, date: str):
        done = subprocess.run(
            [sys.executable, str(home / "block.py"), "KEY", str(home / "channels.txt"), str(home / "inbox"),
             date, str(home / "seen.txt")],
            env={**os.environ, "HOME": str(home)}, capture_output=True, text=True, timeout=60)
        self.assertEqual(done.returncode, 0, done.stderr)
        return done

    def run_block(self, helper_body: str):
        home = self._setup_home(helper_body)
        done = self._run(home, "2026-10-02")
        stats = json.loads((home / "2nd/.ua/youtube-transcript-stats.json").read_text())
        alerts = (home / "alerts.txt").read_text() if (home / "alerts.txt").exists() else ""
        return sorted((home / "inbox").glob("*.md")), stats, alerts, done.stdout

    def test_transcript_success_marks_file_and_keeps_description(self):
        files, stats, alerts, out = self.run_block(
            "import sys\nsys.stdout.write('real transcript text ' * 20)\n")
        self.assertEqual(len(files), 6)
        body = files[0].read_text(encoding="utf-8")
        self.assertIn("transcript: true", body)
        self.assertIn("## 자막", body)
        self.assertIn("## 설명 요약", body)
        self.assertEqual((stats["attempted"], stats["ok"]), (6, 6))
        self.assertEqual(alerts, "")
        self.assertIn("6/6", out)

    def test_history_file_appends_one_row_per_run_without_clobbering(self):
        home = self._setup_home("import sys\nsys.stdout.write('real transcript text ' * 20)\n")
        self._run(home, "2026-10-02")
        self._run(home, "2026-10-03")
        history_path = home / "2nd/.ua/youtube-transcript-stats-history.jsonl"
        rows = [json.loads(line) for line in history_path.read_text().splitlines()]
        self.assertEqual([r["date"] for r in rows], ["2026-10-02", "2026-10-03"])
        for row in rows:
            self.assertEqual((row["attempted"], row["ok"]), (6, 6))
        snapshot = json.loads((home / "2nd/.ua/youtube-transcript-stats.json").read_text())
        self.assertEqual(snapshot["date"], "2026-10-03")

    def test_rate_limit_trips_breaker_after_two_but_collection_continues(self):
        files, stats, alerts, _ = self.run_block("import sys\nsys.exit(3)\n")
        self.assertEqual(len(files), 6)
        self.assertIn("transcript: false", files[0].read_text(encoding="utf-8"))
        self.assertEqual(stats["attempted"], 2)
        self.assertEqual(stats["rate_limited"], 2)
        self.assertEqual(alerts, "")

    def test_zero_transcripts_over_four_attempts_alerts_once(self):
        files, stats, alerts, _ = self.run_block("import sys\nsys.exit(0)\n")
        self.assertEqual(len(files), 6)
        self.assertEqual((stats["attempted"], stats["ok"]), (6, 0))
        self.assertEqual(len(alerts.strip().splitlines()), 1)
        self.assertIn("자막 0/6", alerts)

    def test_missing_ytdlp_stops_attempts_without_failing_fetch(self):
        files, stats, alerts, _ = self.run_block("import sys\nsys.exit(4)\n")
        self.assertEqual(len(files), 6)
        self.assertEqual((stats["attempted"], stats["unavailable"]), (1, 1))


if __name__ == "__main__":
    unittest.main()
