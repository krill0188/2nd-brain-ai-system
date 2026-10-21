---
title: "ArduSimple simpleRTK 4 Optimum (u-blox ZED-X20P)"
created: 2026-10-21
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: ArduSimple
source: https://ardupilot.org/copter/docs/common-ardusimple-rtk-gps-simplertk-4-optimum.html
tags: [drone, hardware, gnss, ArduSimple, ardupilot-doc]
---

# ArduSimple simpleRTK 4 Optimum (u-blox ZED-X20P)

출처 유형: ArduPilot 공식 문서(제조사 페이지가 아님). 제조사 사이트(ardusimple.com 등)는 403/미접근이라 대체. 문서에 적힌 값만 기재.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 수신기 칩 | u-blox ZED-X20P |
| 주파수 대역 | Allband: L1, L2, L5, L6 (Galileo HAS 지원 표기) |
| 정밀도 | 'Down to centimeter GPS accuracy' |
| 갱신율 | RTK 위치 최대 초당 20회 |
| 인터페이스 | JST-GH 6핀: 5V_IN / UART1 RX / TX / Timepulse / Event / GND (3.3 V), XBee 소켓 |
| 재밍/스푸핑 완화 | 미확인 |
| 채널 수·전력·크기·무게·온도 | 미확인

## 용도
모든 주요 위성군과 L1/L2/L5/L6 대역 지원(문서 표현), 도전적 환경용으로 소개.

## 호환·인터페이스
Pixhawk 표준 JST-GH 6핀 커넥터(문서 기재). ArduPilot 에서 SERIALx_PROTOCOL = 5 의 UART 로 연결, 기본 GPS 파라미터로 동작.

## 비고(미확인)
칩 사양은 기존 product-gnss-ublox-zed-x20p 참조.
