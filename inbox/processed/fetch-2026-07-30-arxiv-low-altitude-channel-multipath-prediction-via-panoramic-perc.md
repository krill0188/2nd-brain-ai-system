---
title: "Low-Altitude Channel Multipath Prediction via Panoramic Perception and Vision-Language Model"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: comms-protocol
source: http://arxiv.org/abs/2607.21953v1
authors: "Zihang Zeng, Shu Sun, Meixia Tao, Zhiyong Chen, Jianhua Mo, Xiangwen Gu"
published: "2026-07-24"
tags: [drone, comms-protocol, paper, arxiv]
---

# Low-Altitude Channel Multipath Prediction via Panoramic Perception and Vision-Language Model

**Authors**: Zihang Zeng, Shu Sun, Meixia Tao, Zhiyong Chen, Jianhua Mo, Xiangwen Gu
**Published**: 2026-07-24
**arXiv**: http://arxiv.org/abs/2607.21953v1

## Abstract

Unmanned aerial vehicle (UAV) communication is expected to support a wide range of low-altitude applications in 6G mobile networks. However, traditional statistical channel models provide limited accuracy in specific environments, while deterministic methods such as ray tracing usually rely on accurate three-dimensional environment models and involve high computational complexity. Existing multimodal channel prediction approaches mainly focus on large-scale metrics such as path loss, and remain insufficient for modeling small-scale parameters. To address these limitations, this paper proposes PanoLAMP, a Panoramic perception and vision-language model-based Low-Altitude Multipath Prediction framework. It adopts a pretrained vision-language model as the backbone and captures the propagation environment features through panoramic RGB-D observations collected at both the transmitter and receiver to predict the delay, power, azimuth angle, and zenith angle offset relative to the line-of-sight path. Experiments are conducted on a synthetic dataset containing 18,949 UAV-vehicle links across seven UAV altitudes. Experimental results show that the proposed method consistently outperforms representative baselines in both multipath parameters and statistical metrics, and demonstrates stronger generalization across different flight heights.
