---
title: "mRo Location One GPS (u-blox M9N + RM3100, CAN)"
created: 2026-10-22
captured: 2026-10-22
type: product
domain: hardware
category: gnss
manufacturer: mRobotics (mRo)
source: https://docs.mrobotics.io/gps/location-one.html
tags: [drone, hardware, gnss, mro, m9n, rm3100, dronecan]
---

# mRo Location One GPS (u-blox M9N + RM3100, CAN)

출처 유형: mRobotics 공식 사용자 문서(docs.mrobotics.io). 페이지에 'Unmaintained site notice. Information may be outdated' 경고가 있어 최신 정보가 아닐 수 있음.

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| GNSS 칩 | u-blox M9N |
| 지원 위성군 | GPS, GLONASS, Galileo, BeiDou |
| 컴퍼스 | RM3100 |
| RTK | No |
| CAN | Yes (APPeriph firmware, CAN 2포트 4-pin JST-GH) |
| USB | Type-C |
| 접지판 | 50 mm x 50 mm |
| 크기·무게 | 50 x 50 x 7 mm, 20.26 g |
| 동작 온도 | -20 ~ 80 C |
| 마운트 홀 | 3.2 mm |
| 설계 포인트 | GPS 엔진 전용 3.3 V 레귤레이터, GPS/기타 접지 분리, 컴퍼스 코일을 보드 밖으로 돌출시켜 접지판 유지(제조사 서술) |
| ArduPilot 설정 | CAN_P1_DRIVER, GPS_TYPE=9 (UAVCAN) 등 |

## 용도
페이지 문구: CAN 기반 GNSS+컴퍼스, 패치 안테나는 적절한 접지판이 필요하다는 설명 포함.

## 호환·인터페이스
DroneCAN 호환 플랫폼.

## 비고(미확인)
정확도·TTFF·전력 미확인.
