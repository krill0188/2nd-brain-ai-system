---
title: "Beitian BN-220 GPS / BN-880 GPS & Compass"
created: 2026-10-21
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: Beitian
source: https://ardupilot.org/copter/docs/common-beitian-gps.html
tags: [drone, hardware, gnss, Beitian, ardupilot-doc]
---

# Beitian BN-220 GPS / BN-880 GPS & Compass

출처 유형: ArduPilot 공식 문서(제조사 페이지가 아님). 제조사 사이트(ardusimple.com 등)는 403/미접근이라 대체. 문서에 적힌 값만 기재.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 수신기 칩 | u-blox M8N 모듈 |
| 지원 위성군 | GPS, GLONASS, Galileo, BeiDou, QZSS, SBAS |
| 주파수 대역 | GPS L1, GLONASS L1, BeiDou B1, SBAS L1, Galileo E1 |
| 채널 수 | 72 |
| 갱신율 | 단일 GNSS 1~18 Hz / 동시 GNSS 1~10 Hz |
| 프로토콜 | NMEA-0183(기본) 또는 UBX |
| 내장 컴퍼스 | BN-880: HMC5883L |
| 재밍/스푸핑 완화 | 미확인 |
| 크기·무게·전력·온도 | 미확인

## 용도
저가 경량 듀얼 모드 GPS 및 GPS/컴퍼스(문서 표현).

## 호환·인터페이스
Pixhawk 표준 JST-GH 6핀 커넥터(문서 기재). ArduPilot 에서 SERIALx_PROTOCOL = 5 의 UART 로 연결, 기본 GPS 파라미터로 동작.

## 비고(미확인)
문서 주의: 백플레인이 작은 BN-220 같은 소형 모듈은 EKF3 사전점검 통과에 필요한 속도·위치 안정화에 오래 걸릴 수 있음. 해결책으로 GPS 뒤에 더 큰 알루미늄 호일 접지판 추가(단락 주의) 또는 대기, EKFx_CHECK_SCALE 상향(Copter 비권장) 서술. L1 전용이라 멀티밴드 아님.
