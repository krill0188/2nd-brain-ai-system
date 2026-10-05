---
title: "UAV LiDAR CHM·그레이스케일 Watershed 개체목 분할 최적 조건 (KCI 2026)"
created: 2026-10-04
updated: 2026-10-04
type: concept
domain: ops-mission
tags: [drone, ops-mission]
sources: [raw/papers/_unclassified/analysis-of-optimal-conditions-for-individual-tree-delineation-using-watershed-a.md]
confidence: low
contested: false
contradictions: []
---

# UAV LiDAR CHM·그레이스케일 Watershed 개체목 분할 최적 조건 (KCI 2026)

신아리(강원대)의 Journal of forest and environmental science 논문. 수집 초록이 중간에서 절단되어
정확도 결과는 확인되지 않았다.^[raw/papers/_unclassified/analysis-of-optimal-conditions-for-individual-tree-delineation-using-watershed-a.md]

- 목적: UAV 유래 수관고모델(CHM)과 그레이스케일 영상으로 Watershed 수관 분할의 최적 조건 도출.
- 시험지: 포천(잣나무·낙엽송 침엽수림)과 청주(신갈나무 활엽수림) 3개 플롯.
- 변수: CHM·그레이스케일을 5/25/50 cm 해상도로 구성, 틈(gap) 영역을 Otsu·Entropy·Percentile(5/10/15%)
  3가지 임계법으로 분류 후 Watershed 분할, 육안판독 기준자료와 정확도 비교.

## 관련 개념

- [[drone-lidar-forest-boundary]] — 드론 LiDAR 산림 경계 활용
- [[kci-uav-lidar-ground-point-density-dem-accuracy]] — UAV LiDAR 지면점 밀도와 DEM 정확도
- [[kci-hallasan-fir-ndvi-vitality-assessment]] — 드론 기반 산림 활력 평가
