---
title: "trajectory prediction"
created: 2026-10-24
updated: 2026-10-24
type: entity
tags: [drone-visual-navigation, world-action-model, trajectory-accuracy, prediction-depth]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# trajectory prediction

드리머비주얼 네비게이션 에이전트가 후보 동작이 미래 관찰을 어떻게 변화시킬지 미리 파악하고, 예측된 결과에 따라 동작하도록 돕는 핵심 기능입니다. 특히 드론은 정밀도와 효율성 제약 하에서 작동해야 하므로, 향후 상태를 명시적인 이미지 생성 없이 표현 공간에서 직접 모델링하는 접근이 요구됩니다.

## 개요

World-action model의 핵심 목적 중 하나는 에이전트가 동작의 예측된 결과를 기반으로 동작하게 하는 것입니다. DroneWAM은 JEPA 기반 아키텍처를 사용하여 명시적인 미래 이미지 생성 비용을 회피하고, 미래 상태를 표현 공간에서 직접 모델링합니다. 또한 밀집된 인코더 특징을 더 적은 잠재 토큰으로 압축하는 사전 훈련된 Resampler를 도입하여, 각 상상 단계(reimagined step)에서 반복되는 연산 비용을 감소시킵니다. 여기에 현재 장면 상황에 따라 예측 깊이를 가변적으로 할당하는 adaptive rollout 메커니즘을 적용하여, 예측 리소스를 효율적으로 배분합니다.

## 핵심 파라미터

- **기본 예측 깊이**: 8 steps
- **적응적 예측 깊이(Adaptive rollout)**: 평균 4.58 steps로 감소
- **데이터셋**: DroneNav-6D (동기화 RGB 관측치, 6-DoF 비행 궤적, 제어 명령, 임의 풍동 disturbance 포함)

## 활용처

- 드론 시각 네비게이션에서 향후 관측치 변화 예측
- 동작 결정의 전제 조건으로, 정책이 예측된 결과를 바탕으로 최적의 제어 명령을 선택하도록 지원

## 관련 페이지

- [[world-action-model]] — trajectory prediction을 예측하는 상위 모델
- [[dronewam]] — 본 문서에서 소개된 구체적인 trajectory prediction 구현체
- [[drone-nav-6d]] — trajectory prediction 학습에 사용된 시뮬레이션 데이터셋

## 출처

- (사용자 재확인 필요) 원문 발췌 내용 기반, 상세 검증 필요
---

## 분류

- [[auto-hub-concept]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
