---
title: "Kalibr (ethz-asl): Visual-Inertial Calibration with temporal (time offset) estimation"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, time-synchronization, camera-imu, kalibr, calibration]
sources: [inbox/processed/hw-20261021-data-sync-kalibr-temporal-calibration-readme.md]
confidence: medium
contested: false
contradictions: []
---

# Kalibr (ethz-asl): Visual-Inertial Calibration with temporal (time offset) estimation

- 원문: https://github.com/ethz-asl/kalibr (README) ; 방법 논문 Furgale et al., IROS 2013 (PDF 열람 실패)^[inbox/processed/hw-20261021-data-sync-kalibr-temporal-calibration-readme.md]
- 저자: ETH Zurich ASL (Kalibr)^[inbox/processed/hw-20261021-data-sync-kalibr-temporal-calibration-readme.md]
- 발행: README 최신판(뉴스 항목 최신 2022-11-24)^[inbox/processed/hw-20261021-data-sync-kalibr-temporal-calibration-readme.md]

## 핵심 내용
README가 밝힌 4가지 문제: Multi-Camera Calibration, Visual-Inertial Calibration (CAM-IMU: "Spatial and temporal calibration of an IMU w.r.t a camera-system along with IMU intrinsic parameters"), Multi-Inertial Calibration (IMU-IMU, 카메라 보조 1개 필요), Rolling Shutter Camera Calibration. 뉴스 항목: 2022-05-03 Ubuntu 20.04/Docker 지원 병합, 2020-02-03 Ubuntu 18.04 초기 지원. 설치는 Docker 또는 ROS workspace 소스 빌드(ROS1 기반 배지).^[inbox/processed/hw-20261021-data-sync-kalibr-temporal-calibration-readme.md]
Qin & Shen 2018은 Kalibr를 "offline batch optimization", 체커보드 패턴 필요, 제안법보다 "dozens of times more" 계산이 든다고 묘사(관련 파일 참고).^[inbox/processed/hw-20261021-data-sync-kalibr-temporal-calibration-readme.md]

## 설계에 쓸 수 있는 지침
- 카메라-IMU 시간 오프셋은 Kalibr로 오프라인 1회 추정해 구동 파라미터(타임스탬프 shift)에 반영 가능. 노출시간 등이 바뀌면 오프셋이 변할 수 있으므로(Qin & Shen) 설정 변경 시 재보정.^[inbox/processed/hw-20261021-data-sync-kalibr-temporal-calibration-readme.md]

## 한계·미확인
- Furgale 2013 논문과 정량 정확도(ms)는 열람 못 함(furgalep.github.io 404). Kalibr의 ROS 2 지원 여부는 README에서 미확인(ROS1 배지만 확인).^[inbox/processed/hw-20261021-data-sync-kalibr-temporal-calibration-readme.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
