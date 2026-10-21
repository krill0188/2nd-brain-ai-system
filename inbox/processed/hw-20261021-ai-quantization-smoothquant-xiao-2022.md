---
title: "SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: edge-ai-compute
source: https://arxiv.org/abs/2211.10438
authors: Guangxuan Xiao, Ji Lin, Mickael Seznec, Hao Wu, Julien Demouth, Song Han
published: 2022-11-18 (v7 2024-03-29, ICML 2023)
tags: [drone, ai, quantization, w8a8, llm]
---
## 핵심 내용
학습이 필요 없는 PTQ로 W8A8(가중치·활성화 8비트) 양자화를 가능케 한다. 수학적으로 등가인 변환으로 활성화 이상치의 양자화 난이도를 가중치로 옮겨 활성화를 평탄화한다. OPT, BLOOM, GLM, MT-NLG, Llama-1/2, Falcon, Mistral, Mixtral에서 검증.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 최대 1.56x 추론 속도 향상, 최대 2x 메모리 감소, 정확도 손실 무시할 수준(원문).
- 530B LLM을 단일 노드에서 서빙 가능.

## 한계·미확인
엣지 기기 실측 없음(미확인). 속도 비교 기준 하드웨어 초록에 없음.
