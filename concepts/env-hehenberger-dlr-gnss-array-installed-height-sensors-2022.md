---
title: "Design and Installed Performance Analysis of a Miniaturized All-GNSS Bands Antenna Array for Robust Navigation on UAV Platforms"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: hardware
tags: [drone, gnss, 안테나-장착높이, choke-ring, multipath, 정량]
sources: [inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]
confidence: medium
contested: false
contradictions: []
---

# Design and Installed Performance Analysis of a Miniaturized All-GNSS Bands Antenna Array for Robust Navigation on UAV Platforms

- 원문: https://doi.org/10.3390/s22249645^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]
- 저자: Simon P. Hehenberger, Wahid Elmarissi, Stefano Caizzone^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]
- 발행: 2022-12-09 (Sensors 22(24), 9645, MDPI 오픈액세스)^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]

## 핵심 내용
DLR의 2x2 유전체 공진기 안테나 배열(지름 100 mm 접지판 위, 소자 간격 40 mm)을 헥사로터 UAV 위에 설치했을 때 설치 높이(안테나 접지판~기체 상면)와 수직 초크링이 패턴·다중경로에 미치는 영향을 전자기 시뮬레이션(기체를 완전 도체로 가정한 최악 조건)과 무반향실 측정, 24시간 야외 GNSS 측정으로 평가. 20261021의 EuCAP 2021 요약본(env-dlr-...)과 같은 팀의 저널판이며 이번에는 본문 전체를 읽었다.^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 시뮬레이션 설치 높이 h = 50 mm ~ 130 mm. 낮은 높이일수록 이득 패턴 리플과 후방 로브가 커지고 L5/E5a 대역에서 특히 두드러짐. 높이를 올리면 상반구 패턴이 매끈해짐.^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]
- 편파 순도: 축비(AR) 3 dB 이하 각도 범위가 h=50 mm에서 θ<50도, h=110 mm에서 θ<80도로 넓어짐.^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]
- 기체에 매우 가깝게(예: h=50 mm) 달아야 하면 초크링이 크게 유리, 높이를 확보할 수 있으면 초크링 생략 가능(저자 서술). h=110 mm에서는 초크링 개선이 중·고고도각에서 크지 않아, 중량 절감을 위해 초크링 없이 110 mm로 야외 측정을 진행.^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]
- 야외 24시간 측정: 안테나 단독 vs 헥사로터 장착(110 mm) — 대부분 하늘 영역에서 C/N0 40 dB-Hz 초과. 극저고도각에서는 장착 시 C/N0가 낮아짐(패턴의 방위각 진동). 반대로 L5/E5a에서 C/N0 진동은 장착 시 더 적음.^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]
- 근천저점(nadir) 방향 LHCP(교차편파)는 L5/E5a에서 단독 구성이 UAV 장착 구성보다 약 5 dB 높음 → 기체가 지면 다중경로를 일부 차폐. CMC로 추정한 100 s 평활 의사거리 다중경로는 L1/E1은 장착 시 약간 큼(주로 저고도각), L5/E5a는 장착 시 '눈에 띄게' 작음.^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]

## 한계·미확인
(1) 로터 근처 위치·모터 전자기 간섭·프로펠러 회전 효과는 이 논문에서 다루지 않음(측정 시 로터 가동 여부 서술 없음 → 미확인). (2) 시뮬레이션은 기체를 완전 도체로 가정한 최악 사례. (3) 정량 수치는 거의 그림(패턴·스카이플롯)으로만 제시되어 본문 텍스트에는 위 각도 범위·5 dB·40 dB-Hz 정도만 있음. (4) 연구용 4소자 배열이라 일반 패치 안테나로의 직접 환산은 미확인. 열람 범위: MDPI 본문 전체(Bright Data로 열람; WebFetch는 403). 신뢰도: 중상(동료심사 논문).^[inbox/processed/hw-20261022-env-hehenberger-dlr-gnss-array-installed-height-sensors-2022.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
