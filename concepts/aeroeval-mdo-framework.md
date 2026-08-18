---
title: AeroEval MDO Framework
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone-hw, drone, optimization, simulation, hardware]
sources: [raw/papers/drone-hw/fetch-2026-08-19-arxiv-multi-domain-physics-based-mdo-of-multirotor-uavs-a-determin.md]
confidence: high
contested: false
contradictions: []
---

# AeroEval MDO Framework

AeroEval은 멀티로터 UAV 설계를 위한 물리 기반 다학문 설계 최적화(MDO) 엔진이다. 구조 역학, 전기화학, 공기역학, 운동학을 아우르는 비선형 방정식 시스템을 동시에 해결하여 COTS(상용 부품) 크기를 최적화한다.

## 핵심 특징

- **Mass Snowball 방지**: 순차적 해석이 아닌 동시 해석으로 하위 모델 오차의 누적 전파를 방지
- **COTS 매핑**: 연속적 최적해를 실제 구매 가능한 상용 부품으로 매핑
- **엄격한 검증**: 20개 DIY/레거시 플랫폼으로 보정 후 19개 상용 드론(377g~76kg)에서 블라인드 평가

## 성능 지표

| 지표 | 값 |
|------|-----|
| MTOW 예측 MAPE | 7.2% (상용 테스트 코호트) |
| 복잡도 계수 k | 1.05 ± 0.08 |
| RMSE_MTOW | 1.59 kg |
| 배터리 질량 예측 | 7.9% (단일 팩 플랫폼) |
| 수렴 반복 횟수 | 25-50회 |
| 계산 시간 | <50ms (표준 데스크톱 CPU) |

## 응용 사례

- **농업/배달 역할**: 경로 의존적 질량 감소 모델로 구조 프레임 질량 최대 40.6% 감소, 에너지 용량 33.7% 감소
- **속도 한계**: 25.5 m/s 이상에서 전진 속도가 3차 기생 전력 증가로 발산

## 관련 개념

- [[drone-hw]] — 드론 하드웨어 도메인 개요
- [[flight-controller-hardware]] — 비행 제어기 하드웨어
- [[drone-power-battery]] — 드론 전력 및 배터리 시스템
