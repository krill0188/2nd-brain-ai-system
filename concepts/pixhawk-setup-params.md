---
title: "Pixhawk 6X/6C 초기 파라미터 설정"
created: 2026-07-30
updated: 2026-08-10
type: concept
tags: [drone, hardware, pixhawk, parameter, setup]
sources: []
confidence: low
contested: false
contradictions: []
domain: hardware
note: "출처는 Pixhawk 표준(DS-009)·Holybro 문서 기반 정리(방법론)이나 raw/ 스냅샷 미보존 — 2026-08-10 프로버넌스 감사에서 발견, 재캡처 필요"
---

# Pixhawk 6X/6C 초기 파라미터 설정

Pixhawk 표준 보드(FMUv6X/FMUv6C)를 PX4/ArduPilot에서 처음 세팅할 때의 보드 종속 파라미터. 총론은 [[fc-vendor-param-guide]], 버전별 변경은 [[px4-params-by-version]] 참조.

## 하드웨어 특징 (파라미터에 영향)

| | Pixhawk 6X | Pixhawk 6C |
|---|---|---|
| FMU | STM32H753 | STM32H743 |
| IMU | 3중 (ICM-20649/42688-P/42670-P) | 2중 (ICM-42688-P/BMI055) |
| 기압계 | 2중 | 1개 |
| 전원 | PM02D/PM03D (I2C 디지털) | PM02 v3 (아날로그) 또는 PM02D |

## PX4 필수 설정

- 전원(디지털 PM02D/PM03D): 자동 인식 — `SENS_EN_INA226=1` 확인, 배율 입력 불필요
- 전원(아날로그 PM02): `BAT1_V_DIV=18.0`, `BAT1_A_PER_V=36.4` (모듈 동봉 라벨값 우선)
- 장착 방향이 정방향이 아니면 `SENS_BOARD_ROT` 설정
- 3중 IMU 활용: 기본 활성 — 진동 심한 기체는 `IMU_GYRO_RATEMAX` 상향 검토
- TELEM1 텔레메트리: `MAV_0_CONFIG=101`, `SER_TEL1_BAUD=57600` (SiK 라디오 기준)

## ArduPilot 필수 설정

- 보드 인식: 최신 4.5+ 는 FMUv6X/6C 타깃 펌웨어 사용 (`Pixhawk6X`, `Pixhawk6C`)
- 아날로그 전원모듈: `BATT_MONITOR=4`, `BATT_VOLT_MULT≈18.0`, `BATT_AMP_PERVLT≈36.4`
- 디지털(PM02D): `BATT_MONITOR=21`(INA2xx I2C)
- 방향: `AHRS_ORIENTATION=0`(정방향 기준)
- DroneCAN GPS 사용 시: `CAN_P1_DRIVER=1`, `CAN_D1_PROTOCOL=1`, `GPS_TYPE=9`

## 주의사항

- 6X의 IMU는 진동 절연 마운트 내장 — 추가 소프트마운트 중복 시 오히려 공진 발생 가능
- PWM AUX 핀에서 서보 전원은 공급되지 않음(표준) — 별도 BEC 필요
- 초기화 후 반드시 [[sensor-calibration]] 전 항목 수행

## 공식 참조

- Holybro Pixhawk 6X/6C 문서: https://docs.holybro.com/autopilot/pixhawk-6x
- PX4 하드웨어 문서: https://docs.px4.io/main/en/flight_controller/pixhawk6x.html
