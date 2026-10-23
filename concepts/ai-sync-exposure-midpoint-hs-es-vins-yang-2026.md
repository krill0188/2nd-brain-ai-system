---
title: "Exposure-Midpoint Temporal Alignment and Risk-Aware Adaptive Feature Tracking for Stereo Visual-Inertial Odometry (HS-ES-VINS)"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ai-autonomy
ontology_class: TimingLatency
tags: [drone, time-synchronization, camera-imu, hardware-trigger, vins-fusion, exposure, online-calibration]
sources: [inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]
confidence: medium
contested: false
contradictions: []
---

# Exposure-Midpoint Temporal Alignment and Risk-Aware Adaptive Feature Tracking for Stereo Visual-Inertial Odometry (HS-ES-VINS)

- 원문: https://www.mdpi.com/1424-8220/26/18/5849 (MDPI는 403, 전문은 Europe PMC PMC13611355 / doi 10.3390/s26185849 로 열람)^[inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]
- 저자: Sucheng Yang, Qingqing Liu, Zhihong Zhuang, Xiaofeng Shen^[inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]
- 발행: 2026-09-15 (Sensors 26(18), 5849)^[inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]

## 핵심 내용 (Europe PMC 전문 열람)
하드웨어 동기 환경에서도 이미지 타임스탬프가 가리키는 사건(트리거 도착·드라이버 콜백·판독 완료·수신 등)이 물리적 촬영 시각과 다를 수 있다는 점을 다룸. 하드웨어 동기 플랫폼(STIM300 IMU, HIKROBOT MV-CA013-20GC 글로벌셔터 카메라 2대, Livox LiDAR, RTK GNSS, 자체 MS-HTSS 동기장치; 카메라 25 Hz)에서 이미지 시각을 "노출 중간 시점"으로 재구성(동기 트리거 타임스탬프 + 카메라 debounce 지연 + 프레임별 노출시간).^[inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]
수치(초록·본문 일치): 20 ms 저조도 노출 조건에서 노출 중점 기준이 노출 시작 기준 대비 ATE RMSE 28.6%(고정 오프셋 보정)·22.7%(온라인 추정) 감소. 노출 종료 기준 대비 12.9%/19.2%. 중점 기준 절대 ATE RMSE 0.434 m(고정), 0.415 m(온라인). 정상 조명에서는 노출시간이 0.4~6.4 ms 로 차이가 작음. 적응형 프런트엔드 전체는 기준 VINS-Fusion 대비 ATE RMSE 16.8%(실내 다층), 12.9%(실외 자전거) 감소.^[inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]
서문 문구: 하드웨어 동기 뒤에도 "residual latency and jitter may persist"(참고문헌 23, 24 인용) — 이 파일 안에서는 정량 값이 아니라 선행연구 인용.^[inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 하드웨어 트리거를 쓰더라도 자동노출로 노출이 길어지면(20 ms) 타임스탬프 기준점(시작/중간/끝) 선택만으로 ATE 가 22.7~28.6% 달라짐. 트리거 기준 타임스탬프는 노출 시작이 아니라 중점으로 환산해야 한다는 근거.^[inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]
- IMU 쪽도 지연 존재: STIM300 비트리거 모드 지연 모델 식 제시(저역통과 33 Hz 설정 등), 값은 본문 표에 있으나 이 파일에는 미전사.^[inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]

## 한계·미확인
- 실내 다층·실외 자전거 시퀀스 데이터셋 실험이며 드론 비행 시험 아님. 하드웨어 동기 대 소프트웨어 동기의 직접 비교는 없음(전 구간 하드웨어 동기 데이터). 신뢰도 높음(동료심사 논문, 오픈액세스 전문 열람), 단 인용 수 0건의 신규 논문.^[inbox/processed/hw-20261022-ai-sync-exposure-midpoint-hs-es-vins-yang-2026.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
