---
title: "Precise 6D RTK Positioning System for UAV-based Near-Field Antenna Measurements"
created: 2026-10-22
captured: 2026-10-22
type: paper
domain: hardware
source: https://anavs.de/wp-content/uploads/2020/09/EUCAP2020.pdf
tags: [drone, gnss, 3-설치환경, uav, rtk, attitude, multipath, antenna]
authors: "Patrick Henkel, Andreas Sperl, Ulrich Mittmann, Torsten Fritzel, Rüdiger Strauss, Hans Steiner (ANavS GmbH / AeroXess UG)"
published: "EuCAP 2020 (게재일 2020-09 업로드)"
---

## 핵심 내용
ANavS 다중센서 RTK 모듈(GNSS 수신기 3개+MEMS IMU+기압계)을 AeroXess UAV에 탑재해 위치와 자세(3개 안테나로 기선 2개)를 RTK/INS 밀결합으로 추정한 논문. 안테나는 Tersus 고이득·멀티패스 억제 다주파 안테나 3개를 로터 블레이드 위에 장착했다. 초록: 정지·동적 조건에서 센티미터급 위치 정확도를 달성.

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 안테나를 로터 블레이드 위에 설치(논문 구성). 기체가 기울어지면 위상 멀티패스가 증가해 자세 잔차가 커진다고 서술.
- 고정 위상 잔차: 자세 기선은 대부분 2 cm 이하, RTK 기선은 대부분 5 cm 이하(그림 설명). 지상 궤적 노이즈는 약 2 cm 수준.
- 비행 중 잔차가 정지 초기화 때보다 큼: 수신기 추적 루프 대역폭 적응 때문이라고 서술.
- 자세 기선 모호정수는 기선 길이 제약과 상대 방향 제약으로 빠르게 고정.

## 한계·미확인
RTK 기준국과의 거리·초기화 시간은 열람 범위에서 수치 미확인. 로터 블레이드 위/아래 비교 실험은 없음(단일 구성). 제조사(ANavS) 소속 저자.
