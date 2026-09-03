---
title: "Betaflight 2026.6 FC Alignment Wizard"
created: 2026-09-03
updated: 2026-09-03
type: concept
domain: hardware
tags: [drone-hw, hardware, drone-sw, fpv]
sources: []
confidence: high
contested: false
contradictions: []
---

# Betaflight 2026.6 FC Alignment Wizard

**릴리스**: Betaflight 2026.6  
**기능**: FC(비행 제어기) 보드 정렬(Alignment) 자동 설정 마법사  
**소스**: Joshua Bardwell YouTube (2026-09-02), https://www.youtube.com/watch?v=mHreu_l1FwY

## 개요

Betaflight 2026.6에 FC Alignment Wizard가 신규 추가됐다. FC 보드를 드론 프레임에 비표준 방향으로 장착한 경우, 이전에는 `BOARD_ALIGN_*` CLI 파라미터를 수동으로 입력해야 했다. Alignment Wizard는 이 과정을 GUI 단계별 안내로 대체하여 설정 오류를 줄이고 초보자 접근성을 높인다.

## 의의

- **설정 오류 감소**: 수동 각도 입력에서 발생하는 부호 반전, 축 혼동 실수를 줄임.
- **초보자 진입 장벽 하락**: 특히 비정형 프레임(언더 마운트, 측면 장착 등) 사용 시 유용.
- **기존 사용자**: CLI 직접 입력 방식도 유지되므로 하위 호환성 보장.

## 관련 기능

이전 Betaflight 릴리스 전반은 [[betaflight]]를 참조. FC 보드 종류별 물리적 장착 고려사항은 [[flight-controller-hardware]]에서 확인할 수 있다.

## 📰 최근 관련 소식
- [Joshua Bardwell] Betaflight FINALLY added this feature! FC Alignment Wizard in BF 2026.6 (youtube.com, 2026-09-02) — https://www.youtube.com/watch?v=mHreu_l1FwY
