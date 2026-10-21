---
title: "AeroMap3D: Anchoring Monocular UAV 6-DoF Localization to Visual-Geometric-Semantic Map Priors"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: navigation-gnss-denied
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-gnss-denied-aeromap3d-2607.14009.md]
confidence: medium
contested: false
contradictions: []
---

# AeroMap3D: Anchoring Monocular UAV 6-DoF Localization to Visual-Geometric-Semantic Map Priors

- 원문: https://arxiv.org/abs/2607.14009^[inbox/processed/hw-20261021-gnss-denied-aeromap3d-2607.14009.md]
- 저자: Zhiyun Deng, Luis Sentis^[inbox/processed/hw-20261021-gnss-denied-aeromap3d-2607.14009.md]
- 발행: 2026-07-15 (arXiv, cs.RO)^[inbox/processed/hw-20261021-gnss-denied-aeromap3d-2607.14009.md]

## 핵심 내용
단안 카메라 영상을 위성 지도 타일, DEM, OpenStreetMap 의미 정보에 정합하여 GNSS 없이 드론 6-DoF 자세를 추정한다. 스케일·요 보정 어댑터로 사전학습된 dense matcher를 재학습 없이 쓰고, 의미적으로 신뢰도 낮은 매칭은 걸러 RANSAC-PnP로 자세를 구한 뒤 지연 상태 EKF로 상대 운동 사전정보와 융합한다.^[inbox/processed/hw-20261021-gnss-denied-aeromap3d-2607.14009.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 오스틴 8개 지점의 모든 궤적을 50 m 이내로 위치 추정(초록)^[inbox/processed/hw-20261021-gnss-denied-aeromap3d-2607.14009.md]
- 55 km 비행에서 평균 3D 오차 5.88 m(초록)^[inbox/processed/hw-20261021-gnss-denied-aeromap3d-2607.14009.md]
- 지연 상태 EKF로 지도 기반 측정(지연 도착)을 융합하는 구조 참고 가능^[inbox/processed/hw-20261021-gnss-denied-aeromap3d-2607.14009.md]

## 한계·미확인
초록만 확인. 하드웨어 사양·연산 부하·계절/조명 변화 강건성은 미확인.^[inbox/processed/hw-20261021-gnss-denied-aeromap3d-2607.14009.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
