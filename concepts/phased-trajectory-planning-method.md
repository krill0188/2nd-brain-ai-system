---
title: "Phased Trajectory Planning Method"
created: 2026-11-01
updated: 2026-11-01
type: concept
tags: [swarm-cooperation, trajectory-planning, uav-swarm, genetic-algorithm, a-star]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Phased Trajectory Planning Method

본 개념은 복잡한 동적 환경에서 UAV 군집 협업을 위해 설계된, 전역 계획과 온라인 로컬 재계획이라는 2단계로 구성된 경로 계획 접근법입니다. 전역 단계에서는 유전 알고리즘 기반의 다목적 최적화 모델을 활용해 비행 경로의 길이와 편활주성을 최적화하며, 이 과정에서 중복 웨이포인트 삭제 연산기와 방향 선택 방법이 적용됩니다. 온라인 로컬 재계획 단계는 3차원 탐색을 2차원 경로 찾기와 고도 계획으로 분할하는 계층적 전략을 통해 효율을 높이고, 단계적 가중 A* 알고리즘을 통해 3차원 탐색 복잡도를 낮춥니다.

## 개요

본 논문은 UAV 군집이 복잡하고 동적인 환경에서 협력 비행할 수 있도록 하는 경로 계획 기법을 제안합니다. 전체적인 비행 경로를 결정하는 **전역 계획(global planning)**과, 장애물이나 환경 변화에 실시간으로 대응하기 위한 **온라인 로컬 재계획(online local replanning)**의 두 단계로 나뉩니다. 전역 계획은 유전 알고리즘을 이용해 경로의 길이와 편활주성을 균형 있게 최적화하며, 로컬 재계획은 3차원 탐색 공간을 2차원 평면 탐색과 고도 계획으로 분리하여 계산 효율을 극대화합니다.

## 핵심 파라미터

| 파라미터 | 내용 |
|---|---|
| 최적화 목표 | 비행 경로 길이와 편활주성 |
| 전역 계획 방법 | 개선된 유전 알고리즘 + 다목적 최적화 모델 |
| 로컬 재계획 방법 | 계층적 전략 (2D 경로 찾기 + 고도 계획) |
| 서브 알고리즘 | 개선된 가변 스텝 희귀 A* |

## 활용처

- 복잡한 동적 환경에서 UAV 군집의 협력 비행 임무
- 실시간 장애물 회피 및 환경 변화에 대응하는 공중 작전
- 탐색 및 구조(SAR), 물류 배송 등 고밀도 비행이 필요한 미션

## 관련 페이지

- [[UAV Swarm Cooperation]] — UAV 군집 협업의 전체 개념 및 관련 기술
- [[Genetic Algorithm (GA)]] — 전역 계획에 사용된 최적화 기법
- [[Sparse A* Algorithm]] — 로컬 재계획에 적용된 탐색 알고리즘

## 출처

- (사용자 재확인 필요)
