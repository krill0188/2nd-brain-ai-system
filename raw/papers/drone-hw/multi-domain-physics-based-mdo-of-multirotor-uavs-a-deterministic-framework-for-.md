---
title: "Multi-Domain Physics-Based MDO of Multirotor UAVs: A Deterministic Framework for Discrete COTS Sizing"
created: 2026-08-19
updated: 2026-08-19
type: paper
item_type: preprint
authors: "Burela, Akshay Gupta; Sujit, P. B."
year: "2026"
doi: "10.48550/arXiv.2607.22768"
url: "http://arxiv.org/abs/2607.22768v1"
zotero_key: C54AI7G7
tags: ["auto:2nd-brain", "drone-hw"]
sha256: af483e8f7ea5186d
---

# Multi-Domain Physics-Based MDO of Multirotor UAVs: A Deterministic Framework for Discrete COTS Sizing

**Authors**: Burela, Akshay Gupta; Sujit, P. B.  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2607.22768  
**URL**: http://arxiv.org/abs/2607.22768v1

## Abstract

Multirotor Unmanned Aerial Vehicle (UAV) design is governed by a tightly coupled system of non-linear equations spanning structural mechanics, electrochemistry, aerodynamics, and kinematics. Solved sequentially, a miscalibrated sub-model coefficient triggers a mass-compounding cascade failure--the Mass Snowball effect. This paper presents AeroEval, a physics-based, Multidisciplinary Design Optimization (MDO) engine that simultaneously resolves all subsystem couplings and maps continuous sizing optima to physically purchasable, commercial off-the-shelf (COTS) components. The MDO engine is validated under a strict calibrate/test protocol that eliminates circularity: three structural/packaging coefficients are fitted on a held-out cohort of 20 do-it-yourself (DIY) and legacy platforms, then frozen and evaluated blind on 19 modern commercial drone platforms spanning 377 g to 76 kg. On the commercial test cohort the engine predicts Maximum Takeoff Weight (MTOW) within 7.2% Mean Absolute Percentage Error (MAPE), with a mean complexity factor $k \approx 1.05 \pm 0.08$ and $\text{RMSE}_{\text{MTOW}} = 1.59$ kg; the DIY calibration cohort, characterized by high build variability, yields 26.1% MAPE. Battery mass is predicted within 7.9% on single-pack platforms, with a disclosed systematic underprediction on redundant multi-battery enterprise platforms. A 14-parameter sensitivity suite of >300 simulations quantifies partial derivatives of takeoff mass and flight time; forward velocity diverges beyond 25.5 m/s due to cubic parasite power growth. The path-dependent mass-shedding model for agricultural and delivery roles reduces structural frame mass by up to 40.6% and energy capacity by 33.7% relative to static baselines. Typical solver convergence requires 25-50 iterations, completing in under 50 ms on a standard desktop CPU.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
