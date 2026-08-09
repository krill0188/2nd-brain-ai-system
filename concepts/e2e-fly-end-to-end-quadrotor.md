---
title: "E2E-Fly: End-to-End Quadrotor Autonomy System"
created: 2026-07-30
updated: 2026-08-10
type: concept
tags: [drone, flight-control, ai-autonomy, sim-to-real, reinforcement-learning]
sources: []
confidence: medium
contested: false
contradictions: []
domain: flight-control
note: "Raw source not preserved in repo — found during 2026-08-10 provenance audit, needs recapture"
---

# E2E-Fly: End-to-End Quadrotor Autonomy System

시뮬레이션에서 현실로의 제로샷 전송을 위한 통합 훈련-검증-배포 시스템. 미분 가능한 물리 학습을 강화 학습에 통합하고, 시스템 식별, 도메인 랜덤화, 지연 보상, 노이즈 모델링을 통한 sim-to-real 정렬 방법론을 제공한다.

## 핵심 개념

### 통합 프레임워크
- **Differentiable Physics Learning**: 미분 가능한 물리 학습 지원 고성능 시뮬레이터
- **Structured Reward Design**: 일반적인 쿼드로터 작업에 맞춘 구조화된 보상 설계
- **Two-Stage Validation**: sim-to-sim 전송 및 하드웨어 인더루프 테스트

### Sim-to-Real 정렬
- **System Identification**: 시스템 식별
- **Domain Randomization**: 도메인 랜덤화
- **Latency Compensation**: 지연 보상
- **Noise Modeling**: 노이즈 모링

### 배포
- **Low-Level Control Interface**: 전용 저수준 제어 인터페이스
- **Physical Platforms**: 두 개의 물리적 쿼드로터 플랫폼에 정책 배포
- **Six End-to-End Tasks**: 6개 종단간 제어 작업 훈련 및 실제 배포

## 관련 페이지

- [[drone-simulation]] — Gazebo, SITL, 멀티 기체 시뮬레이션
- [[rl-quadrotor-tunable-control]] — RL 기반 쿼드로터 제어 튜닝
- [[px4-offboard-control]] — ROS2 기반 PX4 Offboard 제어

## 출처

- Sun et al., "E2E-Fly: An Integrated Training-to-Deployment System for End-to-End Quadrotor Autonomy", arXiv:2604.12916, 2026.
