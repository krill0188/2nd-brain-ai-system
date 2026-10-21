---
title: "Depth Anything V2"
created: 2026-10-21
captured: 2026-10-21
type: product
category: ai-model
manufacturer: DepthAnything (HKU / TikTok 팀 저장소)
domain: ai-autonomy
source: https://github.com/DepthAnything/Depth-Anything-V2
tags: [drone, ai, monocular-depth, perception]
---
## 핵심 사양 (README)
| 모델 | 파라미터 | 라이선스 |
|---|---|---|
| Small | 24.8M | Apache-2.0 |
| Base | 97.5M | CC-BY-NC-4.0 |
| Large | 335.3M | CC-BY-NC-4.0 |
| Giant | 1.3B (체크포인트 "coming soon") | CC-BY-NC-4.0 |
기본 추론 입력 크기 518. 모달리티: 단안 RGB -> 상대 깊이.
## 비고(미확인)
README에 추론 시간 수치·벤치마크 수치 없음(DA-2K 평가는 별도 문서 링크). ONNX/TensorRT는 공식이 아닌 커뮤니티 프로젝트(fabio-sim/Depth-Anything-ONNX, spacewalk01/depth-anything-tensorrt). 드론 적용 사례 미확인. 상업 사용은 Small만 Apache-2.0.
