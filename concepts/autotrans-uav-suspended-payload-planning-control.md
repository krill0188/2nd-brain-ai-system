---
title: "AutoTrans: 현수 페이로드 UAV 계획·제어 프레임워크"
created: 2026-10-18
updated: 2026-10-18
type: concept
domain: flight-control
tags: [drone, drone-sw]
sources: [inbox/processed/fetch-2026-10-18-arxiv-autotrans-a-complete-planning-and-control-framework-for-auto.md]
confidence: medium
contested: false
contradictions: []
---

# AutoTrans (현수 페이로드 자율 운송)

**출처**: arXiv 2310.15050 (2023-10-23), Haojia Li 외 (Fei Gao, Boyu Zhou, Shaojie Shen 그룹). 초록 기준.

줄에 매단 페이로드를 운반하는 UAV는 기계 구조가 단순하고 민첩하지만 계획·제어가 어렵다. 논문은 이를 위한 통합 해법을 제시한다.^[inbox/processed/fetch-2026-10-18-arxiv-autotrans-a-complete-planning-and-control-framework-for-auto.md]

- **실시간 계획**: 시변 형상과 비선형 동역학을 고려해 매끄러운 궤적을 만들고 전신(whole-body) 안전과 동역학적 실현 가능성을 보장한다.
- **적응형 NMPC**: 계층적 외란 보상으로 미지의 외란과 부정확한 모델 파라미터를 극복한다.
- **실험**: 제약이 많은 환경에서도 온라인 궤적 생성, 상당한 불확실성 하에서도 공격적 궤적 추종이 가능하다고 보고한다. 코드 공개 예정이라 했으나 공개 여부는 초록에서 확인되지 않는다.

정량 지표는 초록에 없다. 관련: [[uav-cable-payload-cooperative-transport-research]], [[drone-payload-systems]].
