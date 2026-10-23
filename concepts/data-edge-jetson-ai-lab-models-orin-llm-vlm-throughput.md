---
title: "Jetson AI Lab 2.0 Models 페이지 Performance Comparison: Orin AGX 64GB / NX 16GB / Nano 8GB LLM·VLM 생성 처리량 (페이지 내장 JSON)"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge-inference, jetson-orin, llm, vlm, vllm, llama-cpp, benchmark, jetson-ai-lab]
sources: [inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]
confidence: medium
contested: false
contradictions: []
---

# Jetson AI Lab 2.0 Models 페이지 Performance Comparison: Orin AGX 64GB / NX 16GB / Nano 8GB LLM·VLM 생성 처리량 (페이지 내장 JSON)

- 원문: https://www.jetson-ai-lab.com/models/^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]
- 저자: NVIDIA Jetson AI Lab^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]
- 발행: 열람일 2026-10-22 (페이지 갱신일 미표기)^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]

## 핵심 내용
jetson-ai-lab.com 의 Models 페이지는 JS 차트이지만 HTML 안에 `benchmarksData` JSON 이 내장되어 있어 curl 로 받아 값 전체를 추출함(브라우저 렌더링 없이 확인). 열람 방법: 브라우저형 UA curl -> JSON 파싱. 플랫폼 열: Thor T5000/T4000, AGX Orin 64GB, Orin NX 16GB, Orin Nano 8GB, DGX Spark. 아래는 Orin 3종 중 하나라도 값이 있는 행만 옮김(전체 31개 모델 중, 값이 null 인 칸은 "-").^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]
페이지 각주(그대로): "ISL/OSL for all benchmarks: 2048/128", "Unless otherwise specified, all models utilize W4A16 quantization for Orin and NVFP4 for Thor", "NVFP4 and MXFP4 require Blackwell FP4 tensor cores and are not available on Orin (Ampere)". Cosmos3 Edge 행은 ISL 1705/OSL 128, "streaming chat harness ... median of 3" 으로 다른 프로토콜. C=1/C=8 은 동시성(concurrency 1 / 8).^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]
수치 단위: 페이지 데이터·각주에 단위 키 없음 = 미확인(NVIDIA developer 벤치 페이지의 동일 ISL/OSL·동시성 표는 tokens/sec 로 표기되나, 이 페이지 단위는 직접 확인 못 함). JetPack/vLLM 버전도 미확인.^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]

| 모델 | ISL/OSL | 엔진 | 정밀도 | 동시성 | AGX Orin 64GB | Orin NX 16GB | Orin Nano 8GB |
|---|---|---|---|---|---|---|---|
| Nemotron Nano 9B V2 | 2048/128 | vLLM | W4A16 | C=1 | 20 | 11 | - |
| Nemotron Nano 9B V2 | 2048/128 | vLLM | W4A16 | C=8 | 85 | 60 | - |
| Nemotron 3 30B-A3B | 2048/128 | vLLM | W4A16 | C=1 | 35 | - | - |
| Nemotron 3 30B-A3B | 2048/128 | vLLM | W4A16 | C=8 | 71 | - | - |
| Nemotron3 Nano 4B | 2048/128 | llama.cpp | Q4_K_M GGUF | C=1 | 43 | 22 | 18 |
| Nemotron3 Nano 4B | 2048/128 | vLLM | W4A16 | C=1 | 26 | - | - |
| Nemotron3 Nano 4B | 2048/128 | vLLM | W4A16 | C=8 | 132 | - | - |
| Nemotron3 Nano 4B | 2048/128 | vLLM | BF16 | C=1 | 20 | - | - |
| Nemotron3 Nano 4B | 2048/128 | vLLM | BF16 | C=8 | 97 | - | - |
| Nemotron 3 Nano Omni | 2048/128 | llama.cpp | Q4_K_M GGUF | C=1 | 39.12 | - | - |
| Nemotron 3 Nano Omni | 2048/128 | llama.cpp | Q4_K_M GGUF | C=8 | 53.44 | - | - |
| Nemotron 3 Nano Omni | 2048/128 | Ollama | Q4_K_M | C=1 | 17 | - | - |
| Nemotron 3 Nano Omni | 2048/128 | Ollama | Q4_K_M | C=8 | 17 | - | - |
| Cosmos Reasoning 2 2B | 2048/128 | vLLM | W4A16 | C=1 | 59 | 25 | - |
| Cosmos Reasoning 2 2B | 2048/128 | vLLM | W4A16 | C=8 | 273 | 65 | - |
| Cosmos Reasoning 2 8B | 2048/128 | vLLM | W4A16 | C=1 | 19 | 6 | - |
| Cosmos Reasoning 2 8B | 2048/128 | vLLM | W4A16 | C=8 | 108 | 12 | - |
| Qwen 3 4B | 2048/128 | vLLM | W4A16 | C=1 | 50 | 17 | - |
| Qwen 3 4B | 2048/128 | vLLM | W4A16 | C=8 | 222 | 35 | - |
| Qwen 3 8B | 2048/128 | vLLM | W4A16 | C=1 | 30 | 9 | - |
| Qwen 3 8B | 2048/128 | vLLM | W4A16 | C=8 | 157 | 22 | - |
| Qwen3-30B-A3B | 2048/128 | vLLM | W4A16 | C=1 | 55 | - | - |
| Qwen3-30B-A3B | 2048/128 | vLLM | W4A16 | C=8 | 174 | - | - |
| Qwen3-32B | 2048/128 | vLLM | W4A16 | C=1 | 7 | - | - |
| Qwen3-32B | 2048/128 | vLLM | W4A16 | C=8 | 17 | - | - |
| Qwen3.5-35B-A3B | 2048/128 | vLLM | W4A16 | C=1 | 30 | - | - |
| Qwen3.5-35B-A3B | 2048/128 | vLLM | W4A16 | C=8 | 80 | - | - |
| Qwen3.5-27B | 2048/128 | vLLM | W4A16 | C=1 | 9 | - | - |
| Qwen3.5-27B | 2048/128 | vLLM | W4A16 | C=8 | 41 | - | - |
| Qwen3.6-35B-A3B | 2048/128 | vLLM | W4A16 | C=1 | 29 | - | - |
| Qwen3.6-35B-A3B | 2048/128 | vLLM | W4A16 | C=8 | 83 | - | - |
| Qwen3.6-27B | 2048/128 | vLLM | W4A16 | C=1 | 7 | - | - |
| Qwen3.6-27B | 2048/128 | vLLM | W4A16 | C=8 | 21 | - | - |
| Qwen3-VL-2B | 2048/128 | vLLM | W4A16 | C=1 | 60 | 21 | - |
| Qwen3-VL-2B | 2048/128 | vLLM | W4A16 | C=8 | 91 | 28 | - |
| Qwen3-VL-4B | 2048/128 | vLLM | W4A16 | C=1 | 47 | 16 | - |
| Qwen3-VL-4B | 2048/128 | vLLM | W4A16 | C=8 | 214 | 35 | - |
| Qwen3-VL-8B | 2048/128 | vLLM | W4A16 | C=1 | 28 | 9 | - |
| Qwen3-VL-8B | 2048/128 | vLLM | W4A16 | C=8 | 149 | 20 | - |
| Gemma 4 E2B | 2048/128 | llama.cpp | Q8_0 | C=1 | 35 | - | - |
| Gemma 4 E2B | 2048/128 | vLLM | BF16 | C=1 | 32 | - | - |
| Gemma 4 E2B | 2048/128 | vLLM | BF16 | C=8 | 191 | - | - |
| Gemma 4 12B | 2048/128 | llama.cpp | Q4_0 QAT GGUF | C=1 | 11 | - | - |
| Gemma 4 12B | 2048/128 | llama.cpp | Q4_0 QAT GGUF | C=8 | 19 | - | - |
| Gemma 4 26B-A4B | 2048/128 | vLLM | AWQ | C=1 | 32 | - | - |
| Gemma 4 26B-A4B | 2048/128 | vLLM | AWQ | C=8 | 110 | - | - |
| Gemma 4 31B | 2048/128 | vLLM | AWQ | C=1 | 5 | - | - |
| Gemma 4 31B | 2048/128 | vLLM | AWQ | C=8 | 15 | - | - |
| GPT-OSS-20B | 2048/128 | vLLM | W4A16 | C=1 | 39 | - | - |
| GPT-OSS-20B | 2048/128 | vLLM | W4A16 | C=8 | 147 | - | - |
| Cosmos3 Edge (Reasoner) | 1705/128 | vLLM | BF16 | C=1 | 44 | - | - |
| Cosmos3 Edge (Reasoner) | 1705/128 | vLLM | BF16 | C=8 | 171 | - | - |
| Gemma 4 E4B | 2048/128 | vLLM | W4A16 | C=1 | 32 | - | - |
| Gemma 4 E4B | 2048/128 | vLLM | W4A16 | C=8 | 147 | - | - |
| Qwen3.5-4B | 2048/128 | vLLM | W4A16 | C=1 | 28 | - | - |
| Qwen3.5-4B | 2048/128 | vLLM | W4A16 | C=8 | 122 | - | - |
| Qwen3.5-9B | 2048/128 | vLLM | W4A16 | C=1 | 17 | - | - |
| Qwen3.5-9B | 2048/128 | vLLM | W4A16 | C=8 | 73 | - | - |

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- Orin Nano 8GB 칸은 llama.cpp Q4_K_M Nemotron3 Nano 4B 한 행(18)뿐이고 나머지 모델은 "-" (미측정 또는 미지원, 사유 미확인).^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]
- 같은 Qwen3-VL-2B vLLM W4A16 C=1: AGX Orin 60, Orin NX 21. 8B 급은 AGX 28, NX 9.^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]
- Cosmos Reasoning 2 2B C=8: AGX 273, NX 65 (동시성 8에서 AGX 이점 확대).^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]

## 한계·미확인
- 이 표는 언어/비전-언어 모델 생성 처리량이며 YOLO류 검출 지연·FPS 와 다름. 해상도(이미지 입력 크기)·배치·전력 모드 미표기. 단위 미확인. 신뢰도: 제조사 공식 페이지 내장 데이터라 높음, 단 조건 기재가 적어 설계 근거로는 상대 비교용.^[inbox/processed/hw-20261022-data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
