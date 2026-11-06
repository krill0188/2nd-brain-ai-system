---
title: "이기종 다중 UAV 시간-공간 위험도(TTC) 기반 충돌 회피 속도 결정"
created: 2026-11-04
updated: 2026-11-04
type: concept
domain: flight-control
tags: [drone, swarm, drone-sw]
sources: [inbox/processed/fetch-2026-11-04-kci-이기종-다중-uav-환경에서-시간-공간-위험도를-고려한-충돌-회피-속도-결정에-관한-연구.md]
confidence: low
contested: false
contradictions: []
---

# 이기종 다중 UAV 시간-공간 위험도(TTC) 기반 충돌 회피 속도 결정

박지호(경운대), 한국산학기술학회논문지(2026). 기체 크기·속도가 다른 이기종 다중 UAV에서 기존 APF+VO가 안전 후보 간 공간 이격과 시간적 임박도 차이를 반영하지 못하는 한계를 보완한다.^[inbox/processed/fetch-2026-11-04-kci-이기종-다중-uav-환경에서-시간-공간-위험도를-고려한-충돌-회피-속도-결정에-관한-연구.md]

## 방법
APF로 선호 속도 생성 → VO로 충돌 후보 필터링 → 선호도 비용 + 안전 여유(clearance) 비용 + TTC 비용으로 후보 평가. UAV 반지름과 최대 속도를 위험도 계산에 반영한다.

## 결과 (동일 동적 장애물, 제한 무작위 500개 시나리오 시뮬레이션)
- APF+VO 대비 충돌 수·평균 도달 시간 감소, 목표 도달률 향상.
- 최소 clearance 증가, near-miss·TTC 위반 감소. 동기종 환경과 고위험 시나리오에서도 유사한 개선.
- 시뮬레이션 한정이며 구체 수치는 초록에 없다(원문 비공개).

## 관련
- [[collision-risk-assessment]] — 충돌 위험 평가.
- [[collision-detection]] — 충돌 탐지·회피.

## 📰 최근 관련 소식
- 이기종 다중 UAV 환경에서 시간-공간 위험도를 고려한 충돌 회피 속도 결정에 관한 연구 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003400271
