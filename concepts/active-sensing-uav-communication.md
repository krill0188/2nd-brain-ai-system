---
title: "Active Sensing-Assisted UAV Communications with Jittering"
created: 2026-07-30
updated: 2026-08-10
type: concept
tags: [drone, datalink, comms-protocol, sensing, cellular]
sources: []
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
note: "Raw source not preserved in repo — found during 2026-08-10 provenance audit, needs recapture"
---

# Active Sensing-Assisted UAV Communications with Jittering

UAV 지터링으로 인한 빔 불일치 문제를 해결하기 위한 통합 감지 및 통신(ISAC) 기반 2단계 프레임워크. 통신 중심 및 감지 중심 두 가지 방식으로 AoA(Angle-of-Arrival) 획득 및 통신 성능을 균형 있게 최적화한다.

## 핵심 개념

### 2단계 프레임워크
- **Stage 1 (Sensing)**: 결정적 신호로 AoA 획득 (감지 중심) 또는 가우시안 신호로 AoA 추정 (통신 중심)
- **Stage 2 (Communication)**: 추정된 AoA를 활용한 순수 통신 서비스

### 성능 분석
- **Cramér-Rao Bound**: AoA 추정의 이론적 한계
- **Achievable Rates**: 폐형식 달성 가능 전송률
- **Time Allocation**: 전체 전송률을 최대화하는 최적 시간 할당

### 트레이드오프
- 감지와 통신 품질 간 근본적 트레이드오프
- 높은 전송 전력에서 지터 프리 상한 대비 성능 손실이 0에 수렴

## 관련 페이지

- [[datalink-communication]] — RF, LTE, WiFi 등 드론 데이터링크 기술
- [[mavlink-protocol]] — MAVLink 메시지 구조 및 마이크로서비스
- [[drone-hw]] — 안테나 및 RF 하드웨어

## 출처

- Chen et al., "Active Sensing-assisted UAV Communications with Jittering: Framework and Performance Analysis", arXiv:2606.13036, 2026.

## 📰 최근 관련 소식
- “북한군 드론전 경험, 결정적 위협 아냐”…강건작 안보실 1차장의 ‘결이 다른 생각’ 보니[반도 앨리스] (경향신문, Fri, 07 Au) — https://news.google.com/rss/articles/CBMiWkFVX3lxTE50LTk3NTJxWXBWWmxhOXBmN2hJS3lfQ0haekRtNEtsTnFvekE5RUxBV3M2UW8xZnRTemgzWlo2aUJMWmlXWWlEa2t1Q3RGcDlsS1lBdmIxU0x0QdIBX0FVX3lxTE9qdG41WmdVclVUV3doYUxtLVh2OW80VXdNamstX0VtbHVmNVFrUXVpVmkxczBLa1ZDSXEwYWg5VUR1ak42enNQUDc3SW5LOXdjSFJpbGFrQnF4Z2hTNHNZ?oc=5
