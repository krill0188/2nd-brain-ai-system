---
title: "UAV 마이크 배열 에고노이즈 참조 음성 향상"
created: 2026-10-17
updated: 2026-10-18
type: concept
domain: hardware
tags: [drone, drone-hw, voice-control]
sources: [inbox/processed/fetch-2026-10-17-arxiv-speech-enhancement-using-ego-noise-references-with-a-microph.md, inbox/processed/fetch-2026-10-18-arxiv-cyclic-mpdr-beamforming-for-suppression-of-almost-cyclostati.md]
confidence: medium
contested: false
contradictions: []
---

# UAV 에고노이즈 참조 음성 향상

**출처**: arXiv 2211.02690 (2022-11-04)

UAV에 내장된 마이크 배열로, 프로펠러 근처 마이크가 포착한 에고노이즈 참조 신호를 사전지식 다채널 위너 필터(PK-MWF)에 넣어 음성 상관행렬을 추정한다.^[inbox/processed/fetch-2026-10-17-arxiv-speech-enhancement-using-ego-noise-references-with-a-microph.md]

## 실험
- 반무향실에서 UAV를 거치대에 고정하고 3가지 프로펠러 회전수(SNR 3단계)로 스피커 음성을 녹음했다. 녹음은 온라인 공개되었다.^[inbox/processed/fetch-2026-10-17-arxiv-speech-enhancement-using-ego-noise-references-with-a-microph.md]
- 음성 존재 확률(SPP)은 외부 마이크(벤치마크) 또는 내장 마이크(현실 시나리오)로 추정한다.^[inbox/processed/fetch-2026-10-17-arxiv-speech-enhancement-using-ego-noise-references-with-a-microph.md]
- 표준 MWF 대비 STOI·PESQ(명료도·품질) 개선이 더 컸고 SNR 개선은 비슷했다.^[inbox/processed/fetch-2026-10-17-arxiv-speech-enhancement-using-ego-noise-references-with-a-microph.md]

## 관련
음성 명령 인터페이스는 [[voice-control-drone]], 탑재체는 [[drone-payload-systems]] 참조.

## 최신 근거 연결 (2026-10-18)

- 비교 대상 접근: 참조 신호 대신 거의 주기적인 모터 소음의 주파수 간 상관을 활용하는 cMPDR. 두 연구는 실험 조건과 지표 구성이 달라 직접 비교할 수 없다: [[cyclic-mpdr-beamforming-uav-motor-noise]]^[inbox/processed/fetch-2026-10-18-arxiv-cyclic-mpdr-beamforming-for-suppression-of-almost-cyclostati.md]
