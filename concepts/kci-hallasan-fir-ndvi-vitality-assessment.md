---
title: "드론 다중분광센서 기반 NDVI를 활용한 한라산 구상나무 개체의 고도·사면향별 활력도 예비평가"
created: 2026-09-08
updated: 2026-09-08
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, ai-autonomy]
sources: [raw/papers/_unclassified/드론-다중분광센서-기반-ndvi를-활용한-한라산-구상나무-개체의-고도사면향별-활력도-예비평가.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 다중분광센서 기반 NDVI를 활용한 한라산 구상나무 개체의 고도·사면향별 활력도 예비평가

한라산 구상나무의 생존·고사 여부만 보던 기존 평가를 보완해, 드론 다중분광 영상에서 추출한
개체별 NDVI로 활력도 변화를 정량 추적할 수 있는지 검토한 예비 연구다
^[raw/papers/_unclassified/드론-다중분광센서-기반-ndvi를-활용한-한라산-구상나무-개체의-고도사면향별-활력도-예비평가.md].

## 방법

- 한라산 동·서사면의 서로 다른 고도대(1,450–1,745m) 6개 조사구에서 드론(M300 RTK, 비행고도
  100m)과 MicaSense RedEdge-P 센서로 3cm급 정사 모자이크 및 NDVI 분포도를 구축.
- 2017년 구축된 구상나무 개체 위치자료를 활용해 수관 중심점 반경 30cm 내 NDVI를 개체값으로 산정.

## 결과

- 동사면에서는 고도가 높아질수록 NDVI 평균이 감소하고, 저활력 개체 비율과 NDVI 분포 폭이 증가.
- NDVI가 높은 조사구일수록 누적 고사율이 낮게 나타남 — NDVI와 고사 사이 관련성 시사.
- 서사면도 저고도 조사구가 고고도 조사구보다 NDVI 평균이 높고 분포 폭이 좁아 동일 경향 확인.
- NDVI<0.5를 예비 임계값으로 적용해 2017년 이후 추가 고사 가능 개체를 조사구별 0.75~6.58%
  범위에서 탐지.

## 관련 개념

- [[kci-barley-wet-stress-hyperspectral-detection]] — UAV 초분광 영상 기반 보리 습해 조기 탐지(동일
  식생지수 활용 계열)
- [[pine-wilt-disease-uav-detection]] — UAV 영상 기반 식생 이상(병해) 탐지 정확도 비교 연구
- [[computer-vision-drone]] — 드론 컴퓨터 비전 응용 전반
