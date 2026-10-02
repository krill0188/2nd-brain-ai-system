---
title: "드론 이상 징후 탐지 방법 연구 동향 및 개선 방안"
created: 2026-08-19
updated: 2026-10-01
type: concept
tags: [drone, flight-control, safety, research, sensor]
sources:
  - inbox/fetch-2026-08-19-kci-드론-이상-징후-탐지-방법-연구-동향-및-개선-방안-연구.md
  - raw/papers/_unclassified/registration-free-visible-thermal-fusion-for-uav-detection.md
  - raw/papers/_unclassified/mdolf-framework-for-multi-target-detection-and-online-localization-of-ground-obj.md
  - raw/papers/_unclassified/aerodistinct-a-generative-data-construction-pipeline-and-benchmark-for-dronebird.md
  - raw/papers/_unclassified/seeing-what-darkness-conceals-frequency-adaptive-modeling-for-nighttime-uav-vehi.md
  - raw/papers/drone-ai/dynamic-multi-scale-mixture-of-experts-with-cross-scale-feature-enhancement-for-.md
  - raw/papers/_unclassified/감시-드론을-위한-심층-신경망-기반-지상-표적-추적-기법.md
confidence: high
contested: false
contradictions: []
domain: flight-control
---

# 드론 이상 징후 탐지 방법

## 개요

드론 활용 확대에 따라 비행 안전성 확보를 위한 이상 징후 탐지 기술의 중요성이 증대되고 있다.

## 탐지 방법 분류

### 1. 센서 기반 방법
- **원리**: 물리적 센서 신호 변화를 직접 분석
- **장점**: 실시간 탐지에 유리
- **한계**: 센서 노이즈, 외부 환경 변화, 단일 신호 판단의 한계

### 2. 상태 추정 기반 방법
- **원리**: 추정값과 측정값의 차이 활용
- **장점**: 시스템 수준의 이상 판단 가능
- **한계**: 모델 정확도와 파라미터 설정에 따른 성능 변화

### 3. 데이터 기반 방법
- **원리**: 비행 로그와 시계열 데이터 활용
- **장점**: 복잡한 이상 패턴 학습 가능
- **한계**: 데이터 품질과 운용 환경 변화에 따른 일반화 문제

## 융합적 발전 방향

- 센서 기반 + 상태 추정 기반 융합
- 센서 기반 + 데이터 기반 융합
- 상태 추정 기반 + 데이터 기반 융합
- 세 방법의 통합적 융합

## 최근 추가된 관련 탐지 연구 (2026-09-30, 서지정보만 확보 — 초록 미수집)

데이터 기반(센서 융합·딥러닝) 탐지 범주에 해당하는 최근 논문 5건이 Zotero로
인제스트됐다. 초록이 아직 확보되지 않아 제목 수준의 주제 분류만 기록한다:

- "Registration-free visible-thermal fusion for UAV detection" (Huang·Wang·Zou·Dang·Chi,
  2027)^[raw/papers/_unclassified/registration-free-visible-thermal-fusion-for-uav-detection.md] —
  정합(registration) 없는 가시광-열화상 센서 융합 UAV 탐지.
- "MDOLF: Framework for multi-target detection and online localization of ground
  objects based on aerial imagery in the vehicle-UAV collaboration scenario"
  (Zhou·Peng·Wu·Wang·Ma, 2027)^[raw/papers/_unclassified/mdolf-framework-for-multi-target-detection-and-online-localization-of-ground-obj.md] —
  차량-UAV 협업 시나리오의 다중표적 탐지·온라인 위치추정 프레임워크.
- "AeroDistinct: A generative data construction pipeline and benchmark for
  drone–bird discrimination in urban air mobility" (Lin·Zhan·Liang·Tan·Feng,
  2027)^[raw/papers/_unclassified/aerodistinct-a-generative-data-construction-pipeline-and-benchmark-for-dronebird.md] —
  도심 항공 모빌리티 환경의 드론-조류 판별용 생성 데이터 구축 파이프라인·벤치마크.
- "Seeing what darkness conceals: Frequency-adaptive modeling for nighttime UAV
  vehicle detection" (Du·Cheng·Yuan, 2027)^[raw/papers/_unclassified/seeing-what-darkness-conceals-frequency-adaptive-modeling-for-nighttime-uav-vehi.md] —
  야간 UAV 차량 탐지를 위한 주파수 적응형 모델링.
- "Dynamic multi-scale mixture-of-experts with cross-scale feature enhancement
  for UAV small object detection" (Li·Hou·Xiong·Ma·Liu,
  2027)^[raw/papers/drone-ai/dynamic-multi-scale-mixture-of-experts-with-cross-scale-feature-enhancement-for-.md] —
  UAV 소형 객체 탐지를 위한 동적 다중스케일 MoE·교차스케일 특징 강화.

이 5건 모두 "데이터 기반 방법" 범주(비행 로그가 아닌 영상·센서 데이터 기반)의
최신 사례로, 위 "융합적 발전 방향" 절의 센서+데이터 융합 흐름을 뒷받침하는
정성적 근거로 분류한다. 방법·수치 성능은 원문 확보 후 보강이 필요하다.

같은 범주(데이터 기반·영상 탐지)의 국내 연구로, RetinaNet 객체 탐지에 칼만 필터를 결합해
감시 드론의 지상 표적을 추적하는 기법이 있다. 신경망 단독 탐지 대비 칼만 필터 결합 시
표적 인식 정확도가 향상됨을 실험으로 확인했다
^[raw/papers/_unclassified/감시-드론을-위한-심층-신경망-기반-지상-표적-추적-기법.md].

## 관련 개념

- [[flight-logging-analysis]] — ULog 포맷 및 비행 데이터 분석
- [[sensor-calibration]] — 센서 캘리브레이션
- [[drone-safety-failsafe]] — RTL, Geofence 등 안전 시스템
- [[kci-ground-target-tracking-retinanet-kalman]] — RetinaNet+칼만필터 기반 감시 드론 지상 표적 추적(KCI)

## 참고

대진대학교 김남용, 한국융합과학회지 (2026)

## 📰 최근 관련 소식
- 드론 기반 객체 탐지 시스템에 대한 물리적 적대적 패치 공격: 디지털-물리 도메인 갭 분석 및 완화 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003368967
- 제주공항 위협하는 ‘불법 드론’…올해만 84건 탐지 (제민일보, Wed, 02 Se) — https://news.google.com/rss/articles/CBMiZkFVX3lxTE5VM2ExYjFzdlZHTUpONTZTTTVTeElmRHNiY2g4SW5xR1pMczhLYTAyeWNyMlJ6Z01hczFmVGlWVGRHRFg5UlFTWjc3ZjEyYTdaOXlyY3Ftdzg3RS0wTWtudGhXb2NrQQ?oc=5
- 송산동청소년지도협, 드론 교실 운영 (제민일보, Thu, 03 Se) — https://news.google.com/rss/articles/CBMiZkFVX3lxTE16SEswaXJhZlFfM1ktME50VVRrS25uOE1DRDVuNGRIVlVGZ0RlNG1mc0RVNGhtVmRqeFE2OEk3cTVnNlhwd1BCZ0ZRTTN3a2pwb0RLX0hWZUZnWmJVZlk0YVp3cllnZw?oc=5
- 러 제트 추진 드론 맹폭…우크라 전역서 최소 7명 사망·50명 이상 부상 (yna.co.kr, Tue, 29 Se) — https://news.google.com/rss/articles/CBMieEFVX3lxTE81YTdBTVN5am5BQmtONkhRa3JlaThXNlFORkRCTkpIZmJ3NEk1bThWY2tfeGlyLXRsblM2TVhFRHZVR1JGUnc2MVJBMXl3a3FLNjJYLUJ1LVVGbDNCWTFRbjE0dGd3WkpHd01CMG55dVJ4a1NyZ2lHTA?oc=5
- 영주시, 지적재조사 드론 자체 운용…연 8000만원 예산 절감 (kyongbuk.co.kr, Thu, 01 Oc) — https://news.google.com/rss/articles/CBMib0FVX3lxTE03WEU3bm0wc1lIaEN3M0lCTmQ3cTFiajl3WG52T1lPX1VKNFZCb1VYYkMyZXdLeVNFWVpOZmtCZi1uU2t1VjhyMFBaanpFWmlwSjcwa3d5OERmVUgwUmpVSlNXSndLRTROTzdYSmpKMA?oc=5
