---
title: "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: preprint
authors: "Giacomossi, Luiz; Yigit, Zafer; Shakarna, Marwan; Saleemi, Shoaib; Tomasic, Ivan; \u00c7ur\u00fckl\u00fc, Baran; Forsberg, H\u00e5kan"
year: "2026"
doi: "10.48550/arXiv.2608.20906"
url: "http://arxiv.org/abs/2608.20906v1"
zotero_key: RIVEWPF3
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/swarm/a-safety-driven-architectural-framework-for-fail-operational-drone-swarms-in-cri.pdf
attachment_sha256: e2dd434d36dc96eb2eab69461af30288df36bb271db61f3e59d508a0725d5612
sha256: 38bfa4d7ebf8423a
---

# A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions

**Authors**: Giacomossi, Luiz; Yigit, Zafer; Shakarna, Marwan; Saleemi, Shoaib; Tomasic, Ivan; Çurüklü, Baran; Forsberg, Håkan  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.20906  
**URL**: http://arxiv.org/abs/2608.20906v1

## Abstract

The certification of Unmanned Aerial Vehicle (UAV) swarms for safety-critical operations requires verifiable design assurance. Airworthiness standards demand deterministic reliability, whereas multi-agent coordination algorithms execute non-deterministic models. This paper proposes a mixed-criticality architectural framework that applies SAE ARP4754B methods to swarm reconfiguration. First, a hardware-isolated Safety Monitor functions as a Run-Time Assurance (RTA) gateway, decoupling the flight-critical core from the non-deterministic Swarm Manager. Second, the monitor enforces formal safety contracts based on agent Health Vectors derived systematically from a Functional Hazard Assessment (FHA). Third, the framework propagates these Health Vectors to the collective planner to trigger fail-operational task reallocation, enabling intelligent swarm behaviors without compromising flight-critical isolation. Markov reliability modeling demonstrates that the $10^{-7}$ failures per flight hour Hazardous target is theoretically achievable for our SAIL IV scenario, provided the Safety Monitor meets $C_{monitor}>0.9991$, consistent with DAL B CMD/MON implementations.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
