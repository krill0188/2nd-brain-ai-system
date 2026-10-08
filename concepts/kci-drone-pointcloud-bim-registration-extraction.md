---
title: "드론 포인트클라우드–BIM 정합 및 구조부재 추출 (KCI 2건)"
created: 2026-10-05
updated: 2026-10-08
type: concept
domain: ops-mission
tags: [drone, ops-mission, research]
sources: [raw/papers/_unclassified/건설현장-드론-포인트클라우드와-bim-간의-convex-hull-기반-자동-정합-방안.md, raw/papers/_unclassified/bim-모델과의-정합을-통한-드론-기반-포인트클라우드에서-구조부재-추출-방안.md, inbox/processed/fetch-2026-10-08-kci-서로-다른-드론-촬영경로-기반-3dgs-모델의-공간-구성요소별-시각적-재현-품질-단일-대상지-탐색적-비교.md]
confidence: low
contested: false
contradictions: []
---

# 드론 포인트클라우드–BIM 정합 및 구조부재 추출

경상국립대 연구진의 KIBIM Magazine(2026) 논문 2건. 둘 다 원문은 비공개이고 수집된 초록이 문장 중간에서 끊겨 있어
수치 결과는 확인하지 못했다.

## Convex Hull 기반 자동 정합 (임현수)

- 문제: 현장 드론 포인트클라우드에는 가설물·비대상 물체가 섞이고, 외부 촬영이라 실내 데이터가 불완전해 전체 형상·국소
  특징 대응에 의존하는 기존 정합이 잘 맞지 않는다.
- 접근: 두 데이터에서 공통으로 식별 가능한 **최하층 바닥 경계**를 기준으로 삼아 Z축 정렬부터 순차 정합한다(이후 단계는 초록 절단).
  ^[raw/papers/_unclassified/건설현장-드론-포인트클라우드와-bim-간의-convex-hull-기반-자동-정합-방안.md]

## BIM 정합 기반 구조부재 추출 (곽민슬)

- 기존 추출 연구는 지상 LiDAR 중심이었으나 드론 사진측량은 대면적을 빠르게 비접촉 취득하는 대신 가림·촬영 방향·가설물·
  적치 자재·인접 부재의 영향을 받는다.
- 방법: 실제 RC 건설현장의 포인트클라우드를 IFC 기반 BIM과 정합하고, point-to-mesh 거리 필터링과 부재별 규칙 기반 처리로
  기둥·보·벽·슬래브를 추출. 수작업 Ground Truth와 대표 관심영역에서 성능 평가(지표·수치는 초록 절단).
  ^[raw/papers/_unclassified/bim-모델과의-정합을-통한-드론-기반-포인트클라우드에서-구조부재-추출-방안.md]

## 관계

두 논문은 "정합 → 부재 추출"로 이어지는 건설 진행 관리 파이프라인의 앞뒤 단계로 읽을 수 있다(해석).

## 관련 개념

- [[drone-lidar-forest-boundary]] — 드론 LiDAR/점군 처리 사례(산림)
- [[kci-uav-lidar-ground-point-density-dem-accuracy]] — 드론 점군 정확도 관련 KCI 연구
- [[uav-mining-digital-twin]] — 드론 기반 현장 디지털 트윈

## 최신 근거 연결 (2026-10-08)

- 같은 드론 촬영 데이터의 다른 재구성 방식(3DGS)에서 촬영경로별 품질 비교: [[kci-3dgs-flight-path-reconstruction-quality]]^[inbox/processed/fetch-2026-10-08-kci-서로-다른-드론-촬영경로-기반-3dgs-모델의-공간-구성요소별-시각적-재현-품질-단일-대상지-탐색적-비교.md]

## 📰 최근 관련 소식
- BIM 모델과의 정합을 통한 드론 기반 포인트클라우드에서 구조부재 추출 방안 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003390505
