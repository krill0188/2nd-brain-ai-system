---
title: "Sparc-Nart"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [path-planning, swarm-networking, aerial-robotics, sparse-aware-cooperative, radio-technology]
sources: ["raw/papers/drone-sw/path-planning-optimisation-for-sparse-aware-and-cooperative-networked-aerial-rob.md"]
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Sparc-Nart

**Sparc-Nart**는 사전 정보가 부정확하거나 불완전할 경우 온라인 분산 의사결정 및 그룹의 저항성을 지원하는 네트워크형 항공 로봇 팀(NART)의 성능을 극대화하도록 설계된 경로 계획 최적화 도구 및 탐사 임무 프레임워크입니다. 이 도구는 환경에 대한 다양한 수준의 사전 정보, 제한된 에이전트 에너지, 센싱, 통신 기능 및 다양한 NART 구성을 동시에 고려합니다.

## 개요

본 논문은 무선 링크로 연결된 에이전트(예: UAV, 지상 통제국) 그룹인 네트워크형 항공 로봇 팀(NART)의 경로 계획을 최적화하는 데 중점을 둡니다. 특히 간헐적인 인터-에이전트 연결성(희소성)을 고려하여, prior knowledge의 한계를 보완하고 협력적 행동을 인센티브화하여 임무 효율을 향상시키는 오프라인 미션 플래닝 단계를 제안합니다. SpArC-NART 도구는 라디오 기술의 제한물리적 현상을 반영하는 통신 모델을 적용하며, 에이전트 에너지 제한 및 소프트 모션 제약 조건을 반영하여 탐사 임무에서 미션 목표(예: 목표 발견 등)를 극대화합니다.

## 핵심 파라미터

| 파라미터 | 설명 |
|---|---|
| Path Planning Optimisation | 환경 사전 정보, 에이전트 에너지, 센싱, 통신 조건을 종합적으로 고려한 경로 최적화 |
| Communication Model | 사용자 정의 라디오 기술 및 물리적 현상 제한을 반영한 연결 모델 |
| Soft-Motion Constraints | 에이전트의 물리적 운동 제약 조건 |
| Value Of Movement | 이동 가치 평가 지표 |

## 활용처

- **Exploration Missions**: 사전이 불확실한 환경에서의 탐사 임무 수행
- **Cooperative Behaviours**: 에이전트 간의 협력적 행동 지원 및 그룹 저항성 증대
- **Decentralised Decision-Making**: 분산된 환경에서 온라인 의사결정 지원

## 관련 페이지

- [[Nart]] — Sparc-Nart가 구현하는 기반이 되는 네트워크형 항공 로봇 팀 개념
- [[Path Planning]] — SpArC-NART가 적용하는 경로 계획 최적화 기술

## 출처

- (사용자 재확인 필요) — 원문: Conceição, Maria; Grilo, António; Basiri, Meysam (2026). "Path Planning Optimisation for SParse, AwaRe and Cooperative Networked Aerial Robot Teams (SpArC-NARTs)". arXiv:2602.14247. https://arxiv.org/abs/2602.14247v2

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
