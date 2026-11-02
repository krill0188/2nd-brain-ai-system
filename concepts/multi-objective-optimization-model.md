---
title: "Multi-Objective Optimization Model"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [trajectory-optimization, swarm-cooperation, genetic-algorithm, path-smoothness]
sources: []
confidence: medium
contested: false
contradictions: []
domain: navigation-gnss-denied
---

# Multi-Objective Optimization Model

글로벌 궤도 계획 단계에서 UAV 군집의 비행 경로를 최적화하기 위해 유전 알고리즘과 결합된 다목적 최적화 모델로, 비행 경로의 길이와 매끄러움을 동시에 최적화하는 것이 목적입니다. 이 모델은 군집 전체의 효율적인 궤도 계획을 가능하게 하는 핵심 엔진 역할을 수행합니다.

## 개요

본 모델은 UAV 군집이 복잡한 동적 환경에서 협력 비행 수행 시, 각 UAV의 궤적이 충돌을 피하면서도 전체적인 임무 효율성을 극대화하도록 설계되었습니다. 특히 유전 알고리즘(Genetic Algorithm) 기반의 최적화 과정에서, 경로 길이(Path Length) 및 경로의 매끄러움(Smoothness)과 같은 상이하지만 동시에 고려해야 할 여러 목표 함수(Multi-objective Functions)를 균형 있게 처리하여 최적의 솔루션을 도출합니다. 자동 추출된 원문에 따르면, 이 모델에 redundant waypoint deletion operator(중복 waypoint 삭제 연산자)와 directional selection 방법(방향 선택 방법)이 결합되어 적용됩니다.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| 목적 함수 | 궤도 길이(Path Length)와 경로 매끄러움(Smoothness)의 다목적 최적화 |
| 적용 알고리즘 | 개선된 유전 알고리즘(Improved Genetic Algorithm) |
| 보조 연산자 | 중복 waypoint 삭제 연산자(Redundant waypoint deletion operator) |
| 보조 방법 | 방향 선택 방법(Directional selection method) |

## 활용처

- UAV 군집의 전역 전역 경로(global trajectory) 계획
- 복잡한 동적 환경에서의 온라인 로컬 재계획
- 유전 알고리즘 기반의 다목적 최적화가 필요한 기타 비행 계획 시스템

## 관련 페이지

- [[Genetic Algorithm — 유전 알고리즘]]: 이 모델의 기반이 되는 최적화 기법
- [[Phased Trajectory Planning — 상단 궤적 계획]]: 이 모델이 적용된 전체 계획 프레임워크

## 출처

- (사용자 재확인 필요)

## 참고

[[3d-environment-model]] [[3d-modeling]]
