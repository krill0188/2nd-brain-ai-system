---
title: "No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: voice-control
source: http://arxiv.org/abs/2607.19288v1
authors: "Feinan Cheng, Dongliang Xu, Wenli Nong, Zhiheng Zhang, Ang Liu, Tianyu Wang, Yue Yao"
published: "2026-07-21"
tags: [drone, voice-control, paper, arxiv]
---

# No Training, Better Flights: Test-Time Scaled VLMs for UAV Navigation

**Authors**: Feinan Cheng, Dongliang Xu, Wenli Nong, Zhiheng Zhang, Ang Liu, Tianyu Wang, Yue Yao
**Published**: 2026-07-21
**arXiv**: http://arxiv.org/abs/2607.19288v1

## Abstract

Test-time scaling offers a promising method to improve the inference performance of Vision-Language Models (VLMs) without additional training. Existing approaches to vision-language navigation (VLN) for Unmanned Aerial Vehicle (UAV) typically relies on a single inference pass, which can falter in complex environments by producing suboptimal or unsafe trajectories. In this paper, we explore a simple and effective approach to apply test-time scaling to VLN for UAV. We enhance navigation reasoning through an iterative refinement process that requires no extra model training, guiding the model to re-evaluate its initial navigation plan for better accuracy and safety. Our method first prompts the model to generate multiple parallel candidates and then performs a self-correction step, achieving deeper and more robust planning without changing the underlying model. To further strengthen decision-making, we design a multi-criteria scoring function to evaluate the refined candidates based on safety, goal alignment, and forward-progress. This simple yet powerful combination enables a frozen UAV navigation VLMs to self-correct and generate more accurate and reliable flight plans, achieving SOTA performance in this task.
