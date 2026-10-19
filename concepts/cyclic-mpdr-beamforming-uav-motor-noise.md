---
title: "cMPDR 빔포밍: 거의 주기정상 음향 간섭(UAV 모터) 억제"
created: 2026-10-18
updated: 2026-10-18
type: concept
domain: hardware
tags: [drone, drone-hw]
sources: [inbox/processed/fetch-2026-10-18-arxiv-cyclic-mpdr-beamforming-for-suppression-of-almost-cyclostati.md]
confidence: medium
contested: false
contradictions: []
---

# cMPDR 빔포밍 (UAV 모터 소음)

**출처**: arXiv 2510.18391 v3 (2025-10-21), Bologni 외. 초록 기준.

엔진·팬·악기처럼 거의 주기적인 소음원은 주파수 성분 간 상관이 있는 (거의) 주기정상(ACS) 과정으로 모델링할 수 있으나, 기존 빔포머는 주파수 빈을 독립 처리한다.^[inbox/processed/fetch-2026-10-18-arxiv-cyclic-mpdr-beamforming-for-suppression-of-almost-cyclostati.md]

- **방법**: 공간·스펙트럼 상관을 함께 쓰는 cyclic MPDR(cMPDR). FRESH 필터링 기반이며, 부분음이 정수배에서 벗어나는 비조화성은 주기도에서 공진 주파수를 추정해 주파수 이동량을 구해 처리한다. 이론적으로 잔여 잡음의 닫힌 해와 순환 성분 수에 따른 출력 전력의 단조 감소를 증명했다.
- **결과**: 합성 조화 잡음과 실제 UAV 모터 녹음에서, 저 SNR 조건에서 MPDR 대비 SI-SDR 최대 5 dB 개선, STOI 이득을 보였고 단일 마이크에서도 효과가 있다. 스펙트럼 상관이 없으면 기존 MPDR로 환원되어 성능이 떨어지지 않는다.
- 코드와 오디오 샘플은 저자 GitHub(Screeen/cMPDR)에 공개되어 있다고 밝혔다.

관련: [[uav-ego-noise-speech-enhancement]], [[voice-control-drone]].
