---
title: "No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation"
created: 2026-08-19
updated: 2026-08-19
type: paper
item_type: preprint
authors: "Cheng, Feinan; Xu, Dongliang; Nong, Wenli; Zhang, Zhiheng; Liu, Ang; Wang, Tianyu; Yao, Yue"
year: "2026"
doi: "10.48550/arXiv.2607.19288"
url: "http://arxiv.org/abs/2607.19288v1"
zotero_key: ET4FFJK8
tags: ["auto:2nd-brain", "voice-control"]
attachment_path: raw/papers/files/voice-control/no-training-better-flights-test-time-scaled-vlms-for-uav-navigation.pdf
attachment_sha256: 40b46b8f3cb30696ce8d32d6de4f4aad3b3b6b21d3c5048d127db04d7e096b09
sha256: 9f08d3a93fc76f96
---

# No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation

**Authors**: Cheng, Feinan; Xu, Dongliang; Nong, Wenli; Zhang, Zhiheng; Liu, Ang; Wang, Tianyu; Yao, Yue  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2607.19288  
**URL**: http://arxiv.org/abs/2607.19288v1

## Abstract

Test-time scaling offers a promising method to improve the inference performance of Vision-Language Models (VLMs) without additional training. Existing approaches to vision-language navigation (VLN) for Unmanned Aerial Vehicle (UAV) typically relies on a single inference pass, which can falter in complex environments by producing suboptimal or unsafe trajectories. In this paper, we explore a simple and effective approach to apply test-time scaling to VLN for UAV. We enhance navigation reasoning through an iterative refinement process that requires no extra model training, guiding the model to re-evaluate its initial navigation plan for better accuracy and safety. Our method first prompts the model to generate multiple parallel candidates and then performs a self-correction step, achieving deeper and more robust planning without changing the underlying model. To further strengthen decision-making, we design a multi-criteria scoring function to evaluate the refined candidates based on safety, goal alignment, and forward-progress. This simple yet powerful combination enables a frozen UAV navigation VLMs to self-correct and generate more accurate and reliable flight plans, achieving SOTA performance in this task.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
