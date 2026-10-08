---
title: "EO/IR 영상 기반 자율 드론 산불 초기 진화 기술 (KCI)"
created: 2026-10-08
updated: 2026-10-08
type: concept
domain: ops-mission
tags: [drone, drone-ai, ops-mission, research]
sources: [inbox/processed/fetch-2026-10-08-kci-eoir-영상-분석-기반-자율-드론을-활용한-산불-초기-진화-기술-연구.md]
confidence: low
contested: false
contradictions: []
---

# EO/IR 영상 기반 자율 드론 산불 초기 진화

이호준(경북대)의 한국항공우주학회지(2026) 논문. 기존 소방 드론이 수동 조종에 의존하고 감시 역할에 머문다는 한계를 넘기 위해, 자율 드론 탑재
EO/IR 센서로 산불 초기 진화까지 수행하는 기술을 제안한다. 원문은 비공개라 초록 단일 출처(confidence low)다.^[inbox/processed/fetch-2026-10-08-kci-eoir-영상-분석-기반-자율-드론을-활용한-산불-초기-진화-기술-연구.md]

## 제안 파이프라인

1. EO 영상에서 AI·컴퓨터비전으로 가장 의심되는 영역의 산불을 탐지한다.
2. 동기화된 IR 영상에서 가장 시급한 영역을 추출해 진화 대상을 선정한다.
3. 대상의 지리적 위치를 추정한다.
4. **2단계 자율 비행**: 지리 좌표 기반 유도 → 영상 기반 제어로 접근·정렬 후 소화탄 투하.

산불 모사 환경에서 실제 비행 실험을 했으며, EO 또는 IR 단일 센서 방식보다 높은 정확도로 진화함을 확인했다고 한다(구체 수치는 초록에 없음).

## 관련 페이지

- [[drone-wildfire-detection-network-optimization]] — 산불 조기탐지 네트워크 배치·라우팅 최적화
- [[marl-uav-wildfire-exploration]] — 산불 대응 자율 UAV 탐색 MARL
- [[thermal-drone-wildfire-monitoring]] — 열화상 산불 감시
