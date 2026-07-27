---
title: "PX4 Architecture Deep — uORB, Tasks, Work Queue 심층 분석"
created: 2026-07-28
updated: 2026-07-28
type: concept
tags: [drone-sw]
sources:
  - inbox/processed/px4-architecture.md
  - inbox/processed/px4-uorb-messaging.md
  - inbox/processed/px4-system-architecture.md
confidence: high
contested: false
contradictions: []
---

# PX4 Architecture Deep

PX4의 uORB 메시지 버스, 태스크/워크 큐 실행 모델, 계층형 소프트웨어 아키텍처 심층 분석.

## 고수준 소프트웨어 아키텍처

```
┌──────────────────────────────────────────┐
│              Applications                │
│  Commander │ Navigator │ MC_Control      │
├──────────────────────────────────────────┤
│              uORB (메시지 버스)           │
├──────────────────────────────────────────┤
│              Middleware                   │
│  EKF2 │ Sensors │ MAVLink │ Logger       │
├──────────────────────────────────────────┤
│              Drivers                     │
│  IMU │ Baro │ GPS │ RC │ PWM            │
├──────────────────────────────────────────┤
│              NuttX RTOS                  │
└──────────────────────────────────────────┘
```

## uORB 메시징

uORB는 PX4의 비동기 publish/subscribe 메시징 시스템. 부팅 초기에 자동 시작.

### 새 토픽 추가

`msg/` 디렉토리(버전 관리 메시지는 `msg/versioned/`)에 `.msg` 파일 추가하고 `msg/CMakeLists.txt`에 등록. CamelCase 명명 규칙.

```cpp
#include <uORB/topics/velocity_limits.h>
// Reference: ORB_ID(velocity_limits)
```

### 메시지 정의 구조

- **설명 주석**으로 시작 (`#`)
- **필수 필드**: 로깅용 `uint64_t timestamp`
- **버전 관리 메시지**: `uint32 MESSAGE_VERSION` 필수
- **멀티 토픽**: `# TOPICS` 구문으로 여러 토픽 생성

### 퍼블리싱/구독

대부분의 컨텍스트에서 퍼블리싱 가능 (인터럽트 핸들러 포함)하나, 토픽은 먼저 비인터럽트 컨텍스트에서 광고되어야 함.

**멀티 인스턴스 지원**: `orb_advertise_multi`로 동일 토픽의 독립 인스턴스 생성 (동일 유형의 다중 센서용). `orb_subscribe_multi`로 특정 인스턴스 타겟팅.

### 토픽 모니터링

- `listener` 명령: 토픽 내용 표시
- `uorb top`: 실시간 퍼블리싱 주파수 모니터링

## 모듈 실행 방법

### Tasks

독립 실행 모듈. 자체 스택과 프로세스 우선순위 보유.

### Work Queue Tasks

워크 큐를 공유하는 모듈. 협력적으로 동작해야 함 (서로 인터럽트 불가).

- **장점**: RAM 사용량 감소, 태스크 스위치 감소
- **단점**: sleep, poll, 블로킹 I/O 불가

`work_queue status`로 확인 (`top`에는 표시되지 않음).

## Flight Controller + Companion Computer

고급 시스템은 FC와 컴패니언 컴퓨터(미션 컴퓨터)를 짝지음. MAVLink 프로토콜로 직렬 또는 IP 링크 연결.

**역할 분담**:
- FC: 핵심 비행 운영, 실시간 제어 루프
- 컴패니언: 고급 자율 기능, 처리 집약적 작업 (컴퓨터 비전, SLAM 등)

## 업데이트 레이트

모듈은 메시지 업데이트 대기. 대부분 IMU 드라이버는 1kHz 샘플링 후 통합하여 250Hz로 발행. 낮은 주파수 모듈(Navigator 등)은 훨씬 느리게 실행.

## 관련 페이지

- [[px4-system-architecture]] — PX4 시스템 구조
- [[px4-flight-modes]] — 비행 모드
- [[ros2-drone-integration]] — ROS2 연동
