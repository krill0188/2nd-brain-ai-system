---
title: "현수 페이로드 쿼드로터의 PSO 튜닝 하이브리드 다항식 궤적 계획"
created: 2026-10-28
updated: 2026-10-28
type: concept
domain: flight-control
tags: [drone, drone-sw]
sources: [inbox/processed/fetch-2026-10-28-kci-trajectory-planning-for-quadrotor-uav-with-suspended-payload.md]
confidence: low
contested: false
contradictions: []
---

# 현수 페이로드 쿼드로터의 궤적 계획 (Wang, IJASS 2026)

복잡한 3D 환경에서 페이로드를 매단 쿼드로터의 궤적은 매끄럽지 않고 추종 정확도가 낮으며 페이로드 흔들림이 커지기 쉽다는 문제를 다룬다. 원문 비공개, 초록(일부 잘림) 기준.^[inbox/processed/fetch-2026-10-28-kci-trajectory-planning-for-quadrotor-uav-with-suspended-payload.md]

## 파이프라인
1. 3D A*로 충돌 없는 초기 경로 생성
2. Douglas–Peucker로 경로를 단순화해 핵심 기준점 추출
3. jerk와 snap을 함께 최소화하는 하이브리드 최적화 함수 구성, 입자군집최적화(PSO)로 가중치를 적응 조정

## 비고
수집본 초록이 PSO 설명 도중 끝나 정량 결과는 확인되지 않는다.

## 관련 문서
[[autotrans-uav-suspended-payload-planning-control]], [[dual-uav-cable-suspended-payload-transport]], [[quadrotor]]
