---
title: "다중 UAV 케이블 매달림 페이로드 운송 연구 (센서·유도·입력성형)"
created: 2026-10-17
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, drone-hw, research]
sources: [inbox/processed/fetch-2026-10-17-arxiv-compact-force-sensor-for-dual-uav-cable-suspended-payload-tr.md, inbox/processed/fetch-2026-10-17-arxiv-equivalent-agent-guidance-for-cooperative-uav-payload-transp.md, inbox/processed/fetch-2026-10-17-arxiv-global-sensitive-based-input-shaping-for-uav-payload-precisi.md, inbox/processed/fetch-2026-10-18-arxiv-autotrans-a-complete-planning-and-control-framework-for-auto.md, inbox/processed/fetch-2026-10-19-arxiv-an-input-output-feedback-linearization-based-exponentially-s.md, inbox/processed/fetch-2026-10-19-arxiv-temporal-waypoint-navigation-of-multi-uav-payload-system-usi.md, inbox/processed/fetch-2026-10-21-arxiv-maspa-an-efficient-strategy-for-path-planning-with-a-tethere.md]
confidence: medium
contested: false
contradictions: []
---

# 다중 UAV 케이블 매달림 페이로드 운송 연구

2026년 arXiv 논문 3건이 매달린/결합 페이로드 운송의 서로 다른 층(센싱·유도·입력 성형)을 다룬다. 페이로드 하드웨어 일반은 [[drone-payload-systems]], 에너지 모델은 [[multirotor-energy-power-models]] 참조.

## 1. 소형 힘 센서 + 장력 인식 외부 루프 (arXiv 2609.31035, 2026-09-25)
- 듀얼 UAV의 케이블 앵커 지점 상호작용력을 측정하는 소형 맞춤 센서를 설계했다. 선형성·이력·반복성·교차하중을 정적·동적으로 평가했다.^[inbox/processed/fetch-2026-10-17-arxiv-compact-force-sensor-for-dual-uav-cable-suspended-payload-tr.md]
- 제어는 캐스케이드 구조다: 빠른 내부 루프가 기체 안정화, 외부 루프가 측정된 힘을 보상한다.^[inbox/processed/fetch-2026-10-17-arxiv-compact-force-sensor-for-dual-uav-cable-suspended-payload-tr.md]
- 시뮬레이션과 실내 실험(페이로드 낙하, 제한 공간)에서 문헌의 분산 기준 제어 대비 안정화·협조·외란 제거가 개선되었다고 보고한다.^[inbox/processed/fetch-2026-10-17-arxiv-compact-force-sensor-for-dual-uav-cable-suspended-payload-tr.md]

## 2. 등가 에이전트 유도 (arXiv 2609.19312, 2026-09-16)
- 강체 페이로드를 든 UAV 2대를 하나의 가상 등가 에이전트로 표현해 착륙 플랫폼에 대한 상대 거리·시선각(LOS) 동역학으로 문제를 정식화한다.^[inbox/processed/fetch-2026-10-17-arxiv-equivalent-agent-guidance-for-cooperative-uav-payload-transp.md]
- 정지 플랫폼에는 임의의 접근각이 가능하나, 기동 플랫폼에 상대속도 0으로 전달하려면 속도·방향 동기화가 필요하여 착륙각이 0이 된다는 기하학적 조건을 제시한다.^[inbox/processed/fetch-2026-10-17-arxiv-equivalent-agent-guidance-for-cooperative-uav-payload-transp.md]
- 고정시간 슬라이딩 모드 유도로 초기 기하와 무관하게 유계 시간 내 수렴하며, Raspberry Pi 프로세서-인-더-루프에서 실시간 계산 요건을 만족했다.^[inbox/processed/fetch-2026-10-17-arxiv-equivalent-agent-guidance-for-cooperative-uav-payload-transp.md]

## 3. 전역 민감도 기반 입력 성형 (arXiv 2607.26717, 2026-07-29)
- 3D UAV-페이로드 시스템에서 페이로드 질량·로프 길이 불확실성에 강건한 입력 성형기를 설계한다. Shapley 값 개념으로 불확실 파라미터에 대한 민감도를 체계적으로 줄인다.^[inbox/processed/fetch-2026-10-17-arxiv-global-sensitive-based-input-shaping-for-uav-payload-precisi.md]
- 시뮬레이션에서 비강건·강건·미니맥스 설계와 비교해 성능 향상을 보였다(하드웨어 실험은 초록에 없음).^[inbox/processed/fetch-2026-10-17-arxiv-global-sensitive-based-input-shaping-for-uav-payload-precisi.md]

## 한계
세 논문 모두 초록 수준 정보이며 정량 수치(오차, 처리 시간 등)는 확인되지 않았다.

## 최신 근거 연결 (2026-10-18)

- 협업 운송 외에 줄 매단 페이로드 UAV의 실시간 궤적 계획과 적응형 NMPC 제어를 통합한 프레임워크도 보고됐다(초록 기준, 코드 공개 여부는 확인되지 않음): [[autotrans-uav-suspended-payload-planning-control]]^[inbox/processed/fetch-2026-10-18-arxiv-autotrans-a-complete-planning-and-control-framework-for-auto.md]

## 최신 근거 연결 (2026-10-20)

- 케이블이 아니라 2자유도 자기 구형 조인트로 강체 페이로드 프레임에 UAV를 연결한 구성도 연구된다: 입출력 피드백 선형화 추적 제어가 지수 안정이고 Gazebo 실시간 시뮬레이션에서 외란과 페이로드 질량 불확실성에 강건하다고 한다^[inbox/processed/fetch-2026-10-19-arxiv-an-input-output-feedback-linearization-based-exponentially-s.md], STL 시간 사양을 HOCBF로 처리한 웨이포인트 항법은 Gazebo 택배 시나리오로 시연했다^[inbox/processed/fetch-2026-10-19-arxiv-temporal-waypoint-navigation-of-multi-uav-payload-system-usi.md]: [[multi-uav-payload-transport-rao-controllers]]
- 위 케이블 방식 세 연구와 마찬가지로 이 구성의 결과도 초록상 시뮬레이션 단계이며 실기체 시험은 확인되지 않는다.

## 최신 근거 연결 (2026-10-21)

- 케이블이 페이로드가 아니라 지상 차량(UGV)과 UAV를 잇는 구성도 있다: 마수피얼 시스템의 테더를 팽팽하다고 가정하고 볼록성·장애물 기하로 UAV의 실행 가능한 이륙 지점 집합을 구해 경로를 계획하며, 테더로 UAV 비행 중 배터리 제약을 완화하는 것이 이점으로 제시된다(초록 기준, 느슨한 테더로 확장): [[maspa-tethered-marsupial-uav-ugv-path-planning]]^[inbox/processed/fetch-2026-10-21-arxiv-maspa-an-efficient-strategy-for-path-planning-with-a-tethere.md]
