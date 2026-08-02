"""graph_lib.py — update-graph.sh의 핵심 파싱/분류 로직을 테스트 가능하게 분리.

동작은 update-graph.sh 임베디드 스크립트와 100% 동일하다(순수 추출 리팩터링,
로직 변경 없음). G1(2026-08-02): 섹션 맥락 기반 관계타입 분류 로직도 여기 있다.
"""
from __future__ import annotations

import re

ONTOLOGY_CLASS_MAP = {
    "flight-control": "Technology",
    "comms-protocol": "Technology",
    "hardware": "Technology",
    "gcs-software": "Technology",
    "ai-autonomy": "AIModel",
    "ai-agent": "AIModel",
    "ops-mission": "Mission",
    "regulations": "AbstractProcess",
    "voice-control": "Technology",
    "swarm": "AIModel",
    "datalink": "Technology",
    "drone": "Technology",
    "drone-hw": "Technology",
    "drone-sw": "Technology",
    "drone-ai": "AIModel",
}

EVIDENCE_HEADING_RE = re.compile(r'근거|출처|Evidence|Reference|참고자료|Source', re.IGNORECASE)
RELATED_HEADING_RE = re.compile(r'관련|Related|See Also', re.IGNORECASE)


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm_text = text[4:end]
    fm: dict = {}
    for line in fm_text.splitlines():
        m = re.match(r'^(\w+):\s*(.+)', line.strip())
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith('[') and val.endswith(']'):
                items = [x.strip().strip('"').strip("'") for x in val[1:-1].split(',') if x.strip()]
                fm[key] = items
            else:
                fm[key] = val.strip('"').strip("'")
    return fm


def extract_links(text: str) -> list[str]:
    return re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]', text)


def extract_links_by_section(text: str) -> list[tuple[str, str]]:
    """헤딩 섹션별로 wikilink를 추출하고 관계타입을 부여한다. 문서에 실재하는
    구조적 신호(어느 헤딩 아래 있는가)만 사용 — 의미를 추측해 관계를 지어내지
    않는다."""
    parts = re.split(r'(?m)^(##\s+.+)$', text)
    results: list[tuple[str, str]] = []
    for slug in extract_links(parts[0]):
        results.append((slug.strip(), "wikilink"))
    i = 1
    while i < len(parts):
        heading = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        if EVIDENCE_HEADING_RE.search(heading):
            rel = "evidences"
        elif RELATED_HEADING_RE.search(heading):
            rel = "related"
        else:
            rel = "wikilink"
        for slug in extract_links(body):
            results.append((slug.strip(), rel))
        i += 2
    return results


def ontology_class_for_domain(domain: str) -> str | None:
    return ONTOLOGY_CLASS_MAP.get(domain, None)
