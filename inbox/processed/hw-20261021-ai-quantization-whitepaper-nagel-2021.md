---
title: "A White Paper on Neural Network Quantization"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: edge-ai-compute
source: https://arxiv.org/abs/2106.08295
authors: Markus Nagel, Marios Fournarakis, Rana Ali Amjad, Yelysei Bondarenko, Mart van Baalen, Tijmen Blankevoort
published: 2021-06-15
tags: [drone, ai, quantization, ptq, qat, edge-inference]
---
## 핵심 내용
엣지 장치의 전력·지연 절감 수단으로서 양자화를 정리한 백서. PTQ는 재학습과 라벨이 필요 없고 8비트에서는 대체로 'close to floating-point accuracy'에 충분. QAT는 미세조정과 라벨 데이터가 필요하지만 더 낮은 비트에서 경쟁력을 유지. PTQ와 QAT 모두 검증된 파이프라인을 제시.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 8비트: PTQ로 충분(원문 주장). 더 낮은 비트: QAT 고려.
- 수치 표는 초록에 없음.

## 한계·미확인
구체 정확도·속도 수치는 본문 미열람(미확인).
