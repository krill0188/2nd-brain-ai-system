---
title: "카메라-IMU 동기 HW vs SW 직접 정량 비교 — 재조사 결과 (2026-10-23)"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: ros-middleware
tags: [drone, time-synchronization, camera-imu, hardware-sync, software-sync, vins, kalibr]
sources: [inbox/processed/hw-20261023-conv-camera-imu-sync-direct-comparison-2026-10-23.md]
confidence: medium
contested: false
contradictions: []
---

# 카메라-IMU 동기 HW vs SW 직접 정량 비교 — 재조사 결과 (2026-10-23)

- 원문: 본 폴더 ai/research/ai-sync-versavis-tschopp-2019-synced-vs-nonsynced, ai-sync-time-offset-vins-mono-rmse-qin-shen-2018; 20261022 conv-camera-imu-sync-hw-vs-sw-evidence-2026-10^[inbox/processed/hw-20261023-conv-camera-imu-sync-direct-comparison-2026-10-23.md]

## 핵심 내용
판정: **같은 조건에서 HW 트리거 동기와 SW 타임스탬프의 VIO 정확도를 ATE 수치로 직접 비교한 논문은 이번에도 확인하지 못함.** 가장 가까운 두 건을 전문으로 확인.^[inbox/processed/hw-20261023-conv-camera-imu-sync-direct-comparison-2026-10-23.md]
| 근거 | 무엇을 보였나 | 수치 유무 |
|---|---|---|
| VersaVIS (arXiv 1912.02469) | 같은 강체 위에서 동기 센서 대 비동기(FLIR+VI-Sensor IMU) 구성을 ROVIO 로 비교, 비동기는 특징점 추적 실패·궤적 지터. Kalibr 오프셋 표준편차: 동기 구성 0.03~0.05 ms, RealSense 5.98 ms | 오프셋 수치 있음, 궤적 정확도는 정성(그림) |
| Qin & Shen (arXiv 1808.00692) | EuRoC 에 5/15/30 ms 오프셋 주입, 보정 없는 OKVIS RMSE MH03 0.284→2.805 m, VINS-Mono 허용 약 6 ms | RMSE 수치 있음, HW/SW 비교는 아님 |
| Thermal-inertial 논문 (arXiv 2603.02114) | MCU 하드웨어 트리거+1 Hz 동기 펄스로 "sub-millisecond" 일관성, "software-only synchronization 의 지연·지터를 피함" 서술 | 비교 실험 없음(주장만) |
- SciTePress 2019 (Aerts & Demeester): 저가 카메라 타임스탬프를 IMU 시간에 맞추는 방법(옵티컬플로+파티클필터), 초록 기준 하드웨어 대비 비교 아님.^[inbox/processed/hw-20261023-conv-camera-imu-sync-direct-comparison-2026-10-23.md]
## 설계에 쓸 수 있는 지침
- "HW 동기가 SW 보다 X ms/Y% 낫다" 표현 금지. 쓸 수 있는 문장: 오프셋이 수 ms 를 넘으면 보정 없는 VIO 정확도가 급격히 악화(Qin 2018), 비동기 구성은 드리프트·지터가 증가(VersaVIS, 정성).^[inbox/processed/hw-20261023-conv-camera-imu-sync-direct-comparison-2026-10-23.md]
## 한계·미확인
- 시도한 수단: WebSearch 2회, arXiv PDF 3건 전문 텍스트 추출(VersaVIS, Qin, thermal-inertial), SciTePress 초록. Kalibr/VINS GitHub 이슈는 이번에 열람 못 함(미시도). 직접 비교 논문: 미확인.^[inbox/processed/hw-20261023-conv-camera-imu-sync-direct-comparison-2026-10-23.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[mbse-uav-sysml]]
