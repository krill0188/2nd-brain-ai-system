---
title: "KH-Control: Stream Deck으로 Mission Planner 조작"
created: 2026-10-10
updated: 2026-10-10
type: concept
domain: gcs-software
tags: [drone, drone-sw]
sources: [inbox/processed/fetch-2026-10-10-yt-use-a-streamdeck-with-ardupilotmission-planner-using-kh-cont.md]
confidence: low
contested: false
contradictions: []
---

# KH-Control: Stream Deck으로 Mission Planner 조작

Painless360 영상(2026-10-09)이 소개한 Elgato Stream Deck용 플러그인 KH-Control(KH Unmanned)이다. 개발자는 ArduPilot 쪽 개발자 Pete로 소개되며, Stream Deck 버튼을 Mission Planner 기능에 매핑한다. 아래는 자막에 나온 내용이다. 단일 출처이고 시연 영상이라 confidence는 low다.^[inbox/processed/fetch-2026-10-10-yt-use-a-streamdeck-with-ardupilotmission-planner-using-kh-cont.md]

## 동작 방식

- 플러그인이 **Mission Planner websocket**에 연결하고(연결 버튼이 녹색으로 바뀜), 기체 유형별 페이지(copter, plane, VTOL)를 쓴다. 기체 유형에 맞는 비행 모드 버튼만 활성화돼 잘못된 모드 설정을 막는다.
- 버튼 예: 비행 모드, arm/disarm, safety on/off, VTOL 이륙, guided 미션 일시정지/재개, 속도·웨이포인트 번호 설정, aux 기능, 비행 전 airspeed 캘리브레이션.
- **오조작 방지 설계**: Alt Hold처럼 파일럿 조작 모드는 두 번 눌러야 하고, RTL은 한 번만 누른다.
- 버튼에 기체 상태(armed 여부, safety, 현재 모드)가 표시돼 메뉴를 뒤지지 않고 한눈에 확인한다.
- **커스텀 명령**을 지원해 내장 버튼이 없는 기능(예: 일부 짐벌 동작)도 설정한다. 내장 카메라 액션은 NextVision 전용이며, 다른 짐벌 지원 추가는 수요에 달렸다고 한다.

## 요건·비용

- 6키, 15키, XL 모델에서 모두 동작한다. 작은 모델은 페이지를 나눠 쓰고, 개발자는 키가 많은 모델을 권한다.
- 플러그인은 Elgato 마켓플레이스에서 £50(자막 기준)에 판매되며 Stream Deck 하드웨어가 따로 필요하다.

## 관련 개념

- [[mission-planner]] — 대상 GCS
- [[ardupilot]] — 지원 비행 스택
- [[ground-control-station]] — GCS 개요

## 📰 최근 관련 소식
- [Painless360] Use a StreamDeck with Ardupilot/Mission Planner (Using KH-Control) (youtube.com, 2026-10-09) — https://www.youtube.com/watch?v=SUOT5BBDcYU
