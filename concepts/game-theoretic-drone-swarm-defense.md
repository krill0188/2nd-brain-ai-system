---
title: "게임이론 기반 드론 스웜 방어(차등 게임 응용 사례)"
created: 2026-09-08
updated: 2026-09-08
type: concept
domain: ai-autonomy
tags: [drone, ai-autonomy, swarm]
sources: [raw/papers/swarm/game-theoretic-drone-swarm-defense-a-case-study-in-applied-differential-game-the.md]
confidence: medium
contested: false
contradictions: []
---

# 게임이론 기반 드론 스웜 방어(차등 게임 응용 사례)

고가치 자산을 방어하는 드론 스웜이 침입 스웜을 요격하는 표적 할당·중간유도 문제를, 차등 게임(DG,
Differential Game) 이론으로 정식화한 연구다
^[raw/papers/swarm/game-theoretic-drone-swarm-defense-a-case-study-in-applied-differential-game-the.md].
침입 스웜을 합리적 행위자로 간주하고 방어자-침입자 간 내시균형을 탐색하는 게임이론 전술을,
방어측 기동만을 단방향 최적화하는 기존 베이스라인 전술과 비교했다.

## 방법

- Monte Carlo 시뮬레이션과 베이지안 분석으로 두 전술군의 요격 성공률을 비교.
- 침입 스웜이 회피 기동을 수행할 수 있는 시나리오를 별도로 검증.

## 결과

- 게임이론 전술은 베이스라인 대비 전체 침입자 요격 성공 확률이 더 높음.
- 침입 스웜이 회피 기동 가능한 경우 개선폭이 가장 두드러짐: 방어 성공률이 94.6%→96.8%로 상승,
  완전 방어까지 남은 격차의 약 41%를 해소.
- 페어 시행 베이지안 분석 결과, 이 시나리오에서 게임이론 전술이 베이스라인보다 우수할 사후확률은
  99.9%로 산출됨.

## 관련 개념

- [[swarm-coordination]] — 편대 비행 및 리더-팔로워 협업 구조
- [[distributed-aerial-surveillance-swarm]] — LTL 사양 기반 분산 지속 감시 스웜
- [[rigid-covert-gnss-spoofing-swarm]] — UAV 군집 GNSS 스푸핑 탐지 사각지대 분석(적대적 상황 대응 계열)
