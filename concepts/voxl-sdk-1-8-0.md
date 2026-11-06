---
title: "ModalAI VOXL SDK 1.8.0 변경점"
created: 2026-10-22
updated: 2026-11-05
type: concept
domain: ai-autonomy
tags: [drone, drone-sw, drone-ai]
sources:
  - inbox/processed/fetch-2026-10-22-yt-sdk-180-built-to-be-built-on.md
  - inbox/fetch-2026-11-05-yt-sdk-180-same-hardware-new-aircraft.md
confidence: low
contested: false
contradictions: []
---

# ModalAI VOXL SDK 1.8.0 변경점

ModalAI 공식 채널 영상 두 편(2026-10-21, 2026-11-04)의 설명란 기준 요약이다. 자막이 없고 설명란이 잘려 있어 아래 목록이 전부가 아닐 수 있다.^[inbox/processed/fetch-2026-10-22-yt-sdk-180-built-to-be-built-on.md]^[inbox/fetch-2026-11-05-yt-sdk-180-same-hardware-new-aircraft.md]

## 개발자 대상 변경 (2026-10-21 영상)
- **libmodal-pipe 2.15**: PX4 기체 자세(vehicle attitude)와 VTX 상태를 pipe 인터페이스로 노출한다.
- **voxl-logger**: 대화형 설정 편집기, 원시 이미지 로깅과 재생을 추가했다.
- **스테레오**: 정류(rectification)가 어안(fisheye) 모델을 처리하고, 스테레오 깊이 추정이 하드웨어 동기화된 독립 pipe 2개를 지원한다.
- **신규 패키지**: voxl-wireguard, voxl-quectel-cm, voxl-aprilgrid-camera-calibration.
- SDK는 code.modalai.com에서 소스 공개(source-available)다.

## 비행 스택·추정기 업데이트 (2026-11-04 영상)
- **PX4**: 1.14에서 1.18로 단일 단계 업그레이드.
- **EKF2 중력 융합 필터링**: 공격적 비행에서 틸트 드리프트(till drift)를 수정한다.
- **IMU**: 800 Hz로 동작하며, 온칩 필터링으로 모터 진동이 추정기에 도달하기 전 제거한다.
- **VIO**: 초기화 시간이 약 65 ms에서 18 ms로 단축되었고, 비행 데이터로부터 자기 캘리브레이션이 가능해졌다.

## 관련
VOXL은 PX4 기반 컴패니언 컴퓨터 계열이다. 일반 구조는 [[companion-computer]], 비행 스택은 [[px4-flight-stack]], 비전 처리 개요는 [[computer-vision-drone]] 참조.

## 📰 최근 관련 소식
- [ModalAI] SDK 1.8.0 Built to be built on (youtube.com, 2026-10-21) — https://www.youtube.com/watch?v=B_PI7TkdSMA
- [ModalAI] SDK 1.8.0 Same hardware. New aircraft. (youtube.com, 2026-11-04) — https://www.youtube.com/watch?v=HoYsx0tg2pg