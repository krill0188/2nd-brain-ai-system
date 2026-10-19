---
title: "Airspeed estimation for UAVs using only propeller feedback"
created: 2026-10-19
captured: 2026-10-19
type: paper
domain: hardware
source: http://arxiv.org/abs/2507.03456v1
authors: "Evangelos Ntouros, Pavel Kelley, Ewoud Smeur"
published: "2025-07-04"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/airspeed-estimation-for-uavs-using-only-propeller-feedback.html
attachment_type: html
attachment_sha256: 60e93837f5cca09648858bc830b466226200e088c9ad48d087f085142a4f2880
---

# Airspeed estimation for UAVs using only propeller feedback

**Authors**: Evangelos Ntouros, Pavel Kelley, Ewoud Smeur
**Published**: 2025-07-04
**arXiv**: http://arxiv.org/abs/2507.03456v1

## Abstract

This work introduces a novel analytical model for estimating the airspeed of fixed-wing Unmanned Aerial Vehicles (UAVs) using solely propeller power and rotational speed measurements. The model can be used to replace Pitot-tube-based airspeed sensors, or contribute to redundancy in airspeed estimation. It does not require knowledge of the vehicle's dynamic model and is computationally lightweight. It leverages power and rotational speed feedback, which is readily available from modern Electronic Speed Controllers (ESCs), thereby enabling seamless integration with existing systems and off-the-shelf components. A systematic approach is followed to derive the model structure based on least squares optimization and regularization techniques on Blade Element Momentum (BEM) simulation, wind tunnel, and flight test datasets. The final model generalizes well achieving a normalized Root Mean Square Error (nRMSE) of 5% on unseen flight data. The model parameters can be identified either offline, using flight logs with airspeed measurements, or in-flight, using a lightweight identification method based only on Global Positioning System (GPS) velocity data. The resulting system provides a robust and computationally efficient solution for real-time airspeed estimation across diverse fixed-wing UAV platforms.
