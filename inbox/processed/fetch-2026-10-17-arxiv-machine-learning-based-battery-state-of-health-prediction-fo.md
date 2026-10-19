---
title: "Machine Learning-Based Battery State-of-health Prediction for Unmanned Aerial Vehicles Predictive Maintenance"
created: 2026-10-17
captured: 2026-10-17
type: paper
domain: hardware
source: http://arxiv.org/abs/2607.06791v1
authors: "Jiarui Xie, Lingchen Kong, Mohamed Rami Latreche, Sean Smith, Elaine Mosconi, Yaoyao Fiona Zhao"
published: "2026-07-07"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/machine-learning-based-battery-state-of-health-prediction-fo.pdf
attachment_type: pdf
attachment_sha256: 5b00d55dcbb4e08a8fe0920cb58b2e6ee2d97c3b52d6743b1e7524c7fc105b79
---

# Machine Learning-Based Battery State-of-health Prediction for Unmanned Aerial Vehicles Predictive Maintenance

**Authors**: Jiarui Xie, Lingchen Kong, Mohamed Rami Latreche, Sean Smith, Elaine Mosconi, Yaoyao Fiona Zhao
**Published**: 2026-07-07
**arXiv**: http://arxiv.org/abs/2607.06791v1

## Abstract

Battery state-of-health (SoH) prediction aims to estimate the remaining capacity by modeling battery degradation through its life cycle. Machine learning (ML)-based SoH models can accurately predict the battery remaining capacity based on voltage, current, and temperature. Battery SoH prediction for unmanned aerial vehicles (UAVs) is a crucial yet overlooked domain with data scarcity and high variability. Accurate battery SoH information contributes to efficient predictive maintenance, enhancing UAV profitability and flight safety. However, UAVs are compatible with a variety of batteries and the available data for each type of battery are scarce. Furthermore, the available input features from UAV batteries are limited to the built-in sensors because of the lightweight requirements. This research aims to develop an ML pipeline for UAV battery SoH prediction while mitigating data scarcity using knowledge transfer. 342 and 289 flight experiments have been conducted to collect operational data from lithium polymer batteries of 2200 mAh and 1100 mAh, respectively. Voltage, current, and throttle are selected as the input features of the ML model according to the existing literature and sensor availability. The remaining capacity is measured at every 10th experiment to label the dataset. To address data scarcity, the time-series data acquired from the experiments are transformed into images to utilize the image feature extraction capability of a pretrained ResNet-50. Finally, accurate SoH prediction models were obtained using transfer learning between two battery types.
