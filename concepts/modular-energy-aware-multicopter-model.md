---
title: "모듈식 에너지 인식 멀티콥터 모델 (Gasche 외, 2025)"
created: 2026-10-19
updated: 2026-10-19
type: concept
domain: hardware
tags: [drone, drone-hw]
sources: [inbox/processed/fetch-2026-10-19-arxiv-a-modular-energy-aware-framework-for-multicopter-modeling-in.md]
confidence: medium
contested: false
contradictions: []
---

# 모듈식 에너지 인식 멀티콥터 모델

제어·경로계획용으로 기체 동역학, 에너지 소비, 센서 통합을 모듈로 나눠 기술한 모델링 프레임워크다(arXiv 2504.03256, 2025-04). 초록 기준 요약이다.^[inbox/processed/fetch-2026-10-19-arxiv-a-modular-energy-aware-framework-for-multicopter-modeling-in.md]

## 핵심 내용
- 파워트레인 모델은 리튬이온 배터리, ESC, BLDC 모터를 구성요소별로 기술하며 실제 시험비행 데이터로 검증했다고 한다.
- LiDAR·카메라 센서 모델을 합쳐 감시·모니터링 임무 장비를 표현하고, 이를 묶어 에너지 인식 멀티콥터 모델을 만든다.
- 이 모델은 수색구조 군집 경로계획 후속 연구의 기반이며, 이종 군집의 기체별 모델링을 쉽게 한다고 주장한다.

## 연결
전력 모델 개요는 [[multirotor-energy-power-models]], 배터리 특성은 [[drone-power-battery]], 모터/ESC 특성화는 [[bldc-motor-esc-characterization-research]] 참조. 초록에 정량 결과는 없다.
