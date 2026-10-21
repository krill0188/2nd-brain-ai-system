---
title: "Emlid Reach M2 RTK GNSS Module for UAV & Drone Mapping"
created: 2026-10-21
captured: 2026-10-21
type: product
domain: hardware
category: gnss
manufacturer: Emlid
source: https://emlid.com/reach/
tags: [drone, hardware, gnss, emlid, ppk]
---

# Emlid Reach M2

출처 유형: 제조사 공식 제품 페이지(emlid.com/reach/; 브라우저 User-Agent 로 curl 시 200, 이전 403 기록과 달리 열림) + 공식 문서 docs.emlid.com/reach/specifications/specs/.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군·신호 | GPS/QZSS L1C/A, L2C; GLONASS L1OF, L2OF; BeiDou B1I, B2I; Galileo E1B/C, E5b |
| 채널 수 | 184 |
| 정밀도 | Static 수평 4 mm + 0.5 ppm / 수직 8 mm + 1 ppm; Kinematic 수평 7 mm + 1 ppm / 수직 14 mm + 1 ppm |
| RTK/PPK/PPP | RTK, PPK (페이지 소개문), 보정 입력 NTRIP·VRS·RTCM3 |
| 갱신율 | GNSS 10 Hz |
| 인터페이스 | USB, UART, Event(카메라 핫슈 동기, 소개문에 microsecond 미만 해상도 기록 서술) |
| 입력 전압·소비전력 | 4.75 ~ 5.5 V (USB 또는 JST-GH), 일반 전류 300 mA @5V; 공식 문서에는 peak 3 A(탭 표기 기준), 안테나 DC bias 3.3 V |
| 크기·무게 | 56.4 x 45.3 x 14.6 mm, 35 g |
| 내장 IMU/컴퍼스/듀얼안테나 방위 | 미확인 |
| 재밍/스푸핑 완화 | 미확인 |
| 동작 온도 | -20 ~ +65 °C |
| 무선·저장 | Wi-Fi 802.11 b/g/n, Bluetooth 4.0/2.1 EDR, LoRa(별매) 868/915 MHz 최대 8 km, 내부 저장 16 GB, 로그 RINEX with events |
| PX4/ArduPilot 지원 문구 | 문서에 "ArduPilot Integration" 항목 존재(내용은 열람 안 함) |

## 용도
UAV PPK 매핑(소개문). 안테나 위상중심 오프셋 L1 30.5 mm / L2 41.8 mm(공식 문서 문구, Reach M2 GNSS antenna).

## 호환·인터페이스
JST-GH 커넥터 4개, 안테나 커넥터 MCX.

## 비고(미확인)
공식 문서 표는 탭(Reach M2 / M+)으로 나뉘어 있고 텍스트 추출로는 어느 값이 M2 인지 순서로만 추정됨: 제품 페이지의 300 mA 와 일치하는 쪽을 M2 로 적었음.
