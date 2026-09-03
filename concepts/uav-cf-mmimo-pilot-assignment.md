---
title: "이동성 인식 파일럿 할당 for UAV-only CF-mMIMO 네트워크"
created: 2026-09-04
updated: 2026-09-04
type: concept
domain: comms-protocol
tags: [drone, datalink, comms-protocol]
sources: []
confidence: medium
contested: false
contradictions: []
---

# 이동성 인식 파일럿 할당 for UAV-only CF-mMIMO 네트워크

**저자**: Mahdi Haider Salih (University of Tabriz, Iran)  
**학술지**: ICT Express  
**발행연도**: 2026  
**링크**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003377291  
**원문공개**: 비공개(페이월)

## 연구 개요

셀프리 대규모 다중 입출력(CF-mMIMO) 네트워크에서 UAV만으로 구성된 시스템의 파일럿 할당 문제를 다룬다. UAV의 고이동성과 급변하는 채널 조건이 파일럿 오염(pilot contamination) 문제를 심화시킨다는 점에 주목하여, 이를 사전에 완화하는 프레임워크를 제안한다.

## 핵심 기법

- **칼만 필터 기반 궤적 예측**: 채널 변화를 사전 예측해 파일럿 할당 의사결정에 활용
- **이동성 인식 보상 설계**: UAV 속도·방향을 보상 함수에 반영
- **간섭 인식 탐욕 파일럿 할당**: 예측된 채널 진화를 기반으로 파일럿 배정을 사전 조정

## 주요 결과

- 랜덤 및 반응적(reactive) 파일럿 할당 기준선 대비 성능 우위
- 헝가리안 알고리즘 기반 간섭 인식 벤치마크와 유사한 SINR 성능 달성
- 5%-likely SINR 지표에서 유의미한 개선

## 의의

5G/6G 지상 기지국 없이 UAV 단독으로 CF-mMIMO 셀을 구성하는 시나리오에서, 파일럿 오염을 예측적으로 억제하는 경량 알고리즘을 제시한다. 드론 군집 통신 및 임무 운용에서 스펙트럼 효율을 높이는 실용적 접근이다.

## 관련 페이지

다중 UAV 통신 아키텍처 전반은 [[unet-multi-uav-networking]]를, 드론 데이터링크·RF 기반 통신 기술은 [[datalink-communication]]을 참조한다.
