---
title: "Learning High-Speed Flight in the Wild"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: ai-autonomy
source: https://arxiv.org/abs/2110.05113
authors: Antonio Loquercio, Elia Kaufmann, René Ranftl, Matthias Müller, Vladlen Koltun, Davide Scaramuzza
published: 2021-10-11 (Science Robotics 2021, Vol.6, Issue 59, abg5810)
tags: [drone, ai, sim-to-real, end-to-end, obstacle-avoidance]
---
## 핵심 내용
온보드 센싱·연산만으로 복잡한 자연·인공 환경을 고속 비행하는 쿼드로터를 다룬다. 센싱-맵핑-계획을 분리하지 않고 잡음 있는 관측을 receding-horizon 방식으로 충돌 없는 궤적에 직접 매핑하는 end-to-end 방법이다. 합성곱 신경망을 시뮬레이션에서만 privileged learning(특권 정보를 가진 전문가 모방)으로 학습하고 현실적 센서 잡음을 시뮬레이션한다. 저자들은 밀림, 눈 덮인 지형, 탈선 열차, 붕괴 건물 등에서 'zero-shot transfer from simulation to challenging real-world environments'를 보고하며 전통적 장애물 회피 파이프라인보다 우수하다고 주장한다.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 수치: 초록에 비행 속도(m/s) 등 정량 수치 없음.
- 설계 시사점(원문 서술): 시뮬레이션 학습 시 센서 잡음 모델링, 특권 정보 전문가 모방, 단일 네트워크 end-to-end 구성.

## 한계·미확인
비행 속도, 입력 모달리티 세부(깊이 여부)는 초록에서 미확인. 본문 미열람. ~/2nd/concepts의 e2e-fly-end-to-end-quadrotor.md와 주제 근접(보강).
