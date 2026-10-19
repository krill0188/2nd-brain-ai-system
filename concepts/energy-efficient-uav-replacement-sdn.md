---
title: "소프트웨어 정의 UAV 네트워크의 에너지 효율적 UAV 교체 (2025)"
created: 2026-10-19
updated: 2026-10-19
type: concept
domain: rf-datalink-engineering
tags: [drone, datalink, swarm]
sources: [inbox/processed/fetch-2026-10-19-arxiv-energy-efficient-uav-replacement-in-software-defined-uav-net.md]
confidence: medium
contested: false
contradictions: []
---

# 소프트웨어 정의 UAV 네트워크의 UAV 교체

배터리 한계로 UAV를 주기적으로 교체할 때 데이터 흐름 핸드오버를 에너지 효율적으로 관리하는 연구다(arXiv 2504.07500, 2025-04). 초록 기준 요약이다.^[inbox/processed/fetch-2026-10-19-arxiv-energy-efficient-uav-replacement-in-software-defined-uav-net.md]

- UAV와 데이터 흐름에 엄격한 전순서 관계를 두어 정수선형계획(ILP)으로 정식화하고 Gurobi로 최적 핸드오버 스케줄을 구한다.
- 계산 복잡도를 크게 줄이면서 최적에 가까운 성능을 내는 휴리스틱을 제안하고 시뮬레이션으로 확장성을 보였다.

## 연결
교체 계획의 다른 접근은 [[uav-battery-replacement-planner]], 링크 에너지 관점은 [[uav-uplink-energy-efficiency-los]], 통신 개요는 [[datalink-communication]] 참조.
