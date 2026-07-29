---
title: "Stacked Intelligent Metasurfaces Assisted UAV Communications"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, comms-protocol, antenna, metasurface, beamforming, uav]
sources: [inbox/fetch-2026-07-30-arxiv-stacked-intelligent-metasurfaces-assisted-uav-communications.md]
confidence: medium
contested: false
contradictions: []
domain: comms-protocol
---

# Stacked Intelligent Metasurfaces Assisted UAV Communications

Stacked Intelligent Metasurfaces(SIM)를 활용한 UAV 통신 시스템. 다층 캐스케이드 메타표면을 통해 전자기 도메인에서 프로그래머블 파형 신호 처리를 가능하게 한다.

## SIM 아키텍처

### 핵심 특성
- **다층 캐스케이드 메타표면**: 여러 층의 메타표면이 연속적으로 신호 처리
- **전자기 도메인 처리**: RF/디지털 도메인에서 전자기 도메인으로 일부 빔포밍 기능 이전
- **에너지 효율성**: 저전력 하이브리드 빔포밍 아키텍처 실현

### 장점
- 낮은 하드웨어 복잡성
- 높은 스펙트럼 효율성
- UAV 플랫폼에 적합한 에너지 효율

## 최적화 문제

### 목표
다중 사용자 다운링크 합속률 최대화를 위한:
- 디지털 프리코딩 설계
- SIM 위상 구성
- UAV 위치 선정

### 해결 방법
**교대 최적화 프레임워크**: 목적 함수의 단조적 개선 보장

## 성능 분석

| 요소 | 영향 |
|------|------|
| 메타표면 층 수 | 시스템 성능에 직접적 영향 |
| 각 층 크기 | 커버리지 및 이득 결정 |
| 스펙트럼 효율 | 기존 방식 대비 향상 |

## 응용 분야

- UAV-to-Ground 통신
- UAV-to-UAV 통신
- 5G/6G 통합 UAV 네트워크

## 관련 페이지

- [[emnn-doa-estimation]] — EMNN 기반 DOA 추정
- [[vertical-pinching-antenna-systems]] — V-PAS 기반 UAV 통신
- [[datalink-communication]] — 드론 데이터링크 통신 기술
