---
title: "SIYI UniFC 6 PICO 소형 Pixhawk 스타일 비행 컨트롤러"
created: 2026-11-02
updated: 2026-11-02
type: concept
domain: hardware
tags: [drone-hw, hardware]
sources: [inbox/processed/fetch-2026-11-02-yt-first-look-new-compact-siyi-unifc-pico-pixhawk-flight-contro.md]
confidence: low
contested: false
contradictions: []
---

# SIYI UniFC 6 PICO 소형 Pixhawk 스타일 비행 컨트롤러

Painless360의 First Look 영상(2026-11-01) 자막 기준 요약이다. 벤치 셋업만 했고 비행 시험은 하지 않았다고 영상이 밝힌다.^[inbox/processed/fetch-2026-11-02-yt-first-look-new-compact-siyi-unifc-pico-pixhawk-flight-contro.md]

## 사양 (영상 자막)
- **프로세서**: H7 480 MHz, 플래시 3 MB, RAM 1 MB — ArduPilot 전체 기능 구동 가능하다고 설명.
- **센서**: 듀얼 IMU, 기압계, IMU 가열(가열 중 GPS 상태 LED로 표시, 목표 온도 도달 시 녹색).
- **I/O**: PWM 14채널, UART 5개, 이더넷, CAN 2개(하나는 GPS가 사용, 추가 장치는 CAN 노드 필요 — 키트에 포함).
- **크기/무게**: 49 × 42.6 × 16.2 mm, 40 g.
- **펌웨어**: ArduPilot과 PX4 지원, ArduPilot이 선탑재, Mission Planner에서 직접 지원되는 업데이트 제공.
- **가격(영상 언급)**: FC 약 £150, GPS 약 £30~40.

## UniFC GNSS M10 GPS
DroneCAN 연결, BeiDou·GPS·QZSS·GLONASS·Galileo 동시 수신, 내장 IST8310 자력계, 안전 스위치·RGB LED·부저 포함, 13.6 × 50.6 mm 직경, 120 mm GPS 마운트 동봉.

## 셋업 메모
외부 GPS의 DroneCAN(CAN1) 설정과 LED 설정은 공장 출하 시 되어 있지 않아 직접 해야 했다(약 2분). 이후 설정·연결은 다른 Pixhawk 계열과 동일하다.

## 맥락
영상은 SpeedyBee 등이 비운 소형 STM32 호비 FC 시장에 이어 Pixhawk 스타일 FC에서도 신규 벤더 진입이 늘고 있다고 평가한다. 플랫폼 일반 설명은 [[pixhawk]], 펌웨어는 [[ardupilot]]와 [[px4-flight-stack]]을 참조한다.

## 📰 최근 관련 소식
- [Painless360] First Look: New Compact SIYI UniFC PICO 'Pixhawk' flight controller (youtube.com, 2026-11-01) — https://www.youtube.com/watch?v=6TdOrsv4iWo
