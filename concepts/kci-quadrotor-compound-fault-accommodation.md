---
title: "쿼드로터 센서·구동기 복합 고장 보완 기법 (KCI)"
created: 2026-10-07
updated: 2026-10-07
type: concept
domain: flight-control
tags: [drone, drone-ai, research]
sources: [raw/papers/_unclassified/신경망-기반-센서고장-보상과-imu-기반-구동기고장-보상을-통합한-쿼드로터-uav의-복합-고장-보완-기법.md]
confidence: low
contested: false
contradictions: []
---

# 쿼드로터 센서·구동기 복합 고장 보완 기법

정재환(한국항공대)의 한국항공운항학회지(2026) 논문. 센서 고장과 구동기 고장을 하나의 보상 루프로
통합해 추정·보완하는 기법이다. 근거는 초록뿐이며 결과는 시뮬레이션이다(confidence low).
^[raw/papers/_unclassified/신경망-기반-센서고장-보상과-imu-기반-구동기고장-보상을-통합한-쿼드로터-uav의-복합-고장-보완-기법.md]

## 방법

- **센서 고장**: 신경망 관측기로 고장 크기를 추정하고 측정값 보정으로 보상한다.
- **구동기 고장**: IMU 기반 추력·토크 계산으로 추정하고 제어 입력 재구성에 반영한다.
- **특징**: 별도의 고장 판정(decision) 단계 없이 온라인 고장 추정치를 보상 루프에 바로 적용한다.

## 결과

- 시뮬레이션에서 단일 고장과 센서·구동기 복합 고장 모두에서 고장 크기를 효과적으로 추정하고 안정 비행을 유지했다.
  실기체 시험 여부는 초록에 없다.

## 관련 개념

- [[drone-safety-failsafe]] — RTL·Failsafe 등 규칙 기반 안전 장치
- [[calos-lyapunov-safety-layer-quadrotor-rl]] — 쿼드로터 안전 제어 레이어 연구
- [[sensor-calibration]] — 센서 보정과 오차 관리
- [[kci-uav-swarm-mission-reliability-abort]] — 군집 노드 고장률·임무 중단 관점의 신뢰도 모델
- [[indi-stability-tilt-rotor-vtol]] — 제어 효과 불일치·부호 오류가 안정성에 미치는 영향 분석(구동기 고장 추정과 인접한 주제)
