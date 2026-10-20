---
title: "UAV 엔진 마운트 3D 다기준 생성 설계 (CVAE, Petroll 외, 2023)"
created: 2026-10-20
updated: 2026-10-20
type: concept
domain: hardware
tags: [drone, drone-hw, drone-ai]
sources: [inbox/processed/fetch-2026-10-20-arxiv-a-generative-neural-network-approach-for-3d-multi-criteria-d.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 엔진 마운트 3D 다기준 생성 설계 (CVAE)

**출처**: arXiv 2311.03414 (2023-11-06), 초록 기준. 정량 성능 수치는 초록에 없다.

조건 기반 3D 형상 생성에서 조건(기능 요구)이 늘면 신경망이 기능-형상 의존성을 학습하기 어려워지는 다기준 문제를 UAV 모터 마운트로 다룬다. 추상 3D 설계 10,000개를 만들어 역학·열역학·공기역학 세 분야 시뮬레이션을 모두 돌리고, 형상과 다기준 기능 제약을 입력으로 Conditional Variational Autoencoder(CVAE)를 학습한다. 생성 결과는 Marching cubes로 메시화해 시뮬레이션으로 재평가하며, 사용자가 정한 기능 조건 아래에서 최적화된 설계를 생성할 수 있음을 보였다.^[inbox/processed/fetch-2026-10-20-arxiv-a-generative-neural-network-approach-for-3d-multi-criteria-d.md]

## 활용 포인트
- 프레임·마운트 형상 탐색을 시뮬레이션 데이터로 학습한 생성 모델로 대체하는 접근이다. 구조 최적화 흐름은 [[uav-airframe-structure-optimization-research]]와 비교할 수 있다.
- 모터·추진계 특성은 [[bldc-motor-esc-characterization-research]] 참조.
