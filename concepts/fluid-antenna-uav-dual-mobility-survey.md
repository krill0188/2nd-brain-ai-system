---
title: "Fluid Antenna 기반 UAV 통신: 이중 이동성 관점의 개관"
created: 2026-10-28
updated: 2026-10-28
type: concept
domain: comms-protocol
tags: [drone, datalink]
sources: [raw/papers/datalink/fluid-antennas-enabled-uav-communication-systems-fundamentals-challenges-and-fut.md]
confidence: low
contested: false
contradictions: []
---

# Fluid Antenna 기반 UAV 통신 (Liu 외, arXiv 2610.35047)

저고도 무선망(LAWN)의 UAV 통신은 대규모 전파 환경 변화와 빠른 국부 채널 변동에 모두 적응해야 한다. 초록 기준으로 정리한다.^[raw/papers/datalink/fluid-antennas-enabled-uav-communication-systems-fundamentals-challenges-and-fut.md]

- **이중 이동성**: UAV 궤적 계획이 거시 이동성(공대지 기하 적응), 소형 개구 내 Fluid Antenna(FA) 위치 재구성이 미시 이동성(국부 채널 적응)을 담당한다.
- **과제**: 이동성·에너지·하드웨어·보안 제약 아래 UAV 궤적, FA 위치, 빔포밍을 함께 최적화할 때의 계산 복잡도와 정보 불확실성.
- **제안**: 환경 지도·사용자 이동 패턴·통계적 CSI로 장기 계획을 세우고 순시 CSI·UAV 상태로 빠르게 보정하는 하이브리드 오프라인-온라인 최적화 프레임워크. FA 기반 UAV 차량 통신 사례 연구로 효과를 보였다(구체 수치는 초록에 없음).
- **향후 방향**: ISAC, 보안 통신, MEC, 공중 중계.

## 관련 문서
[[fluid-antenna-system]], [[ris-assisted-clustered-uav-noma-bilevel-optimization]], [[uav-base-station-charging-station-placement-return-constraint]]
