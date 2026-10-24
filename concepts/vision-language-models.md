---
title: "Vision-Language Models"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [vision-language-models, vlm, uav-navigation, test-time-scaling, llm]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Vision-Language Models

비전 언어 모델(Vision-Language Models, VLMs)은 시각 입력을 언어 모델과 통합하여 의미적 이해와 의사결정을 가능하게 하는 AI 모델입니다. 드론(UAV) 내비게이션 분야에서 VLMs는 복잡한 환경에서 안전하고 정확한 비행 계획을 수립하는 데 활용됩니다.

원문은 VLMs에 테스트-타임(Test-time) 스케일링을 적용하여, 추가 학습 없이도 여러 내비게이션 후보를 생성하고_self-correction(자율 검증) 과정을 통해 최종 경로를 최적화하는 방식을 제시합니다. 기존의 단일 추론 방식보다 복잡한 환경에서의 안전성과 정확도를 크게 향상시킨다고 보고합니다.

## 개요

Vision-Language Models(VLMs)은 이미지나 비디오와 같은 시각적 데이터와 자연어 처리를 결합한 멀티모달 AI 모델입니다. 자율 비행의 핵심 과제인 환경 인식 및 경로 계획에 적용될 때, VLMs는 센서 입력(카메라 등)을 해석하여 의미 있는 명령을 생성할 수 있습니다.

주요 특징은 다음과 같습니다:
- **추가 학습 없이 성능 향상**: 테스트-타임(Test-time) 스케일링 기법을 활용해 모델 재학습 없이도 성능을 향상시킬 수 있습니다.
- **반복적 정제 과정**: 모델이 초기 내비게이션 계획을 재평가하고 Self-correction하는 반복 과정을 거칩니다.
- **다중 후보 생성 및 평가**: 병렬로 생성된 후보들로부터 안전성, 목표 일치도, 전진 진행도 등을 평가하여 최적의 경로를 도출합니다.

## 핵심 파라미터

원문 발췌 내용 중 직접 인용하거나 파라미터로 명시된 사항은 다음과 같습니다. (구체적인 수치나 표가 없어 기본 개념 정리)

- **Test-time Scaling**: 추가 학습 없이 추론 시 모델의 능력을 확장하는 방법
- **Iterative Refinement**: 초기 계획을 반복적으로 검증하고 수정하는 과정
- **Multi-criteria Scoring Function**: 안전성, 목표 일치도, 전진 진행도를 종합적으로 평가하는 점수 함수

## 활용처

- UAV 자율 내비게이션 및 경로 계획
- 복잡한 환경에서 안전 비행을 위한 의미 기반 의사결정
- 테스트-타임(Test-time) 성능 최적화가 필요한 모든 비전 언어 기반 드론 시스템

## 관련 페이지

- [[Vlms|Vlms]] — Vision-Language Models의 약칭으로 사용되는 경우
- [[Test-Time Scaling|Test-Time Scaling]] — VLMs 성능 향상을 위한 방법론
- [[UAV Navigation|UAV Navigation]] — 자율 비행 내비게이션 시스템

## 출처

- (사용자 재확인 필요) 원문: Feinan Cheng et al., "No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation," arXiv:2607.19288v1, 2026-07-21.

---
[ERROR: 복수개의 [SAME_AS] 관계가 있음. 재확인 필요]

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
