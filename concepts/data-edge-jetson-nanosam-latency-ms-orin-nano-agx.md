---
title: "NVIDIA-AI-IOT NanoSAM README 성능표: Jetson Orin Nano / AGX Orin 지연(ms)"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: edge-ai-compute
tags: [drone, edge-inference, jetson-orin, tensorrt, latency-ms, nanosam, sam]
sources: [inbox/processed/hw-20261023-data-edge-jetson-nanosam-latency-ms-orin-nano-agx.md]
confidence: medium
contested: false
contradictions: []
---

# NVIDIA-AI-IOT NanoSAM README 성능표: Jetson Orin Nano / AGX Orin 지연(ms)

- 원문: https://github.com/NVIDIA-AI-IOT/nanosam (README.md, raw.githubusercontent.com 으로 열람; 마지막 커밋 2023-09-20)^[inbox/processed/hw-20261023-data-edge-jetson-nanosam-latency-ms-orin-nano-agx.md]

## 핵심 내용
출처 유형: NVIDIA-AI-IOT 공식 GitHub 저장소 원문. 단위 ms 가 열 제목에 명시됨. 신뢰도: 높음(제조사 저장소), 단 TensorRT/JetPack 버전은 표에 없음.^[inbox/processed/hw-20261023-data-edge-jetson-nanosam-latency-ms-orin-nano-agx.md]
| 모델 | Orin Nano 이미지 인코더(ms) | Orin Nano 전체 파이프라인(ms) | AGX Orin 이미지 인코더(ms) | AGX Orin 전체(ms) |
|---|---|---|---|---|
| MobileSAM | TBD | 146 | 35 | 39 |
| NanoSAM (ResNet18) | TBD | 27 | 4.2 | 8.1 |
조건(README 각주 그대로): MobileSAM 인코더는 FP32(TensorRT FP16 에서 오류 결과), NanoSAM 인코더는 FP16, 두 파이프라인의 마스크 디코더는 FP32. 입력은 README 빌드 절차의 `image:...x3x1024x1024`(배치 학습용 예시, 지연 측정 조건 자체는 미표기). 정확도(mIoU)는 지연 측정과 동일 설정.^[inbox/processed/hw-20261023-data-edge-jetson-nanosam-latency-ms-orin-nano-agx.md]
## 설계에 쓸 수 있는 지침
- 프롬프트형 분할 모델의 Orin Nano 전체 파이프라인 27 ms(약 37 FPS) 대 AGX Orin 8.1 ms: 모듈 간 약 3.3배(표 값끼리 비율, 원문 계산 아님).^[inbox/processed/hw-20261023-data-edge-jetson-nanosam-latency-ms-orin-nano-agx.md]
## 한계·미확인
- 배치, 정확한 해상도 측정 조건, TensorRT·JetPack 버전, 전력모드: 미확인. Orin NX 값 없음. 객체 검출이 아닌 분할 모델임.^[inbox/processed/hw-20261023-data-edge-jetson-nanosam-latency-ms-orin-nano-agx.md]

상위 허브: [[ai-drone-data-processing-hub]] · 함께 보기: [[companion-computer]]
