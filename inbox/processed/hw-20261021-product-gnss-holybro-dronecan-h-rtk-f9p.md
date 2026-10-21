---
title: "Holybro DroneCAN H-RTK F9P (Rover / Helical)"
created: 2026-10-21
captured: 2026-10-21
type: product
domain: hardware
category: gnss
manufacturer: Holybro
source: https://holybro.com/products/dronecan-h-rtk-f9p-helical
tags: [drone, hardware, gnss, holybro]
---

# Holybro DroneCAN H-RTK F9P (Rover / Helical)

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군 | BeiDou, Galileo, GLONASS, GPS / QZSS |
| 주파수 대역 | B1I, B2I, E1B/C, E5b, L1C/A, L1OF, L2C, L2OF |
| 동시 수신 위성군 수 | 미확인 |
| 채널 수 | 미확인 |
| 정밀도 | 3D FIX 1.5 m / RTK 0.01 m |
| RTK/PPK/PPP | RTK 지원(PPK 미확인) |
| 갱신율 | RAW 20 Hz max; RTK 8 Hz max; Moving Base RTK 5 Hz max(Helical) |
| TTFF | Rover cold ≤ 29 s / hot ≤ 1 s; Helical cold ≤ 25 s / hot ≤ 1 s |
| 인터페이스 | DroneCAN 1 Mbit/s (CAN 종단저항 소프트웨어 전환 지원); Helical은 UART2 노출(Yaw/Heading용) |
| 입력 전압·소비전력 | 4.75 V ~ 5.25 V; ~250 mA |
| 크기·무게 | Rover: 직경 80 mm x 높이 20 mm, 123 g; Helical: 보드 51.1 x 35 x 22.9 mm, 안테나 직경 27.5 mm x 높이 59 mm, 61.2 g |
| 내장 IMU/컴퍼스/듀얼안테나 방위 | BMM150 또는 IST8310 컴퍼스; STM32G473 프로세서 |
| 재밍/스푸핑 완화 | 미확인 |
| 동작 온도 | -20 ℃ ~ 85 ℃ |
| PX4/ArduPilot 지원 문구 | PX4 1.14, ArduPilot 4.4.4 이후 Status LED 지원 문구; DroneCAN 펌웨어 업그레이드(DroneCAN GUI Tool) |

## 용도
DroneCAN 프로토콜 F9P RTK GPS. Rover(패치 안테나)와 Helical(헬리컬 안테나) 두 모델.

## 호환·인터페이스
위 표의 인터페이스·펌웨어 행 참조. 페이지에 없는 항목은 "미확인"으로 표기.

## 비고(미확인)
특이사항 없음. 표 15개 항목 중 '미확인' 시작 항목 3개.
