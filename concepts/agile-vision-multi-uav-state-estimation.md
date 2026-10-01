---
title: "Towards Agile Vision-Based Multi-UAV Flight: Revisiting State Estimation"
created: 2026-10-01
updated: 2026-10-01
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, swarm]
sources: [inbox/processed/fetch-2026-10-01-yt-towards-agile-vision-based-multi-uav-flight-revisiting-state.md]
confidence: low
contested: false
contradictions: []
---

# Towards Agile Vision-Based Multi-UAV Flight: Revisiting State Estimation

체코 프라하 FEE-CTU Multi-robot Systems Group의 연구. 민첩한 다중 UAV(Multi-UAV) 비행에서
충돌 회피·기동 협응을 위해 인접 UAV의 운동 상태(Kinematic State)를 온보드에서 정확하고 저지연으로
추정하는 pose-aware 상태 추정 기법을 다룬다.^[inbox/processed/fetch-2026-10-01-yt-towards-agile-vision-based-multi-uav-flight-revisiting-state.md]

## 핵심 문제의식

- **기존 비전 기반 접근의 한계**: 대부분의 비전 기반 방법은 위치(Position)만 측정하고, 속도·가속도는
  변위(displacement)로부터 간접 추정 — 이 방식이 오차를 유발한다고 지적.
- **제안 방향**: pose-aware 상태 추정으로 인접 기체의 운동 상태를 더 정확히 직접 추정.
- 논문·코드·데이터: `mrs.fel.cvut.cz/agile-uav-estimation` (원문 확인 필요, 영상 설명 텍스트
  도중 절단으로 구체 수치 미확보 — confidence low 유지).

## Related

- [[swarm-coordination]] — Leader-Follower, 편대 비행 등 다중 드론 협응 구조
- [[high-speed-drone-tracking]] — 고속 추적 드론 기술
- [[visual-positioning-odometry]] — Visual/Visual-Inertial Odometry 기반 위치 추정
