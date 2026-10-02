---
title: UTM (UAS Traffic Management)
created: 2026-08-06
updated: 2026-10-02
type: concept
tags: [drone, regulations, utm]
sources: [inbox/processed/fetch-2026-10-02-kci-다양한-지역-환경에서의-utm-k-기반-드론-비행경로-오차-분석.md]
confidence: medium
contested: false
contradictions: []
domain: regulations
---

# UTM (UAS Traffic Management)

UTM은 저고도 공역에서 다수 드론의 안전한 운용을 조율하기 위한 교통관리 체계다. 유인 항공 관제(ATM)와 별도로, 자동화·분산형 방식으로 드론 간 충돌 회피, 지오펜싱, 비행 승인을 처리한다.

## 핵심 기능

- **비행 승인/등록**: 사전 미션 등록 및 공역 접근 승인
- **Detect-and-Avoid(DAA)**: 실시간 충돌 회피
- **지오펜싱**: 금지/제한 구역 자동 회피
- **BVLOS 지원**: 비가시권 비행을 위한 감시·통신 인프라

## 지역별 프레임워크

- **미국**: FAA UTM 개념, Section 2209 UAFR
- **영국**: UK CAA Airspace Architecture (SESAR 연계 HAVEN 프로젝트 등)

## 국내 실증 사례: UTM-K 좌표계 기반 비행경로 오차 분석 (KCI, 2026)

공주·여수·울주·통영·포천 5개 지역의 드론 배송 실증 데이터를 UTM-K 직교좌표계로 변환해 계획
경로 대비 오차를 분석한 결과, 모든 구간에서 한국교통안전공단의 드론 배송 실증사업 안전
기준을 만족했고 오차율도 허용 범위 내로 유지됐다. 도심·도서·해안·산간 등 서로 다른 운용
환경에서도 UTM-K 기반 오차 분석 방법론이 안정적으로 적용 가능함을 시사한다.^[inbox/processed/fetch-2026-10-02-kci-다양한-지역-환경에서의-utm-k-기반-드론-비행경로-오차-분석.md]

## 관련 개념

- [[faa-section-2209-uafr]] — 미국 UAFR 규정
- [[uk-caa-airspace-architecture]] — 영국 CAA 공역 아키텍처
- [[kci-utm-k-flight-path-error-regional-analysis]] — UTM-K 기반 비행경로 오차 분석(5개 지역 실증, KCI)
- [[kci-korea-airspace-eu-uspace]] — 드론 공역시스템 비교: 한국형 드론 공역시스템 vs EU U-space
