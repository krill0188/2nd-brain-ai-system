---
title: "드론 컴패니언·엣지 컴퓨터 제조사 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: vendor-registry
tags: [drone, drone-hw, company]
sources: [inbox/processed/hw-registry-20261017-vendors-compute.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 컴패니언·엣지 컴퓨터 제조사 레지스트리

드론 융합 HW의 컴패니언·엣지 컴퓨터 분야 제조사 17건을 공식 페이지/저장소 기준으로 정리한 레지스트리(2026-10-17 수집)다. 상위 개요는 [[drone-hw-vendor-registry]].

범위: 컴패니언/엣지 AI 모듈. 확인 방법: WF=WebFetch로 공식 페이지 열람(제품명은 페이지 기재분), WF-접근실패=접속 실패(제품 미확인). 국가/본사는 '(일반지식)' 표기 시 페이지 확인 아님. 기수집 제품 파일은 20261016/products/ 참조.


| 제조사 | 국가/본사 | 대표 제품군(공식 페이지에 적힌 것만) | 공식 URL | 확인 방법 | 비고 |
|---|---|---|---|---|---|
| NVIDIA (Jetson) | 미국(일반지식) | Jetson Thor T5000/T4000, AGX Orin, Orin NX, Orin Nano, AGX Xavier, Xavier NX, TX2, Nano | https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/ | WF | 모듈. 도입제약 문구 미확인 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Raspberry Pi | 영국(일반지식) | Compute Module 5/4/4S/Zero/3+/1, CM IO Board | https://www.raspberrypi.com/products/ | WF | 취미/개발 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| ModalAI | 미국(일반지식) | VOXL 2, VOXL 2 Mini (PX4/ArduPilot FC 내장) | https://www.modalai.com | WF | 'NDAA Compliant' 명시(FY2024 NDAA 1823-1833 등 인용) ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| ARK Electronics | 미국(일반지식) | ARK Just A Jetson, Jetson PAB(V3), Just A Pi, Pi6X, Modalix MLSoC 번들 | https://arkelectron.com | WF | NDAA 번들 판매(Jetson 3종) 표기 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Hailo | 이스라엘(일반지식) | Hailo-8L, Hailo-8, Hailo-8R, Hailo-10H 및 M.2/PCIe 모듈 | https://www.hailo.ai | WF | AI 가속기 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Seeed Studio | 중국(일반지식) | reComputer Mini J5012/J5011, Rugged J4012, J601 Carrier(Thor), RK3576 키트, reCamera Pro | https://www.seeedstudio.com | WF | Jetson 기반 완제품 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Connect Tech | 캐나다(일반지식) | Gauntlet Carrier(Jetson Thor), Boson(Orin NX) 캐리어 | https://connecttech.com | WF | 러기드 캐리어 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Auvidea | 독일(일반지식) | X242 AGX Thor Carrier, JNX120X Drone Carrier Board | https://www.auvidea.eu | WF | 드론용 캐리어 명시 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Luxonis | 미국(일반지식) | OAK 4, OAK 카메라/모듈 | https://www.luxonis.com | WF | 엣지 AI 카메라 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Khadas | 중국(일반지식) | VIM4, Edge 2, VIM3/VIM1S, Edge-V | https://www.khadas.com | WF | SBC ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Hardkernel | 한국(일반지식) | ODROID-H5, C5, C4, N2+, M1, M1S, M2 | https://www.hardkernel.com | WF | SBC ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Axiomtek | 대만 뉴타이베이(페이지 명시) | COM Express/SMARC SoM, AIE810-ONX(Jetson Orin NX 엣지AI) 등 | https://www.axiomtek.com | WF | 산업용 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Advantech | 대만(일반지식) | 임베디드 컴퓨터, 엣지 컴퓨팅 일반 | https://www.advantech.com | WF | 드론 전용 제품 미확인 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Rockchips.net | - | RK3588/RK3588S/RK3576/RK3568/RK3399 판매 | https://www.rockchips.net | WF | 판매 사이트, 칩 제조사 아님 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Radxa | 중국(일반지식) | 미확인(제목만 수신) | https://www.radxa.com | WF-제품 미수신 | 미확인 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Qualcomm Drones/Robotics | 미국(일반지식) | 미확인 | https://www.qualcomm.com/drones-robotics | WF-접근실패(404) | 미확인(ModalAI 페이지에 Flight Pro/RB5 언급) ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |
| Orange Pi | 중국(일반지식) | 미확인 | https://www.orangepi.org | WF-접근실패(ECONNREFUSED) | 미확인 ^[inbox/processed/hw-registry-20261017-vendors-compute.md] |

## 한계
- 이 문서는 **누가 만드는가(제조사 목록)** 이며 제품 사양이 아니다. 사양은 제품별 카탈로그/원문 수집이 별도로 필요하다.
- 국가/본사 열은 '페이지 명시'로 표기된 것만 공식 페이지 확인이고, '(일반지식)'은 확인되지 않은 값이다.
- 공식 사이트가 봇을 차단하거나 응답하지 않은 곳은 '미확인/접근실패'로 남겼다. 수출통제·NDAA 등 도입 제약은 공식 페이지에 명시된 경우만 기재했다.

## 관련 문서
- [[ros2-drone-integration]]
- [[drone-software-ecosystem-registry]]
