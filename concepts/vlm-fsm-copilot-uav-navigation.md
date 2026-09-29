---
title: "FSM-VLM 하이브리드 UAV 항법: GPS 미사용 환경의 지연·신뢰성 분석"
created: 2026-09-25
updated: 2026-09-25
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, ai-agent]
sources: [raw/papers/drone-ai/vision-language-models-as-copilots-for-autonomous-uav-navigation-analysis-of-lat.md]
confidence: medium
contested: false
contradictions: []
---

# FSM-VLM 하이브리드 UAV 항법

Sodre 외(arXiv 2609.26084, 2026-08-10)는 GPS 미사용 환경에서 결정론적 유한상태기계(FSM)가
저수준 물리 제어를 맡고, 비동기 VLM(Vision-Language Model) 코파일럿이 고수준 의미 기반
경로탐색을 맡는 하이브리드 제어 구조를 제안했다.^[raw/papers/drone-ai/vision-language-models-as-copilots-for-autonomous-uav-navigation-analysis-of-lat.md]

## 핵심 내용

- **구조 분리**: 실시간 폐루프 안정성은 FSM이 보장하고, VLM은 비동기로 의미 판단만 제공한다.
- **평가**: 파라미터 규모가 다른 3개 모델을 SITL 시뮬레이션에서 정상/열화 시나리오로 비교했다.
- **오류 분리 측정**: 형식 수준의 구문 오류(syntax error)와 논리 수준의 의미적 환각(hallucination)을 구분해 측정한다.
- **결론**: VLM의 안전한 비행 통합에서 병목은 순수 지연이 아니라 파라미터 규모(모델 크기)다.

## 한계

초록만 수집되어 구체 모델명, 수치 결과, 시나리오 설정은 확인되지 않았다.

## 관련 개념

- [[test-time-scaling-vlm-uav]] — UAV용 VLM 추론 시 스케일링 접근
- [[drone-ai-agents]] — 드론 AI 에이전트 개요
- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
