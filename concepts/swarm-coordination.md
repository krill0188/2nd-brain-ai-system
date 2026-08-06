---
title: Swarm Drone Coordination
created: 2026-07-27
updated: 2026-08-06
type: concept
tags: [swarm, drone-ai, multi-drone, formation, coordination]
sources: [raw/articles/mastervault-recon-swarm.md, raw/articles/mastervault-swarm-architecture.md]
confidence: medium
domain: ai-autonomy
contested: false
contradictions: []
---

# Swarm Drone Coordination

스웜 드론은 여러 대의 UAV가 협력하여 공통 목표를 달성하는 다중 기체 시스템이다. Leader-Follower 구조, 분산 제어, 자율 협력 등 다양한 아키텍처가 존재한다.^[raw/articles/mastervault-swarm-architecture.md]

## 시스템 아키텍처

```
┌─────────────────────────────────────────────────┐
│              Ground Station                      │
│    ┌───────────┐  ┌───────────┐  ┌────────┐   │
│    │ Swarm GCS │  │ QGC Custom│  │ Web GCS│   │
│    └─────┬─────┘  └─────┬─────┘  └───┬────┘   │
└──────────┼──────────────┼────────────┼────────┘
           │              │            │
           └──────────────┼────────────┘
                          │ MAVLink
            ┌─────────────┼──────────────┐
            ▼             ▼              ▼
      ┌─────────┐   ┌─────────┐   ┌─────────┐
      │ Leader  │   │Follower │   │Follower │
      │         │◄──►│         │◄──►│         │
      └─────────┘   └─────────┘   └─────────┘
```

## 통신 구조

| 링크 | 프로토콜 | 용도 |
|------|----------|------|
| **GCS ↔ Leader** | MAVLink (SiK/WiFi) | 명령/텔레메트리 |
| **Leader ↔ Followers** | MAVLink (P2P) | 편대 좌표/상태 |
| **Inter-drone** | Custom MAVLink | 장애물 공유/회피 |

## 스웜 모드

| 모드 | 설명 | 상태 |
|------|------|:----:|
| **Formation** | 고정 편대 비행 | 설계 중 |
| **Follow-Leader** | 리더 추종 | 개발 중 |
| **Area Search** | 구역 분할 탐색 | 계획 |
| **RTL Swarm** | 일괄 복귀 | 계획 |

## 프로젝트 사례: 군집정찰드론

지능형 자율 군집정찰 시스템 개발 프로젝트.^[raw/articles/mastervault-recon-swarm.md]

### 4단계 로드맵

| 단계 | 내용 | 상태 |
|:----:|------|:----:|
| 1 | 단일 기체 자율비행 + 센서 통합 | 진행 중 |
| 2 | 2기 편대비행 + 통신 검증 | 계획 |
| 3 | 3+ 기 군집 + 구역 분할 탐색 | 계획 |
| 4 | GPS-denied + 실내 군집 | 계획 |

### 센서 스택

| 센서 | 용도 | 인터페이스 |
|------|------|-----------|
| **LiDAR** | 장애물 감지/매핑 | UART/I2C |
| **카메라 (RGB)** | 정찰/객체 인식 | CSI/USB |
| **Radar** | 전방위 감지 | SPI |
| **Optical Flow** | GPS-denied 위치추정 | I2C |
| **RTK GPS** | 정밀 위치 | UART |

## 핵심 과제

| 과제 | 요구사항 | 접근 방식 |
|------|----------|----------|
| **통신 지연** | < 100ms | 고속 무선링크, 메시지 압축 |
| **GPS-denied** | 실내/협곡 대응 | LiDAR SLAM, Optical Flow |
| **단일 실패점** | 리더 사망 시 승계 | 자동 리더 재선출 |
| **충돌 회피** | 최소 이격거리 | ORCA/VO 알고리즘 |
| **배터리 관리** | 자동 교대 | 상태 기반 스케줄링 |

## 안전 시스템

- **Geofence**: 하드웨어 + 소프트웨어 이중
- **배터리 페일세이프**: 자동 RTL
- **통신 두절 대응**: 독립 귀환
- **충돌 회피**: 최소 이격거리 유지

## SITL 테스트

```bash
# ArduPilot SITL 멀티 기체
sim_vehicle.py -v ArduCopter --instance 0 -L HOME_LAT,HOME_LNG,ALT,HDG
sim_vehicle.py -v ArduCopter --instance 1 -L HOME_LAT,HOME_LNG,ALT,HDG
```

```bash
# PX4 SITL 멀티 기체
Tools/simulation/gazebo-classic/sitl_multiple_run.sh -n 3
```

## 관련 프로젝트

- Swarm OpS GCS (Qt/C++ 기반)
- Swarm QGC Custom (QGC 포크)
- gcs_dev (웹 기반 GCS)

## 관련 개념

- [[px4-system-architecture]] — PX4 시스템 연동
- [[ardupilot-architecture]] — ArduPilot 연동
- [[mavlink-protocol]] — 통신 프로토콜
- [[dronecan-protocol]] — 주변기기 통신
- [[flight-controller-hardware]] — FC 하드웨어 선택

## 스웜 연구 심화

- [[distributed-aerial-surveillance-swarm]] — 분산 항공 감시 스웜(LTL 기반)
- [[mrope-multi-robot-safety]] — 다중 로봇 안전 프로토콜
- [[swarm-modes]] — 스웜 운용 모드
- [[uav-swarm-target-localization]] — 스웜 표적 위치추정
- [[cross-layered-medical-drone-coordination]] — 의료물자 배송용 다중 드론 조율

## 📰 최근 관련 소식
- 충남 첫 ‘국가 지정 드론공원’ 탄생…당진서 비행·교육·대회 한 번에 (녹색경제신문, Tue, 04 Au) — https://news.google.com/rss/articles/CBMiaEFVX3lxTE9ySFBDbWVDbGdTd3ZTTVlfUWhBYTRDNURtZW8zc2FmLW9CZHZmcF8wcEdFa2FfOVpabEgzM1VjV3lEUFJ3V0pteGtDLWlDN3VEYmhmMDdJQTI1bXl6anNrRW9XTjFxdDk2?oc=5
