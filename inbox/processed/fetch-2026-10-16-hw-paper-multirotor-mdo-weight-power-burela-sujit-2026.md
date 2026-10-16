---
title: "Multi-Domain Physics-Based MDO of Multirotor UAVs: A Deterministic Framework for Discrete COTS Sizing"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://arxiv.org/abs/2607.22768
tags: [drone, hardware, mass-budget, power-budget, sizing, mdo, cots]
authors: Akshay Gupta Burela, P. B. Sujit
published: 2026-07-24 (arXiv:2607.22768 v1, 프리프린트)
---

# 멀티로터 다영역 물리 기반 MDO: 이산 COTS 부품 선정 (Burela & Sujit, 2026)

## 핵심 내용
- 구조, 전기화학(배터리), 공력, 운동학 하위 모델을 동시에 풀어 멀티로터 크기를 정하고, 최적값을 상용 부품(COTS)에 매핑하는 엔진 AeroEval을 제시한다.
- 초록은 하위 모델 오차가 순차 계산에서 연쇄적으로 커져 질량 오차가 된다("Mass Snowball effect")고 지적한다.
- 상용 기체 19종 블라인드 테스트에서 MTOW 평균 절대 백분율 오차(MAPE) 7.2%, 배터리 질량은 단일 팩 기종에서 7.9% 이내로 보고됐다.
- 기체 질량·배터리 용량 축소를 함께 다루는 경로 의존 질량 모델은 농업·배송 역할에서 프레임 질량 최대 40.6%, 에너지 용량 33.7% 감소를 보고한다(초록 기준 비교 대상: 정적 기준선).

## 설계에 쓸 수 있는 지침
- 질량 예산과 전력 예산을 순차가 아니라 한 번에 맞추는 방식은 초기 제원 산정 체크리스트의 구조로 참고할 만하다.
- 상용 부품 매핑을 연속 최적값 뒤의 별도 단계로 두는 방식은 "이론값 → 실제 구매 가능 부품" 검증 절차에 그대로 쓸 수 있다.

## 한계·미확인
- 프리프린트이며 동료 심사 여부 미확인.
- 초록에 적힌 수치만 옮겼다. 방정식, 계수(complexity factor k의 산출법), 전력 예산 세부 값은 미확인.
- DIY 보정 코호트의 MAPE는 26.1%로 상용 코호트보다 크다. 자작 기체에 바로 적용하면 오차가 커질 수 있다.
