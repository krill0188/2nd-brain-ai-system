---
title: "NVIDIA Jetson Benchmarks 라이브 페이지(2026-10-22 열람): MLPerf Edge AGX Orin / Orin NX 지연·처리량, AGX Thor LLM·VLM 표"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge-inference, jetson-orin, jetson-thor, mlperf, tensorrt, latency, benchmark]
sources: [inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]
confidence: medium
contested: false
contradictions: []
---

# NVIDIA Jetson Benchmarks 라이브 페이지(2026-10-22 열람): MLPerf Edge AGX Orin / Orin NX 지연·처리량, AGX Thor LLM·VLM 표

- 원문: https://developer.nvidia.com/embedded/jetson-benchmarks^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]
- 저자: NVIDIA^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]
- 발행: 열람일 2026-10-22 (갱신일 미표기)^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]

## 핵심 내용
브라우저형 UA curl 로 받은 HTML 을 텍스트화해 표를 그대로 옮김. 이 라이브 페이지에는 Orin Nano 값과 YOLO류 모델 표가 없음(Orin Nano/NX/AGX 모델별 표는 Wayback 파일 참조).^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]

### MLPerf Inference v3.1 (JetPack 5.1.1, TensorRT 8.5.2, CUDA 11.4; AGX Orin Developer Kit 및 Orin NX 16GB)
열: AGX Orin(TensorRT) Single Stream Latency(ms) / Offline(samples/s) | Orin MaxQ Multi Stream Latency(ms)(원문 표기) / Offline / System Power(W) | Orin NX Offline | Orin NX MaxQ Offline / Power(W). 순서대로:^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]
| 작업 | AGX Orin SS 지연 ms | AGX Orin Offline | MaxQ 지연 ms | MaxQ Offline | MaxQ 전력 W | Orin NX Offline | NX MaxQ Offline | NX MaxQ 전력 W |
|---|---|---|---|---|---|---|---|---|
| ResNet (영상분류) | 0.64 | 6423.63 | 2.18 | 3526.29 | 23.57 | 2640.51 | 1681.87 | 14.95 |
| Retinanet (객체검출) | 11.67 | 148.71 | 82.92 | 74.71 | 22.27 | 66.5 | 47.59 | 15.57 |
| 3D-Unet-99.0 | 4371.46 | 0.51 | N/A | N/A | N/A | 0.2 | 0.19 | 22.04 |
| RNN-T | 94.01 | 1169.98 | N/A | N/A | N/A | 431.92 | 327.79 | 17.25 |
| BERT | 5.71 | 553.69 | N/A | N/A | N/A | 194.5 | 136.59 | 17.04 |
(열 대응은 원문 헤더 순서 기준의 읽기이며 원문 표는 열 병합이 단순화되어 있음 = 해석 일부 미확정.)^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]

### MLPerf v4.0 (AGX Orin Developer Kit, JetPack 5.1.1, TensorRT 9.0.1, CUDA 11.4)
| 작업 | Single Stream 지연 ms | Offline samples/s |
|---|---|---|
| GPT-J 6B (요약) | 10204.46 | 0.15 |
| stable-diffusion-xl | 12941.92 | 0.08 |

### MLPerf v3.0 (AGX Orin, TensorRT 8.5.0 프리뷰, CUDA 11.4): ResNet-50 SS 1538 / Offline 6438.10, Retinanet 51.57 / 92.40, BERT 144.36 / 544.24 등(이 표의 Single Stream 열은 samples/s 로 표기되어 v3.1의 지연(ms) 표와 단위가 다름).

### AGX Thor (JetPack 7.0, CUDA 13.0, TensorRT 10.13; vLLM, ISL/OSL 2048/128) tokens/sec, 동시성 1 / 8
Llama 3.1 8B 41.3 / 150.8; Llama 3.3 70B 4.7 / 12.6; Qwen 3 30B-A3B 61 / 226.4; Qwen 3 32B 13.19 / 79.1; Deepseek R1 7B 41.32 / 304.8; Deepseek R1 32B 13.31 / 82.6; Qwen2.5-VL 3B 71.7 / 356.86; Qwen2.5-VL 7B 45 / 252; Llama 3.2 11B Vision 26.31 / 69.63.^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- MLPerf Retinanet(검출류) AGX Orin 단일 스트림 지연 11.67 ms, Offline 148.71 samples/s. Orin NX Offline 은 66.5 samples/s(MaxQ 47.59, 15.57 W).^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]
- 큰 생성 모델은 AGX Orin 단일 스트림 지연이 수 초~십수 초(GPT-J 10204 ms, SDXL 12942 ms) — 온보드 폐루프 제어에 직접 쓸 수 없는 자릿수.^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]

## 한계·미확인
- 해상도·배치는 MLPerf 규정 기준이라 페이지에 미표기. Orin Nano 값 없음. 이 페이지의 MLPerf v3.1 Orin NX 는 16GB 로 명시(8GB 미확인). 신뢰도 높음(제조사 원문).^[inbox/processed/hw-20261022-data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
