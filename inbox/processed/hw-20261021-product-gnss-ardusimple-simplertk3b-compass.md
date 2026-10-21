---
title: "ArduSimple simpleRTK3B Compass (Unicore UM982, dual antenna heading)"
created: 2026-10-21
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: ArduSimple
source: https://ardupilot.org/copter/docs/common-ardusimple-rtk-gps-simplertk3b-compass.html
tags: [drone, hardware, gnss, ArduSimple, ardupilot-doc]
---

# ArduSimple simpleRTK3B Compass (Unicore UM982, dual antenna heading)

출처 유형: ArduPilot 공식 문서(제조사 페이지가 아님). 제조사 사이트(ardusimple.com 등)는 403/미접근이라 대체. 문서에 적힌 값만 기재.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 수신기 칩 | Unicore UM982 (듀얼 안테나) |
| 주파수 대역 | Tripleband: L1, L2, L5 |
| 정밀도 | 'Down to 10 millimeters GPS accuracy' / 방위 정확도 기선 1 m 당 0.1° |
| 갱신율 | RTK 위치 최대 초당 50회 |
| 재밍/스푸핑 완화 | 'Basic jamming immunity' 문구 |
| 인터페이스 | JST-GH 6핀: 5V_IN / COM3 RX / COM3 TX / Timepulse / Extint / GND (3.3 V), XBee 소켓 |
| 채널 수·전력·크기·무게·온도 | 미확인

## 용도
듀얼 안테나 GNSS 방위(헤딩) 제공 RTK 보드.

## 호환·인터페이스
Pixhawk 표준 JST-GH 6핀 커넥터(문서 기재). ArduPilot 에서 SERIALx_PROTOCOL = 5 의 UART 로 연결, 기본 GPS 파라미터로 동작.

## 비고(미확인)
방위 정확도 0.1°/m 는 기선 길이에 반비례하는 형태로만 서술됨. 칩 사양은 기존 product-gnss-unicore-um982 참조.
