---
title: "BeiDou Signal Plan (Navipedia, ESA)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: rf-datalink-engineering
ontology_class: GNSSSignalsEnvironment
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-gnss-signals-beidou-navipedia.md]
confidence: medium
contested: false
contradictions: []
---

# BeiDou Signal Plan (Navipedia, ESA)

- 원문: https://gssc.esa.int/navipedia/index.php/BeiDou_Signal_Plan^[inbox/processed/hw-20261021-gnss-signals-beidou-navipedia.md]
- 저자: ESA Navipedia^[inbox/processed/hw-20261021-gnss-signals-beidou-navipedia.md]
- 발행: 미확인^[inbox/processed/hw-20261021-gnss-signals-beidou-navipedia.md]

## 핵심 내용
BeiDou의 B1I, B1C, B2a, B2b, B3 대역별 반송파 주파수를 정리한 문서. 드론용 다중성상 수신기에서 BDS 신호가 GPS/Galileo와 어느 대역을 공유하는지 파악할 수 있다.^[inbox/processed/hw-20261021-gnss-signals-beidou-navipedia.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- B1I 1561.098 MHz, B1C 1575.42 MHz, B2a 1176.45 MHz, B2b 1207.14 MHz, B3I 1268.520 MHz^[inbox/processed/hw-20261021-gnss-signals-beidou-navipedia.md]
- B1C는 GPS L1/Galileo E1과, B2a는 GPS L5/Galileo E5a와 같은 중심주파수^[inbox/processed/hw-20261021-gnss-signals-beidou-navipedia.md]

## 한계·미확인
변조 방식·코드율은 이 확인 범위에서 미확인. BDS-2/BDS-3 신호 구분 미확인.^[inbox/processed/hw-20261021-gnss-signals-beidou-navipedia.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
