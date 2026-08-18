---
title: Test-Time Scaling VLM for UAV Navigation
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [voice-control, drone, ai-agent, vlm, navigation]
sources: [raw/papers/voice-control/fetch-2026-08-19-arxiv-no-training-better-flights-test-time-scaled-vlms-for-uav-nav.md]
confidence: high
contested: false
contradictions: []
---

# Test-Time Scaling VLM for UAV Navigation

Vision-Language Model(VLM)의 추론 성능을 추가 학습 없이 개선하는 테스트 시간 스케일링 방법론을 UAV 비전-언어 내비게이션(VLN)에 적용한 기술이다.

## 핵심 아이디어

기존 VLN 접근법은 단일 추론 패스에 의존하여 복잡한 환경에서 최적이 아니거나 안전하지 않은 경로를 생성할 수 있다. 본 방법은 반복적 정제 과정을 통해 모델이 초기 내비게이션 계획을 재평가하도록 유도한다.

## 방법론

1. **병렬 후보 생성**: 모델에 여러 후보 경로를 동시에 생성하도록 프롬프트
2. **자가 교정 단계**: 초기 계획을 재평가하여 더 깊고 강건한 계획 수립
3. **다중 기준 평가**: 안전성, 목표 정렬, 전진 진행도를 기준으로 후보 평가

## 장점

- **추가 학습 불필요**: 기본 모델을 변경하지 않고 동결된 VLM 사용
- **자가 교정**: 모델이 자체 계획을 재평가하고 개선
- **SOTA 성능**: UAV 내비게이션 작업에서 최고 성능 달성

## 관련 개념

- [[voice-control-drone]] — 음성 명령 드론 인터페이스
- [[drone-ai-agents]] — 드론 AI 에이전트 아키텍처
- [[llm-enabled-uav-natural-language-navigation]] — LLM 기반 UAV 자연어 내비게이션
