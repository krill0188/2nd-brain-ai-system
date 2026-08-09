---
title: "FC 제조사별 파라미터 설정 가이드 (총론)"
created: 2026-07-30
updated: 2026-08-10
type: concept
tags: [drone, hardware, flight-control, parameter, setup]
sources: []
confidence: low
contested: false
contradictions: []
domain: hardware
note: "출처는 공식 문서 기반 정리(방법론)이나 raw/ 스냅샷 미보존 — 2026-08-10 프로버넌스 감사에서 발견, 재캡처 필요"
---

# FC 제조사별 파라미터 설정 가이드 (총론)

비행 컨트롤러(FC)는 같은 펌웨어(PX4/ArduPilot)를 써도 **보드마다 반드시 다르게 설정해야 하는 파라미터**가 있다. 제조사별 상세는 [[pixhawk-setup-params]] · [[cuav-setup-params]] · [[holybro-setup-params]] 참조.

## 보드가 바뀌면 반드시 확인할 5가지

| 항목 | PX4 파라미터 | ArduPilot 파라미터 | 이유 |
|---|---|---|---|
| 보드 장착 방향 | `SENS_BOARD_ROT` | `AHRS_ORIENTATION` | FC를 기수 방향과 다르게 장착 시 필수 |
| 전원 모듈 배율 | `BAT1_V_DIV`, `BAT1_A_PER_V` | `BATT_VOLT_MULT`, `BATT_AMP_PERVLT` | 제조사·모듈별 분압비가 전부 다름 |
| IMU 개수/우선순위 | `EKF2_IMU_CTRL`, `CAL_GYROn_*` | `EKF3_IMU_MASK`, `INS_USE*` | 6X는 3중 IMU, 6C는 2중 등 구성 상이 |
| CAN 주변장치 | `UAVCAN_ENABLE` | `CAN_P1_DRIVER`, `CAN_D1_PROTOCOL` | DroneCAN GPS/전원모듈 사용 시 |
| 시리얼 포트 맵 | `SER_TELx_BAUD`, `MAV_x_CONFIG` | `SERIALx_PROTOCOL`, `SERIALx_BAUD` | 보드별 TELEM/GPS 포트 배치가 다름 |

## 제조사별 특징 요약

- **Pixhawk 표준 보드(6X/6C)** — Pixhawk Connector Standard(DS-009) 준수. 전원모듈이 디지털(I2C/CAN)이라 배율 입력 대신 자동 인식되는 경우가 많음. 상세: [[pixhawk-setup-params]]
- **CUAV(X7+/V5+/Nora)** — 자체 CAN PMU 사용 시 `UAVCAN_ENABLE=2` + CUAV 전용 배율. ADC 전원모듈은 CUAV 공식 분압값 필수. 상세: [[cuav-setup-params]]
- **Holybro(Pixhawk 6C/6X, Durandal, Kakute)** — PM02D(디지털)/PM06~07(아날로그) 여부에 따라 배터리 파라미터 계열이 달라짐. Kakute 계열은 Betaflight 겸용 보드라 별도 부트로더 주의. 상세: [[holybro-setup-params]]

## 펌웨어 버전별 파라미터 변화

파라미터 이름 자체가 버전에 따라 바뀐다(예: PX4 v1.14에서 `BAT_` → `BAT1_` 계열 정착). 업그레이드 전 반드시 [[px4-params-by-version]] · [[ardupilot-params-by-version]]에서 변경점을 확인하고, **업그레이드 후 전체 파라미터를 백업본과 diff** 할 것.

## 실무 절차 (권장)

1. 펌웨어 플래시 → 기본값 리셋 (`param reset_all` / Full Parameter Reset)
2. 보드 방향·전원 배율·시리얼 맵 등 보드 종속 파라미터 입력
3. 센서 캘리브레이션 ([[sensor-calibration]])
4. 기체 프레임/모터 설정 → 튜닝 ([[pid-tuning-control]])
5. 전체 파라미터 파일 백업 (QGC/MP → Save to file) — 기체별·버전별 보관

## 공식 참조

- PX4 파라미터 레퍼런스: https://docs.px4.io/main/en/advanced_config/parameter_reference.html
- ArduPilot 전체 파라미터: https://ardupilot.org/copter/docs/parameters.html
