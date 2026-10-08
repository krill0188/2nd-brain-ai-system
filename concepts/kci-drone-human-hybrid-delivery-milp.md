---
title: "드론-인간 혼합배송 입지·네트워크 최적화 MILP (KCI)"
created: 2026-10-08
updated: 2026-10-08
type: concept
domain: ops-mission
tags: [drone, ops-mission, research]
sources: [inbox/processed/fetch-2026-10-08-kci-지형적-특성과-충전소-기능-구분을-고려한-드론-인간-혼합배송의-비용-효율적-입지-및-네트워크-최적화-모형.md]
confidence: low
contested: false
contradictions: []
---

# 드론-인간 혼합배송 비용 최소화 입지 모형

문형훈(청주대)의 경영과학(2026) 논문. 도시 드론-인간 혼합배송을 위한 비용 최소화 **혼합정수선형계획(MILP)** 프레임워크다. 허브·충전소 입지, 설치 시설 간 드론 네트워크 구성, 고객별 배송 수단을 동시에 결정한다.
지형 기반 비행 제약, 지형 의존 비용 가중치, 커버리지 한계, 적재 중량 제약을 반영한다. 초록이 잘려 결과 일부만 확인했다(confidence low).^[inbox/processed/fetch-2026-10-08-kci-지형적-특성과-충전소-기능-구분을-고려한-드론-인간-혼합배송의-비용-효율적-입지-및-네트워크-최적화-모형.md]

## 두 구성 비교

- **Model A**: 설치된 충전소가 고객에게 직접 배송 가능.
- **Model B**: 최종 고객 배송을 지정된 종단(terminal) 충전소로 제한.
- 수치 실험에서 Model B는 드론 이용률을 낮추는 한편 "increasing both"까지만 수집되고 문장이 절단되어, 증가하는 항목과 크기는 확인하지 못했다.

## 관련 페이지

- [[drone-delivery-news]] — 드론 배달 서비스 동향
- [[flytrex-rooftop-docks-ai-fleet-positioning]] — 옥상 도킹스테이션 기반 배달 비용 절감 사례
- [[uav-battery-replacement-planner]] — UAV 배터리 교체 미션 플래너
