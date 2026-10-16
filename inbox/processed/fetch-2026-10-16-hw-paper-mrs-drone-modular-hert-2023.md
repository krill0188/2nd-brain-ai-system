---
title: "MRS Drone: A Modular Platform for Real-World Deployment of Aerial Multi-Robot Systems"
created: 2026-10-16
captured: 2026-10-16
type: paper
domain: hardware
source: https://arxiv.org/abs/2306.07229
authors: "Daniel Hert, Tomas Baca, Pavel Petracek, Vit Kratky, Robert Penicka, Vojtech Spurny, Matej Petrlik, Matous Vrba, et al., Martin Saska"
published: "2023-06-12"
tags: [drone, hardware, paper, modular-platform, frame, payload, multi-robot, real-world]
---

# MRS Drone: A Modular Platform for Real-World Deployment of Aerial Multi-Robot Systems

## 핵심 내용 (방법·결과)

실내외 자율 비행 및 다중 로봇 운용을 위한 모듈형 UAV 플랫폼(MRS Drone)의 기계적·전기적 설계와 소프트웨어 아키텍처를 소개했다. 액추에이터, 프레임, 센서 구성을 교체할 수 있는 모듈성이 핵심이며 비행 전 시뮬레이터도 포함한다. Journal of Intelligent & Robotic Systems 2023, vol. 108, issue 64에 게재.

**공개된 프레임별 하드웨어 사양:**
- **F450 (소형):** 페이로드 약 0.5 kg, 비행 시간 10~15분 (페이로드에 따라 변동)
- **X500 (중형):** 컴팩트함과 페이로드의 균형점
- **T650 (대형):** MRS 표준 플랫폼 중 최고 중량, 페이로드 2.5 kg

## 설계에 쓸 수 있는 지침

- **프레임 급별 페이로드-체공 시간 트레이드오프 실측값:** F450급(~500g 페이로드)→10~15분, T650급(~2.5kg 페이로드)→더 짧음.
- 모듈형 설계 채택 시: 센서·컴퓨터 탑재 변경을 프레임 교체 없이 가능 → 연구/운용 비용 절감.
- 실세계 다중 로봇 배치를 검증한 플랫폼으로, 동일 급 기체 설계의 기준 사례로 활용 가능.

## 한계·미확인 항목

- X500의 구체적 페이로드 수치: 미확인 (초록 미기재).
- 각 프레임의 모터·프로펠러·배터리 세부 부품 번호: 미확인 (PDF 본문 확인 필요).
- 비행 시간은 F450 기준 범위 제공; T650·X500 비행 시간: 미확인.
