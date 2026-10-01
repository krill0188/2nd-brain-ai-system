#!/usr/bin/env python3
"""Best-effort YouTube transcript fetch via yt-dlp.

stdout: transcript text (<= MAX_CHARS) or nothing.
exit:   0 = fetched or no captions exist, 3 = rate-limited/blocked (caller should back off),
        4 = yt-dlp unavailable.
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

MAX_CHARS = 8000
TIMEOUT = 60
LANG_ORDER = ("en-orig", "en", "ko-orig", "ko")
BLOCK_MARKERS = ("429", "too many requests", "sign in to confirm", "not a bot")
FALLBACK_BINARIES = ("/usr/local/bin/yt-dlp", "/opt/homebrew/bin/yt-dlp",
                     os.path.expanduser("~/.local/bin/yt-dlp"))


def find_ytdlp() -> str | None:
    found = shutil.which("yt-dlp")
    if found:
        return found
    return next((p for p in FALLBACK_BINARIES if os.access(p, os.X_OK)), None)


def vtt_to_text(raw: str) -> str:
    out, last = [], ""
    for line in raw.splitlines():
        if not line.strip() or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")) or "-->" in line:
            continue
        line = re.sub(r"<[^>]+>", "", line).strip()
        if line and line != last:
            out.append(line)
            last = line
    return re.sub(r"\s+", " ", " ".join(out)).strip()


def pick_text(directory: str) -> str:
    for lang in LANG_ORDER:
        for path in glob.glob(os.path.join(directory, f"*.{lang}.vtt")):
            with open(path, encoding="utf-8", errors="ignore") as handle:
                text = vtt_to_text(handle.read())
            if len(text) > 200:
                return text[:MAX_CHARS]
    return ""


def fetch(video_id: str, run=subprocess.run) -> tuple[str, str]:
    """Return (text, status); status in ok | empty | rate_limited | unavailable."""
    binary = find_ytdlp()
    if not binary:
        return "", "unavailable"
    with tempfile.TemporaryDirectory() as tmp:
        try:
            proc = run(
                [binary, "--skip-download", "--write-auto-subs", "--write-subs",
                 "--sub-langs", ",".join(LANG_ORDER), "--sub-format", "vtt",
                 "--no-warnings", "-q", "-o", os.path.join(tmp, "%(id)s.%(ext)s"),
                 f"https://www.youtube.com/watch?v={video_id}"],
                capture_output=True, text=True, timeout=TIMEOUT,
            )
            stderr = (getattr(proc, "stderr", "") or "").lower()
        except subprocess.TimeoutExpired:
            return "", "empty"
        except OSError:
            return "", "unavailable"
        text = pick_text(tmp)
        if text:
            return text, "ok"
        blocked = any(marker in stderr for marker in BLOCK_MARKERS)
        return "", "rate_limited" if blocked else "empty"


if __name__ == "__main__":
    if len(sys.argv) != 2 or not re.fullmatch(r"[\w-]{6,20}", sys.argv[1]):
        raise SystemExit(2)
    text, status = fetch(sys.argv[1])
    sys.stdout.write(text)
    raise SystemExit({"rate_limited": 3, "unavailable": 4}.get(status, 0))
