---
title: "UAV-LiDAR 지면점 밀도와 공간 해상도가 DEM 정확도에 미치는 영향"
created: 2026-09-11
updated: 2026-09-11
type: concept
domain: ops-mission
tags: [drone, ops-mission]
sources: [raw/papers/_unclassified/uav-lidar-지면점-밀도와-공간-해상도가-dem-정확도에-미치는-영향.md]
confidence: medium
contested: false
contradictions: []
---

# UAV-LiDAR 지면점 밀도와 공간 해상도가 DEM 정확도에 미치는 영향

UAV-LiDAR는 고밀도 점군을 빠르게 취득할 수 있어 정밀 DEM 제작에 널리 쓰이지만, 데이터양이 많아질수록
저장·처리 부담이 커진다. 이 연구는 항공 LiDAR용 실험설계를 고밀도 UAV-LiDAR 자료에 적용해, 점군
감축이 DEM 정확도에 미치는 영향을 검토했다
^[raw/papers/_unclassified/uav-lidar-지면점-밀도와-공간-해상도가-dem-정확도에-미치는-영향.md].

## 방법

- 안성천 명당교 일대 지면점을 훈련자료 90%·검증점 10%로 분리.
- 훈련자료를 100~0.1%까지 9단계로 축소해 0.10~1.00m 해상도의 DEM을 생성, RMSE로 정확도 평가.

## 결과

- 훈련자료 25% 이상에서는 RMSE 변화가 작음.
- 훈련자료 5~10% 유지 시 RMSE는 4.3~5.5cm 수준.
- 훈련자료 1% 이하로 감소하면 RMSE가 급격히 증가.
- 저밀도 조건에서는 격자 크기(해상도)보다 지면점 부족 자체가 정확도에 더 큰 영향을 미침 — UAV-LiDAR
  점군 감축 시 해상도 조정보다 최소 지면점 밀도 확보를 우선해야 함을 시사.

## 관련 개념

- [[rtk-gps-precise-landing]] — 드론 정밀 측위/착륙 관련 RTK-GPS 활용
- [[micro-drone-slam-imu-vio-lidar-uav-livox-mid-360-pixhawk-4-m]] — 마이크로드론 LiDAR-관성 오도메트리
  플랫폼 비교(동일 LiDAR 매핑 계열)
