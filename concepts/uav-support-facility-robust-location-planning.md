---
title: "시설 고장을 고려한 UAV 감시 지원시설 강건 입지 계획"
created: 2026-09-05
updated: 2026-09-05
type: concept
domain: ops-mission
tags: [drone, ops-mission]
sources: [raw/papers/_unclassified/시설-고장-상황을-고려한-uav-감시-지원시설의-강건-입지-계획-문제.md]
confidence: medium
contested: false
contradictions: []
---

# 시설 고장을 고려한 UAV 감시 지원시설 강건 입지 계획

UAV 감시 시스템의 안정적 운영에는 충전·유지보수·운영 제어를 수행하는 지원시설이 필수적이다. 이
연구는 시설 고장이라는 불확실성이 발생했을 때 UAV 운용 불능과 감시 공백으로 이어지는 문제를
"불확실성 예산(uncertainty budget) 기반 강건 최적화 모형"으로 다룬다 ^[raw/papers/_unclassified/시설-고장-상황을-고려한-uav-감시-지원시설의-강건-입지-계획-문제.md].

## 문제 정식화

- 후보 시설 위치 중 일부를 선택해 UAV 지원시설을 설치, 각 시설은 사전 정의된 감시 범위 내 노드를 감지.
- 감시되지 못한 노드에는 추가 감지 작업에 따른 penalty 비용 발생.
- 시설 설치 비용 + UAV 운영 비용 + 미감지 노드 penalty 비용을 동시에 고려하는 강건 최적화 모형.
- 조합 최적화 문제의 높은 계산 복잡도 해결을 위해 가변 이웃 탐색(Variable Neighborhood Search) 기반
  휴리스틱 알고리즘을 개발.

## 관련 개념

- [[ops-mission]] — 드론 운용/미션 도메인 개요(DFR/배송/검사/재난대응)
- [[drone-power-battery]] — 충전 인프라를 포함한 드론 전력/배터리 운용
- [[swarm-coordination]] — 다중 드론 협조 운용 구조
