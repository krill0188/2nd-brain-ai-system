---
title: Visual SLAM GPS-Denied Evaluation
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone-ai, drone, slam, computer-vision, gps-denied]
sources: [raw/papers/drone-ai/fetch-2026-08-19-arxiv-robust-visual-slam-for-uav-navigation-in-gps-denied-and-degr.md]
confidence: high
contested: false
contradictions: []
---

# Visual SLAM GPS-Denied Evaluation

GPS 차단 및 시각적으로 열악한 환경에서의 안정적인 UAV 자율 비행을 위한 V-SLAM(Visual SLAM) 시스템 비교 평가 연구이다. 5개의 V-SLAM 시스템을 4가지 패러다임(전통적, 딥러닝, 순환, ViT)에서 평가했다.

## 평가 대상 시스템

| 시스템 | 패러다임 | 특징 |
|--------|----------|------|
| ORB-SLAM3 | 전통적 | 특징점 기반, 열악한 환경에서 62.4% TSR, 밀무(0%) 실패 |
| DPVO | 순환 | 효율성-강건성 최적 균형(18.6 FPS, 3.1GB GPU, 86.1% TSR) |
| DROID-SLAM | 딥러닝 | 강건한 성능 |
| DUSt3R | ViT | 최고 추적 성공률 96.5% |
| MASt3R | ViT | 최저 열악 환경 ATE 0.027m |

## 평가 환경

- **데이터셋**: TUM RGB-D, EuRoC MAV, UMA-VI, SubT-MRS 및 커스텀 실내 데이터셋
- **열악 조건**: 정상, 저조도, 먼지 안개, 모션 블러, 복합
- **정밀도**: sub-millimeter Vicon ground truth

## 임베디드 배포

NVIDIA Jetson 플랫폼에서 SWaP(크기, 중량, 전력) 제약 조건 하의 SLAM 선택 가이드라인 제공.

## 관련 개념

- [[drone-ai]] — 드론 AI 도메인 개요
- [[computer-vision-drone]] — 드론 컴퓨터 비전
- [[visual-positioning-odometry]] — 시각적 위치 추정 및 오도메트리
- [[gps-uav-imu]] — GPS 미수신 환경 UAV 위치 추정
