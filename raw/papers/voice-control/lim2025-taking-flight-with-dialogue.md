---
title: "Taking Flight with Dialogue: Enabling Natural Language Control for PX4-based Drone Agent"
authors:
  - Shoon Kit Lim
  - Melissa Jia Ying Chong
  - Jing Huey Khor
  - Ting Yang Ling
venue: arXiv
year: 2025
doi: "10.48550/arXiv.2506.07509"
url: "https://arxiv.org/abs/2506.07509"
pdf: "https://arxiv.org/pdf/2506.07509"
topics: [drone-sw, voice-control, ai-agent, ros2]
abstract: |
  Recent advances in agentic and physical artificial intelligence (AI) have largely focused 
  on ground-based platforms such as humanoid and wheeled robots, leaving aerial robots relatively 
  underexplored. Meanwhile, state-of-the-art unmanned aerial vehicle (UAV) multimodal vision-language 
  systems typically rely on closed-source models accessible only to well-resourced organizations. 
  To democratize natural language control of autonomous drones, we present an open-source agentic 
  framework that integrates PX4-based flight control, Robot Operating System 2 (ROS 2) middleware, 
  and locally hosted models using Ollama. We evaluate performance both in simulation and on a 
  custom quadcopter platform, benchmarking four large language model (LLM) families for command 
  generation and three vision-language model (VLM) families for scene understanding.
source_code: "https://github.com/limshoonkit/ros2-agent-ws"
ingested: 2026-07-27
---

# Taking Flight with Dialogue: Enabling Natural Language Control for PX4-based Drone Agent

## Metadata

| 항목 | 내용 |
|------|------|
| **저자** | Shoon Kit Lim, Melissa Jia Ying Chong, Jing Huey Khor, Ting Yang Ling |
| **발행처** | arXiv [cs.RO] |
| **연도** | 2025 |
| **DOI** | 10.48550/arXiv.2506.07509 |
| **PDF** | https://arxiv.org/pdf/2506.07509 |
| **소스코드** | https://github.com/limshoonkit/ros2-agent-ws |

## 주요 내용

### 연구 목표
- PX4 기반 드론의 자연어 제어를 위한 오픈소스 에이전트 프레임워크 개발
- ROS 2 미들웨어와 Ollama를 활용한 로컬 LLM/VLM 통합

### 기술 스택
- **Flight Control**: PX4
- **Middleware**: ROS 2
- **LLM**: Ollama (로컬 호스팅)
- **VLM**: 3가지 비전-언어 모델 패밀리 벤치마크

### 평가
- 시뮬레이션 및 실제 쿼드콥터 플랫폼에서 성능 평가
- 4가지 LLM 패밀리 명령 생성 벤치마크
- 3가지 VLM 패밀리 장면 이해 벤치마크

## 관련 위키 페이지

- [[voice-control-drone]] — 음성 제어 개념
- [[px4-system-architecture]] — PX4 시스템 아키텍처
- [[ros2-drone-integration]] — ROS2 드론 연동
- [[drone-ai-agents]] — 드론 AI 에이전트

## 인용

```bibtex
@article{lim2025taking,
  title={Taking Flight with Dialogue: Enabling Natural Language Control for PX4-based Drone Agent},
  author={Lim, Shoon Kit and Chong, Melissa Jia Ying and Khor, Jing Huey and Ling, Ting Yang},
  journal={arXiv preprint arXiv:2506.07509},
  year={2025}
}
```
