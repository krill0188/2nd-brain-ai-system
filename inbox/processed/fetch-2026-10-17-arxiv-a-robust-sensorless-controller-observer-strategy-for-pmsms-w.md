---
title: "A Robust Sensorless Controller-Observer Strategy for PMSMs with Unknown Resistance and Mechanical Model"
created: 2026-10-17
captured: 2026-10-17
type: paper
domain: hardware
source: http://arxiv.org/abs/2002.01823v1
authors: "Alessandro Bosso, Andrea Tilli, Christian Conficoni"
published: "2020-02-05"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/a-robust-sensorless-controller-observer-strategy-for-pmsms-w.html
attachment_type: html
attachment_sha256: 56ef0eb9ce27757d5de6111b6f684a5cefbc899ffc3148ccb7f8c0a7f0ff74d1
---

# A Robust Sensorless Controller-Observer Strategy for PMSMs with Unknown Resistance and Mechanical Model

**Authors**: Alessandro Bosso, Andrea Tilli, Christian Conficoni
**Published**: 2020-02-05
**arXiv**: http://arxiv.org/abs/2002.01823v1

## Abstract

In this work, we present a mixed sensorless strategy for Permanent Magnets Synchronous Machines, combining a torque/current controller and an observer for position, speed, flux and stator resistance. The proposed co-design is motivated by the need of an appropriate signal injection technique, in order to guarantee full state observability. Neither the typical constant or slowly-varying speed assumptions, nor a priori mechanical model information are used in the observer design. Instead, the rotor speed is modeled as an unknown input disturbance with constant (unknown) sign and uniformly non-zero magnitude. With the proposed architecture, it is shown that the torque tracking and signal injection tasks can be achieved and asymptotically decoupled. Because of these features, we refer to this strategy as a sensorless controller-observer with no mechanical model. Employing a gradient descent resistance/back-EMF estimation, combined with the unit circle formalism to describe the rotor position, we rigorously prove regional practical asymptotic stability of the overall structure, with a domain of attraction that can be made arbitrarily large, not including a lower dimensional manifold. The effectiveness of this design is further validated with numerical simulations, related to a challenging application of UAV propellers control.
