---
title: "UAV 기지국 충전소 배치 최적화: 복귀 제약과 데이터율 보장"
created: 2026-10-27
updated: 2026-10-27
type: concept
domain: comms-protocol
tags: [drone, datalink]
sources: [inbox/processed/fetch-2026-10-27-kci-uav-기지국-운용을-위한-복귀-제약과-데이터율-보장-기반-충전소-배치-최적화.md]
confidence: low
contested: false
contradictions: []
---

# UAV 기지국 충전소 배치 최적화: 복귀 제약과 데이터율 보장

한국지능시스템학회 논문지(2026) 논문. 원문 비공개, 초록 기준이다.^[inbox/processed/fetch-2026-10-27-kci-uav-기지국-운용을-위한-복귀-제약과-데이터율-보장-기반-충전소-배치-최적화.md]

## 핵심 주장
- 체공 시간이 제한된 UAV 기지국에는 충전소가 필수이며, 충전소 위치가 서비스 가능 영역을 정한다. 기존 연구는 충전소를 주어진 것으로 두고 UAV 배치만 다뤘다.
- 복귀 제약과 개별 사용자의 데이터율 요구를 동시에 만족하는 UAV 위치가 존재할 **필요충분조건이 사용자–충전소 간 수평거리 조건**임을 보이고, 임계 반경을 닫힌 형태로 유도한다.
- 이에 따라 충전소 배치는 **원판 커버리지 문제**로 환원된다. 커버 사용자 최대화와 충전소 수 최소화를 정식화하고 근사 보장이 있는 그리디 알고리즘을 적용한다.
- 시뮬레이션으로 반경의 유효성을 검증하고, 복귀 제한 시간과 필요 충전소 수의 정량 관계를 제시한다. 수치는 초록에 없다.

## 관련 문서
UAV 중계·기지국 운용은 [[uav-relay]], 재난 지역 UAV 중계 규모 산정은 [[dynamic-fleet-sizing-uav-relays-post-disaster-mpc]]을 참조한다.

## 📰 최근 관련 소식
- UAV 기지국 운용을 위한 복귀 제약과 데이터율 보장 기반 충전소 배치 최적화 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003395775
