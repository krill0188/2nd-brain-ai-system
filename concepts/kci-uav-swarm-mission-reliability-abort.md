---
title: "재구성형 UAV 스웜의 임무 중단을 고려한 임무 신뢰도 모델링 및 평가"
created: 2026-09-12
updated: 2026-09-12
type: concept
domain: ai-autonomy
tags: [drone, swarm, ai-autonomy]
sources: [raw/papers/swarm/mission-reliability-modeling-and-evaluation-for-reconfigurable-uav-swarm-conside.md]
confidence: low
contested: false
contradictions: []
---

# 재구성형 UAV 스웜의 임무 중단을 고려한 임무 신뢰도 모델링 및 평가

다단계(phased) 임무를 수행하는 재구성 가능한 UAV 스웜을 대상으로, 단계별 운용 조건·스트레스
변화에 따라 노드 고장률이 달라지는 상황을 반영한 임무 신뢰도 모델링·평가 프레임워크. 동적
재구성과 임무 중단(mission abort) 결정을 통합한 협조적 프레임워크를 제안한다.

## 핵심 메커니즘

- **재구성 전략**: 노드 교체와 링크 재구성을 통해 'detect-decide-engage' 루프를 복원.
- **임무 중단 정책**: 실시간 유효 표적 커버리지 비율(effective target coverage ratio)로 트리거.
- **단계별 중단 임계값 최적화**: 시뮬레이티드 어닐링(simulated annealing) 알고리즘으로 임무
  성공 확률과 자원 보존(resource conservation) 사이의 균형을 최적화.
- 사례 연구를 통해 접근법의 동적 적응성을 검증.

## 참고

원문이 KCI 페이월 뒤에 있어 초록 일부만 확보됨(single-source, 발췌 abstract 기반). 방법론
세부사항(고장률 모델, 사례 연구 파라미터)은 원문 접근 후 보강 필요.

## 관련 개념

- [[game-theoretic-drone-swarm-defense]] — 게임이론 기반 드론 스웜 방어 전술 효과 분석
- [[swarmnxt-aerial-swarm-platform]] — 오픈소스 SW-HW 애자일 공중 스웜 플랫폼
- [[kci-manned-unmanned-teaming-defensive-air-ops]] — 유·무인 복합 편대 임무 효과도 분석
