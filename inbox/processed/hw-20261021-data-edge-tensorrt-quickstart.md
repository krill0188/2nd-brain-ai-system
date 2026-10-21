---
title: "TensorRT Quick Start Guide (NVIDIA)"
created: 2026-10-21
captured: 2026-10-21
type: doc
domain: edge-ai-compute
source: https://docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/quick-start-guide.html
authors: "NVIDIA"
published: "미확인"
tags: [drone, edge, tensorrt, onnx, deployment]
---
## 핵심 내용
TensorRT는 학습된 모델을 GPU 전용 엔진(직렬화된 plan 파일)으로 변환해 추론한다. 빌더가 엔진을 컴파일하고 런타임이 실행한다. 가이드의 4단계: Export the model / Select a precision / Convert the model / Deploy the model. ONNX 변환은 API 또는 trtexec로 가능. 설치는 Container, Debian, pip, Tar, RPM, Zip 방식. 배포는 Torch-TensorRT, TensorRT 런타임 API, Triton Inference Server.
원문 인용: "pip provides Python bindings but does not include trtexec."

## 설계·운용에 쓸 수 있는 지침
- 엔진은 대상 GPU에 종속되므로 드론 탑재 보드(Jetson 등)에서 또는 동일 아키텍처에서 빌드해야 한다(이 문장은 ORT 문서의 엔진-GPU 종속 서술과 합쳐 해석; 본 페이지가 직접 명시하진 않음).

## 한계·미확인
- 지원 플랫폼과 Jetson 설정, 실제 trtexec 명령은 이 페이지에 없음: 미확인.
