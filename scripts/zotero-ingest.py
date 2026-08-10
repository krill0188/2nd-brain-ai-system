#!/usr/bin/env python3
"""
zotero-ingest.py — Zotero → raw/papers/<topic>/ 인제스트 스크립트
사용: python3 scripts/zotero-ingest.py [--topic <tag>] [--dry-run]

Zotero 로컬 API(http://localhost:23119)에서 신규 항목을 가져와
~/2nd/raw/papers/<topic>/ 에 Markdown 레코드를 생성한다.

요구사항:
  - Zotero 앱 실행 중
  - Zotero Settings → Advanced → "Allow other applications" 켜기
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import sys
import urllib.request
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
RAW_PAPERS = WIKI_ROOT / "raw" / "papers"
ATTACHMENT_ROOT = RAW_PAPERS / "files"
ZOTERO_API = "http://localhost:23119/api"
ZOTERO_USER = "users/0"  # 로컬 모드 기본값
# Zotero가 "imported_file" 첨부를 실제로 복사해두는 로컬 저장 디렉토리.
# 동기화 여부와 무관하게 모든 로컬 Zotero 설치가 기본으로 이 위치를 쓴다.
ZOTERO_DATA_DIR = Path(os.environ.get("ZOTERO_DATA_DIR", str(Path.home() / "Zotero")))
_warned_missing_zotero_dir = False

# SCHEMA.md 등록 드론 태그 → raw/papers/<topic>/ 매핑
TAG_MAP = {
    "drone-sw":      "drone-sw",
    "drone-ai":      "drone-ai",
    "datalink":      "datalink",
    "swarm":         "swarm",
    "drone-hw":      "drone-hw",
    "voice-control": "voice-control",
    "ai-agent":      "ai-agent",
    "drone":         "drone-sw",   # 일반 drone → drone-sw 기본
}


def zotero_get(path: str) -> dict | list:
    url = f"{ZOTERO_API}/{ZOTERO_USER}/{path}?format=json&limit=100"
    req = urllib.request.Request(url, headers={"Zotero-API-Version": "3"})
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.loads(r.read())


def resolve_topic(item_data: dict) -> str:
    """Zotero 태그에서 드론 토픽 결정. 매핑 없으면 _unclassified."""
    tags = [t.get("tag", "").lower() for t in item_data.get("tags", [])]
    for tag in tags:
        if tag in TAG_MAP:
            return TAG_MAP[tag]
    return "_unclassified"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:80]


def sha256_str(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def find_pdf_attachment(parent_key: str) -> dict | None:
    """부모 아이템의 자식 첨부 중 로컬에 실제로 존재하는 PDF 파일을 찾는다.

    linked_file/linked_url(Zotero storage 밖 경로)은 이 머신에서 항상 접근
    가능하다는 보장이 없어 제외한다 — imported_file/imported_url만 다룬다.

    contentType == application/pdf인 것만 채택한다. "Add Item by Identifier"로
    추가한 arXiv 논문은 실제 PDF 말고도 웹페이지 스냅샷(text/html) 첨부가 같이
    딸려오고, 스냅샷이 children 응답에서 PDF보다 먼저 나올 수 있다 — contentType
    체크 없이 첫 번째 매치를 쓰면 스냅샷 HTML을 "논문 원문"으로 잘못 저장하게
    된다(2026-08-10 실측 테스트 중 발견: arXiv:2607.26679 첫 자식이 스냅샷이었음).
    """
    global _warned_missing_zotero_dir
    if not ZOTERO_DATA_DIR.exists():
        if not _warned_missing_zotero_dir:
            print(f"  [WARN] Zotero 데이터 디렉토리 없음: {ZOTERO_DATA_DIR} "
                  f"(ZOTERO_DATA_DIR 환경변수 또는 --zotero-data-dir로 지정) — 첨부 복사 전체 스킵")
            _warned_missing_zotero_dir = True
        return None

    try:
        children = zotero_get(f"items/{parent_key}/children")
    except Exception as e:
        print(f"  [WARN] 첨부 조회 실패 ({parent_key}): {e}")
        return None
    if not isinstance(children, list):
        return None

    for child in children:
        cd = child.get("data", {})
        if cd.get("itemType") != "attachment":
            continue
        if cd.get("linkMode") not in ("imported_file", "imported_url"):
            continue
        if cd.get("contentType") != "application/pdf":
            continue
        filename = cd.get("filename", "")
        att_key = child.get("key", "")
        if not filename or not att_key:
            continue
        local_path = ZOTERO_DATA_DIR / "storage" / att_key / filename
        if local_path.exists():
            return {"path": local_path, "filename": filename, "content_type": cd.get("contentType", "")}
    return None


def copy_attachment(attachment: dict, topic: str, slug: str, dry_run: bool) -> dict | None:
    """첨부파일을 raw/papers/files/<topic>/<slug><ext>로 복사하고 메타데이터를 반환.

    raw/ 본문 불변성 원칙과 별개 취급: 첨부 파일 자체는 raw Markdown 레코드가
    아니라 그것을 보조하는 사본이므로(SCHEMA.md Provenance: "Assets and
    attachments ... are not canonical sources entries by themselves"),
    존재 여부만 멱등하게 체크하면 된다.
    """
    ext = Path(attachment["filename"]).suffix or ".pdf"
    dest_dir = ATTACHMENT_ROOT / topic
    dest_file = dest_dir / f"{slug}{ext}"
    rel_path = str(dest_file.relative_to(WIKI_ROOT))

    if dest_file.exists():
        return {"attachment_path": rel_path, "attachment_sha256": sha256_file(dest_file)}

    if dry_run:
        print(f"  [DRY-RUN] 첨부 → {rel_path}")
        return {"attachment_path": rel_path, "attachment_sha256": "(dry-run)"}

    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(attachment["path"], dest_file)
    digest = sha256_file(dest_file)
    print(f"  [OK] 첨부 저장 → {rel_path}")
    return {"attachment_path": rel_path, "attachment_sha256": digest}


def build_markdown(item: dict, attachment_meta: dict | None = None) -> str:
    d = item.get("data", {})
    title = d.get("title", "Untitled")
    authors = "; ".join(
        f"{c.get('lastName', '')}, {c.get('firstName', '')}"
        for c in d.get("creators", [])
        if c.get("creatorType") == "author"
    ) or "Unknown"
    year = d.get("date", "")[:4] if d.get("date") else ""
    doi = d.get("DOI", "")
    url = d.get("url", "")
    abstract = d.get("abstractNote", "").strip()
    item_type = d.get("itemType", "journalArticle")
    tags_raw = [t.get("tag", "") for t in d.get("tags", [])]
    today = datetime.date.today().isoformat()
    zotero_key = item.get("key", "")

    lines = [
        "---",
        f"title: {json.dumps(title)}",
        f"created: {today}",
        f"updated: {today}",
        f"type: paper",
        f"item_type: {item_type}",
        f"authors: {json.dumps(authors)}",
        f"year: \"{year}\"",
        f"doi: \"{doi}\"",
        f"url: \"{url}\"",
        f"zotero_key: {zotero_key}",
        f"tags: {json.dumps(tags_raw)}",
        *([f"attachment_path: {attachment_meta['attachment_path']}",
           f"attachment_sha256: {attachment_meta['attachment_sha256']}"] if attachment_meta else []),
        f"sha256: {sha256_str(title + authors + year)}",
        "---",
        "",
        f"# {title}",
        "",
        f"**Authors**: {authors}  ",
        f"**Year**: {year}  ",
        *([ f"**DOI**: {doi}  "] if doi else []),
        *([ f"**URL**: {url}"] if url else []),
        "",
    ]
    if abstract:
        lines += ["## Abstract", "", abstract, ""]
    lines += [
        "## Notes",
        "",
        "<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->",
        "",
    ]
    return "\n".join(lines)


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip().strip('"')
    return fm


def backfill_attachments(dry_run: bool = False) -> None:
    """이미 인제스트된 raw/papers/*/*.md 중 첨부가 없는 레코드에 소급 반영.

    SCHEMA.md "Zotero metadata repair" 허용 규칙(프론트매터만 교체, 본문 바이트
    불변, 기존 sha256 유지)을 그대로 따른다 — attachment_path/attachment_sha256를
    sha256 라인 앞에 삽입할 뿐, `---` 이후 본문은 한 바이트도 건드리지 않는다.
    """
    md_files = sorted(p for p in RAW_PAPERS.glob("*/*.md") if p.parent.name != "files")
    patched = already = no_key = no_attachment = 0

    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if "attachment_path" in fm:
            already += 1
            continue
        zotero_key = fm.get("zotero_key", "")
        if not zotero_key:
            no_key += 1
            continue

        topic = md_file.parent.name
        slug = md_file.stem

        attachment = find_pdf_attachment(zotero_key)
        if not attachment:
            no_attachment += 1
            continue

        meta = copy_attachment(attachment, topic, slug, dry_run)
        if not meta:
            continue

        if dry_run:
            print(f"  [DRY-RUN] frontmatter 패치 예정 → {md_file.relative_to(WIKI_ROOT)}")
            patched += 1
            continue

        new_lines = []
        inserted = False
        for line in text.splitlines(keepends=True):
            if line.startswith("sha256:") and not inserted:
                new_lines.append(f"attachment_path: {meta['attachment_path']}\n")
                new_lines.append(f"attachment_sha256: {meta['attachment_sha256']}\n")
                inserted = True
            new_lines.append(line)
        md_file.write_text("".join(new_lines), encoding="utf-8")
        print(f"  [OK] frontmatter 패치 → {md_file.relative_to(WIKI_ROOT)}")
        patched += 1

    print(f"\n첨부 소급 반영 완료: 패치 {patched} | 이미보유 {already} | "
          f"zotero_key없음 {no_key} | Zotero측 첨부없음 {no_attachment}")


def ingest(dry_run: bool = False, topic_filter: str | None = None, skip_attachments: bool = False) -> None:
    # Zotero 연결 확인
    try:
        items = zotero_get("items?itemType=-attachment")
    except Exception as e:
        print(f"[ERROR] Zotero 로컬 API 연결 실패: {e}")
        print("  → Zotero 앱을 실행하고 Settings → Advanced → 'Allow other applications' 활성화 필요")
        sys.exit(1)

    if not isinstance(items, list):
        items = items.get("items", [])

    new_count = 0
    skip_count = 0

    for item in items:
        d = item.get("data", {})
        if d.get("itemType") == "attachment":
            continue

        topic = resolve_topic(d)
        if topic_filter and topic != topic_filter:
            continue

        title = d.get("title", "Untitled")
        slug = slugify(title)
        out_dir = RAW_PAPERS / topic
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{slug}.md"

        if out_file.exists():
            skip_count += 1
            continue

        attachment_meta = None
        if not skip_attachments:
            try:
                raw_attachment = find_pdf_attachment(item.get("key", ""))
                if raw_attachment:
                    attachment_meta = copy_attachment(raw_attachment, topic, slug, dry_run)
            except Exception as e:
                print(f"  [WARN] 첨부 처리 실패, 메타데이터만 저장: {e}")

        md = build_markdown(item, attachment_meta)

        if dry_run:
            print(f"[DRY-RUN] → {out_file.relative_to(WIKI_ROOT)}")
        else:
            out_file.write_text(md, encoding="utf-8")
            # inbox에도 복사 → 다음 04:00 cron이 위키 canonical로 컴파일
            inbox_file = WIKI_ROOT / "inbox" / f"zotero-{slug}.md"
            if not inbox_file.exists() and not (WIKI_ROOT / "inbox" / "processed" / f"zotero-{slug}.md").exists():
                inbox_file.write_text(md, encoding="utf-8")
            print(f"[OK] → {out_file.relative_to(WIKI_ROOT)} (+inbox)")
        new_count += 1

    print(f"\n수집 완료: 신규 {new_count}개 | 기존 스킵 {skip_count}개")
    if topic_filter:
        print(f"필터: {topic_filter}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zotero → raw/papers/<topic>/ 인제스트")
    parser.add_argument("--topic", help="특정 토픽만 수집 (예: drone-sw)")
    parser.add_argument("--dry-run", action="store_true", help="파일 쓰기 없이 미리보기")
    parser.add_argument("--skip-attachments", action="store_true",
                         help="PDF 첨부 복사 생략(메타데이터 레코드만 생성)")
    parser.add_argument("--backfill-attachments", action="store_true",
                         help="이미 인제스트된 레코드 중 첨부 누락분만 소급 반영하고 종료")
    parser.add_argument("--zotero-data-dir",
                         help="Zotero 데이터 디렉토리 경로 (기본: $ZOTERO_DATA_DIR 또는 ~/Zotero)")
    args = parser.parse_args()

    if args.zotero_data_dir:
        ZOTERO_DATA_DIR = Path(args.zotero_data_dir)

    if args.backfill_attachments:
        backfill_attachments(dry_run=args.dry_run)
    else:
        ingest(dry_run=args.dry_run, topic_filter=args.topic, skip_attachments=args.skip_attachments)
