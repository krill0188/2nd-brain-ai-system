---
title: "Holybro FC(6C/6X/Durandal/Kakute) 초기 파라미터 설정"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, hardware, holybro, parameter, setup]
sources: [Holybro 공식 문서 기반 정리]
confidence: medium
contested: false
contradictions: []
domain: hardware
---

# Holybro FC(6C/6X/Durandal/Kakute) 초기 파라미터 설정

Holybro는 Pixhawk 표준 라인(6C/6X)과 레이싱 라인(Kakute)의 설정 체계가 완전히 다르다. 총론은 [[fc-vendor-param-guide]], 6X/6C 상세는 [[pixhawk-setup-params]] 참조.

## 전원 모듈 라인업별 파라미터

| 모듈 | 방식 | PX4 | ArduPilot |
|---|---|---|---|
| PM02D / PM03D | I2C 디지털 | 자동 인식 (INA226/228) | `BATT_MONITOR=21` |
| PM08-CAN | DroneCAN | `UAVCAN_ENABLE≥2` | `BATT_MONITOR=8` + CAN 활성 |
| PM02 v3 / PM06 / PM07 | 아날로그 | `BAT1_V_DIV=18.0`, `BAT1_A_PER_V=36.4` | `BATT_MONITOR=4`, `MULT=18.0`, `AMP_PERVLT=36.4` |

> PM06/PM07(미니 쿼드용)은 최대 전류 스펙이 다르므로 실측 캘리브레이션(전류계 대조) 권장.

## Durandal (H7 레거시 플래그십)

- 펌웨어 타깃: `Durandal`(AP) / `holybro_durandal-v1`(PX4)
- IMU 항온 히터 내장 — 냉간 시동 시 안정화 대기
- 아날로그 전원 기준 배율은 표준(18.0/36.4)

## Kakute H7 계열 (FPV/소형기)

- **Betaflight 겸용 보드** — ArduPilot/PX4 플래시 시 전용 부트로더 절차 필요 (Betaflight Configurator로 bl.hex 선주입)
- 전원 센서 온보드: `BATT_MONITOR=4` + 보드별 배율 (Kakute H7: `BATT_VOLT_MULT≈11.0`, `BATT_AMP_PERVLT`는 탑재 ESC 스펙 따름 — 4in1 ESC 데이터시트 확인)
- OSD 내장: `OSD_TYPE=1`(AP) 활성 시 아날로그 OSD 사용 가능
- UART가 적으므로 `SERIALx_PROTOCOL` 우선순위 설계 필수 (수신기/GPS/텔레메트리 경합)

## H-RTK GPS 조합

- H-RTK F9P/UM982: `GPS_TYPE=2`(uBlox 자동) 또는 DroneCAN 버전은 CAN 설정
- 듀얼 안테나 헤딩(UM982): `GPS_TYPE=25`(AP, DroneCAN moving base 구성 시 상이) — 콤파스 대체 가능

## 공식 참조

- Holybro 문서 허브: https://docs.holybro.com/
- Kakute ArduPilot 가이드: https://ardupilot.org/copter/docs/common-holybro-kakuteh7.html
