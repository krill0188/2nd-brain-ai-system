---
title: "UAV 이상 동작 탐지를 위한 편차 특성 기반 적합도 함수"
created: 2026-10-23
updated: 2026-10-23
type: concept
domain: flight-control
tags: [drone, drone-sw]
sources: [raw/papers/drone-sw/uav-이상-동작-탐지를-위한-적합도-함수-연구.md, inbox/processed/fetch-2026-10-23-kci-uav-이상-동작-탐지를-위한-적합도-함수-연구.md]
confidence: low
contested: false
contradictions: []
---

# UAV 이상 동작 탐지를 위한 편차 특성 기반 적합도 함수

정우성(세종대), 정보보호학회논문지 2026. 원문 공개이나 이 페이지는 **초록 기준**이다.

## 문제
비행 제어 소프트웨어의 파라미터는 권장 범위 안이어도 특정 조합에서 경로 이탈·비행 정지·충돌을 일으킬 수 있다. 후보 조합을 모두 실행해 검증하기는 비싸므로 학습 기반 탐색은 적합도 함수로 이상 가능성이 높은 후보를 먼저 탐색한다. 기존 ICSearcher는 구간 내 예측 편차 합산을 쓰는데, 편차 크기·회복 실패 양상·상위 편차를 충분히 반영하지 못한다고 지적한다.^[raw/papers/drone-sw/uav-이상-동작-탐지를-위한-적합도-함수-연구.md]

## 제안
정규화된 제곱 편차, 회복 실패 항, 상위 편차 항을 결합한 적합도 함수. 같은 예측기·탐색 알고리즘에서 적합도 함수만 바꿔 비교했다.

## 결과 (초록)
ArduPilot 기반 시뮬레이션에서 기존 편차 합산 함수보다 이상 동작률과 후보 구분 성능이 높았다. 구체 수치는 확인하지 못했다.

관련: [[drone-anomaly-detection-survey]], [[ardupilot-params-by-version]], [[gnn-uav-anomaly-detection]].

## 📰 최근 관련 소식
- UAV 이상 동작 탐지를 위한 적합도 함수 연구 (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003395578
