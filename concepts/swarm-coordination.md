---
title: Swarm Drone Coordination
created: 2026-07-27
updated: 2026-10-07
type: concept
tags: [swarm, drone-ai, multi-drone, formation, coordination]
sources: [raw/articles/mastervault-recon-swarm.md, raw/articles/mastervault-swarm-architecture.md, raw/papers/swarm/occupation-measure-mean-field-control-optimization-over-measures-and-frank-wolfe.md, raw/papers/swarm/다수-vtol-무인기의-군집비행을-위한-이착륙-운용방안-및-실비행-적용.md]
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
- [[uav-swarm-air-ground-isac]] — 교차 지역 협력 기반 Air-Ground ISAC 군집
- [[kci-vtol-swarm-takeoff-landing-operation]] — 다수 VTOL 고정익 군집 이착륙·천이 운용 절차

## 대규모 군집 최적화: OM-MFC (2026)

Yu·You·Pei의 occupation-measure mean-field control(OM-MFC)은 개별 에이전트가 아니라 에이전트 집단의 **점유측도(occupation measure)** 공간에서 군집의 진화를 모델링하고, 대규모 군집 제어를 측도 위의 무한차원 최적화 문제로 정식화한다. 상호작용 커널이 positive-semidefinite 조건을 만족하면 문제가 볼록해지며, Frank–Wolfe(FW) 및 fully-corrective 변형(FCFW)은 반복마다 고전적 최적제어 하위문제로 환원된다. 볼록성·최적해 존재·수렴 보장이 이론적으로 제시되었고, UAV 군집·위성 군집 수치실험에서 고차원·제약 환경의 확장성을 보였다고 보고한다.^[raw/papers/swarm/occupation-measure-mean-field-control-optimization-over-measures-and-frank-wolfe.md] 수집된 것은 초록뿐이라 실험 수치와 비교 기준선은 확인하지 못했다. 개체 단위 임무할당 접근인 [[kci-llm-cbba-swarm-task-allocation]]과는 달리 집단 분포 수준에서 다루는 접근으로, 에이전트 수가 매우 큰 경우의 대안 후보로 기록한다.

## VTOL 고정익 군집의 이착륙 운용 (KCI 2026)

기존 페이지가 다룬 편대·통신·최적화 외에, 군집이 비행에 진입·이탈하는 구간의 운용도 별도 절차가 필요하다. 이호진(2026)은 전 기체 동시 수직이륙 → 그룹별 지정 고도 분리 → 그룹 순차 출발·병렬 천이, 착륙은 공간 분리 → 순차 이탈 → 역천이 순서를 제안했고, 20대(2개 그룹) 옥외 시험에서 선두 그룹 천이 개시 후 전 기체가 20.5초 이내에 천이를 마쳤다고 보고한다(초록 절단, 단일 출처).^[raw/papers/swarm/다수-vtol-무인기의-군집비행을-위한-이착륙-운용방안-및-실비행-적용.md]

## 📰 최근 관련 소식
- 충남 첫 ‘국가 지정 드론공원’ 탄생…당진서 비행·교육·대회 한 번에 (녹색경제신문, Tue, 04 Au) — https://news.google.com/rss/articles/CBMiaEFVX3lxTE9ySFBDbWVDbGdTd3ZTTVlfUWhBYTRDNURtZW8zc2FmLW9CZHZmcF8wcEdFa2FfOVpabEgzM1VjV3lEUFJ3V0pteGtDLWlDN3VEYmhmMDdJQTI1bXl6anNrRW9XTjFxdDk2?oc=5
