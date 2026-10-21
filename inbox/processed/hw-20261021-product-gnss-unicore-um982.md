---
title: "Unicore UM982 (듀얼안테나 포지셔닝·헤딩)"
created: 2026-10-21
captured: 2026-10-21
type: product
domain: hardware
category: gnss
manufacturer: Unicore
source: https://en.unicore.com/products/um982/
tags: [drone, hardware, gnss, unicore]
---

# Unicore UM982 (듀얼안테나 포지셔닝·헤딩)

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군 | GPS, BDS, GLONASS, Galileo, QZSS, SBAS(주안테나) |
| 주파수 대역 | 주안테나: GPS L1C/A, L2C, L2P(Y), L5; BDS B1I, B3I, B1C, B2a, B2b*; GLONASS G1, G2; Galileo E1, E5a, E5b, E6; QZSS L1C/A, L2C, L5, L6; SBAS L1C/A. 보조안테나: GPS L1C/A, L2C; BDS B1I, B3I; GLONASS G1, G2; Galileo E1, E5b; QZSS L1C/A, L1C/B, L2C |
| 동시 수신 위성군 수 | 미확인 |
| 채널 수 | 1408 channels |
| 정밀도 | 단독 H 1.5 m / V 2.5 m; DGPS H 0.4 m / V 0.8 m; PPP H 5 cm / V 10 cm; 헤딩 0.1°/1 m 기선 |
| RTK/PPK/PPP | RTK (RMS) H 0.8 cm + 1 ppm / V 1.5 cm + 1 ppm |
| 갱신율 | 20 Hz (RTK+Heading) |
| TTFF | Cold start < 30 s; 초기화 < 5 s (typical) |
| 인터페이스 | 3 x UART (LVTTL), 1 x SPI*, 1 x I2C*, 1 x CAN* |
| 입력 전압·소비전력 | 미확인 |
| 크기·무게 | 16.0 x 21.0 x 2.6 mm (48 pin LGA), 1.82 ± 0.03 g |
| 내장 IMU/컴퍼스/듀얼안테나 방위 | 듀얼안테나 방위 지원(Dual-RTK engine); IMU 미표기 |
| 재밍/스푸핑 완화 | anti-jamming/anti-spoofing, jamming detection, spoofing detection 문구 |
| 동작 온도 | -40 °C ~ +85 °C |
| PX4/ArduPilot 지원 문구 | 미확인 |

## 용도
듀얼안테나 포지셔닝+헤딩 모듈. 주/보조 안테나로 컴퍼스 대체 용도.

## 호환·인터페이스
위 표의 인터페이스·펌웨어 행 참조. 페이지에 없는 항목은 "미확인"으로 표기.

## 비고(미확인)
특이사항 없음. 표 15개 항목 중 '미확인' 시작 항목 3개.
