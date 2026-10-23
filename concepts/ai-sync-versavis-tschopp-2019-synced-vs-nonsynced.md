---
title: "VersaVIS: An Open Versatile Multi-Camera Visual-Inertial Sensor Suite (동기 대 비동기 센서 비교 실험)"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: ros-middleware
ontology_class: TimingLatency
tags: [drone, time-synchronization, camera-imu, hardware-trigger, kalibr, rovio, versavis]
sources: [inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]
confidence: medium
contested: false
contradictions: []
---

# VersaVIS: An Open Versatile Multi-Camera Visual-Inertial Sensor Suite (동기 대 비동기 센서 비교 실험)

- 원문: https://arxiv.org/abs/1912.02469 (PDF 전문 열람)^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]
- 저자: Florian Tschopp, Michael Riner, Marius Fehr, Lukas Bernreiter, Fadri Furrer, Tonci Novkovic, Andreas Pfrunder, Cesar Cadena, Roland Siegwart, Juan Nieto^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]
- 발행: 2019-12-05 (arXiv)^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]

## 핵심 내용
열람: arXiv PDF 텍스트 추출, 본문 V절(평가)·표 II·그림 9-10 대조. 신뢰도: 중상(전문 확인, 단 VIO 정확도 비교는 정성적).^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]
- 하드웨어 동기 구성(MCU 트리거+노출 중점 타임스탬프). Kalibr 로 카메라-IMU 시간 오프셋을 추정한 표(원문 Table II, 오프셋 단위 ms, 평균/표준편차):^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]
| 센서 | 오프셋 평균 [ms] | 표준편차 [ms] | 비고 |
|---|---|---|---|
| VersaVIS (IMU 필터 B=4, te=1/3/5 ms 노출) | 20.007 / 20.003 / 19.963 | 0.048 / 0.036 / 0.030 | 노출시간과 무관, 반복 일관 |
| VI-Sensor | 1.173 | 0.046 | 비교 대상(자체 동기) |
| RealSense | 9.885 | 5.977 | 오프셋이 불일치 |
  원문 해석: VersaVIS·VI-Sensor 는 동기 정확도 0.05 ms 이하로 해석할 수 있는 낮은 표준편차. IMU 필터 설정(B)에 따라 오프셋이 1.55 → 5.26 → 19.95 ms 로 변하므로 드라이버/추정기 쪽에서 보상 필요. RealSense 는 프레임 간격의 절반(약 15 ms)으로 구분되는 이중 분포 = 프레임 한 장 어긋남 가능성을 시사한다고 서술.^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]
- 동기 대 비동기 VIO 비교(같은 실험실 데이터, ROVIO): "VersaVIS non synced"(FLIR 카메라+VI-Sensor IMU, 호스트 소프트웨어 시간 변환만 가능)에서는 IMU와 이미지 측정이 맞지 않아 많은 특징점이 추적되지 못했고, 궤적은 VersaVIS(동기)가 가장 낮은 드리프트, 비동기는 지터가 큼(그림 10, 정성적).^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]
- 클록 변환: 호스트-MCU EKF 클록 오프셋 혁신이 약 ±0.2 ms, 시리얼-USB 지터로 잔차가 ±5 ms 이내 진동.^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]
## 설계에 쓸 수 있는 지침
- "같은 카메라/IMU/알고리즘에서 동기 유무에 따른 궤적 차이를 보인" 가장 가까운 공개 사례(정성). 정량 ATE 표는 없음.^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]
## 한계·미확인
- 비동기 구성이 센서가 달라(FLIR+VI-Sensor IMU) 완전한 단일 변수 비교는 아님. 정량 ATE/드리프트 수치 미확인. 해당 그림은 이미지.^[inbox/processed/hw-20261023-ai-sync-versavis-tschopp-2019-synced-vs-nonsynced.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
