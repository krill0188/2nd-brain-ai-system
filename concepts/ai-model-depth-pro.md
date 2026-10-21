---
title: "Depth Pro: Sharp Monocular Metric Depth in Less Than a Second"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: PerceptionModel
tags: [drone, ai, monocular-depth, perception]
sources: [inbox/processed/hw-20261021-model-depth-pro.md]
confidence: medium
contested: false
contradictions: []
---

# Depth Pro: Sharp Monocular Metric Depth in Less Than a Second

- 원문: https://arxiv.org/abs/2410.02073^[inbox/processed/hw-20261021-model-depth-pro.md]
- 제작: Apple (Aleksei Bochkovskii 외, ICLR 2025)^[inbox/processed/hw-20261021-model-depth-pro.md]

## 핵심 사양 (초록)
- 제로샷 단안 미터법(metric) 깊이 파운데이션 모델. 2.25-megapixel 깊이 맵을 표준 GPU에서 0.3초에 생성.^[inbox/processed/hw-20261021-model-depth-pro.md]
- 카메라 내부 파라미터 같은 메타데이터 없이 절대 스케일 깊이 출력, 경계 정확도 강조.^[inbox/processed/hw-20261021-model-depth-pro.md]
- 제출 2024-10-02, v2 2025-04-21.^[inbox/processed/hw-20261021-model-depth-pro.md]
## 비고(미확인)
파라미터 수, 라이선스, 엣지 속도(0.3초는 'standard GPU' 기준, 기종 미확인) 초록에 없음. 0.3초는 고속 제어 루프에 직접 쓰기엔 길다는 점에 유의(원문 수치만 기재). 드론 적용 미확인.^[inbox/processed/hw-20261021-model-depth-pro.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
