---
title: "6G ISAC: MATLAB/USRP 기반 구현"
created: 2026-08-04
updated: 2026-08-04
type: concept
tags: [datalink, 6g, isac, simulation]
domain: comms-protocol
sources: [inbox/fetch-2026-08-04-yt-6g-isac-implementation-with-matlab-and-usrp.md]
confidence: high
contested: false
contradictions: []
---

# 6G ISAC: MATLAB/USRP 기반 구현

통합 감지 및 통신(Integrated Sensing and Communication, ISAC)은 6G의 핵심 기술로, 단일 파형으로 데이터 전송과 레이더 감지를 동시에 수행한다.

## 구현 환경

- **도구**: MATLAB, Simulink, Wireless Testbench
- **하드웨어**: NI USRP FPGA
- **파형**: 6G 후보 OFDM 파형 (100MHz 대역폭)

## 핵심 기술

### 타겟 에뮬레이터
- 설정 가능한 지연, 도플러 시프트, 이득 적용
- 이동하는 표적을 나타내는 현실적인 레이더 반사 생성
- 하드웨어 인더 루프(HIL) 환경에서 반복 가능한 테스트 제공

### 채널 추정
- 통신 및 감지를 위한 채널 추정
- 100MHz 대역폭에서의 성능 검증

## 관련 개념

- [[datalink-communication]] — 드론 데이터링크 통신
- [[uav-isac-cross-region]] — UAV ISAC 교차 지역 협력

## 📰 최근 관련 소식
- [MATLAB] 6G ISAC Implementation with MATLAB and USRP (youtube.com, 2026-08-03) — https://www.youtube.com/watch?v=20bb37XtbIk
