---
title: "Taking Flight with Dialogue: Enabling Natural Language Control for PX4-based Drone Agent"
created: 2026-10-21
captured: 2026-10-21
type: paper
domain: ai-autonomy
source: https://arxiv.org/abs/2506.07509
authors: Shoon Kit Lim, Melissa Jia Ying Chong, Jing Huey Khor, Ting Yang Ling
published: 2025-06-09
tags: [drone, llm, vlm, px4, ros2, ollama, open-source]
---
## 핵심 내용
항공 로봇은 에이전트형 물리 AI 연구에서 덜 다뤄졌고, 주요 UAV 비전-언어 시스템은 폐쇄형 모델에 의존한다는 문제의식. PX4 비행제어, ROS 2, Ollama로 로컬 호스팅한 모델을 결합한 오픈소스 에이전트 프레임워크를 제안. 시뮬레이션과 커스텀 쿼드콥터에서 시험, 명령 생성용 LLM 4계열과 장면 이해용 VLM 3계열을 벤치마크.

## 설계·운용에 쓸 수 있는 지침 (원문에 있는 수치만)
- 초록에서 확인되는 수치: LLM 4계열, VLM 3계열 비교.

## 한계·미확인
- 성공률 등 세부 결과 수치는 초록에서 미확인(검색 요약에는 최고 임무 성공률 40%, DeepSeek-LLM 유효 명령 38% 언급이 있으나 직접 열람 안 함). 실기 비행 규모 미확인.
