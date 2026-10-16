---
title: "드론 융합 SW 레지스트리"
created: 2026-10-17
updated: 2026-10-17
type: concept
domain: software-ecosystem
tags: [drone, drone-sw]
sources: [inbox/processed/hw-registry-20261017-software-INDEX.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 융합 SW 레지스트리

드론과 융합해 쓰는 SW 12개 분야(비행 스택·GCS·미들웨어·SLAM·인식 AI·계획/제어·군집·시뮬레이션·통신 프로토콜·영상·플릿/UTM·보안/운영)의 제품·오픈소스 목록.

| 분야 | 레지스트리 | 항목 수 |
|---|---|---|
| 비행 스택 | [[software-registry-flight-stack]] | 13 |
| GCS | [[software-registry-gcs]] | 14 |
| ROS·미들웨어 | [[software-registry-middleware]] | 18 |
| 항법·SLAM | [[software-registry-navigation-slam]] | 28 |
| 인식·엣지 AI | [[software-registry-perception-ai]] | 24 |
| 계획·제어 | [[software-registry-planning-control]] | 25 |
| 군집·멀티에이전트 | [[software-registry-swarm-multiagent]] | 14 |
| 시뮬레이션 | [[software-registry-simulation]] | 22 |
| 통신 프로토콜 SW | [[software-registry-comms-protocol-sw]] | 23 |
| 영상 스트리밍 | [[software-registry-video-streaming]] | 22 |
| 플릿·UTM | [[software-registry-fleet-utm]] | 22 |
| 보안·운영 | [[software-registry-security-ops]] | 22 |
| **합계** | 12개 분야 | **247** |

## 쓰는 법
- 설계 질의에서 후보 부품/도구가 필요하면 분야별 문서에서 제조사·제품군을 찾고, 사양은 제품별 카탈로그나 공식 페이지 원문으로 확인한다.
- 정보 빈틈(예: 모터 최대추력 미확인)이 드러나면 이 레지스트리에서 수집 우선순위를 뽑아 제품별 사양 수집으로 이어간다.
- 연관 레지스트리: [[drone-hw-vendor-registry]]

## 한계
- 공식 사이트가 봇을 차단하거나 응답하지 않은 곳은 '미확인/접근실패'로 남겼다(상세는 각 분야 문서의 표 참조).
- 국가/본사·라이선스·연동 포인트는 값마다 확인 수준이 달라, 확인되지 않은 칸은 비워 두거나 표시했다.
- 수집 시점(2026-10-17) 기준이며 제품 라인업·정책은 바뀔 수 있다.
