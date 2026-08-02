# INNOVATION_SCHEMA.md — Innovation Engine 실행 계약

> `docs/INNOVATION_ENGINE.md`(설계) + `docs/INNOVATION_ENGINE_ROADMAP.md`
> (구현계획)의 첫 실제 구현(2026-08-02). 마스터 지시: "질문→답변→답변
> 안에서 완전 새로운 질문→..."을 5라운드 고정 체인으로 구현.

## 디렉터리 구조

```
innovations/
├── runs/<run-id>/
│   ├── 00-seed.md          # 초기 시드(Research Engine 후속조사대상 또는 마스터 프롬프트)
│   ├── state.json          # {run_id, status, current_round, max_rounds, llm_calls}
│   ├── .tried-pairs.json   # 이번 런에서 이미 쓴 cross-domain 노드쌍(재선택 방지)
│   └── round-N/
│       ├── 00-pair.md            # 기계: cross-domain 노드쌍(ontologyClass 다름 + 미연결)
│       ├── 01-combination.md     # LLM: 후보 2개 + 다음 질문
│       ├── 02-critique.md        # LLM(독립): Novelty/Feasibility 점수
│       ├── 03-risk-classify.md   # LLM: Risk + 후보 타입 분류
│       └── 04-proposal.md        # LLM: 최종 제안(다음 라운드 시드가 됨)
├── prompts/{combination,critique,risk-classify,proposal}.md
└── registry/<run-id>.md    # 전 라운드 제안이 순서대로 누적되는 최종 산출물(canonical 아님)
```

## 체인 메커니즘 (마스터 지시의 핵심)

각 라운드의 `04-proposal.md` 마지막 섹션("다음 단계 — 완전히 새로운
질문")이 **다음 라운드 Combination 단계의 컨텍스트**로 그대로 들어간다.
동시에 매 라운드마다 기계가 새로운 cross-domain 노드쌍을 하나 더
골라(`.tried-pairs.json`으로 중복 방지) 조합에 신선한 재료를 계속
공급한다 — "이전 답의 연장"과 "완전히 새로운 재료 투입"이 매 라운드
함께 일어난다.

## 실행

```bash
scripts/innovation-run.sh start "<초기 시드>"
scripts/innovation-run.sh status <run-id>
```

- **고정 5라운드** — 무한루프 아님(비용·품질 위험 회피, 마스터 확인).
- **canonical에 절대 쓰지 않는다** — `innovations/registry/`에만 누적.
  `GO` 판정 후 실제 프로젝트로 채택 여부는 항상 사람이 수동으로 결정
  (`docs/INNOVATION_ENGINE.md` §5 원칙 그대로 유지).
- `Weapon System Candidate` 분류가 나와도 구체적 설계·사양을 생성하지
  않는다 — 지식 분류 라벨일 뿐(프롬프트에 강제, `risk-classify.md` 참조).
- LLM 호출 상한 22회(4단계×5라운드+여유), `research-run.sh`와 동일한
  안전 패턴(`--tools "" --safe-mode`, 2회 재시도) 재사용.

## 검증 이력

- 2026-08-02: `INNOVATION_MAX_ROUNDS=1`로 1라운드 라이브 스모크 테스트
  성공(`innovations/registry/20260802-innovation-innovation-1785681075.md`) —
  센서 캘리브레이션+음성인식 마이크 어레이 결합 → 드론 자가 음향진단
  발상 → Critique가 실제로 인과관계 미검증 허점을 잡아 Feasibility
  감점 → 다음 질문이 원 제안을 넘어선 "플릿 연합학습 예측정비"로
  자연 확장됨을 확인. 결정론적 부분(slugify/state.json/노드쌍 선택)
  `test_innovation_run.sh` 6/6, `test_innovation_combine.py` 6/6 통과.

## 사용하지 않은 설계 축소 사항 (정직하게 기록)

`docs/INNOVATION_ENGINE.md` §3의 원안은 8단계(Knowledge Gap/Novel
Combination/Novelty Check/Technology Evolution/Future Technology/
Feasibility Critique/Risk & Regulation/Candidate Type)였으나, 이번
구현은 4단계(Combination/Critique[Novelty+Feasibility 통합]/
Risk-Classify[Risk+Type 통합]/Proposal)로 압축했다 — 5라운드 체인
전체의 LLM 호출 수(20회)를 실행 가능한 범위로 유지하기 위한 의도적
축소다. Technology Evolution/Future Technology(추세 외삽) 단계는
이번 구현에서 생략됐다 — 필요성이 확인되면 별도 단계로 분리 검토.
