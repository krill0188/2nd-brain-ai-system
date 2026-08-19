---
title: "Edge-Constrained UAV Small-Object Detection"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, ai-autonomy, object-detection, edge-computing, yolo]
sources: [inbox/fetch-2026-08-19-arxiv-edge-constrained-uav-small-object-detection-with-p2-enhancem.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# 에지 제약 UAV 소형 객체 탐지

## 개요

YOLOX-Nano 기반 P2 고해상도 탐지 분기와 양자 영감 진화 알고리즘(QIEA)을 결합한 경량 UAV 객체 탐지.

## 핵심 기술

### P2 고해상도 탐지 분기
- 경량 네트워크의 반복적 다운샘플링 문제 해결
- 얕은 공간 정보 보존

### QIEA (Quantum-Inspired Evolutionary Algorithm)
- 경량 구조 검색
- 정확도, FLOPs, 지연, 메모리, 재현율 종합 평가

## 성능 결과

### VisDrone 데이터셋
- P2 분기: AP_small 31.10% 향상 (YOLOX-Nano 대비)
- YOLOX-Nano+-P2: AP_small 44.9% 향상 (NanoDet-Plus 대비)

### QIEA 검색 결과
- Random-best, GA-best, SA/QUBO-best 후보 검증
- 프록시 순위가 최종 AP로 항상 전달되지 않음

## 결론

- P2를 주요 소형 객체 향상 경로로 사용
- QIEA를 경량 후보 검색 및 정확도-비용 분석 도구로 활용

## 관련 개념

- [[yolo]] — 실시간 객체 검출
- [[computer-vision-drone]] — 드론 컴퓨터 비전
- [[dame-net-uav-image-restoration]] — UAV 이미지 복원

## 참고

Wuming Lei et al., arXiv:2606.09081 (2026)
