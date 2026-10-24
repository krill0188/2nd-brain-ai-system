---
title: "BC-NMPC: Battery-Constrained NMPC with Propulsion Prediction and Replanning for High-Speed Flight"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [battery-constrained, nmpc, propulsion-prediction, replanning, high-speed-flight]
sources: []
confidence: medium
contradictions: []
domain: ai-autonomy
contested: false
---

# BC-NMPC: Battery-Constrained NMPC with Propulsion Prediction and Replanning for High-Speed Flight

BC-NMPC는 배터리 제약 조건을 반영한 비선형 모델 예측 제어(NMPC) 알고리즘으로, 추진력 예측과 재계획 기능을 통해 고속 비행 성능을 지원하고 배터리 수명을 최적화하는 기술입니다. [1]

## 개요

BC-NMPC(Battery-Constrained Nonlinear Model Predictive Control)는 드론의 고속 비행 수행을 위해 개발된 제어 전략입니다. 기존 NMPC에 배터리 수준을 제약 조건으로 추가하고, 추진력 예측 및 실시간 재계획 기능을 통합하여 배터리 수명을 효과적으로 최적화하면서 고속 기동을 수행할 수 있습니다. [1]

## 핵심 파라미터

| 매개변수 | 내용 |
|----------|------|
| 제어 방식 | 비선형 모델 예측 제어 (NMPC) |
| 제약 조건 | 배터리 사용량 |
| 보조 기능 | 추진력 예측, 재계획 |
| 주요 목표 | 고속 비행 지원, 배터리 수명 최적화 |

## 활용처

- 고속 비행 임무 수행
- 배터리 효율이 중요한 장기 임무
- 실시간 경로 재계획이 필요한 환경

## 관련 페이지

- [[drone-power-battery]] — 드론 전력/배터리 [1]
- [[px4-flight-modes]] — PX4 비행 모드 [1]
- [[mission-planning]] — 미션 계획 [1]

## 출처

- [1] Parakh M. Gupta et al., "BC-NMPC: Battery-Constrained NMPC with Propulsion Prediction and Replanning for High-Speed Flight," *Robotics and Autonomous Systems*, 2026. arXiv:2607.23867.

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
