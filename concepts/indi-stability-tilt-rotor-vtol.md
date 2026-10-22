---
title: "INDI Pitch-Rate Controller Stability Analysis for Tilt-Rotor VTOL UAV"
created: 2026-07-30
updated: 2026-10-21
type: concept
tags: [drone, flight-control, indi, tilt-rotor, vtol, stability]
sources: [inbox/fetch-2026-07-30-arxiv-linear-stability-analysis-of-an-indi-pitch-rate-controller-u.md, raw/papers/_unclassified/linear-stability-analysis-of-an-indi-pitch-rate-controller-under-model-mismatch-.md, inbox/processed/fetch-2026-10-21-arxiv-design-of-a-flying-humanoid-robot-based-on-thrust-vector-con.md]
confidence: high
contested: false
contradictions: []
domain: flight-control
ontology_class: VTOL
---

# INDI Pitch-Rate Controller Stability Analysis for Tilt-Rotor VTOL UAV

틸트로터 수직 이착륙(VTOL) UAV를 위한 증분 비선형 동적 역전(INDI) 피치 레이트 컨트롤러의 모델 불일치 하에서의 선형 안정성 분석. Routh-Hurwitz 기준을 통한 매개변수 명시적 안정성 특성화.

## INDI의 장점

- **완전한 공기역학 모델에 대한 의존성 감소**
- **강력한 외란 제거 능력 유지**

## 연구 범위

기존 캐스케이드 INDI 컨트롤러의 피치 레이트/엘리베이터 서브채널 격리 분석:
- 선형 안정성 특성화
- 매개변수 명시적 안정성 영역 도출

## 안정성 분석 방법

### 1. 전달 함수 도출
- 5차 전달 함수 (컨트롤러-추정기-액추에이터-플랜트 상호연결)
- Routh-Hurwitz 기준 적용

### 2. 매개변수 스윕
- 3개 매개변수 조합에 대한 해석 가능한 안정성 영역 생성

## 주요 발견

| 불일치 유형 | 안정성 영향 |
|-------------|-------------|
| 액추에이터 지연 | 비교적 양호 (정격 이득에서) |
| 관성 불일치 | 비교적 양호 (정격 이득에서) |
| 제어 효과 불일치 | **가장 위험한 비안정화 요인** |
| 부호 오류 | 치명적 (할당에서) |

## 튜닝 절차 제안

### 1. 견고성 중심 설계
- 최소 이득 여유 및 위상 여유의 가중 최악 조합 최대화

### 2. 성능 중심 설계
- 여유 제약 조건 하에서 최악 케이스 폐쇄 루프 대역폭 최대화

## 시사점

- 보수적 운용 조건을 위한 구체적인 튜닝 권장사항
- 공격적 운용 조건을 위한 구체적인 튜닝 권장사항

## 관련 페이지

- [[px4-flight-modes]] — PX4 비행 모드 및 제어 파라미터
- [[px4-architecture-deep]] — PX4 아키텍처 및 제어 시스템
- [[drone-safety-failsafe]] — 드론 안전 및 페일세이프 시스템
- [[kci-vtol-swarm-takeoff-landing-operation]] — VTOL 군집의 천이·역천이 운용 절차(제어기가 아닌 운용 관점)

## 최신 근거 연결 (2026-10-21)

- 추력 방향 제어로 자세를 안정화하는 다른 사례: Jet-HR2 비행 휴머노이드는 발의 덕티드 팬 자세를 바꿔 추력 벡터를 제어함으로써 이륙 중 회전·다이브를 억제했고, 추력 대 중량비 1.17에서 이륙에 성공했다(초록 기준, 제어기 구조가 달라 INDI와 직접 비교는 불가): [[jet-hr2-flying-humanoid-thrust-vectoring]]^[inbox/processed/fetch-2026-10-21-arxiv-design-of-a-flying-humanoid-robot-based-on-thrust-vector-con.md]

## 📰 최근 관련 소식
- [UAV Coach] Drone Prices Are About to Jump (youtube.com, 2026-08-15) — https://www.youtube.com/watch?v=FEiY1ONxd70
- [UAV Coach] 40+ Drones Disrupt Fire Response in Washington (youtube.com, 2026-08-14) — https://www.youtube.com/watch?v=Xo74V_HZBuM
- Air Force, Army Team Up for Counter-Drone Testing at Joint Base Andrews in Collaboration with JIATF-401 (jba.af.mil, Tue, 24 Ma) — https://news.google.com/rss/articles/CBMi1wFBVV95cUxQNWJsUWZsdTNpMDFqdy1OUk92cGY3dFhLZ3p6a0p3VjRFZ2FOdUJUTWFLUjQ4MmhvVF9DWE1vWTZuek5UQTJVbUF2QkNSWHlaM1A4V0RGUG9VRUc1eDJ6TFlWUy1ZOTJoRjRxVVZtdXlpS1daOXNfTlowZ1UwcXJyQVpWWndLVWZ1RnZSU0JRUzVldDBQV0hOVm43bGdUV2d0SXFQLWk2R1lFZzhOY1dyY1NyZlpkQ1VhYVdMSE14NWJlQ0hib2VkXzVSYVFrLXJzblpsblJBdw?oc=5
- Army Formations Need to Prioritize Drone Dominance (Association of the United States Army, Fri, 31 Ju) — https://news.google.com/rss/articles/CBMigwFBVV95cUxPNjhUSXNQd01IdnFMT19rX0hPbFBrMlM4N0hVRVk3SGxJbldweHAyU2xXSlRwM2RVUmFkRV9xRkZ5a2dEY3RjUXZzVEJlbjBoWFFhRXktY2FQckV6aW5pbHRPcVg4aEtNRGtzdmNwWTZSUDNSeDg0UW5ZUDNPUHdLbnVlTQ?oc=5
- [UAV Coach] Drone Prices Are About To DOUBLE (youtube.com, 2026-08-21) — https://www.youtube.com/watch?v=3lAYXJQyK3w
- Purple UAS Opens Certification Portal for Public Safety Drone Manufacturers (www.suasnews.com, Fri, 21 Au) — https://www.suasnews.com/2026/08/purple-uas-opens-certification-portal-for-public-safety-drone-manufacturers/
- [UAV Coach] Is It Still Worth Starting a Drone Business Today? (youtube.com, 2026-08-20) — https://www.youtube.com/watch?v=Am5-N5FF26A
- [Painless360] Do I really need a compass on my flight controller? (youtube.com, 2026-08-25) — https://www.youtube.com/watch?v=pOs855esffs
- [Joshua Bardwell] Build a $125 Cheap AliExpress 7" Drone with me (youtube.com, 2026-09-04) — https://www.youtube.com/watch?v=vuYEK0POxi0
- [UAV Coach] I Use These 4 Apps on EVERY Drone Flight (youtube.com, 2026-09-11) — https://www.youtube.com/watch?v=Y9bZebPQRvI
- [Joshua Bardwell] Why I paid $60 for this AMAZING cable (I'm stupid) (youtube.com, 2026-09-14) — https://www.youtube.com/watch?v=kagyXl1lvtA
- One year in, America’s counter-drone task force still has ‘a ton of work to do’ (DefenseScoop, Mon, 24 Au) — https://news.google.com/rss/articles/CBMisgFBVV95cUxORThPZklYSTRJS2hZZkF6UXNsRnhOMV9EVWIyLW1vQ29tTEhSVzBKX2ZScHVqbWxlVzRWR3Rhdmh2WkExaEVBTEN3Y0hKaXZhSDFTZjRTbHdicnNvYV9XbURwRGJvODEzMWEzWTFHMUFnemNienFLRHktYWVfRTlRU01PTjVFZmRMdUNuMDFNWl9GbzNob0JPU2M5eFpwS09kcUpLTjdTUEhFMmhURjFUeXpB?oc=5
- [Joshua Bardwell] His audacious plan to open-source EVERY PART of a drone // OPENDRONE (youtube.com, 2026-10-03) — https://www.youtube.com/watch?v=MVr2Vm_6CqQ
- [Joshua Bardwell] Building a P1 whoop to find out how much slower it really is (youtube.com, 2026-10-06) — https://www.youtube.com/watch?v=ZrNlxbI4rlQ
- [Joshua Bardwell] This "durable" drone is awful // Axisflying Bando 5 (youtube.com, 2026-10-14) — https://www.youtube.com/watch?v=Mo15TyjLqgs
- [UAV Coach] Why Does Flying a Drone Feel Illegal? (youtube.com, 2026-10-15) — https://www.youtube.com/watch?v=xmBoKb3wh1U
- [Joshua Bardwell] I Exploded a LiPo in a $600 Safe (It Shot Flames) (youtube.com, 2026-10-17) — https://www.youtube.com/watch?v=H_eHspF-6KM
- Team UAV Completes 500 Transformer Drone Inspections for National Grid Electricity Distribution (dronelife.com, Wed, 21 Oc) — https://dronelife.com/2026/10/21/team-uav-completes-500-transformer-drone-inspections-for-national-grid-electricity-distribution/
- Best Drones For Beginners In 2021 - SlashGear (news.google.com, Fri, 18 Fe) — https://news.google.com/rss/articles/CBMidkFVX3lxTE1PamhMc1RZRVhhQlMwejMweHJiTU8zU1pYX3lXU3FFWWM2NFBHZzhRWXdJMVZielVncXpkOEVHMHk4X0J6T01lV2VfcGhKWVhzT0tZb2tOUnQtTWZtY2Eta1FXX215eTNiSHNabFYwUEVoWlJiR2c?oc=5
