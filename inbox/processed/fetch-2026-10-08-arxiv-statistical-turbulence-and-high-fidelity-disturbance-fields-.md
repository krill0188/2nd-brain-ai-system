---
title: "Statistical Turbulence and High-Fidelity Disturbance Fields for Quadrotor Flight Control"
created: 2026-10-08
captured: 2026-10-08
type: paper
domain: flight-control
source: http://arxiv.org/abs/2610.06874v1
authors: "Xun Huang"
published: "2026-09-09"
tags: [drone, flight-control, paper, arxiv]
attachment_path: raw/papers/files/flight-control/statistical-turbulence-and-high-fidelity-disturbance-fields-.html
attachment_type: html
attachment_sha256: 487d81e392468e7080965280056d76216d7d105764370de963c131a4e2e161b6
---

# Statistical Turbulence and High-Fidelity Disturbance Fields for Quadrotor Flight Control

**Authors**: Xun Huang
**Published**: 2026-09-09
**arXiv**: http://arxiv.org/abs/2610.06874v1

## Abstract

Reinforcement-learning quadrotor controllers are usually trained under simplified wind models, yet the impact of wind-field fidelity, as opposed to magnitude, on policy robustness remains unquantified. This paper compares five disturbance-fidelity levels, from wind-free flight and discrete 1-cosine gusts through statistical turbulence and synthetic coherent structures to large-eddy-simulation fields of the atmospheric boundary layer, in a full cross-fidelity train test evaluation of proximal policy optimization (PPO) agents, with cascaded PID and geometric SE(3) controllers as training-free references, over a 0-12 m/s wind sweep. Before any controller comparison is made, all disturbance data are validated: every synthetic generator is checked quantitatively against its analytical or certification-standard reference, and the large-eddy-simulation fields against the imposed log law. On a racing-class quadrotor in hover, the train test matrix is remarkably flat, and the cheapest structured training wind, which is discrete-gust domain randomization, ranks first in every test column, a ranking replicated on a wind-sensitive 27 g platform; a once-tuned geometric controller brackets the learned PPO policies at zero crash rate. Mechanism diagnostics show that control authority, not wind realism, bounds robustness, so wind-fidelity investment should scale with platform wind sensitivity.
