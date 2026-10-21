---
title: "Deep Drone Acrobatics"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: ai-autonomy
source: https://arxiv.org/abs/2006.05768
authors: Elia Kaufmann, Antonio Loquercio, René Ranftl, Matthias Müller, Vladlen Koltun, Davide Scaramuzza
published: 2020-06-10 (RSS 2020)
tags: [drone, ai, sim-to-real, imitation-learning, agile-flight]
---
## 핵심 내용
온보드 센싱·연산만으로 극한 곡예 기동을 수행하는 쿼드로터 감각운동 정책을 학습한다. 학습은 전부 시뮬레이션에서 특권 정보를 가진 최적 제어기의 시연으로 하고, 시각 입력은 추상화를 거쳐 실제 기체로 전이한다. 'without any fine-tuning on real data'로 배치.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 기동: Power Loop, Barrel Roll, Matty Flip, 가속도 'up to 3g'.
- 사람 시연 불필요, 학습 중 실기체 손상 없음(원문).

## 한계·미확인
상태추정 지연 등 제어 루프 지연 수치는 초록에 없음(미확인).
