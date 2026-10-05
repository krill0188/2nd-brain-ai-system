---
id: idea-004
title: "FPV FC 펌웨어 3종(Betaflight/INAV/ArduPilot) 정량 벤치마크: 정성적 포지셔닝의 실측 검증"
status: draft
created: 2026-10-01
updated: 2026-10-01
gaps: [GAP-001]
sources: [comparisons/fc-firmware-comparison.md]
novelty_confidence: 0.45
---

> ⚠ 미검증 연구 아이디어 — canonical 아님

## Hypothesis

동일 기체(동일 프레임·모터·ESC·IMU)에 Betaflight·INAV·ArduPilot 세 펌웨어를 순차 적용해 세 가지
대표 임무 프로파일(레이싱 게이트 통과, 장거리 웨이포인트 자동복귀, 정밀 호버링 자세유지)에서
루프 지연시간·자세제어 RMSE·배터리 소모를 측정하면, "Betaflight=레이싱, INAV=장거리, ArduPilot=
정밀자율"이라는 현재 위키의 정성적 포지셔닝이 정량 지표에서도 각 펌웨어가 자신의 "주 용도" 임무에서
다른 두 펌웨어를 유의하게 앞서는 형태로 확인될 것이다 — 단, 배터리 소모만큼은 스택 무게/연산량에
비례해 ArduPilot이 세 임무 전반에서 가장 높을 것으로 예상한다.

## Why now (근거 요약)

[[fc-firmware-comparison]]은 세 펌웨어의 주 용도·특징을 표로 정리했지만 "레이싱/프리스타일→
Betaflight, 장거리/자율→INAV, 산업/정밀자율→ArduPilot"이라는 포지셔닝은 전적으로 정성적 서술이며
수치화된 벤치마크가 없다 ^[inbox/fetch-2026-08-09-rss-oscarliang-fpv.md]. GAP-001로 원장에
등재되어 있으며, resolution_condition은 "동일 기체·동일 임무 조건에서 세 펌웨어의 지연시간·자세제어
정확도·배터리 소모를 정량 비교한 벤치마크 데이터"다.

## Novelty Ledger

### Known Similar Work
- [[fc-firmware-comparison]] — 용도별 포지셔닝 표(정성적, 수치 없음).
- [[ardupilot-architecture]] — ArduPilot 아키텍처 설명(개별 펌웨어 내부 구조, 타 펌웨어와의 비교
  없음).

### What already exists
- 세 펌웨어 각각의 설계 철학·목표 사용자층에 대한 커뮤니티 수준 정성적 합의.

### What appears missing
- 동일 하드웨어·동일 임무 조건에서 지연시간(ms)·자세제어 RMSE·배터리 소모(mAh/min)를 세 펌웨어
  간 나란히 비교한 실측 데이터.
- "주 용도 임무에서 해당 펌웨어가 실제로 우위를 보이는가"를 직접 검증한 사례.

### Potential novelty
- FPV/자율비행 커뮤니티에 널리 퍼진 정성적 통념을 통제된 3-way 실측 벤치마크로 검증(또는 반증)하는
  최초 시도가 될 수 있음. 특히 "배터리 소모는 스택 무게에 비례해 ArduPilot이 전반적으로 높다"는
  세부 가설은 원 자료에 전혀 언급되지 않은 축.

### Threat to novelty
- 펌웨어 버전이 빠르게 갱신되므로(예: Betaflight 2026.6 FC Alignment Wizard 추가) 벤치마크 결과의
  유효기간이 짧음 — 측정 시점의 펌웨어 버전을 명시해야 재현성 확보 가능.
- FPV 애호가 커뮤니티(Oscar Liang, RCGroups, Joshua Bardwell 채널 등)에서 유사한 벤치마크가 이미
  수행됐을 가능성이 상당히 높음 — 위키 내에는 확인되지 않으나 위키 밖 문헌 미검색 상태이므로
  novelty_confidence를 중간 이하로 제한.

### Novelty confidence
0.45 — 위키 내 정량 비교 부재는 명확하나, FPV 커뮤니티의 비공식 벤치마크 관행을 고려하면 위키 밖에
유사 사례가 존재할 가능성이 다른 아이디어 대비 높음.

## Evidence Status

2026-10 근거 1편([[fc-firmware-comparison]], GAP-001) → 신규 생성. 재평가 대상 없음(첫 등재).

## Minimal validation plan

1. 동일 프레임/모터/ESC/IMU 하드웨어에 세 펌웨어를 순차 플래시할 수 있는 단일 테스트베드 구성
   (또는 동형 기체 3대에 각각 고정 플래시).
2. 3개 임무 프로파일 정의: (a) 레이싱 게이트 통과 랩타임+반응성, (b) 장거리 웨이포인트 자동복귀,
   (c) 정밀 호버링 자세유지.
3. 각 펌웨어×임무(9개 조합)에서 블랙박스 로그 기준 루프 지연시간, 목표 자세 대비 자세제어 RMSE,
   배터리 소모(mAh)를 측정.
4. 결과를 레이더 차트로 정리해 "정성적 포지셔닝"과 "실측 트레이드오프"의 일치/불일치 구간을 식별.
