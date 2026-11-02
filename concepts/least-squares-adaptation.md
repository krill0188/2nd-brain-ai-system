---
title: "least-squares adaptation"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [adaptive-control, quadrotor, disturbance-rejection, learning-theory]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# least-squares adaptation

Least-squares adaptation is an online residual adaptation method used in quadrotor trajectory tracking under unmodeled disturbances. It updates model parameters by minimizing the squared error between predicted and actual residuals, but short out-of-domain residuals can corrupt the learned disturbance model when constant-step updates treat every residual gradient uniformly.

## 개요

This method retains the random Fourier feature model and offline BPTT policy while modifying the online update step size to distinguish between in-domain and out-of-domain disturbance residuals. It forms the baseline adaptive-learning component in the Dual Gradient Consensus (DGC) framework, where the online update step is adjusted by comparing each residual gradient with long- and short-term gradient memories to classify the current adaptation regime and suppress unreliable updates.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| 업데이트 규칙 | 오차 최소화를 통해 모델 파라미터 갱신 |
| 스텝 사이즈 | 기존에는 상수(step size) 고정이었으나, DGC에서는 적응 상황에 따라 가변 조정 |
| 잔차 분류 | 장기·단기 그래디언트 메모리 비교를 통한 적응 regime 결정 |

## 활용처

- Quadrotor trajectory tracking under unmodeled disturbances
- Out-of-distribution disturbance rejection in adaptive learning pipelines
- Baseline component for Dual Gradient Consensus (DGC) method

## 관련 페이지

- [[Dual Gradient Consensus]] — least-squares adaptation을 구현하는 전체 프레임워크
- [[Random Fourier Feature]] — DGC가 유지하는 모델 아키텍처의 일부

## 출처

- (사용자 재확인 필요) original paper: Tan, Mingtian; Tzoumas, Vasileios. "Dual Gradient Consensus for Adaptive Learning to Transient Out-of-Distribution Disturbances in Quadrotor Control." arXiv:2610.34538, 2026.

재확인 필요: 원문에서 least-squares adaptation이 단순히 상수 스텝 크기로 업데이트되는 방식으로 설명되어 있으나, DGC 프레임워크 내에서 어떻게 수정·개선되는지에 대한 상세한 수식적 검증은 아직 확인되지 않았습니다.
