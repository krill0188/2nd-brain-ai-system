---
title: "Electromagnetic Neural Network for Direction-of-Arrival Estimation"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: comms-protocol
source: http://arxiv.org/abs/2607.23021v1
authors: "Shining Lin, Jiancheng An, Lu Gan, Victor C. M. Leung, Mehdi Bennis, M\u00e9rouane Debbah, Tie Jun Cui"
published: "2026-07-25"
tags: [drone, comms-protocol, paper, arxiv]
---

# Electromagnetic Neural Network for Direction-of-Arrival Estimation

**Authors**: Shining Lin, Jiancheng An, Lu Gan, Victor C. M. Leung, Mehdi Bennis, Mérouane Debbah, Tie Jun Cui
**Published**: 2026-07-25
**arXiv**: http://arxiv.org/abs/2607.23021v1

## Abstract

Accurate and real-time direction of arrival (DOA) estimation is crucial for beamforming in unmanned aerial vehicle (UAV) communication systems. However, the existing high-precision DOA estimation algorithms encounter high computational complexity when implemented on a UAV with on-board signal processing constraints. To tackle this issue, an electromagnetic neural network (EMNN) is developed for DOA estimation, which is capable of generating the angular spectrum of the incident signal based solely on amplitude observation. Specifically, the proposed EMNN consists of two components: a stacked intelligent metasurfaces (SIM) is mounted on the UAV, and each meta-atom is an artificial neuron that can process signals in the electromagnetic domain with low energy consumption and ultra-fast computing speed. Furthermore, a fully connected layer is cascaded to process the received amplitude signal, enhancing the non-linear extraction and representational ability of EMNN. Moreover, to reduce the computational complexity and observation snapshots required for high-resolution DOA estimation, we develop a hierarchical DOA estimation framework, which involves two stages for conducting coarse and fine DOA estimation, respectively. For each stage, EMNN is trained on randomly generated training samples and their corresponding spectra to achieve the desired estimation goal. Finally, the simulation results validate that the proposed EMNN achieves approximately 13 dB gain in classification error reduction over the conventional beamforming (CBF) method in dual-signal scenarios, albeit its lower cost and radio frequency (RF)-related power consumption.
