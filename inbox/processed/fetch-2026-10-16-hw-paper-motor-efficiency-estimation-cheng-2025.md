---
title: "Data-Driven Estimation of Quadrotor Motor Efficiency via Residual Minimization"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://arxiv.org/abs/2510.11388
tags: [drone, hardware, propulsion, motor, efficiency, estimation, arxiv]
authors: Sheng-Wen Cheng, Teng-Hu Cheng
published: 2025-10-13 (v1), 2026-03-06 (v2) — arXiv eess.SY
---

# 쿼드로터 모터 효율 데이터 기반 추정 (Cheng & Cheng, 2025)

## 핵심 내용
- 비행 중 데이터로 쿼드로터 모터 효율을 온라인 추정하는 방법을 제안한다.
- 슬라이딩 윈도우 배치 방식의 잔차(residual) 최소화를 쓰고, IRLS와 primal-dual 내점법으로 푼다.
- 모터 열화(degradation) 시나리오에서 시뮬레이션으로 검증했다. 초록은 EKF 기준선보다 모터 클리핑 구간에서 스파이크가 작다고 정성적으로 밝힌다.

## 설계에 쓸 수 있는 지침
- 추진계 설계 단계에서 모터 효율을 가정값이 아니라 운용 중 추정·모니터링 대상으로 두는 발상을 참고할 수 있다.
- 모터 클리핑(포화)이 추정 오차를 키운다는 점은 ESC·모터 용량 여유 설계 시 고려할 항목이다.

## 한계·미확인
- 시뮬레이션만 수행했다. 실기 모터·프로펠러 데이터는 확인되지 않았다.
- 효율 수치, 오차 값, 샘플 수는 초록에 없어 미확인.
- 추진계 선정(어떤 모터·프로펠러를 고를지)을 다루지 않고 운용 중 효율 추정을 다룬다. 선정 근거 자료로는 간접적이다.
- 2025년 프리프린트라 동료 심사 여부 미확인.
