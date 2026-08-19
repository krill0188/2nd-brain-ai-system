---
title: "When Connectivity Is Not Enough: Cross-Layer Attacks on UAV C2 over 5G"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: gcs-software
source: http://arxiv.org/abs/2603.04662v4
authors: "Wagner Comin Sonaglio, \u00c1gney Lopes Roth Ferraz, Andr\u00e9 Elias Melo, Murray Evangelista de Souza, Guevara Noubir, Louren\u00e7o Alves Pereira J\u00fanior"
published: "2026-03-04"
tags: [drone, gcs-software, paper, arxiv]
---

# When Connectivity Is Not Enough: Cross-Layer Attacks on UAV C2 over 5G

**Authors**: Wagner Comin Sonaglio, Ágney Lopes Roth Ferraz, André Elias Melo, Murray Evangelista de Souza, Guevara Noubir, Lourenço Alves Pereira Júnior
**Published**: 2026-03-04
**arXiv**: http://arxiv.org/abs/2603.04662v4

## Abstract

Beyond Visual Line of Sight (BVLOS) unmanned aerial vehicle (UAV) operations increasingly use 5G standalone (SA) networks for command and control (C2) between the UAV and the ground control station (GCS). The 3rd Generation Partnership Project (3GPP) has specified mechanisms for authentication and authorization of unmanned aircraft systems (UAS) in this architectural setting. As a result, operators may treat registration state, Protocol Data Unit (PDU) session status, and IP reachability as evidence that the C2 path is available. In practice, however, these connectivity indicators alone do not guarantee that closed-loop control remains operationally safe. Attacks can degrade UAS C2 when timeliness degrades under shared User Plane contention, mobility continuity fails during Control Plane instability, or command integrity is violated at a trusted next-generation Node B (gNodeB). Such failures undermine connectivity as the central security indicator for UAV operations. In this paper, we demonstrate these issues using three distinct threat models on a reproducible Open5GS and UERANSIM testbed that carries Micro Air Vehicle Link (MAVLink) over the 5G User Plane, and we use a commercial Nokia core to ground deployment assumptions. We address timeliness, availability, and integrity through experiments in which attack success is defined as forcing an unsafe closed-loop state without a clean disconnect. We observe stale telemetry and heavy-tailed delay under co-tenant User Plane contention, failsafe after handover under Control Plane instability, and navigation hijacking after command rewriting at a compromised gNodeB. We further discuss why each threat model arises and evaluate mitigations for these cross-layer failures. Across the study, we disclosed five robustness issues: three CVEs have already been assigned, and two additional CVE requests are pending.
