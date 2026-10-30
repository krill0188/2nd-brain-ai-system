---
title: "쿼드로터 제어기 비교: 튜닝·프리뷰·액추에이터·폴백이 순위를 바꾼다"
created: 2026-10-28
updated: 2026-10-28
type: concept
domain: flight-control
tags: [drone, drone-sw]
sources: [raw/papers/_unclassified/how-tuning-reference-preview-actuator-modeling-and-fallback-policies-change-quad.md]
confidence: low
contested: false
contradictions: []
---

# 쿼드로터 제어기 비교의 재현성 연구 (Dao 외, arXiv 2610.35165)

단일 추종 오차만 보고하는 제어기 비교가 튜닝 노력, 참조 정보, 액추에이터 예측, 최적화기 폴백, 명령 타이밍에 얼마나 좌우되는지 시뮬레이션으로 정량화했다(초록 기준).^[raw/papers/_unclassified/how-tuning-reference-preview-actuator-modeling-and-fallback-policies-change-quad.md]

## 설정
cascade PID, hover LQR, boundary-layer SMC(BL-SMC), 폴백 LQR 포함 선형 MPC(LMPC-F), preview 지원 LMPC-F, 기하학적 SO(3) 제어기를 자이로 결합·모터 지연·포화를 가진 공통 비선형 plant에서 비교. 1차 연구 556 에피소드(50 Hz), 확인 연구 1462 에피소드(신규 50 실현, 튜닝 후보 12/24/48).

## 결과
- 후보 12개 매칭 튜닝만으로 평균 RMSE 순위가 바뀌어 BL-SMC가 꼴찌에서 1위가 됐고, 신규 실현에서도 재현됐으며 48 후보에서도 불변이었다.
- 참조 preview는 MPC 추종 오차를 크게 줄였고 figure-eight에서 폴백 발동을 없앴다. 급격한 step에서는 폴백 정책·예측기·액추에이터 권한의 상호작용에 따라 결과가 달랐다.
- 측정된 명령 호출 지연을 재생하면 데스크톱에서 nominal MPC 4개 중 3개, Raspberry Pi 5에서 4개 모두 종료됐고, 솔버를 100회 반복으로 제한하면 테스트한 nominal 타이밍에서 deadline miss가 사라졌다.
- 저자들은 추종 정확도, 튜닝 노력, 완료·실패율, 폴백 활동, 입력 변동, 명령 타이밍을 포함한 보고 체크리스트를 제안한다.

## 관련 문서
[[pid-tuning-control]], [[temporal-cascading-quadrotor-mpc]], [[time-optimal-quadrotor-waypoints]]
