---
title: "Tri-Modal Fusion Transformers for UAV Object Detection"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, ai-autonomy, object-detection, transformer, multi-modal]
sources: [inbox/fetch-2026-08-19-arxiv-tri-modal-fusion-transformers-for-uav-based-object-detection.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# 삼중 모달 융합 트랜스포머 UAV 객체 탐지

## 개요

RGB + 열화상(LWIR) + 이벤트 카메라 데이터를 융합한 UAV 기반 객체 탐지 프레임워크.

## 모달리티

### RGB
- 기본 시각 정보
- 조명 변화에 취약

### 열화상 (LWIR)
- 저조도 환경에서 대비 유지
- 야간 탐지에 유효

### 이벤트 카메라
- 마이크로초 수준 시간적 에지 보존
- 고속 움직임 캡처

## 핵심 모듈

### MAGE (Modality-Aware Gated Exchange)
- 인터센서 채널 및 공간 게이팅 적용

### BiTE (Bidirectional Token Exchange)
- 양방향 토큰 수준 어텐션
- 깊이별 포인트와이즈 정제

## 데이터셋

- 10,489 프레임 동기화 RGB-열화상-이벤트 스트림
- 24,223 주석 차량 (주야간 비행)

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전
- [[event-camera-drone]] — 이벤트 카메라 기반 드론 비전
- [[yolo]] — 실시간 객체 검출

## 참고

Craig Iaboni, Pramod Abichandani, arXiv:2604.16630 (2026)
