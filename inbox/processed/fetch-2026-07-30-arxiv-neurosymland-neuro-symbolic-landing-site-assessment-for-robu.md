---
title: "NEUROSYMLAND: Neuro-Symbolic Landing-Site Assessment for Robust and Edge-Deployable UAV Autonomy"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2607.02277v2
authors: "Weixian Qian, Tianyi Yang, Sebastian Schroder, Yao Deng, Jiaohong Yao, Xiao Cheng, Richard Han, Xi Zheng"
published: "2026-07-02"
tags: [drone, ai-autonomy, paper, arxiv]
---

# NEUROSYMLAND: Neuro-Symbolic Landing-Site Assessment for Robust and Edge-Deployable UAV Autonomy

**Authors**: Weixian Qian, Tianyi Yang, Sebastian Schroder, Yao Deng, Jiaohong Yao, Xiao Cheng, Richard Han, Xi Zheng
**Published**: 2026-07-02
**arXiv**: http://arxiv.org/abs/2607.02277v2

## Abstract

Safe landing-site assessment in unstructured environments remains a key challenge for autonomous UAV deployment, as vision-only learning approaches often degrade under terrain variability and provide limited transparency in safety decisions. We present NEUROSYMLAND, a neuro-symbolic landing-site assessment system that integrates lightweight perception with explicit safety reasoning. The framework constructs a probabilistic semantic scene graph from onboard visual input and evaluates candidate landing regions using symbolic constraints capturing terrain flatness, obstacle clearance, and spatial consistency, enabling structured reasoning under perceptual uncertainty while maintaining edge-feasible execution. Across 72 simulated landing scenarios spanning diverse terrains, NEUROSYMLAND achieves 61 successful assessments, outperforming four competitive baselines (37-57 successes). To evaluate deployability, we further conduct 100 hardware-in-the-loop trials with randomized initial poses, profiling end-to-end latency, stage-wise execution time, and system-level metrics including CPU/GPU utilization, memory footprint, and power consumption. Results demonstrate improved robustness and interpretability with bounded edge-resource usage. Profiling shows that symbolic reasoning contributes only a small fraction of end-to-end latency, while the main computational cost arises from perception and PSSG construction. These results demonstrate the feasibility of deploying the landing-site assessment stack on edge-constrained UAV hardware, and all source code, datasets, prompts, and symbolic rule refinement examples are released in an open-source repository
