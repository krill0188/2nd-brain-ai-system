---
title: "Veloxity: Rust 기반 메모리 안전 UAV 오토파일럿"
created: 2026-11-03
updated: 2026-11-03
type: concept
domain: flight-control
tags: [drone-sw, drone]
sources: [inbox/processed/fetch-2026-11-03-arxiv-veloxity-towards-memory-safe-uav-embedded-firmware-using-the.md]
confidence: low
contested: false
contradictions: []
---

# Veloxity: Rust 기반 메모리 안전 UAV 오토파일럿

Ward 등(arXiv 2610.41053, 2026-10-29)이 제안한 오픈소스 임베디드 UAV 오토파일럿으로, 메모리 안전 언어인 Rust로 작성되었다. 초록 기준 요약이며 본문은 확인하지 않았다.^[inbox/processed/fetch-2026-11-03-arxiv-veloxity-towards-memory-safe-uav-embedded-firmware-using-the.md]

## 문제의식
- 메모리 안전 언어는 안전 필수 시스템에서 오류 부류 전체를 제거할 수 있지만, 항공우주(특히 UAV)에서는 채택이 단편적이다.
- 기존 Rust UAV 프로젝트는 시뮬레이션 전용이거나 비공개이거나, 기존 자율 비행 생태계와 통합·C/C++ 펌웨어 대비 검증이 되어 있지 않았다.

## 기여와 결과
- 자율 UAV를 위한 최소·모듈형 기반을 제공해 메모리 안전 언어 도입 장벽을 낮춘다.
- 동등한 C++ 오토파일럿과 시뮬레이션, 하드웨어 테스트벤치, 야외 웨이포인트 추종 비행으로 비교해 **기능 동등성과 성능 개선**을 보였다고 주장한다(구체 수치는 초록에 없음).

## 맥락
C/C++ 기반의 대표 오픈소스 스택은 [[px4-flight-stack]]과 [[ardupilot]]이다. 컴패니언 계층 통합은 [[companion-computer]]를 참조한다.
