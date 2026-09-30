---
title: "DroneWAM: Efficient World Action Model for Drone Visual Navigation"
created: 2026-09-30
captured: 2026-09-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2609.33148v1
authors: "Liang Yao, Fan Liu, Hongbo Lu, Wei Xu, Jianyu Jiang, Yijun Shen, Chuanyi Zhang, Pai Peng"
published: "2026-09-27"
tags: [drone, ai-autonomy, paper, arxiv]
---

# DroneWAM: Efficient World Action Model for Drone Visual Navigation

**Authors**: Liang Yao, Fan Liu, Hongbo Lu, Wei Xu, Jianyu Jiang, Yijun Shen, Chuanyi Zhang, Pai Peng
**Published**: 2026-09-27
**arXiv**: http://arxiv.org/abs/2609.33148v1

## Abstract

World-action models give visual navigation agents a way to anticipate how candidate actions will change future observations and to act from the predicted consequences. For drones, this capability must operate under tight accuracy and efficiency constraints. We present DroneWAM, an efficient world-action model for drone visual navigation. DroneWAM adopts a JEPA-based architecture to model future states directly in representation space, avoiding the cost of explicit future image generation. A pretrained Resampler further compresses dense encoder features into fewer latent tokens, reducing the computation repeated at each imagined step. We also introduce adaptive rollout, where a preference-trained Gate adaptively allocates prediction depth according to the current scene. To support learning under richer aerial motion, we construct DroneNav-6D, a simulated visual navigation dataset with synchronized RGB observations, 6-DoF flight trajectories, control commands, and randomized wind disturbances. On DroneNav-6D, DroneWAM achieves the best trajectory accuracy among the compared methods. Adaptive rollout further reduces the average prediction depth from 8 to 4.58 while improving trajectory accuracy, demonstrating that predictive computation can be allocated more effectively across scenes. \href{https://github.com/1e12Leon/DroneWAM}{Codes and data} will be released.
