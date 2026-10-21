---
title: "OpenVLA: An Open-Source Vision-Language-Action Model"
created: 2026-10-21
updated: 2026-10-21
type: concept
domain: ai-autonomy
ontology_class: AIModel
tags: [drone, ai, vla, robot-policy, quantization]
sources: [inbox/processed/hw-20261021-model-openvla.md]
confidence: medium
contested: false
contradictions: []
---

# OpenVLA: An Open-Source Vision-Language-Action Model

- 원문: https://arxiv.org/abs/2406.09246^[inbox/processed/hw-20261021-model-openvla.md]
- 제작: Stanford / UC Berkeley / TRI / Google DeepMind / MIT 등 (Moo Jin Kim 외 18명)^[inbox/processed/hw-20261021-model-openvla.md]

## 핵심 사양 (초록)
| 항목 | 값 |
|---|---|
| 파라미터 | 7B, 970k 실제 로봇 시연 데이터로 학습 |
| 구성 | Llama 2 언어모델 + DINOv2·SigLIP 융합 비전 인코더 |
| 비교 | RT-2-X(55B) 대비 29개 과제 절대 성공률 +16.5%, 파라미터 7배 적음 |
| 미세조정 | Diffusion Policy 대비 +20.4% |
| 효율 | LoRA로 소비자 GPU 미세조정, 양자화 서빙 시 하류 성공률 저하 없음(원문 주장) |
제출 2024-06-13, v3 2024-09-05. 체크포인트·노트북·PyTorch 코드 공개.^[inbox/processed/hw-20261021-model-openvla.md]
## 비고(미확인)
입력 해상도, 라이선스, 엣지(Jetson) 속도 초록에 없음(미확인). 드론 적용은 초록에 없고 로봇 팔 조작 중심(드론 직접 적용 사례 미확인).^[inbox/processed/hw-20261021-model-openvla.md]

상위 허브: [[ai-drone-models-hub]] · 함께 보기: [[test-time-scaling-vlm-uav]]
