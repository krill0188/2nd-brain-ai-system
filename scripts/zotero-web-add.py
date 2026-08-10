#!/usr/bin/env python3
"""
zotero-web-add.py — 논문 메타데이터(주로 arXiv)를 Zotero Web API로 라이브러리에
직접 추가하고 PDF까지 첨부 업로드한다. "브라우저 Connector로 스크랩"을 API
호출로 대체 — fetch-inbox.sh가 이미 확보한 arXiv 메타데이터를 그대로 밀어넣는다.

목적: fetch-inbox.sh의 arXiv 수집은 즉시 inbox/에 컴파일용 레코드를 쓰지만
원문(PDF)은 보존하지 않는다. 여기서 같은 논문을 Zotero에도 넣어두면, 다음
동기화 후 scripts/zotero-ingest.py가 raw/papers/files/에 PDF까지 보존한다.

중복 컴파일 방지: 여기서 만드는 아이템엔 태그 "auto:2nd-brain"을 붙인다.
fetch-inbox.sh가 같은 논문을 inbox/에 이미 직접 써놓았으므로, zotero-ingest.py는
이 태그가 붙은 아이템을 볼 때 inbox/ 사본을 또 만들지 않는다(raw/papers/만
채운다) — 안 그러면 daily-ingest가 같은 논문을 두 번 컴파일하려 든다.

사용:
  echo '{"title": "...", "authors": ["First Last", ...], "abstract": "...",
         "arxiv_id": "2607.26679", "url": "...", "pdf_url": "...", "date": "2026-07-29",
         "tag": "swarm"}' | python3 scripts/zotero-web-add.py [--dry-run]

.env 필요(~/2nd/.env): ZOTERO_API_KEY, ZOTERO_USER_ID
  (zotero.org/settings/security#applications → Create new private key,
   Personal Library: Allow library access + Allow write access)
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = WIKI_ROOT / ".env"
STATE_PATH = WIKI_ROOT / ".ua" / "zotero-pushed.txt"
API_BASE = "https://api.zotero.org"
UA = "2ndBrainFetcher/2.0"


def load_env() -> dict:
    env = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip()
    return env


_ENV = load_env()
API_KEY = os.environ.get("ZOTERO_API_KEY") or _ENV.get("ZOTERO_API_KEY", "")
USER_ID = os.environ.get("ZOTERO_USER_ID") or _ENV.get("ZOTERO_USER_ID", "")


def api_request(method: str, path: str, json_body=None, raw_body: bytes | None = None,
                 extra_headers: dict | None = None) -> tuple[int, bytes]:
    headers = {"Zotero-API-Key": API_KEY, "Zotero-API-Version": "3"}
    if extra_headers:
        headers.update(extra_headers)
    data = None
    if raw_body is not None:
        data = raw_body
    elif json_body is not None:
        data = json.dumps(json_body).encode("utf-8")
        headers.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(f"{API_BASE}{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def load_pushed() -> set[str]:
    if not STATE_PATH.exists():
        return set()
    return set(STATE_PATH.read_text(encoding="utf-8").splitlines())


def mark_pushed(key: str) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with STATE_PATH.open("a", encoding="utf-8") as f:
        f.write(key + "\n")


def build_creators(authors: list[str]) -> list[dict]:
    creators = []
    for name in authors:
        parts = name.rsplit(" ", 1)
        if len(parts) == 2:
            creators.append({"creatorType": "author", "firstName": parts[0], "lastName": parts[1]})
        else:
            creators.append({"creatorType": "author", "firstName": "", "lastName": name})
    return creators


def find_existing_by_title(title: str) -> str | None:
    """Zotero 라이브러리에서 같은 제목의 아이템이 이미 있는지 서버에 직접 확인한다.

    로컬 state 파일(zotero-pushed.txt)은 "이 스크립트가 이전에 push했는가"만
    안다 — 브라우저 Connector나 마법봉으로 수동 추가된 항목은 모른다. 이 체크가
    없으면 수동으로 이미 추가한 논문을 자동수집이 다시 push해 중복 아이템을
    만든다(2026-08-10 실측 중 발견: arXiv:2607.26679가 중복 생성됐었음).
    """
    q = urllib.parse.quote(title)
    status, body = api_request(
        "GET", f"/users/{USER_ID}/items?q={q}&qmode=titleCreatorYear&itemType=-attachment&limit=10"
    )
    if status != 200:
        return None  # 조회 실패 시 안전하게 "모른다"로 취급 — 로컬 state로만 판단
    try:
        items = json.loads(body)
    except json.JSONDecodeError:
        return None
    norm = title.strip().lower()
    for it in items:
        if it.get("data", {}).get("title", "").strip().lower() == norm:
            return it["key"]
    return None


def create_parent_item(paper: dict, dry_run: bool) -> str | None:
    item = {
        "itemType": "preprint",
        "title": paper["title"],
        "creators": build_creators(paper.get("authors", [])),
        "abstractNote": paper.get("abstract", ""),
        "date": paper.get("date", ""),
        "DOI": paper.get("doi", f"10.48550/arXiv.{paper['arxiv_id']}" if paper.get("arxiv_id") else ""),
        "url": paper.get("url", ""),
        "repository": "arXiv",
        "archiveID": f"arXiv:{paper['arxiv_id']}" if paper.get("arxiv_id") else "",
        "tags": [{"tag": "auto:2nd-brain"}] + ([{"tag": paper["tag"]}] if paper.get("tag") else []),
    }
    if dry_run:
        print(f"  [DRY-RUN] 아이템 생성 → {item['title']}")
        return None

    status, body = api_request("POST", f"/users/{USER_ID}/items", json_body=[item])
    if status != 200:
        print(f"  [ERROR] 아이템 생성 실패({status}): {body[:300]!r}", file=sys.stderr)
        return None
    result = json.loads(body)
    success = result.get("successful", {})
    if not success:
        print(f"  [ERROR] 아이템 생성 실패: {result.get('failed')}", file=sys.stderr)
        return None
    key = list(success.values())[0]["key"]
    print(f"  [OK] 아이템 생성 → {key}")
    return key


def upload_pdf(parent_key: str, pdf_url: str, filename: str, dry_run: bool) -> bool:
    if dry_run:
        print(f"  [DRY-RUN] PDF 업로드 → {filename}")
        return True

    req = urllib.request.Request(pdf_url, headers={"User-Agent": UA})
    pdf_bytes = urllib.request.urlopen(req, timeout=30).read()
    md5 = hashlib.md5(pdf_bytes).hexdigest()
    mtime_ms = int(time.time() * 1000)

    att_item = {
        "itemType": "attachment",
        "parentItem": parent_key,
        "linkMode": "imported_url",
        "title": filename,
        "filename": filename,
        "contentType": "application/pdf",
        "url": pdf_url,
        "md5": None,
        "mtime": None,
    }
    status, body = api_request("POST", f"/users/{USER_ID}/items", json_body=[att_item])
    if status != 200:
        print(f"  [ERROR] 첨부 아이템 생성 실패({status}): {body[:300]!r}", file=sys.stderr)
        return False
    result = json.loads(body)
    success = result.get("successful", {})
    if not success:
        print(f"  [ERROR] 첨부 아이템 생성 실패: {result.get('failed')}", file=sys.stderr)
        return False
    att_key = list(success.values())[0]["key"]

    auth_body = urllib.parse.urlencode(
        {"md5": md5, "filename": filename, "filesize": len(pdf_bytes), "mtime": mtime_ms}
    ).encode("ascii")
    status, body = api_request(
        "POST", f"/users/{USER_ID}/items/{att_key}/file", raw_body=auth_body,
        extra_headers={"Content-Type": "application/x-www-form-urlencoded", "If-None-Match": "*"},
    )
    if status != 200:
        print(f"  [ERROR] 업로드 인가 실패({status}): {body[:300]!r}", file=sys.stderr)
        return False
    auth = json.loads(body)
    if auth.get("exists"):
        print("  [OK] 동일 파일이 이미 Zotero에 존재")
        return True

    prefix = auth.get("prefix", "").encode("latin-1") if isinstance(auth.get("prefix"), str) else b""
    suffix = auth.get("suffix", "").encode("latin-1") if isinstance(auth.get("suffix"), str) else b""
    up_req = urllib.request.Request(
        auth["url"], data=prefix + pdf_bytes + suffix, method="POST",
        headers={"Content-Type": auth.get("contentType", "application/octet-stream")},
    )
    try:
        with urllib.request.urlopen(up_req, timeout=60) as r:
            up_status = r.status
    except urllib.error.HTTPError as e:
        print(f"  [ERROR] 파일 업로드 실패({e.code}): {e.read()[:300]!r}", file=sys.stderr)
        return False
    if up_status not in (200, 201, 204):
        print(f"  [ERROR] 파일 업로드 실패({up_status})", file=sys.stderr)
        return False

    reg_body = urllib.parse.urlencode({"upload": auth["uploadKey"]}).encode("ascii")
    status, body = api_request(
        "POST", f"/users/{USER_ID}/items/{att_key}/file", raw_body=reg_body,
        extra_headers={"Content-Type": "application/x-www-form-urlencoded", "If-None-Match": "*"},
    )
    if status != 204:
        print(f"  [ERROR] 업로드 등록 실패({status}): {body[:300]!r}", file=sys.stderr)
        return False
    print(f"  [OK] PDF 업로드 완료 → {filename} ({len(pdf_bytes)} bytes)")
    return True


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    if not API_KEY or not USER_ID:
        print("[ERROR] ZOTERO_API_KEY / ZOTERO_USER_ID가 .env에 없음", file=sys.stderr)
        sys.exit(1)

    paper = json.load(sys.stdin)
    dedupe_key = paper.get("url") or paper.get("arxiv_id", "")
    if dedupe_key in load_pushed():
        print(f"  skip (이미 push됨): {paper.get('title', '')}")
        return

    if not dry_run:
        existing_key = find_existing_by_title(paper["title"])
        if existing_key:
            print(f"  skip (Zotero에 이미 존재: {existing_key}): {paper['title']}")
            mark_pushed(dedupe_key)  # 다음부터 서버 조회 없이 로컬 state로 바로 스킵
            return

    parent_key = create_parent_item(paper, dry_run)
    if not dry_run and not parent_key:
        sys.exit(1)

    if paper.get("pdf_url"):
        slug = paper.get("arxiv_id", "paper").replace("/", "_")
        ok = upload_pdf(parent_key, paper["pdf_url"], f"{slug}.pdf", dry_run) if not dry_run else True
        if not dry_run and not ok:
            sys.exit(1)

    if not dry_run:
        mark_pushed(dedupe_key)


if __name__ == "__main__":
    main()
