---
title: "Chained Attacks on Drone-Based Federated Learning: From Network Disruption to Device Impersonation"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2607.20280v1
authors: "Suleiman Muhammad Sabo, Hamed Alkharsh, Peilin Li, Chuadhry Mujeeb Ahmed, Aydin Abadi, Shishir Nagaraja, Rajiv Ranjan"
published: "2026-07-22"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Chained Attacks on Drone-Based Federated Learning: From Network Disruption to Device Impersonation

**Authors**: Suleiman Muhammad Sabo, Hamed Alkharsh, Peilin Li, Chuadhry Mujeeb Ahmed, Aydin Abadi, Shishir Nagaraja, Rajiv Ranjan
**Published**: 2026-07-22
**arXiv**: http://arxiv.org/abs/2607.20280v1

## Abstract

Edge Intelligence (EI) has emerged as a transformative model for mission-critical unmanned platforms, such as drone swarms, by enabling collaborative model training at the network periphery. However, the security of FL deployments depends on both network availability and robust client authentication mechanisms. This paper investigates a chained attack against drone-based FL systems that combines network-layer denial-of-service with credential-based impersonation. We demonstrate that an adversary can: (1) force legitimate drones offline using 802.11 deauthentication attacks, and (2) subsequently impersonate the disconnected drone using extracted credentials. Through a systematic literature review and empirical validation using the Flower framework on two distinct testbeds of Raspberry Pi and Jetsons, we quantify the impact of availability disruptions under Independent and Identically Distributed (IID) and Non-Independently and Identically Distributed (Non-IID) data distributions, and confirm that single-factor authentication permits post-disconnect impersonation. Our findings reveal that even short-term wireless interruptions cascade into substantial training instability, particularly under non-IID conditions, while the authentication gap enables adversaries to seamlessly replace disconnected nodes. We discuss the compounded implications for mission-critical drone deployments and outline directions for future defenses addressing both availability and authentication vulnerabilities.
