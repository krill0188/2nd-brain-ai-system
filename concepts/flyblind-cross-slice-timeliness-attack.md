---
title: "FlyBlind: 5G 슬라이스 간 적시성 공격(Silent State Staleness)"
created: 2026-09-19
updated: 2026-09-24
type: concept
domain: comms-protocol
tags: [drone, datalink]
sources: [raw/papers/datalink/flyblind-cross-slice-timeliness-attacks-on-uav-situational-awareness-over-5g.md, inbox/processed/fetch-2026-09-19-arxiv-flyblind-cross-slice-timeliness-attacks-on-uav-situational-a.md]
confidence: medium
contested: false
contradictions: []
---

# FlyBlind: 5G 슬라이스 간 적시성 공격

5G Standalone(SA) 망 위에서 BVLOS UAS가 C2와 영상 피드백을 **공유 User Plane**으로 함께 전송할 때,
같은 망의 인접 슬라이스에 있는 **인가된 co-tenant**가 GCS의 상태 정보를 "낡게" 만들 수 있음을 보인
Sonaglio 등(2026-08-27, arXiv 2608.27604)의 연구다.^[inbox/processed/fetch-2026-09-19-arxiv-flyblind-cross-slice-timeliness-attacks-on-uav-situational-a.md]

## 공격 개요

- 공격자는 rogue gNB나 C2 트래픽 직접 간섭 없이, 합법적인 업링크 수요만 유지한다.
- 슬라이스 간 격리가 **soft isolation**일 때 유휴 자원 공유가 업링크 grant 경쟁으로 이어지고, 이것이
  GCS 측 상태 노후화(state aging)로 나타난다.
- 이 효과를 **Silent State Staleness**로 정의하고, 반증 가능한 "false-healthy" 술어로 형식화했다.

## 실측 결과 (전용 테스트베드)

| 지표 | 결과 |
| --- | --- |
| GCS 텔레메트리 age | 약 12초에서 포화 |
| GCS 추정 위치 vs 실제 위치 | 수십 m 오차 |
| 편도 지연(OWD) p99 | 수십 ms 수준 유지 |
| 가용성 | 99.9% 초과 |
| 기체 상태 | GUIDED 모드 유지, failsafe 미발동 |

## 시사점

- 지연·가용성 같은 전통적 링크 헬스 지표는 이 공격을 탐지하지 못한다.
- 업링크 강제가 비대칭인 배치에서는 링크 상태가 아니라 **목적지에서의 상태 신선도 검증**(예: 텔레메트리
  타임스탬프 age 감시)이 필수라는 것이 논문의 결론이다.
- GCS/failsafe 설계 관점에서는 "연결됨 = 정상"이라는 가정을 버리고 데이터 age 기반 경보를 추가해야 한다.

## 관련 페이지

- [[cross-layer-attacks-uav-5g]] — 같은 5G 기반 C2 경로의 크로스 레이어 공격 분석(사용자 평면 경합으로 인한 적시성 저하 포함).
- [[fcc-drone-cellular-c2-testing]] — 드론 셀룰러 C2 전국 테스트 승인, 셀룰러 C2 확산 배경.
- [[datalink-communication]] — 드론 데이터링크 통신 개요.
