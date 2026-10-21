---
title: "Depth Anything V2"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: PerceptionModel
tags: [drone, ai, monocular-depth, perception]
sources: [inbox/processed/hw-20261021-model-depth-anything-v2.md]
confidence: medium
contested: false
contradictions: []
---

# Depth Anything V2

- 원문: https://github.com/DepthAnything/Depth-Anything-V2^[inbox/processed/hw-20261021-model-depth-anything-v2.md]
- 제작: DepthAnything (HKU / TikTok 팀 저장소)^[inbox/processed/hw-20261021-model-depth-anything-v2.md]

## 핵심 사양 (README)
| 모델 | 파라미터 | 라이선스 |
|---|---|---|
| Small | 24.8M | Apache-2.0 |
| Base | 97.5M | CC-BY-NC-4.0 |
| Large | 335.3M | CC-BY-NC-4.0 |
| Giant | 1.3B (체크포인트 "coming soon") | CC-BY-NC-4.0 |
기본 추론 입력 크기 518. 모달리티: 단안 RGB -> 상대 깊이.^[inbox/processed/hw-20261021-model-depth-anything-v2.md]
## 비고(미확인)
README에 추론 시간 수치·벤치마크 수치 없음(DA-2K 평가는 별도 문서 링크). ONNX/TensorRT는 공식이 아닌 커뮤니티 프로젝트(fabio-sim/Depth-Anything-ONNX, spacewalk01/depth-anything-tensorrt). 드론 적용 사례 미확인. 상업 사용은 Small만 Apache-2.0.^[inbox/processed/hw-20261021-model-depth-anything-v2.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
