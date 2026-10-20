---
title: "UAV 탐색팀 결함 허용 동적 임무 할당 (Nasir·AlDurgam, 2024)"
created: 2026-10-20
updated: 2026-10-20
type: concept
domain: ai-autonomy
tags: [drone, swarm, ai-agent]
sources: [inbox/processed/fetch-2026-10-20-arxiv-fault-tolerant-dynamic-task-assignment-for-uav-based-search-.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 탐색팀 결함 허용 동적 임무 할당

**출처**: arXiv 2408.10564 (2024-08-20), 초록 기준.

협업 탐색에서 센서·액추에이터 고장 후 UAV의 잔여 능력을 임무 할당에 반영하는 프레임워크다. 배터리 잔량으로 목표까지의 도달 범위를 평가해 할당하며, 수리·재충전·확률적 목표 재발생을 모델에 포함한다. 확률적 동적계획법으로 최적 할당 정책을 오프라인에서 구하고 온라인에서 빠르게 적용한다. 상위 임무 규칙과 하위 제어 능력을 잇는 점이 특징이고, 고장·배터리 변동 환경의 시뮬레이션 사례로 견고성을 보였다.^[inbox/processed/fetch-2026-10-20-arxiv-fault-tolerant-dynamic-task-assignment-for-uav-based-search-.md]

관련: [[kci-quadrotor-compound-fault-accommodation]], [[kci-llm-cbba-swarm-task-allocation]], [[kci-uav-swarm-mission-reliability-abort]].
