---
title: "UAV 프레임 구조 최적화·모듈형 플랫폼 연구"
created: 2026-10-16
updated: 2026-10-20
type: concept
domain: hardware
ontology_class: Frame
tags: [drone, drone-hw, hardware]
sources: [inbox/processed/fetch-2026-10-16-hw-paper-carbon-fiber-3d-printed-frame-hoang-2026.md, inbox/processed/fetch-2026-10-16-hw-paper-uav-airframe-strength-stiffener-ye-2025.md, inbox/processed/fetch-2026-10-16-hw-paper-mrs-drone-modular-hert-2023.md, inbox/processed/fetch-2026-10-17-arxiv-a-self-rotating-tri-rotor-uav-for-field-of-view-expansion-an.md, inbox/processed/fetch-2026-10-17-arxiv-fam-dq-a-dual-quadrotor-based-fully-actuated-aerial-manipula.md, inbox/processed/fetch-2026-10-20-arxiv-a-generative-neural-network-approach-for-3d-multi-criteria-d.md, inbox/processed/fetch-2026-10-20-arxiv-capsulebot-a-novel-hybrid-aerial-ground-bi-copter-robot-with.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 프레임 구조 최적화·모듈형 플랫폼 연구

## 경량 3D 프린팅 탄소섬유 프레임 (Hoang 외, 2026)
F450 기준으로 CFD·FEA·위상 최적화를 결합해 연속 탄소섬유 3D 프린팅 프레임을 제작했다. 초록은 40% 경량화를 보고하고, 비행 시간 28% 증가·탑재 36% 개선은 검색 요약 확인값이라 원문 대조가 필요하다. 개선이 질량 효과만인지 공력 효과가 섞였는지는 미확인.^[inbox/processed/fetch-2026-10-16-hw-paper-carbon-fiber-3d-printed-frame-hoang-2026.md]

## 기체 강도 해석 (Ye 외, 2025)
7.30 kg 쿼드로터의 호버 하중 정적 해석. 원설계 최대 응력 309.2 MPa·변위 6.49 mm에서, 방식 I(질량 불변)은 응력 189.2 MPa·변위 5.91 mm, 방식 II(리브 보강 무제약)는 질량 6.92 kg(-5.2%)·응력 120.9 MPa(-60.9%)·변위 1.63 mm(-74.8%)였다. 충격·피로·진동은 다루지 않았다.^[inbox/processed/fetch-2026-10-16-hw-paper-uav-airframe-strength-stiffener-ye-2025.md]

## MRS Drone 모듈형 플랫폼 (Hert 외, 2023)
F450(페이로드 약 0.5 kg, 비행 10~15분), X500, T650(페이로드 2.5 kg) 프레임을 교체 가능한 모듈형 구조로 구성한 다중 로봇 플랫폼이다. X500·T650의 비행 시간과 부품 번호는 미확인.^[inbox/processed/fetch-2026-10-16-hw-paper-mrs-drone-modular-hert-2023.md]

관련: [[drone-frame-platform-specs-catalog]], [[drone-hw]], [[drone-payload-systems]].

## 최신 근거 연결 (2026-10-17)

- 기체 형상 측면 사례: 모터 3개로 위치·롤·피치를 제어하며 연속 회전으로 FoV를 넓히는 트라이로터(풍속 4.8 m/s까지 안정 비행): [[spinner-self-rotating-tri-rotor]]^[inbox/processed/fetch-2026-10-17-arxiv-a-self-rotating-tri-rotor-uav-for-field-of-view-expansion-an.md]
- 수동 조인트로 쿼드로터 모듈 2개를 잇는 완전구동 구조: [[fam-dq-dual-quadrotor-aerial-manipulator]]^[inbox/processed/fetch-2026-10-17-arxiv-fam-dq-a-dual-quadrotor-based-fully-actuated-aerial-manipula.md]

## 최신 근거 연결 (2026-10-20)

- 시뮬레이션 10,000개 데이터로 CVAE를 학습해 역학·열역학·공기역학 기준을 동시에 만족하는 모터 마운트를 생성하는 접근(정량 성능은 초록에 없음): [[generative-cvae-uav-engine-mount-design]]^[inbox/processed/fetch-2026-10-20-arxiv-a-generative-neural-network-approach-for-3d-multi-criteria-d.md] — 위 강도 해석·프레임 설계 사례의 수작업 탐색을 생성 모델로 대체하는 방향이다.
- 틸트 로터가 지상에서 구동 바퀴가 되는 4모터 하이브리드 바이콥터로 급경사 등반·험지 주행을 시제품에서 시연했다: [[capsulebot-hybrid-aerial-ground-bicopter]]^[inbox/processed/fetch-2026-10-20-arxiv-capsulebot-a-novel-hybrid-aerial-ground-bi-copter-robot-with.md]
