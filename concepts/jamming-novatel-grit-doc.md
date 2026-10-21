---
title: "NovAtel GRIT - GNSS Resilience and Integrity Technology (제품군 설명)"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: security
tags: [drone, gnss, novatel]
sources: [inbox/processed/hw-20261021-jamming-novatel-grit-doc.md]
confidence: medium
contested: false
contradictions: []
---

# NovAtel GRIT - GNSS Resilience and Integrity Technology (제품군 설명)

- 원문: https://novatel.com/products/grit^[inbox/processed/hw-20261021-jamming-novatel-grit-doc.md]
- 저자: NovAtel (Hexagon)^[inbox/processed/hw-20261021-jamming-novatel-grit-doc.md]
- 발행: 미확인 (열람일 2026-10-21, web.archive.org 2026 스냅샷)^[inbox/processed/hw-20261021-jamming-novatel-grit-doc.md]

## 핵심 내용
GRIT 는 OEM 수신기 펌웨어 기반 재밍·스푸핑 대응 묶음이다. 구성: Interference Toolkit(ITK, 간섭 주파수 식별·특성화), Spoofing Detection, Time-Tagged Digitized Samples(ADC 샘플의 시간표기 스냅샷으로 재밍 신호 특성 분석 및 자체 간섭 위치추정 알고리즘 개발). 디지털 필터로 간섭 완화를 적용하고, NovAtel Application Suite 의 GRIT Monitor 대시보드로 RF 환경을 시각화한다. 페이지는 "Advanced versions of firmware are available exclusively for defence customers" 라고 밝힌다. 공식 페이지는 직접 접속 403이라 보관본으로 열람.^[inbox/processed/hw-20261021-jamming-novatel-grit-doc.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 수치 없음. 기능 수준 설명만 확인됨.^[inbox/processed/hw-20261021-jamming-novatel-grit-doc.md]
- 하드웨어 측 재밍 방어는 같은 사이트의 GAJT 안티재밍 안테나와 함께 쓰는 구성(GAJT-AE3 페이지: OEM7 + GRIT 펌웨어 조합 언급).^[inbox/processed/hw-20261021-jamming-novatel-grit-doc.md]

## 한계·미확인
스푸핑 탐지 방식(알고리즘), 탐지율, 지원 수신기 모델 목록, 상용 구매 조건은 이 페이지에 없음(미확인). Spoofing Detection 하위 페이지는 보관본이 비어 있어 열람 못함.^[inbox/processed/hw-20261021-jamming-novatel-grit-doc.md]

상위 허브: [[gnss-engineering-hub]] · 함께 보기: [[kci-dual-nis-sac-gnss-ins-spoofing]]
