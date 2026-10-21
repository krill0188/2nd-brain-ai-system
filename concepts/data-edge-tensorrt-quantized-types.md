---
title: "Working with Quantized Types (NVIDIA TensorRT documentation)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
tags: [drone, edge, tensorrt, quantization]
sources: [inbox/processed/hw-20261021-data-edge-tensorrt-quantized-types.md]
confidence: medium
contested: false
contradictions: []
---

# Working with Quantized Types (NVIDIA TensorRT documentation)

- 원문: https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/work-quantized-types.html^[inbox/processed/hw-20261021-data-edge-tensorrt-quantized-types.md]
- 저자: NVIDIA^[inbox/processed/hw-20261021-data-edge-tensorrt-quantized-types.md]
- 발행: 미확인^[inbox/processed/hw-20261021-data-edge-tensorrt-quantized-types.md]

## 핵심 내용
TensorRT는 INT8을 대칭 양자화(0 중심)로 지원하며 변환에 보통 스케일 계수만 필요하다. FP8(E4M3), FP4(E2M1)도 지원 부동소수 저정밀 형식이며 INT4는 가중치 전용이다. 명시적 양자화(Q/DQ 네트워크) 안내서가 별도로 있고 PTQ와 QAT 두 워크플로가 있다.^[inbox/processed/hw-20261021-data-edge-tensorrt-quantized-types.md]
원문 인용: "symmetric quantization scheme"^[inbox/processed/hw-20261021-data-edge-tensorrt-quantized-types.md]

## 설계·운용에 쓸 수 있는 지침
- Jetson 계열 배포 시 지원 정밀도는 GPU 세대에 따라 다르므로 대상 하드웨어 지원표를 별도 확인.^[inbox/processed/hw-20261021-data-edge-tensorrt-quantized-types.md]

## 한계·미확인
- 이 페이지에는 FP16, 보정(calibration) 절차, 정확도/속도 수치가 없음: 미확인.^[inbox/processed/hw-20261021-data-edge-tensorrt-quantized-types.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
