---
title: "Multi-GNSS-Weighted Interpolated Tropospheric Delay to Improve Long-Baseline RTK Positioning"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
ontology_class: PrecisePositioning
tags: [drone, gnss, rtk, baseline]
sources: [inbox/processed/hw-20261021-precise-mirmohammadian-ztd-long-baseline-rtk-sensors-2022.md]
confidence: medium
contested: false
contradictions: []
---

# Multi-GNSS-Weighted Interpolated Tropospheric Delay to Improve Long-Baseline RTK Positioning

- 원문: https://doi.org/10.3390/s22155570^[inbox/processed/hw-20261021-precise-mirmohammadian-ztd-long-baseline-rtk-sensors-2022.md]
- 저자: Farinaz Mirmohammadian, Jamal Asgari, Sandra Verhagen, Alireza Amiri-Simkooei^[inbox/processed/hw-20261021-precise-mirmohammadian-ztd-long-baseline-rtk-sensors-2022.md]
- 발행: 2022-07-26 (Sensors, vol. 22, 5570)^[inbox/processed/hw-20261021-precise-mirmohammadian-ztd-long-baseline-rtk-sensors-2022.md]

## 핵심 내용
중장거리 기선 RTK 에서 대류권 지연이 주요 오차원이라는 전제로, 유럽 6개 관측소 네트워크에서 이중차분 천정 대류권 지연(ZTD)을 모호정수·위치와 함께 추정했다. IGS ZTD 와의 비교에서 평균 RMSE 약 12 mm. 인접 기준국 ZTD 를 보간한 사전값을 준관측치로 넣으면 표준 RTK(ZTD 미지수) 대비 위치 정확도 약 50% 향상. 모호정수 해결(IAR) 성공률도 증가(초록이 "nearly 1."에서 잘림, 증가폭 수치는 미확인).^[inbox/processed/hw-20261021-precise-mirmohammadian-ztd-long-baseline-rtk-sensors-2022.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- ZTD 추정 vs IGS: 평균 RMSE 약 12 mm^[inbox/processed/hw-20261021-precise-mirmohammadian-ztd-long-baseline-rtk-sensors-2022.md]
- 보간 ZTD 사전 제약 시 위치 정확도 약 50% 개선^[inbox/processed/hw-20261021-precise-mirmohammadian-ztd-long-baseline-rtk-sensors-2022.md]
- 기선이 길수록 대류권 보정이 RTK 고정(fix) 성능의 핵심 변수라는 점(드론 RTK 에 직접 적용한 시험은 아님)^[inbox/processed/hw-20261021-precise-mirmohammadian-ztd-long-baseline-rtk-sensors-2022.md]

## 한계·미확인
UAV 시험 아님. 기선 길이별 고정 시간·고정률 표는 초록에 없음. 드론 RTK 기선 길이별 성능 실험 논문(공백 5c)은 이번에 UAV 전용 논문을 확인하지 못함.^[inbox/processed/hw-20261021-precise-mirmohammadian-ztd-long-baseline-rtk-sensors-2022.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
