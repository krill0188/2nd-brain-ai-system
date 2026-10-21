---
title: "ArduSimple simpleRTK3B Pro (Septentrio mosaic-X5)"
created: 2026-10-21
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: ArduSimple
source: https://ardupilot.org/copter/docs/common-ardusimple-rtk-gps-simplertk3b-pro.html
tags: [drone, hardware, gnss, ArduSimple, ardupilot-doc]
---

# ArduSimple simpleRTK3B Pro (Septentrio mosaic-X5)

출처 유형: ArduPilot 공식 문서(제조사 페이지가 아님). 제조사 사이트(ardusimple.com 등)는 403/미접근이라 대체. 문서에 적힌 값만 기재.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 수신기 칩 | Septentrio Mosaic-X5 |
| 주파수 대역 | Tripleband: L1, L2, L5 |
| 정밀도 | 'Down to 10 millimeters GPS accuracy' (조건 미기재) |
| 갱신율 | RTK 위치 최대 초당 100회 |
| 재밍/스푸핑 완화 | 'Anti-jamming and anti-spoofing capabilities' 문구 |
| 인터페이스 | JST-GH 6핀: 5V_IN / COM3 RX / COM3 TX / Timepulse 출력 / Event 입력 / GND (모두 3.3 V 로직), XBee 소켓(무선/Bluetooth/WiFi/Ethernet/CAN/L-Band/4G 등 플러그인) |
| 컴퍼스 | 없음(GPS 만 포함, 문서 명시) |
| 채널 수·전력·크기·무게·온도 | 미확인(ArduPilot 문서에 없음)

## 용도
수신기 칩이 mosaic-X5 이므로 칩 단위 사양은 기존 product-gnss-septentrio-mosaic-x5 및 mosaic 하드웨어 매뉴얼 보강 파일 참조.

## 호환·인터페이스
Pixhawk 표준 JST-GH 6핀 커넥터(문서 기재). ArduPilot 에서 SERIALx_PROTOCOL = 5 의 UART 로 연결, 기본 GPS 파라미터로 동작.

## 비고(미확인)
보드 단위 전력·무게·크기는 ArduSimple 공식 데이터시트 미열람.
