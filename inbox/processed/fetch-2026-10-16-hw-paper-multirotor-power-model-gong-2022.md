---
title: "Modelling Power Consumptions for Multi-rotor UAVs"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://arxiv.org/abs/2209.04128
authors: "Hao Gong, Baoqi Huang, Bing Jia, Hansu Dai"
published: "2022-09-09"
tags: [drone, hardware, paper, power-model, energy, forward-flight, vertical-flight, DJI-M210]
---

# Modelling Power Consumptions for Multi-rotor UAVs

## 핵심 내용 (방법·결과)

멀티로터 UAV의 전진 비행, 수직 상승, 수직 하강 세 가지 비행 모드에 대한 **폐쇄형(closed-form) 전력 소비 모델**을 유도하고, 이를 결합한 일반 3D 비행 전력 소비 모델을 제안했다. 기존 연구는 고정익·단일 로터 또는 휴리스틱 멀티로터 모델에 그쳤으나, 이 논문은 엄밀한 수학적 유도에 기반한다.

**핵심 결과:**
- 단일 로터와 멀티 로터 전력 소비의 관계로부터 각 비행 모드 모델 유도.
- DJI M210 + DJI Mobile SDK로 실세계 비행 실험에서 모델 정확성·유효성 확인.
- 로터 수 변화에 따른 전력 소비 시뮬레이션 제공.
- 호버링 시(v=0) 최적 속도 전진 비행 대비 전력이 더 높음을 확인.

## 설계에 쓸 수 있는 지침

- **임무 설계 시 호버링 최소화** → 최적 전진 속도에서 비행하는 것이 에너지 효율적.
- 로터 수 결정 시 이 모델을 이용해 전력 예산(power budget)을 사전 시뮬레이션 가능.
- DJI M210 실증 데이터로 검증된 모델이므로 유사 급 기체(4~6로터, 3~5kg급) 설계에 즉시 적용 가능.
- 배터리 용량 산정 시: E = P_model × t 형태로 미션 프로파일에 적용.

## 한계·미확인 항목

- 고속 비행(>15 m/s) 또는 강풍 조건에서의 정확도: 미확인.
- 로터 간 공기역학적 간섭 효과 포함 여부: 미확인.
- 모터 및 ESC 변환 효율 손실 포함 여부: 미확인 (본문 확인 필요).
