---
title: "LoRa 기반 드론 탑재형 복합 대기환경정보 수집·모니터링 시스템 (고유진, 2026)"
created: 2026-10-31
updated: 2026-10-31
type: concept
domain: comms-protocol
tags: [drone, datalink]
sources: [inbox/processed/fetch-2026-10-31-kci-lora-기반-드론-탑재형-복합-대기환경정보-수집-및-모니터링-시스템의-설계-및-구현.md]
confidence: low
contested: false
contradictions: []
---

# LoRa 기반 드론 대기환경 수집·모니터링 시스템

고유진(㈜휴넷가이아)의 스마트미디어저널 2026 논문(KCI 원문 공개). **초록 기준** 요약이며 본문은 확인하지 않았다.^[inbox/processed/fetch-2026-10-31-kci-lora-기반-드론-탑재형-복합-대기환경정보-수집-및-모니터링-시스템의-설계-및-구현.md]

## 시스템
- 드론에 온도·습도·기압·미세먼지·CO₂·VOC·복합가스 센서와 GPS를 탑재한다.
- 센서 값을 전용 데이터로거 PCB에서 통합한 뒤 **LoRa**로 지상부에 실시간 전송한다.
- 별도 통신 인프라가 없는 산업현장·특정 고도에서 대기환경정보를 실시간 수집·저장·모니터링하는 용도다.

## 시험 결과(초록)
- 실내 근거리, 지상 개활지, 드론 비행 조건에서 통신시험을 했다.
- 총 7,200개 패킷 기준 **PRR 96.0~100%**, **평균 RSSI -42~-96 dBm**.
- 대표 환경항목은 기준 측정장비와 비교해 측정 특성을 확인했다(비교 수치는 초록에 없음).

## 관련 문서
텔레메트리 프로토콜은 [[mavlink]], 데이터 표준화 쟁점은 [[drone-data-standardization-three-layer-framework]]를 참조한다.
