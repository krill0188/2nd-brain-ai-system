---
title: "UAV-VLC 보조 WMN의 차단 인지 다차원 우선순위 대역 할당 (BMPO)"
created: 2026-10-08
updated: 2026-10-08
type: concept
domain: comms-protocol
tags: [drone, datalink, research]
sources: [inbox/processed/fetch-2026-10-08-kci-multi-dimensional-optimization-of-blocking-aware-resource-al.md]
confidence: low
contested: false
contradictions: []
---

# BMPO: UAV-VLC 보조 무선 메시 네트워크 대역 할당

Yan Zhao(Hainan Univ.)의 KSII Transactions on Internet and Information Systems(2026) 논문. 무선 메시 네트워크(WMN)는 다중 홉·동적 토폴로지·공유 채널 때문에
노드 밀도가 높거나 트래픽이 폭주할 때 자원 경쟁과 혼잡이 심하다. 이를 UAV-가시광통신(VLC) 보조 WMN에서 풀기 위한 **blocking-aware multi-dimensional priority optimization(BMPO)** 대역폭 할당 전략을 제안한다.
수집된 초록이 중간에서 잘려 결과·성능 수치는 확인하지 못했다(confidence low).^[inbox/processed/fetch-2026-10-08-kci-multi-dimensional-optimization-of-blocking-aware-resource-al.md]

## 3차원 노드 상태 인지 모델 (초록 기준)

- 실시간 채널 이용률
- 은닉 마르코프 모델(HMM) 기반 간섭 예측
- 큐잉 이론에서 도출한 확률적 혼잡 위험

## 관련 페이지

- [[unet-multi-uav-networking]] — 다중 UAV 통신·네트워킹 아키텍처
- [[datalink-communication]] — 드론 데이터링크 통신 기술
- [[csi-jamming-attack-detection-uav]] — UAV 네트워크 채널 상태 기반 재밍 탐지
