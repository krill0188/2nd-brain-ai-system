#!/usr/bin/env python3
"""HW 제조사 / SW 레지스트리(수집 폴더) → 위키 canonical 이관.

- 원본을 inbox/processed/ 에 그대로 복사(증거, 내용 불변)한다.
- concepts/ 에 카테고리별 canonical 문서 + 상위 개요 문서를 만든다.
  표 행은 원문 그대로 두고, 행마다 출처 표식 ^[inbox/processed/...] 만 덧붙인다. 값을 만들거나 고치지 않는다.
사용: python3 scripts/import-registry.py <수집일 폴더> [--apply]   (기본은 dry-run)
"""
import re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1]).expanduser()
APPLY = "--apply" in sys.argv
STAMP = "20261017"
TODAY = "2026-10-17"

VENDOR = {
    "frame": "프레임·완기체", "battery": "배터리", "fc": "비행제어기", "propeller": "프로펠러", "esc": "ESC", "motor": "모터",
    "camera": "카메라·짐벌", "lidar": "LiDAR", "radar": "레이더", "gnss-imu": "GNSS·IMU·센서", "datalink": "데이터링크·통신 라디오",
    "compute": "컴패니언·엣지 컴퓨터", "power-charger": "전원·충전기·BMS", "payload-mech": "투하·윈치·낙하산", "gcs-hw": "지상국 HW",
}
SOFT = {
    "flight-stack": "비행 스택", "gcs": "GCS", "middleware": "ROS·미들웨어", "navigation-slam": "항법·SLAM", "perception-ai": "인식·엣지 AI",
    "planning-control": "계획·제어", "swarm-multiagent": "군집·멀티에이전트", "simulation": "시뮬레이션", "comms-protocol-sw": "통신 프로토콜 SW",
    "video-streaming": "영상 스트리밍", "fleet-utm": "플릿·UTM", "security-ops": "보안·운영",
}
# 기존 위키에 실제로 있는 문서에만 연결한다(없으면 제외).
RELATED = {
    "motor": ["drone-motor-product-specs-catalog", "fpv-motor-selection-guide"], "esc": ["drone-esc-product-specs-catalog"],
    "propeller": ["drone-propeller-product-specs-catalog"], "battery": ["drone-battery-cell-pack-specs-catalog", "drone-power-battery"],
    "frame": ["drone-frame-platform-specs-catalog"], "datalink": ["drone-payload-datalink-product-specs-catalog", "datalink-communication"],
    "payload-mech": ["drone-payload-systems", "drone-payload-datalink-product-specs-catalog"], "power-charger": ["drone-power-module-specs-catalog", "drone-power-battery"],
    "fc": ["flight-controller-hardware", "fc-vendor-param-guide"], "camera": ["computer-vision-drone"], "compute": ["ros2-drone-integration"],
    "flight-stack": ["px4-flight-stack", "ardupilot"], "gcs": ["ground-control-station"], "middleware": ["ros2-drone-integration", "ros2-advanced"],
    "navigation-slam": ["visual-positioning-odometry"], "perception-ai": ["computer-vision-drone"], "simulation": ["drone-simulation"],
    "comms-protocol-sw": ["mavlink", "dronecan-protocol"], "swarm-multiagent": ["swarm-coordination"], "security-ops": ["mavlink2-security"],
    "fleet-utm": ["drone-regulations"],
}


def exists(slug: str) -> bool:
    return any((ROOT / d / f"{slug}.md").exists() for d in ("concepts", "entities", "comparisons", "queries"))


def split_fm(text: str):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    return m.group(1), m.group(2)


def rows(body: str) -> int:
    return len([l for l in body.splitlines() if l.startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", l)]) - 1


def with_marker(body: str, src: str) -> str:
    out = []
    for l in body.splitlines():
        if l.startswith("|") and l.rstrip().endswith("|") and not re.match(r"^\|[\s\-:|]+\|$", l) and "제조사 |" not in l[:12] and not l.startswith("| 이름 |"):
            l = l.rstrip()[:-1].rstrip() + f" ^[{src}] |"
        out.append(l)
    return "\n".join(out)


def build(kind: str, cat: str, label: str, srcfile: Path, evidence: str):
    fm, body = split_fm(srcfile.read_text(encoding="utf-8"))
    body = re.sub(r"^# .*\n", "", body, count=1).strip("\n")
    n = rows(body)
    rel = [s for s in RELATED.get(cat, []) if exists(s)]
    is_v = kind == "vendor"
    title = f"드론 {label} {'제조사' if is_v else 'SW'} 레지스트리"
    slug = f"{'vendor' if is_v else 'software'}-registry-{cat}"
    tags = "[drone, drone-hw, company]" if is_v else "[drone, drone-sw]"
    domain = "vendor-registry" if is_v else "software-ecosystem"
    notes = (
        "- 이 문서는 **누가 만드는가(제조사 목록)** 이며 제품 사양이 아니다. 사양은 제품별 카탈로그/원문 수집이 별도로 필요하다.\n"
        "- 국가/본사 열은 '페이지 명시'로 표기된 것만 공식 페이지 확인이고, '(일반지식)'은 확인되지 않은 값이다.\n"
        "- 공식 사이트가 봇을 차단하거나 응답하지 않은 곳은 '미확인/접근실패'로 남겼다. 수출통제·NDAA 등 도입 제약은 공식 페이지에 명시된 경우만 기재했다.\n"
        if is_v else
        "- 라이선스와 '드론 연동 포인트'는 저장소·공식 페이지에 적힌 문구만 옮긴 값이며, 표본 대조 전이다. 버전·인기도·가격은 의도적으로 생략했다.\n"
        "- ROS 공식 사이트 등 봇 차단 사이트는 GitHub 기준으로만 기재했다. 유지보수 상태가 확인되지 않은 항목은 비고에 표시했다.\n"
        "- 공격 성격의 도구(보안 카테고리)는 방어·승인된 시험 목적의 참고 목록이다.\n"
    )
    other = "drone-software-ecosystem-registry" if is_v else "drone-hw-vendor-registry"
    rel = rel + [other]  # 항상 반대편 레지스트리에 연결(제조사↔SW), lint의 링크 2개 이상 규칙도 충족
    relsec = "\n## 관련 문서\n" + "\n".join(f"- [[{s}]]" for s in rel) + "\n"
    text = f"""---
title: "{title}"
created: {TODAY}
updated: {TODAY}
type: concept
domain: {domain}
tags: {tags}
sources: [{evidence}]
confidence: medium
contested: false
contradictions: []
---

# {title}

{'드론 융합 HW' if is_v else '드론과 융합해 쓰는 SW'}의 {label} 분야 {'제조사' if is_v else '제품·오픈소스'} {n}건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[{'drone-hw-vendor-registry' if is_v else 'drone-software-ecosystem-registry'}]].

{with_marker(body, evidence)}

## 한계
{notes}{relsec}"""
    return slug, title, n, text


def main():
    plans = []
    for kind, mapping, sub in (("vendor", VENDOR, "vendors"), ("software", SOFT, "software")):
        for cat, label in mapping.items():
            fname = f"{'vendors' if kind == 'vendor' else 'software'}-{cat}.md"
            src = SRC / sub / fname
            if not src.exists():
                print("MISSING", src); continue
            ev = f"inbox/processed/hw-registry-{STAMP}-{sub}-{cat}.md"
            plans.append((kind, cat, label, src, ev))
    results = {"vendor": [], "software": []}
    for kind, cat, label, src, ev in plans:
        slug, title, n, text = build(kind, cat, label, src, ev)
        results[kind].append((cat, label, slug, n))
        print(f"{kind:8} {cat:20} rows={n:3} -> concepts/{slug}.md")
        if APPLY:
            (ROOT / "concepts" / f"{slug}.md").write_text(text, encoding="utf-8")
            shutil.copyfile(src, ROOT / ev)
    # INDEX 원본도 증거로 보관
    for sub in ("vendors", "software"):
        idx = SRC / sub / "INDEX.md"
        if idx.exists() and APPLY:
            shutil.copyfile(idx, ROOT / f"inbox/processed/hw-registry-{STAMP}-{sub}-INDEX.md")

    def umbrella(kind, title, slug, intro, other):
        cats = results[kind]
        total = sum(n for *_, n in cats)
        tbl = "\n".join(f"| {label} | [[{s}]] | {n} |" for _, label, s, n in cats)
        ev = f"inbox/processed/hw-registry-{STAMP}-{'vendors' if kind == 'vendor' else 'software'}-INDEX.md"
        text = f"""---
title: "{title}"
created: {TODAY}
updated: {TODAY}
type: concept
domain: {'vendor-registry' if kind == 'vendor' else 'software-ecosystem'}
tags: {'[drone, drone-hw, company]' if kind == 'vendor' else '[drone, drone-sw]'}
sources: [{ev}]
confidence: medium
contested: false
contradictions: []
---

# {title}

{intro}

| 분야 | 레지스트리 | 항목 수 |
|---|---|---|
{tbl}
| **합계** | {len(cats)}개 분야 | **{total}** |

## 쓰는 법
- 설계 질의에서 후보 부품/도구가 필요하면 분야별 문서에서 제조사·제품군을 찾고, 사양은 제품별 카탈로그나 공식 페이지 원문으로 확인한다.
- 정보 빈틈(예: 모터 최대추력 미확인)이 드러나면 이 레지스트리에서 수집 우선순위를 뽑아 제품별 사양 수집으로 이어간다.
- 연관 레지스트리: [[{other}]]

## 한계
- 공식 사이트가 봇을 차단하거나 응답하지 않은 곳은 '미확인/접근실패'로 남겼다(상세는 각 분야 문서의 표 참조).
- 국가/본사·라이선스·연동 포인트는 값마다 확인 수준이 달라, 확인되지 않은 칸은 비워 두거나 표시했다.
- 수집 시점(2026-10-17) 기준이며 제품 라인업·정책은 바뀔 수 있다.
"""
        return slug, text

    u1 = umbrella("vendor", "드론 HW 제조사 레지스트리", "drone-hw-vendor-registry",
                  "드론에 융합되는 HW 15개 분야(프레임·배터리·비행제어기·프로펠러·ESC·모터·카메라·LiDAR·레이더·GNSS/IMU·데이터링크·컴퓨트·전원·투하·지상국)의 제조사 목록. 한국·유럽·미국·중국·일본 제조사와 방산/산업/취미 구분을 담았다.",
                  "drone-software-ecosystem-registry")
    u2 = umbrella("software", "드론 융합 SW 레지스트리", "drone-software-ecosystem-registry",
                  "드론과 융합해 쓰는 SW 12개 분야(비행 스택·GCS·미들웨어·SLAM·인식 AI·계획/제어·군집·시뮬레이션·통신 프로토콜·영상·플릿/UTM·보안/운영)의 제품·오픈소스 목록.",
                  "drone-hw-vendor-registry")
    for slug, text in (u1, u2):
        print("umbrella ->", f"concepts/{slug}.md")
        if APPLY:
            (ROOT / "concepts" / f"{slug}.md").write_text(text, encoding="utf-8")
    print("APPLIED" if APPLY else "DRY-RUN (use --apply)")


main()
