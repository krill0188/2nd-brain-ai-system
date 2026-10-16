---
title: "Strength analysis and structural optimization of UAV airframe"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2025.1708043/full
tags: [drone, hardware, airframe, structure, lightweight, fea, stiffener]
authors: Longhai Ye, Yanpeng Zhao, Haifeng Zhang, Yao Zhang, Jiming Lv, Zonghan Yang
published: 2025-12-01 (Frontiers in Mechanical Engineering 11, 2025)
---

# UAV 기체 강도 해석과 구조 최적화 (Ye et al., 2025)

## 핵심 내용
- 쿼드로터 기체를 호버링 하중으로 정적 해석하고, 두 가지 최적화를 비교한다: 질량 제약 구조 최적화(방식 I)와 보강 리브(stiffener) 무제약 최적화(방식 II).
- 원래 설계: 질량 7.30 kg, 최대 폰 미제스 응력 309.2 MPa, 최대 변위 6.49 mm.
- 방식 I: 질량 변화 없음, 응력 189.2 MPa(38.8% 감소), 변위 5.91 mm.
- 방식 II: 질량 6.92 kg(5.2% 감소), 응력 120.9 MPa(60.9% 감소), 변위 1.63 mm(74.8% 감소).
- 본문 표 기준 기체 재질 강도는 230 MPa로 적혀 있다.

## 설계에 쓸 수 있는 지침
- 경량화는 질량을 줄이는 것보다 응력·변위를 함께 보며 보강 위치를 정하는 것이 효과적이라는 점을 구조 검토 기준으로 쓸 수 있다.
- 탑재 하중 증가를 목표로 할 때 리브 보강이 질량 증가 없이 변위를 줄이는 사례로 참고할 수 있다.

## 한계·미확인
- 정적 호버 하중 해석만 다룬다. 충격, 피로, 진동 결과는 확인되지 않았다.
- 안전계수 1.5는 하중 계산 입력값으로만 쓰였으며, 계산된 최종 안전계수는 보고되지 않았다.
- 대상 기체의 전체 질량 7.30 kg은 대형 기체 기준이라 소형 기체에 그대로 적용하기 어렵다.
- 원문은 Frontiers 전문 페이지 요약으로 확인했다. 수치는 본문과 표 8을 근거로 옮겼다.
