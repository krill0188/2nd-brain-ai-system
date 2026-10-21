---
title: "EASA Artificial Intelligence Concept Paper: guidance for artificial intelligence applications, Proposed Issue 03"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: regulations
tags: [drone, certification, machine-learning, learning-assurance, easa, reinforcement-learning, level-3]
sources: [inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]
confidence: medium
contested: false
contradictions: []
---

# EASA Artificial Intelligence Concept Paper: guidance for artificial intelligence applications, Proposed Issue 03

- 원문: https://www.easa.europa.eu/en/newsroom-and-events/news/easa-releases-latest-issue-its-concept-paper-artificial-intelligence ; PDF https://www.easa.europa.eu/en/downloads/143701/en^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]
- 저자: EASA^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]
- 발행: 2026-06-03 (뉴스 게시일), 의견 마감 2026-08-12^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]

## 핵심 내용
EASA 뉴스(2026-06-03): "Proposed Issue 03" 공개, 의견수렴 10주. 뉴스는 이것이 "final Concept Paper deliverable foreseen under the EASA AI Roadmap 2.0"이라고 표기. Issue 02의 Level 1·2에 더해 강화학습, 기호(symbolic) AI 등 추가 기법과 Level 3 AI("advanced automation", 사용자가 원격이거나 부재일 수 있는 운용)를 탐구. 의견 마감 "no later than August 12, 2026".^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]
PDF(239쪽, 본문 텍스트 추출로 확인):^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]
- 적용 범위: Level 0~3 AI. "not covering 'autonomy' or 'autonomous systems'". 비적응형(모델 'frozen') 접근만. 사망·다수 중상에 직접 기여할 위험이 있는 시스템은 수용하지 않음("not accepting those systems presenting a risk directly contributing to the potential for fatalities or multiple life-threatening injuries"). 칼만 필터 등 상태추정기·결정론적 최적화·고정 규칙 전문가 시스템은 LKB 범위에서 제외.^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]
- 표 2 보증수준 상한(IDAL / AL-SWAL / AL-TQL): Supervised IDAL C, AL 3/SWAL 2, AL 3/TQL 3; Unsupervised IDAL D, AL 5/SWAL 4, AL 5/TQL 5; Reinforcement IDAL C, AL 3/SWAL 2, AL 3/TQL 3; Logic- and knowledge-based IDAL C; Large OTS models(범용 LLM 등) IDAL D, AL 5/SWAL 4.^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]
- 두 독립 AI/ML 구성요소의 아키텍처 이점 인정은 "not accepted"(기능·아이템 독립성 개념이 AI에 맞게 조정될 때까지).^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]
- 목차: 3.3 Learning assurance for supervised/unsupervised learning(67쪽), 3.4 Learning assurance for reinforcement learning(88쪽), 3.5 Logic- and knowledge-based AI assurance, 3.8 Hybrid AI assurance, 5장 Safety risk mitigation in advanced automation(Level 3 위임 감독), 부록 D Proportionality.^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]

## 설계·운용에 쓸 수 있는 지침
- 드론 기능에 지도학습 모델을 쓸 때 위 표 기준 최대 IDAL C까지 가정, 범용 LLM/VLM은 IDAL D 상한. 사람 책임 경계(Level 2B vs 3)를 먼저 분류.^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]

## 한계·미확인
- "Proposed" 이슈이며 확정판 아님(마감 이후 최종 발행 여부 미확인). 무인기(UAS) 전용 요건, 수백 개 Objective 세부, 부록 내용은 미요약. 기존 ai-cert-easa-concept-paper-level1-2-issue02.md 의 "최신 Concept Paper 번호 미명시" 공백을 이 파일이 채움.^[inbox/processed/hw-20261021-ai-cert-easa-concept-paper-proposed-issue-03.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[drone-regulations]]
