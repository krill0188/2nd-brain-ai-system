---
title: "Online Temporal Calibration for Monocular Visual-Inertial Systems"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, time-synchronization, camera-imu, kalibr, vins-mono, time-offset, hardware-sync]
sources: [inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]
confidence: medium
contested: false
contradictions: []
---

# Online Temporal Calibration for Monocular Visual-Inertial Systems

- 원문: https://arxiv.org/abs/1808.00692 (PDF 본문 열람)^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]
- 저자: Tong Qin, Shaojie Shen^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]
- 발행: 2018-08-02^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]

## 핵심 내용 (arXiv PDF 본문)
- 문제 서술: 대부분의 VIO는 "strictly hardware-synchronized" 센서 세트를 가정하나, 저가·자체 조립 센서에서는 하드웨어 동기가 없어 triggering·transmission 지연으로 시간 오프셋이 생김. 본문: "The time offset usually ranges from several milliseconds to hundreds of milliseconds."^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]
- 제안: 시간 오프셋을 상수 미지수로 보고 SLAM 최적화에서 카메라/IMU 상태·특징점과 함께 공동 추정(VINS-Mono에 통합).^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]
- 시뮬레이션(IMU 100 Hz, 카메라 10 Hz, 시험 100회): 설정 오프셋 5/15/30 ms에 대해 추정 평균 5.12/15.06/30.17 ms, RMSE 0.36/0.61/0.68 ms.^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]
- 실센서: Intel RealSense ZR300(제조사가 "well synchronized"라 주장)에서도 기본 SDK 기준 카메라-IMU 간 뚜렷한 오프셋이 있고 노출 시간에 따라 변함. 노출 20~30 ms 5단계에서 오프셋이 노출시간에 선형(기울기 약 0.5) -> 오프셋 = 고정 통신·트리거 지연 + 노출시간 절반. Kalibr(오프라인 배치, 체커보드 필요)를 기준으로 비교해 결과가 가깝고, 표준편차는 제안법 [0.095, 0.071, 0.14, 0.16, 0.15] vs Kalibr [0.27, 0.16, 0.13, 0.18, 0.20](ms).^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]
- EuRoC MH03에서 IMU 타임스탬프를 -40~40 ms 인위 이동: 오프셋 보정이 없는 VINS-Mono는 RMSE가 포물선으로 악화되며 "The tolerance interval is only within 6 milliseconds". 제안법은 오프셋과 무관하게 RMSE 일정. 표 II: 예) MH01 오프셋 5ms에서 제안 0.155 m vs OKVIS 0.318 m; V1 03 오프셋 30 ms에서 0.162 m vs 1.010 m.^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]

## 설계에 쓸 수 있는 지침 (원문 수치만)
- 하드웨어 트리거 동기가 없다면 소프트웨어 타임스탬프 오프셋은 ms~수백 ms. 비보정 VIO의 허용 오프셋은 이 실험에서 약 6 ms 이내.^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]
- 카메라 타임스탬프는 노출 중간 시점을 기준으로 해야 하며 노출시간 절반이 오프셋 성분.^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]

## 한계·미확인
- 하드웨어 동기 vs 소프트웨어 동기의 직접 정량 비교 실험은 아님(오프셋 인위 주입). 단안 VIO, 롤링셔터 미다룸. 드론 비행 시험 아님(EuRoC는 MAV 데이터셋이나 오프라인 처리).^[inbox/processed/hw-20261021-ai-sync-camera-imu-online-temporal-calibration-qin-2018.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
