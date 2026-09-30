---
title: "Bio-Inspired Offloading Algorithms in a UAV-Assisted IoV Network with MEC"
created: 2026-09-29
updated: 2026-09-30
type: concept
domain: comms-protocol
tags: [drone, drone-ai, datalink]
sources:
  - inbox/processed/fetch-2026-09-29-kci-bio-inspired-offloading-algorithms-in-a-uav-assisted-iov-net.md
  - raw/papers/_unclassified/bio-inspired-offloading-algorithms-in-a-uav-assisted-iov-network-with-mobile-edg.md
confidence: low
contested: false
contradictions: []
---

# Bio-Inspired Offloading Algorithms in a UAV-Assisted IoV Network with MEC

UAV가 보조하는 Internet of Vehicles(IoV) 네트워크에서 Mobile Edge Computing(MEC) 기반
계산 오프로딩 알고리즘의 성능을 이종 교통 조건별로 평가한 한국 KCI 논문(원광대 Chae Woo NAM,
저널 "인공지능연구", 2026).^[inbox/processed/fetch-2026-09-29-kci-bio-inspired-offloading-algorithms-in-a-uav-assisted-iov-net.md]

## 연구 설계

- **도로 토폴로지 3종**: 신호교차로(T1), 다차로 고속도로(T2), 혼합 도심 회랑(T3) — 실제
  차량 환경에서 시공간적으로 변하는 연산 수요를 반영하기 위한 모델.
- **방향성 차로 인지 혼잡 지수 ρ(t)**: 기존의 밀도 기반 상태 모델링에 신호 페이즈 타이밍과
  차로 단위 차량 밀도를 결합해 확장한 지표.
- **제안 알고리즘**: Congestion-Aware Bio-Inspired Greedy Algorithm(CA-BIGA)과 심층강화학습
  (Deep Reinforcement Learning) 기반 접근을 함께 제시(원문 초록이 DRL 설명 부분에서
  절단되어 세부 비교 결과는 확인 불가).

## 드론 분야 의의

UAV를 IoV(차량 사물인터넷)의 이동형 MEC 노드로 활용해 신호교차로·고속도로·도심 혼합로 등
이종 교통 조건에서 오프로딩 성능을 다르게 최적화한다는 접근은, 교통 모니터링용 UAV 태스크
오프로딩([[uav-task-offloading-traffic-monitoring]])과 같은 축의 연구이나 이 논문은
생체모방(bio-inspired) greedy 알고리즘과 DRL을 결합한다는 점에서 구별된다.

## 한계

- 원문이 페이월로 비공개이며, 수집된 초록이 CA-BIGA 이후 DRL 알고리즘 설명 문장 중간에서
  잘려 있어 정량적 성능 비교 결과를 확인할 수 없다. confidence를 `low`로 표기한다.
- 2026-09-30 Zotero 재인제스트본(raw/papers)도 동일하게 절단된 초록만 확보해, 한계가
  해소되지 않았음을 재확인했다.^[raw/papers/_unclassified/bio-inspired-offloading-algorithms-in-a-uav-assisted-iov-network-with-mobile-edg.md]

## 관련 개념

- [[uav-task-offloading-traffic-monitoring]] — UAV 기반 교통 모니터링 태스크 오프로딩 연구
- [[datalink-communication]] — 드론 데이터링크 및 무선 통신
- [[drone-ai-agents]] — 자율 의사결정, 강화학습 기반 드론 에이전트
