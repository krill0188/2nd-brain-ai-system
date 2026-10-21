---
title: "MobileSAM (Faster Segment Anything: Towards Lightweight SAM for Mobile Applications)"
created: 2026-10-21
captured: 2026-10-21
type: product
category: ai-model
manufacturer: Chaoning Zhang 외 (Kyung Hee Univ. 등)
domain: edge-ai-compute
source: https://arxiv.org/abs/2306.14289
tags: [drone, ai, segmentation, distillation, edge-inference]
---
## 핵심 사양 (초록)
- ViT-H 이미지 인코더를 경량 인코더로 대체(지식 증류). 원본 SAM보다 60배 이상 작음('more than 60 times smaller'), 정확한 파라미터 수는 초록에 없음.
- 속도: 단일 GPU에서 이미지당 약 10 ms(이미지 인코더 8 ms, 마스크 디코더 4 ms 표기). 원본 SAM과 대등한 성능이라 주장. FastSAM보다 약 5배 빠르고 7배 작음. CPU에서 비교적 원활 구동 주장.
- 학습 단일 GPU 하루 미만. 제출 2023-06-25.
## 비고(미확인)
GPU 기종, 라이선스, Jetson 수치 미확인. 드론 적용 미확인.
