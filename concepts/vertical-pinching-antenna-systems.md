---
title: "Vertical Pinching Antenna Systems (V-PAS) for UAV Communications"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, comms-protocol, antenna, pas, uav, urban]
sources: [inbox/fetch-2026-07-30-arxiv-vertical-pinching-antenna-systems-v-pas-aided-uav-communicat.md]
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
---

# Vertical Pinching Antenna Systems (V-PAS) for UAV Communications

도시 건물 외벽을 따라 배치된 핀칭 안테나(PA)를 활용한 초저고도 UAV 통신을 위한 수직 핀칭 안테나 시스템(V-PAS). 2D 커버리지에서 3D 공역으로 확장된 안테나 시스템.

## 기존 PAS의 한계

- **수평 핀칭 안테나 시스템(H-PAS)**: 지상 사용자용으로 설계
- **2D 커버리지 제한**: 초저고도 UAV 통신에 부적합

## V-PAS 아키텍처

### 핵심 구성요소
- **도파관**: 건물 전체 높이를 따라 연속 배치
- **핀칭 안테나(PA)**: 안정적인 시선(LoS) 링크 보장
- **3D 공역 커버리지**: 2D 평면에서 3D 공역으로 확장

## Pinching Multiplicative Path Loss (PMPL)

### 정의
도파관 및 자유 공간 경로 손실의 캐스케이드 승적 감쇄를 특성화하는 지표:

```
PMPL = L_waveguide × L_free-space
```

### 특성
- **수직 거리에 대한 비민감성**: 건물 높이에 적응적
- **성능 안정성**: 다양한 UAV 운용 고도에서 일관된 성능

## 성능 분석

### 정확한 폐형식 도출
- 손실 도파관 조건 하에서의 정전 확률
- 에르고딕 속도(Ergodic Rate)

### 최적성 발견
- 접근점(AP) 높이 중점에 대한 대칭성
- 시스템 성능의 최적성 증명

## 성능 비교

| 시나리오 | V-PAS 성능 |
|----------|------------|
| 대부분의 초저고도 UAV 통신 | 기준 대비 우수 |
| 극도로 높은 전송 전력 및 큰 운용 영역 | 손실 도파관 시 정전 확률 열세 가능 |
| 손실 없는 도파관 | 모든 시나리오에서 이론적 상한 성능 |

## 관련 페이지

- [[stacked-intelligent-metasurfaces]] — SIM 기반 UAV 통신
- [[emnn-doa-estimation]] — EMNN 기반 DOA 추정
- [[datalink-communication]] — 드론 데이터링크 통신 기술
