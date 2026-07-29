---
title: "NEUROSYMLAND: Neuro-Symbolic Landing Site Assessment"
created: 2026-07-30
updated: 2026-07-30
type: concept
tags: [drone, ai-autonomy, computer-vision, safety, landing]
sources: [raw/papers/ai-autonomy/neurosymland-landing-assessment.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# NEUROSYMLAND: Neuro-Symbolic Landing Site Assessment

비구조화 환경에서 안전한 착륙 장소 평가를 위한 신경-기호적 시스템. 경량 인식과 명시적 안전 추론을 통합하여 지형 변화성 하에서도 견고한 성능을 제공하고 에지 하드웨어에서 실행 가능한 해석 가능한 결정을 내린다.

## 핵심 개념

### 신경-기호적 프레임워크
- **Probabilistic Semantic Scene Graph (PSSG)**: 온보드 시각 입력으로부터 확률적 의미 장면 그래프 구성
- **Symbolic Constraints**: 지형 평탄성, 장애물 여유, 공간 일관성을 포착하는 기호 제약
- **Structured Reasoning**: 인지적 불확실성 하에서 구조적 추론

### 성능
- 72개 시뮬레이션 착륙 시나리오에서 61회 성공
- 4개 경쟁 기준선 대비 우수한 성능 (37-57회 성공)
- 100회 하드웨어 인더루프 실험 완료

### 에지 배포 가능성
- **End-to-End Latency**: 전체 지연 시간 프로파일링
- **Resource Usage**: CPU/GPU 활용률, 메모리 사용량, 전력 소모 측정
- **Computational Cost**: 인식 및 PSSG 구성이 주요 비용, 기호 추론은 소수 지연

## 관련 페이지

- [[computer-vision-drone]] — 드론 컴퓨터 비전 및 객체 검출
- [[drone-safety-failsafe]] — RTL, Geofence 등 안전 장치
- [[drone-ai-agents]] — 자율 의사결정 및 BDI 아키텍처

## 출처

- Qian et al., "NEUROSYMLAND: Neuro-Symbolic Landing-Site Assessment for Robust and Edge-Deployable UAV Autonomy", arXiv:2607.02277, 2026.
