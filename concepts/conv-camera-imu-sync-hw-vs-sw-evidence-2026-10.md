---
title: "카메라-IMU 하드웨어 동기 vs 소프트웨어 동기: 직접 비교 근거 정리 (직접 비교 논문 유무 포함)"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ros-middleware
tags: [drone, time-synchronization, camera-imu, hardware-sync, software-sync, kalibr, vins, px4, ardupilot]
sources: [inbox/processed/hw-20261022-conv-camera-imu-sync-hw-vs-sw-evidence-2026-10.md]
confidence: medium
contested: false
contradictions: []
---

# 카메라-IMU 하드웨어 동기 vs 소프트웨어 동기: 직접 비교 근거 정리 (직접 비교 논문 유무 포함)

- 원문: 본 폴더 ai/data/data-sync-px4-*, data-sync-ardupilot-*, ai/research/ai-sync-pirvs-*, ai-sync-exposure-midpoint-*; 20261021 ai-sync-camera-imu-online-temporal-calibration-qin-2018, ai-sync-camera-imu-varying-time-offset-ling-2018, data-sync-kalibr-temporal-calibration-readme, data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock^[inbox/processed/hw-20261022-conv-camera-imu-sync-hw-vs-sw-evidence-2026-10.md]

## 핵심 내용
판정: **같은 카메라·IMU·알고리즘으로 하드웨어 트리거 동기와 소프트웨어 타임스탬프를 정량 비교한 논문은 이번 조사 범위에서 확인하지 못함.** 아래는 간접 근거를 목적별로 분리.^[inbox/processed/hw-20261022-conv-camera-imu-sync-hw-vs-sw-evidence-2026-10.md]
| 근거 | 내용(수치는 원문) | 성격 |
|---|---|---|
| Qin & Shen 2018 (VINS 온라인 시간 보정, 20261021 수집) | 트리거·전송 지연으로 시간 오프셋 수 ms~수백 ms, 보정 안 한 VIO 허용 약 6 ms(기존 파일 기재) | 소프트웨어 추정 방식(비동기 시스템 전제) |
| Kalibr README (20261021) | 오프라인 배치 최적화로 카메라-IMU 시간 오프셋 추정 | 소프트웨어(오프라인 보정) |
| PX4 문서 | 트리거 핀+`CAMERA_TRIGGER` 시퀀스 번호+NTP 변형 시계 오프셋 추정, 캡처핀(핫슈)로 실제 촬영 시각 기록 | 하드웨어 동기 구성(정확도 수치 없음) |
| ArduPilot 문서 | TRIG(명령 시각)와 CAM(핫슈 피드백, `CAM1_FEEDBAK_PIN`) 로그 분리 | 하드웨어 피드백(수치 없음, VIO 절차 없음) |
| PIRVS 2017 | 카메라 간 HW 동기 + 호스트 드라이버 레벨 타임스탬프 혼합, 카메라-IMU 평균 17 ms 오프셋(분산 2 ms)을 Kalibr 변형으로 보정 | 혼합 설계 |
| Yang 등 2026 (HS-ES-VINS) | 하드웨어 동기 환경에서 타임스탬프 기준(노출 시작/중점/끝) 선택으로 ATE RMSE 22.7~28.6% 차이(20 ms 노출). "residual latency and jitter may persist after synchronization" | 하드웨어 동기 위의 잔여 오차 |
| NTNU 위키(20261021) | 직렬 PPS 지터 ±0.125 ms, PTP ±0.1 ms, ZED X 는 도착 시각 스탬프로 "a few frames" 지연 가능 | 비동료심사 프로젝트 문서 |
| NTNU 석사논문(ntnuopen 11250/3095612, 검색 요약만 확인) | LiDAR-IMU SLAM 에서 하드웨어 대 ROS 소프트웨어 타임스탬프 간 포즈 정확도 유의차 없음(고품질 장비), 소프트웨어 방식은 장비·소프트웨어에 크게 좌우 | **본문 미열람**(JS 사이트, 검색 스니펫 기준). 카메라 아님(LiDAR) |
## 설계에 쓸 수 있는 지침
- 정량 비교가 없으므로 "하드웨어 동기가 소프트웨어보다 X ms 낫다"는 문장은 쓰지 말 것. 확인된 것: ① 하드웨어 동기 후에도 타임스탬프 기준점·잔여 지터 문제가 남음(Yang 2026), ② 소프트웨어 타임스탬프 환경은 오프셋이 수 ms~수백 ms로 보고(Qin 2018)되며 오프라인/온라인 보정 필요, ③ FC 계열(PX4/ArduPilot)은 트리거 핀·핫슈 피드백을 제공.^[inbox/processed/hw-20261022-conv-camera-imu-sync-hw-vs-sw-evidence-2026-10.md]
## 한계·미확인
- 시도한 수단: WebSearch 2회, arXiv PDF/HTML, Europe PMC, GitHub raw, ArduPilot/PX4 문서. 실패: MDPI 직접 접근(403, Europe PMC로 우회), NTNU Open(JS), TUM VI/VersaVIS/UMA-VI 원문은 검색 스니펫만(미열람), SciTePress 2019 "Time Synchronisation of Low-cost Camera Images with IMU Data" 미열람. 신뢰도: 판정 중, 개별 수치는 각 파일 신뢰도 따름.^[inbox/processed/hw-20261022-conv-camera-imu-sync-hw-vs-sw-evidence-2026-10.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[mbse-uav-sysml]]
