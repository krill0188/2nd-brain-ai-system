---
title: "OpenDrone — 완전 오픈소스 드론 하드웨어 프로젝트"
created: 2026-10-05
updated: 2026-10-05
type: concept
domain: hardware
tags: [drone, drone-hw, fpv, hardware]
sources: [inbox/processed/fetch-2026-10-05-yt-his-audacious-plan-to-open-source-every-part-of-a-drone-open.md]
confidence: low
contested: false
contradictions: []
---

# OpenDrone — 완전 오픈소스 드론 하드웨어 프로젝트

Joshua Bardwell이 OpenDrone의 CEO·공동창업자 Stan Kuna와 나눈 대화(2026-10-03 영상, 자막 앞부분 8000자 기준)에서
정리한 내용이다. 자막은 중간에서 끊겨 있어 이후 논의는 반영하지 않았다. 단일 인터뷰이며 제작사 주장이 포함된다.
^[inbox/processed/fetch-2026-10-05-yt-his-audacious-plan-to-open-source-every-part-of-a-drone-open.md]

## 목표

- Betaflight·INAV·ExpressLRS 등 소프트웨어는 오픈소스지만 FC·ESC 같은 **하드웨어 참조 설계는 없다**는 문제의식.
- 프레임 CAD, PCB 레이아웃·부품, 코드까지 드론의 모든 부분을 공개하고 판매도 병행한다. 현재 5인치 드론 제작에 필요한
  FC·ESC·수신기·프레임·모터 라인을 갖췄고 이후 다른 드론 유형으로 확장할 계획이라고 한다.

## ESC 설계 논점 (인터뷰이 발언)

- ESC는 표준적인 설계이며 차별점은 부품 선정과 레이아웃. 표준 MOSFET(내압 40 V), 게이트 드라이버, MCU 구성.
- ESC 소손 원인은 배터리 레일 전압 스파이크라는 주장. 완화는 정전용량 증가 또는 고내압 부품. TVS 다이오드는
  MOSFET 한계 전에 동작시키기 어려워 효과가 없다고 보고, 차기 버전에서 TVS를 빼고 커패시터를 늘렸다고 한다. 6S는 문제없고
  8S에서도 시험했다고 언급.
- 30×30(대형)과 20×20(소형) ESC. 소형은 6S 한정. 전류 정격은 소형 약 40 A/모터(양호한 냉각 시), 대형 60~70 A라고 주장.
- 전류 정격은 결국 열 한계이며 업계가 측정 조건(냉각·지속 시간)을 공개하지 않아 비교가 어렵다는 점에 두 사람이 동의.
  5인치 실사용 피크는 약 40 A 수준이라는 진행자의 언급.
- MCU는 STM32가 아닌 Raspberry Pi Pico 계열이 사용됨. 부품 수급난(MCU·OSD·IMU)으로 제조사들이 대체 부품을
  찾는 상황이 배경으로 언급되었다.

## 한계

실측 성능 데이터는 자막 범위에 없고 정격은 모두 제작사 구두 주장이다.

## 관련 개념

- [[flight-controller-hardware]] — FC 하드웨어 일반
- [[fpv-hardware]] — FPV 하드웨어 맥락
- [[betaflight]] — 언급된 오픈소스 FC 펌웨어

## 📰 최근 관련 소식
- [Joshua Bardwell] His audacious plan to open-source EVERY PART of a drone // OPENDRONE (youtube.com, 2026-10-03) — https://www.youtube.com/watch?v=MVr2Vm_6CqQ
