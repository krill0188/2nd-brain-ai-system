---
title: "GNSS Airborne Multipath Error Modeling Under UAV Platform and Operating Environment"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
ontology_class: GNSSSignalsEnvironment
tags: [drone, gnss, multipath]
sources: [inbox/processed/hw-20261021-env-kim-uav-airborne-multipath-jpnt-2015.md]
confidence: medium
contested: false
contradictions: []
---

# GNSS Airborne Multipath Error Modeling Under UAV Platform and Operating Environment

- 원문: https://doi.org/10.11003/jpnt.2015.4.1.001^[inbox/processed/hw-20261021-env-kim-uav-airborne-multipath-jpnt-2015.md]
- 저자: Minchan Kim, Kiwan Kim, Dong-Kyeong Lee, Jiyun Lee^[inbox/processed/hw-20261021-env-kim-uav-airborne-multipath-jpnt-2015.md]
- 발행: 2015-03-15 (Journal of Positioning, Navigation, and Timing, vol. 4, no. 1, pp. 1-7)^[inbox/processed/hw-20261021-env-kim-uav-airborne-multipath-jpnt-2015.md]

## 핵심 내용
UAV 에 설치한 GNSS 센서의 멀티패스 오차를 비행시험으로 모델링하고 유인기 오차모델과 비교했다. 시나리오는 고도 40 m 호버링. 멀티패스 오차값이 기존 유인기 오차모델 범위 내에 잘 포함되어(well bound) 유사한 운용환경에서는 유인기 모델을 쓸 수 있다고 결론. 다수 UAV 운용 시나리오도 고려해, UAV 간 멀티패스 오차의 상관이 크지 않아 서로 상쇄되지 않는다고 분석했다. 열람 경로: 출판사 DOI 가 koreascience.or.kr 초록 페이지로 연결됨(KCI 등재 여부는 확인 못 함).^[inbox/processed/hw-20261021-env-kim-uav-airborne-multipath-jpnt-2015.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 시험 조건: 고도 40 m 호버링 (초록)^[inbox/processed/hw-20261021-env-kim-uav-airborne-multipath-jpnt-2015.md]
- 멀티패스 오차는 유인기 오차모델로 bound 됨 (초록)^[inbox/processed/hw-20261021-env-kim-uav-airborne-multipath-jpnt-2015.md]
- UAV 간 멀티패스 오차 상관 크지 않음 → 다수 기체 오차 상쇄 기대 불가 (초록)^[inbox/processed/hw-20261021-env-kim-uav-airborne-multipath-jpnt-2015.md]

## 한계·미확인
오차 크기(m) 등 정량 수치와 안테나 설치 위치·접지판 조건은 초록에 없어 미확인.^[inbox/processed/hw-20261021-env-kim-uav-airborne-multipath-jpnt-2015.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
