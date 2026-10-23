---
title: "Online Temporal Calibration for Monocular Visual-Inertial Systems — 시간 오프셋 주입 시 VINS 정확도 (EuRoC)"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: ros-middleware
ontology_class: TimingLatency
tags: [drone, time-synchronization, camera-imu, vins-mono, okvis, time-offset, euroc]
sources: [inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]
confidence: medium
contested: false
contradictions: []
---

# Online Temporal Calibration for Monocular Visual-Inertial Systems — 시간 오프셋 주입 시 VINS 정확도 (EuRoC)

- 원문: https://arxiv.org/abs/1808.00692 (PDF 전문 열람)^[inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]
- 저자: Tong Qin, Shaojie Shen^[inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]
- 발행: 2018-08-02 (arXiv)^[inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]

## 핵심 내용
열람: arXiv PDF 텍스트 추출, 본문 VI절·Table II 대조. 신뢰도: 중상(전문 확인).^[inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]
- 설계: 하드웨어 동기된 EuRoC(카메라 20 Hz, IMU 200 Hz)에 고정 시간 오프셋을 IMU 타임스탬프에 인위 주입(같은 데이터·같은 알고리즘, 오프셋만 변수). 오프셋 -40~+40 ms 범위로 VINS-Mono(오프셋 보정 없음)와 제안법 비교(MH03).^[inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]
- 결과 문구: VINS-Mono 의 RMSE 는 오프셋에 대해 포물선 형태로 증가, 허용 구간은 약 6 ms 이내. 제안법은 오프셋과 무관하게 RMSE 일정.^[inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]
- Table II(RMSE [m], 주입 오프셋 5/15/30 ms; 제안법 대 OKVIS=보정 없음) 발췌:^[inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]
| 시퀀스 | 5 ms | 15 ms | 30 ms |
|---|---|---|---|
| MH01 제안 / OKVIS | 0.155 / 0.318 | 0.158 / 0.382 | 0.156 / 0.544 |
| MH03 제안 / OKVIS | 0.194 / 0.284 | 0.194 / 0.451 | 0.195 / 2.805 |
| V1 03 제안 / OKVIS | 0.185 / 0.349 | 0.187 / 1.008 | 0.189 / 1.817 |
## 설계에 쓸 수 있는 지침
- 동기 오차(수 ms~수십 ms)가 VIO 정확도에 미치는 영향을 같은 조건에서 정량한 근거. 단 "하드웨어 트리거 대 소프트웨어 타임스탬프"의 직접 비교가 아니라 "오프셋 주입 실험"임.^[inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]
## 한계·미확인
- 하드웨어/소프트웨어 방식 자체 비교 아님. 6 ms 허용치는 이 알고리즘·이 데이터 기준.^[inbox/processed/hw-20261023-ai-sync-time-offset-vins-mono-rmse-qin-shen-2018.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
