---
title: Monava
created: 2026-08-05
updated: 2026-10-01
type: entity
tags: [drone, ai-agent, counter-uas, security]
sources: [inbox/fetch-2026-08-05-rss-dronelife.md, raw/papers/_unclassified/켑스트럼을-이용한-단일-마이크로폰-기반-드론-거리-추정.md, raw/papers/_unclassified/드론-탐지를-위한-효과적인-특징-기반-후처리-기법.md]
confidence: medium
contested: false
contradictions: []
domain: ai-autonomy
---

# Monava

Monava는 스웨덴-핀란드 기반 방위 기술 기업으로, 수동적 음향 탐지 기술을 활용한 AI 기반 드론 탐지 시스템을 개발한다.

## 개요

- **본사**: 북유럽(스웨덴-핀란드)
- **분야**: Counter-UAS(C-UAS) 기술
- **핵심 기술**: 수동적 음향 탐지(Passive Acoustic Detection), AI 드론 탐지

## 최신 동향

2026년 8월, Monava는 새로운 투자 유치를 발표했다. 정부와 민간 투자자들의 대응 드론 시스템에 대한 관심 증가로 C-UAS 기술 분야의 투자가 계속되고 있다.

Monava의 수동적 음향 탐지 방식은 국내 학계에서 다뤄지는 두 계열의 드론 탐지 연구와
직접 맞닿는다. 켑스트럼 기반 단일 마이크로폰 거리 추정 연구는 음향 신호만으로 드론의
직접파·지면반사파 TDOA를 추출해 거리를 구하는 기법으로, Monava의 수동 음향 탐지 기술과
같은 감지 모달리티(음향)를 공유한다.^[raw/papers/_unclassified/켑스트럼을-이용한-단일-마이크로폰-기반-드론-거리-추정.md]
반면 레이더 기반 CFAR 특징 후처리 연구는 음향이 아닌 레이더 도플러 스펙트럼을 이용한
탐지·오경보율 개선 기법으로, Monava가 채택한 음향 방식과는 별개의 센서 모달리티에
해당한다.^[raw/papers/_unclassified/드론-탐지를-위한-효과적인-특징-기반-후처리-기법.md]

## 관련 개념

- [[droneshield]] — 호주 기반 드론 탐지/방어 기업
- [[lockheed-martin-morfius]] — 록히드마틴 드론 스웜 대응 시스템
- [[drone-first-responder-dfr]] — 응급 대응 드론 활용
- [[kci-cepstrum-single-microphone-drone-distance]] — 켑스트럼 기반 단일 마이크로폰 드론 거리 추정(동일 음향 모달리티)
- [[kci-drone-detection-cfar-feature-postprocessing]] — 레이더 CFAR 특징 기반 드론 탐지 후처리(대비 모달리티)
