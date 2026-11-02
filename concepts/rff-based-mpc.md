---
title: "RFF-based MPC"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [mpc, adaptive-control, rff, quadrotor, trajectory-tracking]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# RFF-based MPC

RFF-based MPC는 무작위 푸리에 특성(Random Fourier Feature)을 이용한 모델 예측 제어(Model Predictive Control) 방식입니다. quadrotor의 궤적 추적에서 온라인 잔차 적응(residual adaptation) 기반의 교외(Out-of-Distribution) 교란에 대한 기존 방법의 한계를 보완하고자 하며, 기본 모델로 무작위 푸리에 특성 모델을 유지합니다.

## 개요

Quadrotor trajectory tracking에서 unmodeled disturbances이 존재할 경우, 기존 방법은 constant-step 업데이트를 통해 모든 잔차 gradient를 균일하게 처리하지만, 이는 short out-domain residuals가 학습된 disturbance model을 오염시킬 수 있습니다. RFF-based MPC는 이러한 문제를 해결하기 위해 무작위 푸리에 특성을 사용하여 함수 근사(function approximation)를 수행하는 접근 방식입니다.

## 스펙

| 파라미터 | 설명 |
|---|---|
| Model | Random Fourier Feature based |
| Control Method | Model Predictive Control |
| Application | Quadrotor trajectory tracking |

## 활용처

- Quadrotor의 궤적 tracking
- unmodeled disturbance가 있는 환경에서의 adaptive control

## 관련 페이지
- [[Dual Gradient Consensus]] — DGC와 비교대상이 되는 방법이며, RFF-based MPC를 COMPARES_TO 관계로 가짐
- [[RFF-based MPC]] — 본 문서

## 출처
- (사용자 재확인 필요) 원문: arXiv 2026 논문 "Dual Gradient Consensus for Adaptive Learning to Transient Out-of-Distribution Disturbances in Quadrotor Control" (DOI: 10.48550/arXiv.2610.34538)

## 참고

[[mpc]] [[quadrotor]]
