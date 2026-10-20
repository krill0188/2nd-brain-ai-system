---
title: "프로펠러 성능 시험·측정 연구 (벤치, 저 Re, 덕티드 동축)"
created: 2026-10-16
updated: 2026-10-20
type: concept
domain: hardware
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-paper-propeller-motor-static-bench-milenkovic-babic-2026.md, inbox/processed/fetch-2026-10-16-hw-paper-propeller-test-bench-esp32-prasetiyo-2026.md, inbox/processed/fetch-2026-10-16-hw-paper-propulsion-efficiency-goli-2023.md, inbox/processed/fetch-2026-10-16-hw-paper-small-propeller-low-re-mollick-2024.md, inbox/processed/fetch-2026-10-16-hw-paper-ducted-coaxial-rotor-hover-li-2023.md, inbox/processed/fetch-2026-10-17-arxiv-machine-learning-for-uav-propeller-fault-detection-based-on-.md, inbox/processed/fetch-2026-10-19-arxiv-airspeed-estimation-for-uavs-using-only-propeller-feedback.md, inbox/processed/fetch-2026-10-20-arxiv-digital-twin-of-a-dc-brushless-electric-motor-propeller-syst.md]
confidence: medium
contested: false
contradictions: []
---

# 프로펠러 성능 시험·측정 연구

소형 UAV 프로펠러·추진계를 실험으로 측정한 논문 5편의 종합이다.

## 벤치 시험
- Milenković-Babić 외(2026): AXI 4130-16/-20 모터와 Aeronaut CAM 접이식 프로펠러 5종을 정적 측정했고 18×11인치가 추력과 추력-토크 비에서 가장 좋았다. 구체 수치는 초록에 없고 저널명·연도는 추정값이다.^[inbox/processed/fetch-2026-10-16-hw-paper-propeller-motor-static-bench-milenkovic-babic-2026.md]
- Prasetiyo 외(2026): ESP32 기반 저비용 벤치로 10×5인치 프로펠러 3종(사출·실리콘 주조·3D 프린팅)을 비교했고 총 추진 효율은 약 18~30%, 상용 사출품이 최고였다. 샘플이 3종뿐이다.^[inbox/processed/fetch-2026-10-16-hw-paper-propeller-test-bench-esp32-prasetiyo-2026.md]
- Goli 외(2023): 모터·프로펠러·배터리 조합 실험에서 12인치 프로펠러 최고 12.9%(3300 mAh)/11.4%(6000 mAh), 700 KV 모터 64.29%/62.01%를 보고했다. 구성품 단위 효율로 보이며 기체 전체와 직접 비교할 수 없다. 6000 mAh 배터리의 탑재 가능 페이로드는 5.82 N 대 2.02 N이었다.^[inbox/processed/fetch-2026-10-16-hw-paper-propulsion-efficiency-goli-2023.md]

## 공력 영역
- Mollick(2024, 석사논문): APC thin electric 14×12E, 17×12E, 19×12E를 저속 풍동·추력 스탠드로 시험, 저 전진비·Re 30,000~300,000 영역을 다룬다. 수치는 미확인.^[inbox/processed/fetch-2026-10-16-hw-paper-small-propeller-low-re-mollick-2024.md]
- Li 외(2023): 덕티드 동축 로터 풍동 시험에서 로터 간격 H/R=0.40 최적, 덕트 내 위치 0.31Cd에서 단일 로터 대비 파워 로딩 약 20% 향상, 팁 간격 δ≤0.015R, 최우수 구성 FOM 0.61. 호버 한정이며 전진 비행은 미확인.^[inbox/processed/fetch-2026-10-16-hw-paper-ducted-coaxial-rotor-hover-li-2023.md]

관련: [[fpv-motor-selection-guide]], [[bldc-motor-esc-characterization-research]], [[multirotor-propulsion-sizing-methods]], [[drone-hw]].

## 최신 근거 연결 (2026-10-17)

- 프로펠러 추력·토크를 RPM 입력 LSTM으로 모델링하고 고장 위치·손상 정도를 CNN으로 분류한 연구(테스트 세트 정확도 80% 이상, 기체 제작 편차로 약식 보정 필요): [[uav-propeller-fault-detection-hybrid-data]]^[inbox/processed/fetch-2026-10-17-arxiv-machine-learning-for-uav-propeller-fault-detection-based-on-.md]

## 최신 근거 연결 (2026-10-20)

- 프로펠러 전력·회전속도로 대기속도를 역산하는 모델을 BEM 시뮬레이션, 풍동, 비행시험 데이터로 유도해 피토관 대체·중복용으로 제안했다(고정익, 초록 기준): [[propeller-feedback-airspeed-estimation]]^[^[inbox/processed/fetch-2026-10-19-arxiv-airspeed-estimation-for-uavs-using-only-propeller-feedback.md]] — 위 벤치 시험이 정적 추력 중심인 데 비해 전진 비행 조건의 프로펠러 응답을 측정 수단으로 쓴 접근이다.
- 모터·프로펠러 쌍의 정지 추력 응답을 디지털 트윈과 비교한 결과 선형화 모델이 과도 응답에서 크게 어긋났다: [[bldc-motor-propeller-digital-twin-static-thrust]]^[^[inbox/processed/fetch-2026-10-20-arxiv-digital-twin-of-a-dc-brushless-electric-motor-propeller-syst.md]]
