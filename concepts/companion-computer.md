---
title: Companion Computer
created: 2026-08-06
updated: 2026-10-14
type: concept
tags: [drone-hw, drone-sw]
sources: [raw/articles/quad-drone-lab-quad-drone-start.md]
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
| Jetson Nano / Jetson Orin Nano / Raspberry Pi (QUAD 교육용 키트) | PX4 FC와 조합해 사물인식·추적 AI 구동 |

## 연결 방식

- FC ↔ Companion Computer: UART/Ethernet, MAVLink
- Offboard 제어: PX4 offboard mode, ROS2/MAVROS

## 사례: 교육/연구용 자율주행 키트 (2026-10-14 추가)

- 쿼드(QUAD) 드론연구소의 Q250/Q500/Q650/Star-2 키트는 PX4 비행 스택 FC에 Jetson Nano 온보드 컴퓨터를 결합하고, Intel Realsense T265(VIO)·D435i(심도) 같은 non-GPS 비전 카메라를 옵션으로 제공한다.^[raw/articles/quad-drone-lab-quad-drone-start.md]
- Q250 플랫폼은 Jetson Nano, Jetson Orin Nano, Raspberry Pi용 사전 세팅 SD 이미지를 제공해 companion 구성의 초기 세팅 비용을 줄인다. 벤더 문서(제품 소개) 단일 출처라 성능 주장은 검증되지 않았다.^[raw/articles/quad-drone-lab-quad-drone-start.md]

## 관련 개념

- [[flight-controller-hardware]] — FC 하드웨어 개요
- [[px4-offboard-control]] — Offboard 제어 인터페이스
- [[visual-slam-gps-denied-evaluation]] — non-GPS 비전 항법의 Jetson 배포 평가

## 📰 최근 관련 소식
- 임현 유비파이 대표 - 드론쇼 기업이 말하는 ‘신방산’ (포브스코리아, Thu, 27 Au) — https://news.google.com/rss/articles/CBMickFVX3lxTFBzRHdaMWhHN0h4YUlrVFhYSDEtU1BVM1gySHFlVExZSHNkVjBsWU1YaTMtS1dwcHdtSWRHeTJMRll1WEhabUh4dGh2UTNpM1VGOVZ4VzdSa2Q4WnEzeHNYMDFWbHVrNHBDLTJUekhpSW45UQ?oc=5
