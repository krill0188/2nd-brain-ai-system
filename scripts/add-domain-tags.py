#!/usr/bin/env python3
"""
기존 concepts/entities 마크다운 파일에 domain 필드를 일괄 추가합니다.
이미 domain 필드가 있는 파일은 건너뜁니다.

사용법:
  python3 scripts/add-domain-tags.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent

DRONE_DOMAINS = {
    "flight-control", "comms-protocol", "hardware",
    "gcs-software", "ops-mission", "regulations", "ai-autonomy",
}

# 키워드 → 도메인 매핑 (순서 중요 — 먼저 매칭된 것 사용)
DOMAIN_RULES: list[tuple[str, list[str]]] = [
    ("comms-protocol", ["mavlink", "dronecan", "uavcan", "rf", "datalink",
                        "통신", "protocol", "telemetry", "xbee", "sik",
                        "radio", "link", "communication"]),
    ("flight-control", ["px4", "ardupilot", "flight controller", "비행제어",
                        "autopilot", "flight stack", "ekf", "pid",
                        "attitude", "stabilization", "firmw"]),
    ("hardware",       ["pixhawk", "fc board", "gps", "battery", "배터리",
                        "센서", "hardware", "imu", "esc", "motor",
                        "propeller", "lidar", "camera", "payload",
                        "power", "weight", "frame"]),
    ("gcs-software",   ["qgroundcontrol", "mission planner", "ros", "gcs",
                        "소프트웨어", "simulation", "gazebo", "sitl",
                        "software", "sdk", "api", "logging"]),
    ("ai-autonomy",    ["slam", "ai", "autonomous", "자율", "군집",
                        "swarm", "opencv", "detection", "vision",
                        "machine learning", "neural", "inference",
                        "knowledge", "llm", "agent", "workflow"]),
    ("ops-mission",    ["waypoint", "mission", "bvlos", "rtl", "임무",
                        "운용", "payload", "failsafe", "safety",
                        "operation", "survey", "delivery", "inspection"]),
    ("regulations",    ["법규", "regulation", "easa", "항공", "승인",
                        "안전", "safety rule", "faa", "법", "규정",
                        "인증", "허가", "국토"]),
]

# 파일명 → 도메인 직접 매핑
SLUG_MAP: dict[str, str] = {
    # comms-protocol
    "advanced-mavlink": "comms-protocol",
    "mavlink-advanced": "comms-protocol",
    "mavlink-advanced-features": "comms-protocol",
    "mavlink-protocol": "comms-protocol",
    "mavlink-protocol-deep": "comms-protocol",
    "mavlink2-security": "comms-protocol",
    "mavsdk": "comms-protocol",
    "dronecan-protocol": "comms-protocol",
    "dronecan-deep": "comms-protocol",
    "datalink-communication": "comms-protocol",
    "mavlink": "comms-protocol",

    # flight-control
    "ardupilot-architecture": "flight-control",
    "ardupilot": "flight-control",
    "px4-flight-stack": "flight-control",
    "px4-architecture-deep": "flight-control",
    "px4-system-architecture": "flight-control",
    "px4-flight-modes": "flight-control",
    "px4-offboard-control": "flight-control",
    "px4-pid-tuning": "flight-control",
    "px4-tuning-control": "flight-control",
    "px4-control-tuning": "flight-control",
    "pid-tuning-control": "flight-control",
    "flight-logging-analysis": "flight-control",
    "drone-safety-failsafe": "flight-control",
    "drone-simulation": "flight-control",

    # hardware
    "pixhawk": "hardware",
    "flight-controller-hardware": "hardware",
    "drone-power-battery": "hardware",
    "drone-payload-systems": "hardware",
    "sensor-calibration": "hardware",
    "rtk-gps-precise-landing": "hardware",
    "visual-positioning-odometry": "hardware",

    # gcs-software
    "ground-control-station": "gcs-software",
    "ros2-drone-deep": "gcs-software",
    "ros2-drone-integration": "gcs-software",
    "ros2-advanced": "gcs-software",
    "ros2-advanced-integration": "gcs-software",
    "px4-cicd-pipeline": "gcs-software",

    # ops-mission
    "mission-planning": "ops-mission",
    "recon-swarm-project": "ops-mission",

    # regulations
    "drone-regulations": "regulations",

    # ai-autonomy
    "ai-knowledge-workflow": "ai-autonomy",
    "ai-personal-knowledge-management": "ai-autonomy",
    "drone-ai-agents": "ai-autonomy",
    "computer-vision-drone": "ai-autonomy",
    "llm-wiki": "ai-autonomy",
    "swarm-coordination": "ai-autonomy",
    "swarm-modes": "ai-autonomy",
    "voice-control-drone": "ai-autonomy",
    "research-feedback-loop": "ai-autonomy",
    "second-brain-research-workflow": "ai-autonomy",
}


def infer_domain(slug: str, title: str, tags: list[str], content: str) -> str:
    if slug in SLUG_MAP:
        return SLUG_MAP[slug]

    text = (slug + " " + title + " " + " ".join(tags) + " " + content[:800]).lower()
    for domain, keywords in DOMAIN_RULES:
        if any(kw in text for kw in keywords):
            return domain
    return "flight-control"


def extract_frontmatter_end(lines: list[str]) -> int:
    """두 번째 '---' 줄 인덱스 반환"""
    if not lines or lines[0].strip() != "---":
        return -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return i
    return -1


def parse_tags(lines: list[str], fm_end: int) -> list[str]:
    for line in lines[1:fm_end]:
        if line.startswith("tags:"):
            raw = line[5:].strip()
            if raw.startswith("[") and raw.endswith("]"):
                inner = raw[1:-1]
                return [t.strip().strip('"').strip("'") for t in inner.split(",") if t.strip()]
    return []


def get_title(lines: list[str], fm_end: int, slug: str) -> str:
    for line in lines[1:fm_end]:
        if line.startswith("title:"):
            return line[6:].strip().strip('"').strip("'")
    return slug.replace("-", " ")


def process_file(path: Path, dry_run: bool) -> str | None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    fm_end = extract_frontmatter_end(lines)
    if fm_end == -1:
        return None

    # 이미 domain 있으면 스킵
    for line in lines[1:fm_end]:
        if line.startswith("domain:"):
            return None

    slug = path.stem
    tags = parse_tags(lines, fm_end)
    title = get_title(lines, fm_end, slug)
    body = "\n".join(lines[fm_end + 1:])

    domain = infer_domain(slug, title, tags, body)

    # confidence: 줄 뒤에 domain: 삽입 (없으면 마지막 frontmatter 항목 앞)
    insert_after = None
    for i, line in enumerate(lines[1:fm_end], 1):
        if line.startswith("confidence:"):
            insert_after = i
            break

    if insert_after is None:
        insert_after = fm_end - 1

    new_lines = lines[: insert_after + 1] + [f"domain: {domain}"] + lines[insert_after + 1 :]
    new_text = "\n".join(new_lines)
    if text.endswith("\n"):
        new_text += "\n"

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return domain


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="실제 수정 없이 결과만 출력")
    args = parser.parse_args()

    dirs = [WIKI_ROOT / "concepts", WIKI_ROOT / "entities"]
    results: dict[str, list[str]] = {d: [] for d in DRONE_DOMAINS}
    skipped = 0
    modified = 0

    for d in dirs:
        if not d.exists():
            continue
        for md in sorted(d.glob("*.md")):
            domain = process_file(md, args.dry_run)
            if domain is None:
                skipped += 1
            else:
                results[domain].append(md.name)
                modified += 1

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}domain 태그 추가 완료")
    print(f"  수정: {modified}개 | 스킵(이미 있음): {skipped}개\n")
    for domain, files in sorted(results.items()):
        if files:
            print(f"  [{domain}] {len(files)}개")
            for f in files:
                print(f"    - {f}")


if __name__ == "__main__":
    main()
