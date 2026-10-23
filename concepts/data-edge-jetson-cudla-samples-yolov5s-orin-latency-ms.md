---
title: "NVIDIA-AI-IOT cuDLA-samples: YOLOv5s INT8 Orin(DLA vs GPU) 배치별 지연(ms)"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge-inference, jetson-orin, tensorrt, dla, int8, yolov5, latency-ms]
sources: [inbox/processed/hw-20261023-data-edge-jetson-cudla-samples-yolov5s-orin-latency-ms.md]
confidence: medium
contested: false
contradictions: []
---

# NVIDIA-AI-IOT cuDLA-samples: YOLOv5s INT8 Orin(DLA vs GPU) 배치별 지연(ms)

- 원문: https://github.com/NVIDIA-AI-IOT/cuDLA-samples (README.md, 마지막 커밋 2024-02-18)^[inbox/processed/hw-20261023-data-edge-jetson-cudla-samples-yolov5s-orin-latency-ms.md]

## 핵심 내용
출처 유형: NVIDIA-AI-IOT 공식 저장소 README. 신뢰도: 높음(제조사), 단 모듈 명칭이 "Orin-X" 로만 표기되어 Jetson Orin Nano/NX/AGX 중 어느 것인지 미확인(DRIVE/AGX 계열 추정은 하지 않음).^[inbox/processed/hw-20261023-data-edge-jetson-cudla-samples-yolov5s-orin-latency-ms.md]
조건(원문): 플랫폼 Orin-X, GPU 1275 MHz, 메모리 3200 MHz, DLA 1331 MHz, TensorRT 8.6, DLA 3.14. YOLOv5s, 입력 1x3x672x672(mAP 측정 조건), INT8 QAT, trtexec 중앙값 GPU 컴퓨트 시간(파이프라인 실측보다 약간 빠르다고 원문 명시).^[inbox/processed/hw-20261023-data-edge-jetson-cudla-samples-yolov5s-orin-latency-ms.md]
| 배치 | DLA INT8 (ms) | GPU INT8 (ms) |
|---|---|---|
| 1 | 3.82 | 1.82 |
| 2 | 7.68 | 2.91 |
| 4 | 15.17 | 4.99 |
| 8 | 30.92 | 9.19 |
| 12 | 46.71 | 13.27 |
| 16 | 62.54 | 16.87 |
- 원문 주석: DLA 입력 `int8:hwc4`+출력 `fp16:chw16` 기준. `int8:hwc4 in + int8:chw32 out` 이면 DLA 배치1 약 2.4 ms 이나 정확도 소폭 하락. 마지막 4개 레이어를 FP16 으로 두면 mAP 37.1→37.3, 지연 4.0→4.46 ms(원문 표현, 위 표의 3.82 와 다른 빌드 기준일 수 있음 = 미확인).^[inbox/processed/hw-20261023-data-edge-jetson-cudla-samples-yolov5s-orin-latency-ms.md]
- mAP(COCO 2017): 공식 37.4, DLA FP16 37.5, DLA INT8 QAT 37.1, GPU INT8 QAT 36.8.^[inbox/processed/hw-20261023-data-edge-jetson-cudla-samples-yolov5s-orin-latency-ms.md]
## 한계·미확인
- 특정 Jetson 모듈(Nano/NX/AGX) 대응 미확인, 전처리·후처리 제외 여부는 "trtexec" 근거로 추론만 가능(원문 직접 언급 없음) → 미확인.^[inbox/processed/hw-20261023-data-edge-jetson-cudla-samples-yolov5s-orin-latency-ms.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
