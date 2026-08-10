---
title: "Rigid-Covert GNSS Spoofing: UAV 군집의 구조적 탐지 사각지대"
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [drone, swarm, paper, security]
domain: ai-autonomy
sources: [raw/papers/swarm/rigid-covert-gnss-spoofing-of-uav-swarms-a-structural-blind-spot-its-detection-l.md]
confidence: high
contested: false
contradictions: []
---

# Rigid-Covert GNSS Spoofing: UAV 군집의 구조적 탐지 사각지대

Park & Yoo(2026, arXiv:2608.06885)가 밝힌 UAV 군집 GNSS 스푸핑 방어의 구조적 약점. 협력 드론 군집이 GNSS 위치를 상대 기하(inter-drone geometry)와 교차검증하는 흔한 방식에는 근본적 사각지대가 있다 — 모든 드론에 공통으로 서서히 걸리는 이동(rigid-covert shift, "RigidShift")은 드론 간 쌍별 거리를 그대로 보존하므로, 상대 기하만 보는 탐지기에는 **관측 불가능**하다(게이지-자유도 논증).^[raw/papers/swarm/rigid-covert-gnss-spoofing-of-uav-swarms-a-structural-blind-spot-its-detection-l.md]

## 핵심 주장

- **탐지 사각지대 실증**: 거리검증·준정부호실현가능성(SDP-feasibility) 기반 탐지기에서 이 사각지대를 검증. 기체 관성/GNSS 모니터는 "경보"는 울릴 수 있어도 군집의 진짜 위치는 복구 못 함과 구분
- **검출 하한 도출**: 외부 기준(anchor)이 있을 때 관측성이 회복되는 시점의 드리프트 종속 검출 하한 $2\gamma/(1-t_s/T)$를 도출, 실측 노이즈 하한(기울기 2.66, 예측치 2.67)까지 확인
- **앵커 기반 복구 파이프라인**: 드론 간 거리로 군집 기하를 재구성 → 신뢰 앵커 서브셋에 비잔틴-강건 피팅으로 정렬 → 비앵커 드론의 절대 위치 복구. 클린 에폭 라벨이 없을 때도 앵커 드리프트·공격률·시작시점을 동시 추정하는 분할 추정기 포함

## 검증 결과

- 통계 시뮬레이션 + ArduPilot SITL + Gazebo(렌더링 비전 앵커) 실험
- 비앵커 드론 위치 복구: GNSS 드리프트 약 10.1m 상황에서 중앙값 오차 0.39m(시드 20개), 렌더링-비전 멀티-SITL 환경에서는 7.1cm(시드 5개)
- RF 스푸핑 하드웨어나 실물 군집 없이 전부 시뮬레이션 기반 — 저자들도 이 한계를 명시

## 관련 개념

- [[decentralized-swarm-gps-denied]] — GPS 거부 환경 분산 스웜 제어
- [[swarm-coordination]] — 드론 군집 협조 제어 일반
