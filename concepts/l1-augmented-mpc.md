---
title: "L1-augmented MPC"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [adaptive-control, robust-tracking, rff-quadrotor, mpc, dr-wiki-autotag]
sources: ["arXiv:2610.34538v1 (2026)"]
confidence: medium
contradictions: []
domain: flight-control
---

# L1-augmented MPC

L1-augmented MPC는 무인항공기(UAV), 특히 쿼드러콥터의 소요 추적 제어에 사용되는 제어 전략으로, MPC(예측 제어)의 한계를 보완하기 위해 L1 적응제어 이론을 결합한 접근법입니다. 일반적인 MPC는 모델링 오차와 외부 교란에 취약할 수 있지만, L1 적응제어와 결합하면 이러한 교란과 모델 불확실성을 실시간으로 추정·보상하여 추적 성능을 향상시킬 수 있습니다.

## 개요

Quadrotor 소요 궤적 추적에서 온라인 잔차 적응은 교란 보상에 효과적이지만, 상수 단계 업데이트는 모든 잔차 기울기를 균일하게 처리하여 도메인 외부 잔차에 의해 학습된 교란 모델이 왜곡될 수 있습니다. L1-augmented MPC는 이러한 문제를 해결하기 위해, Dual Gradient Consensus (DGC)와 같은 적응 학습 방법과 결합하거나 독자적으로 사용되며, 무한대 호라이즌 MPC와 L1 적응제어의 장점을 결합합니다. 특히 고주파 교란 하에서도 쿼드러콥터의 안정적인 비행을 보장하고 추적 정확도를 높이는 것이 목표입니다.

## 핵심 파라미터

| 파라미터 | 설명 |
| :--- | :--- |
| **L1 필터 차수** | L1 적응필터의 차수이며, 교란 추정에 영향을 미칩니다. |
| **MPC 호라이즌** | 예측 제어에서 미래 상태를 예측하는 예측 horiomon의 길이입니다. |
| **적응 이득** | L1 적응기에서 사용하는 이득 매개변수입니다. |

*(위 표는 원문 발췌에 명시된 파라미터에 기반한 추정이며, 실제 값은 해당 논문의 파라미터 섹션을 재확인해야 합니다.)*

## 활용처

- 쿼드러콥터 궤적 추적 제어
- 모델 불확실성이 있는 시스템에서의 비행 안정화
- GCS(Ground Control Station) 기반 실시간 제어 시스템

## 관련 페이지

- [[Dual Gradient Consensus]] — L1-augmented MPC와 비교대상이 되며, 상수 단계 업데이트의 단점을 보완하는 적응 학습 방법으로 제안됨. (COMPARES_TO 관계)
- [[RFF-based MPC]] — 유사한 접근법 중 하나로, 랜덤 푸리에 피처를 활용한 MPC 변형입니다.

## 출처

- (사용자 재확인 필요) — 원문([arXiv:2610.34538v1](http://arxiv.org/abs/2610.34538v1))에 명시된 정의 및 성능 비교 결과이며, 자세한 파라미터 및 메커니즘은 해당 논문을 직접 확인할 것.
