#!/usr/bin/env python3
"""param-diff.py — 펌웨어 버전 간 공식 파라미터 diff → 위키 페이지 자동 생성

소스 (공식):
  PX4      : 릴리즈 펌웨어(px4_fmu-v6x_default.px4) 내장 parameter_xml
  ArduPilot: ardupilot.org 버전별 파라미터 문서 HTML (stable-Vx.y.z)

사용:
  python3 param-diff.py px4 v1.16.0 v1.17.0
  python3 param-diff.py copter 4.6.0 4.7.0
  python3 param-diff.py --auto        # 신규 릴리즈 감지 시 자동 diff (fetch 체인용)
"""
import base64
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
import zlib
from datetime import date

WIKI = os.path.expanduser("~/2nd")
CACHE = os.path.join(WIKI, ".ua", "param-cache")
STATE = os.path.join(WIKI, ".ua", "param-versions.json")
TODAY = date.today().isoformat()
UA = {"User-Agent": "2ndBrainParamDiff/1.0"}

os.makedirs(CACHE, exist_ok=True)


def fetch(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return dest
    req = urllib.request.Request(url, headers=UA)
    data = urllib.request.urlopen(req, timeout=120).read()
    with open(dest, "wb") as f:
        f.write(data)
    return dest


# ── PX4: .px4 컨테이너에서 parameter_xml 추출 ──────────────────
def px4_params(tag: str) -> dict:
    url = f"https://github.com/PX4/PX4-Autopilot/releases/download/{tag}/px4_fmu-v6x_default.px4"
    path = fetch(url, os.path.join(CACHE, f"px4-{tag}.px4"))
    d = json.load(open(path))
    xml = zlib.decompress(base64.b64decode(d["parameter_xml"]))
    root = ET.fromstring(xml)
    params = {}
    for grp in root.iter("group"):
        gname = grp.get("name", "기타")
        for p in grp.iter("parameter"):
            name = p.get("name")
            if not name:
                continue
            params[name] = {
                "default": p.get("default", ""),
                "group": gname,
                "desc": (p.findtext("short_desc") or "").strip()[:80],
            }
    return params


# ── ArduPilot: 버전별 문서 HTML에서 파라미터명 추출 ─────────────
def ap_params(vehicle: str, ver: str) -> dict:
    veh = {"copter": "Copter", "plane": "Plane", "rover": "Rover"}[vehicle]
    url = f"https://ardupilot.org/{vehicle}/docs/parameters-{veh}-stable-V{ver}.html"
    path = fetch(url, os.path.join(CACHE, f"{vehicle}-{ver}.html"))
    html = open(path, encoding="utf-8", errors="ignore").read()
    params = {}
    # sphinx 헤딩: <hN>PARAM_NAME: 설명<a ...></hN>
    for m in re.finditer(r"<h[23][^>]*>([A-Z][A-Z0-9_]{2,24}):\s*([^<]{0,80})", html):
        name, desc = m.group(1), m.group(2).strip()
        params[name] = {"default": "", "group": name.split("_")[0], "desc": desc}
    return params


def build_page(fw_label: str, slug_fw: str, v1: str, v2: str,
               old: dict, new: dict, has_defaults: bool) -> str:
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = []
    if has_defaults:
        for n in sorted(set(new) & set(old)):
            if old[n]["default"] != new[n]["default"]:
                changed.append((n, old[n]["default"], new[n]["default"]))

    def group_block(names, src):
        by_grp = {}
        for n in names:
            by_grp.setdefault(src[n]["group"], []).append(n)
        lines = []
        for g in sorted(by_grp):
            lines.append(f"**{g}** ({len(by_grp[g])}): " + ", ".join(f"`{n}`" for n in by_grp[g]))
        return "\n\n".join(lines) or "_없음_"

    body = [
        "---",
        f'title: "{fw_label} {v1} → {v2} 파라미터 변경 전체 목록"',
        f"created: {TODAY}",
        f"updated: {TODAY}",
        "type: concept",
        f"tags: [drone, flight-control, parameter, diff, {slug_fw}]",
        f"sources: [공식 파라미터 메타데이터 자동 diff]",
        "confidence: high",
        "contested: false",
        "contradictions: []",
        "domain: flight-control",
        "---",
        "",
        f"# {fw_label} {v1} → {v2} 파라미터 변경 전체 목록",
        "",
        f"> 공식 메타데이터 자동 비교 (생성일 {TODAY}). 개요 해설은 "
        f"[[{'px4-params-by-version' if slug_fw == 'px4' else 'ardupilot-params-by-version'}]] 참조.",
        "",
        "## 요약",
        "",
        f"| 구분 | 개수 |",
        f"|---|---|",
        f"| {v1} 총 파라미터 | {len(old)} |",
        f"| {v2} 총 파라미터 | {len(new)} |",
        f"| ➕ 신규 | {len(added)} |",
        f"| ➖ 삭제 | {len(removed)} |",
    ]
    if has_defaults:
        body.append(f"| 🔧 기본값 변경 | {len(changed)} |")
    body += ["", f"## ➕ 신규 파라미터 ({len(added)})", "", group_block(added, new),
             "", f"## ➖ 삭제된 파라미터 ({len(removed)})", "", group_block(removed, old), ""]
    if has_defaults and changed:
        body += [f"## 🔧 기본값 변경 ({len(changed)})", "", "| 파라미터 | 이전 | 변경 |", "|---|---|---|"]
        body += [f"| `{n}` | {a or '-'} | {b or '-'} |" for n, a, b in changed[:200]]
        if len(changed) > 200:
            body.append(f"\n_...외 {len(changed)-200}건_")
        body.append("")
    body.append("> ⚠️ 업그레이드 후 백업 파라미터 파일과 diff하여 기체 종속값을 재확인할 것.")
    return "\n".join(body)


def generate(fw: str, v1: str, v2: str) -> str:
    if fw == "px4":
        old, new = px4_params(v1), px4_params(v2)
        label, has_def = "PX4", True
    else:
        old, new = ap_params(fw, v1), ap_params(fw, v2)
        label, has_def = f"ArduPilot {fw.capitalize()}", False
    slug = f"param-diff-{fw}-{v1.lstrip('v')}-{v2.lstrip('v')}".replace(".", "-")
    out = os.path.join(WIKI, "concepts", f"{slug}.md")
    with open(out, "w") as f:
        f.write(build_page(label, fw, v1, v2, old, new, has_def))
    print(f"✅ {out} (구:{len(old)} → 신:{len(new)})")
    return slug


def auto():
    """신규 릴리즈 감지 시 직전 버전 대비 diff 자동 생성 (fetch 체인용)."""
    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    targets = [
        ("px4", "PX4/PX4-Autopilot", lambda t: t.startswith("v") and "-" not in t),
        ("copter", "ArduPilot/ardupilot", lambda t: t.startswith("Copter-")),
        ("plane", "ArduPilot/ardupilot", lambda t: t.startswith("Plane-")),
    ]
    for fw, repo, match in targets:
        try:
            req = urllib.request.Request(
                f"https://api.github.com/repos/{repo}/releases?per_page=15", headers=UA)
            rels = json.load(urllib.request.urlopen(req, timeout=20))
            tags = [r["tag_name"] for r in rels if match(r["tag_name"]) and not r.get("prerelease")]
            if not tags:
                continue
            latest = tags[0]
            ver = latest.replace("Copter-", "").replace("Plane-", "")
            prev = state.get(fw)
            if prev and prev != ver:
                try:
                    generate(fw, prev if fw == "px4" else prev, ver if fw == "px4" else ver)
                    print(f"  auto: {fw} {prev} → {ver} diff 생성")
                except Exception as ex:
                    print(f"  auto: {fw} diff 실패 — {ex}", file=sys.stderr)
            state[fw] = ver
        except Exception as ex:
            print(f"  auto: {fw} 릴리즈 확인 실패 — {ex}", file=sys.stderr)
    json.dump(state, open(STATE, "w"))


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--auto":
        auto()
    elif len(sys.argv) == 4:
        generate(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
        sys.exit(1)
