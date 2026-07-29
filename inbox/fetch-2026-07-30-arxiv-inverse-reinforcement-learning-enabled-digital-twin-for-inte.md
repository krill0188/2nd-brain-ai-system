---
title: "Inverse-Reinforcement Learning Enabled Digital Twin for Intent-based Drone Networks"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: comms-protocol
source: http://arxiv.org/abs/2607.17186v1
authors: "Jiahao Wang, Ruimin Yang, Hanzhi Yu, Huaiyu Dai, Ye Hu"
published: "2026-07-19"
tags: [drone, comms-protocol, paper, arxiv]
---

# Inverse-Reinforcement Learning Enabled Digital Twin for Intent-based Drone Networks

**Authors**: Jiahao Wang, Ruimin Yang, Hanzhi Yu, Huaiyu Dai, Ye Hu
**Published**: 2026-07-19
**arXiv**: http://arxiv.org/abs/2607.17186v1

## Abstract

In this paper, the problem of the trajectory design for an intent-based drone operating in resource-constrained, dynamic wireless network environments is studied. In the considered model, the drone acts as a supplementary base station that navigates among ground user clusters to provide on-demand uplink data access. Given its intended application (e.g traffic monitoring), the drone base station (DBS) prioritizes serving certain clusters (e.g. high-risk highway sections). A digital twin (DT) system, hosted on a central server, creates a virtual representation of the physical wireless network environment to simulate and predict related changes, in which case the DBS trajectory should also be adjusted. Then, the DT system suggests adjustments to DBS trajectories without guaranteed access to the underlying DBS intent (i.e., service priorities), as this intent evolves over time and cannot be updated to the DT system in a timely manner due to intermittent connectivity between the DBS and the DT server. Such adjustment is posed as an optimization problem whose goal is to find the trajectories with which the fraction of prioritized users served by the DBS is maximized. To solve this problem under unknown DBS intent and unpredictable environment changes, an inverse reinforcement learning (IRL) based DT actuation solution is proposed. Simulation results demonstrate that the proposed solution provides near-real-time, near-optimal trajectory adjustment, with approximately 85\% less performance loss across environmental changes, compared to traditional reinforcement learning based on-board DBS control. The DT framework also enhances drone network performance by up to 2.5 times, compared to standard drone networks where a DBS operates with its erroneous and delayed environmental sensing.
