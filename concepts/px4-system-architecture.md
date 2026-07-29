---
title: PX4 System Architecture
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, PX4, flight-controller, companion-computer]
sources: [raw/articles/px4-system-architecture.md]
confidence: high
domain: flight-control
contested: false
contradictions: []
---

# PX4 System Architecture

PX4는 무인 항공기를 위한 완전한 자동조종장치 시스템을 제공하며, 두 가지 주요 시스템 구성으로 운용된다: FC(Flight Controller) 단독 구성과 FC + Companion Computer 결합 구성.^[raw/articles/px4-system-architecture.md]

## Flight Controller System (기본 구성)

PX4 시스템의 핵심은 PX4 flight stack을 실행하는 **Flight Controller**다.^[raw/articles/px4-system-architecture.md]

### 하드웨어 구성요소

| 구성요소 | 설명 |
|---------|------|
| **Flight Controller** | 내부 센서 내장 (IMU, compass, barometer) |
| **Motor Control** | PWM, DroneCAN 등으로 연결된 ESC |
| **Sensors** | GPS, compass, 거리 센서, optical flow, ADSB 트랜스폰더 |
| **Payloads** | 카메라 및 기타 장비 |
| **Communication** | 텔레메트리 라디오 (GCS 연결) |
| **Input** | 수동 조종용 RC 제어 시스템 |

### 소프트웨어 스택

```
Drivers → Communication modules → Controllers → Estimators → Middleware + QGroundControl GCS
```

- **Drivers**: 센서/액추에이터 하드웨어 드라이버
- **Communication**: MAVLink 등 외부 통신 모듈
- **Controllers**: PID 기반 비행 제어기
- **Estimators**: EKF2 상태 추정기
- **Middleware**: uORB 메시지 버스

## FC + Companion Computer (고급 구성)

고급 시스템은 **Flight Controller**와 **Companion Computer**(미션 컴퓨터)를 직렬 또는 IP 링크로 연결한다.^[raw/articles/px4-system-architecture.md]

### 특징

- **Companion Computer**: Linux 실행, NuttX 대비 우수한 개발 환경 제공
- **컴퓨터 비전, 통신, 클라우드 연동**에 적합
- MAVLink Router를 통해 지상국/클라우드 서비스 경유

### 역할 분리

| 구성요소 | 담당 업무 |
|---------|----------|
| **Flight Controller** | 핵심 비행 연산, 실시간 제어 루프 |
| **Companion Computer** | 고급 자율 기능, 연산 집약적 작업 (CV, SLAM 등) |

### 통신 흐름

```
Ground Station ←→ MAVLink Router ←→ Companion ←→ FC
                                      (Linux)    (NuttX)
```

## 관련 개념

- [[px4-flight-modes]] — PX4 비행 모드 분류
- [[dronecan-protocol]] — FC-주변기기 통신 프로토콜
- [[ros2-drone-integration]] — ROS2 연동 스택
