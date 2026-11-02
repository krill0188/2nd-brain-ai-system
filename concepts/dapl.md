---
title: "DAPL"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [adaptive-learning, control-theory, out-of-distribution, quadrotor, rff, transient-disturbances]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# DAPL

DAPL(대상 도메인 적응형 잔여 정책)은 항목 특성 변환(Random Fourier Feature) 모델과 오프라인 역전파 시계열(offline BPTT) 정책을 기반으로 하며, 최소제곱법을 활용해 잔여 보상 정책을 적응적으로 업데이트하는 방식입니다. 단일 단계 업데이트가 아닌 과거 학습 데이터와 장기/단기 그래디언트 기억을 비교해 현재 적응 레지임을 분류하고, 신뢰도 맵을 통해 신뢰할 수 없는 업데이트를 억제하는 방식을 사용합니다.

## 개요

본 문서에서 언급된 DAPL은 이차원 쿼드콥터 궤도 추적 문제에서 짧은 도메인 외(out-of-distribution) 잔여들에 의한 learned disturbance model의 부패를 방지하기 위한 적응형 학습 기법의 기초가 되는 요소입니다. DAPL은 RFF 기반 정책과 least-squares adaptation을 결합하여, constant-step 업데이트가 가져다주는 단점을 보완합니다.

## 핵심 파라미터

- **기반 모델**: Random Fourier Feature (RFF) 모델
- **최적화 방법**: 오프라인 BPTT(역전파를 통한 시계열 학습) 정책
- **적응 알고리즘**: 최소제곱법(least-squares)
- **특징**: 온라인 업데이트 단계 사이즈 가변성, 장기/단기 그래디언트 기억 비교, 신뢰도 맵을 통한 업데이트 억제

## 활용처

- 쿼드콥터 궤도 추적에서 in-domain과 short out-of-domain disturbance가 혼합된 환경 하에서의 잔여 정책 적응
- 온라인 그래디언트 기반 적응법이 short out-of-domain residuals에 의해 학습 모델이 타락하는 것을 방지하고자 할 때 활용

## 관련 페이지

- [[Dual Gradient Consensus (DGC)]] — DAPL을 기반으로 온라인 업데이트 단계 사이즈를 수정하고, 장기/단기 그래디언트 기억을 비교해 적응 레지임을 분류하는 상위 기법

## 출처

- (사용자 재확인 필요) Dual Gradient Consensus for Adaptive Learning to Transient Out-of-Distribution Disturbances in Quadrotor Control, Tan & Tzoumas, 2026. arXiv:2610.34538.

## 참고

[[quadrotor]] [[constant-step-dapl]]
