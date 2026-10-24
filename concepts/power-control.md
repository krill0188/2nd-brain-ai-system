---
title: "Power Control"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags: [power-control, otfs, sinr-feedback, uav-communications, high-mobility]
sources: []
confidence: medium
contradictions: []
domain: comms-protocol
contested: false
---

# Power Control

Power control in OTFS-enabled UAV communications is a delayed SINR-feedback-driven framework designed to maintain reliability and fairness under high-mobility conditions, where transmit-power vectors are adjusted based on outdated channel measurements rather than instantaneous channel state information.

## 개요

This paper presents a power control scheme specifically for orthogonal time frequency space (OTFS) modulation applied to unmanned aerial vehicle (UAV) communications. Operating under high mobility, the system faces rapidly changing channel conditions due to three-dimensional propagation geometry, including path delays and Doppler shifts. Instead of requiring instantaneous channel state information (CSI), the proposed controller refreshes the transmit-power vector using delayed SINR (signal-to-interference-plus-noise ratio) measurements alone, aligning with the practical limitations of fast-fading aerial links. A key mechanism of this framework is the prediction-smoothing-projection rule, which integrates three normalized utility shares—reliability, fairness, and spectral efficiency—to directly control closed-loop power adjustments. Simulation results indicate that the effective SINR of OTFS changes 37.8% less per frame compared to orthogonal frequency division multiplexing (OFDM) systems, demonstrating improved stability.

## 핵심 특징

- **지연된 SINR 피드백**: instantaneous CSI가 아닌 delayed SINR measurements을 기반으로 전송 전력 벡터를 새로 고침합니다.
- **OTFS 매핑**: uniform linear array를 갖는 기지국이 공통 OTFS 프레임 상에서 여러 UAV에 서비스를 제공합니다.
- **예측-부감-사상 규칙**: reliability share, fairness share, spectral-efficiency share를 혼합하여 유틸리티 가중치가 닫힌 루프를 직접 제어하도록 합니다.
- **높은 모빌리티 안정성**: SIMULATION 결과, OTFS의 effective SINR이 frame당 37.8% 적게 변화하여 OFDM 대비 안정성이 향상됨을 보입니다.

## 관계

- Power Control --[APPLIES_TO]--> OTFS
- Power Control --[USES]--> SINR Feedback
- Power Control --[USES]--> Channel State Information (지연된 정보 사용)
- Prediction-Smoothing-Projection --[IMPLEMENTS]--> Power Control
- Reliability --[DESIGN_OBJECTIVE]--> Power Control
- Fairness --[DESIGN_OBJECTIVE]--> Power Control
- Spectral Efficiency --[DESIGN_OBJECTIVE]--> Power Control

## 출처

- (사용자 재확인 필요) Le, Thuan Van; Luong, Nguyen Cong; Hoang, Trong-Dai; Bao, Vo Nguyen Quoc; Huynh-The, Thien; Li, Xingwang; Tu, Ngo Hoang. "OTFS-Enabled Delayed SINR-Feedback Power Control for Reliable and Fair High-Mobility UAV Communications." arXiv preprint arXiv:2609.22309 (2026).

## 분류

- [[auto-hub-technology]] — 자동 추출 분류
- [[auto-hub-source-papers]] — 출처 유형
