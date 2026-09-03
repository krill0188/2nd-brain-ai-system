---
title: "레이더 반사 면적을 고려한 델타형 무인항공기 날개 형상 최적화"
created: 2026-09-03
updated: 2026-09-03
type: concept
domain: hardware
tags: [drone-hw, hardware, drone]
sources: []
confidence: medium
contested: false
contradictions: []
---

# 레이더 반사 면적을 고려한 델타형 무인항공기 날개 형상 최적화

**저자**: 임동균 (청주대학교)  
**학술지**: 한국기계항공기술학회지  
**발행연도**: 2026  
**링크**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003370838  
**원문공개**: 공개

## 연구 개요

저관측성(low-observable) cranked-lambda 델타익 UAV에 대한 오픈소스 공력-스텔스 설계 탐색 프레임워크 제시. 내측 및 외측 전연(leading edge) 후퇴각을 설계 변수로, 평균 RCS(레이더 반사 면적) 상한을 제약 조건으로 설정.

## 사용 도구 및 방법론

| 도구 | 역할 |
|------|------|
| **OpenVSP + VSPAERO** | 받음각(AoA) 범위에서 양항비(L/D) 평가 |
| **PyPOFacets** | 다방향 관측에서 평균 RCS 추정(전자기 산란 해석) |
| **통합 자동화 워크플로우** | 단일 지오메트리 정의 공유, 목적 함수/제약 조건 집계 → 수동 파일 변환 오류 감소 |
| **다목적 최적화** | 공력 성능과 스텔스 성능의 균형점 탐색 |

## 의의

오픈소스 도구만으로 공력-스텔스 통합 최적화를 구현한 프레임워크라는 점에서, 방산/정찰용 UAV 초기 설계 단계에 활용 가능성이 높다. RCS를 제약으로 두고 공력 성능을 최대화하는 접근은 저관측 고정익 UAV 플랫폼 개발에 실용적이다.

## 관련 페이지

드론 하드웨어 설계 전반은 [[drone-hw]]를 참조하고, 고정익 및 VTOL 비행 제어기 관련 파라미터는 [[flight-controller-hardware]]에서 확인할 수 있다.
