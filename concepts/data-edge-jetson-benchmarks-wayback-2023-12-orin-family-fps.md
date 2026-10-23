---
title: "NVIDIA Jetson Benchmarks (Wayback 2023-12-20 / 2024-06-21 snapshot): Orin Nano 4/8GB, Orin NX 8/16GB, AGX Orin 32/64GB 모델별 처리량 표"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge-inference, jetson-orin, tensorrt, benchmark, orin-nano, orin-nx, agx-orin, yolov5, wayback]
sources: [inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]
confidence: medium
contested: false
contradictions: []
---

# NVIDIA Jetson Benchmarks (Wayback 2023-12-20 / 2024-06-21 snapshot): Orin Nano 4/8GB, Orin NX 8/16GB, AGX Orin 32/64GB 모델별 처리량 표

- 원문: https://web.archive.org/web/20231220004344id_/https://developer.nvidia.com/embedded/jetson-benchmarks (동일 값 확인: https://web.archive.org/web/20240621000123id_/https://developer.nvidia.com/embedded/jetson-benchmarks)^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]
- 저자: NVIDIA^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]
- 발행: 스냅샷 2023-12-20, 2024-06-21 (표 자체의 작성일 미표기)^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]

## 핵심 내용
현재 developer.nvidia.com/embedded/jetson-benchmarks 라이브 페이지에서는 아래 Orin Nano/NX/AGX 표가 사라지고(MLPerf·Thor LLM 표만 남음, 별도 파일 참조) Wayback 보관본에서만 확인됨. 열람 방법: web.archive.org 의 `id_` 원본 HTML을 받아 표를 텍스트로 변환. 두 스냅샷(2023-12, 2024-06)의 값은 동일.^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]

공통 조건(페이지 각주 그대로): "Jetson Orin & Jetson Xavier Benchmarks were run using Jetpack 5.1.1". 구동 모드: "maximum performance (MAXN for JAO64, JAO32, ONX16, ONX8; and 15W mode for JON8, and 10W mode for JON4)". 표 단위: 추출 텍스트에 단위(FPS 등) 표기 없음 = 미확인(이 벤치 스크립트 NVIDIA-AI-IOT/jetson_benchmarks 의 README 출력표는 열 이름이 "FPS"). 배치·정밀도는 페이지에 없음(스크립트 CSV는 모델별 GPU 배치 크기만 기재, data-edge-jetson-benchmarks-github-csv-config 참조). TensorRT 버전은 이 표에 미표기(JetPack 5.1.1 번들 값은 미확인).^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]

### Jetson Family Benchmarks (JetPack 5.1.1)
| 모델 | Orin Nano 4GB | Orin Nano 8GB | Orin NX 8GB | Orin NX 16GB | AGX Orin 32GB | AGX Orin 64GB |
|---|---|---|---|---|---|---|
| Inveption_V4 (원문 표기) | 182 | 361 | 593 | 769 | 1337.8 | 1702.6 |
| VGG19 | 174 | 361 | 442 | 532 | 937 | 1471 |
| Super_resolution | 102 | 203 | 280 | 386 | 610 | 882 |
| UNET-sgmentation (원문 표기) | 76 | 148 | 183 | 217 | 387 | 584 |
| Pose Estimation | 280 | 546 | 665 | 800 | 1424 | 2048 |
| Yolov3-tiny | 371 | 731 | 1156 | 1440 | 2611 | 3179 |
| Resnet50 | 621 | 1158 | 1725 | 2183 | 3717 | 4834 |
| SSD-Mobilnet (원문 표기) | 1094 | 2156 | 2893 | 3457 | 6415 | 7671 |
| SSD_Resnet34_1200x1200 | 18 | 34 | 52 | 72 | 120 | 163 |
| Yolov5m | 69 | 131 | 162 | 193 | 342 | 519 |
| Yolov5s | 158 | 301 | 379 | 449 | 785 | 1135 |

### Jetson Pretrained Model Benchmarks (NVIDIA TAO/NGC 사전학습 모델, Orin 결과)
| 모델 | Orin Nano 4GB | Orin Nano 8GB | Orin NX 8GB | Orin NX 16GB | AGX Orin 32GB | AGX Orin 64GB |
|---|---|---|---|---|---|---|
| PeopleNet (v2.5 unpruned) | 57 | 117 | 192 | 240 | 409 | 685 |
| Action Recognition 2D | 220 | 372 | 440 | 483 | 1158 | 1517 |
| Action Recognition 3D | 13 | 26 | 32 | 39 | 71 | 108 |
| LPR Net | 552 | 974 | 1314 | 1427 | 2800 | 4213 |
| Dashcam Net | 200 | 400 | 689 | 877 | 1482 | 2139 |
| Bodypose Net | 69 | 137 | 169 | 203 | 360 | 563 |

구세대(JetPack 4.6.1, MAXN) 같은 페이지 표: Jetson Nano / TX2 NX / Xavier NX / AGX Xavier = PeopleNet 2/5/120/195, Action Recog 2D 32/88/245/472, 3D 1/3/21/32, LPR Net 47/86/714/1236, Dashcam 11/26/424/667, Bodypose 3/7/104/172. (Xavier 계열 일부는 JetPack 5.1.1이라고도 적혀 있어 각주가 혼재 = 원문 그대로)^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 같은 모델 Yolov5s: Orin Nano 8GB 301, Orin NX 16GB 449, AGX Orin 64GB 1135. Orin Nano 4GB(10W 모드)는 8GB(15W 모드) 값의 약 절반 수준으로 기재(158 대 301) — 모드가 달라 모듈 용량 효과와 전력 제한 효과가 섞임.^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]
- 이 표는 단일 프레임 지연이 아니라 처리량 성격(배치 사용 스크립트)이므로 제어 루프 지연 예산에는 data-edge-jetson-ai-lab 및 YOLO 단일 지연 파일(model-yolo26-ultralytics-jetson-orin-per-variant)과 구분해 쓸 것.^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]

## 한계·미확인
- 단위·배치·정밀도·TensorRT 버전 표기 없음(미확인). 현재 NVIDIA 라이브 페이지에는 이 표가 없어 최신 JetPack 6 대응값은 확보 못 함. 신뢰도: 제조사 원문 보관본이라 높음, 단 단위 해석은 스크립트 README 근거의 간접 추정이므로 중.^[inbox/processed/hw-20261022-data-edge-jetson-benchmarks-wayback-2023-12-orin-family-fps.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
