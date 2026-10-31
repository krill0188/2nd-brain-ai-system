---
title: "선택적 슬라이딩 모드 제어: 외란 하 쿼드로터의 강인성 (Kiran 외, 2026)"
created: 2026-10-31
updated: 2026-10-31
type: concept
domain: flight-control
tags: [drone, drone-sw]
sources: [inbox/processed/fetch-2026-10-31-arxiv-selective-sliding-mode-control-enhances-robustness-of-aerial.md]
confidence: low
contested: false
contradictions: []
---

# 선택적 슬라이딩 모드 제어 (Selective SMC)

Anoop Kiran, Thales C. Silva, Nora Ayanian의 arXiv 논문(2026-10-28, 2610.38930v1). 초록 기준 요약이며 본문은 확인하지 않았다.^[inbox/processed/fetch-2026-10-31-arxiv-selective-sliding-mode-control-enhances-robustness-of-aerial.md]

## 문제
돌풍·페이로드 변화 같은 외란에서 쿼드로터를 제어할 때, 1차 슬라이딩 모드 제어(SMC)나 matched/unmatched 불확실성 구분 같은 고전 기법은 캐스케이드 제어기의 **어느 루프를 강인하게 만들지**, 어떻게 튜닝할지, 임베디드 프로세서에 비용이 얼마나 드는지를 알려주지 않는다. 모든 축에 일률로 강인 제어를 적용하면 외란이 없는 축에도 튜닝 부담이 생기고, 저구동(underactuated) 기체는 일부 축의 외란을 직접 상쇄할 수도 없다.

## 제안 방법
1. 외란 하 PID 호버 비행 데이터에서 운동방정식을 역산해 **작용 중인 외란**을 복원한다.
2. 복원 신호로 외란이 여기(excite)된 축을 식별·정량화한다.
3. 강인 제어(SMC)를 그 축에만 배치한다. 모든 제어는 기체 온보드에서 실행한다.

## 결과(초록)
Crazyflie 2.1에서 슬렁 페이로드와 비스듬한 바람 외란을 시험했고, 추종 성능 향상이 규칙이 선택한 축에 집중됐다. 게인 스윕에서 스위칭 게인은 matched 축의 오차를 줄이지만 여기된 unmatched 축에는 효과가 없었으며, 이는 분석이 예측한 대로라고 한다.

## 관련 문서
플랫폼은 [[crazyflie]], 제어기 비교 재현성은 [[quadrotor-controller-comparison-reproducibility-study]], 외란 대응 합의 제어는 [[dual-gradient-consensus-quadrotor-ood-disturbance]]를 참조한다.
