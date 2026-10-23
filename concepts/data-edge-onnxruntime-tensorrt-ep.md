---
title: "NVIDIA TensorRT Execution Provider (ONNX Runtime docs)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge, onnx, tensorrt, deployment]
sources: [inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]
confidence: medium
contested: false
contradictions: []
---

# NVIDIA TensorRT Execution Provider (ONNX Runtime docs)

- 원문: https://onnxruntime.ai/docs/execution-providers/TensorRT-ExecutionProvider.html^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]
- 저자: ONNX Runtime contributors^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]

## 핵심 내용
ONNX Runtime의 TensorRT EP는 ONNX 모델을 NVIDIA GPU에서 TensorRT로 실행한다. 주요 옵션: trt_fp16_enable(FP16), trt_int8_enable(INT8, 비QDQ 모델은 보정 테이블 필요), trt_engine_cache_enable(엔진 캐시). 엔진은 모델, 정밀도, ORT/TensorRT 버전, GPU에 묶이므로 이 중 하나가 바뀌면 캐시를 지워야 한다. 지원되지 않는 노드는 CUDA EP로 폴백하도록 함께 쓴다.^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]
원문 인용: "delivers better inferencing performance on the same hardware"^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]

## 설계·운용에 쓸 수 있는 지침
- 세션 생성 시간(Stable Diffusion UNet): 캐시 없음 약 384 s, 타이밍 캐시 42 s, 엔진 캐시 9 s, 임베디드 엔진 1.9 s.^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]
- 타이밍 캐시 빌드 시간: efficientnet-lite4-11 34.6 s에서 7.7 s, yolov4 108.62 s에서 9.4 s.^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]
- ORT 1.22부터 CUDA 12 GPU 패키지만 배포. TensorRT 10.0~10.5는 NMS, NonZero, RoiAlign 등 데이터 의존 shape 연산에서 성능 문제가 있음.^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]
- 드론 탑재 기기에서는 부팅 후 첫 추론 지연을 줄이려면 엔진 캐시를 사전 생성해 배포.^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]

## 한계·미확인
- Jetson 전용 설정은 이 페이지에서 미확인.^[inbox/processed/hw-20261021-data-edge-onnxruntime-tensorrt-ep.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
