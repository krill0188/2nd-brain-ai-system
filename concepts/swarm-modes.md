---
title: "Swarm Modes — 군집 드론 운용 모드"
created: 2026-07-28
updated: 2026-10-07
type: concept
tags: [swarm, drone-ai, ai-agent]
sources:
  - raw/articles/mastervault-swarm-architecture.md
  - raw/papers/swarm/hierarchical-optimal-consensus-for-economically-efficient-path-planning-in-multi.md
  - raw/papers/swarm/robust-observer-based-visual-servoing-control-of-gimbal-mounted-cameras-for-mult.md
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

## 관련 연구 (2026-09-30 추가, 서지정보만 확보 — 초록 미수집)

- "Hierarchical optimal consensus for economically efficient path planning in
  multi-UAV" (Zhu·Xu·Bi·Wang, 2027)^[raw/papers/swarm/hierarchical-optimal-consensus-for-economically-efficient-path-planning-in-multi.md] —
  다중 UAV 경제적 효율 경로계획을 위한 계층적 최적 컨센서스. 제목·서지 사항만
  확보, 방법·수치 결과는 원문 확보 후 보강 필요.
- "Robust observer-based visual servoing control of gimbal-mounted cameras for
  multi-UAV target tracking via relative dynamics and distributed Gaussian
  processes" (Miao·Wang·Niu·Zhang·Yu, 2027)^[raw/papers/swarm/robust-observer-based-visual-servoing-control-of-gimbal-mounted-cameras-for-mult.md] —
  짐벌 탑재 카메라의 관측기 기반 강건 비주얼 서보잉으로 다중 UAV 표적 추적 제어.
  제목·서지 사항만 확보, 방법·수치 결과는 원문 확보 후 보강 필요.

## 관련 페이지

- [[swarm-coordination]] — 군집 협업 개념
- [[recon-swarm-project]] — 실제 프로젝트 적용
- [[datalink-communication]] — 통신 기술
- [[drone-ai-agents]] — 자율 에이전트
- [[game-theoretic-drone-swarm-defense]] — 차등 게임이론 기반 드론 스웜 방어 전술
- [[swarmnxt-aerial-swarm-platform]] — 오픈소스 SW-HW 애자일 공중 스웜 플랫폼
- [[kci-uav-swarm-mission-reliability-abort]] — 재구성형 UAV 스웜 임무 신뢰도 모델링
- [[kci-vtol-swarm-takeoff-landing-operation]] — VTOL 군집 이착륙·천이 운용(군집 진입·이탈 절차)
- [[calibrate-once-fly-any-team-swarm-training]] — 저충실도 시뮬레이션 잔차 보정 군집 훈련

## 📰 최근 관련 소식
- '군집 드론' 폭탄테러 가상상황…민·관·군·경·소방 첫 합동훈련 (뉴시스, Wed, 19 Au) — https://news.google.com/rss/articles/CBMiYEFVX3lxTE53Q25RRW5taVdpZ25YWTdOMTJHRXF3aGZ3ckJhMzhtUWUyakVlYTZER0hvanVUWGxHMkN5c2dJM3h3MFUxeDhjWnlBNUR3QmJIVmdNX2xsZHZHeGxuakNBSNIBeEFVX3lxTE96SUcydjlfVjA5eGkweHplNjI3cVo1QVVobU1XWEdDdlJlNlJzN3V5clpaSzRybWZqOGZyaXR5V0wzQlNsaG1NQmNYN0xDVHprajc5OGxNZHJvYTNMRHBwLXM2Y3Q5dWtLalZMeDgzLUZYeGlSdGswLQ?oc=5
- GPS 끊긴 건물서 조난자 찾는다…우주항공청, 드론 경연대회 개최 (뉴시스, Sun, 06 Se) — https://news.google.com/rss/articles/CBMiYEFVX3lxTE9ZakJZMlRhb041TjRzMlNtNWI5MnVMemhCcVpmUy1MSWpCYjYxOGtENWtIZlFPY3VsYlEtYUxxQzh5OE9RV3FGV1hhaXd0cXUtSVhyXzBiUmJwZ0lQTHRUbNIBeEFVX3lxTE5HYUlnUS1Gb2JPeURjNHZrelM5dmtfODMyX0VseWJ4ZDJTcHVKX0dNRjJmdTdPZzl0QUxxamNvamtvenZjakFiQ3BsTlJ2YWlXX2p6aEpuUk5xTDk4cGJyQTJxWTdDQ2VWYnhXTDVQS1VFVUFQM0RSZw?oc=5
- 야영장 안전위반 확인후 미조치…지자체가 '무보험' 드론 운용 (연합뉴스, Wed, 30 Se) — https://news.google.com/rss/articles/CBMiW0FVX3lxTE00c19UQmVtUWVpV1pFY1J1TUhmTnFvZTdiejY2NWNNajNlU05mNWFmN09jR3pFUTVYTHRUblVYTDItaU03ODItRFJPWG9tU3VzdUNQYXE1N29iT2vSAWBBVV95cUxPV2U2b1lURV9zaWVTMHhtSmRTUWszVnFWTXAxblN2dld3OVliTFFFdGNJcnZFWTd2ejV1dFJwNGdrX1J5WElXUkppRDhsSERZc1k4ekF5bXRRclNJaWZhY1M?oc=5
