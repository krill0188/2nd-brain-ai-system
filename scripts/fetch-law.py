#!/usr/bin/env python3
"""fetch-law.py — 법제처 국가법령정보 오픈API로 대상 법령의 현행 정보를 조회해 news-feed에 '법령 이벤트'로 추가한다.

설계: drone-wiki-web/docs/dikw-dynamic-ontology-design.md §5 (동향 이벤트 레이어) — 법령 변경을 이벤트로 적재하는 1단계.
- 대상 법령 목록은 drone-wiki-web/data/ontology/laws.json 한 곳에서만 관리한다(--laws). 마스터가 확정한 목록만 조회한다.
- 이벤트는 사실이 아니다(미검증). 제목·URL·날짜만 피드에 싣고 본문은 가져오지 않는다.
- 인증키(LAW_OC)는 환경변수 또는 ~/2nd/.env 에서만 읽고, 출력·로그·피드·보존 파일 어디에도 쓰지 않는다.
  (API의 '법령상세링크'에는 키가 박혀 있으므로 그 필드는 버리고 공개 URL을 직접 만든다.)
- 조회 결과(필요 필드만)는 .ua/laws/<법령ID>/ 에 해시와 함께 보존한다. raw/ 는 발행 계층(publication-gate)이라 쓰지 않는다.
- 같은 내용(해시 동일)이면 피드에 다시 넣지 않는다. 개정되어 법령일련번호·시행일이 바뀌면 새 이벤트가 된다.

제목 형식(빌더와의 계약): "[법령] {법령명} · {제개정구분} · 시행 YYYY-MM-DD"
URL: https://www.law.go.kr/법령/{법령명}#rev-{법령일련번호}  (프래그먼트는 개정판마다 다른 항목으로 중복 제거되게 하려는 것)

사용:
  python3 scripts/fetch-law.py                  # 실제 조회 → 보존 + 피드 추가
  python3 scripts/fetch-law.py --dry-run        # 조회만, 아무것도 쓰지 않음
  python3 scripts/fetch-law.py --fixture-dir D  # D/<법령ID에서 ':'→'_'>.json 을 응답 대신 사용(시험용)
종료 코드: 0 정상(키 없음 스킵 포함) / 2 일부 법령 조회 실패 / 1 설정 오류
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime

HOME = os.path.expanduser("~")
DEFAULT_LAWS = os.path.join(HOME, "projectm", "drone-wiki-web", "data", "ontology", "laws.json")
DEFAULT_STORE = os.path.join(HOME, "2nd", ".ua", "laws")
FEED_APPEND = os.path.join(HOME, "2nd", "scripts", "news-feed-append.py")
API = "https://www.law.go.kr/DRF/lawSearch.do"
# 보존·이벤트에 쓰는 필드만 통과시킨다(키가 들어 있는 '법령상세링크' 등은 버린다).
KEEP_FIELDS = ("법령일련번호", "법령명한글", "법령ID", "공포일자", "공포번호", "제개정구분명", "소관부처명", "법령구분명", "시행일자", "현행연혁코드")
TITLE_PREFIX = "[법령] "


def load_oc():
    oc = os.environ.get("LAW_OC", "").strip()
    if oc:
        return oc
    try:
        for line in open(os.path.join(HOME, "2nd", ".env"), encoding="utf-8"):
            if line.startswith("LAW_OC="):
                return line.split("=", 1)[1].strip().strip('"\'')
    except OSError:
        pass
    return ""


def iso_day(s):
    """'20260401' → '2026-04-01'. 형식이 틀리거나 존재하지 않는 날짜면 None."""
    m = re.fullmatch(r"(\d{4})(\d{2})(\d{2})", (s or "").strip())
    if not m:
        return None
    try:
        return date(int(m[1]), int(m[2]), int(m[3])).isoformat()
    except ValueError:
        return None


def pick_exact(payload, name):
    """검색 결과는 유사어까지 돌려준다(예: '항공안전법' → 시행령·시행규칙 포함). 법령명이 정확히 같은 항목만 고른다."""
    node = (payload or {}).get("LawSearch") or {}
    laws = node.get("law") or []
    if isinstance(laws, dict):  # 결과가 1건이면 리스트가 아닌 객체로 온다
        laws = [laws]
    exact = [x for x in laws if isinstance(x, dict) and (x.get("법령명한글") or "").strip() == name]
    # 연혁 항목이 섞여 있으면 현행만. 필드가 아예 없으면 그대로 둔다.
    current = [x for x in exact if x.get("현행연혁코드") in (None, "", "현행")]
    return (current or exact or [None])[0]


def clean_record(rec):
    return {k: str(rec[k]).strip() for k in KEEP_FIELDS if rec.get(k) not in (None, "")}


def to_feed_item(name, rec):
    """공포일·시행일을 해석할 수 없으면 None — 날짜를 지어내지 않는다."""
    published, effective = iso_day(rec.get("공포일자")), iso_day(rec.get("시행일자"))
    mst = rec.get("법령일련번호", "")
    if not published or not effective or not mst:
        return None
    kind = rec.get("제개정구분명") or "현행"
    return {
        "title": f"{TITLE_PREFIX}{name} · {kind} · 시행 {effective}",
        "url": f"https://www.law.go.kr/법령/{urllib.parse.quote(name)}#rev-{urllib.parse.quote(mst)}",
        "source": "law.go.kr", "domain": "regulations", "type": "regulation", "region": "KR",
        "summary": "", "published": published,
    }


def record_hash(rec):
    return hashlib.sha256(json.dumps(rec, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:12]


def already_stored(store_dir, law_id, digest):
    d = os.path.join(store_dir, law_id.replace(":", "_"))
    return os.path.isdir(d) and any(f.endswith(f"-{digest}.json") for f in os.listdir(d))


def store(store_dir, law_id, rec, digest, today):
    d = os.path.join(store_dir, law_id.replace(":", "_"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"{today}-{digest}.json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


def log_run(store_dir, entry):
    """실행 기록 1줄(.ua/laws/runs.jsonl). 파이프라인 로그에는 이 스크립트의 출력이 남지 않을 수 있어, 실패율 같은 관찰 지표를 여기서 직접 센다. 키·URL은 넣지 않는다."""
    os.makedirs(store_dir, exist_ok=True)
    entry = {"at": datetime.now().astimezone().isoformat(timespec="seconds"), **entry}
    with open(os.path.join(store_dir, "runs.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")


def fetch_remote(oc, name, timeout=20):
    qs = urllib.parse.urlencode({"OC": oc, "target": "law", "type": "JSON", "query": name})
    with urllib.request.urlopen(urllib.request.Request(f"{API}?{qs}", headers={"User-Agent": "2nd-brain/fetch-law"}), timeout=timeout) as r:
        return json.load(r)


def append_to_feed(items):
    r = subprocess.run([sys.executable, FEED_APPEND], input=json.dumps(items, ensure_ascii=False), text=True, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"news-feed-append 실패: {r.stderr.strip()[:200]}")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--laws", default=DEFAULT_LAWS)
    ap.add_argument("--store-dir", default=DEFAULT_STORE)
    ap.add_argument("--fixture-dir")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)

    try:
        cfg = json.load(open(a.laws, encoding="utf-8"))
        targets = [(x["id"], x["name"]) for x in cfg["laws"]]
    except (OSError, ValueError, KeyError) as e:
        print(f"fetch-law: 대상 법령 목록을 읽을 수 없음 — {type(e).__name__}", file=sys.stderr)
        return 1
    if cfg.get("confirmed") is not True:
        print("  ℹ️  laws.json 이 마스터 확정 전(confirmed≠true) — 초안 목록으로 조회합니다(피드에는 계속 추가되나 화면 노출은 막혀 있음)")

    oc = "" if a.fixture_dir else load_oc()
    if not a.fixture_dir and not oc:
        print("  law: LAW_OC 없음 — 스킵(발급: https://open.law.go.kr → 오픈API 신청, 키는 ~/2nd/.env 의 LAW_OC=)")
        if not a.dry_run:
            log_run(a.store_dir, {"status": "skipped-no-key", "targets": len(targets)})
        return 0

    today = date.today().isoformat()
    items, failed, unchanged = [], [], 0
    pending = []  # 피드 추가에 성공한 뒤에만 보존 파일을 쓴다(실패 시 다음 실행이 다시 시도하도록)
    for law_id, name in targets:
        try:
            if a.fixture_dir:
                payload = json.load(open(os.path.join(a.fixture_dir, law_id.replace(":", "_") + ".json"), encoding="utf-8"))
            else:
                payload = fetch_remote(oc, name)
        except Exception as e:  # URL에 키가 있으므로 예외 본문은 출력하지 않고 종류만 남긴다
            failed.append(f"{name}({type(e).__name__})")
            continue
        rec = pick_exact(payload, name)
        if not rec:
            failed.append(f"{name}(정확히 일치하는 법령 없음)")
            continue
        rec = clean_record(rec)
        item = to_feed_item(name, rec)
        if not item:
            failed.append(f"{name}(날짜·일련번호 해석 불가)")
            continue
        digest = record_hash(rec)
        if already_stored(a.store_dir, law_id, digest):
            unchanged += 1
            continue
        items.append(item)
        pending.append((law_id, rec, digest))
        print(f"  + {item['title']}")

    if items and not a.dry_run:
        try:
            append_to_feed(items)
            for law_id, rec, digest in pending:
                store(a.store_dir, law_id, rec, digest, today)
        except Exception as e:
            failed.append(f"피드 추가({type(e).__name__})")
    print(f"  law: 대상 {len(targets)} · 신규 {len(items)} · 변경없음 {unchanged} · 실패 {len(failed)}" + (" · (dry-run)" if a.dry_run else ""))
    code = 2 if failed else 0
    if not a.dry_run:
        log_run(a.store_dir, {"status": "failed" if failed else "ok", "targets": len(targets), "new": len(items), "unchanged": unchanged, "failed": failed})
    if failed:
        print("  ⚠️  실패: " + ", ".join(failed), file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
