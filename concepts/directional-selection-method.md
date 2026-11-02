---
title: "Directional Selection Method"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [swarm-cooperation, trajectory-planning, optimization, genetic-algorithm]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Directional Selection Method

두 단계(글로벌 계획 및 온라인 로컬 재계획)로 구성된 UAV 군집 협업을 위한 복잡한 동적 환경에서 새로운 위상 소정 경로 계획 방법의 일환으로, 유전 알고리즘에서 경로 최적화(경로 길이 및 매끄러움)을 위해 사용되는 연산자 중 하나이다. 유전 알고리즘 내의 후보 경로군을 평가하고 선정할 때, 특정 방향성을 가진 경로를 선별하거나 선호하는 선택 기법으로 활용된다.

## 개요

본 개념은 `Improved Genetic Algorithm`이 UAV 군집의 궤적을 최적화하기 위해 사용하는 연산자 하나로, 논문 [[Phased Trajectory Planning for UAV Swarm Cooperation in Complex Dynamic Environments]](2026)에서 소개된다. 유전 알고리즘의 연산자 중 하나로, 멀티 오브젝티브 최적화 모델 하에서 후보 경로군 중 '방향성'을 만족하는 경로를 선별하거나 선호하는 역할을 수행한다. 구체적인 수식이나 파라미터 값은 원문에 명시되지 않았으며, 유전 알고리즘 내의 `IMPLEMENTS` 관계에 따라 동작한다고 확인된다.

## 핵심 파라미터

아직 구체적인 수치나 파라미터 값은 확인되지 않았습니다. 원문에서는 유전 알고리즘의 연산자로서 기능하지만, 파라미터 세부사항은 추가 확인이 필요합니다.

## 활용처

- UAV 군집의 위상 소정 경로 계획에서 유전 알고리즘 기반 경로 최적화의 일부로 활용
- 복잡한 동적 환경에서 UAV 군집 협업을 위한 경로 길이 및 매끄러움 최적화

## 관련 페이지

- [[Improved Genetic Algorithm]] — 유전 알고리즘 내에서 Directional Selection Method가 IMPLEMENTS되는 대상

## 출처

- (사용자 재확인 필요)
