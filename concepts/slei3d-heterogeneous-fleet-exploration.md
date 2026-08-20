---
title: "SLEI3D: Simultaneous Exploration and Inspection via Heterogeneous Fleets"
created: 2026-08-20
updated: 2026-08-20
type: concept
tags: [drone-sw, gcs-software, swarm, exploration, inspection]
sources: [raw/papers/drone-sw/slei3d-heterogeneous-fleet-exploration.md]
confidence: high
contested: false
contradictions: []
domain: gcs-software
---

# SLEI3D: Simultaneous Exploration and Inspection via Heterogeneous Fleets

제한된 통신 환경에서 이종 로봇 군집을 활용한 동시 탐사-검사 프레임워크. 장거리 라이다(탐사)와 근거리 카메라(상세 검사)를 갖춘 UAV/UGV 협업.

## 핵심 기능

- **협력적 3D 탐사**: 미지 환경 실시간 탐사
- **적응적 검사**: 관심 영역 동식별 및 상세 검사
- **간헐적/주도적 통신**: 이동 GCS에 보고

## 계획 메커니즘

- **다층 다중 속도 계획**: 로봇 간/내 서브그룹 조율
- **불확실성 처리**: 특징 수/위치 불확실성 고려

## 검증

- **시뮬레이션**: 최대 48대 로봇, 384,000m³ 규모
- **하드웨어**: 7대 로봇 실험

## 관련 개념

- [[swarm-coordination]] — 군집 조율 및 편대 비행
- [[recon-swarm-project]] — 지능형 자율 군집정찰드론
- [[gnss-denied-remote-autonomy-sar]] — GNSS 차단 환경 자율 수색

## 출처

Junfeng Chen et al., "SLEI3D: Simultaneous Exploration and Inspection via Heterogeneous Fleets under Limited Communication", arXiv:2601.00163, 2026. ^[raw/papers/drone-sw/slei3d-heterogeneous-fleet-exploration.md]
