---
title: "GPS 미수신 환경에 특화된 마이크로드론/UAV 위치추정 기법들은 공통적으로 외부 위치 인프라(GPS) 없이 온보드 카메라·IMU·옵티컬 플로우 등 상대적/자기완결적 센싱에만 의존한다는 특징을 공유한다."
created: 2026-08-01
updated: 2026-08-01
type: concept
tags: []
sources:
  - raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md
confidence: medium
domain: ai-agent
contested: false
contradictions: []
---
# GPS 미수신 환경에 특화된 마이크로드론/UAV 위치추정 기법들은 공통적으로 외부 위치 인프라(GPS) 없이 온보드 카메라·IMU·옵티컬 플로우 등 상대적/자기완결적 센싱에만 의존한다는 특징을 공유한다.

> 이 페이지는 인간 승인형 AI 연구 세션 `research/runs/20260801-research-1785543589`에서 마스터 승인을 거쳐 승격된 inference 클레임(`C11`)이다. 세션 원본 산출물은 `research/hypotheses/20260801-research-1785543589.md`, `research/reviews/20260801-research-1785543589.md`에 그대로 보존되어 있다.

## 주장

GPS 미수신 환경에 특화된 마이크로드론/UAV 위치추정 기법들은 공통적으로 외부 위치 인프라(GPS) 없이 온보드 카메라·IMU·옵티컬 플로우 등 상대적/자기완결적 센싱에만 의존한다는 특징을 공유한다.

## 근거

- [[decentralized-swarm-gps-denied]]
- [[visual-positioning-odometry]]
- ^[raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md]

## 검토 노트 (Critic)

- 반론/모순: 없음
- 한계: 세 출처 모두 상대적/자기완결적 센싱을 전제로 하지만, 이는 곧 절대 위치 기준 없는 드리프트 누적이라는 공통 취약점을 내포한다(C9 참고). 또한 decentralized-swarm-gps-denied는 군집간 통신 자체도 차단된 극단적 시나리오를 다뤄, "GPS 미수신"만을 다루는 다른 두 출처와 전제 조건이 다르다 — 세 출처를 하나의 공통 특징으로 묶는 것은 시나리오 이질성을 가릴 수 있다.

## 관련

[[decentralized-swarm-gps-denied]] [[visual-positioning-odometry]]

## 📰 최근 관련 소식
- 사우디 아람코 정유시설서 검은 연기…후티 반군 “드론 공격” 주장 (중앙일보, Sun, 09 Au) — https://news.google.com/rss/articles/CBMiVkFVX3lxTE9HUVdoVFBjc2J0aDdLUGQ5aGFSQm80dlpoV3ctZGFyNTJSSFRzdDdWSERPVVhLT3pra3lvQ0FQT0l5Wm8xclhoMk5kbHB3b2VNVDFuLTJ3?oc=5
