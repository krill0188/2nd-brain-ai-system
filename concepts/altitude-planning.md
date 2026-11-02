---
title: "Altitude Planning"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [trajectory-planning, uav-swarm, optimization, altitude-control]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Altitude Planning

Altitude Planning은 UAV 스웜 협력에서Three-Dimensional Search를 고효율로 처리하기 위해, 3차원 검색을 2차원 경로 탐색과 고도 계획으로 분리하는 계층적 전략의 일부로 기능한다. 글로벌 계획 단계에서 개선된 유전 알고리즘이 trajectory length와 smoothness를 최적화하는 데 사용되며, 로컬 재계획 단계에서는 improved variable-step sparse A* 알고리즘을 활용하여 3차원 검색 복잡도를 낮춘다.

## 개요

복잡한 동적 환경에서 UAV 스웜의 협력을 가능하게 하기 위해 개발된 개념이다. 논문에서는 전역 계획과 온라인 로컬 재계획의 두 단계로 구성된 상향식 접근 방식을 제시한다. 전역 계획 단계에서는 trajectory의 길이와 smoothness를 최적화하기 위해 개선된 유전 알고리즘과 multi-objective optimization model이 사용되며, redundant waypoint deletion operator와 directional selection method가 포함된다. 로컬 재계획 단계에서는 3차원 검색을 2차원 경로 탐색과 고도 계획으로 분리하여 효율을 높이며, improved variable-step sparse A* 알고리즘이 3차원 검색 복잡도를 감소시키는 역할을 한다.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| Optimization Model | Multi-objective optimization model for trajectory length and smoothness |
| Algorithm | Improved genetic algorithm with redundant waypoint deletion operator and directional selection method |
| Search Strategy | Hierarchical decoupling of 3D search into 2D pathfinding and altitude planning |
| Local Replanning Algorithm | Improved variable-step sparse A* algorithm |

## 활용처

- UAV 스웜 협력 비행에서 복잡한 동적 환경 탐색 및 경로 계획
- 3차원 검색 공간의 복잡도 감소 및 계획 효율 향상이 필요한 경우

## 관련 페이지

- [[Three-Dimensional Search Decoupling]] — IMPLEMENTS Altitude Planning
- [[Trajectory Planning]] — 연관 개념 (전역 계획 및 로컬 재계획의 기초가 되는 broader 개념)

## 출처

- (사용자 재확인 필요)
