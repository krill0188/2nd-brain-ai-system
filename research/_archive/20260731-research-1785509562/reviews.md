# 검토 (Critic + Verifier)

## C1

- opposing_sources: 없음. 다만 동일 출처 내에서 "UAV 간 통신 불가"라는 환경 가정과 "군집으로 협업"·"분산 포위 전략으로 협업"이라는 서술이 병존해, 통신 없이 어떻게 협업적 포위 행동이 조율되는지가 출처 자체에서 명확히 설명되지 않는다.
- limitations: 단일 arXiv 프리프린트(Silveria et al., 2026)에만 근거하며, 동료심사 여부·재현 검증이 확인되지 않는다. "실제 로봇 검증 완료"의 규모(기체 수, 실내/실외, 표적 복잡도)가 불명확해 군사 표적 방어라는 응용 시나리오로 일반화하기엔 근거가 얕다.
- confidence: medium
- verification_status: grounded

## C2

- opposing_sources: 없음
- limitations: 이는 일반 산업 표준이 아니라 마스터 개인 프로젝트(Recon Swarm/Swarm Architecture 노트)의 특정 설계이다. Leader-Follower + MAVLink 구조는 Leader 기체 또는 GCS-Leader 링크에 단일 실패점(SPOF)이 존재해, 통신 제한 환경에서는 구조적으로 취약하다는 점이 이 claim 자체에는 반영되지 않았다.
- confidence: high
- verification_status: grounded

## C3

- opposing_sources: 없음
- limitations: 단일 연구(federated-lightweight-intrusion-detection)의 자체 보고 수치이며 독립 재현이 확인되지 않는다. "리소스 제약 드론 스웜 환경"이라는 일반화된 표현과 달리, 실제 검증은 Raspberry Pi 4 단일 하드웨어·특정 데이터셋에 한정된다(C7 참조). 비행 중 열·전력 제약, 무선 링크 변동성 등 실제 비행 조건은 테스트에 포함되지 않았을 가능성이 높다.
- confidence: medium
- verification_status: grounded

## C4

- opposing_sources: 없음
- limitations: swarm-modes(LF+MAVLink)와 decentralized-swarm-gps-denied(온보드 센서만 의존, UAV 간 통신 불가 가정)는 서로 다른 논문/프로젝트의 설계 철학으로, 하나의 시스템이 두 모드를 "전환"한다는 근거는 검색 결과 어디에도 없다. 이는 두 개념을 결합한 추론(가설)일 뿐, 실제 모드 전환 메커니즘이 구현·검증되었다는 근거는 없다.
- confidence: low
- verification_status: insufficient_evidence

## C5

- opposing_sources: 없음
- limitations: 검색 범위(canonical+raw+뉴스)의 한계일 뿐 실제로 그런 알고리즘이 존재하지 않는다는 증거는 아니다. 후속 조사 필요성만 시사한다.
- confidence: low
- verification_status: grounded

## C6

- opposing_sources: 없음
- limitations: computer-vision-drone 문서의 FPS 수치는 출처 논문/벤치마크가 명시되지 않은 요약 표로, 어떤 Jetson 모델(Nano/Xavier NX/Orin 등)인지 특정되지 않아 재현·검증이 불가능하다. 마스터의 로컬 개발 환경(Intel 듀얼코어 Mac)에서는 Jetson급 GPU 추론을 직접 재현·검증할 수 없어 이 수치의 사실 여부를 독자적으로 확인하기 어렵다.
- confidence: low
- verification_status: grounded

## C7

- opposing_sources: 없음(C3과 동일 출처 중복 인용)
- limitations: Raspberry Pi 4는 GPU 가속이 없는 저전력 SBC로, 실제 비행 중 온보드 연산(비행 제어+FL 학습 동시 수행) 시 열·전력·타이밍 제약이 실험 환경과 다를 수 있다. "실용적 배포가 가능함을 보였다"는 결론은 실험실 조건에서의 결과이며 실비행 검증은 아니다.
- confidence: medium
- verification_status: grounded

## C8

- opposing_sources: 없음
- limitations: 단일 연구(chained-attacks-drone-fl)의 특정 공격 시나리오(802.11 deauth, Flower 프레임워크) 실험 결과로, 다른 통신 프로토콜이나 자연 발생적 통신 장애(전파 음영, 배터리 저하 등)에도 동일하게 적용되는지는 검증되지 않았다.
- confidence: medium
- verification_status: grounded

## C9

- opposing_sources: 없음
- limitations: Jetson 기반 비전 모델 벤치마크(C6)와 Raspberry Pi 4 기반 FL+KD 침입탐지 실험(C7)은 하드웨어·태스크·연구 목적이 전혀 다른 별개의 연구로, 이를 결합해 "연산 등급이 임무 복잡도 상한을 결정한다"는 일반 원칙을 도출하는 것은 근거를 넘어서는 확장 추론이다.
- confidence: low
- verification_status: insufficient_evidence

## C10

- opposing_sources: 없음
- limitations: 이는 마스터 개인 프로젝트의 2026-07-27 시점 스냅샷(dev notes)으로, 외부에서 독립 검증된 사실이 아니라 프로젝트 소유자 자신의 상태 보고다. 리뷰 시점(2026-07-31)까지 진행 상황이 이미 바뀌었을 수 있다.
- confidence: high
- verification_status: grounded

## C11

- opposing_sources: 없음
- limitations: 알고리즘 목록 자체는 널리 알려진 사실이나(일반적으로 알려진 사실: ORB-SLAM3, VINS-Fusion 등은 공개 오픈소스 프로젝트로 실재함), computer-vision-drone 표는 이들이 "드론에" 실제로 적용된 구체적 사례·성능을 제시하지 않고 일반적 SLAM 분류표만 나열한다.
- confidence: medium
- verification_status: grounded

## C12

- opposing_sources: 없음
- limitations: danial2025 논문은 arXiv 프리프린트로 동료심사 여부가 불명확하다. "실증되었다"는 표현은 통제된 실험실 조건에서의 결과일 가능성이 높으며, 조명 변화·고속 기동 등 실제 야외 마이크로 드론 운용 조건에서의 강건성은 확인되지 않는다.
- confidence: low
- verification_status: grounded

## C13

- opposing_sources: 없음
- limitations: shapira2025 역시 arXiv 프리프린트(2512.00037)이며, "제시한다"는 표현대로 접근법 제안 수준으로 실비행 통합·검증 결과는 abstract에서 확인되지 않는다.
- confidence: low
- verification_status: grounded

## C14

- opposing_sources: recon-swarm-project 출처는 Optical Flow를 단순히 센서 스택의 한 항목("GPS-denied 위치추정")으로 나열할 뿐, LiDAR/카메라/Radar/RTK GPS와의 "계층적 결합" 구조를 명시하지 않는다.
- limitations: "저수준 오도메트리-고수준 매핑의 계층적 결합"이라는 구체적 아키텍처 패턴은 두 출처 어디에도 직접 서술되어 있지 않으며, 이는 일반적인 로보틱스 관행에 기반한 저자의 추정에 가깝다.
- confidence: low
- verification_status: insufficient_evidence

## C15

- opposing_sources: 없음
- limitations: 이 항목들은 프로젝트 "설계"에 포함된 것이지 구현·비행 검증된 것이 아니다. C10에 따르면 프로젝트는 아직 1단계(단일 기체)에 머물러 있어, 다중 기체 상황에서의 통신 두절 대응(독립 귀환)이나 최소 이격거리 충돌회피는 아직 실제 군집 조건에서 테스트되지 않았을 가능성이 높다.
- confidence: medium
- verification_status: grounded

## C16

- opposing_sources: 없음
- limitations: 검증 규모가 쿼드로터 2대에 불과해, 대규모 군집(수십 기)으로의 확장성은 확인되지 않는다.
- confidence: high
- verification_status: grounded

## C17

- opposing_sources: CEDA의 "분산 실행(Decentralized Execution)"은 CTDE(강화학습 패러다임) 맥락에서 "훈련은 중앙집중, 실행 시 각 에이전트가 로컬 관측만으로 정책을 수행한다"는 의미이며, 이것이 곧 "완전 무통신 상태에서의 오프라인 사전계획 실행"과 동일한 개념이라는 근거는 출처에 없다. 두 개념을 동일시하는 것은 개념적 비약이다.
- limitations: CEDA는 PX4 SITL 시뮬레이션(C21)에서만 검증되었고 실제 무통신 상황에서의 실비행 검증이 아니다.
- confidence: low
- verification_status: insufficient_evidence

## C18

- opposing_sources: 없음
- limitations: 검색 공백을 지적하는 수준의 가설로, 그 자체로는 큰 한계가 없다.
- confidence: low
- verification_status: grounded

## C19

- opposing_sources: 없음(단, C21에서 확인되듯 유사한 다른 연구(CEDA)는 SITL 시뮬레이션에 그친 것과 대비되어, "실제 로봇 검증"이라는 표현이 상대적으로 이례적임)
- limitations: 단일 프리프린트의 자체 보고 주장이며, "실제 로봇"의 규모·환경 복잡도(실외/실내, 기체 수, 표적 종류)가 구체적으로 명시되지 않아 군사적 표적 방어 시나리오로의 일반화는 과장일 수 있다.
- confidence: medium
- verification_status: grounded

## C20

- opposing_sources: 없음
- limitations: "실제 하드웨어 테스트베드"라 해도 실험실 규모의 소수 기체 테스트일 가능성이 높으며, 실제 비행 중(진동, 전력 변동, RF 간섭) 조건에서의 검증인지는 출처에서 확인되지 않는다.
- confidence: medium
- verification_status: grounded

## C21

- opposing_sources: 없음. 오히려 이 claim은 C16이 암시할 수 있는 "실제 검증됨"이라는 인상을 명확히 교정하는 역할을 한다.
- limitations: 식별된 제약 없음(출처에 명시적으로 기재됨)
- confidence: high
- verification_status: grounded

## C22

- opposing_sources: 없음
- limitations: 검색 범위 내 부재를 근거로 한 가설로, 검색되지 않은 군사 기밀·비공개 상용 배치 사례가 존재할 가능성을 배제할 수 없다.
- confidence: low
- verification_status: grounded

## C23

- opposing_sources: 없음
- limitations: 일반적으로 알려진 사실: 각국 규제는 지속적으로 개정되므로(예: FAA Part 107 세부 조항, EASA U-space 규정 등) 문서상 요약이 최신 규정과 정확히 일치하는지는 별도 확인이 필요하다.
- confidence: medium
- verification_status: grounded

## C24

- opposing_sources: 없음
- limitations: 2026년 7월 시점의 "협의 진행 중" 상태를 보도하는 시사성 뉴스 요약으로, 리뷰 시점(2026-07-31) 기준으로도 최종 확정된 규정이 아니라 유동적인 정책 논의 단계다.
- confidence: medium
- verification_status: grounded

## C25

- opposing_sources: 없음
- limitations: 검색 공백에 기반한 가설이며, 특히 한국 국토교통부 등 마스터의 실제 프로젝트(Recon Swarm)가 적용받을 국내 규제 맥락에서 통신 제한 군집 운용에 대한 규정 유무는 별도로 직접 확인이 필요하다.
- confidence: low
- verification_status: grounded

## C26

- opposing_sources: 없음(C15와 사실상 동일 내용 중복)
- limitations: C15와 동일 — 설계 포함 사실이지 실비행 검증 사실은 아니다.
- confidence: medium
- verification_status: grounded

## C27

- opposing_sources: 없음
- limitations: 단일 요소 인증의 취약점 및 공격 체인은 특정 테스트베드(Flower, RPi/Jetson)에서의 시연이며, 실제 상용/군용 드론의 인증 체계(예: MAVLink 2.0 서명 등)가 다를 경우 동일하게 적용되지 않을 수 있다.
- confidence: medium
- verification_status: grounded

## C28

- opposing_sources: C1에서 지적한 것과 동일하게, "통신 없이" 협업적 포위가 가능하다는 서술은 출처 내부에서 협업 메커니즘이 구체적으로 설명되지 않아 자기모순적으로 읽힐 여지가 있다(상대 위치 관측 자체가 일종의 암묵적 정보 교환일 수 있음).
- limitations: 단일 프리프린트 기반, 실증 규모 불명확(C1과 동일).
- confidence: medium
- verification_status: grounded

## C29

- opposing_sources: 없음
- limitations: chained-attacks-drone-fl은 연합학습 모델 훈련의 보안/가용성 문제를 다루고, recon-swarm-project의 독립 귀환은 비행 안전 페일세이프를 다룬다. 두 영역(사이버보안 vs 비행안전)은 서로 다른 문제 도메인으로, 이를 결합해 "군집 수준 결함 허용 메커니즘이 필요하다"는 일반 결론을 도출하는 것은 카테고리를 혼합한 추론이며 두 출처 어디에도 직접적으로 연결되어 있지 않다.
- confidence: low
- verification_status: insufficient_evidence

## C30

- opposing_sources: 없음
- limitations: 검색 공백에 근거한 가설이며, 정량적 결함 허용 임계치는 도메인(항공 안전공학, 분산시스템 이론)에 따라 표준이 존재할 수 있으나 이번 검색 범위에서는 확인되지 않았다.
- confidence: low
- verification_status: grounded
