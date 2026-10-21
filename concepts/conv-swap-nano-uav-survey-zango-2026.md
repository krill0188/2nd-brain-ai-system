---
title: "Autonomous Navigation at the Nano-Scale: Algorithms, Architectures, and Constraints"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: hardware
tags: [drone, swap, nano-uav, edge-ai, survey]
sources: [inbox/processed/hw-20261021-conv-swap-nano-uav-survey-zango-2026.md]
confidence: medium
contested: false
contradictions: []
---

# Autonomous Navigation at the Nano-Scale: Algorithms, Architectures, and Constraints

- 원문: arXiv:2601.13252^[inbox/processed/hw-20261021-conv-swap-nano-uav-survey-zango-2026.md]
- 저자: Mahmud S. Zango, Jianglin Lan^[inbox/processed/hw-20261021-conv-swap-nano-uav-survey-zango-2026.md]
- 발행: 2026-01-19 (v2 2026-02-04)^[inbox/processed/hw-20261021-conv-swap-nano-uav-survey-zango-2026.md]

## 핵심 내용
50 g 미만 나노 UAV, 프로세서 소비전력 100 mW 미만 조건의 센싱·연산·제어 리뷰. 기하 기반 항법에서 엣지 AI로의 이동(저전력 칩의 양자화 신경망, 뉴로모픽 이벤트 기반 제어), 고밀도 광학 흐름·효율적 SLAM·학습 기반 비행제어의 HW-SW 공동설계를 다룬다. 남은 과제로 장기 지속 시간, 동적 장애물 회피, 시뮬레이션에서 실기로의 강화학습 정책 전이를 든다. 30쪽, 그림 5, 표 2.^[inbox/processed/hw-20261021-conv-swap-nano-uav-survey-zango-2026.md]
원문 인용: "governed by extreme Size, Weight, and Power (SWaP) constraints"^[inbox/processed/hw-20261021-conv-swap-nano-uav-survey-zango-2026.md]

## 설계·운용에 쓸 수 있는 지침
- GPS 없는 환경에서 경량 고전 제어와 데이터 기반 인식을 결합한 하이브리드 구조 제안(초록 기재).^[inbox/processed/hw-20261021-conv-swap-nano-uav-survey-zango-2026.md]

## 한계·미확인
- 초록 외 구체적 성능 수치 미확인(본문 미열람).^[inbox/processed/hw-20261021-conv-swap-nano-uav-survey-zango-2026.md]

상위 허브: [[drone-convergence-engineering-hub]] · 함께 보기: [[drone-power-battery]]
