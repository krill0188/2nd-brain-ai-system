---
title: "How to Model Your Crazyflie Brushless"
created: 2026-10-17
captured: 2026-10-17
type: paper
domain: hardware
source: http://arxiv.org/abs/2603.05944v1
authors: "Alexander Gr\u00e4fe, Christoph Scherer, Wolfgang H\u00f6nig, Sebastian Trimpe"
published: "2026-03-06"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/how-to-model-your-crazyflie-brushless.pdf
attachment_type: pdf
attachment_sha256: fa0bb08449c6876ece808a2b1130b4a1bd5a6f97de145eba0c92e04466b25af6
---

# How to Model Your Crazyflie Brushless

**Authors**: Alexander Gräfe, Christoph Scherer, Wolfgang Hönig, Sebastian Trimpe
**Published**: 2026-03-06
**arXiv**: http://arxiv.org/abs/2603.05944v1

## Abstract

The Crazyflie quadcopter is widely recognized as a leading platform for nano-quadcopter research. In early 2025, the Crazyflie Brushless was introduced, featuring brushless motors that provide around 50% more thrust compared to the brushed motors of its predecessor, the Crazyflie 2.1. This advancement has opened new opportunities for research in agile nano-quadcopter control. To support researchers utilizing this new platform, this work presents a dynamics model of the Crazyflie Brushless and identifies its key parameters. Through simulations and hardware analyses, we assess the accuracy of our model. We furthermore demonstrate its suitability for reinforcement learning applications by training an end-to-end neural network position controller and learning a backflip controller capable of executing two complete rotations with a vertical movement of just 1.8 meters. This showcases the model's ability to facilitate the learning of controllers and acrobatic maneuvers that successfully transfer from simulation to hardware. Utilizing this application, we investigate the impact of domain randomization on control performance, offering valuable insights into bridging the sim-to-real gap with the presented model. We have open-sourced the entire project, enabling users of the Crazyflie Brushless to swiftly implement and test their own controllers on an accurate simulation platform.
