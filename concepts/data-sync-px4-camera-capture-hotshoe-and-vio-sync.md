---
title: "PX4 문서: 카메라 트리거(TRIG_*)·캡처핀(CAM_CAP_FBACK)과 카메라-IMU(VIO) 동기 예제"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: hardware
ontology_class: TimingLatency
tags: [drone, px4, camera-trigger, camera-capture, time-synchronization, vio, camera-imu, mavros]
sources: [inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
confidence: medium
contested: false
contradictions: []
---

# PX4 문서: 카메라 트리거(TRIG_*)·캡처핀(CAM_CAP_FBACK)과 카메라-IMU(VIO) 동기 예제

- 원문: https://github.com/PX4/PX4-Autopilot/blob/main/docs/en/camera/fc_connected_camera.md ; https://github.com/PX4/PX4-Autopilot/blob/main/docs/en/camera/camera_architecture.md ; https://github.com/PX4/PX4-Autopilot/blob/main/docs/en/msg_docs/CameraCapture.md^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
- 저자: PX4 문서 (PX4-Autopilot main 브랜치 docs/)^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
- 발행: 미확인 (main 브랜치 열람일 2026-10-22)^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]

## 핵심 내용
열람 방법: docs.px4.io 페이지는 1MB 이상 HTML 이라 GitHub raw 원본(docs/en/camera/)을 직접 읽음(구 PX4-user_guide 저장소 경로는 404 = 문서가 PX4-Autopilot 저장소로 이전됨).^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
- 하드웨어 동기 경로: 카메라 트리거를 비행 컨트롤러(FC) 출력으로 구동. `TRIG_MODE`(4개 모드), `TRIG_INTERFACE` 1 = GPIO(AUX 출력을 `TRIG_INTERVAL`마다 펄스, "most standard machine vision cameras" 직접 트리거 가능, PX4FMU 계열 AUX 신호 3.3 V), 2 = Seagull MAP2 등. `TRIG_POLARITY`, `TRIG_INTERVAL`(ms), `TRIG_ACT_TIME`(ms; PWM 모드는 최소 40 ms).^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
- 트리거 시각 보고: 트리거마다 MAVLink `CAMERA_TRIGGER`(이미지 시퀀스 번호 + 타임스탬프) 발행. 문서가 용도로 직접 든 것: "synchronising a multi-camera system or visual-inertial navigation".^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
- 캡처핀(핫슈 피드백): 카메라 핫슈 신호를 FC 캡처 핀에 연결하면 "exact moment" 기록 가능. `CAM_CAP_FBACK = 1` 로 활성화, 액추에이터 설정에서 `Camera_Capture` 기능을 FMU 출력에 할당, 상승 에지(Pixhawk 3.3 V) 검출. 캡처가 설정되면 `CAMERA_TRIGGER` 의 타임스탬프는 캡처 드라이버 값, 아니면 트리거 시각. 문서 문구: 지오태깅 정밀도 향상과 "the right IMU sample for VIO synchronization". 현재 FMU 핀에서만 캡처 동작("At time of writing").^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
- uORB `CameraCapture`: timestamp(부팅 후 마이크로초), timestamp_utc, seq, 위치·자세 필드, `result`(1 성공/0 실패/-1 카메라 피드백 없음). 이 토픽은 항상 로그에 기록.^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
- VIO 예제(문서 섹션 "Camera-IMU sync example (VIO)"): 목적은 "IMU 측정을 사진과 정확히 같은 시각에 찍는 것이 아니라 이미지에 올바른 타임스탬프를 주는 것". FC(부팅 시간 기준)와 컴패니언(UNIX epoch) 시계가 달라 시계를 보정하지 않고 오프셋을 관측해 MAVLink 메시지(HIGHRES_IMU 등) 타임스탬프에 가감; 알고리즘은 NTP 변형 + 지수이동평균 평활, MAVROS 고대역 링크(onboard 모드)에서 자동 수행. 이미지는 `CAMERA_TRIGGER` 시퀀스 번호로 매칭해 노출 시작 시점의 IMU 타임스탬프를 부여. 예: Point Grey Firefly MV 30 FPS 기준 `TRIG_INTERVAL` 33.33 ms, `TRIG_POLARITY` 0(active low), `TRIG_ACT_TIME` 0.5 ms, `TRIG_MODE` 1(명령 제어). 참조 구현 저장소로 ueye_cam, camera1394 언급.^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
- Camera Protocol v2 MAVLink 카메라는 트리거 이벤트가 PX4 안에서 생성되지 않아 캡처 이벤트 로그 없음(camera_architecture 문서).^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 내용만)
- 하드웨어 트리거 + 시퀀스 번호 매칭 + 시계 오프셋 추정(NTP 변형)의 3요소가 PX4 문서가 제시한 동기 구성. 수 ms 급 정확도 수치는 이 문서에 없음.^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]
- 캡처핀을 쓰면 FC가 "실제 노출" 신호를 받아 시각을 기록(트리거 명령 시각과 분리).^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]

## 한계·미확인
- 정량 지연·지터(마이크로초/밀리초) 수치 없음. 예제는 구형 카메라(Firefly MV)·ROS1 MAVROS 기반이며 최신 uXRCE-DDS/ROS 2 경로의 동등 절차는 이 문서에서 미확인. 카메라 소프트웨어 타임스탬프 대비 정량 비교는 없음 → 직접 비교 근거로는 불충분(conv-camera-imu-sync-hw-vs-sw-evidence 참조). 신뢰도 높음(공식 문서), 정확도 주장은 없음.^[inbox/processed/hw-20261022-data-sync-px4-camera-capture-hotshoe-and-vio-sync.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
