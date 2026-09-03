---
title: "군용 무인항공기 지상안테나조립체 BIT 오탐 개선 로직"
created: 2026-09-04
updated: 2026-09-04
type: concept
domain: hardware
tags: [drone, hardware, drone-hw, datalink]
sources: []
confidence: medium
contested: false
contradictions: []
---

# 군용 무인항공기 지상안테나조립체 BIT 오탐 개선 로직

**저자**: 양은석 (국방기술품질원)  
**학술지**: 한국기계항공기술학회지  
**발행연도**: 2026  
**링크**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003370834  
**원문공개**: 공개(KCI 원문 다운로드)

## 연구 배경

군용 UAV는 감시·정찰·통신 중계 임무에 광범위하게 사용되며, 항공기와 지상 통제 장비 간 데이터링크 신뢰성이 안정적 임무 운용의 핵심이다. 지상안테나조립체(Ground Antenna Assembly, GCA)는 항공기 위치 데이터를 기반으로 안테나의 방위각·앙각을 제어하고, LNA·인코더 등 주요 부품 상태를 BIT(Built-In Test)로 모니터링한다.

## 문제 정의

운용 및 점검 중 **BIT 오탐(false alarm)** 사례 발생: 실제 고장이 없음에도 BIT 오류 보고. 주요 원인:

1. LNA BIT 결과 처리 방식의 문제
2. 동일 인코더 값 누적 조건의 부적절성
3. 오류 카운터 처리 로직의 취약성

## 개선 방향

- LNA BIT 판정 알고리즘 수정
- 인코더 값 동일 누적 기준 재설계
- 오류 카운터 임계값 및 클리어 조건 개선

## 의의

군용 드론 지상 장비의 신뢰성 향상을 위한 BIT 오탐 감소 연구로, 지상 데이터링크 장비의 정비·운용 신뢰성 개선에 직접 참고 가능하다. 특히 LNA 및 인코더 기반 GCA 시스템에서 오탐으로 인한 불필요한 정비 소요를 줄이는 실용적 로직을 제시한다.

## 관련 페이지

드론 하드웨어 부품 및 비행 제어기 일반은 [[flight-controller-hardware]]를, 데이터링크 통신 기술은 [[datalink-communication]]을 참조한다.
