---
title: "대드론 하드킬 무인기의 교전영역 계산 알고리즘 개발"
created: 2026-09-03
updated: 2026-09-03
type: concept
domain: ops-mission
tags: [drone, ops-mission, drone-ai]
sources: []
confidence: medium
contested: false
contradictions: []
---

# 대드론 하드킬 무인기의 교전영역 계산 알고리즘 개발

**저자**: 안효득 (국방과학연구소 항공기술연구원)  
**학술지**: 한국항공우주학회지  
**발행연도**: 2026  
**링크**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003376575  
**원문공개**: 비공개 (페이월)

## 연구 개요

**교전영역(Engagement Zone)**: 요격 UAV가 침투하는 적 UAV를 성공적으로 요격하기 위해 적 드론이 진입해야 하는 공간 영역.

이동 표적(공중 정찰/타격 기동 드론)에 적용 가능한 교전영역 산출 알고리즘을 개발. 요격 UAV와 적 UAV의 상대 위치·속도·고도·비행 방위각을 매개변수로 6-DOF 다중 시뮬레이션을 수행한 후, **로지스틱 분류 + 다항 선형 회귀(CLARA 기법)**를 결합하여 실시간 시현이 가능한 함수를 도출.

## 핵심 기법

- **CLARA(Logistic-Polynomial Regression Combined Approach)**: 교전 경계면의 비선형 불연속성을 로지스틱 지시함수로 판별 → 교전영역 추정 정밀도 향상.
- 이동 표적 및 상대 방위각 조건에서 발생하는 경계면 불연속성 처리가 핵심 과제.

## 의의

방산 분야 C-UAS(Counter-UAS) 체계 설계에서 실시간 교전영역 시현은 전술적 의사결정 속도를 높이는 핵심 요소다. 로지스틱-다항 회귀 결합형 접근은 기존 룩업 테이블 방식 대비 연속 갱신이 가능하다.

## 관련 페이지

대드론 방어 체계의 개요는 [[drone-wall-defense-system]]을, 탐지·방어 통합 솔루션 기업 현황은 [[droneshield]]를 참조한다.
