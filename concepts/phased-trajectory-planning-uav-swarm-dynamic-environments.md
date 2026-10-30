---
title: "복잡 동적 환경 UAV 군집의 단계적 궤적 계획 (GA + 가변 스텝 희소 A*)"
created: 2026-10-28
updated: 2026-10-28
type: concept
domain: ai-autonomy
tags: [drone, swarm]
sources: [inbox/processed/fetch-2026-10-28-kci-phased-trajectory-planning-for-uav-swarm-cooperation-in-comp.md]
confidence: low
contested: false
contradictions: []
---

# 단계적 궤적 계획 (Zhou, IJASS 2026)

UAV 군집 협업 궤적을 전역 계획과 온라인 국부 재계획의 두 단계로 나눈다. 원문 비공개, 초록(일부 잘림) 기준.^[inbox/processed/fetch-2026-10-28-kci-phased-trajectory-planning-for-uav-swarm-cooperation-in-comp.md]

- **전역 계획**: 궤적 길이와 매끄러움을 목적으로 하는 다목적 모델에 개선 유전 알고리즘을 적용. 중복 waypoint 삭제 연산자와 방향성 선택법을 포함한다.
- **국부 재계획**: 3D 탐색을 2D 경로 탐색과 고도 계획으로 분리하는 계층 전략, 개선된 가변 스텝 희소 A*로 3D 탐색 복잡도를 낮춘다.
- 수집본이 여기서 끝나 시뮬레이션 결과는 확인되지 않는다.

## 관련 문서
[[swarm-flight]], [[formation-flight]], [[path-planning]]
