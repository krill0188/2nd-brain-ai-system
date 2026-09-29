---
title: "대드론 방어체계 소요산정: 확률적 대기행렬 모형"
created: 2026-09-25
updated: 2026-09-25
type: concept
domain: ai-autonomy
tags: [drone, swarm, ops-mission]
sources: [raw/papers/_unclassified/대드론-방어체계-소요산정에-관한-확률적-대기행렬-모형-연구.md]
confidence: medium
contested: false
contradictions: []
---

# 대드론 방어체계 소요산정: 확률적 대기행렬 모형

한만준(연세대 국방융합공학과, 전자공학회논문지 2026)은 드론 포화 공격을 c(G/D/1)
대기행렬로 모델링하고 Monte Carlo 시뮬레이션으로 방공체계 성능을 분석했다.^[raw/papers/_unclassified/대드론-방어체계-소요산정에-관한-확률적-대기행렬-모형-연구.md]

## 핵심 내용

- 이용률이 증가하면 실패확률이 **비선형**으로 증가한다.
- 다층 방공체계를 Queueing Network로 확장해 계층 간 부하 전이를 분석했고, 단일 체계보다 방어 성능이 우수했다.
- 위험 기반 최소 전력 수준과 비용-위험 균형 기반 최적 전력 수준을 도출했다.
- 다층 구조도 **비용 비대칭성**(저가 드론 vs 고가 요격체)은 근본적으로 해결하지 못한다.
- 향후 과제로 JADC2 기반 통합 방공망에서 AI 자원 할당과 G/D/c 협력 큐 구조를 제시했다.

## 한계

원문이 비공개(페이월)여서 초록만 근거로 했다. 수치·파라미터는 확인되지 않았다.

## 관련 개념

- [[drone-wall-defense-system]] — Drone Wall 기반 자율 대드론 방어체계
- [[dfend-counter-drone-worldcup]] — 월드컵 대드론 운용 사례
- [[drone-ai-agents]] — 드론 AI 에이전트
