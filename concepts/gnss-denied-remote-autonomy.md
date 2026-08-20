---
title: "GNSS-Denied Remote Autonomy for Small UAVs"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-sw, gcs-software, gnss-denied, autonomy]
sources: [raw/papers/gcs-software/gnss-denied-remote-autonomy.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# GNSS-Denied Remote Autonomy for Small UAVs

소형 상용 DJI 드론을 활용한 GNSS 차단 환경 자율 비행 시스템. Android 앱 기반 상태 추정 및 장애물 회피, 단일 운용자 다중 드론 감독.

## 시스템 구성

### 하드웨어
- 상용 DJI 드론 (소형, 저비용)
- 드론 리모트 컨트롤러 (Android 앱 실행)
- 별도 온보드 컴퓨터 불필요

### 소프트웨어
- Android 기반 상태 추정
- 장애물 회피 알고리즘
- 지상 통제 시스템(GCS)

## 핵심 기능

### 1. 자율 비행
- GNSS 차단 환경에서의 자율 운용
- 구조물 주변 안전 비행
- 훈련된 조종사 불필요

### 2. 다중 드론 감독
- 단일 운용자가 다수 이질적 UAV 설정 및 감독
- 공동 3D 환경 모델 구축
- 상황 인식 향상

## 장점

- 특수 프로그래밍 인터페이스 불필요
- 커스텀 센서 설정 불필요
- 강력한 온보드 컴퓨터 불필요
- 광범위한 배포 가능

## 관련 개념

- [[visual-positioning-odometry]] — GPS 미가용 환경 시각적 위치 추정
- [[decentralized-swarm-gps-denied]] — GPS 차단 환경 분산형 UAV 군집
- [[flight-ready-lidar-inertial-odometry]] — 임베디드 LIO 시스템

## 출처

- Schleich et al., "Remote Autonomy for Multiple Small Lowcost UAVs in GNSS-denied Search and Rescue Operations", arXiv:2510.21357, 2025.
