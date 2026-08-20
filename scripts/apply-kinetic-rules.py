#!/usr/bin/env python3
"""apply-kinetic-rules.py — ONTOLOGY_SPEC.md §4 SWRL 규칙 중 실시간 텔레메트리
없이 정적 메타데이터만으로 평가 가능한 2개(규칙4 SLM/LLM 판별, 규칙6 미승인
가설로 Mission 근거 금지)를 실제로 실행하는 Action(Kinetic Layer) 스크립트.

2026-08-20, 마스터의 명시적 지시("팔란티어 온톨로지 방향이 나오는것이 목표")로
착수. 나머지 SWRL 규칙 6개는 실시간 드론 텔레메트리가 전제인데 Swarm OPS GCS가
실기체 미검증·워킹트리 dirty 상태라 지금 연동 부적절 — 스코프에서 명시적으로
제외했다(자세한 판단은 8/20 세션 기록 참고).

패턴 출처: github.com/justinjoy/agent-workflows — "요청을 ABox 트리플로 선언
→ TBox 서브섬션/조건 매칭 추론 → 실제 행동"이라는 실증 패턴을 그대로 이식.
여기서는 rdflib Graph에 canonical 문서/연구 클레임을 ABox 트리플로 넣고
SPARQL로 규칙을 평가한 뒤, 매칭된 대상에 실제 쓰기(frontmatter 필드 갱신,
감사 파일 생성)를 가한다.

주의(build-owl.py와의 관계): build-owl.py는 "위키 문서 ≠ 실세계 인스턴스"
원칙을 지키며 ABox 인스턴스화를 의도적으로 하지 않는다. 이 스크립트는 그
원칙과 다른 전제(마스터의 명시적 지시로 문서를 Link/Action의 대상 인스턴스로
취급)로 동작하는 별도 실험적 산출물이다 — build-owl.py의 설계를 바꾸거나
그 원칙이 틀렸다고 주장하는 게 아니다.

실행:
  source .venv/bin/activate
  python3 scripts/apply-kinetic-rules.py

부작용: entities/*.md frontmatter에 aiModelClass 필드 갱신(규칙4),
concepts/*.md frontmatter에 ontology_status: INVALID 플래그(규칙6 위반 시만),
research/runs/<id>/ontology-audit.json 생성/갱신(규칙6 감사 기록).
위반이 있으면 hermes로 텔레그램 알림.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD

ROOT = Path(__file__).resolve().parent.parent
ENTITIES_DIR = ROOT / "entities"
CONCEPTS_DIR = ROOT / "concepts"
HYPOTHESES_DIR = ROOT / "research" / "hypotheses"
RUNS_DIR = ROOT / "research" / "runs"

DR = Namespace("https://2nd-brain.local/ontology#")

SLM_PARAM_THRESHOLD = 3_000_000_000  # ONTOLOGY_SPEC.md §4 규칙4 예시 임계값


# ── frontmatter 유틸(graph_lib.py의 정규식 파서와 동일한 관례) ──────────────

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
            fm[key] = val.strip('"').strip("'")
    return fm


def upsert_frontmatter_field(path: Path, key: str, value: str) -> bool:
    """frontmatter에 key: value를 추가하거나(없으면) 갱신한다(값이 다르면).
    이미 같은 값이면 파일을 건드리지 않고 False를 반환한다."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    if end == -1:
        return False
    fm_block = text[:end]
    rest = text[end:]

    pattern = re.compile(rf'(?m)^{re.escape(key)}:\s*.*$')
    if pattern.search(fm_block):
        current = pattern.search(fm_block).group(0)
        if current == f"{key}: {value}":
            return False
        new_fm_block = pattern.sub(f"{key}: {value}", fm_block)
    else:
        new_fm_block = fm_block + f"\n{key}: {value}"

    path.write_text(new_fm_block + rest, encoding="utf-8")
    return True


# ── 규칙4 — SLM/LLM 판별 ──────────────────────────────────────────────────

def rule4_slm_llm_classification() -> list[dict]:
    g = Graph()
    changed = []
    entries = []

    for fpath in sorted(ENTITIES_DIR.glob("*.md")):
        fm = parse_frontmatter(fpath.read_text(encoding="utf-8"))
        if not fm.get("deploymentLocation") or not fm.get("parameterCount"):
            continue
        slug = fpath.stem
        uri = DR[slug]
        g.add((uri, RDF.type, DR.AIModel))
        g.add((uri, DR.deploymentLocation, Literal(fm["deploymentLocation"])))
        g.add((uri, DR.parameterCount, Literal(int(fm["parameterCount"]), datatype=XSD.integer)))
        entries.append((slug, fpath))

    if not entries:
        return []

    # ONTOLOGY_SPEC.md §4 규칙4 의사코드를 SPARQL ASK 조건으로 그대로 옮김
    for slug, fpath in entries:
        uri = DR[slug]
        is_slm = g.query(f"""
            PREFIX dr: <{DR}>
            ASK {{
                dr:{slug} dr:deploymentLocation "onboard" .
                dr:{slug} dr:parameterCount ?p .
                FILTER(?p < {SLM_PARAM_THRESHOLD})
            }}
        """).askAnswer
        is_cloud = list(g.objects(uri, DR.deploymentLocation))[0] == Literal("cloud")

        if is_cloud:
            model_class = "LLM"
        elif is_slm:
            model_class = "SLM"
        else:
            # onboard이지만 파라미터가 임계값 이상 — 규칙4가 커버하지 않는
            # 회색지대. 억지로 분류하지 않는다(update-graph.sh와 동일 원칙).
            continue

        if upsert_frontmatter_field(fpath, "aiModelClass", model_class):
            changed.append({"slug": slug, "aiModelClass": model_class})

    return changed


# ── 규칙6 — 미승인 가설로 Mission(canonical 문서) 근거 금지 ─────────────────

def collect_hypothesis_claims() -> dict[str, dict]:
    """research/hypotheses/*.md에서 claim_type: hypothesis인 클레임 ID를 세션별로 수집."""
    by_session: dict[str, dict] = {}
    for fpath in sorted(HYPOTHESES_DIR.glob("*.md")):
        session_id = fpath.stem
        text = fpath.read_text(encoding="utf-8")
        blocks = re.split(r'(?m)^##\s+(\S+)\s*$', text)
        hypothesis_ids = []
        for i in range(1, len(blocks), 2):
            claim_id = blocks[i]
            body = blocks[i + 1] if i + 1 < len(blocks) else ""
            if re.search(r'-\s*claim_type:\s*hypothesis', body):
                hypothesis_ids.append(claim_id)
        if hypothesis_ids:
            by_session[session_id] = {"hypothesis_ids": hypothesis_ids}
    return by_session


def rule6_unapproved_hypothesis_audit() -> dict:
    sessions = collect_hypothesis_claims()
    violations = []
    clean_sessions = []

    for session_id, info in sessions.items():
        state_path = RUNS_DIR / session_id / "state.json"
        promoted = {}
        if state_path.exists():
            state = json.loads(state_path.read_text(encoding="utf-8"))
            promoted = state.get("promoted", {})

        # 규칙6: claimType(hypothesis) ∧ NOT approvedBy(human) → Mission 근거로 못 씀.
        # "Mission 근거로 채택"의 실측 신호는 promote.py가 쓰는 promoted 딕셔너리
        # (승격되어 concepts/<slug>.md가 된 클레임 ID 목록)다.
        session_violations = [cid for cid in info["hypothesis_ids"] if cid in promoted]

        if session_violations:
            for cid in session_violations:
                concept_slug = promoted[cid]
                concept_path = CONCEPTS_DIR / f"{concept_slug}.md"
                if concept_path.exists():
                    upsert_frontmatter_field(
                        concept_path, "ontology_status",
                        f'"INVALID — 규칙6 위반: 미승인 hypothesis 클레임({cid})이 Mission 근거로 승격됨"'
                    )
            violations.append({
                "session_id": session_id,
                "violating_claim_ids": session_violations,
            })
        else:
            clean_sessions.append({
                "session_id": session_id,
                "hypothesis_count": len(info["hypothesis_ids"]),
                "promoted_count": len(promoted),
            })

    audit_result = {
        "rule": "ONTOLOGY_SPEC.md §4 규칙6 — 미승인 가설로 Mission 근거 금지",
        "checked_at": subprocess.run(
            ["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True
        ).stdout.strip(),
        "violations": violations,
        "clean_sessions": clean_sessions,
    }

    for session_id in sessions:
        run_dir = RUNS_DIR / session_id
        if run_dir.exists():
            audit_path = run_dir / "ontology-audit.json"
            audit_path.write_text(json.dumps(audit_result, ensure_ascii=False, indent=2), encoding="utf-8")

    return audit_result


# ── 알림 ──────────────────────────────────────────────────────────────────

def notify_telegram(message: str) -> None:
    try:
        subprocess.run(
            ["hermes", "send", "-t", "telegram", message],
            check=False, capture_output=True, text=True, timeout=30,
        )
    except FileNotFoundError:
        print("⚠ hermes CLI를 찾을 수 없어 텔레그램 알림 생략", file=sys.stderr)


def main() -> None:
    print("🔧 apply-kinetic-rules.py — SWRL 규칙4·6 평가 시작")

    r4_changed = rule4_slm_llm_classification()
    print(f"규칙4(SLM/LLM 판별): {len(r4_changed)}건 분류")
    for c in r4_changed:
        print(f"  - {c['slug']} → {c['aiModelClass']}")

    r6_result = rule6_unapproved_hypothesis_audit()
    n_violations = len(r6_result["violations"])
    n_clean = len(r6_result["clean_sessions"])
    print(f"규칙6(미승인 가설 감사): 세션 {n_clean + n_violations}개 중 위반 {n_violations}건")

    if n_violations > 0:
        lines = [f"⚠️ 온톨로지 규칙6 위반 발견: {n_violations}개 세션에서 미승인 hypothesis가 Mission 근거로 승격됨"]
        for v in r6_result["violations"]:
            lines.append(f"  - {v['session_id']}: {', '.join(v['violating_claim_ids'])}")
        notify_telegram("\n".join(lines))
    elif r4_changed:
        notify_telegram(
            f"🔧 2nd Brain 온톨로지 Kinetic Layer 실행 완료 — "
            f"규칙4 SLM/LLM 분류 {len(r4_changed)}건, 규칙6 위반 0건(정상)"
        )

    print("완료.")


if __name__ == "__main__":
    main()
