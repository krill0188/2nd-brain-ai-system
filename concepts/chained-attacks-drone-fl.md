---
title: "Chained Attacks on Drone-Based Federated Learning"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, ai-autonomy, swarm, security, federated-learning]
sources: [inbox/fetch-2026-07-30-arxiv-chained-attacks-on-drone-based-federated-learning-from-netwo.md]
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Chained Attacks on Drone-Based Federated Learning

드론 기반 연합학습(Federated Learning, FL) 시스템에 대한 체인 공격 연구. 네트워크 계층의 DoS 공격과 자격 증명 기반 사칭을 결합한 공격 체인을 분석한다.

## 개요

Edge Intelligence(EI)는 드론 스웜과 같은 미션 크리티컬 무인 플랫폼에 협업적 모델 학습을 가능하게 하는 변혁적 모델이다. 그러나 FL 배포의 보안은 네트워크 가용성과 강력한 클라이언트 인증 메커니즘 모두에 의존한다.

## 공격 벡터

### 1. 네트워크 계층 DoS 공격
- **802.11 deauthentication 공격**: 합법적인 드론을 오프라인으로 강제 종료
- 무선 연결 중단을 통한 가용성 저해

### 2. 자격 증명 기반 사칭
- 연결 해제된 드론의 추출된 자격 증명을 사용한 사칭
- 단일 요소 인증이 연결 해제 후 사칭을 허용함

## 영향 분석

| 조건 | 영향 |
|------|------|
| IID 데이터 분포 | 상대적으로 안정적인 학습 |
| Non-IID 데이터 분포 | 상당한 학습 불안정성 |
| 단기 무선 중단 | 장기적인 학습 품질 저하로 확대 |

## 실험 검증

- **프레임워크**: Flower 프레임워크
- **테스트베드**: Raspberry Pi 및 Jetson 장비
- **데이터 분포**: IID 및 Non-IID 조건 모두 테스트

## 시사점

미션 크리티컬 드론 배포에서 가용성과 인증 취약점을 동시에 해결하는 방어 방향 필요:
- 다중 요소 인증(MFA) 도입
- 무선 연결 복원 메커니즘 강화
- 비정상 노드 탐지 및 격리

## 관련 페이지

- [[federated-lightweight-intrusion-detection]] — 지식 증류를 활용한 FL 기반 IDS
- [[swarm-coordination]] — 스웜 협업 및 보안
- [[drone-ai-agents]] — 자율 에이전트 아키텍처

## 📰 최근 관련 소식
- 명지대 ‘드론봇·대드론 센터’ 출범... 산학군 협력 안보 네트워크 강화 (보안뉴스, Fri, 07 Au) — https://news.google.com/rss/articles/CBMiXkFVX3lxTE5XdUZ2TnIwaktzN3F0dFBmXzZ6UFBqbC1hcFFHS3AxZUYzSmFkNl9IQ1RYQ0VxZlpGX3JRZjJqMzNvbXlLLUNhLV92dk4xaHpUb0xUQWlNVF9oR2xReGc?oc=5
- Michigan Drone Lawsuit Challenges Restrictions on Flights Near Police Operations (dronelife.com, Wed, 12 Au) — https://dronelife.com/2026/08/12/michigan-drone-lawsuit-state-law/
