---
title: Drone Hardware Overview
created: 2026-08-06
updated: 2026-08-06
type: concept
tags: [drone-hw]
sources: []
confidence: medium
contested: false
contradictions: []
domain: hardware
---

# Drone Hardware Overview

드론 하드웨어 스택 전반을 아우르는 도메인 개요 페이지. Flight Controller, 센서, 모터/ESC, 배터리, 통신, 페이로드 등 물리적 구성요소를 다룬다. 세부 항목은 각 하위 개념 페이지를 참조한다.

## 구성 레이어

| 레이어 | 대표 구성요소 |
|---|---|
| 비행 제어 | Flight Controller(Pixhawk 계열), IMU, 바로미터, GPS/RTK |
| 동력 | BLDC 모터, ESC, LiPo 배터리, PDB |
| 통신 | RC 수신기, 텔레메트리 라디오, 데이터링크 |
| 컴퓨팅 확장 | 컴패니언 컴퓨터(Jetson, RPi) |
| 페이로드 | 카메라, 짐벌, 센서 페이로드 |

## 관련 개념

- [[flight-controller-hardware]] — FC/센서/전원 등 하드웨어 상세 레퍼런스
- [[companion-computer]] — AI 추론·오프보드 처리용 보조 컴퓨터
- [[px4-system-architecture]] — FC 소프트웨어와 하드웨어의 결합 구조

## 제품/부품 사례

- [[divimath-4w-analog-vtx]] — Divimath 4W 아날로그 FPV VTX
- [[dji-matrice-5-rumor]] — DJI Matrice 5 루머
- [[dji-mic-mini-2s]] — DJI 무선 마이크 시스템
- [[dji-osmo-pocket-4p-dlog2]] — DJI Osmo Pocket 4P D-Log 2
- [[emlid-corrections]] — Emlid Reach RTK 보정 서비스
- [[hglrc-talon-cinewhoop]] — HGLRC Talon 시네후프
- [[hoverair-versa]] — HoverAir Versa 자율 촬영 드론
- [[radial-impeller-drone]] — 방사형 임펠러 추진 드론
- [[rtk-gps-precise-landing]] — RTK GPS 정밀 착륙
- [[event38-tb2-drops-integration]] — Event 38 TB2 드롭 통합
- [[ideaforge-yeti-heavy-lift]] — ideaForge Yeti 중량물 리프트 드론
- [[wallefpv]] — FPV 드론 하드웨어 제조업체
- [[6g-isac-matlab-usrp]] — 6G ISAC MATLAB/USRP 구현
- [[sol-one]] — 벨기에 자율 드론 시스템 기업
- [[eve-air-mobility-transition]] — eVTOL 도심항공모빌리티 전환

## 📰 최근 관련 소식
- [DJI] Munch. Crunch. Repeat. 🍃｜DJI Mic Mini 2S (youtube.com, 2026-08-10) — https://www.youtube.com/watch?v=E-Pg5OWkidU
