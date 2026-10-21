---
title: "Most resilient GNSS receiver: results from JammerTest in Norway (Septentrio)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
tags: [drone, gnss, jammertest, aim-plus, anti-jam-antenna]
sources: [inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]
confidence: medium
contested: false
contradictions: []
---

# Most resilient GNSS receiver: results from JammerTest in Norway (Septentrio)

- 원문: https://www.septentrio.com/en/learn-more/insights/most-resilient-gnss-receiver-results-jammertest-norway^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]
- 저자: Septentrio (제조사 보도·해설, 개별 저자 없음)^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]
- 발행: JammerTest 2023 결과 글(게재일 미확인)^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]

## 핵심 내용
출처 유형: 제조사 기술 해설 페이지(Septentrio). septentrio.com 직접 접속은 403이라 web.archive.org 보관본(2026 스냅샷)으로 열람. 제조사 주장이며 독립 검증 아님.^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]

Norway Andøya 섬 JammerTest 2023(5일, 정부 주관 실제 간섭 시험)에서 Septentrio 수신기의 재밍·스푸핑 대응을 제시한 글. 1일간 집중 재밍 시험에서 AIM+ 수신기가 '99,5% positioning availability'를 보였다고 서술한다. 자동차 탑재 시험에서 경쟁 GNSS/INS 수신기는 두 번 위치를 잃었다고 주장.^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 'cigarette lighter' 형 저가 재머: 출력 10~15 dBm, GPS L1·L2 교란. 그 외 GNSS 신호보다 1,000만 배 강한 고출력 재머 시험도 수행.^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]
- 안티재밍 안테나 시험: 간섭 약 10 dB 감소 효과. 수신기 기술(AIM+)이 핵심이고 안테나는 보조 역할이며, 안티재밍 안테나는 광대역 백색잡음형 재밍에 효과적이나 다른 유형에는 덜 효과적이라고 서술.^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]
- 표준 광대역 헬리컬 안테나 + AIM+ 없음: 재밍 시 즉시 추적 상실. 같은 안테나 + AIM+: 추적·측위 유지. AIM+ + 안티재밍 안테나: 신호 품질 추가 개선.^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]
- 스푸핑: 경쟁 수신기 스푸핑 플래그가 시험 중 한 번도 켜지지 않았고, 10 m 이상 오차 위치를 상당 시간 출력했다고 주장(Septentrio는 모든 대오차 사례를 플래그했다고 주장).^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]
- 드론: 재밍된 드론은 통제 상실·추락 또는 hover/land/circle 모드 전환 가능하다는 서술.^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]

## 한계·미확인
제조사 자체 결과 요약이며 시험 보고서 원문·측정 수치(전력별 거리·dB)는 없음. 경쟁사 이름 비공개. 군 시험은 비공개라 결과를 공유할 수 없다는 언급이 있음. 소형 드론 탑재 시험 결과 아님(차량 탑재).^[inbox/processed/hw-20261021-jamming-septentrio-jammertest-2023-results-page.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
