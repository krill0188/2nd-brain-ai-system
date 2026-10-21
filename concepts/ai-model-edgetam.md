---
title: "EdgeTAM: On-Device Track Anything Model"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: PerceptionModel
tags: [drone, ai, segmentation, video-tracking, on-device]
sources: [inbox/processed/hw-20261021-model-edgetam.md]
confidence: medium
contested: false
contradictions: []
---

# EdgeTAM: On-Device Track Anything Model

- 원문: https://arxiv.org/abs/2501.07256^[inbox/processed/hw-20261021-model-edgetam.md]
- 제작: Meta 계열 (Chong Zhou 외 11명)^[inbox/processed/hw-20261021-model-edgetam.md]

## 핵심 사양 (초록)
| 항목 | 값 |
|---|---|
| J&F | DAVIS 2017 87.7 / MOSE 70.0 / SA-V val 72.3 / SA-V test 71.7 |
| 속도 | 16 FPS on iPhone 15 Pro Max |
| 기법 | 2D Spatial Perceiver로 프레임 메모리 압축 (메모리 어텐션이 지연 병목), 증류 파이프라인 |
SAM 2 기반. 제출 2025-01-13.^[inbox/processed/hw-20261021-model-edgetam.md]
## 비고(미확인)
파라미터 수, 라이선스, Jetson 수치 초록에 없음(미확인). 드론 적용 미확인.^[inbox/processed/hw-20261021-model-edgetam.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
