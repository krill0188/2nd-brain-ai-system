---
title: "시각 마커 기반 자율 배송 드론 시스템"
created: 2026-09-02
updated: 2026-09-02
type: concept
tags: [drone, ai-autonomy, delivery, computer-vision, ros2]
sources: [inbox/fetch-2026-09-02-kci-시각-마커-탐지를-이용한-자율-배송-드론-시스템-설계.md]
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# 시각 마커 기반 자율 배송 드론 시스템

ROS2 기반 자율 배송 UAV 시스템. 웨이포인트 내비게이션, 목표 지역 도달, 시각적 착륙 마커 탐지, 정밀 착륙 등의 자율 작업 수행이 가능하다.

## 시스템 구성

- **ROS2 기반**: ROS2 프레임워크 위에 구축
- **웨이포인트 내비게이션**: 자동 경로 추적
- **시각적 마커 탐지**: 딥러닝 기반 객체 탐지 모델 온보드 배포
- **정밀 착륙**: 마커 탐지 신뢰도 기반 자동 착륙 절차

## 관련 개념

- [[ros2-drone-integration]] — ROS2 드론 연동
- [[mavsdk]] — MAVLink 기반 드론 제어
- [[mission-planning]] — 미션 계획 및 실행

## 출처

- 예타오, "시각 마커 탐지를 이용한 자율 배송 드론 시스템 설계", 드라이브·컨트롤, 2026
