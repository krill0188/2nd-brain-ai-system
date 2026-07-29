---
title: "Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, ai-autonomy, slam, lidar, imu, navigation]
sources: [inbox/fetch-2026-07-30-arxiv-flight-ready-lidar-inertial-odometry-for-embedded-drone-plat.md]
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms

실시간 폐쇄 루프 항공 제어에 최적화된 LiDAR-관성 오도메트리(LIO) 시스템. IESKF 기반 LIO의 아키텍처 결함을 해결하여 임베디드 드론 플랫폼에서 실제 비행 준비 상태를 달성한다.

## 기존 LIO의 아키텍처 결함

| 결함 | 문제점 |
|------|--------|
| LiDAR 레이트에 묶인 오도메트리 발행 | 10 Hz (IMU 200 Hz 대비) |
| 누락된 속도 출력 | 완전한 상태 벡터 부재 |
| 실행 병목 현상 | IMU 처리 차단 |
| 뮤텍스 경쟁 | 동기화 문제 |
| 동기화 경쟁 조건 | 데이터 일관성 문제 |

## 개선 사항

### 1. IMU 레이트 전파 (IMU-rate Forward Propagation)
- 오도메트리 출력: ~10 Hz → 안정적인 200 Hz
- 모든 IMU 샘플에서 완전한 Twist 상태 제공

### 2. 직접 바디 프레임 속도 발행
- 완전한 상태 벡터 (위치 + 속도) 출력

### 3. SLERP 기반 스무딩
- LiDAR 손실 시에도 연속성 유지

### 4. 듀얼 실행기 격리
- 실행 병목 현상 제거

### 5. 명시적 동기화 보호
- 뮤텍스 경쟁 및 경쟁 조건 방지

## 검증

- **플랫폼**: Livox Mid-360 / Pixhawk 4 Mini 자율 UAV
- **그라운드 트루스**: 모션 캡처 시스템
- **결과**: 실시간 제어 요구사항 충족 확인

## 적용 가능성

기본 추정기(IESKF + ikd-Tree)를 변경하지 않으므로, FAST-LIO2 파생 구현체에 직접 적용 가능하다.

## 관련 페이지

- [[computer-vision-drone]] — 드론 컴퓨터 비전 및 SLAM
- [[px4-offboard-control]] — PX4 오프보드 제어
- [[drone-simulation]] — 드론 시뮬레이션 환경
