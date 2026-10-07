---
title: "PSO 기반 UAV 산불 위험 관리 경로계획 (Natural Hazards Review)"
created: 2026-10-07
updated: 2026-10-07
type: concept
domain: ai-autonomy
tags: [drone, drone-ai, swarm, research]
sources: [raw/papers/swarm/a-novel-efficient-particle-swarm-optimization-algorithm-for-uav-applications-in-.md]
confidence: low
contested: false
contradictions: []
---

# PSO 기반 UAV 산불 위험 관리 경로계획

Natural Hazards Review(2027-02 발행 예정, Crossref 메타데이터)에 실린 논문. 호주 NSW 산불을 대상으로 UAV 보조
산불 탐지·예방 시스템을 개발한다. 초록이 중간에서 잘려 다른 알고리즘과의 비교 결과는 확인하지 못했다(confidence low).
^[raw/papers/swarm/a-novel-efficient-particle-swarm-optimization-algorithm-for-uav-applications-in-.md]

## 구성

- 실시간 데이터에 기반해 산불 영향 핵심 기반시설을 식별하는 **규칙 기반 검증 프레임워크**(메타휴리스틱 최적화 사용).
- 제한된 자원·에너지 제약 하에서 **UAV 피해지역 커버리지 최대화**.
- UAV 개체 수별 경로계획용 수리 최적화 모델을 구축·시험.

## 관련 개념

- [[drone-wildfire-detection-network-optimization]] — 산불 조기탐지 네트워크 배치·라우팅 최적화
- [[marl-uav-wildfire-exploration]] — 산불 대응 MARL 탐색
- [[thermal-drone-wildfire-monitoring]] — 열화상 드론 산불 감시
