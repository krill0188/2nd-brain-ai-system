---
title: "Electromagnetic Neural Network for DOA Estimation"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, comms-protocol, ai-autonomy, beamforming, antenna]
sources: [inbox/fetch-2026-07-30-arxiv-electromagnetic-neural-network-for-direction-of-arrival-esti.md]
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
---

# Electromagnetic Neural Network for DOA Estimation

UAV 통신 시스템의 빔포밍을 위한 전자기 신경망(EMNN) 기반 도달 각도(DOA) 추정. 진폭 관측만으로 각도 스펙트럼을 생성하는 저전력 고속 처리 아키텍처.

## 시스템 구성

### 1. Stacked Intelligent Metasurfaces (SIM)
- UAV에 장착된 다층 메타표면
- 각 메타원자가 전자기 도메인에서 신호 처리
- 저에넥지 소비 및 초고속 연산

### 2. 완전 연결 계층
- 수신된 진폭 신호 처리
- EMNN의 비선형 추출 및 표현 능력 향상

## 계층적 DOA 추정 프레임워크

| 단계 | 기능 | 목표 |
|------|------|------|
| 1단계 | Coarse DOA 추정 | 대략적 각도 범위 |
| 2단계 | Fine DOA 추정 | 고해상도 정밀 각도 |

## 성능 개선

- **분류 오류 감소**: 기존 CBF 대비 약 13 dB 개선
- **듀얼 신호 시나리오**: 복수 신호 환경에서 우수한 성능
- **비용 효율성**: 낮은 하드웨어 비용 및 RF 전력 소비

## 응용 분야

- UAV 간 통신 빔포밍
- 방향성 안테나 제어
- 간섭 회피 및 신호 품질 향상

## 관련 페이지

- [[stacked-intelligent-metasurfaces]] — SIM 기반 UAV 통신
- [[datalink-communication]] — 드론 데이터링크 통신 기술
- [[drone-ai-agents]] — AI 기반 자율 시스템
