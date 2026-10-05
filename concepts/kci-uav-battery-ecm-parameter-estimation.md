---
title: "소형 UAV 리튬이온 배터리 ECM 파라미터 추정 (KCI)"
created: 2026-10-05
updated: 2026-10-05
type: concept
domain: hardware
tags: [drone, drone-hw, research]
sources: [raw/papers/_unclassified/소형-무인항공기용-리튬이온-배터리-등가회로모델-파라미터-추정에-관한-연구.md]
confidence: low
contested: false
contradictions: []
---

# 소형 UAV 리튬이온 배터리 ECM 파라미터 추정

김진희(국방과학연구소)가 항공우주시스템공학회지(2026)에 발표. 원문 비공개, 초록만 확인했다.
^[raw/papers/_unclassified/소형-무인항공기용-리튬이온-배터리-등가회로모델-파라미터-추정에-관한-연구.md]

- 전제: 등가회로모델(ECM)의 정확도는 평형전위와 총 내부저항 파라미터의 정확도에 직접 의존한다.
- 방법: 가우스과정 회귀로 평형전위·내부저항 대리모델을 구성.
- 결과(저자 주장): 대리모델이 엔트로피 계수·활성화에너지 같은 전기화학적 특성을 반영하는 물리적 충실도를 가지며,
  30~50 V 단자전압 검증 데이터에서 평균절대오차 약 0.3 V, MAPE 1% 미만.

비행 중 잔여 에너지 예측의 기반이 되는 모델이다(해석). 같은 날 수집된 복귀 가능 판단 논문과 연결된다.

## 관련 개념

- [[drone-power-battery]] — 드론 전원·배터리 일반
- [[kci-fixed-wing-return-feasibility-logic]] — 전압 예측 기반 복귀 판단
- [[uav-battery-replacement-planner]] — 배터리 운용 계획
