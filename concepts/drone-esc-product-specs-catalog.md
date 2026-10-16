---
title: "드론 ESC 제품 사양 카탈로그 (Holybro Tekko32·KDE UAS95HVC·T-Motor FLAME)"
created: 2026-10-16
updated: 2026-10-16
type: concept
domain: hardware
ontology_class: ESC
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-product-esc-holybro-tekko32-f4-4in1-50a.md, inbox/processed/fetch-2026-10-16-hw-product-esc-holybro-tekko32-f4-metal-65a.md, inbox/processed/fetch-2026-10-16-hw-product-esc-kde-kde-uas95hvc.md, inbox/processed/fetch-2026-10-16-hw-product-esc-tmotor-flame-60a-12s-v2.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 ESC 제품 사양 카탈로그

| 모델 | 전압 | 연속/피크 전류 | 무게·크기 | 신호·기타 |
|---|---|---|---|---|
| Holybro Tekko32 F4 4in1 50A | 4~6S | 50 A×4 / 60 A×4 | 13.8 g, 48×37×6 mm | AM32, DShot150~1200, BEC 없음, 텔레메트리 ^[inbox/processed/fetch-2026-10-16-hw-product-esc-holybro-tekko32-f4-4in1-50a.md] |
| Holybro Tekko32 F4 Metal 65A | 4~6S | 65 A×4 / 75 A×4 | 15.8 g, 43×44 mm | AM32, DShot150~1200, BEC 없음, 1000 µF 커패시터 동봉 ^[inbox/processed/fetch-2026-10-16-hw-product-esc-holybro-tekko32-f4-metal-65a.md] |
| KDE-UAS95HVC | 3S~12S(11.1~52.2 V) | 95 A(180 s) / 165 A(5 s) | 78 g, 37×82 mm | PWM 600 Hz, 옵토 절연, IP56, DShot/CAN 미확인 ^[inbox/processed/fetch-2026-10-16-hw-product-esc-kde-kde-uas95hvc.md] |
| T-Motor FLAME 60A 12S V2 | 6~12S | 60 A / 80 A(10 s) | 미확인 | 시동 실패·스로틀 상실·모터 락업·과부하 보호 ^[inbox/processed/fetch-2026-10-16-hw-product-esc-tmotor-flame-60a-12s-v2.md] |

## 해석
- Tekko32 두 제품은 FPV급 4-in-1 스택(M4 30.5 mm)이고, KDE·FLAME은 대형 멀티콥터용 단품이다.
- 출처 한계: FLAME은 호환 모터 표기가 본문(U12)과 매칭 가이드(P60, MN701-S)에서 상충한다. Holybro는 변형마다 펌웨어 표기(AM32/BLHeli_32)가 다르다는 언급이 있다. 이 부분은 직접 확인하지 못했다.
- KDE는 NDAA 비준수 언급이 검색 요약에 있었으나 직접 확인하지 않았다.
- 고장 사례는 [[drone-esc-failure-cases]], 효율·열 특성은 [[bldc-motor-esc-characterization-research]]를 본다.

관련: [[drone-motor-product-specs-catalog]], [[dronecan-protocol]], [[fpv-hardware]].
