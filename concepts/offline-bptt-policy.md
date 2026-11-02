---
title: "offline BPTT policy"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [adaptive-learning, quadrotor-control, offline-training, gradient-descent]
sources: []
confidence: medium
contradictions: []
domain: ai-autonomy
---

# offline BPTT policy

Quadrotor trajectory tracking under unmodeled disturbances often relies on online residual adaptation, but short out-domain residuals can corrupt the learned disturbance model when constant-step updates treat every residual gradient uniformly. This concept refers to a policy that applies Backpropagation Through Time (BPTT) in an offline manner, allowing the model to learn from sequences of residuals without real-time computation overhead during flight. It is retained within the Dual Gradient Consensus (DGC) framework alongside random Fourier feature models and least-squares adaptation of a prior domain-adaptive residual policy (DAPL).

## 개요

오프라인 BPTT(Backpropagation Through Time) 정책은 quadrotor 소프트웨어 스택 내에서 트랜지언트(일시적) 외래역(disturbance) 적응을 지원하는 학습 패러다임입니다. 온라인 잔차 적응이 단기 외래역 잔차가 학습된 교란 모델을 오염시킬 수 있는 반면, 이 정책은 BPTT를 오프라인에서 적용하여 시퀀스 내 잔차 그래디언트를 효율적으로 활용합니다. 상수 단계 업데이트가 모든 잔차 그래디언트를uniform하게 다루는 기존 방식과 달리, 오프라인 BPTT 정책은 과거의 그래디언트 정보를 활용해 더 견고한 disturbancemodel을 학습할 수 있습니다. 본 개념은 Random Fourier Feature(RFF) 모델 및 least-squares 적응을 적용한 prior domain-adaptive residual policy(DAPL)와 함께 DGC 프레임워크 내에 포함되어 있습니다.

## 핵심 파라미터

| 파라미터 | 설명 |
|----------|------|
| BPTT horizon | 오프라인 정책이 펼쳐볼 시계열 길이 (구체적 값은 논문별 상이, 재확인 필요) |
| residual sequence | 정책 학습에 사용되는 잔차 그래디언트 시퀀스 |
| domain shift indicator | 도메인 이동을 감지하여 정책 업데이트를 트리거하는 임계값 |

*위 표의 수치는 원문에 직접 명시되지 않았으며, 재확인 필요합니다.*

## 활용처

- **Quadrotor trajectory tracking**: 모델 기반 제어와 데이터 기반 적응을 결합한 비행을 목표로 하는 연구 및 실증 플랫폼에서 활용됩니다.
- **Out-of-distribution disturbance rejection**: 일반적인 상수 단계 업데이트가 불안정해지는 상황에서, 과거 그래디언트 정보를 활용해 적응을 회복하는 데 적합합니다.
- **Dual Gradient Consensus (DGC) 프레임워크**: DGC 알고리즘의 핵심 구성 요소 중 하나로, long- 및 short-term gradient memories와 연계하여 작동합니다.

## 관련 페이지

- [[dual-gradient-consensus]] — 오프라인 BPTT 정책을 활용해 상수 단계 업데이트의 한계를 극복하는 적응 학습 방법
- [[random-fourier-feature-model]] — 오프라인 BPTT 정책과 함께 RFF 기반 모델로 retention되는 구성 요소
- [[domain-adaptive-residual-policy-DAPL]] — least-squares 적응과 연계된 prior 정책

## 출처

- (사용자 재확인 필요) — 원문 발췌에는 "offline BPTT policy"라는 용어가 언급되나, 이에 대한 독립적인 정의나 표준 문서는 현재까지 확인되지 않았습니다.
