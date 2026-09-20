---
title: Drone Software Stack Overview
created: 2026-08-06
updated: 2026-08-06
type: concept
tags: [drone-sw]
sources: []
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# Drone Software Stack Overview

드론 소프트웨어 스택 전반을 아우르는 도메인 개요 페이지. 비행 제어 펌웨어(PX4/ArduPilot), GCS, 미들웨어(MAVLink/ROS2), SDK 계층을 포함한다.

## 계층 구조

| 계층 | 대표 소프트웨어 |
|---|---|
| 비행 제어 펌웨어 | PX4, ArduPilot |
| 통신 프로토콜 | MAVLink, DroneCAN |
| 미들웨어/브릿지 | ROS2, MAVROS, MAVSDK |
| 지상 제어국(GCS) | QGroundControl, Mission Planner |
| 시뮬레이션 | SITL, Gazebo |

## 관련 개념

- [[px4-system-architecture]] — PX4 소프트웨어 아키텍처
- [[ardupilot-architecture]] — ArduPilot 아키텍처
- [[mavros]] — ROS↔MAVLink 브릿지

## 📰 최근 관련 소식
- Counter-UAS software upgrade demonstrated on U.S. Army air-defense system (Military Embedded Systems, Wed, 12 Au) — https://news.google.com/rss/articles/CBMivgFBVV95cUxOU2pZSUtKcGVoMWpnWnBQdjEzamRZdm9mclZqT0M3SUsxN1RyZHVDSEg4V0oteDE5Q2JDX2NOZWxBa3ZTUlAyX2dIckpuMFk4UXY0bVFySGg5b1J6Q01mRFBKNDk4akFqQkMyV2NubFZIb1VQbGFGVXlhRTdKeXRXWVJVWmhGOWFhTTFRQk5GYlFSQ2ZPRjdkN1N6ZWF4bGZfY3c2T3dqRE02QjU3UFFNSnZvZEY2cTdueGwzSW9n?oc=5
- [멈춤보단 천천히라도] [자막][3분 자료구조 #3] 스택 (Stack) — 나중에 넣은 게 먼저 나온다 (youtube.com, 2026-08-20) — https://www.youtube.com/watch?v=aJsL2W8wPro
- [멈춤보단 천천히라도] [3분 자료구조 #4] 큐 (Queue) — 줄 선 순서대로, FIFO (youtube.com, 2026-08-21) — https://www.youtube.com/watch?v=tycAcSbBUxc
- [멈춤보단 천천히라도] [3분 자료구조 #6] 덱 (Deque) — 양쪽 끝이 모두 열린 큐 (youtube.com, 2026-08-23) — https://www.youtube.com/watch?v=PFCCdiJMCe4
- [멈춤보단 천천히라도] [3분 자료구조 #5] 원형 큐 — 나머지 연산으로 배열을 무한히 재활용 (youtube.com, 2026-08-22) — https://www.youtube.com/watch?v=_AZqxG0BS9k
- [멈춤보단 천천히라도] 재귀 — 자기 자신을 부르는 함수 | 3분 알고리즘 #2 (youtube.com, 2026-09-05) — https://www.youtube.com/watch?v=X90eAB-s3lM
- [멈춤보단 천천히라도] 버블 정렬 — 거품처럼 떠오르는 최댓값 | 3분 알고리즘 #4 (youtube.com, 2026-09-07) — https://www.youtube.com/watch?v=GWOCNpTMzdk
- [멈춤보단 천천히라도] 러스트 Option과 Result — null 없는 언어가 실패를 다루는 법 | 러스트 입문 #6 (youtube.com, 2026-09-07) — https://www.youtube.com/watch?v=2KI6wW8z0H8
- [멈춤보단 천천히라도] 병합 정렬 — 쪼개서 정복하는 O(n log n) | 3분 알고리즘 #7 (youtube.com, 2026-09-10) — https://www.youtube.com/watch?v=TZPSTBHIPM4
- [멈춤보단 천천히라도] 러스트 생명주기 — 허공에 매달린 참조를 잡는 법 | 러스트 입문 #9 (youtube.com, 2026-09-10) — https://www.youtube.com/watch?v=NwKJrn4NyA0
- [멈춤보단 천천히라도] 러스트 trait — 상속 대신 자격증, derive의 정체 | 러스트 입문 #10 (youtube.com, 2026-09-11) — https://www.youtube.com/watch?v=q-X5UdfCrjE
- [멈춤보단 천천히라도] 퀵 정렬 — 실전 최강자의 비밀, 피벗 | 3분 알고리즘 #8 (youtube.com, 2026-09-11) — https://www.youtube.com/watch?v=OXNDcpR7HcI
- [멈춤보단 천천히라도] DP — 한 번 구한 답은 기억한다 | 3분 알고리즘 #15 (youtube.com, 2026-09-18) — https://www.youtube.com/watch?v=eYO62e2alYA
- [멈춤보단 천천히라도] 3분 알고리즘 — 애니메이션으로 배우는 알고리즘 기초 (youtube.com, 2026-09-18) — https://www.youtube.com/watch?v=WII-LeqSI58
