---
title: "LLM-Enabled UAV Natural Language Navigation via STL"
created: 2026-08-12
updated: 2026-08-12
type: concept
tags: [drone, voice-control, ai-agent, llm, regulations]
domain: ai-autonomy
sources: [inbox/fetch-2026-08-12-arxiv-llm-enabled-low-altitude-uav-natural-language-navigation-via.md]
confidence: medium
contested: false
contradictions: []
---

# LLM-Enabled UAV Natural Language Navigation via STL

## 개요

저고도 UAV를 위한 자연어 내비게이션 프레임워크. 자연어 명령을 Signal Temporal Logic(STL) 사양으로 변환하고 안전한 궤적을 합성하는 통합 접근법.

## 핵심 기술

### NL-to-STL 변환
- **Chain-of-Thought(CoT) supervision**: 추론 강화된 LLM
- **GRPO(Group-Relative Policy Optimization)**: 높은 구문 유효성 및 의미 일관성 확보
- **MILP 기반 궤적 합성**: 공간-시간 제약 하에서 동적으로 실행 가능한 모션 계획

### 사양 복구 메커니즘
- MILP 기반 진단 + LLM 유도 의미 추론
- 엄격한 논리/공간 요구사항으로 인한 비실행성 해결
- 안전 보장을 유지하며 작업 제약 선택적 완화

## 시스템 특징

| 기능 | 설명 |
|------|------|
| 직관적 인터페이스 | 비전문가 운용자를 위한 자연어 입력 |
| 안전 임계 | 도시 환경에서 안전-임계 모션 계획 |
| 폐쇄 루프 | NL-to-STL 변환 강건성 향상 |
| 해석 가능성 | STL 기반 명확한 사양 표현 |

## 실험 검증

- 광범위한 시뮬레이션
- 실제 비행 실험
- 복잡한 시나리오에서 안전하고 해석 가능하며 적응 가능한 내비게이션 입증

## 관련 개념

- [[voice-control-drone]] — 음성 명령 인터페이스 및 MAVLink 매핑
- [[drone-ai-agents]] — 자율 의사결정 및 BDI 아키텍처
- [[utm-system]] — 저고도 공역 드론 교통관리 체계
- [[drone-regulations]] — FAA, EASA 규제 및 BVLOS

## 출처

Yuqi Ping et al., "LLM-Enabled Low-Altitude UAV Natural Language Navigation via Signal Temporal Logic Specification Translation and Repair", arXiv:2603.27583, 2026-03-29.
