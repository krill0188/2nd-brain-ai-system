---
title: "LLM 전략 파라미터 생성 기반 상황 적응형 군집 무인기 임무 할당"
created: 2026-09-06
updated: 2026-09-06
type: concept
domain: ai-autonomy
tags: [drone, swarm, ai-agent, ai-autonomy]
sources: [raw/papers/_unclassified/대규모-언어-모델-기반의-전략적-파라미터-생성을-통한-상황-적응형-군집-무인기-임무-할당.md]
confidence: medium
contested: false
contradictions: []
---

# LLM 전략 파라미터 생성 기반 상황 적응형 군집 무인기 임무 할당

대형 언어 모델(LLM)과 합의 기반 번들 알고리즘(Consensus-Based Bundle Algorithm, CBBA)을 결합한
계층형 하이브리드 의사결정 아키텍처를 제안하는 연구다 ^[raw/papers/_unclassified/대규모-언어-모델-기반의-전략적-파라미터-생성을-통한-상황-적응형-군집-무인기-임무-할당.md].
다중 UAV 임무 할당에서 "전략적 의도"와 "수치적 제어" 사이의 의미적 간극을 메우는 것이 목적이다.

## 아키텍처

- **상위 계층 — LLM 전략 플래너**: 동적 이벤트의 의미적 맥락을 해석하고 고수준 전략 파라미터를 생성.
- **하위 계층 — CBBA 분산 실행**: LLM이 생성한 전략 파라미터를 입력으로 받아 탈중앙화된 방식으로
  실제 임무 할당을 수행.
- 전통적인 규칙 기반 최적화 알고리즘은 경직된 로직 때문에 예측 불가능한 상황 변화에 유연하게
  적응하지 못한다는 한계를 LLM 전략 계층이 보완하는 구조.

## 의의

LLM을 하위 실행 알고리즘(CBBA)의 파라미터 튜너/전략가로 배치해 "해석 가능한 고수준 의사결정"과
"검증된 분산 최적화 실행"을 분리한 하이브리드 패턴으로, 순수 LLM 직접 제어나 순수 규칙 기반
최적화 각각의 한계(설명 불가능성 vs. 경직성)를 절충한다.

## 관련 개념

- [[uav-swarm-ai-trends-kci]] — MARL부터 LLM까지 UAV 군집 AI 아키텍처 진화 개관
- [[swarm-coordination]] — Leader-Follower 구조 및 편대 비행 협업 구조
- [[drone-ai-agents]] — 자율 의사결정 및 다중 에이전트 협력 아키텍처
