---
title: "DAME-Net: Compositional UAV Image Restoration"
created: 2026-08-19
updated: 2026-08-19
type: concept
tags: [drone, ai-autonomy, image-restoration, computer-vision]
sources: [inbox/fetch-2026-08-19-arxiv-compositional-degradation-uav-image-restoration-conditional-.md]
confidence: high
contested: false
contradictions: []
domain: ai-autonomy
---

# DAME-Net: 구성적 UAV 이미지 복원

## 개요

Degradation-Aware Mixture-of-Experts Network. 비, 안개, 노이즈 등 복합적 열화 요인이 있는 UAV 이미지 복원을 위한 네트워크.

## 핵심 모듈

### FDPM (Factor-wise Degradation Perception Module)
- 명시적 요인별 열화 신호 제공
- 다중 레이블 예측을 통한 해석 가능한 열화 설명

### CDMM (Conditioned Decoupled MoE Module)
- 단계별 조건 적용
- 공간-주파수 하이브리드 처리
- 마스크 제약 분리 전문가 라우팅

## MDUR 벤치마크

- **Multi-Degradation UAV Restoration benchmark**
- 43가지 열화 구성 (단일~4요인 복합)
- 표준화된 seen/unseen 분할

## 성능

- 기존 통합 복원 방법 대비 일관된 개선
- unseen 및 고차 복합 열화에서 더 큰 이득
- UAV 객체 탐지 다운스트림 작업에서 유효성 검증

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전
- [[yolo]] — 실시간 객체 검출
- [[edge-constrained-uav-small-object-detection]] — 에지 제약 UAV 소형 객체 탐지

## 참고

Jinquan Yan et al., arXiv:2604.09313 (2026)

## 📰 최근 관련 소식
- "러 파병 북한군 현재 8천500명…정찰·공격용 드론부대 포함" (v.daum.net, Sat, 22 Au) — https://news.google.com/rss/articles/CBMiRkFVX3lxTE82bXkwUDZ0WnNmSE4zbVNZRzV6cTVzbTcyYmhtX0U3N0dYQld6MUx2a3JjMDg3eU1fZ09kc1dHQXhTM1dIQ0E?oc=5
- 러, '시속 600㎞' 제트 엔진 드론 공세 확대…우크라 요격 고전 (v.daum.net, Mon, 31 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE54cEpvaUF1b2hGUkdlSzlmVF9YYUNYUTdFcVpwVDFnT24tOUdwVE01R3YwTnpPUXVIZVBkNXA3dVNTTjl3NVAtTGp5WU0tT0k?oc=5
- 폴란드 드론공장 방화…'또 러시아 공작' 의심 (v.daum.net, Mon, 31 Au) — https://news.google.com/rss/articles/CBMiT0FVX3lxTE9OTkdQR2UzdVZ4cGdwVWsyb0pDUUdRaUFmUTViY0FfRURPVDFkcktyYW5pQTJpX0hRMEhTWWtwZXo4UUVoRC1mQ2NabzA3clU?oc=5
- "차세대 對드론 방산 선도"…인천시, 방산혁신 지역협의회 출범 (v.daum.net, Wed, 02 Se) — https://news.google.com/rss/articles/CBMiVEFVX3lxTE1oWWxGSEZFVHpBcXJoVWlfczNyYXBzaUxQTUdEY0FNYkMyVFE0Y1BrSG95Zk9ZNHJINW5RUmhJT1hXUEd0Y0tKZmVUSS01YmNhUFdzdA?oc=5
