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
SERVICE = "https://www.law.go.kr/DRF/lawService.do"  # 본문(조문) API — 여기서는 기본정보의 대표 시행일·부분 시행일만 쓴다
FEED_PATH = os.path.join(HOME, "2nd", ".ua", "news-feed.json")
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
    """공포일·시행일을 해석할 수 없으면 None — 날짜를 지어내지 않는다.
    시행일은 본문 API 의 대표 시행일(기본정보.시행일자)을 쓰고, 일부 조항이 나중에 시행되면 "(일부 YYYY-MM-DD 시행)"을 병기한다.
    목록 API 의 시행일자는 후속 부분 시행일일 수 있어(예: 시행령 대표 2026-07-01, 목록 2026-07-09) 본문 API 를 못 받았을 때만 폴백으로 쓴다."""
    published = iso_day(rec.get("공포일자"))
    effective = iso_day(rec.get("대표시행일자")) or iso_day(rec.get("시행일자"))
    mst = rec.get("법령일련번호", "")
    if not published or not effective or not mst:
        return None
    kind = rec.get("제개정구분명") or "현행"
    partial = [iso_day(d) for d in (rec.get("부분시행일자") or "").split(",") if iso_day(d)]
    suffix = f" (일부 {', '.join(partial)} 시행)" if partial else ""
    return {
        "title": f"{TITLE_PREFIX}{name} · {kind} · 시행 {effective}{suffix}",
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


def fetch_service(oc, mst, timeout=60):
    qs = urllib.parse.urlencode({"OC": oc, "target": "law", "MST": mst, "type": "JSON"})
    with urllib.request.urlopen(urllib.request.Request(f"{SERVICE}?{qs}", headers={"User-Agent": "2nd-brain/fetch-law"}), timeout=timeout) as r:
        return json.load(r)


def service_dates(payload):
    """본문 API 응답에서 (대표 시행일, 부분 시행일 목록)을 8자리 문자열로 뽑는다.
    대표 = 기본정보.시행일자, 부분 = 기본정보.조문시행일자문자열("20260709:제26조제1항제30호, …")의 날짜 중 대표와 다른 것. 해석 불가면 (None, [])."""
    base = ((payload or {}).get("법령") or payload or {}).get("기본정보") or {}
    rep = str(base.get("시행일자") or "").strip()
    rep = rep if iso_day(rep) else None
    found = re.findall(r"(\d{8})\s*:", str(base.get("조문시행일자문자열") or ""))
    return rep, sorted({d for d in found if iso_day(d) and d != rep})


def last_service_fields(store_dir, law_id, mst):
    """본문 API 가 일시적으로 실패한 날, 같은 개정판(MST)의 직전 보존 레코드에서 대표·부분 시행일을 이어받는다(제목이 폴백 값으로 흔들리지 않도록)."""
    d = os.path.join(store_dir, law_id.replace(":", "_"))
    if not os.path.isdir(d):
        return {}
    for f in sorted(os.listdir(d), reverse=True):
        if not f.endswith(".json"):
            continue
        try:
            with open(os.path.join(d, f), encoding="utf-8") as fh:
                r = json.load(fh)
        except (OSError, ValueError):
            continue
        return {k: r[k] for k in ("대표시행일자", "부분시행일자") if k in r} if r.get("법령일련번호") == mst else {}
    return {}


def sync_feed_titles(items, feed_path=FEED_PATH):
    """이미 피드에 있는 같은 URL 항목의 제목이 달라졌으면 갱신한다(news-feed-append 는 URL 중복을 건너뛰므로 제목 보정은 여기서 한다).
    항목의 sha256 은 그대로라 이벤트 id 는 바뀌지 않는다. 바뀐 건수를 돌려준다. 저장 서식은 news-feed-append 와 같다(indent=1)."""
    if not items or not os.path.exists(feed_path):
        return 0
    with open(feed_path, encoding="utf-8") as f:
        feed = json.load(f)
    want = {it["url"]: it["title"] for it in items}
    n = 0
    for e in feed:
        t = want.get(e.get("url"))
        if t and e.get("title") != t:
            e["title"] = t
            n += 1
    if n:
        tmp = feed_path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(feed, f, ensure_ascii=False, indent=1)
        os.replace(tmp, feed_path)
    return n


def append_to_feed(items):
    r = subprocess.run([sys.executable, FEED_APPEND], input=json.dumps(items, ensure_ascii=False), text=True, capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"news-feed-append 실패: {r.stderr.strip()[:200]}")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--laws", default=DEFAULT_LAWS)
    ap.add_argument("--store-dir", default=DEFAULT_STORE)
    ap.add_argument("--fixture-dir")
    ap.add_argument("--feed", default=FEED_PATH)  # 제목 보정 대상 피드(시험에서 임시 경로로 바꾼다)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)

    try:
        with open(a.laws, encoding="utf-8") as fh:
            cfg = json.load(fh)
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
    all_items, fallback = [], []  # all_items: 변경 여부와 무관한 이번 실행의 모든 법령 항목(제목 보정용)
    pending = []  # 피드 추가에 성공한 뒤에만 보존 파일을 쓴다(실패 시 다음 실행이 다시 시도하도록)
    for law_id, name in targets:
        try:
            if a.fixture_dir:
                with open(os.path.join(a.fixture_dir, law_id.replace(":", "_") + ".json"), encoding="utf-8") as fh:
                    payload = json.load(fh)
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
        # 본문 API 에서 대표 시행일·부분 시행일을 받는다. 실패해도 수집은 계속한다(직전 보존분 → 목록 API 시행일 순으로 폴백).
        rep, partial, sp = None, [], None
        try:
            if a.fixture_dir:
                sf = os.path.join(a.fixture_dir, law_id.replace(":", "_") + ".service.json")
                sp = None
                if os.path.exists(sf):
                    with open(sf, encoding="utf-8") as fh:
                        sp = json.load(fh)
            else:
                sp = fetch_service(oc, rec.get("법령일련번호", ""))
            rep, partial = service_dates(sp) if sp else (None, [])
        except Exception as e:  # URL에 키가 있으므로 종류만 남긴다
            fallback.append(f"{name}({type(e).__name__})")
        else:
            if not rep:
                fallback.append(f"{name}(대표 시행일 미확인)")
        if rep:
            rec["대표시행일자"] = rep
            if partial:
                rec["부분시행일자"] = ",".join(partial)
        else:
            rec.update(last_service_fields(a.store_dir, law_id, rec.get("법령일련번호", "")))
        item = to_feed_item(name, rec)
        if not item:
            failed.append(f"{name}(날짜·일련번호 해석 불가)")
            continue
        all_items.append(item)
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
    synced = 0
    if all_items and not a.dry_run:
        try:
            synced = sync_feed_titles(all_items, a.feed)
        except Exception as e:
            failed.append(f"제목 보정({type(e).__name__})")
    print(f"  law: 대상 {len(targets)} · 신규 {len(items)} · 변경없음 {unchanged} · 실패 {len(failed)}" + (f" · 대표시행일 폴백 {len(fallback)}" if fallback else "") + (f" · 제목 보정 {synced}" if synced else "") + (" · (dry-run)" if a.dry_run else ""))
    code = 2 if failed else 0
    if not a.dry_run:
        log_run(a.store_dir, {"status": "failed" if failed else "ok", "targets": len(targets), "new": len(items), "unchanged": unchanged, "failed": failed, "fallback": fallback, "titles_synced": synced})
    if failed:
        print("  ⚠️  실패: " + ", ".join(failed), file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
