---
title: LLM Swarm WoT Framework
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [swarm, ai-agent, drone, llm, wot]
sources: [raw/papers/swarm/fetch-2026-08-19-arxiv-say-the-mission-execute-the-swarm-agent-enhanced-llm-reasoni.md]
confidence: high
contested: false
contradictions: []
---

# LLM Swarm WoT Framework

자연어로 표현된 임무 목표를 자율적으로 실행하는 UAV 스웜 제어를 위한 에이전트 기반 LLM 프레임워크이다. W3C Web of Things(WoT) 표준을 기반으로 한 Web-of-Drones 추상화를 사용한다.

## 아키텍처

- **LLM 기반 에이전트 코어**: 고수준 추론 엔진
- **MCP(Model Context Protocol) 게이트웨이**: 표준화된 인터페이스
- **WoT 기반 추상화**: 드론, 센서, 서비스를 표준화된 WoT Things로 노출

## 핵심 기능

- **자연어 임무 지정**: 사용자가 자연어로 임무 목표 표현
- **구조화된 도구 기반 상호작용**: 코드 생성 없이 안전한 작동
- **지속적 상태 관찰**: 실시간 피드백 루프
- **실시간 폐쇄 루프 실행**: 장기 실행 지원

## 평가 결과

ArduPilot 기반 시뮬레이션에서 4가지 스웜 임무와 6개의 SOTA LLM으로 평가:

- 일반 목적 LLM은 명시적 구현 지원 없이는 단순 스웜 작업에서도 신뢰할 수 있는 실행에 어려움
- 작업별 계획 도구와 런타임 가드레일이 강건성을 크게 향상
- 토큰 소비만으로는 실행 품질이나 신뢰성을 나타내지 않음

## 관련 개념

- [[swarm-coordination]] — 스웜 협업 및 편대 비행
- [[drone-ai-agents]] — 드론 AI 에이전트 아키텍처
- [[mavlink-protocol]] — MAVLink 통신 프로토콜
