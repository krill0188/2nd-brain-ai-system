---
title: "GNSS-denied Remote Autonomy for SAR Operations"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-sw, gcs-software, gnss-denied, search-rescue]
sources: [raw/papers/drone-sw/gnss-denied-remote-autonomy-sar.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# GNSS-denied Remote Autonomy for SAR Operations

상용 DJI 드론을 활용한 GNSS 차단 환경 수색 구조 자율 비행 시스템. 안드로이드 앱 기반 상태 추정 및 장애물 회피를 리모트 컨트롤러에서 직접 실행.

## 시스템 구성

- **플랫폼**: 경량 상용 DJI 드론
- **온보드 처리**: Android 앱이 리모트 컨트롤러에서 실행
- **지상 통제**: 단일 운용자 다중 이종 UAV 설정/감독
- **환경 모델링**: 모든 UAV 관측을 결합한 통합 3D 환경 모델

## 핵심 기능

- GNSS 차단/구조물 근접 환경 자율 비행
- 상태 추정 및 장애물 회피
- 다중 이종 UAV 동시 감독
- 상황 인식 향상을 위한 공유 3D 모델

## 관련 개념

- [[visual-positioning-odometry]] — GPS 미가용 환경 시각적 위치 추정
- [[drone-first-responder-dfr]] — 응급 대응 드론 활용
- [[ground-control-station]] — GCS 소프트웨어 및 텔레메트리

## 출처

Daniel Schleich et al., "Remote Autonomy for Multiple Small Lowcost UAVs in GNSS-denied Search and Rescue Operations", arXiv:2510.21357, 2025. ^[raw/papers/drone-sw/gnss-denied-remote-autonomy-sar.md]
