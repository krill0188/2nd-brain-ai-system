---
title: "AdDiff-GT: UAV 군집 네트워크 커버리지 보존 자가 복구"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: gcs-software
ontology_class: SwarmResearch
tags: [drone, swarm, datalink]
sources: [inbox/processed/fetch-2026-10-17-arxiv-coverage-preserving-self-healing-in-partially-observable-3d-.md]
confidence: medium
contested: false
contradictions: []
---

# AdDiff-GT: 군집 네트워크 자가 복구

**출처**: arXiv 2610.22085 (2026-10-15)

적대적 환경에서 심각한 네트워크 분할이 발생한 UAV 군집 통신망의 복원력을 다룬다.^[inbox/processed/fetch-2026-10-17-arxiv-coverage-preserving-self-healing-in-partially-observable-3d-.md]

## 구성
- **손상 상태 추론**: GCS가 위치 좌표를 전송하지 않고 희소한 로컬 보고만으로 전역 고장을 추론한다.^[inbox/processed/fetch-2026-10-17-arxiv-coverage-preserving-self-healing-in-partially-observable-3d-.md]
- **AdDiff-GT**: 이류-확산(advection-diffusion) 동역학을 노드-슈퍼노드 하이브리드 그래프에 넣은 그래프 트랜스포머. 로컬 메시지 전파는 클러스터 내부 구조, 전역 어텐션은 클러스터 간 상호작용을 모델링한다.^[inbox/processed/fetch-2026-10-17-arxiv-coverage-preserving-self-healing-in-partially-observable-3d-.md]
- 손실은 연결 복원·기동 비용·운동 일관성·클러스터 간 조율·공간 보존을 함께 고려하고, 메타러닝으로 손상 패턴·군집 규모 간 초기화를 전이한다.^[inbox/processed/fetch-2026-10-17-arxiv-coverage-preserving-self-healing-in-partially-observable-3d-.md]
- 8,000개 분할 시나리오(대규모 5,000개 포함) 시뮬레이션에서 6개 기준선 대비 토폴로지 복구와 공간 보존이 우수했다. 메타러닝은 복구 단계는 약간 늘지만 온라인 계획 부담을 줄인다.^[inbox/processed/fetch-2026-10-17-arxiv-coverage-preserving-self-healing-in-partially-observable-3d-.md]

## 관련
[[swarm-coordination]], [[ground-control-station]] 참조. 시뮬레이션 전용 결과다.
