---
title: "Selective Sliding Mode Control Enhances Robustness of Aerial Robots Under Disturbances"
created: 2026-11-07
updated: 2026-11-07
type: paper
item_type: preprint
authors: "Kiran, Anoop; Silva, Thales C.; Ayanian, Nora"
year: "2026"
doi: "10.48550/arXiv.2610.38930"
url: "http://arxiv.org/abs/2610.38930v1"
zotero_key: TV2TX4UA
tags: ["auto:2nd-brain"]
sha256: 2444863cdfe2dc02
---

# Selective Sliding Mode Control Enhances Robustness of Aerial Robots Under Disturbances

**Authors**: Kiran, Anoop; Silva, Thales C.; Ayanian, Nora  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2610.38930  
**URL**: http://arxiv.org/abs/2610.38930v1

## Abstract

Quadrotor control under disturbances such as wind gusts and payload variations remains challenging. First-order sliding mode control (SMC) and matched/unmatched uncertainty distinction are classical approaches; however, neither tells a practitioner which loops in a cascaded controller should be made robust to sustain disturbances, how to tune those loops, nor what the additional costs are on an embedded processor. Applying robust control uniformly across all axes addresses disturbances indiscriminately, adding tuning effort on axes where no disturbance acts. On inherently underactuated vehicles, disturbances along some axes cannot be opposed directly at all. We propose a principled methodology for deciding where robust control belongs in a cascaded architecture, with all control running onboard the vehicle. We recover the acting disturbance from PID hover flights under disturbance by inverting the equations of motion, use the recovered signal to identify and quantify the excited axes, and deploy robust control where it counts. Experiments on a Crazyflie 2.1 quadrotor under slung-payload and oblique-wind disturbances show tracking improvements concentrated on the axes the rule selects, and gain sweeps confirm that the switching gain reduces error on matched axes but has no effect on an excited unmatched axis, as the analysis predicts.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
