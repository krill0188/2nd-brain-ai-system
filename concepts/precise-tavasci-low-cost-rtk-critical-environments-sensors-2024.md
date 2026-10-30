---
title: "Reliability of Real-Time Kinematic (RTK) Positioning for Low-Cost Drones' Navigation across Global Navigation Satellite System (GNSS) Critical Environments"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: hardware
ontology_class: PrecisePositioning
tags: [drone, gnss, rtk, f9p, 차폐, 재고정, 실측]
sources: [inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]
confidence: medium
contested: false
contradictions: []
---

# Reliability of Real-Time Kinematic (RTK) Positioning for Low-Cost Drones' Navigation across Global Navigation Satellite System (GNSS) Critical Environments

- 원문: https://doi.org/10.3390/s24186096^[inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]
- 저자: Luca Tavasci, Francesco Nex, Stefano Gandolfi^[inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]
- 발행: 2024-09-20 (Sensors 24(18), 6096, MDPI 오픈액세스; PMC11435761)^[inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]

## 핵심 내용
저가 u-blox F9P(Holybro H-RTK F9P 키트, 헬리컬 안테나) RTK가 터널 입구, 30 m 높이 건물 벽면 근처, 터널·교량 아래에서 고정(fix)을 잃고 되찾는 특성을 실측. 소프트웨어는 QGroundControl 4.2.0 / PX4 v1.12. 중요: 수신기는 드론이 아니라 카트에 장착해 움직임(시험 1·3은 약 1~2 m/s). 기준국은 로버에서 100 m 미만에 설치(네트워크 RTK/NTRIP은 시험하지 않음).^[inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 시험1(터널 입구, 24회): 고정 상실은 주로 터널 입구 0~5 m 구간. 재고정 지연 2~204 s(25 s 초과 8건 제외 평균 약 9 s). 2회 실행에서 고도 오차 약 2 m의 가짜 고정(false fix).^[inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]
- 시험2(30 m급 벽면 옆 정지, 31회): 가시 위성 7~14개. 재고정 평균 13 s(표준편차 1 s 미만). 가짜 고정으로 높이 오차 약 40 cm 1건.^[inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]
- 시험3(터널 하 이동, 26회): 재고정 6~35 s(35 s 제외 평균 약 11 s, RMS 4 s). 교량 하 10/30/60 s 차단은 성능 변화 없음, 유의한 가짜 고정 없음.^[inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]
- 저자 권고: HRMS/VRMS 4 cm 임계로 가짜 고정 배제(실용 범위 3~5 cm), 재고정 직후에는 정지 비행 대신 수직 0.5 m 또는 수평 1 m 이상 이동. 목표 정확도 10 cm.^[inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]

## 한계·미확인
(1) 실제 드론 비행이 아닌 카트 시험. (2) 기준선 100 m 미만 조건만 시험 → 기선 길이별 오차 자료는 아님. (3) 안테나 장착 위치 비교 없음. (4) 열람 범위: PMC 본문을 WebFetch 요약으로 읽음(요약 도구 경유라 표·그림 세부는 미확인). 신뢰도: 중상(동료심사). 같은 수치가 20261022 리뷰(env-jiang-...)에도 2차 인용됨.^[inbox/processed/hw-20261022-precise-tavasci-low-cost-rtk-critical-environments-sensors-2024.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]

## 📰 최근 관련 소식
- FCC Seeks Input on Simplifying Satellite Communications Rules for Drones (dronelife.com, Mon, 26 Oc) — https://dronelife.com/2026/10/26/fcc-satellite-communications-rules-drones/
