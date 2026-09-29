---
title: "선호 기반 강화학습을 통한 곡예비행 학습 (UZH, IROS 2026)"
created: 2026-09-23
updated: 2026-09-23
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-09-23-yt-learning-acrobatic-flight-from-preferences-iros-2026.md]
confidence: medium
contested: false
contradictions: []
---

## Definition

취리히대(UZH) Robotics and Perception Group이 IROS 2026에서 발표한 연구로, 수동 설계된
보상 함수 없이 선호 기반 강화학습(Preference-based Reinforcement Learning, PbRL)만으로
쿼드로터 곡예비행 제어 정책을 학습한다.^[inbox/processed/fetch-2026-09-23-yt-learning-acrobatic-flight-from-preferences-iros-2026.md]

## Why It Matters

곡예비행은 복잡한 동역학·빠른 기동·정밀한 실행이 요구되어 목표를 수식으로 정형화하기
어렵고, 수동 설계 보상 함수로는 "중요한 품질"을 포착하지 못하는 경우가 많다. PbRL은
목적을 형식화하기 어렵거나 본질적으로 주관적인 과제에 적합한 접근으로 제시된다.^[inbox/processed/fetch-2026-09-23-yt-learning-acrobatic-flight-from-preferences-iros-2026.md]

## Key Properties

- 보상 함수를 수작업 설계하지 않고 선호 비교 데이터로 정책 학습
- 적용 대상: 쿼드로터 곡예비행(빠른 기동, 정밀 실행이 핵심 난제)
- 출처: UZH Robotics and Perception Group, IROS 2026

## Related

- [[agile-quadrotor-learning]]
- [[rl-quadrotor-tunable-control]]
