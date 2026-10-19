---
title: "다중 UAV 페이로드 운송 제어 (Rao 외, 2022)"
created: 2026-10-19
updated: 2026-10-19
type: concept
domain: flight-control
tags: [drone, swarm, drone-sw]
sources: [inbox/processed/fetch-2026-10-19-arxiv-an-input-output-feedback-linearization-based-exponentially-s.md, inbox/processed/fetch-2026-10-19-arxiv-temporal-waypoint-navigation-of-multi-uav-payload-system-usi.md]
confidence: medium
contested: false
contradictions: []
---

# 다중 UAV 페이로드 운송 제어 (Rao 외)

같은 연구진의 2022년 두 논문. 2-자유도 자기 구형 조인트로 강체 페이로드 프레임에 UAV를 연결한 시스템을 다룬다. 둘 다 초록 기준 요약이다.

## 입출력 피드백 선형화 추적 제어 (arXiv 2207.04375)
- 전체 페이로드-UAV 시스템의 입출력 피드백 선형화 모델과 추력 벡터링 제어를 유도하고, 추적 법칙이 지수 안정임을 이론적으로 보인다.
- 수치 시뮬레이션과 고충실도 Gazebo 실시간 시뮬레이션으로 검증했으며, 외란과 페이로드 질량 불확실성에 강건하다고 보고한다.^[inbox/processed/fetch-2026-10-19-arxiv-an-input-output-feedback-linearization-based-exponentially-s.md]

## STL 시간 사양 웨이포인트 항법 (arXiv 2211.14261)
- 신호 시간 논리(STL) 시간 사양을 고차 시변 제어 장벽 함수(HOCBF)로 처리하고, 피드백 선형화 후 최적화 기반 제어 법칙을 도출한다.
- Gazebo 택배 시나리오로 효용과 실시간 구현 가능성을 시뮬레이션했다. 실기체 시험은 초록에 없다.^[inbox/processed/fetch-2026-10-19-arxiv-temporal-waypoint-navigation-of-multi-uav-payload-system-usi.md]

## 연결
케이블 방식 협동 운송은 [[uav-cable-payload-cooperative-transport-research]], 페이로드 시스템 개요는 [[drone-payload-systems]], 군집 협조는 [[swarm-coordination]] 참조.
