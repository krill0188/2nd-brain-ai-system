---
title: "Ultralytics YOLO26 on Jetson Orin: per-variant (n/s/m/l/x) inference time, from docs source"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: PerceptionModel
tags: [drone, edge-inference, jetson-orin, yolo26, tensorrt, benchmark, int8, fp16]
sources: [inbox/processed/hw-20261021-model-yolo26-ultralytics-jetson-orin-per-variant.md]
confidence: medium
contested: false
contradictions: []
---

# Ultralytics YOLO26 on Jetson Orin: per-variant (n/s/m/l/x) inference time, from docs source

- 원문: https://github.com/ultralytics/ultralytics/blob/main/docs/en/guides/nvidia-jetson.md (rendered: https://docs.ultralytics.com/guides/nvidia-jetson/)^[inbox/processed/hw-20261021-model-yolo26-ultralytics-jetson-orin-per-variant.md]
- 제작: Ultralytics / NVIDIA^[inbox/processed/hw-20261021-model-yolo26-ultralytics-jetson-orin-per-variant.md]

## 핵심 사양 (공식 문서 소스 표 그대로)
기존 model-yolo-ultralytics-jetson-orin-benchmarks.md 가 "모델 변형 미명시"였던 공백을 GitHub docs 소스(.md)로 채움. 조건: 입력 640, 지표는 "Inference time does not include pre/post-processing", 값은 ms/im(이미지당). PyTorch와 TensorRT FP32/FP16/INT8 행이 문서에 별도로 있음. 괄호는 mAP50-95(B). 문서가 명시한 테스트 환경: AGX Orin 64GB는 JetPack 7.2, Orin Nano Super는 JP6.1, Orin NX 16GB(reComputer J4012)는 JP6.0 또는 JP5.1.3 (표가 어느 JetPack으로 측정됐는지는 미확인).^[inbox/processed/hw-20261021-model-yolo26-ultralytics-jetson-orin-per-variant.md]

| 장치 | 모델 | PyTorch ms | TensorRT FP32 ms | TensorRT FP16 ms (mAP) | TensorRT INT8 ms (mAP) |
|---|---|---|---|---|---|
| AGX Orin 64GB | YOLO26n | 11.58 | 4.18 | 2.62 (0.4789) | 2.30 (0.4640) |
| AGX Orin 64GB | YOLO26s | 13.18 | 6.82 | 3.76 (0.5660) | 2.98 (0.5480) |
| AGX Orin 64GB | YOLO26m | 19.36 | 12.60 | 6.24 (0.6220) | 4.72 (0.5820) |
| AGX Orin 64GB | YOLO26l | 23.53 | 15.90 | 7.93 (0.6240) | 5.97 (0.5920) |
| AGX Orin 64GB | YOLO26x | 38.37 | 28.43 | 13.50 (0.6570) | 9.33 (0.6080) |
| Orin NX 16GB | YOLO26n | 13.90 | 7.01 | 4.13 (0.4789) | 3.49 (0.4489) |
| Orin NX 16GB | YOLO26s | 20.40 | 12.62 | 6.41 (0.5652) | 4.78 (0.5468) |
| Orin NX 16GB | YOLO26m | 38.60 | 24.69 | 11.66 (0.6225) | 8.22 (0.5817) |
| Orin NX 16GB | YOLO26l | 48.60 | 31.64 | 14.77 (0.6225) | 10.49 (0.5923) |
| Orin NX 16GB | YOLO26x | 84.40 | 57.18 | 26.76 (0.6632) | 17.32 (0.6170) |
| Orin Nano Super | YOLO26n | 15.60 | 7.53 | 4.57 (0.4800) | 3.80 (0.4490) |
| Orin Nano Super | YOLO26s | 22.83 | 13.60 | 7.17 (0.5649) | 5.25 (0.5468) |
| Orin Nano Super | YOLO26m | 44.43 | 28.19 | 13.59 (0.6225) | 9.30 (0.5817) |
| Orin Nano Super | YOLO26l | 60.97 | 35.88 | 17.42 (0.6225) | 11.83 (0.5923) |
| Orin Nano Super | YOLO26x | 98.44 | 67.17 | 32.60 (0.6637) | 19.99 (0.6170) |

참고(같은 문서): AGX Thor 개발자 키트 YOLO26n TensorRT FP16 1.39 ms, YOLO26x FP16 5.16 ms.^[inbox/processed/hw-20261021-model-yolo26-ultralytics-jetson-orin-per-variant.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 같은 장치에서 변형이 커질수록 지연이 크게 늘어남: Orin Nano Super TensorRT FP16 기준 YOLO26n 4.57 ms vs YOLO26x 32.60 ms.^[inbox/processed/hw-20261021-model-yolo26-ultralytics-jetson-orin-per-variant.md]
- INT8은 FP16보다 빠르지만 mAP50-95가 낮아짐(예: Orin Nano Super YOLO26n 0.4800 -> 0.4490).^[inbox/processed/hw-20261021-model-yolo26-ultralytics-jetson-orin-per-variant.md]
- 이 값은 추론만의 시간이므로 카메라 취득, 전처리, 후처리, FC로의 전송 지연은 별도 합산 필요.^[inbox/processed/hw-20261021-model-yolo26-ultralytics-jetson-orin-per-variant.md]

## 한계·미확인
- 표는 Ultralytics 팀 측정값으로 전력 모드(nvpmodel), 배치, 열 조건 미확인. 기존 YOLO11 수치와 달리 YOLO26 기준. FPS 수치는 문서가 표기하지 않음(1000/ms 계산은 규칙상 하지 않음).^[inbox/processed/hw-20261021-model-yolo26-ultralytics-jetson-orin-per-variant.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
