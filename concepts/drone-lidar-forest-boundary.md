---
title: "드론 라이다를 이용한 임야 현황경계 추출 및 분석"
created: 2026-08-19
updated: 2026-10-05
type: concept
tags: [drone, ops-mission, lidar, mapping, survey]
sources: [inbox/fetch-2026-08-19-kci-드론-라이다를-이용한-임야-현황경계-추출-및-분석.md, raw/papers/_unclassified/건설현장-드론-포인트클라우드와-bim-간의-convex-hull-기반-자동-정합-방안.md]
confidence: high
contested: false
contradictions: []
domain: ops-mission
---

# 드론 라이다 임야 현황경계 추출

## 개요

드론 라이다를 이용해 취득한 포인트클라우드, DTM, 정사영상 등의 자료를 활용하여 임야 현황경계를 추출하고 지적측량에 적용 가능성을 검증한 연구.

## 방법론

1. 실험지역 선정
2. 드론 라이다 관측 수행
3. 수목 제거된 DTM 생성
4. 포인트클라우드 단면 분석
5. 정사영상 판독을 통한 경계 추출

## 정확도 검증 결과

| 지표 | RMSE |
|------|------|
| X좌표 | ±1.138m |
| Y좌표 | ±1.162m |
| 연결오차 | ±1.627m |

## 결론

현행 법률에서 규정하는 임야지역(1/6,000) 경계결정의 오차 허용범위 이내의 성과로, 지적측량에 적용 가능함.

## 관련 개념

- [[rtk-gps-precise-landing]] — RTK GPS 차등 측위
- [[visual-positioning-odometry]] — GPS 미가용 환경 위치 추정
- [[dji-terra]] — DJI 매핑 소프트웨어

## 관련 페이지

- [[kci-watershed-individual-tree-delineation-uav-lidar-chm]] — UAV LiDAR CHM Watershed 개체목 분할 최적 조건(2026 KCI)
- [[kci-drone-pointcloud-bim-registration-extraction]] — 드론 점군을 기준 모델(BIM)에 정합하는 접근; 임야·건설 현장의 점군 활용 대비^[raw/papers/_unclassified/건설현장-드론-포인트클라우드와-bim-간의-convex-hull-기반-자동-정합-방안.md]

## 참고

청주대학교 박수범, 한국지적학회지 (2026)

## 📰 최근 관련 소식
- 드론 라이다를 이용한 임야 현황경계 추출 및 분석 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003368639
- 남원시, 드론 공공서비스 실증 본격화 (klan.kr, Wed, 19 Au) — https://news.google.com/rss/articles/CBMiQEFVX3lxTE5KeUgyZXNWdFQtMWtHWDFRSk13UjFiQzNiNjlvWGVKZ1Ytb0pkYmZvWWVSeW5XbXhyWFVuSllOTUU?oc=5
