---
title: "Holybro H-RTK Unicore UM982 (Dual Antenna Heading)"
created: 2026-10-21
captured: 2026-10-21
type: product
domain: hardware
category: gnss
manufacturer: Holybro
source: https://holybro.com/products/h-rtk-unicore-um982
tags: [drone, hardware, gnss, holybro]
---

# Holybro H-RTK Unicore UM982 (Dual Antenna Heading)

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군 | GPS, GLONASS, Beidou, Galileo, QZSS |
| 주파수 대역 | BDS B1I/B2I/B3I; GPS L1C/A/L2P(Y)/L2C/L5; GLONASS L1/L2; Galileo E1/E5a/E5b; QZSS L1/L2/L5 |
| 동시 수신 위성군 수 | 미확인 |
| 채널 수 | 미확인 |
| 정밀도 | RTK(RMS) H 0.8 cm + 1 ppm / V 1.5 cm + 1 ppm; DGPS H 0.4 m / V 0.8 m; 단독 H 1.5 m / V 2.5 m; 속도 0.03 m/s; 헤딩 0.1°/1 m 기선 |
| RTK/PPK/PPP | RTK 지원(PPK/PPP 미확인) |
| 갱신율 | 20 Hz Positioning & Heading; 20 Hz Raw |
| TTFF | Cold start ≤ 30 s; Hot start ≤ 5 s; RTK-SurveyIn ≤ 5 min @ 2.0 m CEP |
| 인터페이스 | Port 1 GH1.25 10-pin; Port 2 USB Type-C; Port 3 UART2 (GH1.25 6pin); 기본 baud 230400 5 Hz |
| 입력 전압·소비전력 | 4.75 V ~ 5.25 V; ~350 mA |
| 크기·무게 | 보드 34.8 x 58.9 x 14.4 mm; 안테나 직경 27.5 mm, 높이 59 mm; 40.3 g (안테나 제외) |
| 내장 IMU/컴퍼스/듀얼안테나 방위 | IST8310 컴퍼스 내장; 듀얼안테나 Moving Baseline Yaw(GPS Heading) |
| 재밍/스푸핑 완화 | 재밍/스푸핑 관련 Holybro 페이지 문구 미확인(UM982 칩 자체는 Unicore 페이지 참조) |
| 동작 온도 | 미확인 |
| PX4/ArduPilot 지원 문구 | PX4 1.14 / ArduPilot 4.4.0 이후 Status LED 드라이버 지원 문구; QGC는 UM982를 기지국으로 자동 설정 불가(수동 필요)라고 기재 |

## 용도
UM982 기반 듀얼안테나 RTK GPS, 컴퍼스 대체 방위용. 로버/이동기선 로버/기지국 겸용.

## 호환·인터페이스
위 표의 인터페이스·펌웨어 행 참조. 페이지에 없는 항목은 "미확인"으로 표기.

## 비고(미확인)
특이사항 없음. 표 15개 항목 중 '미확인' 시작 항목 3개.
