---
title: "A Modular Energy Aware Framework for Multicopter Modeling in Control and Planning Applications"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://arxiv.org/abs/2504.03256
tags: [drone, hardware, battery, energy-model, endurance]
authors: Sebastian Gasche, Christian Kallies, Andreas Himmel, Rolf Findeisen
published: 2025-04-04 (arXiv:2504.03256v1, cs.RO)
---

# 요약

멀티콥터의 동역학, 에너지 소비, 파워트레인(리튬이온 배터리·ESC·BLDC 모터)을 하나의 모듈형 프레임워크로 묶은 모델링 논문이다. 제어와 경로 계획에 쓸 수 있도록 구성 요소별 모델을 분리해 두었다고 초록에 기술되어 있다.

# 핵심 내용

- 파워트레인 모델이 리튬이온 배터리, 전자변속기(ESC), 브러시리스 DC 모터를 상세히 기술한다고 초록에 명시.
- 구성 요소 모델을 실제 시험비행 데이터로 검증했다고 초록에 명시.

# 설계에 쓸 수 있는 지침

- 배터리·ESC·모터를 독립 모듈로 나눈 구조는 체공시간 계산 로직을 부품 교체(셀·모터 변경)에 맞춰 갈아 끼우기 좋다.
- 에너지 모델을 제어·계획 루프에 넣을 때 "구성요소 모델 + 비행 데이터 검증" 절차를 참고할 수 있다.

# 한계·미확인

- 검증 오차 수치(정확도, 오차율)는 초록 페이지에 없어 **미확인**.
- 사용된 기체 사양, 배터리 셀 종류·용량, 비행 조건은 초록에서 **미확인**(본문 미열람).
- 본문 열람 전이므로 세부 모델식은 확인하지 않았다.
