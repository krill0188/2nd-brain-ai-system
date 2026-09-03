---
title: "다중 무인기 데이터 수집에서 클러스터링 및 경로 생성 기법 특성 연구"
created: 2026-09-03
updated: 2026-09-03
type: concept
domain: ops-mission
tags: [swarm, ops-mission, drone-ai, drone]
sources: []
confidence: medium
contested: false
contradictions: []
---

# 다중 무인기 데이터 수집에서 클러스터링 및 경로 생성 기법 특성 연구

**저자**: 김상현 (국립부경대학교)  
**학술지**: 사물인터넷융복합논문지  
**발행연도**: 2026  
**링크**: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003375001  
**원문공개**: 공개

## 연구 개요

대규모 IoT 센서 네트워크에서 다중 UAV로 데이터를 수집하는 시스템의 구성요소 특성을 시뮬레이션으로 분석. 시스템은 ①클러스터링(노드를 UAV별로 분할), ②경로 생성(클러스터별 방문 경로 계산), ③주기적 경로 재생성으로 구성된다.

## 핵심 발견

- **데이터 신선도**는 경로 생성 알고리즘에 의해 결정됨. 중복 재방문 페널티를 반영하면 경로 산출 시간을 늘려도 신선도가 오히려 저하 (방문 순서 불변성 때문).
- **클러스터링을 매 주기 재수행**하면 데이터 수집량이 최대 1/4로 급감.
- **수요 가중 클러스터링(demand-weighted clustering)**을 적용하면 중복 재방문을 절반 이하로 감소.
- **최적 조합**: 탐욕 기반 경로 생성 + 수요 가중 클러스터링.

## 의의

다중 UAV IoT 수집 시스템 설계 시 클러스터링 전략과 경로 생성 방식의 상호작용 특성을 체계적으로 분석한 드문 연구다. 수요 가중 클러스터링의 중복 재방문 억제 효과는 실용적 배치 전략에 직접 적용 가능하다.

## 관련 페이지

군집 협업 경로 계획 알고리즘은 [[swarm-coordination]]을, IoT 환경 데이터 수집 드론 응용은 [[drone-ai]]를 참조한다.
