---
title: "Federated Lightweight Intrusion Detection in Drone Swarms"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, ai-autonomy, swarm, security, federated-learning, intrusion-detection]
sources: [inbox/fetch-2026-07-30-arxiv-federated-lightweight-intrusion-detection-in-drone-swarms-wi.md]
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Federated Lightweight Intrusion Detection in Drone Swarms

지식 증류(Knowledge Distillation, KD)를 활용한 드론 스웜용 경량 연합학습(FL) 기반 침입 탐지 시스템(IDS). 리소스 제약 환경에서 효율성과 탐지 성능의 균형을 달성한다.

## 배경

드론 스웜은 감시, 재난 대응, 인프라 모니터링 등 중요한 애플리케이션에 배포되지만:
- 개방형 통신 채널에 의존
- 제한된 계산 리소스
- 다양한 사이버 위협에 취약

## 기존 방식의 한계

| 방식 | 한계 |
|------|------|
| 중앙집중식 ML | 모든 데이터 수집 필요, 프라이버시 문제 |
| 기존 FL | 통신 및 계산 오버헤드 |
| 리소스 제약 | 효율성과 탐지 성능 균형 어려움 |

## 제안 프레임워크

### 핵심 기술
- **Deep Neural Networks (DNN)**: 복잡한 패턴 학습
- **Knowledge Distillation (KD)**: 모델 복잡성 및 통신 비용 감소
- **Federated Learning**: 분산 학습 및 프라이버시 보존

### 성능 결과

| 지표 | 결과 |
|------|------|
| 탐지 정확도 | 약 98.6% |
| 통신 비용 감소 | 약 70% |
| 계산 오버헤드 감소 | 29% |

## 실험 환경

- **하드웨어**: Raspberry Pi 4
- **데이터셋**: 실제 드론 네트워크 데이터셋
- **평가**: 리소스 제약 조건에서의 실용성 검증

## 시사점

FL과 KD의 결합은 리소스 제약 드론 네트워크에서 안전하고 효율적인 배포를 위한 실용적이고 적합한 솔루션임을 입증한다.

## 관련 페이지

- [[chained-attacks-drone-fl]] — 드론 FL 체인 공격 분석
- [[swarm-coordination]] — 스웜 협업 및 보안
- [[drone-ai-agents]] — 자율 에이전트 아키텍처
