---
title: "UAV 지원 SWIPT-MEC 자원 관리 SAC 강화학습 (Chen 외, 2025)"
created: 2026-10-19
updated: 2026-10-19
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, datalink]
sources: [inbox/processed/fetch-2026-10-19-arxiv-joint-resource-management-for-energy-efficient-uav-assisted-.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 지원 SWIPT-MEC 자원 관리 (DRL)

지상 인프라가 없는 원격·재난 지역에서 UAV가 지향성 안테나로 IoT 단말에 연산 자원과 무선 전력을 함께 제공하는 시스템이다(arXiv 2505.03230, 2025-05). 초록 기준 요약이다.^[inbox/processed/fetch-2026-10-19-arxiv-joint-resource-management-for-energy-efficient-uav-assisted-.md]

- 시스템 에너지 효율과 단말 배터리 지속성을 동시에 다루는 2목적 비볼록 문제를 MDP로 재정식화한다.
- 행동 단순화 메커니즘을 넣은 개선 SAC 알고리즘을 제안하며, 경계 페널티와 충전 보상이 수렴·일반화에 기여한다고 한다.
- 시뮬레이션에서 여러 기준선보다 우수하고 복잡한 환경에서도 일반화가 강하다고 보고한다. 실기체 검증은 없다.

## 연결
링크 에너지 효율은 [[uav-uplink-energy-efficiency-los]], 통신 개요는 [[datalink-communication]], 전력 모델은 [[multirotor-energy-power-models]] 참조.
