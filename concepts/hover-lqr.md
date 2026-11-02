---
title: "hover LQR"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [lqr, quadrotor, controller-comparison, tuning-protocol, hover-control]
sources: []
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# hover LQR

hover LQR은 쿼드럽터 안정 비행 제어에서 사용되는 선형 quadratic regulator 기반 제어기로, 시스템 선형화를 기반으로 한 최적 제어 방법입니다. [hover LQR]는 [tuning protocol]의 매칭 12개 후보 튜닝 전략 변화에 따라 평균 RMSE 순위가 변동하는 주요 후보로 확인된 바 있으며, [BL-SMC]가 최하위에서 1위로 상승하는 재순위가 발생한 영향을 직접적으로 받았습니다.

## 개요

[hover LQR]는 쿼드롭터의 6자유도 모델을 선형화하여 디자인된 LQR 이득 행렬을 사용하는 피드백 제어 방식입니다. [paper: How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study](http://arxiv.org/abs/2610.35165v1)에 제시된 연구에 따르면, [hover LQR]는 PID, SLIDING-MODE, MPC 등 다양한 제어기와 비교 평가 대상으로 포함되었으며, [tuning protocol]의 후보군 확대에 따라 성능 순위가 영향을 받는 경향을 보였습니다. 연구에서는 50Hz 샘플링 주파수에서 556개의 에피소드를 대상으로 비교 실험을 수행했으며, [hover LQR]는 기준 설정 하에서 BL-SMC에 이어 중간 이하 수준의 성능을 보이다가, 매칭된 12개 튜닝 후보 프로토콜 적용 후 순위가 상승한 것으로观测되었습니다.

## 핵심 파라미터

| 파라미터 | 내용 |
|---|---|
| 제어 방식 | LQR (Linear Quadratic Regulator) |
| 플랫폼 | 쿼드럽터 (Quadrotor) |
| 연구 맥락 | 컨트롤러 비교 시뮬레이션 연구 |
| 샘플링 주파수 | 50 Hz |
| 튜닝 후보군 | 12개 매칭 프로토콜 |

## 활용처

- 쿼드럽터 비행 제어 연구 및 시뮬레이션 비교 실험
- 최적 제어 이론 기반 자율비행 알고리즘 개발
- 다른 제어 전략(BL-SMC, MPC 등)과의 성능 벤치마킹

## 관련 페이지

- [[tuning protocol]] — IMPACTS: [tuning protocol] --[IMPACTS]--> [hover LQR]
- [[BL-SMC]] — boundary-layer sliding-mode control
- [[LMPC-F]] — linear MPC with LQR fallback

## 출처

- (사용자 재확인 필요) [paper: How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study](http://arxiv.org/abs/2610.35165v1), Dao et al., 2026.

## 참고

[[quadrotor]] [[hover-point-throttle-curve]]
