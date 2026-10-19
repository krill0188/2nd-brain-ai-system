---
title: "Equivalent-Agent Guidance for Cooperative UAV Payload Transportation"
created: 2026-10-17
captured: 2026-10-17
type: paper
domain: hardware
source: http://arxiv.org/abs/2609.19312v1
authors: "Saurabh Kumar, Shashi Ranjan Kumar, Abhinav Sinha"
published: "2026-09-16"
tags: [drone, hardware, paper, arxiv]
attachment_path: raw/papers/files/hardware/equivalent-agent-guidance-for-cooperative-uav-payload-transp.html
attachment_type: html
attachment_sha256: 746eb160333b9d498bfadde305d29a51659ead5d3bf4492dad124b3d6925b80b
---

# Equivalent-Agent Guidance for Cooperative UAV Payload Transportation

**Authors**: Saurabh Kumar, Shashi Ranjan Kumar, Abhinav Sinha
**Published**: 2026-09-16
**arXiv**: http://arxiv.org/abs/2609.19312v1

## Abstract

This paper develops a guidance framework for cooperative transportation of a rigid payload by two uncrewed aerial vehicles (UAVs) to stationary and maneuvering landing platforms. A virtual equivalent-agent representation is first introduced to describe the translational motion of the rigidly coupled UAV-payload system, allowing the transportation problem to be formulated in terms of relative range and line-of-sight dynamics with respect to the landing platform. A geometric analysis establishes the terminal feasibility conditions for payload delivery. In particular, an arbitrary prescribed approach angle can be achieved for a stationary platform, whereas successful delivery to a maneuvering platform with zero relative velocity requires terminal velocity and heading angle synchronization and consequently a zero landing angle. Leveraging this framework, a robust fixed-time sliding mode guidance strategy is developed to regulate both relative range and line-of-sight dynamics. A separate link-orientation controller and control allocation scheme is presented to map virtual equivalent agent commands to the individual UAV's control inputs. The proposed strategy guarantees convergence to the desired landing configuration within a uniformly bounded time, independent of initial engagement geometries, while explicitly accommodating uncertainties arising from target maneuvers. Numerical simulations demonstrate accurate delivery under different terminal approach angles and platform maneuvers, while processor-in-the-loop implementation on a Raspberry Pi demonstrates that the guidance algorithm satisfies the real-time computational requirements. Nonetheless, a comparative analysis shows that the proposed framework achieves better tracking accuracy and faster sliding surface convergence while requiring significantly less control energy from each UAV.
