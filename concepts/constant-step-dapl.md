---
title: "constant-step DAPL"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [dapl, adaptive-learning, quadrotor-control, rff, out-of-disturbance, gradient-update]
sources: [http://arxiv.org/abs/2610.34538v1]
confidence: medium
contradictions: []
domain: ai-autonomy
---

# constant-step DAPL

constant-step DAPL은 드론 쿼드롯 제어에서 잔차 경사하강법(update step size)을 고정하여 사용하며, 모든 잔차 기울기를 동일하게 처리하는 고정 스텝 크기의 온라인 적응법입니다. 이 방식은 온라인 잔차 적응에 의존하지만, 짧은 도메인 외(out-of-distribution) 잔차는 학습된 교란 모델을 부패시킬 수 있습니다.

## 개요

Quadrotor trajectory tracking under unmodeled disturbances often relies on online residual adaptation, but short out-domain residuals can corrupt the learned disturbance model when constant-step updates treat every residual gradient uniformly. constant-step DAPL(Domain-Adaptive Residual Policy)은 오프라인 BPTT 정책과 least-squares adaptation을 유지하면서, 온라인 업데이트 스텝 크기를 고정하여 구현되는 접근 방식입니다. 논문 [arXiv:2610.34538v1](http://arxiv.org/abs/2610.34538v1)에 따르면, 이 방법은 모든 잔차 경사도를 동일한 스텝 크기로 업데이트하므로, 도메인 외 잔차에 의해 학습 모델이 왜곡될 위험이 있습니다.

## 핵심 파라미터

| 파라미터 | 설명 |
|---------|------|
| step size | 고정값으로 설정된 온라인 업데이트 스텝 크기 |
| least-squares adaptation | prior domain-adaptive residual policy의 가중치 업데이트 방식 |

## 활용처

- 쿼드롯 제어에서의 교란 성분 적응
- 온라인 잔차 기반 모델 업데이트가 필요한 상황

## 관련 페이지

- [[Dual Gradient Consensus (DGC)]] — constant-step DAPL과 비교되며, 잔차 경사를 장기·단기 메모리와 비교해 적응 규제를 수행하는 방식
- [[RFF-based MPC]] — RFF 기반 모델 예측 제어
- [[L1-augmented MPC]] — L1 보강 MPC

## 출처

- (사용자 재확인 필요) [arXiv:2610.34538v1](http://arxiv.org/abs/2610.34538v1) - Dual Gradient Consensus for Adaptive Learning to Transient Out-of-Distribution Disturbances in Quadrotor Control
