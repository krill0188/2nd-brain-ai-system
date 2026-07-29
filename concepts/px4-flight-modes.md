---
title: PX4 Flight Modes
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [drone-sw, PX4, flight-control]
sources: [raw/articles/px4-flight-modes.md]
confidence: high
domain: flight-control
contested: false
contradictions: []
---

# PX4 Flight Modes

PX4는 다양한 자율 비행 지원 수준을 제공하는 여러 비행 모드를 지원한다. 조종사의 개입 정도와 자동조종장치의 제어 범위에 따라 분류된다.

## Manual Modes (수동 모드)

가장 기본적인 수동 조종 모드로, 조종사가 직접 기체를 제어한다.

- **Manual/Stabilized**: 조종사가 롤/피치를 직접 제어. 자동조종장치가 자세 안정화만 제공.^[raw/articles/px4-flight-modes.md]
- **Acro**: 완전 수동 레이트 제어. 안정화 기능 없음.^[raw/articles/px4-flight-modes.md]

## Assisted Modes (보조 모드)

자동조종장치가 일정 수준의 제어를 제공하되, 조종사가 여전히 주요 조종을 담당한다.

- **Altitude Control**: 자동조종장치가 고도를 유지. 조종사가 롤/피치/요 제어.^[raw/articles/px4-flight-modes.md]
- **Position Control**: GPS 기반 위치 홀드. 가장 쉬운 비행 모드.^[raw/articles/px4-flight-modes.md]

## Auto Modes (자동 모드)

자동조종장치가 미션 실행을 담당하며, 조종사는 감시 및 개입만 수행한다.

- **Mission**: 사전 계획된 웨이포인트 미션 실행.^[raw/articles/px4-flight-modes.md]
- **Return to Launch (RTL)**: 자동으로 홈 위치로 복귀.^[raw/articles/px4-flight-modes.md]
- **Hold**: 현재 GPS 위치와 고도를 유지.^[raw/articles/px4-flight-modes.md]

## 주요 파라미터

| 파라미터 | 설명 |
|---------|------|
| `COM_RC_LOSS_T` | RC 신호 손실 타임아웃 |
| `NAV_RCL_ACT` | RC 손실 시 failsafe 동작 |
| `MPC_XY_VEL_MAX` | Position 모드 최대 수평 속도 |

## 관련 개념

- [[llm-wiki]] — 지식 관리 시스템
- [[ai-knowledge-workflow]] — AI 기반 지식 작업 흐름
