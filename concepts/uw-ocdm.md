---
title: "UW-OCDM"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [communication, waveform, isac, uwocdm, cooperative-sensing]
sources: []
confidence: medium
contradictions: []
domain: comms-protocol
contested: false
---

# UW-OCDM

통합 센싱과 통신(ISAC) 시스템에서 저고도 UAV 환경에 맞게 개발된 특수 통신 파형( waveform )입니다. 기존 직교 직교 카시미어 분할 멀티플렉싱(Orthogonal Chirp Division Multiplexing, OCDM)에 고유 단어(Uniqueness Word, UW)를 내장하여, 별도의 동기화 시퀀스 없이 타이밍 동기화와 도플러 추정·보상을 수행하고, 분산된 기지국이 페이로드 기호를 교환하지 않고 협력 센싱이 가능하도록 설계된 것이 특징입니다.

## 개요

본 문서에서 제안하는 UW-OCDM은 저고도 UAV 경제에서 통합 센싱과 통신(ISAC)의 핵심 enabling 기술이 되기 위해 고안되었습니다. 핵심 아이디어는 OCDM 변조 방식 내부에 고유 워드(Unique Word)를 주입하는 것이며, 이를 통해 수신 측은 별도의 동기화 시퀀스 없이도 타이밍 동기화와 도플러 효과 추정·보상을 수행할 수 있습니다. 또한, sparse spatio-temporal channel estimation 방법을 활용하여 다중 수신 안테나 간의 공통 채널 서포트를 활용해 신뢰성 높은 데이터 디모듈레이션을 지원하며, 센싱 측면에서는 결정론적인 UW를 공유 전제로 하여 분산된 기지국이 실시간으로 임의 페이로드 기호를 교환하지 않고 로컬에서 센싱 딕셔너리를 구축할 수 있게 합니다. 저자들에 의해 계층형 다중 목표 탐지·추적 알고리즘이 제안되었으며, 직접 경로 간섭 억제, kinematic prediction, multi-candidate 스크리닝, off-grid 보정, 잔류 검증, successive interference cancellation 등을 통합하여 robust한 국지화 및 추적을 가능하게 합니다.

## 핵심 파라미터

- 기반 변조 방식: Orthogonal Chirp Division Multiplexing (OCDM)
- 핵심 기능: Unique Word (UW) 내장
- 지원 기능: Timing Synchronization, Doppler Estimation, Doppler Compensation
- 대상 시나리오: High-mobility UAV scenarios
- 연계 기술: Integrated Sensing and Communications (ISAC)

## 활용처

- 저고도 UAV 통신 환경에서의 ISAC 시스템
- 고이동성 UAV 시나리오를 위한 타이밍·도플러 동기화
- 분산된 기지국을 활용한 협력 센싱 구축
- robust한 다중 목표 탐지·추적 알고리즘 구현

## 관련 페이지

- [[OCDM]] — UW-OCDM의 기반이 되는 원본 변조 방식
- [[ISAC]] — UW-OCDM이 적용되는 통합 센싱과 통신 기술 체계

## 출처

- (사용자 재확인 필요) Tao, Yi; Gao, Zhen; Wan, Ziwei; Lv, Yuezu; Wang, Hua; Huang, Kaibin; Chen, Sheng. "UW-OCDM for Low-Altitude UAV Communication and Cooperative Sensing." arXiv preprint arXiv:2608.21050 (2026).

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
