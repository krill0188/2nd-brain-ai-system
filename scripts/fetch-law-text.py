#!/usr/bin/env python3
"""fetch-law-text.py — 법령 3단계(조문 원문) 수집기. 1단계(fetch-law.py)가 보존한 최신 개정판(MST)의 본문(lawService)을 받아 보존한다.

설계: drone-wiki-web/docs/law-stage3-design.md §4.2. 보존은 비공개 영역(~/2nd/.ua/laws-text/, raw/ 아님).
동작: laws.json 의 각 법령 → 1단계 보존 레코드(~/2nd/.ua/laws/<id>/) 중 최신의 법령일련번호(MST) → 같은 MST 본문이 이미 있으면 호출하지 않는다
      → 없으면 lawService 로 받아 검증(법령명 일치·조문 존재) 후 <MST>-<sha12>.json 으로 저장. 실행 기록은 runs.jsonl(키·URL 없음).
종료 코드: 0 정상(변경 없음 포함) / 1 실패 있음 / 2 키 없음.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("fetch_law", os.path.join(HERE, "fetch-law.py"))
fl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fl)

HOME = os.path.expanduser("~")
DEFAULT_STORE = os.path.join(HOME, "2nd", ".ua", "laws-text")
DEFAULT_RECORDS = fl.DEFAULT_STORE  # 1단계 보존 레코드


def latest_mst(records_dir, law_id):
    """1단계 보존 레코드 중 가장 최근 파일의 법령일련번호. 없으면 None."""
    d = os.path.join(records_dir, law_id.replace(":", "_"))
    if not os.path.isdir(d):
        return None
    for f in sorted((x for x in os.listdir(d) if x.endswith(".json")), reverse=True):
        try:
            with open(os.path.join(d, f), encoding="utf-8") as fh:
                mst = str(json.load(fh).get("법령일련번호") or "").strip()
        except (OSError, ValueError):
            continue
        if mst:
            return mst
    return None


def stored_path(store_dir, law_id, mst):
    d = os.path.join(store_dir, law_id.replace(":", "_"))
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if f.startswith(f"{mst}-") and f.endswith(".json"):
                return os.path.join(d, f)
    return None


def payload_hash(payload):
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:12]


def validate(payload, name):
    """본문 응답이 요청한 법령의 조문을 담고 있는지. 문제 있으면 사유 문자열, 정상이면 None."""
    body = (payload or {}).get("법령")
    if not isinstance(body, dict):
        return "응답에 '법령' 없음"
    got = (body.get("기본정보") or {}).get("법령명_한글")
    if got != name:
        return f"법령명 불일치({got!r} ≠ {name!r})"
    units = (body.get("조문") or {}).get("조문단위")
    if not units:
        return "조문 없음"
    return None


def save(store_dir, law_id, mst, payload):
    d = os.path.join(store_dir, law_id.replace(":", "_"))
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"{mst}-{payload_hash(payload)}.json")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    os.replace(tmp, path)
    return path


def run(laws, store_dir, records_dir, oc, fetch=None, dry_run=False):
    """반환: dict(new=[], unchanged=[], failed=[(이름, 사유)], skipped=[이름])"""
    fetch = fetch or fl.fetch_service
    res = {"new": [], "unchanged": [], "failed": [], "skipped": []}
    for law in laws:
        name, lid = law["name"], law["id"]
        mst = latest_mst(records_dir, lid)
        if not mst:
            res["skipped"].append(name)  # 1단계가 아직 이 법령을 보존하지 않음
            continue
        if stored_path(store_dir, lid, mst):
            res["unchanged"].append(name)
            continue
        if dry_run:
            res["new"].append(name)
            continue
        try:
            payload = fetch(oc, mst)
        except Exception as e:  # 네트워크·JSON 오류. 키가 담길 수 있는 메시지는 쓰지 않고 형식만 남긴다
            res["failed"].append((name, type(e).__name__))
            continue
        why = validate(payload, name)
        if why:
            res["failed"].append((name, why))
            continue
        save(store_dir, lid, mst, payload)
        res["new"].append(name)
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--laws", default=fl.DEFAULT_LAWS)
    ap.add_argument("--store", default=DEFAULT_STORE)
    ap.add_argument("--records", default=DEFAULT_RECORDS)
    ap.add_argument("--dry-run", action="store_true", help="호출·저장 없이 수집 대상만 표시")
    a = ap.parse_args(argv)
    cfg = json.load(open(a.laws, encoding="utf-8"))
    if cfg.get("confirmed") is not True:
        print("laws.json confirmed≠true — 중단", file=sys.stderr)
        return 1
    oc = "" if a.dry_run else fl.load_oc()
    if not a.dry_run and not oc:
        print("LAW_OC 없음 — 중단", file=sys.stderr)
        fl.log_run(a.store, {"status": "no-key"})
        return 2
    res = run(cfg["laws"], a.store, a.records, oc, dry_run=a.dry_run)
    line = {"new": len(res["new"]), "unchanged": len(res["unchanged"]), "skipped": len(res["skipped"]), "failed": [n for n, _ in res["failed"]]}
    print(f"신규 {res['new']} · 변경없음 {len(res['unchanged'])} · 건너뜀 {res['skipped']} · 실패 {res['failed']}")
    if not a.dry_run:
        fl.log_run(a.store, {"status": "ok" if not res["failed"] else "partial", **line})
    return 1 if res["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
