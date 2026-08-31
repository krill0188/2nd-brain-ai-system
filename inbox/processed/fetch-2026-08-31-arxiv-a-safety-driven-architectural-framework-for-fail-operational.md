---
title: "A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions"
created: 2026-08-31
captured: 2026-08-31
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2608.20906v1
authors: "Luiz Giacomossi, Zafer Yigit, Marwan Shakarna, Shoaib Saleemi, Ivan Tomasic, Baran \u00c7ur\u00fckl\u00fc, H\u00e5kan Forsberg"
published: "2026-08-21"
tags: [drone, ai-autonomy, paper, arxiv]
---

# A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions

**Authors**: Luiz Giacomossi, Zafer Yigit, Marwan Shakarna, Shoaib Saleemi, Ivan Tomasic, Baran Çurüklü, Håkan Forsberg
**Published**: 2026-08-21
**arXiv**: http://arxiv.org/abs/2608.20906v1

## Abstract

The certification of Unmanned Aerial Vehicle (UAV) swarms for safety-critical operations requires verifiable design assurance. Airworthiness standards demand deterministic reliability, whereas multi-agent coordination algorithms execute non-deterministic models. This paper proposes a mixed-criticality architectural framework that applies SAE ARP4754B methods to swarm reconfiguration. First, a hardware-isolated Safety Monitor functions as a Run-Time Assurance (RTA) gateway, decoupling the flight-critical core from the non-deterministic Swarm Manager. Second, the monitor enforces formal safety contracts based on agent Health Vectors derived systematically from a Functional Hazard Assessment (FHA). Third, the framework propagates these Health Vectors to the collective planner to trigger fail-operational task reallocation, enabling intelligent swarm behaviors without compromising flight-critical isolation. Markov reliability modeling demonstrates that the $10^{-7}$ failures per flight hour Hazardous target is theoretically achievable for our SAIL IV scenario, provided the Safety Monitor meets $C_{monitor}>0.9991$, consistent with DAL B CMD/MON implementations.
