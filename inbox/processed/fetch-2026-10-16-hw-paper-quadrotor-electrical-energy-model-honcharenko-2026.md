---
title: "An Analytical Model of Quadrotor Electrical Energy Consumption"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://doi.org/10.48084/etasr.15062
tags: [drone, hardware, battery, energy-model, esc]
authors: Vadym Honcharenko, Valentyn Yesilevskyi
published: 2026-04-04 (online), Engineering, Technology & Applied Science Research (ETASR), Vol. 16, No. 2, pp. 33302-33309
---

# 요약

제조사가 제공하는 부품 파라미터만으로 쿼드로터의 전기 에너지 소비를 추정하는 해석적 모델이다. 공력 모델과 분리되어 있어 다양한 시뮬레이션·제어 시스템에 붙여 쓸 수 있다고 초록에 기술되어 있다.

# 핵심 내용

- 2차 Thevenin 등가회로 배터리 모델, ESC 모델, 1차 모터 모델(비선형 전압 강하·부하 의존 효율 포함)을 결합.
- 입력은 로터 각속도와 토크뿐.
- 상수 전압 기준 모델 대비 최대 **21%** 에너지 감소를 보고(초록 기재).
- 공개된 벤치 측정의 모터 전류 곡선과 일치한다고 저자가 기술.

# 설계에 쓸 수 있는 지침

- 배터리 내부저항과 전압 강하를 반영해야 고부하(호버·급가속) 구간의 에너지 추정 오차가 줄어든다는 점을 설계 검토 체크리스트에 넣을 수 있다.
- 공력 모델 없이 제조사 사양만으로 시작할 수 있어, 초기 체공시간 견적 단계에 적합하다.

# 한계·미확인

- 시뮬레이션 설정, 사용한 배터리·모터 사양, 오차 지표(RMSE 등)는 초록 페이지에 없어 **미확인**.
- 본문 미열람. 21% 수치는 초록 기재값이며 비교 기준(상수 전압 베이스라인)의 조건은 **미확인**.
