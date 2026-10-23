---
title: "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, ai, quantization, integer-inference, edge-inference]
sources: [inbox/processed/hw-20261021-ai-quantization-integer-only-jacob-2017.md]
confidence: medium
contested: false
contradictions: []
---

# Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference

- 원문: https://arxiv.org/abs/1712.05877^[inbox/processed/hw-20261021-ai-quantization-integer-only-jacob-2017.md]
- 저자: Benoit Jacob, Skirmantas Kligys, Bo Chen, Menglong Zhu, Matthew Tang, Andrew Howard, Hartwig Adam, Dmitry Kalenichenko^[inbox/processed/hw-20261021-ai-quantization-integer-only-jacob-2017.md]
- 발행: 2017-12-15^[inbox/processed/hw-20261021-ai-quantization-integer-only-jacob-2017.md]

## 핵심 내용
정수 연산만으로 추론하는 양자화 방식과, 양자화 후 정확도를 유지하는 공동 설계 학습 절차를 제안한다. 정확도-온디바이스 지연 트레이드오프를 개선하며 MobileNet에서도 유의미한 이득을 주장. ImageNet 분류와 COCO 검출을 'popular CPUs'에서 시연.^[inbox/processed/hw-20261021-ai-quantization-integer-only-jacob-2017.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 수치(정확도·지연·가속비)는 초록에 없음(미확인).^[inbox/processed/hw-20261021-ai-quantization-integer-only-jacob-2017.md]
- 시사점: 정수 전용 하드웨어(마이크로컨트롤러급)로 이식 가능한 양자화 경로.^[inbox/processed/hw-20261021-ai-quantization-integer-only-jacob-2017.md]

## 한계·미확인
ARM 등 구체 기기 수치 미확인.^[inbox/processed/hw-20261021-ai-quantization-integer-only-jacob-2017.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[companion-computer]]
