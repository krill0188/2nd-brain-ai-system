---
source_url: "file://MasterVault/Drone/Swarm/Swarm-Architecture.md"
ingested: 2026-07-27
captured: 2026-07-27
type: article
author: "Master (personal dev notes)"
sha256: "4b8g0d3f6e9c2a5d8f1a4b7c9e2d5f8a1b4c7e9f2a5b8c1d4e7f9a2b5c8d1e4"
tags: [swarm, datalink]
---

# 스웜 드론 아키텍처

## 시스템 구조

```
┌─────────────────────────────────────────────────┐
│                  Ground Station                  │
│  ┌───────────┐  ┌───────────┐  ┌────────────┐  │
│  │ Swarm GCS │  │ QGC Custom│  │  Web GCS   │  │
│  └─────┬─────┘  └─────┬─────┘  └─────┬──────┘  │
└────────┼───────────────┼──────────────┼─────────┘
         │               │              │
         └───────────────┼──────────────┘
                         │ MAVLink
         ┌───────────────┼──────────────┐
         ▼               ▼              ▼
   ┌──────────┐    ┌──────────┐   ┌──────────┐
   │ Leader   │    │ Follower │   │ Follower │
   │ (CUAV)   │◄──►│ (Holybro)│◄──►│ (Holybro)│
   └──────────┘    └──────────┘   └──────────┘
     V7+ #1009       6C #1041       6C #xxxx
```

## 통신 구조

| 링크 | 프로토콜 | 용도 |
|------|----------|------|
| GCS ↔ Leader | MAVLink (SiK/WiFi) | 명령/텔레메트리 |
| Leader ↔ Followers | MAVLink (P2P) | 편대 좌표/상태 |
| Inter-drone | Custom MSG (MAVLink) | 장애물 공유/회피 |

## 스웜 모드

| 모드 | 설명 | 구현 상태 |
|------|------|:---------:|
| Formation | 고정 편대 비행 | 설계 중 |
| Follow-Leader | 리더 추종 | 설계 중 |
| Area Search | 구역 분할 탐색 | 계획 |
| RTL Swarm | 일괄 복귀 | 계획 |

## 핵심 과제

- Inter-drone 통신 지연 < 100ms
- GPS-denied 환경 대응 (LiDAR/Optical Flow)
- 단일 실패점 제거 (리더 사망 시 자동 승계)
- 충돌 회피 알고리즘 (ORCA/VO)
- 배터리 기반 자동 교대

## 관련 프로젝트

- Swarm OpS GCS (Qt/C++ 기반 데스크탑)
- Swarm QGC Custom (QGC 포크)
- gcs_dev (웹 기반 GCS)
- recon-swarm-drone (정찰 특화)
