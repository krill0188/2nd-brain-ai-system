---
title: "Transient Electro-Thermal Coupled Modeling of Three-Phase Power MOSFET Inverter during Load Cycles"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://doi.org/10.3390/ma14185427
tags: [drone, hardware, esc, thermal, mosfet, bldc, inverter, cfd]
authors: Hsien-Chie Cheng, Siang-Yu Lin, Yan-Cheng Liu
published: 2021-09-19 (Materials (Basel) 14(18):5427)
---

# BLDC 구동 3상 MOSFET 인버터의 과도 전기-열 결합 모델링 (Cheng et al., 2021)

## 핵심 내용
- BLDC 모터를 구동하는 3상 MOSFET 인버터(ESC 전력단에 해당)를 대상으로 전기-열 결합 해석(ETCA)을 제안한다.
- 3D 전자기 해석으로 기생성분을 추출하고, 등가회로로 전력 손실을 계산하며, 병렬 CFD 열해석으로 만든 Foster 열 회로망 모델을 쓴다.
- 접합 온도와 전력 손실이 서로 영향을 주는 되먹임을 모델에 포함한다.
- 자연대류와 강제대류에서 6-step 운전을 분석했다. 본문 수치: 첫 스위칭 상태에서 전력 손실은 25 °C 약 99.9 W에서 200 °C 약 108.4 W로 증가; 자연대류 시 하측 스위치 접합 온도 약 160 °C, 상측 약 152 °C; 강제대류에서는 약 135 °C로 낮아진다.

## 설계에 쓸 수 있는 지침
- ESC 방열 설계에서 강제 냉각(팬·기류) 유무가 접합 온도에 큰 차이를 만든다는 점을 열 검토 항목으로 넣을 수 있다.
- 손실이 온도에 따라 증가하므로 고온 조건에서 전류 정격을 다시 보는 절차가 필요하다.

## 한계·미확인
- 대상은 소형 드론 ESC가 아니라 일반 BLDC 구동 인버터 모델이다. 기체 장착 조건(프롭 기류, 밀폐 케이스)은 다루지 않는다.
- 초록은 정성 설명 위주이며, 사용한 MOSFET 부품 번호와 열저항 값은 본 자료에서 미확인.
- 수치는 본문 요약 확인 기준이며, 원문 표 전체는 열람하지 않았다.
