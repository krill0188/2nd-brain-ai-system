---
title: "UAV 연합학습(FL) 보안·공격: 실기체(비행) 실증 논문 존재 여부 확인 (2026-10-22 기준)"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ai-autonomy
tags: [drone, federated-learning, security, real-flight, evidence-check]
sources: [inbox/processed/hw-20261022-conv-fl-uav-real-airframe-attack-evidence-check.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 연합학습(FL) 보안·공격: 실기체(비행) 실증 논문 존재 여부 확인 (2026-10-22 기준)

- 원문: 본 폴더 ai/research/ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md, ai-fl-uav-aerpaw-poisoning-kostage-2025.md; arXiv 2607.20280, 2412.02863, 2409.09794; ACM DOI 10.1145/3700838.3700857^[inbox/processed/hw-20261022-conv-fl-uav-real-airframe-attack-evidence-check.md]

## 핵심 내용
판정: **비행 중 실기체 UAV에서 FL 공격·방어를 시험했다고 확인된 논문은 찾지 못함(확인된 범위 내 '없음').** 전수 조사가 아니므로 '존재하지 않음의 증명'은 아님.^[inbox/processed/hw-20261022-conv-fl-uav-real-airframe-attack-evidence-check.md]
| 후보 | 하드웨어 | 비행 여부 | 공격·보안 평가 | 판정 |
|---|---|---|---|---|
| Sabo 등 2026 (arXiv 2607.20280) | RPi 4B 10대, Jetson 8대, 공격자 RPi (실제 802.11 deauth 주입) | 비행 안 함, 본문이 "drone surrogates" 명시 | 있음(가용성+신원 위장) | 실제 무선 하드웨어 실측이나 실기체 아님 |
| Kostage 등 2025 (ICDCN, AERPAW) | AERPAW 고정/이동 노드 | 서술 모순: "flight 25~60분" 대 "emulated", "simulated flight paths", "emulation setup" | 데이터 오염(소프트웨어 주입)+방어 | 실비행 구간 불명확, 실기체 실증으로 불채택 |
| Federated Learning in Adversarial Environments (arXiv 2409.09794) | Jetson Nano 클라이언트+RPi 서버 | 지상 장치 | 오염 시험 | 드론 아님(검색 결과 요약 기준, 본문 미정독) |
| Proximal Control of UAVs with FL (arXiv 2412.02863) | 초록: "real robots" 정확도 96% 초과 주장 | 초록만 확인, 비행 세부 미확인 | 보안 평가 없음 | 보안 논문 아님 |
| Real-Time UAV Urban Object Detection with FL (ResearchGate 380455433) | 검색 요약: 실제 UAV 배포, 약 18 FPS | 실제 UAV(요약 기준) | 공격 평가 없음(요약 기준) | 원문 미열람 |
- 이미 20261021 수집분(Jedrzejczak 2026 등)은 시뮬레이션/초록 수준.^[inbox/processed/hw-20261022-conv-fl-uav-real-airframe-attack-evidence-check.md]

## 설계에 쓸 수 있는 지침
- 인용 시 "실기체 FL 공격 실증은 확인 못 함, 지상 대용 장치 실측(Sabo 2026)이 가장 가까움"으로 표기.^[inbox/processed/hw-20261022-conv-fl-uav-real-airframe-attack-evidence-check.md]

## 한계·미확인
- 사용 수단: WebSearch 3회(표준·확장), arXiv HTML 전문(2607.20280), NSF PAR PDF 전문(AERPAW), arXiv 초록(2412.02863). 미사용/실패: IEEE Xplore, Google Scholar(차단 가능성으로 시도 안 함), 2409.09794·380455433 본문 미정독. 신뢰도: 판정 문장은 중(부정 증명 불가).^[inbox/processed/hw-20261022-conv-fl-uav-real-airframe-attack-evidence-check.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[mbse-uav-sysml]]
