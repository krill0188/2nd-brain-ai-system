---
title: "이중 레벨 경로 최적화와 위험 탐색 UAV (Choi 외, 2025)"
created: 2026-10-19
updated: 2026-10-19
type: concept
domain: ops-mission
tags: [drone, ops-mission, drone-ai]
sources: [inbox/processed/fetch-2026-10-19-arxiv-bi-level-route-optimization-and-path-planning-with-hazard-ex.md]
confidence: medium
contested: false
contradictions: []
---

# 이중 레벨 경로 최적화와 위험 탐색

재난 지역 위험 모니터링을 위해 상위 경로 최적화와 하위 경로 계획을 결합한 UAV 전략이다(arXiv 2503.24044, 2025-03). 초록 기준 요약이다.^[inbox/processed/fetch-2026-10-19-arxiv-bi-level-route-optimization-and-path-planning-with-hazard-ex.md]

- **상위**: 알려진 위험 지점 방문 순서를 VRP로 최적화한다. 엣지 기반 중심 보로노이 분할(CVT)이 의사 노드로 기준 경로를 다듬고, 선분 보로노이 도표로 배터리 용량 기반 경로 예산을 배분한다.
- **하위**: 예산 안에서 정보 이득을 최대화하는 B-스플라인 경로를 만들고, 베이지안 추론으로 위험 확률을 갱신해 미탐색 영역을 우선한다.
- 시뮬레이션에서 엣지 기반 CVT가 노드 기반보다 커버리지와 경로 균일성이 좋고, 위험 발견률이 기준선을 일관되게 앞섰다고 한다.

## 연결
산불 위험 관리 비교는 [[pso-uav-bushfire-hazard-management]], 에너지 제약 계획은 [[time-optimal-quadrotor-waypoints]] 참조.
