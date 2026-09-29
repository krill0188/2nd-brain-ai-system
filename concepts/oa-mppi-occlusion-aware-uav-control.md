---
title: "OA-MPPI: 가림(occlusion) 인지 MPPI 기반 UAV 비행 제어"
created: 2026-09-26
updated: 2026-09-26
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [raw/papers/_unclassified/oa-mppi-occlusion-aware-model-predictive-path-integral-control-for-uav-flight.md]
confidence: medium
contested: false
contradictions: []
---

# OA-MPPI: 가림 인지 MPPI 기반 UAV 비행 제어

Palladino, Yang, Zhang, Mueller(arXiv 2609.28709, 2026-09-23)는 관측된 장애물뿐 아니라 센서가 볼 수 없는
가림 영역에서 튀어나올 수 있는 이동 개체까지 고려하는 MPPI(Model Predictive Path Integral) 확장인
OA-MPPI를 제안했다.^[raw/papers/_unclassified/oa-mppi-occlusion-aware-model-predictive-path-integral-control-for-uav-flight.md]

## 핵심 내용

- **가림 경계 추출**: 매 계획 주기마다 온라인 점유 지도에서 3D 가림 경계를 추출한다.
- **확장 영역 모델링**: 숨은 개체가 예측 구간 동안 도달할 수 있는 영역을 확장되는 영역으로 모델링하고,
  MPPI 롤아웃 중 이 영역에 진입하는 궤적에 페널티를 준다.
- **동역학**: 비선형 쿼드로터 동역학과 개별 로터 추력 한계를 반영한 롤아웃을 사용한다.
- **검증**: 시뮬레이션과 실기체 비행에서 전체 파이프라인을 기체 탑재(onboard) 실시간으로 구동했고,
  기준 MPPI 대비 가림 경계와의 이격이 증가했으며 시뮬레이션에서 가림 뒤에서 나타난 개체를 회피했다.

## 한계

초록만 수집되어 정량 수치(이격 거리, 연산 주기)와 비교 기준 세부는 확인되지 않았다.

## 관련 개념

- [[multi-uav-collision-avoidance-survey]] — 다중 UAV 충돌 회피 서베이
- [[pilot-uav-motion-planning]] — UAV 모션 플래닝
- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용
