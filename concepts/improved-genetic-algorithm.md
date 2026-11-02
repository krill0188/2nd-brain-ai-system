---
title: "Improved Genetic Algorithm"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [genetic-algorithm, trajectory-planning, uav-swarm, optimization]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Improved Genetic Algorithm

핵심 요약: UAV 군집 협업을 위한 위상 trajectory planning 방식에서 사용되는, 경로 길이와 부드러움을 최적화하기 위해 다목적 최적화 모델과 중복 waypoint 삭제 연산자, 방향 선택 방법을 적용한 유전 알고리즘 변형.

## 개요

본 개념은 "[Phased Trajectory Planning for UAV Swarm Cooperation in Complex Dynamic Environments](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003396199)" 논문에서 소개된 알고리즘입니다. UAV 군집이 복잡하고 동적인 환경에서 협력 비행할 때, 전역 계획 단계에서 사용되는 핵심 최적화 기법입니다. 기존 유전 알고리즘을 개선하여, **다목적 최적화 모델**을 통해 trajectry의 길이와 부드러움(objectives)을 동시에 최적화하고, **중복 waypoint 삭제 연산자(redundant waypoint deletion operator)**와 **방향 선택 방법(directional selection method)**을 도입하여 탐색 효율과 경로 품질을 향상시킵니다.

논문에 따르면, 이 알고리즘은 전역 계획(Global Planning) 단계에서 사용되며, 온라인 로컬 재계획(Local Replanning) 단계에서는 계층형 전략과 개선된 변폭 희소 A* 알고리즘이 활용됩니다.

## 핵심 파라미터

| 파라미터 | 설명 |
| :--- | :--- |
| 최적화 대상 | trajectry 길이, smoothness |
| 연산자 | redundant waypoint deletion operator |
| 기법 | directional selection method |
| 적용 단계 | Global Planning phase |

## 활용처

- UAV 군집 협업에서의 전역 trajectry 계획
- 복잡하고 동적인 환경에서 UAV 군집의 효율적인 경로 최적화
- 다목적 최적화가 필요한 항공기 경로 계획 시스템

## 관련 페이지

- [[Phased Trajectory Planning for UAV Swarm Cooperation in Complex Dynamic Environments]] — 본 논문의 전체 내용이 포함된 문서
- [[Redundant Waypoint Deletion Operator]] — Improved Genetic Algorithm이 구현하는 연산자
- [[Directional Selection Method]] — Improved Genetic Algorithm이 구현하는 기법

## 출처

- (사용자 재확인 필요) 원문 발췌 기반 자동 추출
- 【원문】Zhou, W. et al., "Phased Trajectory Planning for UAV Swarm Cooperation in Complex Dynamic Environments," 2026.

## 참고

[[bio-inspired-algorithms]] [[branch-price-and-cut-algorithm]]
