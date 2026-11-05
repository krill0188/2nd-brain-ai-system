#!/usr/bin/env python3
"""fetch-law-kskill.py — k-skill 프록시로 법제처 자치법규·행정규칙·법령해석례 수집(보조 수집기).

역할 분담(2026-11-06 정비):
  · 현행법령·시행일 법령 = 공식 수집기 fetch-law.py(법제처 직접 호출, 원문 대조·개정 감지의 기준). 이 스크립트는 법령 본문을 만들지 않는다.
  · 이 스크립트 = 공식 수집기에 없는 종류(드론 관련 자치법규 조례·행정규칙·법령해석례)를 inbox/ 로 가져오는 보조 경로.
  · 판례(prec)는 제외: 검색 결과 대부분이 국세법령정보시스템 출처라 프록시 상세 조회가 "일치하는 판례 없음"을 돌려준다(2026-11-06 실측).
무결성: k-skill 프록시(k-skill-proxy.nomadamas.org)는 제3자 중계라 산출물은 항상 verified: false 로 표시한다. TLS 인증서는 검증한다.
        검색 결과의 법령상세링크에는 프록시 운영자의 OC 키가 들어 있으므로 어떤 파일에도 저장하지 않는다. 본문이 비어 있으면 파일을 만들지 않는다.

사용: python3 scripts/fetch-law-kskill.py [--dry-run] [--max-items N] [--target ordin|admrul|expc] [--inbox DIR]
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROXY_BASE = os.environ.get("KSKILL_PROXY_BASE_URL", "https://k-skill-proxy.nomadamas.org")
SEARCH_ENDPOINT = f"{PROXY_BASE}/v1/korean-law/search"
DETAIL_ENDPOINT = f"{PROXY_BASE}/v1/korean-law/detail"
USER_AGENT = "2ndBrainFetcher/3.0"

# target → (표시 이름, 검색 응답 최상위 키, 목록 키, 제목 키, 상세 ID 키, 문서 type)
TARGETS = {
    "ordin": ("자치법규", "OrdinSearch", "law", "자치법규명", "자치법규ID", "ordinance"),
    "admrul": ("행정규칙", "AdmRulSearch", "admrul", "행정규칙명", "행정규칙일련번호", "regulation"),
    "expc": ("법령해석례", "Expc", "expc", "안건명", "법령해석례일련번호", "interpretation"),
}
QUERIES = ["드론", "무인비행장치", "초경량비행장치", "무인항공기", "비행승인"]
# 검색은 본문 전체를 뒤져 무관한 항목이 많이 섞인다(예: '드론' → 하이브리드 자동차 보조금) → 제목에 드론·항공 낱말이 있는 것만 받는다.
RELEVANT = re.compile(r"드론|무인(?:비행|항공|기|멀티)|초경량|비행장치|항공안전|항공사업|도심항공|UAM|UAV|비행금지|비행승인|항공기|항공대")
EXCLUDE = re.compile(r"항공보안|항공운송|항공권|항공료")  # 이름만 비슷한 무관 법령
MIN_BODY = 30          # 본문이 이보다 짧으면 저장하지 않는다
MAX_BODY = 6000        # 본문 상한(초과 시 잘렸음을 문서에 명시)
DEFAULT_MAX_ITEMS = 5  # 대상 종류별 한 번에 새로 저장할 최대 건수


def _get(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # 기본 SSL 컨텍스트: 인증서·호스트명 검증 유지
        return json.loads(r.read())


def kskill_search(target: str, query: str, display: int = 10) -> list:
    _, top, key, *_ = TARGETS[target]
    data = _get(f"{SEARCH_ENDPOINT}?{urllib.parse.urlencode({'target': target, 'query': query, 'display': display})}")
    items = (data.get(top) or {}).get(key) or []
    return items if isinstance(items, list) else [items]  # 결과가 1건이면 목록이 아니라 딕셔너리로 온다


def kskill_detail(target: str, ident: str) -> dict:
    return _get(f"{DETAIL_ENDPOINT}?{urllib.parse.urlencode({'target': target, 'ID': ident})}")


def _as_list(x):
    return x if isinstance(x, list) else ([] if x in (None, "") else [x])


def _text(x) -> str:
    if isinstance(x, str):
        return x
    if isinstance(x, list):
        return "\n".join(t for t in (_text(i) for i in x) if t)
    if isinstance(x, dict):
        return "\n".join(t for t in (_text(v) for v in x.values()) if t)
    return ""


def relevant(title: str) -> bool:
    return bool(RELEVANT.search(title or "")) and not EXCLUDE.search(title or "")


def extract(target: str, detail: dict) -> tuple[str, str]:
    """상세 응답 → (본문 텍스트, 시행·해석일자 8자리). 본문을 못 찾으면 ('', '')."""
    if target == "ordin":
        d = detail.get("LawService") or {}
        info = d.get("자치법규기본정보") or {}
        lines = [_text(j.get("조내용")).strip() for j in _as_list((d.get("조문") or {}).get("조")) if isinstance(j, dict)]
        add = _text((d.get("부칙") or {}).get("부칙내용")).strip()
        return "\n".join([*(l for l in lines if l), *([add] if add else [])]), str(info.get("시행일자") or "")
    if target == "admrul":
        d = detail.get("AdmRulService") or {}
        info = d.get("행정규칙기본정보") or {}
        return _text(d.get("조문내용")).strip(), str(info.get("시행일자") or "")
    if target == "expc":
        d = detail.get("ExpcService") or {}
        parts = [(h, _text(d.get(h)).strip()) for h in ("질의요지", "회답", "이유")]
        return "\n\n".join(f"### {h}\n{t}" for h, t in parts if t), str(d.get("해석일자") or "")
    return "", ""


def yq(s: str) -> str:
    """YAML 큰따옴표 문자열(한글 그대로, \\uXXXX 이스케이프 없음)."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def build_doc(target: str, title: str, ident: str, body: str, eff: str, today: str) -> str:
    label, *_rest = TARGETS[target]
    doc_type = TARGETS[target][5]
    cut = len(body) > MAX_BODY
    body = body[:MAX_BODY].rstrip() + ("\n\n(이하 생략 — 분량 상한으로 잘림, 전문은 법제처에서 확인)" if cut else "")
    eff_iso = f"{eff[:4]}-{eff[4:6]}-{eff[6:8]}" if re.fullmatch(r"\d{8}", eff or "") else ""
    return f"""---
title: {yq(title)}
created: {today}
captured: {today}
type: {doc_type}
domain: regulations
source: https://www.law.go.kr
via: k-skill-proxy.nomadamas.org
verified: false
target: {target}
law_id: {yq(ident)}
{f"effective: {eff_iso}" + chr(10) if eff_iso else ""}tags: [drone, law, {label}]
---

# {title}

> 법제처 국가법령정보를 k-skill 프록시(제3자 중계)로 가져온 **미검증 사본**입니다. 원문 대조 전이므로 사실 근거로 쓰기 전에 법제처 원문을 확인하세요.

**종류**: {label} · **식별자**: {ident}{f" · **시행·해석일**: {eff_iso}" if eff_iso else ""}

## 내용

{body}
"""


def seen(inbox: Path, processed: Path, target: str, key: str) -> bool:
    pat = f"fetch-*-law-{target}-{key}.md"
    return any(True for d in (inbox, processed) if d.exists() for _ in d.glob(pat))


def run(targets, inbox: Path, processed: Path, today: str, max_items: int, dry_run: bool = False, search=kskill_search, detail=kskill_detail, sleep=time.sleep) -> dict:
    stat = {"written": 0, "skipped_empty": 0, "skipped_seen": 0, "errors": 0, "calls": 0}
    for target in targets:
        label, top, key, title_key, id_key, _ = TARGETS[target]
        cands: dict[str, dict] = {}
        for q in QUERIES:
            try:
                stat["calls"] += 1
                items = search(target, q)
            except Exception as e:  # 네트워크·JSON 오류 — 메시지에 URL 이 들어갈 수 있어 형식만 남긴다
                stat["errors"] += 1
                print(f"  ⚠️  {label} 검색 실패 '{q}': {type(e).__name__}")
                continue
            for it in items:
                if not isinstance(it, dict):
                    continue
                ident, title = str(it.get(id_key) or ""), str(it.get(title_key) or "")
                if ident and title and relevant(title):
                    cands.setdefault(ident, it)
            sleep(0.3)
        print(f"{label}: 관련 후보 {len(cands)}건")
        wrote = 0
        for ident, it in cands.items():
            if wrote >= max_items:
                break
            title = str(it.get(title_key))
            try:
                stat["calls"] += 1
                body, eff = extract(target, detail(target, ident))
            except Exception as e:
                stat["errors"] += 1
                print(f"  ⚠️  {label} 상세 실패 {ident}: {type(e).__name__}")
                continue
            body = body.strip()
            if len(body) < MIN_BODY:
                stat["skipped_empty"] += 1
                print(f"  ⏭  본문 없음 — 저장 안 함: {title[:40]}")
                continue
            fkey = f"{ident}-{eff}" if eff else ident
            if seen(inbox, processed, target, fkey):
                stat["skipped_seen"] += 1
                continue
            out = inbox / f"fetch-{today}-law-{target}-{fkey}.md"
            if not dry_run:
                inbox.mkdir(parents=True, exist_ok=True)
                out.write_text(build_doc(target, title, ident, body, eff, today), encoding="utf-8")
            stat["written"] += 1
            wrote += 1
            print(f"  ✅ {label} '{title[:40]}' ({len(body)}자){' [dry-run]' if dry_run else ' → inbox/'}")
            sleep(0.3)
    return stat


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true", help="저장 없이 수집 대상만 표시")
    ap.add_argument("--max-items", type=int, default=DEFAULT_MAX_ITEMS, help="종류별 새로 저장할 최대 건수")
    ap.add_argument("--target", choices=sorted(TARGETS), help="특정 종류만")
    ap.add_argument("--inbox", default=str(ROOT / "inbox"), help="저장 폴더(검증용으로 바꿀 수 있음)")
    a = ap.parse_args(argv)
    inbox = Path(a.inbox)
    stat = run([a.target] if a.target else list(TARGETS), inbox, inbox / "processed", date.today().isoformat(), a.max_items, a.dry_run)
    print(f"\n신규 {stat['written']}건 · 본문 없어 제외 {stat['skipped_empty']} · 이미 수집 {stat['skipped_seen']} · 오류 {stat['errors']}/{stat['calls']}회")
    return 1 if stat["calls"] and stat["errors"] == stat["calls"] else 0  # 모든 호출이 실패했을 때만 실패


if __name__ == "__main__":
    sys.exit(main())
