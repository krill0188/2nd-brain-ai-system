---
title: Drone Hardware Overview
created: 2026-08-06
updated: 2026-08-06
type: concept
tags: [drone-hw]
sources: []
confidence: medium
contested: false
contradictions: []
domain: hardware
---

# Drone Hardware Overview

드론 하드웨어 스택 전반을 아우르는 도메인 개요 페이지. Flight Controller, 센서, 모터/ESC, 배터리, 통신, 페이로드 등 물리적 구성요소를 다룬다. 세부 항목은 각 하위 개념 페이지를 참조한다.

## 구성 레이어

| 레이어 | 대표 구성요소 |
|---|---|
| 비행 제어 | Flight Controller(Pixhawk 계열), IMU, 바로미터, GPS/RTK |
| 동력 | BLDC 모터, ESC, LiPo 배터리, PDB |
| 통신 | RC 수신기, 텔레메트리 라디오, 데이터링크 |
| 컴퓨팅 확장 | 컴패니언 컴퓨터(Jetson, RPi) |
| 페이로드 | 카메라, 짐벌, 센서 페이로드 |

## 관련 개념

- [[flight-controller-hardware]] — FC/센서/전원 등 하드웨어 상세 레퍼런스
- [[companion-computer]] — AI 추론·오프보드 처리용 보조 컴퓨터
- [[px4-system-architecture]] — FC 소프트웨어와 하드웨어의 결합 구조
