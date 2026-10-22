---
title: "Airspeed estimation for UAVs using only propeller feedback"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: preprint
authors: "Ntouros, Evangelos; Kelley, Pavel; Smeur, Ewoud"
year: "2025"
doi: "10.48550/arXiv.2507.03456"
url: "http://arxiv.org/abs/2507.03456v1"
zotero_key: C6R6VJCD
tags: ["auto:2nd-brain"]
sha256: 2d1987c59bac2b29
---

# Airspeed estimation for UAVs using only propeller feedback

**Authors**: Ntouros, Evangelos; Kelley, Pavel; Smeur, Ewoud  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2507.03456  
**URL**: http://arxiv.org/abs/2507.03456v1

## Abstract

This work introduces a novel analytical model for estimating the airspeed of fixed-wing Unmanned Aerial Vehicles (UAVs) using solely propeller power and rotational speed measurements. The model can be used to replace Pitot-tube-based airspeed sensors, or contribute to redundancy in airspeed estimation. It does not require knowledge of the vehicle's dynamic model and is computationally lightweight. It leverages power and rotational speed feedback, which is readily available from modern Electronic Speed Controllers (ESCs), thereby enabling seamless integration with existing systems and off-the-shelf components. A systematic approach is followed to derive the model structure based on least squares optimization and regularization techniques on Blade Element Momentum (BEM) simulation, wind tunnel, and flight test datasets. The final model generalizes well achieving a normalized Root Mean Square Error (nRMSE) of 5% on unseen flight data. The model parameters can be identified either offline, using flight logs with airspeed measurements, or in-flight, using a lightweight identification method based only on Global Positioning System (GPS) velocity data. The resulting system provides a robust and computationally efficient solution for real-time airspeed estimation across diverse fixed-wing UAV platforms.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
