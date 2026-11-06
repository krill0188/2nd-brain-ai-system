---
title: "베지어 곡선 기반 UAV 충돌회피 경로 최적화와 IG-Net 초기값 생성"
created: 2026-11-04
updated: 2026-11-04
type: concept
domain: flight-control
tags: [drone, drone-sw, drone-ai]
sources: [inbox/processed/fetch-2026-11-04-kci-베지어-곡선-기반-uav-충돌회피-경로-최적화를-위한-학습-기반-초기값-생성-기법.md]
confidence: low
contested: false
contradictions: []
---

# 베지어 곡선 기반 UAV 충돌회피 경로 최적화와 IG-Net 초기값 생성

김진영(아주대), 한국항공우주학회지(2026). 5차 베지어 곡선으로 경로를 매개화하고, 최적화의 초기값을 학습 모델 **IG-Net**이 예측한다.^[inbox/processed/fetch-2026-11-04-kci-베지어-곡선-기반-uav-충돌회피-경로-최적화를-위한-학습-기반-초기값-생성-기법.md]

## 방법
- 다중 초기값 기반 최적화로 얻은 고품질 최적해를 지도학습 데이터로 사용한다.
- IG-Net은 경로 최적화에 유리한 초기값을 한 번에 예측해, 다중 시작 최적화의 비용을 대체한다.

## 결과 (몬테카를로 수치 시뮬레이션)
- 단일 초기값 최적화보다 경로가 짧고 충돌 횟수가 적다.
- 다중 초기값 최적화보다 계산시간이 훨씬 짧으면서 경쟁력 있는 경로 품질을 보인다.
- 수치 정량값은 초록에 없고, 실기체 검증은 언급되지 않았다.

## 관련
- [[hermes-evolutionary-uav-path-planning]] — 진화 기반 UAV 경로계획.
- [[collision-detection]] — 충돌 탐지/회피 개념.

## 📰 최근 관련 소식
- 베지어 곡선 기반 UAV 충돌회피 경로 최적화를 위한 학습 기반 초기값 생성 기법 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003401170
