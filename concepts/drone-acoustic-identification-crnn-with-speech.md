---
title: "음성 혼재 야외 드론 음향 데이터의 CRNN 기종 식별 성능 분석"
created: 2026-11-03
updated: 2026-11-03
type: concept
domain: ai-autonomy
tags: [drone-ai, drone]
sources: [inbox/processed/fetch-2026-11-03-kci-야외-환경에서-음성과-함께-수집된-드론-음향-데이터-세트에-대한-crnn-기반-식별기-성능-분석.md]
confidence: low
contested: false
contradictions: []
---

# 음성 혼재 야외 드론 음향 데이터의 CRNN 기종 식별 성능 분석

김근환(세종대, 한국산업정보학회논문지, 2026) 논문 초록 기준 요약이다. 원문은 비공개라 본문은 확인하지 않았다.^[inbox/processed/fetch-2026-11-03-kci-야외-환경에서-음성과-함께-수집된-드론-음향-데이터-세트에-대한-crnn-기반-식별기-성능-분석.md]

## 배경
레이더·광학·RF 방식은 소형 드론 식별에 한계와 환경 제약(시야, 기상)이 있어 음향 감시가 보완책으로 주목받는다.

## 방법
야외에서 음성과 함께 수집·공개된 드론 음향 데이터 세트에 전처리를 적용하고 CNN, RNN, FDY-CRNN(Frequency Dynamic CRNN), PFD-CRNN(Partial Frequency Dynamic CRNN)을 학습·평가해 드론 **기종 식별** 성능을 비교했다.

## 결과
음성이 포함된 시험 데이터 기준으로 본 데이터·실험 조건에서는 **CRNN 계열의 우위가 CNN, RNN 대비 뚜렷하지 않았다.** 일반화는 초록만으로 판단할 수 없다.

## 관련 문서
다중 모달 드론 탐지는 [[wave-detr-multimodal-drone-detector]], 대드론 탐지는 [[uav-detr-anti-drone-detection]], 일반 비전은 [[computer-vision-drone]]을 참조한다.

## 📰 최근 관련 소식
- 야외 환경에서 음성과 함께 수집된 드론 음향 데이터 세트에 대한 CRNN 기반 식별기 성능 분석 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003399857
