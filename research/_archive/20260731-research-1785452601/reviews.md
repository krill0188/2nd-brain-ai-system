# 검토 (Critic + Verifier)

## C1

- opposing_sources: 없음
- limitations: 원문이 "Master (personal dev notes)" 저작의 개인 정리 자료이며 공식 제조사 데이터시트가 아니므로, 프로세서 사양(STM32 계열) 표기에 오탈자·구버전 정보 혼입 가능성이 있음. 공식 Holybro/PX4 문서 대조 없이는 세부 모델명(예: STM32H7 vs H743) 확정 불가.
- confidence: high
- verification_status: grounded

## C2

- opposing_sources: 없음 (검색 결과 자체가 "부재"를 근거로 하는 주장이라 상충 근거를 낼 수 없음)
- limitations: 검색 결과는 논문의 요약/발췌본이며 전체 본문이 아니므로, 실제 논문에는 실행 플랫폼 벤치마크(FPS, 지연시간)가 포함되어 있으나 발췌에만 빠졌을 가능성을 배제할 수 없음. "검색 결과에 나타나지 않는다"는 "존재하지 않는다"와 다름 — 부재의 증거가 아니라 증거의 부재.
- confidence: low
- verification_status: grounded

## C3

- opposing_sources: 일반적으로 알려진 사실: Jetson Orin Nano/NX 계열은 공식 스펙상 최대 20~100 TOPS급 성능을 제공하며 다수의 온보드 VIO/SLAM 파이프라인(VINS-Fusion 등)이 이 플랫폼에서 실시간 구동된 사례가 산업계에 존재한다. 다만 이는 검색 결과가 아닌 외부 일반 지식이므로 이 세션의 근거로는 채택 불가.
- limitations: `claim_type: hypothesis`이므로 원칙상 high 부여 불가. 또한 마스터의 실제 개발 환경(Intel 듀얼코어 Mac)은 저사양이라 Jetson 벤치마크를 로컬에서 직접 재현·검증하기 어렵고, 시뮬레이션 기반 간접 검증에 의존해야 하는 현실적 제약이 있음.
- confidence: low
- verification_status: grounded

## C4

- opposing_sources: 없음
- limitations: 문서 존재 여부는 사실이나, 문서 내용의 최신성·정확성(작성일 기준 최신 연구 반영 여부)은 별도 검증 필요.
- confidence: high
- verification_status: grounded

## C5

- opposing_sources: 없음
- limitations: "Ground Station을 포함하는 구조"가 곧 "데이터링크 통신 전제"라는 연결은 타당하나, 이는 설계도상 구조에서 도출한 추론이며 실제 구현체가 완전 오프라인/두절 모드를 별도 지원하지 않는다고 단정할 근거는 없음. `mastervault-swarm-architecture` 원문에 "완전 무통신 시 폴백 모드"가 별도 명시돼 있는지는 발췌만으로 확인 불가.
- confidence: medium
- verification_status: grounded

## C6

- opposing_sources: 없음 (직접적 상충 근거는 검색 결과에 없음)
- limitations: 일반적으로 알려진 사실: Reynolds boids 모델·인공 포텐셜 필드 기반 분산 군집 알고리즘은 학계에 존재하지만, 이들 대부분은 국소 센싱(카메라/LiDAR 상호 인식)이나 최소한의 근거리 통신(UWB, 광학 마커)에 의존하며, "완전 무통신" 조건에서의 실험적 검증은 여전히 활발한 연구 주제로 남아있음. 즉 완전한 부재라기보다 "이 세션 검색 범위 내 부재"로 한정해야 함. `claim_type: hypothesis`이므로 high 불가.
- confidence: low
- verification_status: grounded

## C7

- opposing_sources: 없음
- limitations: 논문 초록/메타데이터 발췌 수준의 확인이며, arXiv ID(2402.07537)·DOI 표기가 소스에 명시되어 사실 검증 신뢰도는 높음. 다만 "3D 장면 그래프 재구성"이 논문의 핵심 기여인지 부가 실험인지는 발췌만으로 완전히 구분되지 않음.
- confidence: high
- verification_status: grounded

## C8

- opposing_sources: 없음
- limitations: arXiv ID(2512.00037)가 2025년 12월 등록분으로 표기되어 있어 현재 시점(2026-07-31) 기준 프리프린트로서는 시간상 정합적이나, peer-review 통과 여부(정식 게재본 여부)는 확인되지 않음.
- confidence: high
- verification_status: grounded

## C9

- opposing_sources: 없음
- limitations: 두 논문을 동일하게 "학술논문/프리프린트 단계"로 묶었으나, `radwan2024`는 IEEE ICUAS 2024 정식 학회 발표논문(peer-reviewed, DOI 존재)이고 `shapira2025`는 arXiv 프리프린트(미검증)로 성숙도 단계가 다름 — 두 연구를 동일 선상에 놓고 "실용화 여부 불명"으로 뭉뚱그리는 것은 다소 과도한 단순화. 또한 상용 배치 여부는 방산/군사 분야 특성상 비공개(classified)일 수 있어 검색 결과 부재가 곧 미배치를 의미하지 않음.
- confidence: medium
- verification_status: grounded

## C10

- opposing_sources: 없음
- limitations: 문서 존재는 사실이나 내용 최신성 검증 별도 필요.
- confidence: high
- verification_status: grounded

## C11

- opposing_sources: 없음
- limitations: MAVLink/ArduPilot 엔티티 문서가 재분배 로직을 "언급하지 않는다"는 것은 해당 발췌(개요 수준 레퍼런스 문서) 범위 내 관찰이며, ArduPilot 소스코드나 별도 군집 모듈(예: Swarm Manager, DroneKit 기반 커스텀 로직) 문서까지 전수 검색한 결과는 아님. 일반적으로 알려진 사실: 군집 재할당은 대부분 애플리케이션 레이어(미션 플래너/커스텀 스크립트)에서 구현되며 프로토콜 자체 표준 기능이 아니므로, MAVLink/ArduPilot 문서에 없는 것이 당연할 수 있음 — 이는 "검색 실패"라기보다 "본래 다른 계층의 책임"일 가능성.
- confidence: low
- verification_status: grounded

## C12

- opposing_sources: 없음
- limitations: 검색된 canonical 문서(`knowledge-tool-roles`, `ai-knowledge-workflow`)가 주제 불일치라는 지적은 타당함. 다만 일반적으로 알려진 사실: 컴패니언 컴퓨터(Jetson 등) 추가 시 전력 소모 증가로 체공시간이 통상 10~20% 내외 감소한다는 것은 업계에 널리 알려진 트레이드오프이나, 이는 이 세션 검색 결과에 없는 외부 지식이므로 근거로 사용 불가. `claim_type: hypothesis` 특성상 high 불가.
- confidence: low
- verification_status: grounded

## C13

- opposing_sources: 없음
- limitations: 뉴스 검색 결과에 제목과 URL만 확인되고 기사 본문 내용은 발췌되지 않아, "실전 데이터+AI" 기반이라는 세부 서술이 제목 이상의 근거로 뒷받침되는지는 본문 확인이 필요함. 제목 자체는 검색 결과에 정확히 일치.
- confidence: high
- verification_status: grounded

## C14

- opposing_sources: 없음
- limitations: 기사 본문을 읽지 않고 제목만으로 "성숙도 격차"를 추론한 것은 근거가 얕음. 또한 `mastervault-recon-swarm`이 스스로 "학술연구 기반"이라 명시한 것과 실전 사례 간 비교는 서로 다른 개발 단계(연구 vs 실전배치)를 비교하는 것이어서 유의미하나, 이는 이중 추론(기사 해석 + 프로젝트 문서 해석)에 기반한 2차 추론이라 불확실성이 누적됨.
- confidence: low
- verification_status: grounded

## C15

- opposing_sources: 없음
- limitations: 문서 존재 자체는 사실이나, 규제 문서(`drone-regulations`)가 다루는 범위(국내/해외, 최신 개정 여부)는 검증되지 않음.
- confidence: high
- verification_status: grounded

## C16

- opposing_sources: 없음
- limitations: 일반적으로 알려진 사실: 한국 항공안전법 및 시행규칙상 무인비행장치의 비가시권(BVLOS) 비행이나 자율 임무 수행은 국토교통부 특별승인을 요구하며, 통신 두절 상태에서의 완전 자율 임무 수행은 현행 규제 프레임워크에서 명확히 다뤄지지 않는 회색지대로 알려져 있음 — 다만 이는 이 세션 검색 결과가 아닌 외부 일반지식이므로 그대로 사실 근거로 채택할 수 없고, 별도의 법령 원문 조회(예: `korean-law-advisor` 에이전트)가 필요함. `claim_type: hypothesis` 특성상 high 불가.
- confidence: low
- verification_status: grounded
