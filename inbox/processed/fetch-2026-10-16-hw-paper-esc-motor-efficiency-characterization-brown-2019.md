---
title: "Characterization and Modeling of Brushless DC Motors and Electronic Speed Controllers with a Dynamometer"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://drum.lib.umd.edu/handle/1903/25410
tags: [drone, hardware, esc, motor, efficiency, dynamometer, bldc]
authors: Robert Brown
published: 2019 (University of Maryland 학위논문)
---

# BLDC 모터·ESC 특성 측정과 모델링 (Brown, 2019)

## 핵심 내용
- 동력계(dynamometer)로 DC·AC·기계 출력을 동시에 측정해 BLDC 모터와 ESC의 효율을 구한다.
- 시험 대상은 920 KV부터 2500 KV까지의 모터, 18 A·30 A·40 A ESC, 7.2 V·11.1 V·14.8 V 전압이다.
- 초록은 "ESCs could have efficiencies as low as 65%"라고 밝히며, 이것이 전체 시스템 효율을 크게 떨어뜨릴 수 있다고 쓴다.
- 3상 교류 회로를 등가 단일 회로로 묶은 해석 모델을 만들었고, 기계·AC·DC 출력 예측이 실험과 잘 맞는다고 보고한다.

## 설계에 쓸 수 있는 지침
- 추진계 효율을 모터 효율만으로 계산하지 말고 ESC 손실을 별도 항목으로 넣어야 한다는 근거로 쓸 수 있다.
- ESC 정격을 모터 전류에 맞출 때 전압 조건별 효율 저하를 함께 확인해야 한다(시험 전압 7.2–14.8 V 범위).

## 한계·미확인
- 학위논문이며 동료 심사 학술지 논문이 아니다.
- 초록은 65%라는 최저값만 제시한다. 측정 조건별 효율 곡선과 오차 범위는 본문 확인 전까지 미확인.
- DRUM 항목 페이지에서 초록을 요약 확인했다. 원문 PDF 전문은 열람하지 않았다.
