---
title: "Distilling the Knowledge in a Neural Network"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, ai, model-compression, distillation, edge-inference]
sources: [inbox/processed/hw-20261021-ai-compression-distillation-hinton-2015.md]
confidence: medium
contested: false
contradictions: []
---

# Distilling the Knowledge in a Neural Network

- 원문: https://arxiv.org/abs/1503.02531^[inbox/processed/hw-20261021-ai-compression-distillation-hinton-2015.md]
- 저자: Geoffrey Hinton, Oriol Vinyals, Jeff Dean^[inbox/processed/hw-20261021-ai-compression-distillation-hinton-2015.md]
- 발행: 2015-03-09 (NIPS 2014 Deep Learning Workshop)^[inbox/processed/hw-20261021-ai-compression-distillation-hinton-2015.md]

## 핵심 내용
앙상블의 지식을 배포하기 쉬운 단일 모델로 압축하는 증류 기법. MNIST 결과와 상용 음향 모델 개선을 보이고, 전체 모델과 세밀 클래스를 담당하는 다수의 specialist 모델 앙상블도 제안(specialist는 빠르게 병렬 학습 가능).^[inbox/processed/hw-20261021-ai-compression-distillation-hinton-2015.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 정량 수치는 초록에 없음.^[inbox/processed/hw-20261021-ai-compression-distillation-hinton-2015.md]
- 시사점: 큰 검출/제어 모델을 엣지용 소형 모델로 옮기는 기본 기법.^[inbox/processed/hw-20261021-ai-compression-distillation-hinton-2015.md]

## 한계·미확인
수치·드론 적용 미확인.^[inbox/processed/hw-20261021-ai-compression-distillation-hinton-2015.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[companion-computer]]
