---
title: "CUAV FC(X7+/V5+/Nora+) 초기 파라미터 설정"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, hardware, cuav, parameter, setup]
sources: [CUAV 공식 문서 기반 정리]
confidence: medium
contested: false
contradictions: []
domain: hardware
---

# CUAV FC(X7+/V5+/Nora+) 초기 파라미터 설정

CUAV 보드는 **전원 모듈(PMU) 종류에 따라 파라미터가 크게 달라진다**. 총론은 [[fc-vendor-param-guide]] 참조.

## 하드웨어 특징

| | X7+ / X7+ Pro | V5+ | Nora+ |
|---|---|---|---|
| FMU | STM32H743 | STM32F765 | STM32H743 |
| IMU | 3중 (Pro: 진동절연+항온) | 3중 | 3중 |
| 권장 PMU | CAN PMU / PMU 2 Lite | HV_PM (아날로그) | CAN PMU |

## 전원 모듈별 설정 (핵심)

**CAN PMU (DroneCAN 디지털) — X7+/Nora+ 권장**
- PX4: `UAVCAN_ENABLE=2` (센서만) 또는 `3`(센서+ESC), 배율 입력 불필요
- ArduPilot: `CAN_P1_DRIVER=1`, `CAN_D1_PROTOCOL=1`, `BATT_MONITOR=8`(DroneCAN)

**HV_PM 아날로그 (V5+ 동봉 기준)**
- PX4: `BAT1_V_DIV=18.0`, `BAT1_A_PER_V=24.0` (CUAV HV_PM 공식값)
- ArduPilot: `BATT_MONITOR=4`, `BATT_VOLT_MULT=18.0`, `BATT_AMP_PERVLT=24.0`

> ⚠️ CUAV 아날로그 모듈 배율은 Pixhawk 표준 모듈(36.4)과 다르다. 표준값을 그대로 쓰면 전류가 크게 잘못 표시됨.

## 기타 보드 종속 설정

- 펌웨어 타깃: X7+ → `CUAV-X7`(AP)/`cuav_x7pro`(PX4), V5+ → `CUAVv5`/`cuav_v5plus`
- NEO 3 Pro(DroneCAN GPS): CAN 활성 + `GPS_TYPE=9`(AP) — Compass 자동 인식 확인
- C-RTK 9Ps 사용 시: `GPS_TYPE=17/18`(AP, Moving Base 구성) 또는 PX4 `GPS_1_PROTOCOL` 확인
- X7+ Pro 항온 IMU: 이륙 전 히팅 안정화 30~60초 대기 권장 (`SENS_IMU_TEMP` 계열)

## 주의사항

- X7+ 시리얼 포트가 많아(UART×5+) 포트-파라미터 매핑 표를 만들어 관리할 것
- CAN PMU 펌웨어도 자체 업데이트 존재 — 전압 이상 시 PMU 펌웨어부터 확인
- 초기화 후 [[sensor-calibration]] 필수

## 공식 참조

- CUAV 문서: https://doc.cuav.net/
- X7+ 매뉴얼: https://doc.cuav.net/flight-controller/x7/en/
