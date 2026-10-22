---
title: "Equivalent-Agent Guidance for Cooperative UAV Payload Transportation"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: preprint
authors: "Kumar, Saurabh; Kumar, Shashi Ranjan; Sinha, Abhinav"
year: "2026"
doi: "10.48550/arXiv.2609.19312"
url: "http://arxiv.org/abs/2609.19312v1"
zotero_key: ZHT6ARHU
tags: ["auto:2nd-brain"]
sha256: 0a8371ebc34cb43b
---

# Equivalent-Agent Guidance for Cooperative UAV Payload Transportation

**Authors**: Kumar, Saurabh; Kumar, Shashi Ranjan; Sinha, Abhinav  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2609.19312  
**URL**: http://arxiv.org/abs/2609.19312v1

## Abstract

This paper develops a guidance framework for cooperative transportation of a rigid payload by two uncrewed aerial vehicles (UAVs) to stationary and maneuvering landing platforms. A virtual equivalent-agent representation is first introduced to describe the translational motion of the rigidly coupled UAV-payload system, allowing the transportation problem to be formulated in terms of relative range and line-of-sight dynamics with respect to the landing platform. A geometric analysis establishes the terminal feasibility conditions for payload delivery. In particular, an arbitrary prescribed approach angle can be achieved for a stationary platform, whereas successful delivery to a maneuvering platform with zero relative velocity requires terminal velocity and heading angle synchronization and consequently a zero landing angle. Leveraging this framework, a robust fixed-time sliding mode guidance strategy is developed to regulate both relative range and line-of-sight dynamics. A separate link-orientation controller and control allocation scheme is presented to map virtual equivalent agent commands to the individual UAV's control inputs. The proposed strategy guarantees convergence to the desired landing configuration within a uniformly bounded time, independent of initial engagement geometries, while explicitly accommodating uncertainties arising from target maneuvers. Numerical simulations demonstrate accurate delivery under different terminal approach angles and platform maneuvers, while processor-in-the-loop implementation on a Raspberry Pi demonstrates that the guidance algorithm satisfies the real-time computational requirements. Nonetheless, a comparative analysis shows that the proposed framework achieves better tracking accuracy and faster sliding surface convergence while requiring significantly less control energy from each UAV.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
