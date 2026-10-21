---
title: "Trajectory Optimization for Cellular-Enabled UAV with Connectivity and Battery Constraints"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: electrical-power
tags: [drone, battery-aware, cellular, trajectory, comm-control]
sources: [inbox/processed/hw-20261021-conv-energy-comm-trajectory-battery-im-2023.md]
confidence: medium
contested: false
contradictions: []
---

# Trajectory Optimization for Cellular-Enabled UAV with Connectivity and Battery Constraints

- 원문: arXiv:2307.16207^[inbox/processed/hw-20261021-conv-energy-comm-trajectory-battery-im-2023.md]
- 저자: Hyeon-Seong Im, Kyu-Yeong Kim, Si-Hyeon Lee^[inbox/processed/hw-20261021-conv-energy-comm-trajectory-battery-im-2023.md]
- 발행: 2023-07-30 (v3 2025-06-18)^[inbox/processed/hw-20261021-conv-energy-comm-trajectory-battery-im-2023.md]

## 핵심 내용
페이로드를 두 지점 간 운반하는 셀룰러 연결 드론의 경로 계획. 기지국과 연결을 유지하고 배터리 한계를 지키며, 충전소에서 소진된 배터리를 충전된 것으로 교체할 수 있다. 문제를 2단계 그래프 최단경로 탐색으로 바꿔 다항시간에 최적 궤적을 얻는다. 기존 알고리즘과 비교하고 에너지 최소화, 적재 가능 페이로드 중량 최대화 목적으로 확장한다. IEEE Trans. Vehicular Technology 게재(초록 기재).^[inbox/processed/hw-20261021-conv-energy-comm-trajectory-battery-im-2023.md]
원문 인용: "only our algorithm outputs an optimal UAV trajectory in polynomial time"^[inbox/processed/hw-20261021-conv-energy-comm-trajectory-battery-im-2023.md]

## 설계·운용에 쓸 수 있는 지침
- 연결성 제약과 배터리 제약을 하나의 그래프 탐색으로 합치는 모델링 방법.^[inbox/processed/hw-20261021-conv-energy-comm-trajectory-battery-im-2023.md]

## 한계·미확인
- 초록에 수치 없음. 환경 모델(커버리지 지도) 세부 미확인.^[inbox/processed/hw-20261021-conv-energy-comm-trajectory-battery-im-2023.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[drone-power-battery]]
