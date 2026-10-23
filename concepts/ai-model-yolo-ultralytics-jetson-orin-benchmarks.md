---
title: "Ultralytics YOLO on NVIDIA Jetson: Orin benchmarks (YOLO26 page) and DeepStream guide (YOLO11)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge-inference, jetson-orin, yolo, tensorrt, benchmark]
sources: [inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]
confidence: medium
contested: false
contradictions: []
---

# Ultralytics YOLO on NVIDIA Jetson: Orin benchmarks (YOLO26 page) and DeepStream guide (YOLO11)

- 원문: https://docs.ultralytics.com/guides/nvidia-jetson/ ; https://docs.ultralytics.com/guides/deepstream-nvidia-jetson/^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]
- 제작: Ultralytics / NVIDIA^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]

## 핵심 사양 (공식 문서 표 그대로, 입력 640)
기존 model-yolo11.md 와 대응. 주의: 현재 Jetson 가이드 페이지는 YOLO11이 아닌 YOLO26 기준으로 갱신되어 있고, 추출 텍스트에는 한 모델 변형(파일 크기 5.3 MB로 볼 때 n으로 보이나 페이지가 명시하지 않음)의 값만 보였다.^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]

### nvidia-jetson 가이드 (YOLO26 계열, 변형 미명시), 추론 ms/im
| 장치 (Ultralytics 버전) | 형식 | 크기 MB | mAP50-95(B) | ms/im |
|---|---|---|---|---|
| AGX Orin 64GB (8.4.32) | PyTorch | 5.3 | 0.4790 | 11.58 |
| | TensorRT FP32 | 11.5 | 0.4770 | 4.18 |
| | TensorRT FP16 | 7.9 | 0.4789 | 2.62 |
| | TensorRT INT8 | 5.4 | 0.4640 | 2.30 |
| Orin Nano Super (8.4.33) | PyTorch | 5.3 | 0.4790 | 15.60 |
| | TensorRT FP32 | 11.3 | 0.4770 | 7.53 |
| | TensorRT FP16 | 8.1 | 0.4800 | 4.57 |
| | TensorRT INT8 | 5.3 | 0.4490 | 3.80 |
| Orin NX 16GB (8.4.33) | PyTorch | 5.3 | 0.4799 | 13.90 |
| | TensorRT FP32 | 11.4 | 0.4770 | 7.01 |
| | TensorRT FP16 | 8.0 | 0.4789 | 4.13 |
| | TensorRT INT8 | 5.5 | 0.4489 | 3.49 |
(참고: AGX Thor는 PyTorch 7.39, TensorRT FP16 1.39 ms/im.)^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]

### deepstream-nvidia-jetson 가이드 (YOLO11, Orin NX 16GB, 640x640)
| 모델 | 정밀도 | ms/im | FPS |
|---|---|---|---|
| 미명시(YOLO11n 추정이나 페이지 미명시) | TensorRT FP32 / FP16 / INT8 | 8.64 / 5.27 / 4.54 | 미표기 |
| YOLO11s (FAQ) | TensorRT FP32 | 14.53 | 68.8 |
| YOLO11s | TensorRT FP16 | 7.91 | 126 |
| YOLO11s | TensorRT INT8 | 6.05 | 165 |

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 페이지 문구: 측정은 "at FP32 precision with default input image size of 640", "Inference time does not include pre/post-processing."^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]
- 같은 Orin NX에서 TensorRT FP16(4.13 ms/im)은 PyTorch(13.90)의 약 1/3 수준 값이 표에 나타난다(비교는 표 값 그대로).^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]
- INT8은 mAP50-95가 FP16보다 낮게 표기됨(Orin Nano Super: 0.4800 대 0.4490).^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]
- 페이지 권고: 최대 전력모드 `nvpmodel -m 0` 및 Jetson Clocks 사용.^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]

## 한계·미확인
- 모델 변형(n/s/m/l/x)별 값은 미확인(추출본에는 한 세트만). 배치 크기, JetPack 버전, 전력모드는 벤치마크 행에 대해 미확인. 비교 차트는 이미지라 미열람.^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]
- 표 정밀도 표기(FP32 기준)와 FP16/INT8 행 간 설정 관계가 페이지에서 불명확.^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]
- YOLO11 대응 값은 DeepStream 가이드의 Orin NX 한 장치뿐.^[inbox/processed/hw-20261021-model-yolo-ultralytics-jetson-orin-benchmarks.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]
