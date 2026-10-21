---
title: "UAV-VLA: Vision-Language-Action System for Large Scale Aerial Mission Generation"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: AIModel
tags: [drone, ai, vla, uav, mission-planning, vlm]
sources: [inbox/processed/hw-20261021-model-uav-vla.md]
confidence: medium
contested: false
contradictions: []
---

# UAV-VLA: Vision-Language-Action System for Large Scale Aerial Mission Generation

- 원문: https://arxiv.org/abs/2501.05014^[inbox/processed/hw-20261021-model-uav-vla.md]
- 제작: Skoltech 계열 (Oleg Sautenkov 외, HRI 2025)^[inbox/processed/hw-20261021-model-uav-vla.md]

## 핵심 사양 (초록)
- 위성 영상 처리 + VLM + GPT로 텍스트 요청을 비행 경로·행동 계획으로 변환.^[inbox/processed/hw-20261021-model-uav-vla.md]
- 보고 수치: 궤적 길이 차이 22%, 지도상 목표 물체 위치 평균 오차 34.22 m (Euclidean, KNN 방식).^[inbox/processed/hw-20261021-model-uav-vla.md]
- 제출 2025-01-09, v2 2025-05-13 (arXiv:2501.05014).^[inbox/processed/hw-20261021-model-uav-vla.md]
## 비고(미확인)
22% 차이의 기준(비교 대상), 벤치마크 데이터셋, 파라미터·라이선스·엣지 속도 미확인.^[inbox/processed/hw-20261021-model-uav-vla.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]
