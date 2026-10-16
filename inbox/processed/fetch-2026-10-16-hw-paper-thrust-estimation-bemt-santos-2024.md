---
title: "A Generalized Thrust Estimation and Control Approach for Multirotors Micro Aerial Vehicles"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://arxiv.org/abs/2412.02874
authors: "Davi Santos, Martin Saska, Tiago Nascimento"
published: "2024-12-03"
tags: [drone, hardware, paper, thrust, BEMT, motor-control, ESC, propeller]
---

# A Generalized Thrust Estimation and Control Approach for Multirotors Micro Aerial Vehicles

## 핵심 내용 (방법·결과)

소형 멀티로터 UAV에서 일반적으로 사용되는 **로터 회전속도²에 비례하는 이차함수(quadratic) 추력 모델**이 비호버링 비행 조건에서는 부정확하다는 문제를 해결했다. Blade Element Momentum Theory(BEMT)를 기반으로 폐루프 추력 추정기와 컨트롤러를 제안했다.

**핵심 결과:**
- BEMT 기반 접근으로 공기역학적 계수를 다수 측정할 필요 없이, **테스트벤치 1회 실험에서 단일 스케일링 값**만 얻으면 추력 추정 가능.
- 250mm 및 500mm 플랫폼에서 실외 비행 검증 완료.
- 기존 이차함수 모델 대비 **공기역학 조건이 변화하는 환경에서 더 높은 견고성** 확인.
- 관련 저널: IEEE Robotics and Automation Letters (DOI: 10.1109/LRA.2024.3433749).

## 설계에 쓸 수 있는 지침

- 모터-프로펠러 매칭 후 **간단한 벤치 테스트 1회로** 실용적 추력 모델 구축 가능 → 개발 비용 절감.
- 비호버링(기울기 비행, 고속 기동) 조건에서는 이차 모델 대신 BEMT 기반 모델을 사용해야 추력 오차를 줄일 수 있다.
- 소형(250mm) 및 중형(500mm) 플랫폼 모두 동일 방법론 적용 가능 → 프레임 크기 무관하게 재사용 가능한 접근법.

## 한계·미확인 항목

- 추력 추정 정량 오차(%) 수치: 미확인 (초록에 미기재).
- 매우 소형(100mm 이하) 또는 대형 플랫폼에서의 유효성은 미확인.
- 열관리 또는 ESC 손실 모델은 포함되지 않음.
