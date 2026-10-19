---
title: "드론 양자 자력계 기반 붕괴 건물 능동 자기 매핑"
created: 2026-10-18
updated: 2026-10-18
type: concept
domain: ops-mission
tags: [drone, ops-mission, drone-hw]
sources: [inbox/processed/fetch-2026-10-18-arxiv-from-rubble-simulation-to-active-magnetic-mapping-quantum-se.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 양자 자력계 재난 대응

**출처**: arXiv 2606.25957 (2026-06-24), Tovey 외. 초록 기준, 시뮬레이션 연구.

붕괴 후 72시간 내 생존자 위치 파악을 위해 기존 센서를 보완하는 수단으로 드론 탑재 양자 자력계를 제안하고 시뮬레이션 파이프라인을 구축했다.^[inbox/processed/fetch-2026-10-18-arxiv-from-rubble-simulation-to-active-magnetic-mapping-quantum-se.md]

- **시뮬레이션**: Unreal Engine으로 철근 콘크리트 주차장 붕괴를 생성하고 삼각형별 쌍극자 근사로 유도 자기장을 계산했다. 지붕선 위 약 1 m에서 sub-pT~sub-nT 범위의 자기 구조를 복원할 수 있음을 보였다.
- **능동 샘플링**: 희소한 다중 센서 샘플을 베이지안 능동 샘플링 기반 가우시안 프로세스 회귀 백엔드에 입력한다. 여러 독립 붕괴 사례에서 검증했고, 약 100개 샘플에서 구조 상관이 정점에 도달했다.
- **페이로드 절충**: 3센서 어레이가 기울기 해상도와 UAV 탑재 중량 제약 사이에서 최적이라고 보고한다.

실제 비행 시험 결과는 없다. 관련: [[kci-disaster-response-drone-tech-direction]], [[drone-fluxgate-magnetometer-crossline-correction]].
