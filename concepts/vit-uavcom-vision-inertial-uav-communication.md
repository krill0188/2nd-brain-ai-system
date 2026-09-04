---
title: "VIT-UAVCom: Vision-Inertial Tracking-Assisted UAV Communication"
created: 2026-09-05
updated: 2026-09-05
type: concept
domain: comms-protocol
tags: [drone, comms-protocol, drone-ai]
sources: [raw/papers/_unclassified/enhancing-uav-trajectory-and-communications-through-vision-inertial-tracking.md]
confidence: medium
contested: false
contradictions: []
---

# VIT-UAVCom: Vision-Inertial Tracking-Assisted UAV Communication

VIT-UAVCom(Vision–Inertial Tracking-Assisted UAV Communication)은 GPS가 차단된 동적 무선 환경에서
비지상 네트워크(non-terrestrial network)를 위한 에너지 효율적이고 신뢰성 있는 통신 시스템이다.
온보드 카메라와 IMU 센서를 UAV 지원 통신에 활용한 최초 연구로 제시되었다 ^[raw/papers/_unclassified/enhancing-uav-trajectory-and-communications-through-vision-inertial-tracking.md].

## 핵심 아이디어

- 시스템 잡음과 잔여 추적 오차(residual tracking inaccuracy)를 명시적으로 반영한 완전한 VIT-UAVCom
  시스템 모델을 구성.
- UAV 궤적과 통신 성능(추진 에너지 효율, 아웃티지 확률, 물리계층 보안)을 공동 최적화하는 문제로 정식화.
- 실시간 구현을 위해 선형 탐색(LS), 이진 탐색(BS), 유전 탐색(genetic search) 세 가지 옵티마이저를 제안·평가.

## 성능 결과

- K-means 벤치마크 대비 에너지 효율 **144% 개선**.
- 강건한 비밀유지(secrecy) 성능과 신뢰성 있는 사용자 커버리지를 유지.
- BS가 LS 대비 계산 시간을 약 **50% 단축**.

## 관련 개념

- [[datalink-communication]] — 드론 데이터링크 통신 기술 전반
- [[gps-uav-imu]] — GPS 미수신 환경 UAV 위치추정 기법
- [[active-sensing-uav-communication]] — 감지 지원 UAV 통신 최적화
