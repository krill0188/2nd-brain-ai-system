---
title: "input-output feedback linearization"
created: 2026-10-24
updated: 2026-10-24
type: entity
tags: [control-theory, flight-control, multi-uav, optimization-based-control]
sources: []
confidence: medium
contested: false
contradictions: []
domain: flight-control
---

# input-output feedback linearization

Input-output feedback linearization is a nonlinear control technique that transforms a complex nonlinear system into a simple linear system through a feedback transformation of the input and output variables. In the context of multi-UAV payload systems, this method enables the realization of temporal waypoint navigation under temporal specifications by simplifying the system dynamics.

## 개요

원래 시스템이 갖는 상대도에 따라 입력-출력 선형화를 통해 비선형 체계에서 선형 체계와 동일한 동작을 수행하게 한다. 다중 UAV 페이로드 시스템과 같이 상대도가 두인 복잡한 비선형 시스템을 제어하기 쉽도록 선형화하는 전처리 기법으로 활용된다. 본 기법은 이후 최적화 기반 제어법이 동작할 수 있는 단순화된 수학적 모델을 제공하는 역할을 한다.

## 활용처

- [x] Multi-UAV payload system temporal waypoint navigation using barrier functions
  - 본 문서에서 입력-출력 피드백 선형화를 통해 상대도 2인 비선형 시스템을 단순화하고, Signal Temporal Logic (STL) 하에서 시간적 웨이포인트 항법 목표를 달성하기 위한 최적화 기반 제어법의 기초로 활용됨.

## 출처

- (사용자 재확인 필요) Rao, Nishanth; Sundaram, Suresh; Jagtap, Pushpak. (2022). "Temporal Waypoint Navigation of Multi-UAV Payload System using Barrier Functions." arXiv:2211.14261. http://arxiv.org/abs/2211.14261v1

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
