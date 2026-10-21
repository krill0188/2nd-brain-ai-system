---
title: "SAM 2 / SAM 2.1 (Segment Anything Model 2)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: PerceptionModel
tags: [drone, ai, segmentation, video, tracking]
sources: [inbox/processed/hw-20261021-model-sam2.md]
confidence: medium
contested: false
contradictions: []
---

# SAM 2 / SAM 2.1 (Segment Anything Model 2)

- 원문: https://github.com/facebookresearch/sam2^[inbox/processed/hw-20261021-model-sam2.md]
- 제작: Meta FAIR^[inbox/processed/hw-20261021-model-sam2.md]

## 핵심 사양 (README 표)
| 체크포인트(SAM 2.1) | Size (M) | FPS | SA-V test J&F | MOSE val J&F | LVOS v2 J&F |
|---|---|---|---|---|---|
| hiera_tiny | 38.9 | 91.2 | 76.5 | 71.8 | 77.3 |
| hiera_small | 46 | 84.8 | 76.6 | 73.5 | 78.3 |
| hiera_base_plus | 80.8 | 64.1 | 78.2 | 73.7 | 78.2 |
| hiera_large | 224.4 | 39.5 | 79.5 | 74.6 | 80.6 |
SAM 2(2024-07-29)도 유사: tiny 38.9M/91.5 FPS ... large 224.4M/39.7 FPS.^[inbox/processed/hw-20261021-model-sam2.md]
## 조건 / 라이선스
FPS는 A100, torch 2.5.1, CUDA 12.4에서 모델 구성요소 컴파일 후 측정. 체크포인트·데모·학습 코드 Apache 2.0.^[inbox/processed/hw-20261021-model-sam2.md]
## 비고(미확인)
"Size (M)"가 파라미터 수인지 README가 명시하지 않음. Jetson 수치, 드론 적용 사례 미확인.^[inbox/processed/hw-20261021-model-sam2.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
