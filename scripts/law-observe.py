#!/usr/bin/env python3
"""law-observe.py — 법령 개정 알림 1단계 관찰 점검(읽기 전용, 네트워크·.env 접근 없음).

설계: drone-wiki-web/docs/dikw-dynamic-ontology-design.md §15. 관찰 기간(7일) 동안 쌓인 자료가 합격 기준을 만족하는지 판정한다.
입력: ~/2nd/.ua/laws/(보존 레코드·runs.jsonl), ~/2nd/.ua/news-feed.json, drone-wiki-web/data/ontology/laws.json
확인 항목
  [1] 실행 기록: 고유 실행일 ≥ 7, 실패·키없음 스킵 0
  [2] 보존 레코드 정확도: 법령명 = laws.json, 날짜 해석, 시행일 ≥ 공포일, 파일명 해시 = 내용 해시(무결성)
  [3] 피드: 법령 항목 제목 형식·법령명 일치·중복 0
  [4] 링크: 법령 이벤트 → 같은 이름의 법령에만 링크, 제조사·제품 링크 0, 목록 밖 법령명 0 (빌더를 임시 출력으로 실행)
  [5] 누출: 보존 파일·실행 기록·피드 항목에 OC= / 법령상세링크 문자열 0
종료 코드: 0 전부 합격(또는 관찰 진행 중 경고만) / 1 불합격 항목 있음
노출률(질문 패널)은 TS 쪽 점검이라 이 스크립트 범위 밖이다.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile

HOME = os.path.expanduser("~")
STORE = os.path.join(HOME, "2nd", ".ua", "laws")
FEED = os.path.join(HOME, "2nd", ".ua", "news-feed.json")
WEB = os.path.join(HOME, "projectm", "drone-wiki-web")
LAWS = os.path.join(WEB, "data", "ontology", "laws.json")
BUILD = os.path.join(WEB, "scripts", "build-events.py")
MIN_DAYS = 7
TITLE_RE = re.compile(r"^\[법령\] (?P<name>.+?) · (?P<kind>.+?) · 시행 \d{4}-\d{2}-\d{2}(?: \(일부 \d{4}-\d{2}-\d{2}(?:, \d{4}-\d{2}-\d{2})* 시행\))?$")  # 부분 시행 병기 허용

spec = importlib.util.spec_from_file_location("fetch_law", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fetch-law.py"))
fl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fl)

rows = []  # (항목, 판정, 근거)


def add(name, verdict, note):
    rows.append((name, verdict, note))


def check_runs():
    path = os.path.join(STORE, "runs.jsonl")
    runs = [json.loads(x) for x in open(path, encoding="utf-8").read().splitlines() if x.strip()] if os.path.exists(path) else []
    days = {r["at"][:10] for r in runs}
    bad = [r for r in runs if r["status"] != "ok"]
    note = f"실행 {len(runs)}회 · 고유 실행일 {len(days)} · 실패/스킵 {len(bad)}"
    if bad:
        add("[1] 실행 기록", "FAIL", note + " · " + "; ".join(f"{r['at'][:16]} {r['status']} {r.get('failed', '')}" for r in bad[:3]))
    elif len(days) < MIN_DAYS:
        add("[1] 실행 기록", "WARN", note + f" · 관찰 진행 중(목표 {MIN_DAYS}일)")
    else:
        add("[1] 실행 기록", "PASS", note)


def check_records(laws):
    by_id = {x["id"]: x["name"] for x in laws}
    n, problems, versions = 0, [], {}
    for law_id, name in by_id.items():
        d = os.path.join(STORE, law_id.replace(":", "_"))
        files = sorted(f for f in os.listdir(d) if f.endswith(".json")) if os.path.isdir(d) else []
        versions[name] = len(files)
        if not files:
            problems.append(f"{name}: 보존 레코드 없음")
        for f in files:
            n += 1
            rec = json.load(open(os.path.join(d, f), encoding="utf-8"))
            pub, eff = fl.iso_day(rec.get("공포일자")), fl.iso_day(rec.get("시행일자"))
            if rec.get("법령명한글") != name:
                problems.append(f"{f}: 법령명 불일치({rec.get('법령명한글')})")
            if not pub or not eff or not rec.get("법령일련번호"):
                problems.append(f"{f}: 날짜·일련번호 해석 불가")
            elif eff < pub:
                problems.append(f"{f}: 시행일({eff}) < 공포일({pub})")
            if not f.endswith(f"-{fl.record_hash(rec)}.json"):
                problems.append(f"{f}: 파일명 해시 ≠ 내용 해시(변조/손상)")
    note = f"레코드 {n}건 · 법령별 버전수 " + ", ".join(f"{k} {v}" for k, v in versions.items())
    add("[2] 보존 레코드 정확도", "FAIL" if problems else "PASS", note + (" · 문제: " + "; ".join(problems[:4]) if problems else ""))


def law_feed_items():
    feed = json.load(open(FEED, encoding="utf-8")) if os.path.exists(FEED) else []
    return [i for i in feed if (i.get("title") or "").startswith(fl.TITLE_PREFIX)]


def check_feed(laws):
    names = {x["name"] for x in laws}
    items = law_feed_items()
    problems = []
    for it in items:
        m = TITLE_RE.match(it["title"])
        if not m:
            problems.append(f"형식 불일치: {it['title'][:40]}")
        elif m["name"] not in names:
            problems.append(f"목록 밖 법령명: {m['name']}")
    for key in ("url", "title"):
        vals = [i[key] for i in items]
        if len(vals) != len(set(vals)):
            problems.append(f"{key} 중복")
    add("[3] 피드", "FAIL" if problems else "PASS", f"법령 항목 {len(items)}건" + (" · 문제: " + "; ".join(problems[:4]) if problems else ""))


def check_links(laws):
    names = {x["id"]: x["name"] for x in laws}
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "events.json")
        r = subprocess.run([sys.executable, "-I", BUILD, "--feed", FEED, "--out", out, "--laws", LAWS], capture_output=True, text=True)
        if r.returncode != 0:
            add("[4] 링크", "FAIL", "빌더 실패: " + r.stderr.strip()[:120])
            return
        ev = json.load(open(out, encoding="utf-8"))
    law_events = [e for e in ev["events"] if e["title"].startswith(fl.TITLE_PREFIX)]
    problems = []
    for e in law_events:
        links = [l for l in ev["links"] if l["event"] == e["id"]]
        name = TITLE_RE.match(e["title"])["name"] if TITLE_RE.match(e["title"]) else None
        law_links = [l for l in links if l["nodeType"] == "Law"]
        if len(law_links) != 1 or names.get(law_links[0]["node"]) != name:
            problems.append(f"링크 오류/누락: {e['title'][:40]}")
        if any(l["nodeType"] != "Law" for l in links):
            problems.append(f"제조사·제품 링크 혼입: {e['title'][:40]}")
    add("[4] 링크", "FAIL" if problems else "PASS", f"법령 이벤트 {len(law_events)}건(365일 창 안) · Law 링크 {sum(1 for l in ev['links'] if l['nodeType'] == 'Law')}건" + (" · 문제: " + "; ".join(problems[:4]) if problems else ""))


def check_leaks():
    hits = []
    for root, _, files in os.walk(STORE):
        for f in files:
            text = open(os.path.join(root, f), encoding="utf-8", errors="replace").read()
            if re.search(r"OC=|법령상세링크|lawService", text):
                hits.append(os.path.join(os.path.basename(root), f))
    for it in law_feed_items():
        if re.search(r"OC=|lawService", json.dumps(it, ensure_ascii=False)):
            hits.append("feed:" + it["title"][:30])
    add("[5] 누출", "FAIL" if hits else "PASS", "누출 " + (", ".join(hits[:4]) if hits else "0건"))


def main():
    try:
        cfg = json.load(open(LAWS, encoding="utf-8"))
    except (OSError, ValueError) as e:
        sys.exit(f"laws.json 을 읽을 수 없음: {type(e).__name__}")
    laws = cfg["laws"]
    if cfg.get("confirmed") is not True:
        add("[0] 목록 확정", "WARN", "laws.json confirmed≠true")
    check_runs(); check_records(laws); check_feed(laws); check_links(laws); check_leaks()
    w = max(len(r[0]) for r in rows)
    for name, verdict, note in rows:
        print(f"{verdict:<5} {name:<{w}}  {note}")
    fails = sum(1 for r in rows if r[1] == "FAIL")
    warns = sum(1 for r in rows if r[1] == "WARN")
    print(f"\n판정: {'불합격' if fails else ('관찰 진행 중' if warns else '합격')} (FAIL {fails}, WARN {warns})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
