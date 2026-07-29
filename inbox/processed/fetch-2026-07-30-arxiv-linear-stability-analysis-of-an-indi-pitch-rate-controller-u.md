---
title: "Linear Stability Analysis of an INDI Pitch-Rate Controller under Model Mismatch for a Tilt-Rotor VTOL UAV"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2607.16471v1
authors: "Lorenzo Schenk, Guillaume Ducard, Christopher Onder"
published: "2026-07-17"
tags: [drone, flight-control, paper, arxiv]
---

# Linear Stability Analysis of an INDI Pitch-Rate Controller under Model Mismatch for a Tilt-Rotor VTOL UAV

**Authors**: Lorenzo Schenk, Guillaume Ducard, Christopher Onder
**Published**: 2026-07-17
**arXiv**: http://arxiv.org/abs/2607.16471v1

## Abstract

Incremental Nonlinear Dynamic Inversion (INDI) is attractive for unmanned aerial vehicle (UAV) flight control because it reduces dependence on a full aerodynamic model while retaining strong disturbance-rejection capability. For a tilt-rotor vertical takeoff and landing (VTOL) architecture, however, the admissible model-mismatch range of the fast inner loop is still not characterized analytically in a parameter-explicit way. This paper isolates the pitch-rate/elevon subchannel of an existing cascaded INDI controller and studies its linear stability under model mismatch. A closed-form fifth-order transfer function is derived for the full controller-estimator-actuator-plant interconnection, and stability is characterized through the Routh-Hurwitz criterion over a parameterized linear model. Two representative three-parameter sweeps produce interpretable stability regions. Based on these feasibility maps, two uncertainty-aware tuning procedures are proposed: a robustness-oriented design that maximizes a weighted worst-case combination of gain margin and phase margin, and a performance-oriented design that maximizes worst-case closed-loop bandwidth subject to margin constraints. The results show that actuator lag and inertia mismatch are comparatively benign at nominal gain, whereas control-effectiveness mismatch, particularly a sign error in the allocation, is the most dangerous destabilizing factor, leading to concrete tuning recommendations for conservative and aggressive operating conditions.
