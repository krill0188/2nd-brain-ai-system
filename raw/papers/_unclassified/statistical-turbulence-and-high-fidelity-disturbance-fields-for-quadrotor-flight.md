---
title: "Statistical Turbulence and High-Fidelity Disturbance Fields for Quadrotor Flight Control"
created: 2026-10-10
updated: 2026-10-10
type: paper
item_type: preprint
authors: "Huang, Xun"
year: "2026"
doi: "10.48550/arXiv.2610.06874"
url: "http://arxiv.org/abs/2610.06874v1"
zotero_key: ESPKIGKA
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/_unclassified/statistical-turbulence-and-high-fidelity-disturbance-fields-for-quadrotor-flight.pdf
attachment_sha256: 2ee6b350ef50cbd39b8fc90381853ef4a18bd1def4dbaf3550097a95e1202d74
sha256: 8ab73f7c03b2e0cf
---

# Statistical Turbulence and High-Fidelity Disturbance Fields for Quadrotor Flight Control

**Authors**: Huang, Xun  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2610.06874  
**URL**: http://arxiv.org/abs/2610.06874v1

## Abstract

Reinforcement-learning quadrotor controllers are usually trained under simplified wind models, yet the impact of wind-field fidelity, as opposed to magnitude, on policy robustness remains unquantified. This paper compares five disturbance-fidelity levels, from wind-free flight and discrete 1-cosine gusts through statistical turbulence and synthetic coherent structures to large-eddy-simulation fields of the atmospheric boundary layer, in a full cross-fidelity train test evaluation of proximal policy optimization (PPO) agents, with cascaded PID and geometric SE(3) controllers as training-free references, over a 0-12 m/s wind sweep. Before any controller comparison is made, all disturbance data are validated: every synthetic generator is checked quantitatively against its analytical or certification-standard reference, and the large-eddy-simulation fields against the imposed log law. On a racing-class quadrotor in hover, the train test matrix is remarkably flat, and the cheapest structured training wind, which is discrete-gust domain randomization, ranks first in every test column, a ranking replicated on a wind-sensitive 27 g platform; a once-tuned geometric controller brackets the learned PPO policies at zero crash rate. Mechanism diagnostics show that control authority, not wind realism, bounds robustness, so wind-fidelity investment should scale with platform wind sensitivity.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
