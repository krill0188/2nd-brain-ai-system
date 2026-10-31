---
title: "AI 분석을 위한 드론 데이터 표준화 3계층 프레임워크 (이현주, 2026)"
created: 2026-10-31
updated: 2026-10-31
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-31-kci-ai-분석을-위한-드론-데이터-표준화-방안-현황분석과-3계층-프레임워크-제안--.md]
confidence: low
contested: false
contradictions: []
---

# 드론 데이터 표준화 3계층 프레임워크

이현주(동국대 국제정보보호대학원)의 항공우주시스템공학회지 2026 논문. KCI 원문 비공개로 **초록 기준**이다.^[inbox/processed/fetch-2026-10-31-kci-ai-분석을-위한-드론-데이터-표준화-방안-현황분석과-3계층-프레임워크-제안--.md]

## 문제
드론 데이터를 AI 학습에 쓰려는 시도가 늘지만 제조사마다 **타임스탬프 형식**과 **좌표계 기준**이 다르고, 주석 체계는 레이블 정의조차 통일돼 있지 않다. 이 문제가 AI 분석 파이프라인 전 단계에 누적돼 데이터셋 재사용을 구조적으로 막는다.

## 제안
국내외 표준화 현황과 한계를 검토한 뒤 세 요소로 구성된 프레임워크를 제안한다.
1. 최소정보 프레임워크
2. 멀티모달 시간동기화 기준
3. AI 학습데이터 품질기준

세부 항목과 검증 결과는 초록에 없다.

## 관련 문서
하드웨어 타임스탬프·시간동기는 [[data-sync-hardware-timestamp-ntnu-wiki-and-gnss-clock]], 비행 로그 형식은 [[data-flightlog-ardupilot-aplogger-formats]]를 참조한다.
