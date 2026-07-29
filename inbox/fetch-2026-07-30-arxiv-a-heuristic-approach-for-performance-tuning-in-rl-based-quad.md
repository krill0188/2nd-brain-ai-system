---
title: "A Heuristic Approach for Performance Tuning in RL-based Quadrotor Control via Reward Design and Termination Conditions"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2605.19166v1
authors: "Fausto Mauricio Lagos Suarez, Akshit Saradagi, Vidya Sumathy, George Nikolakopoulos"
published: "2026-05-18"
tags: [drone, flight-control, paper, arxiv]
---

# A Heuristic Approach for Performance Tuning in RL-based Quadrotor Control via Reward Design and Termination Conditions

**Authors**: Fausto Mauricio Lagos Suarez, Akshit Saradagi, Vidya Sumathy, George Nikolakopoulos
**Published**: 2026-05-18
**arXiv**: http://arxiv.org/abs/2605.19166v1

## Abstract

Reinforcement learning (RL)-based quadrotor control policies have achieved impressive performance in tasks such as fast navigation in cluttered environments and drone racing, where the focus is on speed and agility. However, in several applications, such as infrastructure inspection, it is critical to achieve precise, controlled maneuvers with tunable performance. In this article, we present a novel heuristic approach to achieve tunable performance in RL-based Quadrotor control through reward design and termination conditions. We present a novel reward structure containing dual bandwidth exponentials that achieves a baseline critically damped response in setpoint tracking, with low steady-state errors. When trained with a Proximal Policy Optimization (PPO) algorithm, in conjunction with episode truncation conditions, the desired performance is achieved in 6 million time steps in a sample-efficient manner. In order to tune the performance about the baseline behavior, we present intuitive heuristic rules to adjust the reward weights and exponential coefficients to achieve faster (acrobatic-like) and slower (inspection-like) settling time performance, while retaining the baseline critically damped response and approximately 2\% steady-state error. We evaluate the three RL policies (baseline, acrobatic, and inspection) across 100 trials and show accurate and tunable performance in position and yaw tracking from random initial conditions, thereby demonstrating the effectiveness of the proposed heuristic approach.
