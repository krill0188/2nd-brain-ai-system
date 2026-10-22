---
title: "Jetson Orin Nano/NX/AGX 모델 지연·FPS 표 출처 지도 (조건·단위 차이 정리)"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: edge-ai-compute
tags: [drone, edge-inference, jetson-orin, benchmark, tensorrt, source-map]
sources: [inbox/processed/hw-20261022-conv-jetson-orin-benchmark-source-map-2026-10.md]
confidence: medium
contested: false
contradictions: []
---

# Jetson Orin Nano/NX/AGX 모델 지연·FPS 표 출처 지도 (조건·단위 차이 정리)

- 원문: 본 폴더 ai/data/data-edge-jetson-*; 20261021 data-edge-deepstream-9-2-jetson-orin-model-fps, model-yolo26-ultralytics-jetson-orin-per-variant, model-jetson-ai-lab-orin-nano-super^[inbox/processed/hw-20261022-conv-jetson-orin-benchmark-source-map-2026-10.md]

## 핵심 내용
| 출처 | 모듈 | 측정 대상 | 조건 명시 | 단위 | 파일 |
|---|---|---|---|---|---|
| NVIDIA jetson-benchmarks (Wayback 2023-12/2024-06) | Orin Nano 4/8, NX 8/16, AGX 32/64 | CNN·검출(Yolov5s/m 등)·TAO 모델 11+6종 | JetPack 5.1.1, 전력모드(MAXN/15W/10W) | 미표기(스크립트는 FPS) | data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps |
| NVIDIA jetson-benchmarks 라이브 | AGX Orin, Orin NX 16GB, AGX Thor | MLPerf 지연·처리량, Thor LLM | JetPack/TensorRT/CUDA 버전 명시 | ms, samples/s, tokens/sec | data-edge-nvidia-jetson-benchmarks-live-page-mlperf-thor-2026-10 |
| Jetson AI Lab Models (2026-10) | AGX Orin 64, NX 16, Nano 8 | LLM/VLM 생성 처리량 | ISL/OSL 2048/128, 정밀도·엔진 | 미표기 | data-edge-jetson-ai-lab-models-orin-llm-vlm-throughput |
| jetson_benchmarks GitHub | Orin Nano 등 | 설정 CSV(배치) | JetPack 4.4+, TensorRT 7+ | FPS | data-edge-jetson-benchmarks-github-csv-config |
| DeepStream 9.2 (20261021) | AGX Orin, Thor | 종단 파이프라인 FPS | FP16 | FPS | data-edge-deepstream-9-2-jetson-orin-model-fps |
| Ultralytics YOLO26 (20261021) | AGX/NX/Nano Super | TensorRT FP16 640 지연 ms | 전후처리 제외 | ms | model-yolo26-ultralytics-jetson-orin-per-variant |
## 설계에 쓸 수 있는 지침
- 제어 루프 지연 예산은 단일 배치 지연(ms) 출처(YOLO26 등)로, 모듈 간 상대 비교는 Wayback 표로. 같은 단위가 아니므로 표 간 값 혼합 금지.^[inbox/processed/hw-20261022-conv-jetson-orin-benchmark-source-map-2026-10.md]
## 한계·미확인
- 끝내 못 찾은 것: Orin Nano/NX/AGX 별 "해상도·배치·정밀도·TensorRT 버전이 모두 명시된 지연(ms) 표"(NVIDIA 공식 페이지에서는 JetPack 5.1.1 만 명시). Jetson AI Lab 아카이브 벤치 페이지의 AGX Orin/Thor 값은 이미지(차트)라 20261021 에서도 미확인, 이번에도 재시도하지 않음.^[inbox/processed/hw-20261022-conv-jetson-orin-benchmark-source-map-2026-10.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[mbse-uav-sysml]]
