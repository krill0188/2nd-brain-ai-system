---
title: "Chained Attacks on Drone-Based Federated Learning: From Network Disruption to Device Impersonation"
created: 2026-10-22
updated: 2026-10-22
type: concept
domain: ai-autonomy
tags: [drone, federated-learning, deauthentication, impersonation, availability-attack, raspberry-pi, jetson, flower, physical-testbed]
sources: [inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]
confidence: medium
contested: false
contradictions: []
---

# Chained Attacks on Drone-Based Federated Learning: From Network Disruption to Device Impersonation

- 원문: https://arxiv.org/abs/2607.20280^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]
- 저자: Suleiman Muhammad Sabo, Hamed Alkharsh, Peilin Li, Chuadhry Mujeeb Ahmed, Aydin Abadi, Shishir Nagaraja, Rajiv Ranjan^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]
- 발행: 2026-07-22^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]

## 핵심 내용 (arXiv HTML 전문 열람)
실제 무선 하드웨어에서 수행한 연합학습(FL) 공격 실험이지만 비행하지 않는 "드론 대용(surrogate)" 장치 사용. 본문 방법 절 문구: "Raspberry Pi and NVIDIA Jetson devices as drone surrogates", 이유는 취약점이 802.11 링크 계층과 FL 클라이언트 인증 계층에 있어 기체 동역학·비행제어·공중 전파에 의존하지 않기 때문이라고 명시.^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]
- 테스트베드: Raspberry Pi 4B 10대(+PC 워크스테이션 FL 서버) 클러스터, NVIDIA Jetson 8대(클라이언트 7 + SuperLink 서버 1) 클러스터, 공격자는 모니터 모드 어댑터(RTL8812AU) 장착 Raspberry Pi. Flower 프레임워크, 동기식 FedAvg, 격리된 802.11 네트워크.^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]
- 공격 1단계(가용성): aireplay-ng 로 802.11 deauthentication 주입, 라운드당 대상 클라이언트 비율(intensity)을 조절. 결과(10라운드): Raspberry Pi 기준 정확도 57.00% 가 지속 공격 하에 49.80% (-7.20%), Jetson 기준 73.40% 가 71.10% (-2.30%). RPi는 강도 80%까지, Jetson은 60%까지 평가(더 높은 강도는 추가 열화가 미미했다고 서술). 비IID에서 데이터가 집중된 "expert node" 를 끊으면 클래스별 모델 열화가 더 큼.^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]
- 공격 2단계(신원 위장): 단일 요소 인증(키 소지만으로 인증)은 연결이 끊긴 드론 자리를 추출한 자격증명으로 탐지 없이 대체 가능함을 확인. TLS·EC 키쌍 기반 서명 구성을 추가한 확장 설정에서 시험.^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]
- 윤리 절·논의 절 존재, 방어는 "future work"(클라이언트 측 검증, 하드웨어 연속성 암호 증명, 차분 프라이버시 등 제안만).^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]

## 설계·운용에 쓸 수 있는 지침 (원문 수치만)
- 드론 FL의 무선 링크가 Wi-Fi(802.11)면 관리 프레임 위조로 라운드 중 클라이언트를 끊을 수 있고, 단순 키 보유 인증은 불충분하다는 실측 근거(대용 장치 기준).^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]

## 한계·미확인
- 비행 기체·비행 중 시험 아님(대용 장치) → "실기체 UAV FL 보안 실증"에는 해당하지 않음(conv-fl-uav-real-airframe-attack-evidence-check 참조). 위 정확도는 소형 모델/데이터 설정이며 모델·데이터셋 세부는 이 파일에 미전사. 신뢰도 중상(arXiv 프리프린트, 심사 여부 미확인).^[inbox/processed/hw-20261022-ai-fl-uav-real-hardware-chained-attacks-sabo-2026.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[swarm-coordination]]
