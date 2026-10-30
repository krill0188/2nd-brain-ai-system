---
title: "멀티로터 추진계·질량 사이징 방법 (Dai 2019, Burela 2026)"
created: 2026-10-16
updated: 2026-10-30
type: concept
domain: hardware
ontology_class: Multirotor
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-paper-propulsion-optimization-analytical-dai-2019.md, inbox/processed/fetch-2026-10-16-hw-paper-multirotor-mdo-weight-power-burela-sujit-2026.md, inbox/processed/fetch-2026-10-16-hw-paper-propulsion-efficiency-goli-2023.md]
confidence: medium
contested: false
contradictions: []
---

# 멀티로터 추진계·질량 사이징 방법

## Dai 외(2019, IEEE/ASME T-Mech)
호버링 체공 목표에서 설계를 프로펠러 → 모터 → ESC → 배터리 순의 하위 문제로 분리해 해석적으로 풀고, 부품 데이터베이스에서 최근접 제품을 고르는 방법이다. 전진 비행은 포함하지 않고 DB는 2018년 기준이며 ESC 열 손실 포함 여부는 미확인.^[inbox/processed/fetch-2026-10-16-hw-paper-propulsion-optimization-analytical-dai-2019.md]

## Burela & Sujit(2026, 프리프린트)
구조·전기화학·공력·운동학 모델을 동시에 풀어 크기를 정하고 상용 부품(COTS)에 매핑하는 AeroEval 엔진이다. 순차 계산의 오차 누적("Mass Snowball effect")을 지적하며 상용 기체 19종 블라인드 테스트에서 MTOW MAPE 7.2%를 보고한다. DIY 보정 코호트 MAPE는 26.1%로 더 크다.^[inbox/processed/fetch-2026-10-16-hw-paper-multirotor-mdo-weight-power-burela-sujit-2026.md] 같은 논문을 다룬 [[aeroeval-mdo-framework]] 페이지가 이미 있으므로 세부는 그쪽을 참고한다.

## 실험 기반 조합 선정
Goli 외(2023)는 모터 KV·프로펠러 크기·배터리 용량을 바꿔 가며 ESC 신호, 전류, 추력, 토크를 측정하는 절차를 제시한다.^[inbox/processed/fetch-2026-10-16-hw-paper-propulsion-efficiency-goli-2023.md]

관련: [[multirotor-propeller-test-research]], [[multirotor-energy-power-models]], [[drone-hw]], [[ecalc-xcoptercalc]].
