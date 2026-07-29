---
title: "Swarm Modes — 군집 드론 운용 모드"
created: 2026-07-28
updated: 2026-07-28
type: concept
tags: [swarm, drone-ai, ai-agent]
sources:
  - inbox/processed/mastervault-swarm-architecture.md
confidence: medium
domain: ai-autonomy
contested: false
contradictions: []
---

# Swarm Modes

군집 드론 시스템의 운용 모드 정의. Leader-Follower 구조 기반의 4가지 주요 모드.

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

## 관련 페이지

- [[swarm-coordination]] — 군집 협업 개념
- [[recon-swarm-project]] — 실제 프로젝트 적용
- [[datalink-communication]] — 통신 기술
- [[drone-ai-agents]] — 자율 에이전트
