---
title: "From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response"
created: 2026-10-18
captured: 2026-10-18
type: paper
domain: hardware
source: http://arxiv.org/abs/2606.25957v1
authors: "Samuel Tovey, Stefan Prestel, Hiroshi Yamauchi"
published: "2026-06-24"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/from-rubble-simulation-to-active-magnetic-mapping-quantum-se.html
attachment_type: html
attachment_sha256: f26200a2ddc309a00b87284271bdb0300b2734308807a78543c3310a996665ec
---

# From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response

**Authors**: Samuel Tovey, Stefan Prestel, Hiroshi Yamauchi
**Published**: 2026-06-24
**arXiv**: http://arxiv.org/abs/2606.25957v1

## Abstract

Locating survivors of building collapses within the first 72 hours is a critical challenge in disaster response, and existing sensing modalities provide only partial information about the structure beneath the rubble. This paper proposes drone-based quantum magnetometry as a complementary modality and develops a simulation pipeline spanning rubble physics, sensor-array deployment, and active spatial reconstruction. We use Unreal Engine to generate a steel-reinforced concrete parking-garage collapse and compute the induced magnetic field via a per-triangle dipole approximation, establishing that meaningful magnetic structure is recoverable in the sub-pT to sub-nT range from roughly 1 m above the roofline. Then, we feed sparse multi-sensor samples into a Gaussian Process Regression back-end driven by Bayesian active sampling and validate the pipeline across multiple independent collapse realizations; a three-sensor array optimizes the trade-off between gradient resolution and UAV payload constraints, and active sampling reaches peak structural correlation in roughly $100$ samples. Together, these results indicate that quantum-grade sensing could become a useful tool for drone-based structural analysis and potentially void detection in collapsed buildings.
