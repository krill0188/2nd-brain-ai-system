# 클레임 목록

## C1

- claim: 분산형 UAV 군집 시스템은 GPS 및 통신이 차단된 환경에서 온보드 센서만으로 표적을 추적하고, 칼만 필터로 상대 측정만을 이용해 UAV와 표적의 상태를 추정하며 분산 포위(encirclement) 전략으로 협업한다.
- claim_type: fact
- supporting_sources:
  - [[decentralized-swarm-gps-denied]]

## C2

- claim: 스웜 드론 시스템은 Leader-Follower 구조를 기반으로 GCS-Leader-Follower 간 MAVLink 통신 구조를 사용하는 아키텍처를 갖는다.
- claim_type: fact
- supporting_sources:
  - [[swarm-modes]]
  - ^[raw/articles/mastervault-swarm-architecture.md]

## C3

- claim: 연합학습(FL)과 지식 증류(KD)를 결합한 경량 침입탐지 프레임워크는 리소스 제약 드론 스웜 환경에서 통신 비용을 약 70%, 계산 오버헤드를 29% 감소시키면서 약 98.6%의 탐지 정확도를 달성했다.
- claim_type: fact
- supporting_sources:
  - [[federated-lightweight-intrusion-detection]]

## C4

- claim: Leader-Follower 기반 스웜 구조는 지속적인 MAVLink 통신 링크를 전제로 하므로, 통신이 완전히 두절된 환경에서는 온보드 센서·칼만 필터 기반 분산 협업 방식으로 전환해야 임무 지속이 가능할 것으로 보인다.
- claim_type: inference
- supporting_sources:
  - [[swarm-modes]]
  - [[decentralized-swarm-gps-denied]]

## C5

- claim: 검색 결과에는 Paxos, gossip protocol 등 명명된 "분산 합의(consensus) 알고리즘"에 대한 구체적 기술 문서가 없어, 저대역/통신두절 환경에서 실제 사용되는 합의 알고리즘의 구체적 종류는 충분한 근거로 확인되지 않는다.
- claim_type: hypothesis
- supporting_sources:
  - [[decentralized-swarm-gps-denied]]
  - [[swarm-modes]]

## C6

- claim: Jetson 환경에서 YOLOv5/v8/v10 등 온디바이스 객체 감지 모델은 30-60+ FPS, YOLO-NAS는 40-80 FPS, RT-DETR은 20-40 FPS의 처리 성능을 보인다.
- claim_type: fact
- supporting_sources:
  - [[computer-vision-drone]]

## C7

- claim: Raspberry Pi 4 기반 실험에서 FL+KD 침입탐지 프레임워크는 통신 비용 약 70%, 계산 오버헤드 29% 감소를 달성해 리소스 제약 환경에서도 실용적 배포가 가능함을 보였다.
- claim_type: fact
- supporting_sources:
  - [[federated-lightweight-intrusion-detection]]

## C8

- claim: 드론 기반 연합학습에서 무선 연결 중단은 Non-IID 데이터 분포 조건에서 상당한 학습 불안정성을 유발하며, 단기적 무선 중단이 장기적인 학습 품질 저하로 확대될 수 있다.
- claim_type: fact
- supporting_sources:
  - [[chained-attacks-drone-fl]]

## C9

- claim: 온디바이스 비전 모델의 처리 성능(Jetson 30-80 FPS급)과 FL+KD 프레임워크의 저사양 하드웨어(Raspberry Pi 4) 실험 결과를 종합하면, 탑재 하드웨어의 연산 등급에 따라 실시간 인지와 협업 학습을 동시에 수행할 수 있는 임무 복잡도의 상한이 달라진다고 볼 수 있다.
- claim_type: inference
- supporting_sources:
  - [[computer-vision-drone]]
  - [[federated-lightweight-intrusion-detection]]

## C10

- claim: Recon Swarm Project는 4단계 로드맵 중 1단계(단일 기체 자율비행+센서 통합)만 진행 중이며 2~4단계(편대비행, 군집, GPS-denied 실내 군집)는 아직 계획 단계에 머물러 있다.
- claim_type: fact
- supporting_sources:
  - [[recon-swarm-project]]
  - ^[raw/articles/mastervault-recon-swarm.md]

## C11

- claim: GPS가 없거나 신뢰할 수 없는 환경에서 드론은 ORB-SLAM3, VINS-Fusion, RTAB-Map, LIO-SAM 등 다양한 SLAM/VIO 알고리즘을 통해 위치와 지도를 동시에 추정한다.
- claim_type: fact
- supporting_sources:
  - [[computer-vision-drone]]
  - [[visual-positioning-odometry]]

## C12

- claim: 마이크로 드론에서는 단안(monocular) 카메라와 관성 센서(IMU)만으로도 동시 위치추정 및 3D 준밀집(semi-dense) 매핑이 가능함이 실증되었다.
- claim_type: fact
- supporting_sources:
  - ^[raw/papers/drone-hw/danial2025-microdrone-slam.md]

## C13

- claim: ICD-Net은 관성 공분산 변위 네트워크를 딥러닝으로 학습해 시각-관성 SLAM의 상태추정 정확도를 개선하는 접근을 제시한다.
- claim_type: fact
- supporting_sources:
  - ^[raw/papers/drone-ai/shapira2025-icdnet.md]

## C14

- claim: Recon Swarm Project의 센서 스택(Optical Flow를 GPS-denied 위치추정용으로 채택)과 SLAM 알고리즘 분류를 종합하면, 실제 소형 군집 드론은 Optical Flow 기반 저수준 오도메트리와 VIO/SLAM 기반 고수준 매핑을 계층적으로 결합해 GPS 단절 항법을 구성하는 것으로 보인다.
- claim_type: inference
- supporting_sources:
  - [[recon-swarm-project]]
  - [[computer-vision-drone]]

## C15

- claim: Recon Swarm Project는 통신 두절 시 개별 기체의 독립 귀환, 이중 Geofence, 배터리 페일세이프(자동 RTL), 최소 이격거리 기반 충돌회피로 구성된 안전 시스템을 설계에 포함하고 있다.
- claim_type: fact
- supporting_sources:
  - [[recon-swarm-project]]
  - ^[raw/articles/mastervault-recon-swarm.md]

## C16

- claim: Cross-Layered Multi-Drone Coordination 연구는 CTDE(중앙집중식 학습·분산 실행) 기반 CEDA 알고리즘을 PX4 SITL 환경에서 X500 쿼드로터 2대로 검증했다.
- claim_type: fact
- supporting_sources:
  - [[cross-layered-medical-drone-coordination]]

## C17

- claim: Leader-Follower 구조가 MAVLink 링크에 의존하는 점과 CEDA가 "중앙집중식 학습, 분산 실행" 구조를 채택한 점을 종합하면, 완전 무통신 상황에서 임무를 지속하려면 사전에 학습·계획된 정책을 각 기체가 오프라인으로 독립 실행하는 방식이 통신 의존적 리더-팔로워 구조의 대안으로 요구된다.
- claim_type: inference
- supporting_sources:
  - [[swarm-modes]]
  - [[cross-layered-medical-drone-coordination]]

## C18

- claim: 검색 결과는 통신 두절 시의 "독립 귀환" 같은 개별 기체 페일세이프는 확인되나, 다수 기체가 사전 합의된 임무 계획을 무통신 상태에서 어떻게 시간·공간적으로 동기화해 실행하는지에 대한 구체적 알고리즘 설계는 확인되지 않는다.
- claim_type: hypothesis
- supporting_sources:
  - [[recon-swarm-project]]
  - [[swarm-modes]]

## C19

- claim: Decentralized UAV Swarms 연구는 GPS/통신 차단 조건에서의 분산 포위 기법을 실제 로봇으로 검증 완료했다고 명시한다.
- claim_type: fact
- supporting_sources:
  - [[decentralized-swarm-gps-denied]]

## C20

- claim: FL 기반 침입탐지 프레임워크와 체인 공격 연구는 각각 Raspberry Pi 4, Raspberry Pi/Jetson을 이용한 실제 하드웨어 테스트베드에서 검증되었다.
- claim_type: fact
- supporting_sources:
  - [[federated-lightweight-intrusion-detection]]
  - [[chained-attacks-drone-fl]]

## C21

- claim: Cross-Layered Multi-Drone Coordination의 CEDA 알고리즘 검증은 실제 비행이 아닌 PX4 SITL 시뮬레이션 환경에서 이루어졌다.
- claim_type: fact
- supporting_sources:
  - [[cross-layered-medical-drone-coordination]]

## C22

- claim: 검색 결과에서 확인되는 온디바이스 AI 군집 자율성 검증 사례는 소규모 실제 로봇 실험과 SITL 시뮬레이션 수준에 머물러 있어, 대규모 실전 군사·상업 배치 수준의 실증 사례는 현재 확보된 근거로는 확인되지 않는다.
- claim_type: hypothesis
- supporting_sources:
  - [[decentralized-swarm-gps-denied]]
  - [[cross-layered-medical-drone-coordination]]

## C23

- claim: FAA Part 107, EASA, 영국 CAA, 한국 국토교통부 등 각국 기관은 고도·속도·시야(VLOS) 등을 규정하는 드론 운용 규제 프레임워크를 운영한다.
- claim_type: fact
- supporting_sources:
  - [[drone-regulations]]

## C24

- claim: 2026년 7월 기준 영국 CAA는 저고도 공역 충돌 방지를 위한 Electronic Conspicuity 의무화를 협의 중이며, SESAR HAVEN 프로젝트는 AI·클라우드 기반 미래 항공교통관제 플랫폼을 개발하고 있다.
- claim_type: fact
- supporting_sources:
  - [[drone-news-regulations]]

## C25

- claim: 검색된 규제 동향(Electronic Conspicuity, SORA GOM, BVLOS Detect-and-Avoid)은 일반적인 공역 안전·가시성 규제에 초점을 두고 있으며, "통신 제한/두절 환경에서의 군집 드론 운용"에 특화된 규제나 정책은 검색 결과에서 확인되지 않아 외부 조사가 필요하다.
- claim_type: hypothesis
- supporting_sources:
  - [[drone-news-regulations]]
  - [[drone-regulations]]

## C26

- claim: Recon Swarm Project는 통신 두절 대응으로 개별 기체의 독립 귀환과 최소 이격거리 유지 기반 충돌 회피를 결함 완화 수단으로 설계에 포함한다.
- claim_type: fact
- supporting_sources:
  - [[recon-swarm-project]]
  - ^[raw/articles/mastervault-recon-swarm.md]

## C27

- claim: 드론 기반 FL 시스템에 대한 체인 공격 연구에 따르면, 802.11 deauthentication 공격으로 연결이 끊긴 드론의 자격 증명을 이용한 사칭이 가능하며, 단기 무선 중단이 장기적 학습 품질 저하로 확대될 수 있다.
- claim_type: fact
- supporting_sources:
  - [[chained-attacks-drone-fl]]

## C28

- claim: 분산형 UAV 군집은 상호 통신 없이도 칼만 필터로 상대 측정만을 이용해 UAV 및 표적 상태를 추정함으로써 개별 기체 간 통신 실패에 대한 강건성을 확보한다.
- claim_type: fact
- supporting_sources:
  - [[decentralized-swarm-gps-denied]]

## C29

- claim: 체인 공격 연구가 보이는 "단기 무선 중단의 장기적 학습 저하 확대"와 Recon Swarm Project의 개별 기체 중심 페일세이프(독립 귀환)를 종합하면, 개별 기체 단위의 안전 귀환 절차만으로는 협업 학습·의사결정을 수행하는 군집 전체의 성능 저하를 방지하기 어려우며, 군집 수준의 결함 허용 메커니즘이 별도로 필요하다.
- claim_type: inference
- supporting_sources:
  - [[chained-attacks-drone-fl]]
  - [[recon-swarm-project]]

## C30

- claim: 검색 결과에는 군집 규모 대비 허용 가능한 노드 탈락 비율이나 정족수(quorum) 기준 등 정량적 결함 허용 임계치에 대한 근거가 없어, 이 부분은 충분한 근거 없이 후속 조사가 필요하다.
- claim_type: hypothesis
- supporting_sources:
  - [[decentralized-swarm-gps-denied]]
  - [[chained-attacks-drone-fl]]
