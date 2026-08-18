---
title: Drone AI Overview
created: 2026-08-06
updated: 2026-08-07
type: concept
tags: [drone-ai]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Drone AI Overview

드론과 AI/ML 통합 전반을 아우르는 도메인 개요 페이지. 컴퓨터 비전, 자율 비행, 탐지·추적, SLAM, 자율 의사결정 에이전트를 포함한다.

## 주요 응용 영역

| 영역 | 설명 |
|---|---|
| 컴퓨터 비전 | 객체 탐지, 추적, 검사 |
| SLAM / 위치추정 | GPS 미수신 환경 항법 |
| 자율 의사결정 | Perception-Action Loop, 다중 에이전트 |
| Counter-UAS AI | RF/영상 기반 드론 탐지 AI |

## 관련 개념

- [[drone-ai-agents]] — 드론 AI 에이전트 아키텍처
- [[computer-vision-drone]] — 드론 탑재 컴퓨터 비전

## 세부 연구/기업

- [[agile-quadrotor-learning]] — 강화학습 기반 민첩 쿼드로터 제어
- [[divide-conquer-uav-detector]] — Divide-and-Conquer UAV 이미지 탐지기
- [[gnn-uav-anomaly-detection]] — GNN 기반 UAV 이상탐지
- [[lightweight-safe-rl-uav]] — 경량 안전 강화학습
- [[multi-modal-human-intent-uav]] — 다중모달 인간 의도 인식
- [[neurosymland-landing-assessment]] — 신경-기호 착륙 평가
- [[rgb-ir-fusion-uav-detection]] — RGB-IR 융합 객체 탐지
- [[skyjepa-world-models]] — 월드모델 기반 sim-to-real
- [[yolo-v8-4-115]] — YOLO v8.4.115 릴리스
- [[micro-drone-slam-imu-vio-lidar-uav-livox-mid-360-pixhawk-4-m]] — 마이크로드론 SLAM 사례 비교
- [[tekever]] — 유럽 AI 기반 자율 시스템 기업
- [[xtend-ai-robotics]] — XTEND-JFB 합병 방위 로봇 기업
- [[multi-uav-collision-avoidance-survey]] — 다중 UAV 딥러닝 충돌회피 서베이 논문
- [[moe-multimodal-uav-detection]] — MoE 기반 강건한 멀티모달 객체 탐지 논문

## 📰 최근 관련 소식
- U.S. military to continue dispatching counter-drone capabilities to the Middle East (DefenseScoop, Fri, 10 Ap) — https://news.google.com/rss/articles/CBMihwFBVV95cUxOY1ZGcm0xWmFSY19Scjl2ckhiZ1ZMOW52X2lXR3lSOWFIaFNWanZ3OVoxZE4zMG0xM1AtZnBwQTBqTWFZZjhJV2NETVR4dEk4cW1zNGFUREVuY09EMWdHb3FUVWg4VF9HTURJTi1zSFZidzM0ZGl4T0hTcm1PS1RBRlZGbDRnUU0?oc=5
- 니어스랩 "AI 방산 드론은 승자독식…데이터 확보 기업이 시장 장악" (v.daum.net, Sun, 09 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE40RmFYamRyTDNnLUcyV0ZCRktFXzhQd0FFd200cEdYOTBDUzkwenplNFNvSVZEX1lrTHM4X3I2RDNSeEFqcGZhc0diTEN6WlU?oc=5
- Parrot Drone BeBop 2 Is Like a “Flying Image Processor” - IEEE Spectrum (news.google.com, Thu, 29 Ju) — https://news.google.com/rss/articles/CBMihwFBVV95cUxOcHZmc0tpbmlSdVRpUHdQaXloS245ekxWcXRzZ2ZJZ2U4LXdEUUZWbEo0UEpKU21EWE84cUhuT3FpOGo1TVoyYmNTT3dTQ18xZGlLX2syTXZqaUFEMVNEanpVLXZjS2swMDExVlIxRkRDb3BzSXJYenIweWc4LXRQbWJhejV4WnM?oc=5
- Marine Corps establishes robotics integration group for drone and counter-drone training (DefenseScoop, Mon, 06 Ju) — https://news.google.com/rss/articles/CBMipgFBVV95cUxPbXhGMTRJVktiY0IyYmdhU2xMVjVlRERBQTZSRzVqX0VVamJ3Q2UyR1BLM2ZYcVFrZl9lT25jbGwtOS16WlhfSG5EZERCWl92TXRVMVRVeDJ3N1ozajU1WncycUEydlBFbzR5MzVNSU1RaGtKdjhFY3FXZU1EbWtsSExvQ0Iwakh6NVpUR2tjWFRLZXVpcHRPWlJJR3NCZ3QxNk9QU3dR?oc=5
- 'AI 탑재 바다의 드론' 무인수상정 개발…K방산 3사 3색 전략 (v.daum.net, Wed, 12 Au) — https://news.google.com/rss/articles/CBMiVEFVX3lxTE1va2RqNlR5eXRNRjgzbUlROV91QnUtOXJuajJ2T0RUY3Vub0hjM1Zwdlp6OHZpdlNhWFdrT2xnaXJBSEdCLWc1ME43bEgxOVN0djVPVg?oc=5
- 'AI 선장'이 몬다‥'바다 위 드론' 무인수상정 (MBC 뉴스, Wed, 12 Au) — https://news.google.com/rss/articles/CBMiekFVX3lxTE55R3hCVnN2djdYRWtnRTJwc1JKMGNBZFNzdUd6ZGVrck1iaVE3WU9rcWplZllpWXdtTWZWZVcycHhPWE9MdTVmbVJ3dm13a01TM3RUeWpnSVNRdEppcFRya1FQckhqQWlaWXB2XzZHX1dBdWdYN01TRVZR?oc=5
- 무인이동체·국방 AI·안티드론·무인이동체 한자리에 모인다 (v.daum.net, Thu, 13 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE50VHNNWTZJU3ZzSnBrd3FITWxfUWFpV2FZdUd3ZWN3OUdSY2pUekltRm5qbzViLXBCYW9EUE1ncDRiaDdRUmtkTFNxVl9od1E?oc=5
- 美, 중동 다국적 공격드론TF 띄운다 (MBC 뉴스, Fri, 14 Au) — https://news.google.com/rss/articles/CBMidEFVX3lxTFBqTTdKTjB5SWxMSnRvbHNCSHlINVlLYWF6bVpaN3hZUFh0U1V4bHVVZWJYSUpERjBHZEtOMFByNUlGa2tSZE41bmRoWm9lMTJ5OHljLVhfakllT2JneV9xZlAtSDVPV0ZaWkRjR2ZVelhRYkJh0gF0QVVfeXFMTi12QTVOMW1fOGRTWmVsTUo3NmVsNER4YmtGUVZjUHQwWklFMVRfUHdxZEdweGdQb3BIRTRNekJYcHlmOHd1RkRZT3p1eGhiOXNweV9LdmkyajBtMWZ0QmtNWk01RUZMcGhsUEJxM29DYk9iRmE?oc=5
