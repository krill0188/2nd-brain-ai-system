---
title: "Learning Vision-Based Omnidirectional Navigation: A Teacher-Student Approach Using Monocular Depth Estimation (Jetson Orin NX / AGX Orin / Thor 지연 표)"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: edge-ai-compute
tags: [drone, edge-inference, jetson-orin, tensorrt, latency-ms, depth-anything, navigation]
sources: [inbox/processed/hw-20261023-ai-edge-jetson-orin-nx-agx-depth-anything-latency-finke-2026.md]
confidence: medium
contested: false
contradictions: []
---

# Learning Vision-Based Omnidirectional Navigation: A Teacher-Student Approach Using Monocular Depth Estimation (Jetson Orin NX / AGX Orin / Thor 지연 표)

- 원문: https://arxiv.org/abs/2603.01999 (PDF https://arxiv.org/pdf/2603.01999)^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nx-agx-depth-anything-latency-finke-2026.md]
- 저자: Jan Finke, Wayne Paul Martis, Adrian Schmelter, Lars Erbach, Christian Jestel, Marvin Wiedemann^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nx-agx-depth-anything-latency-finke-2026.md]
- 발행: 2026-03-02 (arXiv)^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nx-agx-depth-anything-latency-finke-2026.md]

## 핵심 내용
열람: arXiv PDF 전문을 Ghostscript 로 텍스트 추출 후 Table I 대조. 신뢰도: 중상(프리프린트, 동일 표 1개).^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nx-agx-depth-anything-latency-finke-2026.md]
Table I 원문: 파인튜닝된 Depth Anything V2 기반 단안 깊이 모델, TensorRT(BF16) 내보내기, 배치 추론: 카메라 이미지 4장, 480x300 픽셀.^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nx-agx-depth-anything-latency-finke-2026.md]
| 플랫폼 | JetPack | 지연 [ms] | 평균 FPS |
|---|---|---|---|
| Jetson Orin NX | 6.1 | 98.63 ± 2.06 | 10.1 |
| Jetson Orin AGX | 6.1 | 50.16 ± 8.22 | 19.9 |
| Jetson Thor | 7.0 | 19.02 ± 4.81 | 52.6 |
본문: AGX Orin 에서 배치를 50.16 ± 8.22 ms 에 처리, 10 Hz 제어 주기에 충분하다고 서술.^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nx-agx-depth-anything-latency-finke-2026.md]
## 설계에 쓸 수 있는 지침
- 지연이 "4장 배치" 값이므로 이미지 1장당 지연이 아님. 단일 이미지 환산은 원문에 없음(계산 금지).^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nx-agx-depth-anything-latency-finke-2026.md]
## 한계·미확인
- Orin Nano 값 없음, TensorRT 버전·전력모드·모델 파라미터 수 미확인(논문 본문 범위에서 확인 못 함).^[inbox/processed/hw-20261023-ai-edge-jetson-orin-nx-agx-depth-anything-latency-finke-2026.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[mbse-uav-sysml]]
