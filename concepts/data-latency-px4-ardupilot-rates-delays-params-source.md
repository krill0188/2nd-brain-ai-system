---
title: "PX4 and ArduPilot source docs: control loop rates, EKF delay parameter defaults, offboard timeout"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
tags: [drone, control-loop, latency, px4, ardupilot, ekf2, ekf3, parameters]
sources: [inbox/processed/hw-20261021-data-latency-px4-ardupilot-rates-delays-params-source.md]
confidence: medium
contested: false
contradictions: []
---

# PX4 and ArduPilot source docs: control loop rates, EKF delay parameter defaults, offboard timeout

- 원문: https://github.com/PX4/PX4-Autopilot/blob/main/docs/en/advanced_config/parameter_reference.md ; https://github.com/PX4/PX4-Autopilot/blob/main/docs/en/concept/architecture.md ; https://github.com/PX4/PX4-Autopilot/blob/main/docs/en/advanced_config/tuning_the_ecl_ekf.md ; https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_NavEKF3/AP_NavEKF3.cpp ; https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scheduler/AP_Scheduler.cpp^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-rates-delays-params-source.md]
- 저자: PX4 / ArduPilot (GitHub 소스, docs main/master 브랜치 2026-10-22 열람)^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-rates-delays-params-source.md]
- 발행: 미확인 (브랜치 최신본)^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-rates-delays-params-source.md]

## 핵심 내용
기존 data-latency-px4-ardupilot-loop-rates-official.md 에서 "미확인"이던 기본값을 GitHub 원본에서 직접 읽어 채움. 표의 값은 모두 파라미터 정의에 적힌 default 그대로.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-rates-delays-params-source.md]

### PX4 (docs/en main 브랜치)
| 항목 | 값 | 출처 파일 |
|---|---|---|
| IMU_GYRO_RATEMAX (레이트 컨트롤러·출력의 루프 주기) | default 400 Hz (선택지 100/250/400/800/1000/2000) | parameter_reference.md |
| 설명 | "This is the loop rate for the rate controller and outputs"; 센서는 항상 원시 주기로 읽고 필터링 | 같음 |
| IMU_INTEG_RATE | default 200 Hz (100~1000) | 같음 |
| EKF2_PREDICT_US | default 10000 us (=10 ms, 범위 1000~20000) | 같음 |
| IMU 드라이버 | "sample the data at 1kHz, integrate it and publish with 250Hz" | architecture.md |
| EKF2_BARO_DELAY | default 0 ms (0~300) | parameter_reference.md |
| EKF2_MAG_DELAY | default 0 ms (0~300) | 같음 |
| SENS_GNSS0_DELAY | default 110 ms (0~300), 드라이버가 timestamp_sample 보정을 안 줄 때만 적용 | 같음 |
| EKF2_EV_DELAY (외부 비전) | default 0 ms | 같음 |
| EKF2_RNG_DELAY | default 5 ms | 같음 |
| EKF2_OF_DELAY (광류) | default 7 ms | 같음 |
| EKF2_ASP_DELAY / EKF2_AVEL_DELAY | 100 ms / 5 ms | 같음 |
| EKF2_DELAY_MAX | default 200 ms (0~1000), "at least as large as the largest EKF2_XXX_DELAY" | 같음 |
| COM_OF_LOSS_T (오프보드 손실 타임아웃) | default 1.0 s (0~60) | 같음 |
| COM_OBL_RC_ACT 기본 동작 | default 0 = Position mode (선택지 0~7) | 같음 |
| 오프보드 하트비트 | "continuous 2Hz proof of life signal" 필요 | offboard.md |
| EKF 최소 입력률 | IMU 100 Hz 이상, 자력계 5 Hz 이상, 고도원 5 Hz 이상 | tuning_the_ecl_ekf.md |

### ArduPilot (소스 master)
| 항목 | 값 | 출처 |
|---|---|---|
| SCHED_LOOP_RATE 기본 | Copter/Heli/Sub 400 Hz, 그 외 기체 50 Hz (범위 50~400, "Values over 400 are considered highly experimental") | AP_Scheduler.cpp |
| EK3_HGT_DELAY | default 60 ms (0~250) | AP_NavEKF3.cpp |
| EK3_FLOW_DELAY | default 10 ms (FLOW_MEAS_DELAY), 센서 내부 100 ms 평균 지연 별도 | AP_NavEKF3.cpp |
| EK3_BCN_DELAY | default 50 ms | AP_NavEKF3.cpp |
| GPS _DELAY_MS | 0 = "use the default delay for the detected GPS type" (범위 0~250); EKF3 자체 GPS_DELAY 파라미터는 폐지(소스 주석) | AP_GPS.cpp, AP_NavEKF3.cpp |

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 컴패니언이 외부 비전(EKF2_EV_DELAY)을 주입하면 기본 0 ms이므로 실제 카메라 처리 지연을 이 값에 반영하고 EKF2_DELAY_MAX(기본 200 ms)가 그보다 크게 유지.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-rates-delays-params-source.md]
- 오프보드 제어는 2 Hz 이상 유지, 끊기면 기본 1.0 s 후 Position mode 동작(기본 설정).^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-rates-delays-params-source.md]
- 레이트 루프 400 Hz(PX4 기본)와 EKF 갱신 10 ms는 AI 추론 주기(수십 ms 이상)와 분리된 하위 루프.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-rates-delays-params-source.md]

## 한계·미확인
- PX4 레이트 컨트롤러가 실제 실행되는 주기와 자세 컨트롤러 주기의 별도 공식 표는 열람하지 못함(IMU_GYRO_RATEMAX 설명에서 레이트 컨트롤러 주기만 확인). PX4 EKF2의 GNSS 지연은 EKF2_* 이 아니라 SENS_GNSS0_DELAY로 노출됨. ArduPilot 자세/위치 컨트롤러별 주기와 EK3 자력계·GPS 지연 기본 숫자는 미확인(GPS는 타입별 코드 내부값).^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-rates-delays-params-source.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[px4-offboard-control]]
