---
title: "드론 촬영경로별 3DGS 공간 구성요소 재현 품질 비교 (KCI)"
created: 2026-10-08
updated: 2026-10-08
type: concept
domain: ops-mission
tags: [drone, drone-ai, ops-mission, research]
sources: [inbox/processed/fetch-2026-10-08-kci-서로-다른-드론-촬영경로-기반-3dgs-모델의-공간-구성요소별-시각적-재현-품질-단일-대상지-탐색적-비교.md]
confidence: low
contested: false
contradictions: []
---

# 촬영경로별 3D Gaussian Splatting 재현 품질

황병연(한국폴리텍대)의 산업기술연구논문지(2026) 논문. 같은 대상지를 서로 다른 드론 촬영경로로 촬영해 3DGS 모델을 만들고 공간 구성요소별 재현 품질을 탐색적으로 비교했다.
단일 대상지·단일 기체·경로당 1회 학습이라는 탐색적 사례이므로 일반화하지 않는다(저자도 명시). 단일 출처라 confidence는 low다.^[inbox/processed/fetch-2026-10-08-kci-서로-다른-드론-촬영경로-기반-3dgs-모델의-공간-구성요소별-시각적-재현-품질-단일-대상지-탐색적-비교.md]

## 설계

- 경로: A = 0° 평행 왕복형, B = 45° 대각 왕복형, C = 객체 중심 궤도+연결형. 경로당 학습 이미지 300장, 30,000회 학습.
- 평가: 학습에 쓰이지 않은 경로별 20장(총 60장)을 각 모델의 COLMAP 재구성에 독립 등록. 지붕·입면·연결부·도로/포장면·수목/녹지 5범주 50개 ROI에서 PSNR·SSIM·LPIPS 측정.

## 결과

- 전체 평균: B가 PSNR, C가 SSIM·LPIPS에서 우수. **A는 5개 구성요소×3개 지표 15개 조합 모두에서 가장 불리**했다.
- 도로·포장면은 B, 입면은 C가 상대적으로 우세했으나 요소별 검정은 Holm 보정 후 유의하지 않아 절대적 우열로 해석하지 않았다.
- 시사점: 3DGS 촬영경로 설계 시 재현 대상의 특성을 함께 고려해야 한다.

## 관련 페이지

- [[kci-drone-pointcloud-bim-registration-extraction]] — 드론 점군 기반 BIM 정합
- [[mission-planning]] — 미션 계획(Survey/Waypoint)
- [[computer-vision-drone]] — 드론 컴퓨터 비전
