# 연구 메모 — 통신이 제한된 환경에서 온디바이스 AI를 탑재한 군집 드론이 자율 임무를 수행할 수 있는가?

## 1. 연구 질문
통신이 제한된 환경에서 온디바이스 AI를 탑재한 군집 드론이 자율 임무를 수행할 수 있는가?

## 2. 하위 질문
- **Q1**: 통신 두절/저대역 환경에서 군집 드론이 사용하는 자율 협조 알고리즘(분산 합의, 스웜 알고리즘)에는 어떤 것들이 있는가?
- **Q2**: 온디바이스 AI(엣지 컴퓨팅) 기반 드론의 연산·전력 제약이 자율 임무 수행 성능에 어떤 영향을 미치는가?
- **Q3**: GPS/통신이 제한된 환경에서 드론이 사용하는 대체 위치추정·항법 기법(SLAM, 시각-관성 항법 등)은 무엇인가?
- **Q4**: 군집 드론 간 통신이 완전 단절되었을 때 임무 지속을 가능하게 하는 사전 계획 기반 자율 실행 방식은 어떻게 설계되는가?
- **Q5**: 군집 드론의 온디바이스 AI 자율 임무 수행이 실제로 검증된 실증/실험 사례는 어떤 것이 있는가?
- **Q6**: 통신 제한 환경에서 군집 드론 운용에 관한 각국의 규제 및 정책 동향은 어떠한가? (외부조사 필요로 표시됨)
- **Q7**: 군집 내 일부 드론의 고장/통신 두절이 전체 임무 신뢰성에 미치는 영향과 결함 허용(fault tolerance) 기법은 무엇인가?

## 3. 사용한 내부 자료
**canonical**
- `concepts/decentralized-swarm-gps-denied.md`
- `concepts/swarm-modes.md`
- `concepts/swarm-coordination.md`
- `concepts/federated-lightweight-intrusion-detection.md`
- `concepts/computer-vision-drone.md`
- `concepts/recon-swarm-project.md`
- `concepts/visual-positioning-odometry.md`
- `concepts/cross-layered-medical-drone-coordination.md`
- `concepts/chained-attacks-drone-fl.md`
- `concepts/drone-regulations.md`
- `concepts/drone-news-regulations.md`

**raw**
- `raw/articles/mastervault-swarm-architecture.md`
- `raw/articles/mastervault-recon-swarm.md`
- `raw/papers/drone-hw/danial2025-microdrone-slam.md`
- `raw/papers/drone-ai/shapira2025-icdnet.md`

## 4. 관련 그래프 개념
질문별 1-hop 인접 슬러그를 취합·중복 제거한 목록:
`ai-agent`, `ai-knowledge-workflow`, `ai-personal-knowledge-management`, `amazon-mk30-safety-incident`, `ardupilot-architecture`, `brinc-emergency-drone-funding`, `chained-attacks-drone-fl`, `computer-vision-drone`, `cross-layered-medical-drone-coordination`, `datalink-communication`, `decentralized-swarm-gps-denied`, `digital-twin-intent-drone-networks`, `distributed-aerial-surveillance-swarm`, `dji-easa-sail-bvlos`, `doordash-air`, `drone-ai-agents`, `drone-payload-systems`, `drone-safety-failsafe`, `drone-simulation`, `flight-controller-hardware`

## 5. 확인된 사실
- **C1**: 분산형 UAV 군집은 GPS·통신 차단 환경에서 온보드 센서만으로 표적을 추적하고, 칼만 필터로 상대 측정만을 이용해 UAV·표적 상태를 추정하며 분산 포위 전략으로 협업한다. [[decentralized-swarm-gps-denied]]
- **C2**: 스웜 드론 시스템은 Leader-Follower 구조 기반 GCS-Leader-Follower MAVLink 통신 구조를 갖는다. [[swarm-modes]] ^[raw/articles/mastervault-swarm-architecture.md]
- **C3/C7**: FL+KD 결합 경량 침입탐지 프레임워크는 Raspberry Pi 4 실험에서 통신 비용 약 70%, 계산 오버헤드 29% 감소, 탐지 정확도 약 98.6%를 달성했다. [[federated-lightweight-intrusion-detection]]
- **C6**: Jetson 환경에서 YOLOv5/v8/v10 30-60+ FPS, YOLO-NAS 40-80 FPS, RT-DETR 20-40 FPS. [[computer-vision-drone]]
- **C8**: 드론 FL에서 무선 연결 중단은 Non-IID 조건에서 상당한 학습 불안정성을 유발하며, 단기 중단이 장기 학습 품질 저하로 확대될 수 있다. [[chained-attacks-drone-fl]]
- **C10**: Recon Swarm Project는 1단계(단일 기체 자율비행+센서 통합)만 진행 중이며 2~4단계(편대비행·군집·GPS-denied 실내 군집)는 계획 단계다. [[recon-swarm-project]] ^[raw/articles/mastervault-recon-swarm.md]
- **C11**: GPS 제한 환경에서 ORB-SLAM3, VINS-Fusion, RTAB-Map, LIO-SAM 등 SLAM/VIO 알고리즘이 사용된다. [[computer-vision-drone]] [[visual-positioning-odometry]]
- **C12**: 마이크로 드론에서 단안 카메라+IMU만으로 동시 위치추정·3D 준밀집 매핑이 가능함이 제시되었다. ^[raw/papers/drone-hw/danial2025-microdrone-slam.md]
- **C13**: ICD-Net은 관성 공분산 변위 네트워크로 시각-관성 SLAM 상태추정 정확도 개선을 제시한다. ^[raw/papers/drone-ai/shapira2025-icdnet.md]
- **C15/C26**: Recon Swarm Project는 통신 두절 대응 독립 귀환, 이중 Geofence, 배터리 페일세이프(자동 RTL), 최소 이격거리 충돌회피를 설계에 포함한다. [[recon-swarm-project]] ^[raw/articles/mastervault-recon-swarm.md]
- **C16**: Cross-Layered Multi-Drone Coordination은 CTDE 기반 CEDA 알고리즘을 PX4 SITL에서 X500 쿼드로터 2대로 검증했다. [[cross-layered-medical-drone-coordination]]
- **C19**: Decentralized UAV Swarms 연구는 GPS/통신 차단 조건의 분산 포위 기법을 실제 로봇으로 검증 완료했다고 명시한다. [[decentralized-swarm-gps-denied]]
- **C20**: FL 침입탐지·체인 공격 연구는 각각 Raspberry Pi 4, Raspberry Pi/Jetson 실제 하드웨어 테스트베드에서 검증되었다. [[federated-lightweight-intrusion-detection]] [[chained-attacks-drone-fl]]
- **C21**: CEDA 알고리즘 검증은 실제 비행이 아닌 PX4 SITL 시뮬레이션에서 이루어졌다. [[cross-layered-medical-drone-coordination]]
- **C23**: FAA Part 107, EASA, 영국 CAA, 한국 국토교통부 등이 고도·속도·VLOS 등을 규정하는 드론 운용 규제 프레임워크를 운영한다. [[drone-regulations]]
- **C24**: 2026년 7월 기준 영국 CAA는 Electronic Conspicuity 의무화를 협의 중이며, SESAR HAVEN 프로젝트는 AI·클라우드 기반 미래 항공교통관제 플랫폼을 개발 중이다. [[drone-news-regulations]]
- **C27**: 802.11 deauthentication 공격으로 연결이 끊긴 드론의 자격 증명을 이용한 사칭이 가능하며, 단기 무선 중단이 장기 학습 품질 저하로 확대될 수 있다. [[chained-attacks-drone-fl]]
- **C28**: 분산형 UAV 군집은 상호 통신 없이도 칼만 필터로 상대 측정만을 이용해 상태를 추정함으로써 통신 실패에 대한 강건성을 확보한다. [[decentralized-swarm-gps-denied]]

## 6. AI의 추론
검색 결과에서 도출된 추론(inference) 클레임 5건(C4, C9, C14, C17, C29)은 검토 단계에서 모두 `insufficient_evidence`로 판정되어, 확정된 추론으로 제시할 수 없다. 해당 내용은 "10. 근거 부족 사항"을 참고할 것.

## 7. 가설
- **C5**: 검색 결과에는 Paxos, gossip protocol 등 명명된 "분산 합의 알고리즘"에 대한 구체적 문서가 없어, 저대역/통신두절 환경에서 실제 사용되는 합의 알고리즘의 구체적 종류는 확인되지 않는다. [[decentralized-swarm-gps-denied]] [[swarm-modes]]
- **C18**: 통신 두절 시 "독립 귀환" 같은 개별 기체 페일세이프는 확인되나, 다수 기체가 사전 합의된 임무 계획을 무통신 상태에서 시공간적으로 동기화 실행하는 구체적 알고리즘은 확인되지 않는다. [[recon-swarm-project]] [[swarm-modes]]
- **C22**: 검색 결과에서 확인되는 온디바이스 AI 군집 자율성 검증 사례는 소규모 실제 로봇 실험과 SITL 시뮬레이션 수준에 머물러, 대규모 실전 배치 수준의 실증 사례는 확인되지 않는다. [[decentralized-swarm-gps-denied]] [[cross-layered-medical-drone-coordination]]
- **C25**: 검색된 규제 동향은 일반 공역 안전·가시성 규제에 초점이 있으며, "통신 제한/두절 환경에서의 군집 드론 운용"에 특화된 규제·정책은 확인되지 않아 외부 조사가 필요하다. [[drone-news-regulations]] [[drone-regulations]]
- **C30**: 군집 규모 대비 허용 가능한 노드 탈락 비율·정족수 기준 등 정량적 결함 허용 임계치에 대한 근거는 검색 결과에 없다. [[decentralized-swarm-gps-denied]] [[chained-attacks-drone-fl]]

## 8. 반대 근거
- **C14**에 대해: recon-swarm-project 출처는 Optical Flow를 센서 스택의 한 항목으로만 나열할 뿐, LiDAR·카메라·Radar·RTK GPS와의 "계층적 결합" 구조를 명시하지 않는다 — 해당 아키텍처 패턴은 일반적 로보틱스 관행에 기반한 추정에 가깝다.
- **C17**에 대해: CEDA의 "분산 실행(Decentralized Execution)"은 CTDE 강화학습 패러다임에서 "훈련은 중앙집중, 실행 시 로컬 관측만 사용"이라는 의미이며, 이를 "완전 무통신 상태에서의 오프라인 사전계획 실행"과 동일시할 근거는 출처에 없다.
- **C1/C28**에 대해: "UAV 간 통신 불가"라는 환경 가정과 "군집으로 협업"·"분산 포위 전략"이라는 서술이 동일 출처 내에서 병존해, 통신 없이 협업 행동이 어떻게 조율되는지가 출처 자체에서 명확히 설명되지 않는다(상대 위치 관측 자체가 암묵적 정보 교환일 수 있다는 지적도 있음).

## 9. 기술적 제약
- 다수 클레임(C1, C12, C13, C19, C28)이 단일 arXiv 프리프린트에만 근거하며, 동료심사·독립 재현 여부가 확인되지 않는다.
- 실증 검증 규모가 작다: CEDA는 쿼드로터 2대(C16), FL 침입탐지는 Raspberry Pi 4 단일 하드웨어(C3, C7), 체인 공격 연구는 특정 테스트베드(Flower, RPi/Jetson)에 한정된다(C20, C27).
- 시뮬레이션과 실비행의 구분이 필요하다: CEDA 알고리즘은 PX4 SITL 시뮬레이션에서만 검증되었고 실비행 검증이 아니다(C21).
- Recon Swarm Project의 안전 시스템(독립 귀환, Geofence 등)은 설계 단계이며, 프로젝트 자체가 아직 1단계(단일 기체)에 머물러 있어 다중 기체 조건에서 검증되지 않았다(C10, C15).
- Jetson 기반 비전 FPS 수치(C6)는 구체적 모델(Nano/Xavier NX/Orin 등)이 특정되지 않아 재현·검증이 어렵다.
- 규제 관련 정보(C23, C24)는 2026년 7월 시점 유동적 정책 논의 단계이며 최종 확정 규정이 아니다.

## 10. 근거 부족 사항
- **C4**: Leader-Follower 구조(MAVLink 의존)와 온보드 센서 기반 분산 협업 방식 간 "전환"이 실제로 구현·검증되었다는 근거가 없다 — 서로 다른 프로젝트/논문의 설계 철학을 결합한 추론.
- **C9**: Jetson 비전 벤치마크(C6)와 Raspberry Pi 4 FL+KD 실험(C7)은 하드웨어·태스크·연구 목적이 전혀 다른 별개 연구로, "연산 등급이 임무 복잡도 상한을 결정한다"는 일반 원칙을 도출하기엔 근거를 넘어선다.
- **C14**: "저수준 오도메트리-고수준 매핑의 계층적 결합" 아키텍처는 두 출처 어디에도 직접 서술되어 있지 않다.
- **C17**: CTDE의 "분산 실행"과 "완전 무통신 오프라인 사전계획 실행"을 동일시하는 것은 개념적 비약이며, CEDA는 시뮬레이션 검증에 그친다.
- **C29**: 연합학습 보안/가용성 문제(사이버보안 도메인)와 비행 안전 페일세이프(비행안전 도메인)를 결합해 "군집 수준 결함 허용 메커니즘이 필요하다"는 결론을 내리는 것은 서로 다른 문제 도메인을 혼합한 추론으로, 두 출처가 직접 연결되어 있지 않다.

## 11. 후속 조사 대상
- Paxos, gossip protocol 등 명명된 분산 합의 알고리즘이 실제 저대역/통신두절 군집 드론에 적용된 사례를 별도 검색.
- 다수 기체가 완전 무통신 상태에서 사전 합의된 임무 계획을 시공간적으로 동기화 실행하는 구체적 알고리즘(예: 사전 분산 타임라인, 로컬 정책 기반 자율 실행) 조사.
- 통신 제한/두절 환경에 특화된 각국 규제·정책(특히 한국 국토교통부의 군집 드론 통신 두절 대응 규정) 별도 조사 — Q6은 "외부조사 필요"로 이미 표시됨.
- 군집 규모 대비 허용 노드 탈락 비율·정족수 기준 등 정량적 결함 허용 임계치에 대한 항공 안전공학·분산시스템 이론 문헌 조사.
- 대규모(수십 기 이상) 실전 군사·상업 배치 수준의 온디바이스 AI 군집 자율성 실증 사례에 대한 별도 조사(현재는 소규모 로봇 실험·시뮬레이션 수준만 확인됨).
- 연산 등급(엣지 하드웨어 사양)과 수행 가능한 임무 복잡도 간의 관계를 다루는, 동일 플랫폼·동일 태스크 기반 비교 연구 탐색.

## 12. 출처 목록
- [[decentralized-swarm-gps-denied]]
- [[swarm-modes]]
- ^[raw/articles/mastervault-swarm-architecture.md]
- [[federated-lightweight-intrusion-detection]]
- [[computer-vision-drone]]
- [[recon-swarm-project]]
- ^[raw/articles/mastervault-recon-swarm.md]
- [[visual-positioning-odometry]]
- ^[raw/papers/drone-hw/danial2025-microdrone-slam.md]
- ^[raw/papers/drone-ai/shapira2025-icdnet.md]
- [[cross-layered-medical-drone-coordination]]
- [[chained-attacks-drone-fl]]
- [[drone-regulations]]
- [[drone-news-regulations]]

## 13. 마스터 승인 상태
awaiting_approval

---
> 참고: 이 연구 메모의 모든 판단은 전체 원문이 아닌 검색 스니펫(발췌)에
> 근거합니다. 스니펫 범위 밖에 반박/보강 근거가 존재할 수 있습니다.
