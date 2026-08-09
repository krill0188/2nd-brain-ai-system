---
title: "UAV ISAC via Cross-Region Cooperation"
created: 2026-07-31
updated: 2026-08-10
type: concept
tags: [drone, comms-protocol, swarm, datalink]
sources: []
confidence: medium
contested: false
contradictions: []
note: "Raw source not preserved in repo — found during 2026-08-10 provenance audit, needs recapture"
---

# UAV ISAC via Cross-Region Cooperation

공중-지상 통합 감지 및 통신(ISAC)을 위한 UAV 스워밍. 교차 지역 협력 프레임워크.

## Key Challenges

1. 동적이고 불균형한 지상 통신 수요
2. 센싱을 위한 관찰 다양성 제한

## Technical Approach

- **서비스 중심 지역 분할**: 트래픽 인식 UAV 통신 지원
- **적응형 핸드셰이킹**: 제어된 동기화 오버헤드로 영역 간 잔여 위상 오류 완화
- **MAPPO 프레임워크**: CTDE(Centralized Training, Decentralized Execution) 기반 영역 수준 다중 에이전트 PPO

## Results

- 통신 QoS 약 90% 달성
- Cramér-Rao bound (CRB) 약 45% 감소

## References

- [[swarm-coordination]]
- [[datalink-communication]]
- [[mavlink-protocol]]
