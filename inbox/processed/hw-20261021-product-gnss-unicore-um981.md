---
title: "Unicore UM981 (RTK/INS)"
created: 2026-10-21
captured: 2026-10-21
type: product
domain: hardware
category: gnss
manufacturer: Unicore
source: https://en.unicore.com/products/um981/
tags: [drone, hardware, gnss, unicore]
---

# Unicore UM981 (RTK/INS)

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군 | GPS, BDS, GLONASS, Galileo, QZSS, NavIC, SBAS |
| 주파수 대역 | GPS L1C/A, L1C, L2C, L2P(Y), L5; BDS B1I, B3I, B1C, B2a, B2b; GLONASS G1, G2, G3; Galileo E1, E5a, E5b, E6; QZSS L1C/A, L1C, L2C, L5, L6; NavIC L5; SBAS L1C/A |
| 동시 수신 위성군 수 | 미확인 |
| 채널 수 | 1408 channels |
| 정밀도 | 단독 H 1.5 m / V 2.5 m; DGPS H 0.4 m / V 0.8 m; PPP H 5 cm / V 10 cm; 자세 Heading 0.3°, Roll 0.2°, Pitch 0.2°; INS 단독 오차 < 이동거리의 5 % |
| RTK/PPK/PPP | RTK (RMS) H 0.8 cm + 1 ppm / V 1.5 cm + 1 ppm |
| 갱신율 | IMU RAW 100 Hz; RTK 50 Hz* |
| TTFF | Cold start < 12 s; 초기화 < 5 s (typical) |
| 인터페이스 | 3 x UART (LVTTL), 1 x I2C*, 1 x SPI*, 1 x CAN* |
| 입력 전압·소비전력 | 미확인 |
| 크기·무게 | 17.0 x 22.0 x 2.6 mm (54 pin LGA), 1.91 g ± 0.03 g |
| 내장 IMU/컴퍼스/듀얼안테나 방위 | IMU 통합(RTK/INS 모듈, IMU 부품 미확인); 자세 정확도 표기 |
| 재밍/스푸핑 완화 | anti-jamming/anti-spoofing 문구 |
| 동작 온도 | -40 °C ~ +85 °C |
| PX4/ArduPilot 지원 문구 | 미확인 |

## 용도
RTK/INS 통합 위치·자세 모듈.

## 호환·인터페이스
위 표의 인터페이스·펌웨어 행 참조. 페이지에 없는 항목은 "미확인"으로 표기.

## 비고(미확인)
특이사항 없음. 표 15개 항목 중 '미확인' 시작 항목 3개.
