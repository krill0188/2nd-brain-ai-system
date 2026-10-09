---
title: "UAV 기반 강우 유발 지형 변화 분석: 이종 데이터 비교와 탐지한계 (KCI)"
created: 2026-10-03
updated: 2026-10-09
type: concept
domain: ops-mission
tags: [drone, ops-mission, drone-ai]
sources: [inbox/processed/fetch-2026-10-03-kci-uav-based-analysis-of-rainfall-induced-terrain-change.md, raw/papers/_unclassified/uav-based-analysis-of-rainfall-induced-terrain-change.md]
confidence: low
contested: false
contradictions: []
---

# UAV 기반 강우 유발 지형 변화 분석

윤공현(강원대학교)이 대한토목학회논문집(2026)에 발표한 연구. 산사태 등 지형 변화를 정량화하려면
사건 전·후 지형자료를 정밀하게 비교해야 하는데, 취득일·센서 종류·공간해상도·위치정확도가 서로
다른 자료를 비교하면 측정 오차가 실제 변화로 오해될 수 있다는 문제를 다룬다. 원문은 비공개이며,
수집된 초록은 중간에서 절단되어 있어 **결론부 수치는 확인하지
못했다.**^[inbox/processed/fetch-2026-10-03-kci-uav-based-analysis-of-rainfall-induced-terrain-change.md]

## 방법

- **사건 전 지형**: 1:5,000 수치지도의 등고선·표고점으로 TIN(불규칙 삼각망)을 구성해 복원.
- **사건 후 지형**: UAV LiDAR로 DTM 생성.
- 두 자료에 지형변화탐지(GCD, geomorphic change detection)를 적용.

## 확인된 수치

- 안정 구간(도로)의 잔차 표고차: 평균 -0.04 m, 표준편차 0.84 m → 평균 수직 오프셋은 산포 대비
  무시 가능한 수준.
- 이에 따라 경험적 **최소 탐지한계(LoD) 0.84 m**를 적용(이보다 작은 표고 변화는 변화로 해석하지
  않음).

## 시사점

이종 자료 비교에서는 안정 지물 구간의 잔차 분포로 LoD를 정해야 측정 오차를 실제 변화로 오인하지
않는다는 점이 핵심이다. UAV-LiDAR DEM 정확도 변수는 [[kci-uav-lidar-ground-point-density-dem-accuracy]]
참조.

## 관련 페이지

- [[kci-uav-lidar-ground-point-density-dem-accuracy]] — 지면점 밀도·해상도와 DEM 정확도
- [[drone-lidar-forest-boundary]] — 드론 라이다 임야 경계 추출
- [[emesent-trimble-lidar-integration]] — 모바일 SLAM 스캐너 측량 워크플로
- [[kci-uav-random-walk-debris-flow-reproducibility]] — UAV 관측범위를 정답으로 쓴 토석류 이동범위 모의 재현성 평가(같은 UAV 지형 변화 관측 계열)

## 📰 최근 관련 소식
- 아산시, 최신 항공·드론영상으로 도시 변화 신속 파악 (뉴데일리 충청세종, Wed, 07 Oc) — https://news.google.com/rss/articles/CBMiekFVX3lxTFBNdWFfTjhZcXNQTFYyanVhbnV5Q2NyYW9McURFZk9jTWtJZ3llZUJtSGdwSkRoWU4wOUVQRjVlTWl6YXBOZ3cydF90ckF2RnRpSGlqWU8zWXh6TzUydFpkYjZaWm9GVDdpbDJ2R0NkLUlrNm5xRGdXUjJB0gF_QVVfeXFMT2ZrVHRkcVRiQVpXMUQ4MzN3VzJUSFhOdXN1aFk5am9uZlVFX1lDbTdpMC15dndpUTkwMkxqNGlmVXNnTU1Bc0JqWXRxSnFhd2EyLTVRNWZqR240anYzSDJLcUdIV0ZmWXhNb3NKbmtOMkFiMndmcXdfMDF5bGFiWQ?oc=5
