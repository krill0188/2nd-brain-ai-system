---
title: "SLEI3D - Simultaneous Exploration and Inspection via Heterogeneous Fleets"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-sw, gcs-software, swarm, exploration]
sources: [raw/papers/gcs-software/slei3d-heterogeneous-fleet.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# SLEI3D - Simultaneous Exploration and Inspection via Heterogeneous Fleets

제한된 통신 환경에서 이질적 로봇 군집을 활용한 동시 탐사 및 검사 프레임워크. 장거리 LiDAR(탐사)와 근거리 카메라(상세 검사)를 갖춘 다양한 로봇 협업.

## 문제 정의

- 미지 환경에서의 관심 영역 실시간 식별
- 제한된 통신 환경 (ad-hoc 무선 네트워크)
- 이동식 GCS에 실시간 보고

## 프레임워크 구성

### 1. 협업 3D 탐사
- 온라인 전략 통합
- 다층 다중 속도 계획 메커니즘

### 2. 적응적 검사
- 특징의 수와 위치에 대한 불확실성 고려
- 로봇 간/로봇 내 하위 그룹 계획

### 3. 적시 통신
- 간헐적(intermittent) 또는 선제적(proactive) 프로토콜
- 로컬 계획 조정을 위한 적극적 만남

## 검증

| 환경 | 규모 |
|------|------|
| 고충실도 시뮬레이션 | 최대 48대 로봇, 384,000 m³ |
| 하드웨어 실험 | 7대 로봇 |

## 관련 개념

- [[swarm-coordination]] — 군집 조정 및 편대 비행
- [[recon-swarm-project]] — 지능형 자율 군집정찰드론 프로젝트
- [[decentralized-swarm-gps-denied]] — GPS 차단 환경 분산형 UAV 군집

## 출처

- Chen et al., "SLEI3D: Simultaneous Exploration and Inspection via Heterogeneous Fleets under Limited Communication", arXiv:2601.00163, 2026.
- Project: https://junfengchen-robotics.github.io/SLEI3D/
