---
title: "물리 반영 트럭-드론 배송 계획 (최적화 + ML)"
created: 2026-10-18
updated: 2026-10-18
type: concept
domain: ops-mission
tags: [drone, ops-mission, drone-ai]
sources: [inbox/processed/fetch-2026-10-18-arxiv-physics-aware-truck-and-drone-delivery-planning-using-optimi.md]
confidence: medium
contested: false
contradictions: []
---

# 물리 반영 트럭-드론 배송 계획

**출처**: arXiv 2507.16259 (2025-07-22), Yineng Sun, Armin Fügenschuh, Vikrant Vaze. 초록 기준.

드론 비행 물리를 무시한 단순 모델은 트럭 경로 계획에서 최적이 아닌 배송 계획을 낳는다. 논문은 트럭 경로와 드론 궤적을 함께 계획하는 통합 정식화와 종단 해법을 제안한다.^[inbox/processed/fetch-2026-10-18-arxiv-physics-aware-truck-and-drone-delivery-planning-using-optimi.md]

- **방법**: 오프라인으로 푼 드론 궤적 최적화 해로 신경망을 학습해 드론 비행 시간을 근사하고, 그 근사를 기존 order-first-split-second 휴리스틱에 넣어 전체 배송 계획을 최적화한다. 궤적 최적화에는 운동학·에너지 식을 명시적으로 포함한다.
- **결과**: 합성 데이터와 실제 사례에서 비행 물리를 무시하는 최신 벤치마크보다 투어 시간과 드론 에너지 소비가 크게 개선된다고 보고한다. 연간 수백만 달러 절감 가능성을 언급하나 구체 수치는 초록에 없다.

관련: [[kci-drone-human-hybrid-delivery-milp]], [[payload-dependent-green-drone-routing]], [[multirotor-energy-power-models]].
