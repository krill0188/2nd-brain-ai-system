---
title: "ModalAI VOXL SDK 1.8.0 변경점"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ai-autonomy
tags: [drone, drone-sw, drone-ai]
sources: [inbox/processed/fetch-2026-10-22-yt-sdk-180-built-to-be-built-on.md]
confidence: low
contested: false
contradictions: []
---

# ModalAI VOXL SDK 1.8.0 변경점

ModalAI 공식 채널 영상(2026-10-21)의 설명란 기준 요약이다. 자막이 없고 설명란도 끝이 잘려 있어 아래 목록이 전부가 아닐 수 있다.^[inbox/processed/fetch-2026-10-22-yt-sdk-180-built-to-be-built-on.md]

## 개발자 대상 변경
- **libmodal-pipe 2.15**: PX4 기체 자세(vehicle attitude)와 VTX 상태를 pipe 인터페이스로 노출한다.
- **voxl-logger**: 대화형 설정 편집기, 원시 이미지 로깅과 재생을 추가했다.
- **스테레오**: 정류(rectification)가 어안(fisheye) 모델을 처리하고, 스테레오 깊이 추정이 하드웨어 동기화된 독립 pipe 2개를 지원한다.
- **신규 패키지**: voxl-wireguard, voxl-quectel-cm, voxl-aprilgrid-camera-calibration.
- SDK는 code.modalai.com에서 소스 공개(source-available)다.

## 관련
VOXL은 PX4 기반 컴패니언 컴퓨터 계열이다. 일반 구조는 [[companion-computer]], 비행 스택은 [[px4-flight-stack]], 비전 처리 개요는 [[computer-vision-drone]] 참조.

## 📰 최근 관련 소식
- [ModalAI] SDK 1.8.0 Built to be built on (youtube.com, 2026-10-21) — https://www.youtube.com/watch?v=B_PI7TkdSMA
