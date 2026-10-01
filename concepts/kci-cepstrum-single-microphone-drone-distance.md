---
title: "켑스트럼을 이용한 단일 마이크로폰 기반 드론 거리 추정 (KCI)"
created: 2026-10-01
updated: 2026-10-01
type: concept
domain: hardware
tags: [drone, drone-hw]
sources: [inbox/processed/fetch-2026-10-01-kci-켑스트럼을-이용한-단일-마이크로폰-기반-드론-거리-추정.md]
confidence: medium
contested: false
contradictions: []
---

# 켑스트럼을 이용한 단일 마이크로폰 기반 드론 거리 추정

한양대학교(ERICA캠퍼스) 양원준(한국음향학회지, 2026)의 연구. 음원 위치 추정에는 일반적으로
다수 센서로 구성된 마이크로폰 배열이 쓰이지만, 설치 공간·운용 조건상 배열 구성이 제한될 때
단일 마이크로폰만으로 드론 거리를 추정하는 기법을 제안한다.^[inbox/processed/fetch-2026-10-01-kci-켑스트럼을-이용한-단일-마이크로폰-기반-드론-거리-추정.md]
원문은 페이월로 비공개이며 초록만 확보됨.

## 원리

- 드론은 비행 중 연속적인 광대역 소음을 방사하며, 직접파와 지면반사파가 함께 수신되면 두
  전달경로의 도달시간차(Time Difference of Arrival, TDOA)에 의해 주파수 영역에서 주기적인
  간섭구조가 형성된다.
- 켑스트럼(Cepstrum)으로 이 간섭구조에 포함된 TDOA 정보를 추출.
- 드론 비행 고도를 기지(known) 값으로 가정하고, 추출한 TDOA와 직접파·지면반사파의 기하학적
  관계를 이용해 드론의 수평거리를 추정(단일 TDOA만으로는 고도·거리 동시 추정이 어려움).

## 검증

- 일정 고도를 유지하며 거리를 변화시킨 드론 비행 실험에서 측정한 소음에 기법을 적용.
- 추정 거리와 GPS 거리를 비교해 단일 마이크로폰 기반 드론 거리 추정의 적용 가능성을 확인.

## Related

- [[monava]] — 스웨덴-핀란드 수동 음향 탐지 기반 C-UAS 기업
- [[kci-drone-detection-cfar-feature-postprocessing]] — 낮은 SCR 환경 드론 레이더 탐지 후처리 기법
- [[drone-fluxgate-magnetometer-crossline-correction]] — 단일 센서 기반 드론 탑재 계측 보정 기법(유사 방법론 계열)
