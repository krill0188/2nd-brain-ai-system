---
title: "Two-Dimensional Pathfinding"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [pathfinding, uav-swarm, trajectory-planning, a-star, algorithm]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Two-Dimensional Pathfinding

Two-dimensional pathfinding is a hierarchical motion planning strategy that decouples three-dimensional UAV swarm trajectory search into independent two-dimensional pathfinding and altitude planning components. It is employed in the local replanning phase of phased trajectory planning to achieve high computational efficiency when navigating complex dynamic environments.

## 개요

The method emerges from research on UAV swarm cooperation in complex dynamic environments, where full three-dimensional search spaces present significant computational complexity. By decoupling the three-dimensional search into two-dimensional pathfinding and separate altitude planning, the approach reduces the search space dimensionality while maintaining navigational capability. This strategy is specifically implemented in the local replanning phase of phased trajectory planning systems, enabling real-time path adjustment for swarms operating in challenging environments.

## 핵심 파라미터

| 파라미터 | 설명 |
|----------|------|
| 차원 | 2D 공간 내 경로 탐색 |
| 목적 | 3D 검색 복잡도 감소 및 실시간 경로 재계산 가능하게 함 |
| 적용 계층 | 로컬 재계획 단계 (local replanning phase) |
| 알고리즘 개선 | Improved Variable-Step Sparse A* Algorithm |

## 활용처

- UAV 스웜의 로컬 재계획 단계에서 고효율 경로 탐색
- 복합 동적 환경에서의 스웜 협력 비행
- 실시간 경로 수정 및 장애물 회피가 필요한 상황

## 관련 페이지

- [[Improved Variable-Step Sparse A* Algorithm]] — Two-Dimensional Pathfinding을 구현하는 알고리즘
- [[Phased Trajectory Planning for UAV Swarm Cooperation]] — Two-Dimensional Pathfinding이 적용된 전체 프레임워크

## 출처

- (사용자 재확인 필요)
