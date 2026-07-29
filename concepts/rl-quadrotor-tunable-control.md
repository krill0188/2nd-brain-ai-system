---
title: "RL-Based Quadrotor Control with Tunable Performance"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, flight-control, reinforcement-learning, control-theory, px4]
sources: [raw/papers/flight-control/rl-quadrotor-tunable-control.md]
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# RL-Based Quadrotor Control with Tunable Performance

보상 설계와 종료 조건을 통한 RL 기반 쿼드로터 제어의 성능 튜닝 방법론. PPO(Proximal Policy Optimization) 알고리즘과 이중 대역폭 지수 보상 구조를 활용하여 임계 감쇠 응답 기준선을 달성하고, 직관적인 휴리스틱 규칙으로 빠른(곡예) 및 느린(검사) 정착 시간 성능을 조정한다.

## 핵심 개념

### 보상 구조
- **Dual Bandwidth Exponentials**: 임계 감쇠 응답을 달성하는 새로운 보상 구조
- **Setpoint Tracking**: 낮은 정상 상태 오차(~2%) 달성
- **Episode Truncation**: 600만 시간 단계 내 샘플 효율적 학습

### 성능 모드
- **Baseline**: 임계 감쇠 응답, 정상 상태 오차 ~2%
- **Acrobatic**: 빠른 정착 시간, 곡예 비행 성능
- **Inspection**: 느린 정착 시간, 정밀 검사 성능

## 응용 분야

- 인프라 검사 (정밀 제어 필요)
- 드론 레이싱 (속도와 민첩성)
- 숲 상공 검사 (Under-canopy forest inspection)

## 관련 페이지

- [[px4-flight-modes]] — PX4 자동조종장치 비행 모드 분류
- [[drone-simulation]] — Gazebo, SITL 기반 시뮬레이션
- [[ros2-drone-integration]] — ROS2 기반 드론 연동 스택

## 출처

- Lagos Suarez et al., "A Heuristic Approach for Performance Tuning in RL-based Quadrotor Control via Reward Design and Termination Conditions", arXiv:2605.19166, 2026.
- Lagos Suarez et al., "Aerial Inspection Behaviors via RL-based Quadrotor Control for Under-canopy Forest Environments", arXiv:2605.19202, 2026.
