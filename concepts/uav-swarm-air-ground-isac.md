---
title: "교차 지역 협력 기반 Air-Ground ISAC UAV 군집"
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [drone, swarm, paper]
domain: ai-autonomy
sources: [raw/papers/swarm/uav-swarming-for-air-ground-isac-via-cross-region-cooperation.md]
confidence: medium
contested: false
contradictions: []
---

# 교차 지역 협력 기반 Air-Ground ISAC UAV 군집

Miao & Gao(2026, arXiv:2607.26679)가 제안한 UAV 군집을 이용한 공중-지상 통합 센싱·통신(ISAC, Integrated Sensing and Communication) 프레임워크. 두 가지 핵심 과제 — (1) 동적이고 불균형한 지상 통신 수요, (2) 센싱 관측 다양성의 한계 — 를 교차 지역 협력 구조로 해결한다.^[raw/papers/swarm/uav-swarming-for-air-ground-isac-via-cross-region-cooperation.md]

## 핵심 설계

- **서비스 기반 지역 분할(regional partitioning)**: 트래픽 인지 UAV 통신을 지원하기 위해 지역을 나눠 관리
- **적응형 핸드셰이킹**: 지역 간 잔여 위상 오차를 동기화 오버헤드로 완화해 협력 센싱 정확도 향상
- **지역 단위 MAPPO(Multi-Agent Proximal Policy Optimization)**: 중앙집중 학습·분산 실행(CTDE) 구조로 교차 지역 협력 의사결정 수행

## 결과 (시뮬레이션)

- 통신 QoS(Quality of Service) 약 90% 달성
- Cramér-Rao Bound(CRB, 센싱 정밀도 하한) 기존 대비 약 45% 감소

## 관련 개념

- [[swarm-coordination]] — 드론 군집 협조 제어 일반
- [[datalink-communication]] — 드론 데이터링크·통신 기초
