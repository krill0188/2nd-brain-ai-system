---
title: "Dynamic Multi-scale Mixture-of-Experts"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [object-detection, uav, multimodal-enhancement, ai-architecture]
sources: []
confidence: medium
contradictions: []
domain: ai-autonomy
contested: false
---

# Dynamic Multi-scale Mixture-of-Experts

동적 멀티-스케일 Mixture-of-Experts(동적 Mixture-of-Experts)는 UAV(무인기) 소형 물체 감지를 위해 cross-scale(다중 스케일) feature enhancement(특성 강화)을 통합한 AI 아키텍처입니다.

본 기술은 입력 이미지나 센서 데이터의 다중 스케일 특징을 동적으로 통합하고, 각 스케일에 최적화된 전문가 네트워크(Experts)를 활용하여 작은 물체의 탐지 성능을 향상시킵니다. UAV 영상처럼 복잡한 배경 속에서 소규모 객체를 식별해야 하는 상황에서 효과적입니다.

## 개요

UAV 소형 물체 탐지는 배경 clutter(잡음) 및 해상도 제한으로 인해 어려움이 있습니다. 본 논문에서 제안하는 Dynamic Multi-scale Mixture-of-Experts는 cross-scale feature enhancement 메커니즘을 통해 서로 다른 스케일의 특징을 상호 보완하고, Mixture-of-Experts 구조를 통해 각 스케일에 특화된 전문가 모델을 동적으로 활성화합니다. 이를 통해 전체 네트워크의 계산 비용을 크게 늘리지 않으면서도 탐지 정확도를 높일 수 있습니다.

## 핵심 파라미터

| 파라미터 | 내용 |
|---|---|
| **핵심 구성** | Cross-scale Feature Enhancement, Mixture-of-Experts 기반 동적 라우팅 |
| **대상** | UAV 소형 물체 탐지 |
| **목표** | 탐지 정확도 향상 및 계산 효율성 유지 |
| **연도** | 2027 |
| **출처** | DOI: 10.1016/j.eswa.2026.134461 |

## 활용처

- UAV(무인기) 영상 기반 소형 물체 탐지 (예: 건물 검사, 농업 모니터링, 구조 탐색)
- 드론 기반 영상 인식 시스템에서 계산 리소스 제한 하에 성능 개선이 필요한 경우
- 멀티 스케일 특징이 중요한 고해상도 항공 영상 처리

## 관련 페이지

- [[small-object-detection]] — UAV 영상에서 소형 객체를 식별하는 일반적인 기술 및 과제
- [[mixture-of-experts]] — 전문가 네트워크 기반의 대표적인 AI 라우팅 아키텍처

## 출처

- (사용자 재확인 필요) DOI: 10.1016/j.eswa.2026.134461, "Dynamic multi-scale mixture-of-experts with cross-scale feature enhancement for UAV small object detection", Xiangyu, Li; Zhiqiang, Hou; Lingling, Xiong; Sugang, Ma; Yang, Liu, 2027.

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
