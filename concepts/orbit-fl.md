---
title: "Orbit-Fl"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [federated-learning, continual-learning, multi-uav, environmental-monitoring, swarm-intelligence]
sources: ["https://doi.org/10.1016/j.future.2026.108775"]
confidence: medium
contradictions: []
domain: ai-autonomy
contested: false
---

# Orbit-Fl

Orbit-Fl는 다체 UAV 환경 감시를 위해 설계된 장면 인식 및 예산 적응형 연방 지속 학습 프레임워크이다.

본 논문에서 제안한 Orbit-FL은 다체 무인기 시스템에서 환경 감시 작업을 수행하는 가운데, 각 UAV가 현지 환경 상황을 인식하고 학습 예산을 효율적으로 배분함으로써 연방 학습과 지속 학습의 장점을 결합한 것이 특징이다. 이는 UAV들이 중앙 서버에 의존하지 않고도 서로의 지식 습득을 공유하면서도, 변화하는 환경에 적응할 수 있게 한다.

## 개요

Orbit-FL은 다체(UAV) 환경 감시 시나리오에서 연방 지속 학습(Federated Continual Learning)의 문제를 해결하기 위해 제안된 프레임워크이다. 기존의 연방 학습은 IID 데이터 가정 하에 설계되었으나, 실제 UAV 운영 환경에서는 데이터가 분산되어 있고 시간이 지남에 따라 변화하는 Non-IID 특성을 보인다. Orbit-FL은 이러한 한계를 극복하기 위해 각 UAV가 현재 환경을 인식(Scene-aware)하고, 연산 및 통신 자원 제약 내에서의 학습 예산을 적절히 조정(Budget-adaptive)하는 메커니즘을 도입하였다. 이를 통해 UAV 군집은 새로운 작업을 학습하면서 기존 지식을 보존하고, 중앙 집중식 데이터 모음 없이도 협업 지능을 향상시킬 수 있다.

## 핵심 파라미터

| 파라미터 | 내용 |
|---|---|
| Learning Type | Federated Continual Learning (연방 지속 학습) |
| Target Domain | Multi-UAV Environmental Monitoring (다체 UAV 환경 감시) |
| Key Feature | Scene-aware & Budget-adaptive (장면 인식 및 예산 적응형) |
| Data Assumption | Non-IID (Non-Independent and Identically Distributed) |

## 활용처

- **다체 UAV 환경 감시**: 광역 지역의 환경 데이터(예: 대기 질, 산불 감시, 수질 모니터링)를 실시간으로 수집 및 분석하기 위한 군집 지능 구축
- **연방 인공지능**: 통신 인프라가 제한적이거나 지연이 발생하는 분산 환경에서 UAV 간 지식 공유 및 모델 업데이트
- **지속 학습 시나리오**: UAV가 임무 수행 중 점진적으로 변화하는 환경 조건에 적응하면서 catastrophic forgetting(재앙적 망각) 문제 해결

## 관련 페이지

- [[Federated Learning]] — Orbit-Fl가 구현하는 학습 패러다임
- [[Continual Learning]] — Orbit-Fl가 지원하는 학습 기법
- [[Multi-Uav]] — Orbit-Fl가 적용되는 대상 시스템

## 출처

- (사용자 재확인 필요) original paper: "ORBIT-FL: Scene-aware and budget-adaptive federated continual learning for multi-UAV environmental monitoring", Zhao et al., 2027, DOI: 10.1016/j.future.2026.108775

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
