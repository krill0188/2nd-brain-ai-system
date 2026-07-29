---
title: "Lightweight Safe RL for UAV Navigation"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, ai-autonomy, reinforcement-learning, safety, collision-avoidance]
sources: [raw/papers/ai-autonomy/lightweight-safe-rl-uav.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# Lightweight Safe RL for UAV Navigation

밀집 환경에서 안전한 UAV 내비게이션을 위한 경량 안전 강화 학습 프레임워크. 비대칭 및 깊이별 분리 합성곱으로 희소 관측을 충돌 위험 인지 특징으로 인코딩하고, 제약 마르코프 결정 과정과 라그랑주 기반 안전 PPO로 안전성을 보장한다.

## 핵심 개념

### 경량 네트워크
- **Asymmetric Convolutions**: 비대칭 합성곱
- **Depthwise Separable Convolutions**: 깊이별 분리 합성곱
- **Collision-Risk-Aware Features**: 충돌 위험 인지 특징 인코딩

### 안전 메커니즘
- **Constrained MDP**: 제약 마르코프 결정 과정
- **Hierarchical Control Architecture**: 계층적 제어 아키텍처
- **Lagrangian-Based Safe PPO**: 라그랑주 기반 안전 PPO 알고리즘
- **Curriculum Learning**: 커리큘럼 학습으로 훈련 안정성 향상

### 성능
- 다양한 장애물 밀도 및 비행 속도에서 높은 성공률
- 기존 RL 기준선 대비 개선된 안전성 및 효율성
- 경량 온보드 배포 가능

## 관련 페이지

- [[computer-vision-drone]] — 드론 컴퓨터 비전 및 객체 검출
- [[drone-safety-failsafe]] — RTL, Geofence 등 안전 장치
- [[rl-quadrotor-tunable-control]] — RL 기반 쿼드로터 제어

## 출처

- Zhang et al., "Lightweight Safe Reinforcement Learning for End-to-End UAV Navigation", arXiv:2607.01794, 2026.
