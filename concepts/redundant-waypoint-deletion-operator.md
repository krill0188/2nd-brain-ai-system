---
title: "Redundant Waypoint Deletion Operator"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [trajectory-planning, swarm-cooperation, genetic-algorithm, waypoint-optimization]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Redundant Waypoint Deletion Operator

Global trajectory planning for UAV swarms employs a Redundant Waypoint Deletion Operator to remove unnecessary waypoints within an improved genetic algorithm framework. This operator optimizes trajectory length and smoothness by filtering out redundant path points while preserving the essential flight path characteristics. The operator works in conjunction with a directional selection method as part of a multi-objective optimization model designed for complex dynamic environments.

## 개요

UAV swarm cooperation in complex dynamic environments requires efficient trajectory planning that balances path optimality with computational feasibility. The Redundant Waypoint Deletion Operator emerges as a specialized component within the global planning phase of phased trajectory planning systems. Its primary function is to eliminate waypoints that do not contribute to the essential flight path, thereby reducing trajectory length and improving smoothness without compromising the swarm's ability to navigate dynamic obstacles or maintain formation integrity. The operator is integrated into an improved genetic algorithm that utilizes multi-objective optimization, simultaneously optimizing for trajectory length, smoothness, and path efficiency.

## 핵심 파라미터

| 파라미터 | 설명 |
|----------|------|
| Optimization Target | Trajectory length and smoothness |
| Algorithm Framework | Improved Genetic Algorithm |
| Integration | Combined with directional selection method |
| Environment Complexity | Complex dynamic environments |
| Objective | Redundant waypoint identification and removal |

## 활용처

- UAV swarm formation maintenance during coordinated movement
- Trajectory optimization for mission efficiency in dynamic obstacle courses
- Computational load reduction for on-board flight computers
- Path smoothing for improved flight stability and passenger comfort
- Real-time adaptation to changing environmental conditions

## 관련 페이지

- [[Improved Genetic Algorithm]] — Improved Genetic Algorithm --[IMPLEMENTS]--> Redundant Waypoint Deletion Operator
- [[Phased Trajectory Planning]] — Phased approach encompassing global planning and online local replanning for UAV swarm cooperation

## 출처

- (사용자 재확인 필요) — Original paper: "Phased Trajectory Planning for UAV Swarm Cooperation in Complex Dynamic Environments" (2026)

## 참고

[[time-optimal-quadrotor-waypoints]] [[waypoint-navigation]]
