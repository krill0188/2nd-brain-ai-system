# 클레임 목록

## C1

- claim: `mastervault-hardware-reference` 문서에는 Pixhawk 6X 등 FC(비행제어기)의 프로세서(STM32 계열) 사양이 정리되어 있다.
- claim_type: fact
- supporting_sources:
  - ^[raw/articles/mastervault-hardware-reference.md]

## C2

- claim: 마이크로드론용 단안카메라+IMU 기반 SLAM 연구(`danial2025-microdrone-slam`)와 GPS-거부 환경 UAV SLAM 연구(`radwan2024-uav-slam-gpsdenied`)는 온보드에서 시각·관성 데이터를 실시간 처리하는 것을 전제로 하지만, 두 연구 모두 실행 플랫폼의 구체적 온디바이스 AI 프로세서(Jetson Orin/Nano 등) 성능 지표는 검색 결과에 나타나지 않는다.
- claim_type: inference
- supporting_sources:
  - ^[raw/papers/drone-hw/danial2025-microdrone-slam.md]
  - ^[raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md]

## C3

- claim: Jetson Orin/Nano와 같은 특정 온디바이스 AI 하드웨어가 실시간 자율 임무 처리 요구사항(지연시간·FPS 등 정량 지표)을 충족하는지를 직접 판단할 근거는 검색 결과에 없다. `computer-vision-drone`, `flight-controller-hardware` 개념 문서가 관련 주제를 다루는 것으로 보이나 발췌 본문에 구체적 벤치마크는 포함되어 있지 않다.
- claim_type: hypothesis
- supporting_sources:
  - [[computer-vision-drone]]
  - [[flight-controller-hardware]]

## C4

- claim: canonical 계층에 통신/GPS 두절 환경의 분산형 UAV 군집을 다루는 `decentralized-swarm-gps-denied` 문서와 군집 운용 모드를 다루는 `swarm-modes` 문서가 존재한다.
- claim_type: fact
- supporting_sources:
  - [[decentralized-swarm-gps-denied]]
  - [[swarm-modes]]

## C5

- claim: 내부 프로젝트 자료(`mastervault-recon-swarm`, `mastervault-swarm-architecture`)에 기술된 군집 아키텍처는 Ground Station을 포함하는 시스템 구조로 설계되어 있어, 실제 구현 단계에서는 데이터링크 통신의 존재를 전제로 하는 것으로 보인다.
- claim_type: inference
- supporting_sources:
  - ^[raw/articles/mastervault-recon-swarm.md]
  - ^[raw/articles/mastervault-swarm-architecture.md]

## C6

- claim: 완전한 무통신 상황에서 대형 유지·충돌 회피를 보장하는 구체적 알고리즘명이나 실험적 검증 결과는 검색 결과에 직접 제시되지 않았다.
- claim_type: hypothesis
- supporting_sources:
  - [[decentralized-swarm-gps-denied]]
  - ^[raw/articles/mastervault-swarm-architecture.md]

## C7

- claim: `radwan2024-uav-slam-gpsdenied` 논문(IEEE ICUAS 2024)은 GPS-거부 환경에서 UAV 지원 시각 SLAM을 통한 3D 장면 그래프 재구성을 다룬다.
- claim_type: fact
- supporting_sources:
  - ^[raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md]

## C8

- claim: `shapira2025-icdnet` 논문(2025 arXiv 프리프린트)은 드론 시각-관성 SLAM을 위한 ICD-Net(Inertial Covariance Displacement Network)을 제안한다.
- claim_type: fact
- supporting_sources:
  - ^[raw/papers/drone-ai/shapira2025-icdnet.md]

## C9

- claim: `radwan2024-uav-slam-gpsdenied`와 `shapira2025-icdnet` 두 연구 모두 학술논문/프리프린트 단계이며, 검색 결과 내에서 이 VIO/SLAM 기법이 실제 상용 제품이나 실전 임무에 배치되어 "실용화"되었음을 확인해주는 근거는 없다.
- claim_type: inference
- supporting_sources:
  - ^[raw/papers/drone-ai/radwan2024-uav-slam-gpsdenied.md]
  - ^[raw/papers/drone-ai/shapira2025-icdnet.md]

## C10

- claim: canonical 계층에 군집 운용 모드(`swarm-modes`)와 임무 계획(`mission-planning`) 개념 문서가 존재한다.
- claim_type: fact
- supporting_sources:
  - [[swarm-modes]]
  - [[mission-planning]]

## C11

- claim: 군집 내 일부 드론이 통신 두절/손실될 경우 중앙 통제 없이 임무를 자율 재분배하는 구체적 메커니즘은 검색 결과에서 확인되지 않는다. MAVLink(`entity-mavlink-protocol`)와 ArduPilot(`entity-ardupilot`) 관련 문서는 개별 기체-지상국 간 통신 프로토콜을 다룰 뿐, 손실된 드론의 임무를 다른 드론이 인계하는 재분배 로직은 언급하지 않는다.
- claim_type: hypothesis
- supporting_sources:
  - ^[raw/articles/entity-mavlink-protocol.md]
  - ^[raw/articles/entity-ardupilot.md]

## C12

- claim: 온디바이스 AI 탑재로 인한 전력·무게 증가가 체공시간에 미치는 정량적 영향(배터리 소모율, 비행시간 감소폭 등)을 직접 다루는 검색 결과는 없다. 상위 canonical 결과(`knowledge-tool-roles`, `ai-knowledge-workflow`)는 AI 지식관리 도구에 관한 것으로 주제가 다르며, raw 결과(`mastervault-hardware-reference`)도 FC 하드웨어 사양만 제공할 뿐 전력 소비 데이터는 포함하지 않는다.
- claim_type: hypothesis
- supporting_sources:
  - [[knowledge-tool-roles]]
  - ^[raw/articles/mastervault-hardware-reference.md]

## C13

- claim: 뉴스 보도에 따르면 우크라이나가 "실전 데이터+AI" 기반 드론돔을 수출하며 이를 한국 방산의 시험대로 언급하는 기사가 존재한다.
- claim_type: fact
- supporting_sources:
  - ^[https://news.google.com/rss/articles/CBMiiAFBVV95cUxPM1FpQVA2LVZ5Y0ZVQXNHQVlpMElnQlNOa0RmSGdWMllYSVZ4LWxlMTQwRkFiVk5SR1JuUEM3YmNKaUo4dHM2a0hUMUZCQnhUTlBFazhfaklJOTB6aXRvcGpoMk9rQldBWFJjZVNrN001eW15UzBoRTdMRHloZ1phRzliaFFSQ0NB?oc=5]

## C14

- claim: 우크라이나 드론돔 뉴스(실전 사례)와 내부 `mastervault-recon-swarm` 프로젝트(스스로 "학술연구 기반"으로 명시)를 비교하면, 실전 검증된 군집 자율 임무 사례와 마스터의 자체 프로젝트 사이에는 성숙도 격차가 있는 것으로 보이며, 뉴스 기사 자체는 해당 임무가 통신 제한 환경에서 수행되었는지를 구체적으로 명시하지 않는다.
- claim_type: inference
- supporting_sources:
  - ^[https://news.google.com/rss/articles/CBMiiAFBVV95cUxPM1FpQVA2LVZ5Y0ZVQXNHQVlpMElnQlNOa0RmSGdWMllYSVZ4LWxlMTQwRkFiVk5SR1JuUEM3YmNKaUo4dHM2a0hUMUZCQnhUTlBFazhfaklJOTB6aXRvcGpoMk9rQldBWFJjZVNrN001eW15UzBoRTdMRHloZ1phRzliaFFSQ0NB?oc=5]
  - ^[raw/articles/mastervault-recon-swarm.md]

## C15

- claim: canonical 계층에 `drone-regulations` 개념 문서가 존재한다.
- claim_type: fact
- supporting_sources:
  - [[drone-regulations]]

## C16

- claim: "통신 두절 상태에서의 자율 임무 수행"에 특화된 국내외 규제·안전 기준을 직접 다루는 검색 결과는 없다. 해당 질문 검색에서는 `recon-swarm-project`, `datalink-communication` 등 기술 문서만 반환되었고 뉴스 검색 결과는 매칭되지 않았다(규제 관련 `drone-regulations` 문서는 별도 질문(Q2)의 검색에서만 발견됨). 외부 법령 조사가 별도로 필요하다.
- claim_type: hypothesis
- supporting_sources:
  - [[recon-swarm-project]]
  - [[datalink-communication]]
