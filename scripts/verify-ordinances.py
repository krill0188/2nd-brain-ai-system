#!/usr/bin/env python3
"""verify-ordinances.py — 자치법규(조례) 요약을 법제처 공식 API 원문과 대조하는 읽기 전용 점검기(2026-11-07).

k-skill 프록시(제3자 중계)로 받은 inbox 사본이 위키 개념 문서에 요약돼 공개됐을 때, 공식 원문의 명칭·시행일·조문 제목·핵심 낱말이 맞는지 확인한다.
인증키(LAW_OC)는 fetch-law.py 의 load_oc() 로만 읽고 출력·기록하지 않는다. 어떤 파일도 쓰지 않는다.
사용: python3 scripts/verify-ordinances.py ID [ID...]   (ID = 법제처 자치법규ID, inbox 파일명 fetch-…-law-ordin-<ID>-<시행일>.md)
"""
import importlib.util
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load_fetch_law():
    spec = importlib.util.spec_from_file_location("fetch_law", HERE / "fetch-law.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fetch(oc, ident):
    qs = urllib.parse.urlencode({"OC": oc, "target": "ordin", "ID": ident, "type": "JSON"})
    req = urllib.request.Request("https://www.law.go.kr/DRF/lawService.do?" + qs, headers={"User-Agent": "2ndBrainVerify/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:  # 인증서 검증 유지
        return json.loads(r.read())


def flat(x):
    if isinstance(x, str):
        return x
    if isinstance(x, list):
        return "\n".join(flat(i) for i in x)
    if isinstance(x, dict):
        return "\n".join(flat(v) for v in x.values())
    return ""


def summarize(data):
    d = data.get("LawService") or {}
    info = d.get("자치법규기본정보") or {}
    arts = (d.get("조문") or {}).get("조") or []
    arts = arts if isinstance(arts, list) else [arts]
    rows = []
    for a in arts:
        if not isinstance(a, dict):
            continue
        rows.append((str(a.get("조문번호") or "").strip(), flat(a.get("조제목")).strip(), flat(a.get("조내용")).strip()))
    return info, rows


def main(argv):
    if not argv:
        print(__doc__)
        return 64
    oc = load_fetch_law().load_oc()
    if not oc:
        print("LAW_OC 없음 — 중단", file=sys.stderr)
        return 2
    for ident in argv:
        try:
            info, rows = summarize(fetch(oc, ident))
        except Exception as exc:  # 메시지에 URL(키 포함)이 들어갈 수 있어 형식만 남긴다
            print(f"[{ident}] 조회 실패: {type(exc).__name__}")
            continue
        print(f"\n[{ident}] {info.get('자치법규명')} | 공포 {info.get('공포일자')} | 시행 {info.get('시행일자')} | {info.get('지자체기관명')} | 조문 {len(rows)}개")
        for num, title, body in rows:
            one = re.sub(r"\s+", " ", body)[:90]
            print(f"  제{num}조 {title}: {one}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
