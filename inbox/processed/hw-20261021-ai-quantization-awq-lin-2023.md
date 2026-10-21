---
title: "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: edge-ai-compute
source: https://arxiv.org/abs/2306.00978
authors: Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang, Wei-Ming Chen, Wei-Chen Wang, Guangxuan Xiao, Xingyu Dang, Chuang Gan, Song Han
published: 2023-06-01 (v6 2026-04-25, MLSys 2024 Best Paper)
tags: [drone, ai, quantization, on-device-llm, edge-inference]
---
## 핵심 내용
저비트 weight-only LLM 양자화 기법. 가중치가 아닌 활성화 통계로 중요 채널을 식별하며, 'Protecting only 1% salient weights can greatly reduce quantization error.' 중요 채널을 등가 변환으로 스케일업해 혼합 정밀도를 피한다. 역전파·재구성이 없어 보정 세트 과적합이 적다고 주장. 지시 튜닝 및 멀티모달 LM에 처음 적용. TinyChat은 4비트 온디바이스 LLM/VLM 추론 프레임워크.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 중요 가중치 1%만 보호해도 양자화 오차 크게 감소.
- TinyChat: Hugging Face FP16 구현 대비 'more than 3x speedup'(데스크톱·모바일 GPU), 70B Llama-2를 모바일 GPU에서 구동 가능.

## 한계·미확인
Jetson Orin 등 구체 기기 수치는 초록에 없음(미확인). 정확도 수치 본문 미열람.
