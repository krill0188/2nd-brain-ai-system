---
title: "Unicore UM980"
created: 2026-10-21
captured: 2026-10-21
type: product
domain: hardware
category: gnss
manufacturer: Unicore
source: https://en.unicore.com/products/um980/
tags: [drone, hardware, gnss, unicore]
---

# Unicore UM980

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군 | GPS, BDS, GLONASS, Galileo, QZSS, NavIC, SBAS |
| 주파수 대역 | GPS L1C/A, L1C, L2C, L2P(Y), L5; BDS B1I, B3I, B1C, B2a, B2b; GLONASS G1, G2, G3; Galileo E1, E5a, E5b, E6; QZSS L1C/A, L1C, L2C, L5, L6; NavIC L5; SBAS L1C/A |
| 동시 수신 위성군 수 | 미확인 |
| 채널 수 | 1408 channels (NebulasIV) |
| 정밀도 | 단독 H 1.5 m / V 2.5 m (RMS); DGPS H 0.4 m / V 0.8 m; PPP H 5 cm / V 10 cm |
| RTK/PPK/PPP | RTK (RMS) H 0.8 cm + 1 ppm / V 1.5 cm + 1 ppm; PPP(B2b-PPP, E6-HAS, QZSS L6E MADOCA) 지원; PPK 미확인 |
| 갱신율 | 50 Hz |
| TTFF | Cold start < 12 s; 초기화 < 5 s (typical) |
| 인터페이스 | 3 x UART (LVTTL), 1 x SPI*, 1 x I2C*, 1 x CAN* (*특정 펌웨어) |
| 입력 전압·소비전력 | 미확인 |
| 크기·무게 | 17.0 x 22.0 x 2.6 mm (54 pin LGA), 1.88 ± 0.03 g |
| 내장 IMU/컴퍼스/듀얼안테나 방위 | IMU 없음(미표기); Heading2 기술로 방위 정보 제공(듀얼안테나 보드는 UM982) |
| 재밍/스푸핑 완화 | 'Excellent anti-jamming and anti-spoofing capabilities, supporting jamming detection and spoofing detection' |
| 동작 온도 | 작동 -40 °C ~ +85 °C; 보관 -55 °C ~ +95 °C |
| PX4/ArduPilot 지원 문구 | 미확인(PX4/ArduPilot 문구 없음) |

## 용도
고정밀 RTK GNSS 모듈(정밀농업·측량·UAV 용도 분류에 포함).

## 호환·인터페이스
위 표의 인터페이스·펌웨어 행 참조. 페이지에 없는 항목은 "미확인"으로 표기.

## 비고(미확인)
전원 전압·소비전력은 spec 표에 없어 미확인. 표 15개 항목 중 '미확인' 시작 항목 3개.
