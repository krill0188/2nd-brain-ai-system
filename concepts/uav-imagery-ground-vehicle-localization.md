---
title: "UAV 영상 기반 지상차량 시각 위치추정: 참조DB 구축 vs 질의단계 매칭"
created: 2026-09-05
updated: 2026-09-05
type: concept
domain: ops-mission
tags: [drone, ops-mission, ai-autonomy]
sources: [raw/papers/_unclassified/uav-imagery-for-ground-vehicle-visual-localization-reference-database-constructi.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 영상 기반 지상차량 시각 위치추정: 참조DB 구축 vs 질의단계 매칭

GNSS가 차단된 도심 환경에서 무인지상차량(UGV)의 정확한 위치추정은 어렵고, 고정밀지도(HD map)는
구축·유지 비용이 크다. UAV 영상과 지상 영상을 결합한 이미지 기반 참조지도가 저비용 대안으로 연구되어
왔으나, 성능 향상이 "기하학적으로 안정적인 참조 데이터베이스 구축"에서 오는 것인지 "항공-지상 영상
직접 매칭(질의단계)"에서 오는 것인지는 불분명했다. 이 연구는 UAV 영상의 기여를 두 단계로 정량 분해한다
^[raw/papers/_unclassified/uav-imagery-for-ground-vehicle-visual-localization-reference-database-constructi.md].

## 접근 방법

- 4가지 참조 데이터 구성을 비교해 UAV 영상이 참조DB 구축 단계와 질의(query) 매칭 단계 중
  어디에서 더 큰 기여를 하는지 분리 평가.
- 서울시립대 공간정보공학과 정진우 저자, 대한원격탐사학회지 게재.

## 관련 개념

- [[visual-positioning-odometry]] — Visual/Visual-Inertial Odometry 기반 GPS 미가용 위치 추정
- [[gps-uav-imu]] — GPS 미수신 환경 UAV/UGV 위치추정 기법
- [[gnss-denied-remote-autonomy]] — GNSS 차단 환경 원격 자율
