---
title: "Scheduling Analysis of UAV Flight Control Workloads on PREEMPT_RT Linux Using a Raspberry Pi 5"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: flight-control
source: http://arxiv.org/abs/2604.19275v2
authors: "Luiz Giacomossi, H\u00e5kan Forsberg, Ivan Tomasic, Baran \u00c7\u00fcr\u00fckl\u00fc, Tommaso Cucinotta"
published: "2026-04-21"
tags: [drone, flight-control, paper, arxiv]
---

# Scheduling Analysis of UAV Flight Control Workloads on PREEMPT_RT Linux Using a Raspberry Pi 5

**Authors**: Luiz Giacomossi, Håkan Forsberg, Ivan Tomasic, Baran Çürüklü, Tommaso Cucinotta
**Published**: 2026-04-21
**arXiv**: http://arxiv.org/abs/2604.19275v2

## Abstract

Modern UAV architectures increasingly aim to unify high-level autonomy and low-level flight control on a single General-Purpose Operating System (GPOS). However, complex multi-core System-on-Chips (SoCs) introduce significant timing indeterminism due to shared resource contention. This paper performs an architectural analysis of the PREEMPT RT Linux kernel on a Raspberry Pi 5, specifically isolating the impact of kernel activation paths (deferred execution SoftIRQs versus real-time direct activation) on a 250 Hz control loop. Results show that under heavy stress, the standard kernel is unsuitable, exhibiting worst-case latencies exceeding 9 ms. In contrast, PREEMPT RT reduced the worst-case latency by nearly 88 percent to under 225 microseconds, enforcing a direct wake-up path that mitigates OS noise. These findings demonstrate that while PREEMPT RT resolves scheduling variance, the residual jitter on modern SoCs is primarily driven by hardware memory contention.
