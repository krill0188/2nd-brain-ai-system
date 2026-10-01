---
title: "드론 탐지를 위한 효과적인 특징 기반 후처리 기법 (KCI)"
created: 2026-10-01
updated: 2026-10-01
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-01-kci-드론-탐지를-위한-효과적인-특징-기반-후처리-기법.md]
confidence: medium
contested: false
contradictions: []
---

# 드론 탐지를 위한 효과적인 특징 기반 후처리 기법

국립부경대학교 최인오(한국정보기술학회논문지, 2026)의 연구. 낮은 신호대클러터비(SCR,
Signal-to-Clutter Ratio) 환경에서 강한 클러터·잡음으로 인해 드론과 같은 소형 표적 탐지가
어렵고, 기존 CFAR(Constant False Alarm Rate) 기반 탐지기가 높은 오경보율을 보이는 문제를
다룬다.^[inbox/processed/fetch-2026-10-01-kci-드론-탐지를-위한-효과적인-특징-기반-후처리-기법.md]
원문은 페이월로 비공개이며 초록만 확보됨.

## 방법

- CFAR 기반 후보 탐지 이후 적용되는 특징 기반 후처리 기법을 제안.
- 도플러 스펙트럼의 형상 및 주기적 특징을 점수 기반으로 결합해 표적과 클러터를 구분.

## 결과

- 시뮬레이션 결과, 기존 CFAR 및 CFAR+DSCR 기법과 유사한 탐지확률을 유지하면서 오경보율을 크게
  감소 — 낮은 SCR 환경에서 우수한 탐지 성능 확인.

## Related

- [[monava]] — 스웨덴-핀란드 수동 음향 탐지 기반 C-UAS 기업
- [[robin-radar]] — 대드론 레이더 제조 기업
- [[pt-detr-small-target-detection]] — RT-DETR 기반 UAV 소형 객체 탐지
