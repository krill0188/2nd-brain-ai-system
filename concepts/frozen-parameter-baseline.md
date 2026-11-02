---
title: "Frozen-parameter baseline"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [baseline, disturbance-rejection, quadrotor-control, rff-mpc]
sources: [raw/papers/_unclassified/dual-gradient-consensus-for-adaptive-learning-to-transient-out-of-distribution-d.md]
confidence: medium
contested: false
contradictions: []
domain: navigation-gnss-denied
---

# Frozen-parameter baseline

DGC와 비교 대상으로 제시된 드론 제어 시스템에서 사용되는 기본 베이스라인 구현으로, 온라인 파라미터 업데이트를 수행하지 않고 사전에 학습된 고정된 파라미터 집합을 사용한다. 이는 적응형 학습 방법과 대비되며, transient out-of-disturbance에 대한 robustness를 평가하는 기준점이 된다.

## 개요

Quadrotor trajectory tracking research에서 온라인 잔차 적응이 disturbance rejection performance에 미치는 영향을 평가하기 위해 사용되는 비교군 베이스라인이다. L1-augmented MPC, RFF-based MPC, constant-step DAPL과 같은 다른 적응법과 비교했을 때, frozen-parameter baseline는 학습이나 파라미터 업데이트가 일어나지 않으므로 가장 단순한 형태의 disturbance rejection 전략을 대표한다. 본 논문에서 DGC가 four types of residuals (in-domain component + short out-domain events)를 테스트한 결과, 모든 경우에 DGC가 가장 낮은 mean position RMSE를 기록했지만, frozen-parameter baseline는 그중에서도 특히 out-domain events에 취약한 것으로 나타났다.

## 핵심 파라미터

| 파라미터 | 값 | 비고 |
| --- | --- | --- |
| 적응 여부 | 비적응 (frozen) | 온라인 업데이트 없음 |
| 베이스라인 군집 | quadrotor trajectory tracking | DGC와 비교 대상 |

## 관련 페이지

- [[Dual Gradient Consensus (DGC)]] — DGC와 비교되었으며, 잔차 그래디언트를 long- 및 short-term memory를 기준으로 분류하고 confidence map을 통해 unreliable updates를 억제하는 적응형 학습 방법
- [[RFF-based MPC]] — random Fourier feature 기반 MPC 베이스라인
- [[L1-augmented MPC]] — L1 augmented MPC 베이스라인
- [[DAPL (Domain-Adaptive Residual Policy)]] — least-squares adaptation을 사용하는 선행 도메인 적응 잔차 정책

## 출처

- (사용자 재확인 필요) raw/papers/_unclassified/dual-gradient-consensus-for-adaptive-learning-to-transient-out-of-distribution-d.md

## 참고

[[frozen-rank-consensus]] [[kci-uav-battery-ecm-parameter-estimation]]
