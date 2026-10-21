---
title: "NVIDIA Jetson Benchmarks (MLPerf Inference Edge on Jetson AGX Orin / Orin NX)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: edge-ai-compute
source: https://developer.nvidia.com/embedded/jetson-benchmarks
authors: NVIDIA
published: 미확인
tags: [drone, edge-inference, jetson-orin, mlperf, benchmark]
---
## 핵심 내용
NVIDIA 공식 Jetson 벤치마크 페이지는 현재 MLPerf Inference Edge 결과를 싣고 있고, PeopleNet/DetectNet/YOLO/SSD 등 모델별 FPS 표는 페이지에서 확인되지 않았다(이전 버전 페이지와 다름). 열 헤더가 값과 깔끔히 대응되지 않아 장치 매핑은 페이지 헤더 순서 기준 추정이므로 v3.1 표는 참고용.

MLPerf v3.1 (JetPack 5.1.1, TensorRT 8.5.2, CUDA 11.4), AGX Orin 열
| 모델 | Single-stream 지연 ms | Offline samples/s |
|---|---|---|
| ResNet | 0.64 | 6423.63 |
| Retinanet | 11.67 | 148.71 |
| BERT | 5.71 | 553.69 |
| RNN-T | 94.01 | 1169.98 |
| 3D-Unet-99.0 | 4371.46 | 0.51 |

Orin NX Offline (S/s): ResNet 2640.51, Retinanet 66.5, BERT 194.5. NX MaxQ Offline: ResNet 1681.87 (전력 14.95 W), Retinanet 47.59 (15.57 W).
MLPerf v4.0 (AGX Orin, TensorRT 9.0.1): GPT-J 6B single-stream 10204.46 ms, offline 0.15 S/s; stable-diffusion-xl 12941.92 ms, 0.08 S/s.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- AGX Orin ResNet 단일 스트림 지연 0.64 ms, Retinanet 11.67 ms (표 값).
- MaxQ 모드 값은 전력(W)과 함께 표기됨(예: Orin NX MaxQ ResNet 1681.87 S/s, 14.95 W).

## 한계·미확인
- 정밀도, 배치 크기는 페이지 미표기. 전력모드는 "MaxQ" 라벨 외 미표기. 드론 용도 모델(YOLO 등) 수치 없음. 발행일 미확인.
- 헤더-값 매핑이 불명확해 일부 열(Orin MaxQ Multi 등)은 수록하지 않음.
