---
title: "송전 인프라 점검 트럭-드론 협업 MILP 최적화"
created: 2026-11-03
updated: 2026-11-03
type: concept
domain: ops-mission
tags: [ops-mission, drone]
sources: [inbox/processed/fetch-2026-11-03-kci-대규모-송전-인프라-점검을-위한-3차원-이산화-기반-트럭-드론-협업-최적화-연구.md]
confidence: low
contested: false
contradictions: []
---

# 송전 인프라 점검 트럭-드론 협업 MILP 최적화

신정호(고려대, 물류과학기술연구, 2026) 논문 초록 기준 요약이다(KCI 원문 공개, 본문 미확인).^[inbox/processed/fetch-2026-11-03-kci-대규모-송전-인프라-점검을-위한-3차원-이산화-기반-트럭-드론-협업-최적화-연구.md]

## 모델
- 지상 트럭과 다수 드론이 협업하는 **VRP-D** 3차원 시공간 동기화 MILP 모델.
- 철탑 전압별 차등 점검 부하, 3차원 비행거리, 드론 배터리·체공시간 제약 반영.
- 521개 노드 규모의 연산 한계는 K-Means 기반 공간 분할(CFRS)과 Big-M Tightening, MTZ, Valid Inequalities로 대응.

## 결과
- 47개 철탑을 10개 클러스터로 분할해 배터리·시공간 동기화 제약을 만족하는 점검 스케줄을 도출, 총 누적시간 **555.04분**.
- 거점 간 거리 민감도 분석에서 거리가 늘면 시스템 병목이 전환되는 메커니즘을 확인, 현장 도입용 스케줄링 가이드라인으로 제안.

## 관련 문서
유사한 점검 최적화는 [[multi-uav-wind-farm-inspection]], 배터리 교체 계획은 [[uav-battery-replacement-planner]], 미션 계획 일반은 [[mission-planning]]을 참조한다.

## 📰 최근 관련 소식
- 대규모 송전 인프라 점검을 위한 3차원 이산화 기반 트럭-드론 협업 최적화 연구 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003400653
