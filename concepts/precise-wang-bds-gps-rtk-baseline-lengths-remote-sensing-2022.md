---
title: "Evaluation of BDS/GPS Multi-Frequency RTK Positioning Performance under Different Baseline Lengths"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
ontology_class: PrecisePositioning
tags: [drone, gnss, rtk, baseline, ambiguity-fixing-rate, 비UAV]
sources: [inbox/processed/hw-20261021-precise-wang-bds-gps-rtk-baseline-lengths-remote-sensing-2022.md]
confidence: medium
contested: false
contradictions: []
---

# Evaluation of BDS/GPS Multi-Frequency RTK Positioning Performance under Different Baseline Lengths

- 원문: https://doi.org/10.3390/rs14153561^[inbox/processed/hw-20261021-precise-wang-bds-gps-rtk-baseline-lengths-remote-sensing-2022.md]
- 저자: Wang, Song, Zhang, Shi, Wang, Xu, Shu (Crossref 성 표기)^[inbox/processed/hw-20261021-precise-wang-bds-gps-rtk-baseline-lengths-remote-sensing-2022.md]
- 발행: 2022-07-25 (Remote Sensing 14(15), 3561)^[inbox/processed/hw-20261021-precise-wang-bds-gps-rtk-baseline-lengths-remote-sensing-2022.md]

## 핵심 내용
IGS/MGEX 관측소 5개 기선 세트로 BDS-3, BDS-2+BDS-3, GPS의 단일·이중·삼중 주파수 RTK 정확도와 모호정수 고정률을 기선 길이별로 평가. 기선이 길어질수록 대기 잔차가 커져 부동해 정확도가 떨어진다. 이중주파수 BDS-3(B1C/B2a)와 삼중주파수 BDS-3(B1C/B2a/B3I)의 고정률은 100 km 이내에서 90% 이상이 될 수 있다고 초록에 서술.^[inbox/processed/hw-20261021-precise-wang-bds-gps-rtk-baseline-lengths-remote-sensing-2022.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 드론 RTK 기선 설계 시 다주파 수신이 장기선에서 고정률·정확도 모두 유리하다는 일반 근거(UAV 실험은 아님).^[inbox/processed/hw-20261021-precise-wang-bds-gps-rtk-baseline-lengths-remote-sensing-2022.md]
- 삼중주파수 BDS-3 가 정확도·고정률에서 이중주파수보다 우수.^[inbox/processed/hw-20261021-precise-wang-bds-gps-rtk-baseline-lengths-remote-sensing-2022.md]
- BDS-2+BDS-3 이중주파수는 GPS 수준의 센티미터급 실시간 상대측위를 제공한다고 서술.^[inbox/processed/hw-20261021-precise-wang-bds-gps-rtk-baseline-lengths-remote-sensing-2022.md]

## 한계·미확인
UAV 가 아닌 지상 고정국 데이터라 비행 동특성·초기화 시간은 다루지 않음. 초기화(TTFF) 초 단위 수치는 초록에 없음. 이 목록의 '드론 RTK 기선별 fix 성능 UAV 실험 논문'은 이번에도 찾지 못함.^[inbox/processed/hw-20261021-precise-wang-bds-gps-rtk-baseline-lengths-remote-sensing-2022.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
