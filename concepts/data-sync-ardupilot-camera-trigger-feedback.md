---
title: "ArduPilot Copter 문서: Camera Shutter Configuration — 서보/릴레이 트리거와 핫슈 피드백(CAM1_FEEDBAK_PIN) 로깅"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: hardware
tags: [drone, ardupilot, camera-trigger, hotshoe, time-synchronization, cam1-params]
sources: [inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]
confidence: medium
contested: false
contradictions: []
---

# ArduPilot Copter 문서: Camera Shutter Configuration — 서보/릴레이 트리거와 핫슈 피드백(CAM1_FEEDBAK_PIN) 로깅

- 원문: https://ardupilot.org/copter/docs/common-camera-shutter-with-servo.html ; 파라미터 확인 https://ardupilot.org/copter/docs/parameters.html^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]
- 저자: ArduPilot 문서^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]
- 발행: 미확인 (열람일 2026-10-22)^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]

## 핵심 내용
- 요청에 적힌 `CAM_TRIGG_*` 파라미터명은 현재 Copter 파라미터 문서에서 확인되지 않음(문자열 `CAM_TRIGG_TYPE` 부재). 현재 문서는 `CAM1_*` 계열(`CAM1_TYPE`, `CAM1_SERVO_ON/OFF`, `CAM1_DURATION`, `CAM1_RELAY_ON`, `CAM1_TRIGG_DIST`, `CAM1_INTRVAL_MIN`, `CAM1_FEEDBAK_PIN`, `CAM1_FEEDBAK_POL`)를 사용. (구 이름과의 대응 이력은 이 열람에서 미확인.)^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]
- 서보 트리거: `SERVOx_FUNCTION`=10(CameraTrigger), `CAM1_TYPE`=1(Servo), `CAM1_SERVO_ON/OFF`(PWM 예 1300/1100), `CAM1_DURATION`(예 0.1 s). IOMCU 보드는 AUX OUT 1~6 권장.^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]
- 릴레이 트리거(GPIO): 4.6 이상은 임의 릴레이 사용 가능(`RELAY1_FUNCTION`=4 Camera, `RELAY1_PIN`), 4.5 이하는 첫 릴레이만(`RELAY_PIN`). 경고문: GPIO 는 전류 용량 제한.^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]
- 피드백 로깅(동기 관련 핵심): "ArduPilot logs TRIG messages when it triggers the camera." 카메라가 GPIO 출력(플래시 핫슈)을 내면 연결해 "CAM messages at the exact moment that pictures are taken" 을 로그. `CAM1_FEEDBAK_PIN`(핀 번호), `CAM1_FEEDBAK_POL`(핫슈 전압이 촬영 시 low면 0, high면 1). 핫슈 신호 변환기로 Seagull SYNC2 언급.^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 내용만)
- ArduPilot에서 트리거 명령 시각(TRIG)과 실제 촬영 시각(CAM, 핫슈 피드백)이 별도 로그 메시지로 분리됨. 카메라-IMU 정밀 매칭이 목적이면 피드백 핀 배선이 필요.^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]
- 이 문서에는 PX4 같은 VIO 동기 예제(시퀀스 번호 매칭, 컴패니언 시계 오프셋 추정)가 없음.^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]

## 한계·미확인
- 정확도(지연·지터) 수치 없음. 컴패니언 컴퓨터로 타임스탬프를 전달하는 ArduPilot 공식 절차는 이 페이지에 없음(다른 페이지 미조사 = 미확인). 신뢰도 높음(공식 문서).^[inbox/processed/hw-20261022-data-sync-ardupilot-camera-trigger-feedback.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
