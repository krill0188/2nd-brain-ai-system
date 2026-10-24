---
title: "AERIAL: 비행 네트워크용 임무 인지 LLM 선택 프레임워크"
created: 2026-10-24
updated: 2026-10-24
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, ai-agent, voice-control]
sources: [raw/papers/voice-control/aerial-mission-aware-llm-selection-for-language-driven-uav-control-in-flying-net.md]
confidence: low
contested: false
contradictions: []
---

# AERIAL: 비행 네트워크용 임무 인지 LLM 선택 프레임워크

Nunes 외, arXiv 2610.31029 (2026-10-22). **초록 기준**이며 본문 수치는 확인하지 못했다.

## 요지
- 문제: 비행 네트워크(Flying Networks)의 UAV가 자연어 목표를 실행 가능한 임무로 바꾸려면 LLM이 필요한데, 기존 방식은 모델 구성을 고정하고 임무에 따른 성능 편차를 무시한다.^[raw/papers/voice-control/aerial-mission-aware-llm-selection-for-language-driven-uav-control-in-flying-net.md]
- 방법: 모델 벤치마킹과 임무 실행을 분리한다. 벤치마크로 시나리오-모델 매핑을 경험적으로 만들고, 런타임에 임무에 맞는 모델을 고른다. 엣지-클라우드 혼합 구성을 전제로 한다.^[raw/papers/voice-control/aerial-mission-aware-llm-selection-for-language-driven-uav-control-in-flying-net.md]
- 평가: 항법·공간 추론·알고리즘 호출 시나리오에서 자동 시뮬레이션 720회를 돌렸고, 시나리오와 모델의 조합에 따라 성능 편차가 크게 나타났다고 보고한다.^[raw/papers/voice-control/aerial-mission-aware-llm-selection-for-language-driven-uav-control-in-flying-net.md]
- 사례 연구: 비행 네트워크 배치 알고리즘과 자연어로 연동해 도메인 최적화 모듈과의 인터페이스 가능성을 보였다고 한다.^[raw/papers/voice-control/aerial-mission-aware-llm-selection-for-language-driven-uav-control-in-flying-net.md]

## 위키 내 위치
단일 LLM을 고정하는 접근([[llm-enabled-uav-natural-language-navigation]])과 달리 임무별 모델 선택을 다룬다. 추론 지연·신뢰성 관점은 [[vlm-copilot-uav-navigation-latency-reliability]], 분산 LLM 통신 프레임워크는 [[aero-llm-framework]] 참조.

## 한계
선택 정책의 구체 기준, 사용한 LLM 목록, 실기체 검증 여부는 초록에 없다.
