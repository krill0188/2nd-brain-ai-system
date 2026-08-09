---
title: "Multi-Modal Human Intent Mediation for Safe UAV Maneuvers"
created: 2026-07-30
updated: 2026-08-10
type: concept
tags: [drone, voice-control, ai-autonomy, human-machine-interface, safety]
sources: []
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
note: "Raw source not preserved in repo — found during 2026-08-10 provenance audit, needs recapture"
---

# Multi-Modal Human Intent Mediation for Safe UAV Maneuvers

음성, 제스처, GUI 등 다중 모달리티 인간 입력을 안전한 UAV 기동으로 중재하는 요구사항 기반 모델. 운용자 입력을 직접 명령이 아닌 제약된 기동 요청으로 처리하여 지형, 분리 요구사항, 비행 봉투 제한과의 충돌을 방지한다.

## 핵심 개념

### Request-Evaluate-Execute Pipeline
1. **Request Interpretation**: 다중 모달 입력 해석 및 신뢰도 평가
2. **Constraint Validation**: 지형, 분리, 작업 공간, 비행 봉투 제한 검증
3. **Execution Monitoring**: 연속적 런타임 모니터링하에 실행

### 요구사항 기반 사양 모델
- **Preconditions**: 기동 허용 선결조건
- **Invariants**: 실행 중 불변조건
- **Guard Conditions**: 전이 보호 조건
- **Postconditions**: 완료 후 조건 및 비상 처리

### 안전 보장
- 런타임 검증 지원
- 반응적 합성 접근법을 위한 기반 제공
- 음성/GUI 입력의 신뢰적 해석 및 안전한 실행

## 관련 페이지

- [[voice-control-drone]] — 음성 명령 인터페이스 및 MAVLink 매핑
- [[drone-safety-failsafe]] — RTL, Geofence, Arming 등 안전 장치
- [[drone-ai-agents]] — 자율 의사결정 및 BDI 아키텍처

## 출처

- Nelson et al., "A Model for Mediating Multi-Modal Human Intent into Safe Maneuvers for UAVs", arXiv:2607.11654, 2026.
