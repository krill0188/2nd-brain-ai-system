---
title: "LAF-YOLOv10 ... Small Object Detection in Drone Aerial Imagery — Table 8 Jetson Orin Nano / AGX Orin 지연(ms)"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: edge-ai-compute
tags: [drone, edge-inference, jetson-orin, tensorrt, latency-ms, yolo, visdrone]
sources: [inbox/processed/hw-20261023-ai-edge-jetson-orin-nano-agx-yolo-latency-laf-yolov10-2026.md]
confidence: medium
contested: false
contradictions: []
---

# LAF-YOLOv10 ... Small Object Detection in Drone Aerial Imagery — Table 8 Jetson Orin Nano / AGX Orin 지연(ms)

- 원문: https://arxiv.org/abs/2602.13378 (HTML https://arxiv.org/html/2602.13378v1)^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nano-agx-yolo-latency-laf-yolov10-2026.md]
- 저자: Sohail Ali Farooqui, Zuhair Ahmed Khan Taha, Mohammed Mudassir Uddin, Shahnawaz Alam^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nano-agx-yolo-latency-laf-yolov10-2026.md]
- 발행: 2026-02 (arXiv v1, 정확한 일자 미확인)^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nano-agx-yolo-latency-laf-yolov10-2026.md]

## 핵심 내용
열람: arXiv HTML 전문 4.8절·Table 8 확인(PDF 는 텍스트 추출 불가여서 HTML 사용). 신뢰도: 중(단일 프리프린트, 자체 측정).^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nano-agx-yolo-latency-laf-yolov10-2026.md]
조건(원문): Jetson Orin Nano 8GB(40 TOPS INT8), Jetson AGX Orin 32GB(200 TOPS INT8), TensorRT 8.6, FP16, 배치 1, 1000회 순전파(워밍업 200회), 전력은 tegrastats.^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nano-agx-yolo-latency-laf-yolov10-2026.md]
| 방법 | Orin Nano 지연(ms) | FPS | 전력(W) | AGX Orin 지연(ms) | FPS | 전력(W) |
|---|---|---|---|---|---|---|
| YOLOv5n | 24.1 | 41.5 | 8.2 | 8.4 | 119.0 | 18.6 |
| YOLOv8n | 33.7 | 29.7 | 10.1 | 12.8 | 78.1 | 22.4 |
| YOLOv10n | 31.2 | 32.1 | 9.8 | 11.5 | 87.0 | 21.1 |
| YOLO11n | 26.8 | 37.3 | 8.9 | 9.2 | 108.7 | 19.3 |
| OSD | 29.4 | 34.0 | 9.5 | 10.8 | 92.6 | 20.5 |
| LAF-YOLOv10 | 41.2 | 24.3 | 11.4 | 15.3 | 65.4 | 24.8 |
## 한계·미확인
- 입력 해상도, JetPack 버전, 전력모드가 표·4.8절에 없음(미확인). 같은 논문의 RTX 4090 측정은 별개. 20261021 의 Ultralytics YOLO26 표(전후처리 제외 ms)와 방법이 달라 값 혼합 금지.^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nano-agx-yolo-latency-laf-yolov10-2026.md]
- 저자 표기 순서·일자는 arXiv HTML/PDF 메타 기준; 정확한 제출일은 미확인.^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nano-agx-yolo-latency-laf-yolov10-2026.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
