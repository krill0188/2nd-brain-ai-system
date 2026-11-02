---
title: "Online Local Replanning"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [swarm-cooperation, trajectory-planning, uav-swarm, dynamic-environment, replanning]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Online Local Replanning

Online Local Replanning은 UAV 군집이 복잡한 동적 환경에서 협력 비행 중 실시간으로 국소적인 경로 재계산을 수행하는 개념입니다. 전역 계획 수립 후 발생하는 예상치 못한 장애물이나 환경 변화에 대응하여, 계층형 전략을 통해 3차원 검색을 2차원 경로 탐색과 고도 계획으로 분리하여 효율을 높이는 방식으로 동작합니다.

## 개요

본 개념은 UAV 군집 협력의 두 번째 주요 단계인 온라인 국소 재계획(Online Local Replanning)을 의미합니다. 전역 계획 phase에서 유전 알고리즘을 이용한 전역 경로 최적화가 수행된 이후, 실제 비행 중 감지된 동적 장애물이나 환경 변화에 대응하기 위해 실시간으로 국소 경로를 재설계하는 역할을 합니다. 계층형 전략을 활용하여 3차원 공간의 검색 복잡도를 낮추고, 개선된 단계적 희소 A* 알고리즘을 통해 효율적인 2차원 경로 탐색과 고도 계획을 동시에 수행합니다.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| 검색 차원 | 3차원 검색을 2차원 경로 탐색과 고도 계획으로 분리 |
| 알고리즘 | 개선된 단계적 희소 A* (improved variable-step sparse A*) |
| 목표 | 고효율 국소 경로 재획득 및 동적 환경 적응 |

## 활용처

- 복잡한 동적 환경에서 UAV 군집의 실시간 항법 및 협력 비행
- 장애물 회피 및 동적 경로 재조정이 필요한 임무 수행 상황
- 전역 계획 후 실시간으로 발생하는 예외 상황 처리

## 관련 페이지

- [[Phased Trajectory Planning Method]] — [HAS_PHASE] 관계가 존재하는 상위 개념
- [[Hierarchical Strategy]] — [IMPLEMENTS] 관계가 존재하는 하위 전략

## 출처

- (사용자 재확인 필요)
