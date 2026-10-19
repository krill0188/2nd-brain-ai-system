---
title: "Lyapunov 유도 확산 RL 기반 UAV 지원 차량 네트워크 (D3PG)"
created: 2026-10-18
updated: 2026-10-18
type: concept
domain: comms-protocol
tags: [drone, datalink, drone-ai]
sources: [inbox/processed/fetch-2026-10-18-arxiv-a-lyapunov-guided-diffusion-based-reinforcement-learning-app.md]
confidence: medium
contested: false
contradictions: []
---

# Lyapunov 유도 확산 RL (UAV-V2X)

**출처**: arXiv 2507.20524 (2025-07-28), Zhang Liu 외 (Dusit Niyato, Xuemin Shen 포함). 초록 기준.

저고도 UAV가 차량 통신(V2X)을 지원할 때 자원·궤적의 동적 최적화, 제한된 체공 시간, 불완전한 채널 상태 정보(CSI)가 문제가 된다.^[inbox/processed/fetch-2026-10-18-arxiv-a-lyapunov-guided-diffusion-based-reinforcement-learning-app.md]

- **문제**: 채널 할당, 전력 제어, 비행 고도 조정을 함께 최적화한다. CSI 피드백 지연을 반영하며, UAV 장기 에너지 제약 하에서 차량-UAV 합 전송률을 최대화한다.
- **방법**: Lyapunov 최적화로 장기 문제를 슬롯별 결정론적 하위 문제로 분해하고, 확산 모델을 결합한 D3PG(diffusion-based deep deterministic policy gradient)로 결정을 내린다.
- **결과**: 실제 차량 이동 궤적을 쓴 시뮬레이션에서 기존 벤치마크보다 우수하다고 보고한다(구체 수치는 초록에 없음).

관련: [[datalink-communication]], [[uav-3d-spectrum-sensing-rem]], [[multirotor-energy-power-models]].
