---
title: "ArduSimple simpleRTK2B Budget (u-blox ZED-F9P)"
created: 2026-10-21
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: ArduSimple
source: https://ardupilot.org/copter/docs/common-ardusimple-rtk-gps-simplertk2b-budget.html
tags: [drone, hardware, gnss, ArduSimple, ardupilot-doc]
---

# ArduSimple simpleRTK2B Budget (u-blox ZED-F9P)

출처 유형: ArduPilot 공식 문서(제조사 페이지가 아님). 제조사 사이트(ardusimple.com 등)는 403/미접근이라 대체. 문서에 적힌 값만 기재.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 수신기 칩 | u-blox ZED-F9P |
| 주파수 대역 | Multiband: L1, L2, E5b |
| 정밀도 | 'Down to centimeter GPS accuracy' |
| 갱신율 | RTK 위치 최대 초당 10회 |
| 인터페이스 | JST-GH 6핀: 5V_IN / ZED-F9P UART1 RX / TX / 4,5 미연결 / GND (3.3 V), XBee 소켓(고출력 XLR 무선·4G NTRIP Master 는 비호환, simpleRTK2B Pro 권장 문구) |
| 재밍/스푸핑 완화 | 미확인 |
| 채널 수·전력·크기·무게·온도 | 미확인

## 용도
저가형 ZED-F9P 기반 RTK 보드.

## 호환·인터페이스
Pixhawk 표준 JST-GH 6핀 커넥터(문서 기재). ArduPilot 에서 SERIALx_PROTOCOL = 5 의 UART 로 연결, 기본 GPS 파라미터로 동작.

## 비고(미확인)
ZED-F9P 칩 사양은 이번에 직접 확인하지 않음.
