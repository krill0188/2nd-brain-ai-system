---
title: "Dual Gradient Consensus: 쿼드로터의 일시적 분포 외 외란 적응 학습"
created: 2026-10-28
updated: 2026-10-28
type: concept
domain: flight-control
tags: [drone, drone-ai]
sources: [raw/papers/_unclassified/dual-gradient-consensus-for-adaptive-learning-to-transient-out-of-distribution-d.md]
confidence: low
contested: false
contradictions: []
---

# Dual Gradient Consensus (DGC)

Tan & Tzoumas(arXiv 2610.34538, 2026-10-25). 초록 기준 정리.^[raw/papers/_unclassified/dual-gradient-consensus-for-adaptive-learning-to-transient-out-of-distribution-d.md]

## 문제
온라인 residual 적응으로 쿼드로터 궤적 추종 외란을 보상할 때, 짧은 분포 외(out-domain) residual이 고정 step 업데이트로 학습된 외란 모델을 오염시킨다.

## 방법
기존 도메인 적응 residual 정책(DAPL)의 random Fourier feature 모델, 오프라인 BPTT 정책, 최소제곱 적응을 유지하고 **온라인 업데이트 step size만** 바꾼다. 각 residual gradient를 장기·단기 gradient 메모리와 비교해 적응 상태를 분류하고, confidence map으로 신뢰할 수 없는 업데이트를 억제하되 지속적 도메인 변화 후에는 적응을 복구한다.

## 결과
in-domain 성분에 짧은 out-domain 이벤트가 섞인 4가지 residual 수치 실험에서, L1 증강 MPC·RFF 기반 MPC·고정 step DAPL·파라미터 동결 baseline 대비 4건 모두 평균 위치 RMSE가 가장 낮았다(수치 시뮬레이션만, 실기체 검증 언급 없음).

## 관련 문서
[[agile-quadrotor-learning]], [[quadrotor]], [[calos-lyapunov-safety-layer-quadrotor-rl]]
