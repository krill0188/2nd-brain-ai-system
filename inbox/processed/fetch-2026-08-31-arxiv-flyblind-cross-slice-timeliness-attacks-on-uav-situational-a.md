---
title: "FlyBlind: Cross-Slice Timeliness Attacks on UAV Situational Awareness over 5G"
created: 2026-08-31
captured: 2026-08-31
type: paper
domain: gcs-software
source: http://arxiv.org/abs/2608.27604v1
authors: "Wagner Comin Sonaglio, \u00c1gney Lopes Roth Ferraz, Andr\u00e9 Elias Melo, Guevara Noubir, Louren\u00e7o Alves Pereira J\u00fanior"
published: "2026-08-27"
tags: [drone, gcs-software, paper, arxiv]
---

# FlyBlind: Cross-Slice Timeliness Attacks on UAV Situational Awareness over 5G

**Authors**: Wagner Comin Sonaglio, Ágney Lopes Roth Ferraz, André Elias Melo, Guevara Noubir, Lourenço Alves Pereira Júnior
**Published**: 2026-08-27
**arXiv**: http://arxiv.org/abs/2608.27604v1

## Abstract

Beyond Visual Line of Sight (BVLOS) Uncrewed Aerial Systems (UAS) operating over 5G Standalone (SA) networks use a shared User Plane for both command-and-control (C2) data and video feedback. Operators assess link quality through latency and availability, relying on soft isolation between network slices. However, the risk that an authorized co-tenant could make the Ground Control Station (GCS) state outdated without disrupting the connection remains underexplored. This work introduces FlyBlind, a timeliness attack in which an authorized co-tenant on a neighboring slice maintains legitimate uplink demand, causing state aging at the GCS without a rogue gNB or direct interference with C2 traffic. Our key insight is that, under soft isolation, sharing idle resources turns authorized competition for grants into state aging that conventional link monitors fail to detect. We formalize this effect, termed Silent State Staleness, as a falsifiable false-healthy predicate. On a dedicated testbed, telemetry age at the GCS saturates at approximately 12 seconds, with discrepancies of tens of meters between the GCS position estimate and ground truth, while the one-way delay (OWD) p99 remains in the tens of milliseconds, availability exceeds 99.9%, and the vehicle keeps operating in GUIDED mode without triggering failsafe mechanisms. These findings indicate that, in deployments with asymmetric uplink enforcement, verifying state freshness at the destination is essential rather than relying solely on link health.
