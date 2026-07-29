---
title: "Distributed Continuous Aerial Surveillance by UAS Swarms"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, swarm, flight-control, ltl, surveillance]
sources: [inbox/fetch-2026-07-30-arxiv-distributed-continuous-aerial-surveillance-by-uas-swarms-und.md]
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# Distributed Continuous Aerial Surveillance by UAS Swarms

경계 Linear Temporal Logic(LTL) 미션 사양 하에서 분산 지속적 공중 감시를 위한 프레임워크. 다중 무인 항공 시스템(UAS)의 분산 협업과 연속적인 팀 재구성을 다룬다.

## 핵심 개념

### 시스템 아키텍처
- **정지 앵커(Stationary Anchors)**: 기준점 역할 수행
- **모바일 워커(Mobile Workers)**: 순환 교체 모드로 운용
- **DNN 기반 통신 토폴로지**: 완전 분산 협업 가능

### 미션 사양 (Bounded LTL)

| 사양 항목 | 설명 |
|-----------|------|
| 모드 간 참조 일관성 | 모드 전환 시 상태 유지 |
| 순환 팀 순환 | 주기적인 드론 교체 |
| 유한 시간 도달성 | 목표 지점 도달 보장 |
| 궤적 추적 | 계획된 경로 추적 |
| 감시 범위 | 처방된 감시 커버리지 |

## 정보 이론적 최적화

Kullback-Leibler 발산 최소화를 통한 감시 노드 분포와 유도된 커버리지 밀도 간 차이 최소화:

```
min KL(P_surveillance || P_coverage)
```

## 기술적 특징

- **온라인 통신 그래프 최적화 불필요**: 모드 종속적 결정론적 통신 토폴로지
- **분산 쿼드로터 컨트롤러**: 로컬 통신만으로 분산 참조 실현
- **유한 시간 수렴 보장**: 워커 에이전트 협업 역학의 수렴성 증명

## 검증 결과

- 순환 팀 재구성 시뮬레이션
- 분산 통신 토폴로지 합성
- 유한 시간 포메이션 수렴
- 인증된 지속적 감시 커버리지

## 관련 페이지

- [[swarm-coordination]] — 스웜 협업 및 편대 비행
- [[recon-swarm-project]] — 지능형 자율 군집정찰드론 프로젝트
- [[drone-simulation]] — 드론 시뮬레이션 환경
