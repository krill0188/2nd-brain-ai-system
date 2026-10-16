---
title: "드론 모터 제품 사양 카탈로그 (KDE·T-Motor·Scorpion·Hobbywing·Holybro)"
created: 2026-10-16
updated: 2026-10-16
type: concept
domain: hardware
ontology_class: Motor
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-product-motor-kde-kde5215xf-435.md, inbox/processed/fetch-2026-10-16-hw-product-motor-tmotor-mn505-s-kv320.md, inbox/processed/fetch-2026-10-16-hw-product-motor-scorpion-hkiv-4035-560kv.md, inbox/processed/fetch-2026-10-16-hw-product-motor-hobbywing-xrotor-x8-g2.md, inbox/processed/fetch-2026-10-16-hw-product-motor-holybro-ripper-1404-3800kv.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 모터 제품 사양 카탈로그

제조사 공식 페이지 게재값 기준이다. 모터 선정 이론은 [[fpv-motor-selection-guide]], 추진계 설계 방법은 [[multirotor-propulsion-sizing-methods]]를 본다.

| 모델 | KV | 연속 전류/출력 | 무게 | 전압 | 비고 |
|---|---|---|---|---|---|
| KDE5215XF-435 | 435 | 72 A / 1,595 W (180 s) | 305 g | 4S~8S | ф60×41 mm, 24N22P, 권장 ESC UAS95HVC ^[inbox/processed/fetch-2026-10-16-hw-product-motor-kde-kde5215xf-435.md] |
| T-Motor MN505-S KV320 | 320 | 피크 55 A / 1,300 W (180 s) | 225 g | 6S | ф55.6×38.9, IP45, 최대 추력 6.6 kg, 프롭 20~22" ^[inbox/processed/fetch-2026-10-16-hw-product-motor-tmotor-mn505-s-kv320.md] |
| Scorpion HKIV-4035-560KV | 560 | 100 A / 4,440 W | 456 g | 최대 12S | RC 헬리콥터 라인, 드론 전용 아님 ^[inbox/processed/fetch-2026-10-16-hw-product-motor-scorpion-hkiv-4035-560kv.md] |
| Hobbywing XRotor X8 G2 | 100 | 정격 20 A | 1,095 g(케이블·프롭 포함) | 12~14S | 최대 추력 17.5 kg, PWM+DroneCAN, IPX6 ^[inbox/processed/fetch-2026-10-16-hw-product-motor-hobbywing-xrotor-x8-g2.md] |
| Holybro Ripper 1404 3800KV | 3800 | 미확인 | 미확인 | 3S/4S | 2.5~4" 경량 기체용, 상세 수치는 이미지에만 있음 ^[inbox/processed/fetch-2026-10-16-hw-product-motor-holybro-ripper-1404-3800kv.md] |

## 출처 내 불일치·한계
- T-Motor MN505-S: 설명부 제목이 KV380이고, 6S 정격인데 ESC는 12S 제품을 권장한다.
- Scorpion: 다른 자료에는 4,200 W로 적혀 있다는 언급이 있으나 직접 확인하지 못했다.
- KDE의 연속 정격은 권선 위 5 mph 이상 기류 조건이다.
- 효율·추력 곡선은 대부분 미게재다. 실측은 [[multirotor-propeller-test-research]], 효율 특성은 [[bldc-motor-esc-characterization-research]]를 참고한다.

관련: [[drone-esc-product-specs-catalog]], [[drone-propeller-product-specs-catalog]], [[drone-power-battery]].
