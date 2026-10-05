---
title: "UAV-MEC 클러스터링 비교 및 PSO-ACO 멀티에이전트 태스크 오프로딩 (KCI 2026)"
created: 2026-10-04
updated: 2026-10-04
type: concept
domain: comms-protocol
tags: [drone, datalink, drone-ai]
sources: [raw/papers/_unclassified/comparison-of-clustering-algorithms-for-ground-and-hybrid-mobile-edge-computing-.md, raw/papers/swarm/multi-agent-based-qos-aware-task-offloading-in-single-cell-uav-mec-systems-using.md]
confidence: low
contested: false
contradictions: []
---

# UAV-MEC 클러스터링 비교 및 PSO-ACO 멀티에이전트 태스크 오프로딩 (KCI 2026)

두 KCI 논문 모두 원문 비공개이며 초록만 확인했다(결과 수치는 수집 초록에 없음, 일부는 중간 절단).

## 지상 MEC vs 하이브리드 항공-지상 MEC (남채우, 원광대)

- 새 클러스터링/오프로딩 알고리즘 제안이 아니라 동일한 클러스터형 UAV 네트워크 구조에서 두 시나리오를
  통제 비교한 구현 지향 연구다.^[raw/papers/_unclassified/comparison-of-clustering-algorithms-for-ground-and-hybrid-mobile-edge-computing-.md]
- 시나리오 A: UAV는 중계만 하고 계산은 지상 MEC. 시나리오 B(하이브리드): 항공 MEC 병용. 동기: 항공 MEC는
  통신 거리·서비스 유연성에서, 지상 MEC는 안정성·계산 용량에서 유리.

## 단일 셀 PSO-ACO 멀티에이전트 오프로딩 (이연우, 국립목포대)

- 각 UAV를 지능형 에이전트로 모델링해 로컬 실행 vs 서빙 엣지 노드 오프로딩과 자원 할당을 자율 결정한다.
  PSO(전역 탐색)와 ACO(후반 정밀 탐색)를 결합한 IPAA로 수렴 품질·강건성을 높이는 것이 목표.
  고려 요소는 지연, 에너지, 신뢰성, 마감시간 충족, 자원 등.^[raw/papers/swarm/multi-agent-based-qos-aware-task-offloading-in-single-cell-uav-mec-systems-using.md]

## 관련 개념

- [[bio-inspired-offloading-uav-iov-mec]] — 생체모방 UAV-MEC 오프로딩 선행 사례
- [[uav-task-offloading-traffic-monitoring]] — 교통 모니터링 UAV 태스크 오프로딩
- [[swarm-coordination]] — 다수 UAV 에이전트 협조 맥락
