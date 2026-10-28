---
title: "How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study"
created: 2026-10-28
updated: 2026-10-28
type: paper
item_type: preprint
authors: "Dao, Xuan-Quy; Nguyen, Le-Minh; Le, Ngoc-Bich"
year: "2026"
doi: "10.48550/arXiv.2610.35165"
url: "http://arxiv.org/abs/2610.35165v1"
zotero_key: F52NA8A9
tags: ["auto:2nd-brain"]
sha256: 0c1295344aeec945
---

# How Tuning, Reference Preview, Actuator Modeling, and Fallback Policies Change Quadrotor Controller Comparisons: A Reproducible Simulation Study

**Authors**: Dao, Xuan-Quy; Nguyen, Le-Minh; Le, Ngoc-Bich  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2610.35165  
**URL**: http://arxiv.org/abs/2610.35165v1

## Abstract

Quadrotor controller comparisons commonly report a single tracking error, although the resulting ranking also depends on tuning effort, reference information, actuator prediction, optimizer fallback, and command timing. We quantify these effects for cascade PID, hover LQR, boundary-layer sliding-mode control (BL-SMC), linear MPC with LQR fallback (LMPC-F), a preview-enabled LMPC-F, and a geometric $SO(3)$ controller on a common nonlinear plant with rotor gyroscopic coupling, motor lag, and saturation. A primary study (556 episodes at 50~Hz) combines matched twelve-candidate tuning, 400 paired evaluation episodes, and a 48-cell MPC factorial; a confirmation study (1462 episodes) repeats the evaluation on 50 fresh realizations with tuning budgets of 12, 24, and 48 candidates. A matched twelve-candidate tuning protocol changed the mean-RMSE ordering obtained with the fixed baseline settings, moving BL-SMC from last to first; the new ordering recurred on the fresh realizations, and a 48-candidate budget left it unchanged. Reference preview substantially reduced MPC tracking error and, on the figure-eight task, removed fallback activity. On an abrupt step, the outcome depended on the interplay between fallback policy, predictor, and actuator authority. Command timing also changed the outcome: replaying measured command-call delays terminated three of four nominal MPC configurations on a desktop computer and all four on a Raspberry Pi~5, whereas capping the solver at 100 iterations removed every deadline miss in the tested nominal timing profiles. Controller rankings therefore depend not only on tracking accuracy but also on the tuning protocol, reference information, fallback behavior, and implementation timing. We propose a reporting checklist covering tracking accuracy, tuning effort, completion and failure rates, fallback activity, applied-input variation, and command timing.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
