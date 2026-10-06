---
title: "AI 기반 드론을 활용한 중요시설 비인가 침입 탐지 연구"
created: 2026-10-02
updated: 2026-10-06
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-02-kci-ai-기반-드론을-활용한-중요시설-비인가-침입-탐지-연구.md, raw/papers/_unclassified/ai-기반-드론을-활용한-중요시설-비인가-침입-탐지-연구.md]
confidence: low
contested: false
contradictions: []
---

# AI 기반 드론을 활용한 중요시설 비인가 침입 탐지 연구

조성범(ktds)이 한국IT정책경영학회 논문지(2026)에 게재한 개념설계 연구로, 중요시설의 감시
공백을 보완하기 위해 문헌검토에 기반한 AI 드론 비인가 침입 탐지체계를 제안한다. 원문은
비공개(페이월)이며 초록만 확인 가능하다.^[inbox/processed/fetch-2026-10-02-kci-ai-기반-드론을-활용한-중요시설-비인가-침입-탐지-연구.md]

## 제안 체계

- 객체의 위치·이동경로·체류시간과 출입인가 정보를 연계해 객체검출 결과를 침입 의심 이벤트로
  전환하는 방식.
- 5단계 파이프라인: **영상수집 → 객체탐지·추적 → 구역판단 → 이벤트 생성 → 관제 대응**.
- 항법·통신 보안과 개인영상정보 보호요건을 탐지 신뢰성·관제 활용 기준에 반영.

## 한계

- 개념설계 단계이며 실증 데이터는 제시되지 않음.
- 후속 실증에서 객체검출 정확도, 사건 단위 탐지율, 오경보율, 경보지연을 평가할 예정이라고만
  언급되어 있어 정량적 성능은 미확인.

## 관련 개념

- [[computer-vision-drone]] — 드론 컴퓨터 비전: YOLO, SLAM, 객체 추적 기반 기술
- [[drone-ai-agents]] — 자율 의사결정 및 다중 에이전트 협력 아키텍처
- [[kci-critical-facility-illegal-drone-counter-uas-zones]] — 같은 국가중요시설 대상 대드론 체계 개선안(억제·중첩 탐지식별·3지대 확장)

## 📰 최근 관련 소식
- [멈춤보단 천천히라도] 블렌더를 활용한 애니메이션을 만들어보고 있어요 (youtube.com, 2026-10-02) — https://www.youtube.com/watch?v=A8f1DRuyE14
