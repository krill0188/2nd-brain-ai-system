---
title: "드론 전원 모듈 사양 카탈로그 (Holybro PM02·CUAV CAN PMU Lite·mRo Power Zero)"
created: 2026-10-16
updated: 2026-10-16
type: concept
domain: hardware
ontology_class: Battery
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-product-power-module-holybro-pm02-v3-12s.md, inbox/processed/fetch-2026-10-16-hw-product-power-module-holybro-pm02d.md, inbox/processed/fetch-2026-10-16-hw-product-power-module-cuav-can-pmu-lite.md, inbox/processed/fetch-2026-10-16-hw-product-power-module-mro-power-zero-m10077.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 전원 모듈 사양 카탈로그

| 모델 | 입력 | 전류 | 센싱 출력 | 무게·크기 |
|---|---|---|---|---|
| Holybro PM02 V3 12S | 2~12S | 연속 60 A / 버스트 100 A, 센싱 최대 120 A | 아날로그 6핀 JST-GH, 5.2 V 3 A | 20 g ^[inbox/processed/fetch-2026-10-16-hw-product-power-module-holybro-pm02-v3-12s.md] |
| Holybro PM02D | 2~12S | 연속 60 A / 버스트 100 A, 센싱 최대 327 A | I2C 디지털, 5.2 V 3 A | 20 g ^[inbox/processed/fetch-2026-10-16-hw-product-power-module-holybro-pm02d.md] |
| CUAV CAN PMU Lite | 10~60 V(페이지 내 10~62 V 병기) | 최대 90 A(기능 목록 110 A) | DroneCAN(UAVCAN), 5.2 V 4 A | 140×25×13 mm ^[inbox/processed/fetch-2026-10-16-hw-product-power-module-cuav-can-pmu-lite.md] |
| mRo Power Zero | 12S(50.4 V) | 센싱 최대 90 A | 아날로그, 5.3 V 2 A | 2.5 g, 18×18 mm ^[inbox/processed/fetch-2026-10-16-hw-product-power-module-mro-power-zero-m10077.md] |

## 호환성 요점
- 아날로그 PM02 V3는 Pixhawk 5X/6X와 호환되지 않으므로 디지털 PM02D를 써야 한다. PM02D는 Pixhawk 6C·4·Durandal처럼 아날로그 PM을 쓰는 FC와 비호환이다. ^[inbox/processed/fetch-2026-10-16-hw-product-power-module-holybro-pm02d.md]
- PM02D는 ArduPilot 4.4 이상, PX4 HV 버전을 지원한다.
- CAN PMU Lite는 ArduPilot Copter 3.7+, PX4 1.10.1+ 지원이다. 입력 전압·최대 전류·프로세서(STM32F103/F412)가 페이지 안에서 상충하므로 구매 전 제조사 확인이 필요하다. 수집 시점에는 품절이었다.
- 두 Holybro 모듈의 XT60·12~14AWG 배선 정격은 연속 30 A / 버스트 60 A이며, 그 이상은 커넥터·배선 교체가 필요하다.
- mRo는 문서 사이트에 "unmaintained" 경고가 있고, ArduPilot 기준 BATT_VOLT_MULT 15.30, BATT_AMP_PERVLT 50이다. 보드에 인쇄된 값을 우선 적용한다. ^[inbox/processed/fetch-2026-10-16-hw-product-power-module-mro-power-zero-m10077.md]

관련: [[drone-power-battery]], [[flight-controller-hardware]], [[dronecan-protocol]], [[pixhawk]].

## 📰 최근 관련 소식
- [Painless360] Why modern RC radio power buttons are safer than you think! (youtube.com, 2026-10-20) — https://www.youtube.com/watch?v=DLFeyCly0T8
