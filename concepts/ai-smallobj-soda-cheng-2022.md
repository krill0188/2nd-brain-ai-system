---
title: "Towards Large-Scale Small Object Detection: Survey and Benchmarks"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
tags: [drone, ai, small-object-detection, survey, benchmark, aerial]
sources: [inbox/processed/hw-20261021-ai-smallobj-soda-cheng-2022.md]
confidence: medium
contested: false
contradictions: []
---

# Towards Large-Scale Small Object Detection: Survey and Benchmarks

- 원문: https://arxiv.org/abs/2207.14096^[inbox/processed/hw-20261021-ai-smallobj-soda-cheng-2022.md]
- 저자: Gong Cheng, Xiang Yuan, Xiwen Yao, Kebing Yan, Qinghua Zeng, Xingxing Xie, Junwei Han^[inbox/processed/hw-20261021-ai-smallobj-soda-cheng-2022.md]
- 발행: 2022-07-28 (v4 2023-04-11, TPAMI vol.45 no.11)^[inbox/processed/hw-20261021-ai-smallobj-soda-cheng-2022.md]

## 핵심 내용
소형 물체 검출(열악한 외관과 잡음 표현으로 어려움) 서베이와 SODA 벤치마크. SODA-D(주행): 교통 이미지 24,828장, 278,433 인스턴스, 9개 범주. SODA-A(항공): 고해상도 항공 이미지 2,513장, 872,069 인스턴스, 9개 클래스. 주요 검출기를 SODA에서 벤치마크.^[inbox/processed/hw-20261021-ai-smallobj-soda-cheng-2022.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 위 데이터셋 규모 수치(원문).^[inbox/processed/hw-20261021-ai-smallobj-soda-cheng-2022.md]
- 고고도 소형 물체 검출 한계 평가용 벤치마크로 활용 가능.^[inbox/processed/hw-20261021-ai-smallobj-soda-cheng-2022.md]

## 한계·미확인
이미지 픽셀 크기, 검출기별 AP는 초록에 없음(미확인).^[inbox/processed/hw-20261021-ai-smallobj-soda-cheng-2022.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[yolo]]
