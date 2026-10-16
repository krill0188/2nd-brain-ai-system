---
title: "드론 인식·엣지 AI SW 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: software-ecosystem
tags: [drone, drone-sw]
sources: [inbox/processed/hw-registry-20261017-software-perception-ai.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 인식·엣지 AI SW 레지스트리

드론과 융합해 쓰는 SW의 인식·엣지 AI 분야 제품·오픈소스 24건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[drone-software-ecosystem-registry]].

> 확인 방법: GitHub 저장소 페이지 접속(HTTP 200)과 표시된 라이선스, 저장소 설명문, 상용 제품은 공식 사이트 응답 기준. 표의 "드론 연동 포인트"는 저장소·공식 문서에 적힌 문구만 옮김. 최신 버전·스타 수·가격은 의도적으로 생략.

| 이름 | 유형(오픈소스/상용) | 라이선스(공식 페이지·저장소에 적힌 것만) | 개발 주체 | 공식 URL/저장소 | 드론 연동 포인트(지원 FC/프로토콜/ROS 버전 등, 공식 문서에 적힌 것만) | 비고 |
|---|---|---|---|---|---|---|
| Ultralytics YOLO | 오픈소스 | AGPL-3.0 | Ultralytics | https://github.com/ultralytics/ultralytics | 저장소 설명: 객체탐지·분할·분류·포즈·추적 지원 | AGPL이므로 상용 배포 시 조건 검토 필요(라이선스 원문 확인) ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| YOLOv7 | 오픈소스 | GPL-3.0 | WongKinYiu | https://github.com/WongKinYiu/yolov7 | 논문 구현체(저장소 설명) | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| YOLOv9 | 오픈소스 | GPL-3.0 | WongKinYiu | https://github.com/WongKinYiu/yolov9 | 논문 구현체(저장소 설명) | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| YOLOv6 | 오픈소스 | GPL-3.0 | Meituan | https://github.com/meituan/YOLOv6 | 저장소 설명: 산업용 단일단계 객체탐지 프레임워크 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| YOLOv10 | 오픈소스 | AGPL-3.0 | THU-MIG(칭화대) | https://github.com/THU-MIG/yolov10 | 저장소 설명: 실시간 End-to-End 객체탐지 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| YOLOX | 오픈소스 | Apache-2.0 | Megvii | https://github.com/Megvii-BaseDetection/YOLOX | 저장소 설명: MegEngine, ONNX, TensorRT, ncnn, OpenVINO 지원 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| MMDetection | 오픈소스 | Apache-2.0 | OpenMMLab | https://github.com/open-mmlab/mmdetection | 저장소 설명: OpenMMLab 객체탐지 툴박스·벤치마크 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| MMYOLO | 오픈소스 | GPL-3.0 | OpenMMLab | https://github.com/open-mmlab/mmyolo | 저장소 설명: YOLO 계열 툴박스(RTMDet, YOLOv5/6/7/8, YOLOX 등) | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| ByteTrack | 오픈소스 | MIT | FoundationVision (저장소 이전 표시) | https://github.com/ifzhang/ByteTrack | 저장소 설명: 모든 탐지박스를 연결하는 다중객체추적(ECCV 2022) | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| BoT-SORT | 오픈소스 | MIT | NirAharon | https://github.com/NirAharon/BoT-SORT | 저장소 설명: 강건한 다중객체추적 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| BoxMOT | 오픈소스 | AGPL-3.0 | Mikel Broström | https://github.com/mikel-brostrom/boxmot | 저장소 설명: 교체 가능한 SOTA 다중객체추적 모듈(Python/C++) | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| Supervision | 오픈소스 | MIT | Roboflow | https://github.com/roboflow/supervision | 저장소 설명: 재사용 가능한 컴퓨터 비전 도구 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| NVIDIA TensorRT | 오픈소스 | 오픈소스 구성요소 Apache-2.0 (SDK 전체 약관 미확인) | NVIDIA | https://github.com/NVIDIA/TensorRT | 저장소 설명: NVIDIA GPU용 고성능 추론 SDK의 오픈소스 부분 | SDK 페이지 https://developer.nvidia.com/tensorrt ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| NVIDIA DeepStream SDK | 상용 | NVIDIA 약관(미확인). 파이썬 앱 저장소는 NVIDIA 라이선스 헤더 | NVIDIA | https://developer.nvidia.com/deepstream-sdk | 페이지 설명: AI 기반 멀티센서·비디오·오디오·이미지 이해를 위한 스트리밍 분석 툴킷 | 개발 가이드 https://docs.nvidia.com/metropolis/deepstream/dev-guide , 파이썬 앱 https://github.com/NVIDIA-AI-IOT/deepstream_python_apps ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| torch2trt | 오픈소스 | MIT | NVIDIA-AI-IOT | https://github.com/NVIDIA-AI-IOT/torch2trt | 저장소 설명: PyTorch→TensorRT 변환기 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| ONNX Runtime | 오픈소스 | MIT | Microsoft | https://github.com/microsoft/onnxruntime | 저장소 설명: 크로스플랫폼 고성능 ML 추론·학습 가속기 | https://onnxruntime.ai ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| OpenVINO | 오픈소스 | Apache-2.0 | Intel (openvinotoolkit) | https://github.com/openvinotoolkit/openvino | 저장소 설명: AI 추론 최적화·배포 툴킷 | https://docs.openvino.ai ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| DL Streamer | 오픈소스 | MIT | Intel (open-edge-platform) | https://github.com/open-edge-platform/dlstreamer | 저장소 설명: GStreamer 기반 미디어 분석 파이프라인 프레임워크(클라우드/엣지) | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| LiteRT (TensorFlow Lite 후속) | 오픈소스 | Apache-2.0 | Google AI Edge | https://github.com/google-ai-edge/LiteRT | 저장소 설명: 엣지 플랫폼용 온디바이스 ML·GenAI 배포 프레임워크 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| ncnn | 오픈소스 | 미확인 | Tencent | https://github.com/Tencent/ncnn | 저장소 설명: 모바일 최적화 고성능 신경망 추론 프레임워크 | LICENSE.txt는 Tencent 문구, 종류 미확정 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| Apache TVM | 오픈소스 | Apache-2.0 | Apache Software Foundation | https://github.com/apache/tvm | 저장소 설명: 오픈소스 ML 컴파일러 프레임워크 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| ExecuTorch | 오픈소스 | BSD 계열(LICENSE 첫 줄 'BSD License') | Meta / PyTorch | https://github.com/pytorch/executorch | 저장소 설명: 모바일·임베디드·엣지용 온디바이스 AI | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| OpenCV | 오픈소스 | Apache-2.0 | OpenCV | https://github.com/opencv/opencv | 저장소 설명: 오픈소스 컴퓨터 비전 라이브러리 | 미확인 ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |
| Isaac ROS Object Detection | 오픈소스 | Apache-2.0 | NVIDIA | https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_object_detection | 저장소 설명: NVIDIA 가속 딥러닝 이미지 객체탐지 ROS 지원 | 문서 https://nvidia-isaac-ros.github.io ^[inbox/processed/hw-registry-20261017-software-perception-ai.md] |

## 한계
- 라이선스와 '드론 연동 포인트'는 저장소·공식 페이지에 적힌 문구만 옮긴 값이며, 표본 대조 전이다. 버전·인기도·가격은 의도적으로 생략했다.
- ROS 공식 사이트 등 봇 차단 사이트는 GitHub 기준으로만 기재했다. 유지보수 상태가 확인되지 않은 항목은 비고에 표시했다.
- 공격 성격의 도구(보안 카테고리)는 방어·승인된 시험 목적의 참고 목록이다.

## 관련 문서
- [[computer-vision-drone]]
- [[drone-hw-vendor-registry]]
