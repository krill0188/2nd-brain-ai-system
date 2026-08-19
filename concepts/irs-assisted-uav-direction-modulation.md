---
title: "IRS-Assisted UAV Direction Modulation"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, datalink, irs, security, beamforming]
sources: [inbox/fetch-2026-08-19-arxiv-direction-modulation-design-for-uav-assisted-by-irs-with-dis.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# IRS 지원 UAV 방향 변조

## 개요

지능형 반사 표면(IRS)을 활용한 방향 변조(DM) 방안. 불연속 위상 시프트를 통한 UAV 보안 통신 전송률 극대화.

## 핵심 메커니즘

### IRS 지원 방향 변조
- 합법적 사용자 위치에서 별자리 패턴 유지
- 도청자 위치에서 별자리 패턴 왜곡

### 최적화 문제
- 디지털 가중 계수
- UAV 위치
- IRS 불연속 위상 시프트

## 제안 알고리즘

### 1. 전력 최소화를 통한 최적화
- 디지털 가중 벡터 및 UAV 위치 최적화

### 2. IRS 위상 시프트 최적화
- **VT (Vector Trajectory) 방법**
- **CE-VT (Cross Entropy Vector Trajectory)**
- **BCD-VT (Block Coordinate Descent Vector Trajectory)**

## 성능 개선

- 기존 CE 및 BCD 방법 대비 전송률 성능 향상
- IRS 지원 UAV 통신의 효과성 검증

## 관련 개념

- [[isac-uav-security]] — ISAC-UAV 시스템 보안
- [[fluid-antenna-system]] — 유동 안테나 시스템
- [[hybrid-beamforming-ntn]] — NTN 하이브리드 빔포밍

## 참고

Maolin Li et al., arXiv:2410.04709 (2024)
