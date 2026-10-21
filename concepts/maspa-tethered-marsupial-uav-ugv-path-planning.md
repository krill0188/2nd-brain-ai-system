---
title: "MASPA: 테더 연결 UGV-UAV(마수피얼) 경로 계획"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-21-arxiv-maspa-an-efficient-strategy-for-path-planning-with-a-tethere.md]
confidence: medium
contested: false
contradictions: []
---

# MASPA: 테더 연결 UGV-UAV(마수피얼) 경로 계획

Capitán 등(arXiv 2408.02141 v3, 2024-08)의 논문. UGV, UAV, 둘을 잇는 테더로 구성된 마수피얼 시스템의 경로 계획 전략이다. 초록 기준 요약이다.^[inbox/processed/fetch-2026-10-21-arxiv-maspa-an-efficient-strategy-for-path-planning-with-a-tethere.md]

## 문제 설정
- UAV가 UGV 위에서 시작해 공중 목표에 도달해야 하며, 세 구성요소 모두 3D 직육면체로 모델링된 지상·공중 장애물을 피한다.
- UGV가 먼저 이륙 지점으로 이동한 뒤 UAV가 수직 평면을 따라 비행한다고 가정한다.
- 테더로 UAV 비행 중 배터리 제약을 완화하는 것이 산업적 이점이다.

## 방법
- 공간을 이산화해 지상 경로와 공중 경로 길이의 합을 최소화하는 해를 근사한다.
- 팽팽한(taut) 테더를 가정하고 테더의 볼록성과 장애물 기하를 이용해 UAV의 실행 가능한 이륙 지점 집합(locus)을 효율적으로 구한다. 이를 느슨한 테더 시나리오로 확장한다.
- 시뮬레이션에서 복잡한 상황을 수 초 내 풀었고 RRT* 기반 기준 알고리즘보다 우수했다.

## 관련
테더·케이블 연결 다중체 제어는 [[uav-cable-payload-cooperative-transport-research]], 에너지 제약은 [[multirotor-energy-power-models]], 상위 개요는 [[drone-ai-agents]] 참조.

## 📰 최근 관련 소식
- MASPA: An efficient strategy for path planning with a tethered marsupial robotics system (arxiv.org, 2024-08-04) — http://arxiv.org/abs/2408.02141v3
