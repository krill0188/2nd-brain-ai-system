---
title: "RTK and PPK GNSS Positioning Accuracy Assessment for UAVs Using a PPS-Synchronized Robotic Total Station"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: hardware
ontology_class: PrecisePositioning
tags: [drone, gnss, rtk, ppk, total-station, 단기선, 실측]
sources: [inbox/processed/hw-20261022-precise-beni-rtk-ppk-uav-total-station-sensors-2026.md]
confidence: medium
contested: false
contradictions: []
---

# RTK and PPK GNSS Positioning Accuracy Assessment for UAVs Using a PPS-Synchronized Robotic Total Station

- 원문: https://doi.org/10.3390/s26154907^[inbox/processed/hw-20261022-precise-beni-rtk-ppk-uav-total-station-sensors-2026.md]
- 저자: Alessandra Beni, Luca Bigazzi, Lapo Miccinesi, Andrea Cioncolini, Andrea Bulletti, Lorenzo Pagnini, Enrico Boni, Massimiliano Pieraccini^[inbox/processed/hw-20261022-precise-beni-rtk-ppk-uav-total-station-sensors-2026.md]
- 발행: 2026 (Sensors 26(15), 4907, MDPI 오픈액세스; Università degli Studi di Firenze)^[inbox/processed/hw-20261022-precise-beni-rtk-ppk-uav-total-station-sensors-2026.md]

## 핵심 내용
비행 중 드론의 RTK/PPK 위치를 사진측량 산출물이 아니라 로봇 토털스테이션(TS) 독립 기준과 직접 비교. 플랫폼은 VESTA(듀얼 GNSS, IMU, UTC 동기 로깅). GNSS 안테나 2개를 기체 상부에 3D 프린트 지지대로 장착, 수평 기선 525 mm. GNSS PPS와 TS 프리즘 이동으로 시간 정렬.^[inbox/processed/hw-20261022-precise-beni-rtk-ppk-uav-total-station-sensors-2026.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 보고 품질이 최적일 때 RTK와 PPK 모두 TS 대비 오차 약 0.05 m로 비슷.^[inbox/processed/hw-20261022-precise-beni-rtk-ppk-uav-total-station-sensors-2026.md]
- 비행 전체 구간 RMSE: RTK 0.126 m / 0.118 m (비행 a / b), PPK 0.390 m / 0.205 m. GNSS 열화 뒤 PPK는 float 또는 저하 상태가 더 오래 지속되어 일시 오차가 큼(RTKLIB-EX 설정 기준).^[inbox/processed/hw-20261022-precise-beni-rtk-ppk-uav-total-station-sensors-2026.md]
- PPK 설정 민감도: 고도각 마스크 15도에서 10도로 낮추면 전체 RMSE가 비행 a 0.037 m, 비행 b 0.027 m 감소. 20도로 올리면 비행 a에서 0.231 m 증가. GPS 단독 처리는 가장 크게 악화.^[inbox/processed/hw-20261022-precise-beni-rtk-ppk-uav-total-station-sensors-2026.md]

## 한계·미확인
**기선 길이 영향은 시험하지 않음**: 논문이 직접 '단기선 구성(RTK와 PPK 모두 같은 로컬 기준국 사용)'이라고 쓰고, 더 긴 기선과 제3자 기준국은 향후 과제로 명시. 따라서 이 자료는 항목 3(기선 길이별 오차)을 채우지 못함. 기준국·수신기 모델, 비행 고도·거리는 이번 열람에서 확인하지 못함(미확인). 열람 범위: MDPI 본문 전체(Bright Data), 관련 절만 grep으로 확인. 신뢰도: 중상(동료심사).^[inbox/processed/hw-20261022-precise-beni-rtk-ppk-uav-total-station-sensors-2026.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
