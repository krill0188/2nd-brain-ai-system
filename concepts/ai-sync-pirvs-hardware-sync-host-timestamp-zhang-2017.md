---
title: "PIRVS: An Advanced Visual-Inertial SLAM System with Flexible Sensor Fusion and Hardware Co-Design"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ai-autonomy
tags: [drone, time-synchronization, camera-imu, hardware-trigger, vio, kalibr]
sources: [inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]
confidence: medium
contested: false
contradictions: []
---

# PIRVS: An Advanced Visual-Inertial SLAM System with Flexible Sensor Fusion and Hardware Co-Design

- 원문: https://arxiv.org/abs/1710.00893^[inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]
- 저자: Zhe Zhang, Shaoshan Liu, Grace Tsai, Hongbing Hu, Chen-Chi Chu, Feng Zheng^[inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]
- 발행: 2017-10 (arXiv; 정확한 제출일은 PDF 본문에서 미확인)^[inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]

## 핵심 내용 (PDF 본문 확인)
하드웨어 동기와 소프트웨어 타임스탬프를 같은 장치 안에서 혼합한 설계 기록. 열람 방법: arXiv PDF를 받아 Ghostscript 로 텍스트 추출, 하드웨어 동기 절 확인.^[inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]
- 하드웨어: ISP가 스테레오 카메라 간 하드웨어 동기와 자동노출을 트리거. 본문 수치: CMOS 센서-ISP, ISP-CPU 지연은 MIPI 경유 "roughly 10ns"(IMU I2C도 동일 주장), ISP 이미지 전처리 약 10 ms 이며 "consistent with little uncertainty".^[inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]
- 타임스탬프 위치: 이미지를 ISP 단계가 아닌 "host CPU 의 driver level" 에서 이미지·IMU 둘 다 타임스탬프. 이유(원문): 이미지 타임스탬프를 IMU 와 같은 시계에 맞추는 것이 복잡하기 때문.^[inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]
- 보정: Kalibr 기반으로 수정한 시간 오프셋 보정을 장치별 공장 보정에 포함. 측정치: "an average of 17ms timestamp offset with 2ms variance between the stereo camera and IMU", 보정 3분/대.^[inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 카메라를 하드웨어 동기해도 센서-호스트 타임스탬프 방식에 따라 카메라-IMU 간 평균 17 ms 오프셋(분산 2 ms)이 남아 오프라인 보정으로 제거한 사례.^[inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]

## 한계·미확인
- 하드웨어 동기 vs 소프트웨어 동기를 같은 조건에서 나란히 비교한 실험은 아님(단일 하드웨어 설계 보고). 항공기·드론 탑재 시험 아님. 17 ms 오프셋이 하드웨어 트리거 도입 이전/이후 어느 쪽인지 본문에서 구분 명시 미확인. 신뢰도 중(기업 시스템 논문).^[inbox/processed/hw-20261022-ai-sync-pirvs-hardware-sync-host-timestamp-zhang-2017.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
