---
title: "Holybro H-RTK F9P Series (Rover / Helical / Base, IST8310)"
created: 2026-10-21
captured: 2026-10-21
type: product
domain: hardware
category: gnss
manufacturer: Holybro
source: https://holybro.com/products/h-rtk-f9p-gnss-series
tags: [drone, hardware, gnss, holybro]
---

# Holybro H-RTK F9P Series (Rover / Helical / Base, IST8310)

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군 | GPS, GLONASS, BeiDou, Galileo |
| 주파수 대역 | GPS L1C/A, L2C; GLONASS L1OF, L2OF; BeiDou B1, B2; Galileo E1-B/C, E5b (페이지 표 원문이 일부 깨져 있음) |
| 동시 수신 위성군 수 | 미확인 |
| 채널 수 | 미확인 |
| 정밀도 | 수치 미확인(페이지 표에 정밀도 행 없음; ZED-F9P 일반 사양 참조) |
| RTK/PPK/PPP | RTK 지원; Moving Base RTK 5 Hz max(Helical/Base) |
| 갱신율 | RAW 20 Hz max; RTK 8 Hz max |
| TTFF | Rover: cold ≤ 29 s / hot ≤ 1 s; Helical: cold ≤ 25 s / hot ≤ 1 s; Base: cold ≤ 24 s / hot ≤ 1 s |
| 인터페이스 | Rover: GH1.25 10pin 또는 6pin 케이블; Helical/Base: Port 1 GH1.25 10-pin, Port 2 USB Type-C, Port 3 UART2 (GH1.25 6pin) |
| 입력 전압·소비전력 | 4.75 V ~ 5.25 V; ~250 mA |
| 크기·무게 | Rover: 직경 76 mm x 높이 20 mm, 106 g (IPX6); Helical: 보드 34.8 x 52.7 x 12.9 mm, 안테나 직경 27.5 mm x 높이 59 mm, 49 g; Base: 안테나 직경 152 mm x 높이 62.2 mm, 469 g |
| 내장 IMU/컴퍼스/듀얼안테나 방위 | IST8310 컴퍼스, 안전스위치, 3색 LED; 듀얼안테나 방위는 Moving Baseline 방식(2개 모듈 사용) |
| 재밍/스푸핑 완화 | 재밍/스푸핑 문구 미확인 |
| 동작 온도 | 미확인 |
| PX4/ArduPilot 지원 문구 | PX4 1.14, ArduPilot 4.4.0 이후 LED 드라이버 지원 문구 |

## 용도
u-blox ZED-F9P 기반 H-RTK 시리즈. Rover(항공기 전용), Helical(로버 또는 기지국), Base(기지국 전용)를 한 페이지에서 비교.

## 호환·인터페이스
위 표의 인터페이스·펌웨어 행 참조. 페이지에 없는 항목은 "미확인"으로 표기.

## 비고(미확인)
세 모델이 한 페이지여서 파일 하나로 통합. 기존 H-RTK NEO-F9P(RM3100) 수집분과는 별개 모델. 표 15개 항목 중 '미확인' 시작 항목 3개.
