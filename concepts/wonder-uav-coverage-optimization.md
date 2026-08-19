---
title: "WONDER: Radio World Model-based Negotiation for UAV Coverage"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, swarm, ai-agent, world-model, coverage]
sources: [inbox/fetch-2026-08-19-arxiv-wonder-a-radio-world-model-based-negotiation-framework-for-m.md]
confidence: high
contested: false
contradictions: []
domain: comms-protocol
---

# WONDER: 라디오 월드 모델 기반 UAV 커버리지 최적화

## 개요

재난 후 지상 인프라 복구를 위한 JEPA 기반 라디오 월드 모델 협상 프레임워크.

## 문제 정의

### 도전 과제
- 지역 기하 관측의 한계
- 숨겨진 라디오 영향
- UAV 간 통신 제한
- 지역적 움직임 선택과 스웜 수준 결과 간 간극

## WONDER 프레임워크

### JEPA 기반 라디오 월드 모델
- 미래 라디오 필드 예측 학습
- 배치 가능한 정보에서 각 후보 궤적의 증분 라디오 효과 예측

### 다중 라운드 협상
- 순위별 제안 조정
- 한 번에 하나의 궤적 확정
- 업데이트된 컨텍스트에서 나머지 제안 재평가

### PPO 스타일 Actor
- 월드 모델과 액터 번갈아 업데이트

## RadioDynamics 시뮬레이션

- 62개 대도시 장면의 광선 추적 필드
- UAV 이동성, 라디오 전파, UAV 간 통신 통합

## 성능

- 11개 테스트 장면에서 최고 균형 점수 0.870
- STACCA 대비 0.162 커버리지 우위
- 100% UAV 간 연결성 유지

## 관련 개념

- [[swarm-coordination]] — 군집 협업
- [[digital-twin-intent-drone-networks]] — 디지털 트윈 드론 네트워크
- [[skyjepa-world-models]] — JEPA 스타일 세계 모델

## 참고

Jiahao Huang et al., arXiv:2608.16955 (2026)
