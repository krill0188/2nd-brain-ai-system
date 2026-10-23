---
title: "NVIDIA DeepStream SDK 9.2 Performance: TAO pre-trained models end-to-end FPS on Jetson AGX Orin / AGX Thor"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: edge-ai-compute
ontology_class: EdgeAIPerformance
tags: [drone, edge-inference, jetson-orin, deepstream, tao, rt-detr, grounding-dino, fps]
sources: [inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]
confidence: medium
contested: false
contradictions: []
---

# NVIDIA DeepStream SDK 9.2 Performance: TAO pre-trained models end-to-end FPS on Jetson AGX Orin / AGX Thor

- 원문: https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Performance.html^[inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]
- 저자: NVIDIA^[inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]
- 발행: 미확인 (DeepStream 9.2 문서)^[inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]

## 핵심 내용
페이지 설명: "end-to-end performance of the entire video analytic application considering video capture and decode, pre-processing, batching, inference, and post-processing". 출력 렌더링(OSD/tiler)은 끈 상태이며 입력은 sample_1080p_h265.mp4. 전체 모델 FP16, 열 관리 양호 조건. 표 열 이름은 "GPU(FPS)"이며 스트림 수·배치·전력 모드는 추출 텍스트에 없음(미확인).^[inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]

| 모델 | 입력(C H W, 원문 표기 붙어 있음) | 트래커 | AGX Thor FPS | AGX Orin FPS |
|---|---|---|---|---|
| C-RADIO-B | 3x224x224 | 없음 | 1320 | 544 |
| C-RADIO-L | 3x224x224 | 없음 | 557 | 179 |
| NV-DinoV2-L | 3x224x224 | 없음 | 451 | 126 |
| RT-DETR | 3x640x640 | 없음 | 208 | 96 |
| RT-DETR | 3x640x640 | NvDCF | 189 | 96 |
| RT-DETR (warehouse) | 3x544x960 | MV3DT | 95 | 39 |
| PeopleNet 2.6.3 | 3x640x640 | MV3DT | 349 | 147 |
| PeopleNet Transformer | 3x544x960 | MV3DT | 25 | 16 |
| Grounding-DINO | 3x544x960 | 없음 | 24 | 13 |
| MaskGroundingDINOv2 | 3x544x960 | 없음 | 24 | 15 |
| TrafficCamnet Transformer Lite | 3x544x960 | NvDCF | 153 | 105 |
| SegFormer | 3x640x640 | 없음 | 256 | 145 |
| Mask2Former + SWIN | 3x800x800 | 없음 | 26 | 18 |

(입력 해상도 표기는 원문이 "3224224"처럼 공백 없이 나와 3/224/224로 읽은 것이며, 544x960 등은 같은 방식 해석 — 원문 표기 모호함.)^[inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 개방형 어휘 검출 Grounding-DINO는 AGX Orin에서 13 FPS로 실시간 제어 루프(수십 Hz)보다 한 자릿수 느림. 폐쇄형 RT-DETR는 같은 장치에서 96 FPS.^[inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]
- 트래커(NvDCF) 추가는 RT-DETR AGX Orin FPS를 96에서 96(변화 없음)으로, AGX Thor에서는 208에서 189로 낮춤.^[inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]
- 이 FPS는 여러 스트림의 합산 처리량일 수 있으므로 단일 프레임 지연으로 쓰면 안 됨(스트림 수 미확인).^[inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]

## 한계·미확인
- Orin NX/Nano 수치 없음(페이지는 AGX Orin과 Thor만). 지연(ms) 값 없음. 스트림 수·nvpmodel·JetPack 버전 미확인. Jetson AI Lab와 developer.nvidia.com/embedded/jetson-benchmarks는 단일/멀티 스트림 지연(ms) 열이 보이나 JS 렌더링 표라 값 추출 실패(미확인).^[inbox/processed/hw-20261021-data-edge-deepstream-9-2-jetson-orin-model-fps.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]

## 📰 최근 관련 소식
- [ModalAI] SDK 1.8.0 Built to be built on (youtube.com, 2026-10-21) — https://www.youtube.com/watch?v=B_PI7TkdSMA
