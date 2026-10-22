---
title: "Jetson Orin 지연(ms) 표 신규 출처 정리 (2026-10-23) — 조건 그대로"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: edge-ai-compute
tags: [drone, edge-inference, jetson-orin, latency-ms, source-map]
sources: [inbox/processed/hw-20261023-conv-jetson-orin-latency-ms-sources-2026-10-23.md]
confidence: medium
contested: false
contradictions: []
---

# Jetson Orin 지연(ms) 표 신규 출처 정리 (2026-10-23) — 조건 그대로

- 원문: 본 폴더 ai/data/data-edge-jetson-nanosam-*, data-edge-jetson-cudla-samples-*, ai/research/ai-edge-jetson-*; 20261022/convergence/conv-jetson-orin-benchmark-source-map-2026-10^[inbox/processed/hw-20261023-conv-jetson-orin-latency-ms-sources-2026-10-23.md]

## 핵심 내용
| 출처 | 모듈 | 대상 | 정밀도 | 배치 | 해상도 | SW 버전 | 단위 |
|---|---|---|---|---|---|---|---|
| NVIDIA-AI-IOT NanoSAM README | Orin Nano, AGX Orin | SAM 변형 | 인코더 FP16/FP32, 디코더 FP32 | 미표기 | 미표기(빌드 예시 1024) | 미표기 | ms |
| NVIDIA-AI-IOT cuDLA-samples | "Orin-X" | YOLOv5s | INT8 QAT | 1~16 | 672x672 | TensorRT 8.6, DLA 3.14 | ms |
| Finke 2026 (arXiv 2603.01999) | Orin NX, AGX Orin (+Thor) | 깊이 모델 | BF16 | 4 | 480x300 | JetPack 6.1(Thor 7.0) | ms |
| LAF-YOLOv10 2026 (arXiv 2602.13378) | Orin Nano 8GB, AGX Orin 32GB | YOLO n급 5종 | FP16 | 1 | 미표기 | TensorRT 8.6 | ms |
Orin Nano/NX/AGX 세 모듈 전부에 대해 해상도·정밀도·배치·TensorRT·JetPack 이 모두 적힌 단일 ms 표는 이번에도 확인 못 함. 각 파일 값은 같은 모델·조건끼리만 비교.^[inbox/processed/hw-20261023-conv-jetson-orin-latency-ms-sources-2026-10-23.md]
## 한계·미확인
- 시도한 수단: NVIDIA 공식 저장소 README(GitHub raw), arXiv 전문, Bright Data 검색. 미시도/실패: NVIDIA TAO 문서의 모델 성능 표(이번에 열람 못 함), Ultralytics Jetson 가이드(검색 결과 비어 있음, 20261021 YOLO26 파일 참조), arXiv API(레이트 제한).^[inbox/processed/hw-20261023-conv-jetson-orin-latency-ms-sources-2026-10-23.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[mbse-uav-sysml]]
