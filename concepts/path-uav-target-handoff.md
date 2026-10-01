---
title: "PATH: 협력 드론 간 연속 표적 감지 핸드오프"
created: 2026-09-15
updated: 2026-10-01
type: concept
domain: comms-protocol
tags: [drone, comms-protocol, swarm]
sources: [inbox/fetch-2026-09-15-arxiv-path-continuous-target-sensing-among-autonomous-cooperative-.md, raw/papers/_unclassified/감시-드론을-위한-심층-신경망-기반-지상-표적-추적-기법.md]
confidence: medium
contested: false
contradictions: []
---

# PATH: 협력 드론 간 연속 표적 감지 핸드오프

Perspective Alignment & Tracking Handoff(PATH)는 비행 지속시간이 제한된 두 협력 UAV 사이에서
동일한 물리적 표적의 추적 책임을 넘겨주는 플랫폼 비종속형(geometry-assisted) 프레임워크다.
Kim 외 7인, arXiv:2609.12456v1 (2026-09-11 게시).^[inbox/fetch-2026-09-15-arxiv-path-continuous-target-sensing-among-autonomous-cooperative-.md]

## 문제 정의

기존 표적 핸드오프 방식은 전역 위치 추정(글로벌 로컬라이제이션) 또는 외형 기반
교차 시점 연관(cross-view association)에 의존하는데, 각각 위치 불확실성과 모호한
시각적 특징이라는 한계를 가진다.

## 동작 방식

- **송신 드론(sender)**: RGB-D 센싱으로 추적 중인 표적을 미터 단위 3D 포인트로 재구성.
- **수신 드론(receiver)**: 표식(fiducial) 관측으로 상대 자세(relative pose)를 추정하고,
  전달받은 표적 3D 포인트를 자신의 영상에 투영해 표적 획득의 공간적 사전정보(spatial prior)로 사용.
- 수신 드론이 생성한 후보를 송신 드론에 재전송해 **Cross-view Mutual Agreement Handshake**로
  검증한 뒤에만 추적 책임이 이전됨.

## 실측 성능

- 상대 위치·표적 위치 평균 오차: 각각 0.047m, 0.030m.
- 시각적으로 모호한 조건에서 프레임 단위 수신측 표적 획득 정확도 96.0%(거짓양성 2.0%, 거짓음성 2.0%).
- 상대 자세(relative-pose) 불확실성이 수신측 투영 오차의 지배적 요인으로 확인됨(센서 오차 민감도 분석).
- 비디오 프레임률(60Hz)에서 동작, UAV 간 통신량 16kB/s 미만으로 자원 제약 플랫폼에서도 경량 구현이 가능함을 시연.

PATH는 협력 드론 "사이"의 표적 추적 책임 이전을 다루는 반면, 국내 연구인 RetinaNet+칼만필터
기법은 단일 감시 드론이 다수 지상 표적을 "혼자" 탐지·추적하는 문제를 다룬다. 두 연구는 표적
추적의 서로 다른 단계(단일 플랫폼 내부 추적 vs 플랫폼 간 핸드오프)를 보완적으로 다룬다는
점에서 연결된다^[raw/papers/_unclassified/감시-드론을-위한-심층-신경망-기반-지상-표적-추적-기법.md].

## 관련 개념

- [[datalink-communication]] — 드론 데이터링크 통신 기술
- [[swarm-coordination]] — 다중 드론 협력 구조
- [[uav-swarm-target-localization]] — 다중경로 환경 UAV 스웜 표적 위치 추정
- [[kci-ground-target-tracking-retinanet-kalman]] — RetinaNet+칼만필터 기반 단일 감시 드론 지상 표적 추적(KCI)
