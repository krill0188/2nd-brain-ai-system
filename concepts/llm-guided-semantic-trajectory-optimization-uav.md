---
title: "LLM 유도 의미 인식 UAV 궤적 최적화 (ETRI Journal 2026)"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ai-autonomy
tags: [drone, drone-ai]
sources: [inbox/processed/fetch-2026-10-22-kci-llm-guided-semantic-aware-trajectory-optimization-for-uav-pa.md]
confidence: low
contested: false
contradictions: []
---

# LLM 유도 의미 인식 UAV 궤적 최적화 (ETRI Journal 2026)

이한섭(ETRI 우정물류기술연구센터)의 ETRI Journal 2026 논문. 원문은 비공개(KCI 페이월)라 초록 일부만 근거이며, 초록도 끝부분이 잘려 있다.^[inbox/processed/fetch-2026-10-22-kci-llm-guided-semantic-aware-trajectory-optimization-for-uav-pa.md]

## 문제 의식
- 도시 환경의 자율 UAV 경로 계획은 기하학적 안전과 의미(semantic) 인식을 모두 요구한다.
- 고정 비용이나 사전 정의된 위험 모델 기반 플래너는 임무에 따라 달라지는 의미적 우선순위를 반영하기 어렵다.

## 제안 구조
- LLM은 제한된(bounded) 상위 의사결정 모듈로만 쓴다.
- OpenStreetMap 데이터를 클래스별 의미 포텐셜 필드로 변환한다.
- 경로 상대 컨텍스트와 자연어 임무 설명으로부터 검증된 의미 변조 계수를 추론한다.
- 결정론적 B-스플라인 최적화기가 여러 요인을 함께 고려해 부드러운 경로를 생성한다.
- 기존 모델과의 비교에서 경로 효율과 의미 인식 사이의 경쟁력 있는 절충을 보였다고 한다(정량 수치는 초록에 없음).

## 위키 내 위치
LLM이 경로를 직접 생성하지 않고 계수만 추론해 결정론적 최적화기에 넘기는 설계다. LLM 에이전트가 경로를 찾는 [[lapf-llm-agent-pathfinder]], 자연어 항법 개요 [[llm-enabled-uav-natural-language-navigation]], 진화 기반 경로 계획 [[hermes-evolutionary-uav-path-planning]]과 대비된다.

## 📰 최근 관련 소식
- LLM-guided semantic-aware trajectory optimization for UAV path planning using environmental context (kci.go.kr, 2026) — https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003395386
