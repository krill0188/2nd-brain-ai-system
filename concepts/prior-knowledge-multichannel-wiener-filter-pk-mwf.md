---
title: "prior knowledge multichannel Wiener filter (PK-MWF)"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [speech-enhancement, uav, microphone-array, noise-reduction, wireless-comms]
sources: []
confidence: medium
contradictions: []
domain: comms-protocol
contested: false
---

# prior knowledge multichannel Wiener filter (PK-MWF)

The prior knowledge multichannel Wiener filter (PK-MWF) is a speech enhancement filtering method that incorporates ego-noise reference signals—captured by microphones positioned near the UAV's propellers—to estimate the speech correlation matrix and improve speech intelligibility in drone-borne acoustic environments.

## 개요

드론(무인기) 내장 마이크로폰 어레이를 이용한 음성 증강 기술입니다. 프롭엘러(Propeller) 근처에 위치한 마이크로부터 ego-noise reference signals를 추출하여, 표준 Multichannel Wiener Filter (MWF) 대비 음성 상관 행렬 추정 정확도와 STOI, PESQ 지표를 향상시킵니다. 본 방법은 논문에서 UAV mounted on a stand in a semi-anechoic chamber에서 다양한 프로펠러 회전 속도(3단계) 조건 하에 실험 평가를 수행했습니다.

## 핵심 원리

- **ego-noise reference signals**: 프롭엘러 진동 및 공기역학적 소음을 포착하는 근접 마이크로부터 수신
- **speech correlation matrix estimate**: PK-MWF를 통해 추정되며, 음성 활동 검출(Speech Presence Probability, SPP)에 활용 가능
- **performance benchmark**: 외부 마이크(화자 인근) 혹은 내장 마이크에서 SPP를 추정하여 성능 평가 가능

## 실험 조건 및 결과

- **환경**: 반향음을 최소화한 세미 이코초크 챔버(Semi-anechoic chamber)
- **구성**: UAV를 스탠드에 고정, loudspeaker로 speech signal 재생
- **변수**: 3개의 고정된 프로펠러 회전 속도에 따른 다른 SNR 조건 생성
- **비교**: PK-MWF vs. 표준 MWF (프롭 마이크 포함/미포함 변형)와 성능 비교
- **지표**: STOI 및 PESQ 점수에서 개선 효과 검증됨 (원문에 구체적 수치 명시되지 않음, 재확인 필요)

## 관련 페이지

- [[multichannel Wiener filter (MWF)]] — 표준 MWF와 대비되는 본 알고리즘의 기준점이 되는 필터
- [[speech enhancement]] — 드론 환경에서 적용되는 더 광범위한 기술군
- [[speech presence probability (SPP)]] — 본 필터가 활용하는 음성 검출 지표

## 출처

- (사용자 재확인 필요) — 원문(full text)확인이 필요한 부분: 실험 결과의 구체적 수치 및 통계적 유의성Details are based on the abstract and relationship graph only. Full paper text should be reviewed to verify quantitative results and underlying assumptions.

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
