---
title: "UAV 영상 기반 소나무재선충병 탐지 정확도 비교"
created: 2026-09-05
updated: 2026-09-05
type: concept
domain: ai-autonomy
tags: [drone, ai-autonomy, drone-ai]
sources: [raw/papers/drone-ai/comparison-of-uav-image-based-detection-accuracy-of-pine-wilt-disease-affected-t.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 영상 기반 소나무재선충병 탐지 정확도 비교

UAV RGB 정사영상과 YOLO26-Large 모델을 사용해 소나무재선충병(pine wilt disease, PWD) 의심목 탐지에서
입력 채널 구성과 어텐션 모듈 적용이 정확도에 미치는 영향을 평가한 연구다 ^[raw/papers/drone-ai/comparison-of-uav-image-based-detection-accuracy-of-pine-wilt-disease-affected-t.md].

## 데이터셋 구성

| 데이터셋 | 채널 구성 |
|---|---|
| A | RGB 3채널 |
| B | RGB + 표고·경사(5채널) |
| C | RGB + GLCM 텍스처(ASM/Entropy/Homogeneity, 6채널) |
| D | RGB + GLCM 텍스처 + 표고·경사(8채널) |

## 방법

- YOLO26-Large 기반 탐지 모델에 Squeeze-and-Excitation(SE) 블록 등 어텐션 모듈을 결합해
  채널 구성별 탐지 정확도를 비교.
- 지형·텍스처 부가 정보가 RGB 단독 대비 탐지 성능에 미치는 영향을 정량 분석하는 것이 목적.

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전 전반(YOLO, 객체 탐지)
- [[yolo]] — YOLO 아키텍처 개요
- [[drone-lidar-forest-boundary]] — 드론 라이다 기반 임야 경계 추출 연구
