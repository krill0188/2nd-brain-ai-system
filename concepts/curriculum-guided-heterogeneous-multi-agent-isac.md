---
title: "Curriculum-Guided Heterogeneous Multi-Agent Intelligence for Multi-UAV Cooperative ISAC"
created: 2026-08-12
updated: 2026-08-12
type: concept
tags: [drone, swarm, drone-ai, ai-agent, datalink]
domain: swarm
sources: [inbox/fetch-2026-08-12-arxiv-curriculum-guided-heterogeneous-multi-agent-intelligence-for.md]
confidence: medium
contested: false
contradictions: []
---

# Curriculum-Guided Heterogeneous Multi-Agent Intelligence for Multi-UAV Cooperative ISAC

## 개요

6G 네트워크에서 통신과 감지를 통합하는 ISAC(Integrated Sensing and Communication) 시스템을 위한 다중 UAV 협력 프레임워크. 이질적 에이전트(heterogeneous agents) 간 협업을 통해 공중-지상 통합 감지 및 통신을 구현한다.

## 핵심 개념

### 시스템 구성
- **이질적 에이전트**: 다수의 UAV와 지상 기지국(BS) 간 협업
- **목표**: 공동 표적 감지, 추적, 통신
- **최적화 문제**: PCRB(Posterior Cramer-Rao Bound) 최소화 + 통신 성능 제약

### C-HAPPO 알고리즘
Curriculum-based Heterogeneous-Agent Proximal Policy Optimization:
- 커리큘럼 학습으로 점진적 정책 개선
- Kronecker/QR 분해로 액션 차원 축소
- NP-hard 문제에 대한 확장 가능한 해결책

## 성능 향상

| 지표 | 개선률 |
|------|--------|
| 감지 성능 | +30% 이상 |
| 수렴 속도 | 더 빠름 |
| 추적 정확도 | 더 높음 |

## 관련 개념

- [[swarm-coordination]] — 스웜 드론 협업 및 편대 비행
- [[uav-isac-cross-region]] — 공중-지상 통합 ISAC 교차 지역 협력
- [[drone-ai-agents]] — 자율 의사결정 및 다중 에이전트 협력
- [[datalink-communication]] — RF, LTE 기반 드론 데이터링크

## 출처

Kang Yan et al., "Curriculum-Guided Heterogeneous Multi-Agent Intelligence for Multi-UAV Cooperative ISAC", arXiv:2605.17905, 2026-05-18.

## 📰 최근 관련 소식
- [freeCodeCamp.org] System Design for AI Agents – Building a Multi-Agent PR Reviewer (youtube.com, 2026-08-14) — https://www.youtube.com/watch?v=iqRcGCah0Kw
