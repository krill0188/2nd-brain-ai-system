---
title: "PX4 / ArduPilot official docs: loop rates, offboard streaming and EKF2 delay compensation"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: flight-control
ontology_class: TimingLatency
tags: [drone, control-loop, latency, px4, ardupilot, offboard, ekf2]
sources: [inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
confidence: medium
contested: false
contradictions: []
---

# PX4 / ArduPilot official docs: loop rates, offboard streaming and EKF2 delay compensation

- 원문: https://docs.px4.io/main/en/flight_modes/offboard.html ; https://docs.px4.io/main/en/ros2/offboard_control.html ; https://docs.px4.io/main/en/concept/architecture.html ; https://docs.px4.io/main/en/advanced_config/tuning_the_ecl_ekf.html ; https://ardupilot.org/dev/docs/code-overview-scheduling-your-new-code-to-run-intermittently.html^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- 저자: PX4 / ArduPilot documentation^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- 발행: 미확인 (문서 버전 main)^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]

## 핵심 내용
PX4/ArduPilot 공식 문서에서 확인한 제어·통신 주기 관련 서술만 정리한다. 두 문서 모두 컴패니언 컴퓨터의 AI 추론 지연에 대한 명시적 지연 예산(ms)은 제시하지 않는다.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- PX4 Offboard: 외부 컨트롤러가 "continuous 2Hz proof of life signal"을 보내야 함(MAVLink 설정점 또는 ROS 2 `OffboardControlMode`). 끊기면 `COM_OF_LOSS_T` 타임아웃 후 `COM_OBL_RC_ACT` 동작. 스트림은 arm/모드 전환 전에 이미 흐르고 있어야 함.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- ROS 2 Offboard 예제: 100ms 타이머(약 10 Hz)로 송신, "PX4 will switch out of offboard mode if the stream rate of OffboardControlMode messages drops below approximately 2Hz". 페이지는 ROS 2 경로에서 MAVLink와 달리 설정점이 정기적으로 안 오면 failsafe를 발동하지 않는다고 명시.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- PX4 아키텍처: "Most of the IMU drivers sample the data at 1kHz, integrate it and publish with 250Hz."^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- EKF2: 센서별 지연은 EKF2_*_DELAY, 지연된 "fusion time horizon"은 EKF2_DELAY_MAX("at least as large as the longest delay"). 센서 데이터는 FIFO 버퍼로 보관. 최소 센서율: IMU 100 Hz 이상, 자력계 5 Hz 이상, 고도원 5 Hz 이상.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- ArduPilot Copter: fast_loop는 "100Hz on APM2, 400Hz on Pixhawk"; 스케줄러 기본 틱 2.5 ms, 50 Hz/10 Hz/3.3 Hz/1 Hz 루프가 별도 존재.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- AI 추론 결과를 Offboard 설정점으로 보낼 때 추론이 느려도 스트림은 2 Hz 이상 유지(필요 시 마지막 설정점 재전송). PX4 ROS 2 경로는 자동 failsafe가 없으므로 컴패니언 쪽 감시 필요.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- 비전 측정에는 지연 보정 파라미터(EKF2_*_DELAY)로 실제 지연을 반영하고 EKF2_DELAY_MAX를 최대 지연 이상으로 설정.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- 컴패니언 → FC 계층은 250 Hz(PX4 IMU 발행)/400 Hz(ArduPilot fast loop)보다 훨씬 느린 제어 계층으로 설계.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]

## 한계·미확인
- 제어 루프(레이트/자세 컨트롤러) 주기의 공식 수치, EKF2 갱신 주기, EKF2_*_DELAY 기본값, COM_OF_LOSS_T 기본값은 페이지 추출본에서 미확인(페이지 일부 미열람, 길이 한도).^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]
- MAVLink/uXRCE-DDS 전송 지연 수치는 공식 문서에서 미확인.^[inbox/processed/hw-20261021-data-latency-px4-ardupilot-loop-rates-official.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[px4-offboard-control]]
