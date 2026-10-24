---
title: "재난 후 이종 UAV 중계기의 동적 가동 대수 결정 (MPC)"
created: 2026-10-24
updated: 2026-10-24
type: concept
domain: comms-protocol
tags: [drone, datalink, ops-mission]
sources: [raw/papers/_unclassified/dynamic-active-fleet-sizing-of-heterogeneous-uav-relays-for-post-disaster-commun.md]
confidence: low
contested: false
contradictions: []
---

# 재난 후 이종 UAV 중계기의 동적 가동 대수 결정

Choi·Li, arXiv 2610.30323 (2026-10-21). **초록 기준**이다.

## 요지
- 문제: 허리케인·산불로 지상 통신망이 손상되면 UAV가 임시 연결을 제공하지만, 지상망이 복구되고 통신 수요가 변하면서 필요한 공중 지원량도 달라진다. 고정된 보유 기체 중 몇 대를 어떻게 가동할지 동적으로 조정하는 문제를 다룬다.^[raw/papers/_unclassified/dynamic-active-fleet-sizing-of-heterogeneous-uav-relays-for-post-disaster-commun.md]
- 방법: 모델 예측 제어(MPC) 프레임워크. 통신 수요, 지상망 복구, 이종 UAV 운용, 기체 에너지 가용량, 외부망으로 보낼 수 있는 트래픽을 제한하는 백홀 용량을 반영한다. 정식화는 볼록 2차 계획(QP)이라 온라인 결정이 가능하다.^[raw/papers/_unclassified/dynamic-active-fleet-sizing-of-heterogeneous-uav-relays-for-post-disaster-commun.md]
- 평가: FCC 보고서 기반 과거 재난 복구 사례 7건, 백홀 시나리오 4종, 민감도 분석. 복구 기간 중 필요한 가동 대수가 크게 변하고, 백홀 용량과 기체 구성이 통신 성능에 영향을 준다고 보고한다.^[raw/papers/_unclassified/dynamic-active-fleet-sizing-of-heterogeneous-uav-relays-for-post-disaster-commun.md]

## 관련
재난 대응 드론 기술 방향은 [[kci-disaster-response-drone-tech-direction]], 다중 UAV 통신망 구조는 [[unet-multi-uav-networking]], UAV 중계 6G 연구는 [[xai-uav-relay-6g-terahertz]] 참조.

## 한계
구체 수치(절감 대수, 처리량)는 초록에 없다. 사례는 과거 보고서 기반 시뮬레이션이다.
