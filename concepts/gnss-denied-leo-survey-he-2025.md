---
title: "Survey on positioning technology based on signal of opportunity from low earth orbit"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: navigation-gnss-denied
ontology_class: GNSSDeniedNavigation
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]
confidence: medium
contested: false
contradictions: []
---

# Survey on positioning technology based on signal of opportunity from low earth orbit

- 원문: https://doi.org/10.3389/fphy.2025.1592447^[inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]
- 저자: Jiawei He, Shaojie Ni, Honglei Lin, Zhe Liu, Zhibin Xiao^[inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]
- 발행: 2025-05-20 (Frontiers in Physics 13)^[inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]

## 핵심 내용
LEO 위성 기회신호(SOP) 기반 측위 리뷰. Doppler 측위 원리와 오차원, 관측량 추출(인지 기반/블라인드), Iridium·Orbcomm·Globalstar·Starlink·OneWeb 등 성상별 정리, 향후 방향(위성 식별, 알고리즘 최적화, 다중 소스 융합)을 다룬다.^[inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 정적 수신기 보고 오차(Table 6): Iridium 22 m(2D), Orbcomm 77.5 m(3D), Globalstar 100 m 이하(2D), Starlink 4.3 m(2D)/19.4 m(3D), OneWeb 30.4 m(2D)^[inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]
- 성상: Iridium 66기/6궤도면/약 780 km, Starlink 약 550 km 위주^[inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]
- TLE 궤도 정확도 epoch에서 약 3 km, TRANSIT Doppler 약 70 m^[inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]
- Doppler 최소제곱은 초기 위치 오차 200 km 초과 시 실패^[inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]

## 한계·미확인
본문 앞 100,000자만 확인(후반부 미확인). 드론 탑재 실험 여부는 이 확인 범위에서 미확인.^[inbox/processed/hw-20261021-gnss-denied-leo-survey-he-2025.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
