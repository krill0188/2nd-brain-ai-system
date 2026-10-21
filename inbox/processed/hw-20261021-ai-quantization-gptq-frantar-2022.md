---
title: "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: edge-ai-compute
source: https://arxiv.org/abs/2210.17323
authors: Elias Frantar, Saleh Ashkboos, Torsten Hoefler, Dan Alistarh
published: 2022-10-31 (v2 2023-03-22, ICLR 2023)
tags: [drone, ai, quantization, llm, model-compression]
---
## 핵심 내용
근사 2차 정보를 쓰는 one-shot 가중치 양자화. 1750억 파라미터 GPT를 약 4 GPU 시간에 양자화하고, 가중치를 3~4비트로 줄여도 정확도 손실이 미미하다. 2비트·ternary에서도 쓸 만한 정확도. 이전 one-shot 방식의 압축 이득을 2배 이상으로 높이고 175B 모델의 단일 GPU 생성 추론을 가능케 한다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- FP16 대비 추론 속도 약 3.25x(NVIDIA A100), 4.5x(NVIDIA A6000).
- 3~4비트에서 정확도 손실 미미(원문 표현).

## 한계·미확인
엣지 디바이스(Jetson) 수치 없음(미확인). 드론 직접 적용 없음.
