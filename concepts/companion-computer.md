---
title: Companion Computer
created: 2026-08-06
updated: 2026-08-06
type: concept
tags: [drone-hw, drone-sw]
sources: []
confidence: medium
contested: false
contradictions: []
domain: hardware
---

# Companion Computer

Flight Controller와 별도로 탑재되어 AI 추론·영상처리·미션 계획 등 고연산 작업을 오프로드하는 보조 컴퓨터. FC와는 시리얼(UART)이나 이더넷으로 연결되며, MAVLink 또는 PX4 ROS2 offboard 인터페이스로 비행 명령을 전달한다.

## 대표 하드웨어

| 모델 | 용도 |
|---|---|
| NVIDIA Jetson Orin Nano | YOLO 등 온보드 AI 추론 |
| Raspberry Pi 5 | 경량 처리, 통신 게이트웨이 |
| Holybro Jetson Baseboard | Jetson 전용 FC 결합 캐리어 |

## 연결 방식

- FC ↔ Companion Computer: UART/Ethernet, MAVLink
- Offboard 제어: PX4 offboard mode, ROS2/MAVROS

## 관련 개념

- [[flight-controller-hardware]] — FC 하드웨어 개요
- [[px4-offboard-control]] — Offboard 제어 인터페이스
