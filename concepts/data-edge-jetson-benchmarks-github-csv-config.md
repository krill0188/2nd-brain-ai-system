---
title: "NVIDIA-AI-IOT/jetson_benchmarks: 벤치 스크립트 조건(JetPack 4.4+, TensorRT 7+)과 Orin Nano 모델별 배치·해상도 설정 CSV"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge-inference, jetson, tensorrt, benchmark, batch-size, methodology]
sources: [inbox/processed/hw-20261022-data-edge-jetson-benchmarks-github-csv-config.md]
confidence: medium
contested: false
contradictions: []
---

# NVIDIA-AI-IOT/jetson_benchmarks: 벤치 스크립트 조건(JetPack 4.4+, TensorRT 7+)과 Orin Nano 모델별 배치·해상도 설정 CSV

- 원문: https://github.com/NVIDIA-AI-IOT/jetson_benchmarks (README.md, benchmark_csv/orin-nano-benchmarks.csv)^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-github-csv-config.md]
- 저자: NVIDIA-AI-IOT^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-github-csv-config.md]
- 발행: 미확인(저장소 최신 커밋일 미조회)^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-github-csv-config.md]

## 핵심 내용
README: 스크립트는 "GPU+2DLA" 대상 벤치마크를 실행하며 입력 해상도는 Inception V4 299x299, ResNet-50 224x224, OpenPose 256x456, VGG-19 224x224, YOLO-V3 608x608, Super Resolution 481x321, Unet 256x256. 버전 의존성: "JetPack 4.4+", "TensorRT 7+". 출력표 열은 "Model Name / FPS" (README 샘플은 Xavier NX 값: inception_v4 311.73, ResNet50_224x224 824.02, ssd-mobilenet-v1 887.6 등).^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-github-csv-config.md]
orin-nano-benchmarks.csv 의 조건(GPU 배치 크기, DLA 사용 0, WS 2048): inception_v4 32, vgg19_N2 64, super_resolution_bsd500 8, unet-segmentation 32 (입력 1x512x512 표기), pose_estimation 64, yolov3-tiny-416 32, ResNet50_224x224 32, mobilenet_v1_ssd 32, ssd_resnet34_1200x1200 1. 프레임워크는 caffe/onnx/tensorrt(uff) 혼재.^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-github-csv-config.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- NVIDIA 표의 처리량 값은 위 배치(대부분 32~64)로 측정된 스크립트 출력이므로 배치 1 지연과 직접 비교 금지. 단 ssd_resnet34_1200x1200 은 배치 1.^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-github-csv-config.md]

## 한계·미확인
- 이 CSV는 설정이지 결과가 아님. 결과 수치와의 대응(어느 CSV 버전이 어느 표를 만들었는지)은 NVIDIA 페이지에 명시되지 않아 미확인. nx/orin CSV 는 다운로드했으나 표로 옮기지 않음.^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-github-csv-config.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
