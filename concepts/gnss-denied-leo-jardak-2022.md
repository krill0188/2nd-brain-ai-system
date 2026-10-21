---
title: "The Potential of LEO Satellite-Based Opportunistic Navigation for High Dynamic Applications"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: navigation-gnss-denied
tags: [drone, gnss]
sources: [inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]
confidence: medium
contested: false
contradictions: []
---

# The Potential of LEO Satellite-Based Opportunistic Navigation for High Dynamic Applications

- 원문: https://doi.org/10.3390/s22072541 (PMC9003064)^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]
- 저자: Nabil Jardak, Quentin Jault^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]
- 발행: 2022-03-25 (Sensors 22(7):2541)^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]

## 핵심 내용
Iridium Next LEO 위성 신호를 기회신호(SOP)로 쓰고 IMU·자력계와 융합하여 고동적 비행체를 항법하는 가능성을 시뮬레이션으로 분석했다. 궤도 오차나 위성 시계 드리프트가 크면 위치 오차가 크게 늘지만, 정밀 궤도가 있으면 더 좋은 IMU를 쓴 INS와 경쟁 가능한 수준이 된다. 자세 추정은 이 오차에 상대적으로 둔감하다. GNSS 거부 환경의 대안으로 유망하다고 결론.^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 기준(열잡음만, 완전한 궤도·시계) 위치 RMSE: X 128.84 m, Y 95.90 m, Z 166.60 m; 자세 roll 1.49 deg, pitch 1.88 deg, yaw 4.18 deg^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]
- 위성 위치 오차 시 3D 위치 오차 약 2.5 km(중간)/4.4 km(최악)^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]
- 위성 시계 드리프트 1 ppb에 위치 81 m, 10 ppb에 1.76 km 악화^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]
- 비교 전술급 INS: 위치 X 181.78 m, Y 238.02 m, Z 182.31 m, 자세 roll 0.45 deg, pitch 0.27 deg, yaw 0.63 deg^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]
- Doppler 측정 표준편차 5~12.5 Hz, 자세 수렴 약 15 s, 평균 가시 위성 약 8^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]

## 한계·미확인
시뮬레이션 기반(초록 기준). 수치는 수백 m~km 급이라 소형 드론 정밀 착륙 용도로는 부족. 실비행 검증 여부 미확인.^[inbox/processed/hw-20261021-gnss-denied-leo-jardak-2022.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[gnss-denied-remote-autonomy]]
