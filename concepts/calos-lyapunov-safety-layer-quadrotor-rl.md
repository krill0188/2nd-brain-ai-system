---
title: "CALOS: 쿼드로터 안전 강화학습을 위한 Control-Affine Lyapunov On-manifold Safety Layer"
created: 2026-09-18
updated: 2026-09-18
type: concept
domain: flight-control
tags: [drone, flight-control, reinforcement-learning, safety]
sources: [inbox/fetch-2026-09-18-arxiv-calos-control-affine-lyapunov-on-manifold-safety-layer-for-s.md]
confidence: medium
contested: false
contradictions: []
---

# CALOS: 쿼드로터 안전 강화학습을 위한 Control-Affine Lyapunov On-manifold Safety Layer

Cesareo·Mengozzi·Mimmo·Acquaviva(2026-09-15, arXiv)가 제안한 런타임 안전 계층으로,
학습 알고리즘 자체를 바꾸지 않고 쿼드로터 자세(attitude) 제약을 강제한다.^[inbox/fetch-2026-09-18-arxiv-calos-control-affine-lyapunov-on-manifold-safety-layer-for-s.md]
4개의 틸트각 부등식과 Lyapunov 감쇠 조건을 하나의 이차계획법(QP)으로 정식화하고,
정책이 출력한 명목 토크에 대한 최소 노름 보정값을 QP 해로 계산한다.

## 핵심 메커니즘

- 3차원 토크 공간에서 active-set 전수 탐색으로 QP를 정확히(exactly) 풂 — 수천 개의
  병렬 시뮬레이션 환경에서 실시간 제약 강제가 가능할 만큼 저비용.
- NVIDIA Isaac Lab 궤적 추종 과제에서 검증: 제약 없는 PPO 베이스라인 대비 횡방향
  추종 오차 55~60% 감소, 학습 궤적 상 자세 제약 위반 0건 달성.
- 탐색을 안전한 상태공간 영역으로 제한함으로써 학습 수렴 속도와 데이터 효율도
  함께 개선되며, 정책이 과도하게 보수적으로 변질되지 않음.

## 시사점

대규모 병렬 DRL 훈련(수천 환경 동시 실행)에서 안전 제약을 별도 레이어로 분리해
강제하는 접근은, 비행 제어기에 강화학습 정책을 직접 탑재하려는 시도에서 검증·인증
가능성을 높이는 실용적 경로로 볼 수 있다.

## 관련 개념

- [[rl-quadrotor-tunable-control]] — 튜닝 가능한 성능을 갖는 RL 기반 쿼드로터 제어
- [[lightweight-safe-rl-uav]] — 경량 안전 강화학습 UAV 내비게이션
