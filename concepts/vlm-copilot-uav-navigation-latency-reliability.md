---
title: "UAV 항법 VLM 코파일럿: 스트레스 질의와 시간적 신뢰성 벤치마크"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-21-arxiv-stress-query-and-temporal-reliability-of-vision-language-mod.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 항법 VLM 코파일럿: 스트레스 질의와 시간적 신뢰성 벤치마크

Sodre 등(arXiv 2610.23877, 게시 2026-09-21)의 벤치마크 논문. 초록 기준 요약이며 모델명·수치는 확인하지 않았다.^[inbox/processed/fetch-2026-10-21-arxiv-stress-query-and-temporal-reliability-of-vision-language-mod.md]

- **문제**: VLM은 고수준 의미 추론을 주지만 추론 지연이 비행 제어를 불안정하게 만들 수 있다.
- **방법**: 고성능 워크스테이션과 내장 그래픽 노트북에서 모델 규모·하드웨어 제약·비행 신뢰성의 상충을 스트레스 테스트로 평가해 추론 지연의 운동학적 영향을 추론 정확도와 분리했다.
- **발견**: 경량 모델은 구조적 환각으로 결정론적 상태 기계를 깨뜨리고, 대형 모델은 추론 지연 탓에 궤적 과보정을 일으킨다. 중간 규모 모델이 균형이 가장 좋아 열화된 환경의 항법을 하드웨어 프로파일 전반에서 실시간 안정성 저하 없이 회복시켰다.

## 관련
[[llm-enabled-uav-natural-language-navigation]], [[test-time-scaling-vlm-uav]], 온보드 연산 제약은 [[companion-computer]].

## 📰 최근 관련 소식
- Stress-Query and Temporal Reliability of Vision-Language Models as copilots in Autonomous UAV Navigation (arxiv.org, 2026-09-21) — http://arxiv.org/abs/2610.23877v1
