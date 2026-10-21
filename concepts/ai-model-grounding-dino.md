---
title: "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: PerceptionModel
tags: [drone, ai, object-detection, open-set, vlm]
sources: [inbox/processed/hw-20261021-model-grounding-dino.md]
confidence: medium
contested: false
contradictions: []
---

# Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection

- 원문: https://arxiv.org/abs/2303.05499^[inbox/processed/hw-20261021-model-grounding-dino.md]
- 제작: IDEA Research 등 (Shilong Liu 외 12명)^[inbox/processed/hw-20261021-model-grounding-dino.md]

## 핵심 사양 (초록)
- DINO 검출기 + grounded pre-training. 카테고리 이름이나 지칭 표현(referring expression)으로 지정한 객체 검출.^[inbox/processed/hw-20261021-model-grounding-dino.md]
- 구성: feature enhancer, language-guided query selection, cross-modality decoder.^[inbox/processed/hw-20261021-model-grounding-dino.md]
- COCO 제로샷 전이 52.5 AP(COCO 학습 데이터 없이), ODinW 제로샷 평균 26.1 AP('sets a new record').^[inbox/processed/hw-20261021-model-grounding-dino.md]
- 제출 2023-03-09, v5 2024-07-19.^[inbox/processed/hw-20261021-model-grounding-dino.md]
## 비고(미확인)
파라미터, 라이선스, 엣지 속도 초록에 없음(미확인). 드론 적용 미확인.^[inbox/processed/hw-20261021-model-grounding-dino.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
