---
title: "UAV Positioning Using GNSS: A Review of the Current Status"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: hardware
tags: [drone, gnss, review, 로터변조, 기선길이, 2차출처]
sources: [inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]
confidence: medium
contested: false
contradictions: []
---

# UAV Positioning Using GNSS: A Review of the Current Status

- 원문: https://doi.org/10.3390/drones10020091^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]
- 저자: Chaopei Jiang, Xingyu Zhou, Hua Chen, Tianjun Liu^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]
- 발행: 2026-01-28 (Drones 10(2), 91, MDPI 오픈액세스 리뷰)^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]

## 핵심 내용
무인기 GNSS 측위 리뷰. 설치환경·RTK 기선에 관한 서술 중 인용 가치가 있는 문장과 수치만 정리(리뷰이므로 2차 출처).^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 로터 블레이드가 안테나 시야를 주기적으로 가로지르며 신호를 산란시켜 로터 주파수와 고조파에서 진폭·C/N0 변동을 일으키고, 이는 반송파 위상 잡음과 cycle slip 검출을 어렵게 한다(서술, 정량 수치는 이 리뷰에 없음).^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]
- 소형 UAV는 로터·암·배터리·페이로드 베이 가까이에 소형 패치/칩 안테나를 달기 때문에 시야 차폐와 반복적 플랫폼 다중경로가 생긴다. 인용된 실증 연구들은 안테나 위치·기체 형상이 소형 UAV에서 오차 예산을 지배할 수 있다고 서술.^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]
- 헥사로터 장착 연구(Hehenberger 외) 요약: 24 h 동안 대부분 C/N0 > 40 dB-Hz, 장착 시 천저 방향 LHCP 이득 약 5 dB 낮음.^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]
- 구조물 근접 점검(Tavasci 외 인용): 장애물 0~5 m 이내에서 RTK 고정 실패가 빈번, 장애물 통과 후 재고정 통상 9~13 s, 높이 방향 가짜 고정 최대 약 0.4 m.^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]
- 안테나 의도적 지터(Liu 외 인용): 직선 ±6.2 cm 지터로 3D RMS 오차가 2.45 m에서 1.51 m로 감소(개방 플랫폼).^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]
- RTK 기선: 단일 기준국 RTK의 성능은 기선 길이·위성 기하·보정 링크 품질에 강하게 의존하며, UAV 고도·범위에서는 5~15 km 기선이 높은 ambiguity 고정률 유지에 흔히 권장된다고 서술(인용 문헌 기반, 이 리뷰 자체의 실험 아님).^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]

## 한계·미확인
열람 범위: MDPI 본문 전체를 스크랩해 관련 절만 grep으로 확인. 모든 수치는 인용 문헌의 2차 전달이므로 설계 근거로 쓰기 전에 원 논문 확인 필요(Tavasci, Liu 원문은 이번에 미열람). 신뢰도: 서지 높음, 수치는 중간(2차).^[inbox/processed/hw-20261022-env-jiang-uav-gnss-review-drones-2026.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[vendor-registry-gnss-imu]]
