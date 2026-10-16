---
title: "Micro Neural Policies for Safe Real-Time Robotic Control"
created: 2026-10-08
captured: 2026-10-08
type: paper
domain: flight-control
source: http://arxiv.org/abs/2610.08541v1
authors: "Hongpeng Cao, Riccardo Curcio, Daniele Ottaviano, Marco Caccamo"
published: "2026-10-06"
tags: [drone, flight-control, paper, arxiv]
attachment_path: raw/papers/files/flight-control/micro-neural-policies-for-safe-real-time-robotic-control.html
attachment_type: html
attachment_sha256: 48a6f2ad2c43b412c01b795b1f169aa00c8ac135db6ff1d2f4f20e0c40c1cc5d
---

# Micro Neural Policies for Safe Real-Time Robotic Control

**Authors**: Hongpeng Cao, Riccardo Curcio, Daniele Ottaviano, Marco Caccamo
**Published**: 2026-10-06
**arXiv**: http://arxiv.org/abs/2610.08541v1

## Abstract

In this paper, we investigate the synthesis of Micro Neural Policies (MNP) to enable safe and robust real-time robotic control on computationally constrained embedded devices. We demonstrate that integrating Evolution Strategy (ES) and Statistical Model Checking (SMC)-based verification for policy search can drastically reduce neural network size without compromising safety and robustness. We conduct a large-scale training and evaluation of MNP on Cartpole and Quadrotor control tasks, varying control frequencies and network architectures. After validating these policies in simulation, we evaluate their deployability through zero-shot transfer to physical systems. Our experiments show that MNP can successfully achieve safe sim-to-real transfer without sacrificing control performance. We then show that the policies' memory footprint, ranging from 0.5 to 7.5 kB, allows deployment on microcontrollers, where they achieve real-time inference latency with under 25 ns of jitter while leaving the chip idle for over 97% of the time for additional workloads. This makes them a highly practical solution for severely resource-constrained robotic systems.
