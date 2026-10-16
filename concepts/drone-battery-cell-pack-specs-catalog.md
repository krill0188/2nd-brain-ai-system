---
title: "드론 배터리 셀·팩 사양 카탈로그 (Molicel P50B·Tattu 16000mAh·Amprius SiCore)"
created: 2026-10-16
updated: 2026-10-16
type: concept
domain: hardware
ontology_class: Battery
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-product-battery-molicel-inr-21700-p50b.md, inbox/processed/fetch-2026-10-16-hw-product-battery-tattu-plus-16000mah-6s-15c.md, inbox/processed/fetch-2026-10-16-hw-product-battery-amprius-sicore.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 배터리 셀·팩 사양 카탈로그

| 제품 | 유형 | 핵심 사양 |
|---|---|---|
| Molicel INR-21700-P50B | Li-ion 21700 셀 | 5,000 mAh(최소 4,850), 3.6 V 공칭, 연속 방전 60 A, 260 Wh/kg, 71 g 이하, 직경 21.55×70.15 mm ^[inbox/processed/fetch-2026-10-16-hw-product-battery-molicel-inr-21700-p50b.md] |
| Tattu Plus 16000mAh 6S 15C | LiPo 스마트 팩 | 22.2 V 6S1P, 15C(버스트 30C), 1,932 g, 203×82×70 mm, XT90-S, BMS 경보 ^[inbox/processed/fetch-2026-10-16-hw-product-battery-tattu-plus-16000mah-6s-15c.md] |
| Amprius SiCore | 실리콘 음극 셀 | 340/390/450 Wh/kg 3종, 방전 최대 10C 연속, 용량·전압·무게 미확인 ^[inbox/processed/fetch-2026-10-16-hw-product-battery-amprius-sicore.md] |

## 주의
- P50B는 셀 데이터시트이며 드론 전용 사양서가 아니다. 사이클 수명 수치는 그래프로만 있다.
- Tattu는 에너지 밀도와 사이클 수를 게재하지 않는다. 계산하면 22.2 V×16 Ah≈355 Wh, 약 184 Wh/kg이지만 이는 이 위키의 산술 추정이다.
- Amprius는 표의 1,000 Wh/L와 프레스 릴리스의 950 Wh/L가 불일치한다. 모델별 매칭도 미확인이다. 별도 페이지는 [[amprius-sicore-battery]]다.
- 방전 모델 검증은 [[multirotor-energy-power-models]]에서 다룬다.

관련: [[drone-power-battery]], [[drone-power-module-specs-catalog]], [[uav-alternative-power-hybrid-fuel-cell-research]].
