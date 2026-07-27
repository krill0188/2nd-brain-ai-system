---
title: Drone AI Agents
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [ai-agent, drone-ai, autonomous, decision-making, multi-agent]
sources: []
confidence: medium
contested: false
contradictions: []
---

# Drone AI Agents

드론 AI 에이전트는 자율적 의사결정, 환경 인식, 목표 달성을 수행하는 지능형 소프트웨어 시스템이다. 단일 에이전트에서 다중 에이전트 협업까지 다양한 형태가 있다.

## 에이전트 유형

| 유형 | 설명 | 예시 |
|------|------|------|
| **Reactive Agent** | 간단한 조건-행동 매핑 | 장애물 회피 |
| **Deliberative Agent** | 계획 및 추론 | 미션 계획 |
| **Hybrid Agent** | 반응 + 의도 결합 | 현실용 시스템 |
| **Multi-Agent System** | 다중 에이전트 협력 | 스웜 드론 |

## 아키텍처 패턴

### 1. Perception-Action Loop

```
┌─────────┐    ┌─────────┐    ┌─────────┐
│ Sensors │───▶│  Brain  │───▶│ Actuators│
└─────────┘    └─────────┘    └─────────┘
       ▲           │                │
       │           ▼                │
       └────┌──────────────┐◄──────┘
            │   Memory/KB    │
            └────────────────┘
```

### 2. BDI (Belief-Desire-Intention)

| 구성요소 | 설명 |
|----------|------|
| **Beliefs** | 환경에 대한 지식 |
| **Desires** | 목표/원하는 상태 |
| **Intentions** | 실행 중인 계획 |

### 3. Reinforcement Learning Agent

```
State ──▶ Policy ──▶ Action ──▶ Reward ──▶ Update
  ▲                                     │
  └────────────── Environment ◄──────┘
```

## 주요 기능

### 1. Perception (인식)

| 모달리티 | 센서 | 기술 |
|---------|------|------|
| **Vision** | 카메라 | Object Detection, SLAM |
| **LiDAR** | 레이저 | 3D 매핑, 장애물 감지 |
| **Radar** | RF | 저시간 해상도, all-weather |
| **Fusion** | 다중 | Sensor Fusion, EKF |

### 2. Decision Making (의사결정)

| 기술 | 설명 |
|------|------|
| **Behavior Trees** | 계층적 행동 조직 |
| **Finite State Machines** | 상태 기반 전환 |
| **Planning Algorithms** | A*, RRT, PRM |
| **Reinforcement Learning** | 보상 기반 학습 |

### 3. Action Execution (행동)

| 행동 | 설명 |
|------|------|
| **Navigation** | 경로 추종, 장애물 회피 |
| **Manipulation** | 매니퓰레이션 (payload) |
| **Communication** | 타 에이전트와 협력 |

## 실제 시스템 아키텍처

### Companion Computer Agent

```
┌─────────────────────────────────────────┐
│           AI Agent (Linux)            │
│  ┌─────────┐  ┌─────────┐  ┌────────┐ │
│  │YOLO/SLAM│  │  Nav2   │  │Mission │ │
│  └────┬────┘  └────┬────┘  └───┬────┘ │
│       └─────────────┴───────────┘      │
│              ROS2 / MAVSDK            │
│                   │                   │
└───────────────────┼───────────────────┘
                    │
            ┌───────┴───────┐
            ▼               ▼
     ┌────────────┐   ┌────────────┐
     │  PX4/Ardu │   │   GCS      │
     │  (Nuttx)  │   │            │
     └────────────┘   └────────────┘
```

## 사용 사례

| 사례 | AI 기술 | 설명 |
|------|---------|------|
| **자율 탐색** | SLAM + Path Planning | GPS-denied 환경 |
| **객체 추적** | Computer Vision | 타겟 추종 |
| **협력 탐색** | Multi-Agent | 병렬 탐색 |
| **적응적 제어** | Reinforcement Learning | 풍향 대응 |

## 도전 과제

| 과제 | 설명 | 접근 방식 |
|------|------|----------|
| **Real-time** | 지연 제한 | Edge AI, 최적화 |
| **Safety** | 안전 보장 | Formal verification |
| **Explainability** | 설명 가능성 | Attention, Saliency |
| **Scalability** | 확장성 | Distributed computing |

## 관련 개념

- [[px4-offboard-control]] — Offboard 제어 인터페이스
- [[swarm-coordination]] — 다중 에이전트 협업
- [[computer-vision-drone]] — 드론 컴퓨터 비전
- [[ros2-drone-integration]] — ROS2 기반 AI 연동
