---
title: "Automated System-level Testing of Unmanned Aerial Systems"
created: 2026-08-24
captured: 2026-08-24
type: paper
domain: gcs-software
source: http://arxiv.org/abs/2403.15857v2
authors: "Hassan Sartaj, Asmar Muqeet, Muhammad Zohaib Iqbal, Muhammad Uzair Khan"
published: "2024-03-23"
tags: [drone, gcs-software, paper, arxiv]
---

# Automated System-level Testing of Unmanned Aerial Systems

**Authors**: Hassan Sartaj, Asmar Muqeet, Muhammad Zohaib Iqbal, Muhammad Uzair Khan
**Published**: 2024-03-23
**arXiv**: http://arxiv.org/abs/2403.15857v2

## Abstract

Unmanned aerial systems (UAS) rely on various avionics systems that are safety-critical and mission-critical. A major requirement of international safety standards is to perform rigorous system-level testing of avionics software systems. The current industrial practice is to manually create test scenarios, manually/automatically execute these scenarios using simulators, and manually evaluate outcomes. The test scenarios typically consist of setting certain flight or environment conditions and testing the system under test in these settings. The state-of-the-art approaches for this purpose also require manual test scenario development and evaluation. In this paper, we propose a novel approach to automate the system-level testing of the UAS. The proposed approach (AITester) utilizes model-based testing and artificial intelligence (AI) techniques to automatically generate, execute, and evaluate various test scenarios. The test scenarios are generated on the fly, i.e., during test execution based on the environmental context at runtime. The approach is supported by a toolset. We empirically evaluate the proposed approach on two core components of UAS, an autopilot system of an unmanned aerial vehicle (UAV) and cockpit display systems (CDS) of the ground control station (GCS). The results show that the AITester effectively generates test scenarios causing deviations from the expected behavior of the UAV autopilot and reveals potential flaws in the GCS-CDS.
