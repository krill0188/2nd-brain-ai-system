---
title: "UAV 초분광 영상 기반 보리 습해 조기 탐지"
created: 2026-09-06
updated: 2026-09-06
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, ai-autonomy]
sources: [raw/papers/_unclassified/무인기-기반-초분광-영상을-이용한-보리-습해-조기-탐지.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 초분광 영상 기반 보리 습해 조기 탐지

2026년 3월 19일 습해 처리 시작 이후 3월 21일~4월 3일까지 2일 간격 총 7회 취득한 UAV 초분광
영상으로 보리(맥류)의 습해 스트레스를 진단하는 머신러닝 분류 모델을 개발하고, 기존 SPAD 측정법
대비 조기 탐지 가능성을 비교한 연구다
^[raw/papers/_unclassified/무인기-기반-초분광-영상을-이용한-보리-습해-조기-탐지.md].

## 방법

- 과습구/적습구 파장별 보리 캐노피 반사율에 Two sample t-test를 적용해 Blue, Green, Red,
  Red-edge, NIR 대표 밴드를 선정.
- 대표 밴드로 산출한 식생지수를 5개→1개까지 단계적으로 축소하며 머신러닝 분류모델(KNN 등)을
  각각 개발·비교.

## 결과

- **전체 시계열 모델**: 식생지수 4개를 사용한 KNN이 오분류를 최소화하며 최적 모델로 선정됨.
- **시계열별 모델**: 습해 처리 초기(3월 21일)부터 어느 시점에 촬영하더라도 식생지수 2개만으로
  비교적 일정한 성능을 유지하는 KNN이 실용적으로 효과적임을 확인.
- 결론적으로 축소된 대표 파장 기반 소수 식생지수만으로도 UAV 초분광 영상을 통한 보리 습해의
  실용적 조기 탐지가 가능함을 시사.

## 관련 개념

- [[pine-wilt-disease-uav-detection]] — UAV 영상 기반 식생 이상(병해) 탐지 정확도 비교 연구
- [[kci-hyperspectral-litter-detection-unetpp]] — 동일 초분광 영상 활용 계열의 UAV 탐지 연구
- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용 전반

## 📰 최근 관련 소식
- [포착] ‘희귀한’ 북한 다연장로켓, 우크라 드론에 박살…“북한군 2000여명 사망” [영상] (나우뉴스, Sun, 13 Se) — https://news.google.com/rss/articles/CBMicEFVX3lxTFBqbzJoQmhqa2VpRzZnUWVPMGMxRzMycDIwX2FTbjF1SUFBMmo3VkRFMTZOcUtSTHJQMVFfWU40eXJxRXFWbXhnZ1pWSUR2Nk1lWkMyVzg5RWpvRGJyaDNxcTlTMmE0dXdvT0YzZEtVTlE?oc=5
