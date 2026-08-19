---
title: "Multi-view Glint Correction for UAV Multispectral Imagery"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, ops-mission, multispectral, image-processing, research]
sources: [inbox/fetch-2026-08-19-kci-multi-view-glint-correction-for-uav-multispectral-imagery-in.md]
confidence: high
contested: false
contradictions: []
domain: ops-mission
---

# UAV 다중분광 영상 글린트 보정

## 개요

UAV 다중분광 영상은 해안 수역의 센티미터급 관찰을 가능하게 하지만, 태양 반사(glare)로 인한 반사율 과대추정과 공간적 불연속성 문제가 발생한다.

## MVGC (Multi-View Glint Correction) 방법

### 핵심 개념
- 고중복 UAV 촬영의 다중 뷰 중복성 활용
- 각 지상 위치별 다중 뷰 관측 스택 분석

### 구성 요소
1. **NIR-분포 기반 이상치 제거**: 안정적인 VIS-NIR 결합 유지
2. **다중 뷰 스택 결합**: 공간적 불연속성 완화

## 적용 분야

- 해안 수역 모니터링
- 저서 생물 영향 shallow water 관찰
- 수질 분석

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전
- [[uav-task-offloading-traffic-monitoring]] — UAV 기반 교통 모니터링

## 참고

부산대학교 백승일, Ocean Science Journal (2026)
