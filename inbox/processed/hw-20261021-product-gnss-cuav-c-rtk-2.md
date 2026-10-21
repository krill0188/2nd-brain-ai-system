---
title: "CUAV C-RTK 2 (PPK/RTK module)"
created: 2026-10-21
captured: 2026-10-21
type: product
domain: hardware
category: gnss
manufacturer: CUAV
source: https://ardupilot.org/copter/docs/common-cuav-c-rtk2.html
tags: [drone, hardware, gnss, cuav]
---

# CUAV C-RTK 2 (PPK/RTK module)

## 핵심 사양 (출처 페이지에 적힌 값만)

| 항목 | 값 |
|---|---|
| 지원 위성군 | GPS, GLONASS, Galileo, BeiDou (4 concurrent), QZSS, SBAS |
| 주파수 대역 | GPS L1C/A, L2C; GLONASS L1OF, L2OF; Galileo E1B/C, E5b; BeiDou B1I, B2I; QZSS L1C/A, L2C, L1S; SBAS L1C/A |
| 동시 수신 위성군 수 | 4 (GPS, GLONASS, GALILEO, Beidou) |
| 채널 수 | 184 receiving channels (ZED-F9P) |
| 정밀도 | RTK 수평 0.01 m + 1 ppm / 수직 0.02 m + 1 ppm; GPS 1.5 m (수평) |
| RTK/PPK/PPP | RTK 및 PPK 지원(RAW 저장); PPK base로는 비권장 |
| 갱신율 | RTK up to 20 Hz; RAW up to 25 Hz (기본 5 Hz) |
| TTFF | Cold start 24 s; Aided start 2 s; Re-acquisition 2 s |
| 인터페이스 | DroneCAN; USB Type-C (HS), F9P USB 1, F9P UART 1, 안테나 MMCX 1, Hotshoe 1, Shutter in/out, micro-SD |
| 입력 전압·소비전력 | 4.5 ~ 6 V (소비전력 미확인) |
| 크기·무게 | 56 x 33 x 16.5 mm, 약 39 g |
| 내장 IMU/컴퍼스/듀얼안테나 방위 | ICM20689 가속도/자이로, RM3100 자력계, ICP10111 기압계, STM32H743VIH6 |
| 재밍/스푸핑 완화 | Active CW detection and removal, onboard band pass filter; Advanced anti-spoofing algorithms |
| 동작 온도 | -20 ~ 85 ℃ |
| PX4/ArduPilot 지원 문구 | ArduPilot/PX4 호환(CUAV X7 시리즈와 plug and play) |

## 용도
항공측량용 PPK/RTK 모듈, 카메라 hotshoe·셔터 트리거 지원. 소스는 ArduPilot 문서의 CUAV C-RTK 2 항목.

## 호환·인터페이스
위 표의 인터페이스·펌웨어 행 참조. 페이지에 없는 항목은 "미확인"으로 표기.

## 비고(미확인)
CUAV 공식 사이트의 C-RTK 2 페이지 URL을 찾지 못해(404) ArduPilot 공식 문서를 근거로 사용. 표 15개 항목 중 '미확인' 시작 항목 0개.
