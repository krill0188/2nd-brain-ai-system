---
title: "AutoPilot: Automating SoC Design Space Exploration for SWaP Constrained Autonomous UAVs"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, swap, co-design, accelerator, bayesian-optimization]
sources: [inbox/processed/hw-20261021-conv-swap-autopilot-krishnan-2021.md]
confidence: medium
contested: false
contradictions: []
---

# AutoPilot: Automating SoC Design Space Exploration for SWaP Constrained Autonomous UAVs

- 원문: arXiv:2102.02988^[inbox/processed/hw-20261021-conv-swap-autopilot-krishnan-2021.md]
- 저자: Srivatsan Krishnan, Zishen Wan, Kshitij Bhardwaj, Paul Whatmough, Aleksandra Faust, Sabrina Neuman, Gu-Yeon Wei, David Brooks, Vijay Janapa Reddi^[inbox/processed/hw-20261021-conv-swap-autopilot-krishnan-2021.md]
- 발행: 2021-02-05 (v3 2021-09-10)^[inbox/processed/hw-20261021-conv-swap-autopilot-krishnan-2021.md]

## 핵심 내용
온보드 컴퓨트 설계에 체계적 방법론이 없는 문제를 다룬다. 센서율, 연산 성능 같은 사이버 요소와 페이로드 중량 같은 물리 요소가 결합되며 조합 수가 수만에서 수십억에 이른다. AutoPilot은 베이지안 최적화로 자율 알고리즘과 하드웨어 가속기를 함께 선택한다. 3종 UAV, 3종 환경에서 Xavier NX, Jetson TX2, 전용 UAV 가속기보다 우수하며 수행 가능한 임무 수를 나노 UAV 최대 2.25배, 마이크로 1.62배, 미니 1.43배 늘린다고 보고.^[inbox/processed/hw-20261021-conv-swap-autopilot-krishnan-2021.md]
원문 인용: "AutoPilot uses Bayesian optimization to navigate a large design space"^[inbox/processed/hw-20261021-conv-swap-autopilot-krishnan-2021.md]

## 설계·운용에 쓸 수 있는 지침
- 컴퓨트 선정을 점수가 아니라 임무 수(에너지·중량 포함)로 평가하는 공동설계 관점.^[inbox/processed/hw-20261021-conv-swap-autopilot-krishnan-2021.md]

## 한계·미확인
- 임무 수의 기준 정의와 절대값은 초록에 없음: 미확인.^[inbox/processed/hw-20261021-conv-swap-autopilot-krishnan-2021.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[drone-power-battery]]
