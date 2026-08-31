---
title: "FlyBlind: Cross-Slice Timeliness Attacks on UAV Situational Awareness over 5G"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: preprint
authors: "Sonaglio, Wagner Comin; Ferraz, \u00c1gney Lopes Roth; Melo, Andr\u00e9 Elias; Noubir, Guevara; J\u00fanior, Louren\u00e7o Alves Pereira"
year: "2026"
doi: "10.48550/arXiv.2608.27604"
url: "http://arxiv.org/abs/2608.27604v1"
zotero_key: QEFSZGRN
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/datalink/flyblind-cross-slice-timeliness-attacks-on-uav-situational-awareness-over-5g.pdf
attachment_sha256: 0666c9758054f6ff27467d3ecf97653844dcbccb86ed1cf4b55e02e544d9c624
sha256: 699bc9b43dda0f20
---

# FlyBlind: Cross-Slice Timeliness Attacks on UAV Situational Awareness over 5G

**Authors**: Sonaglio, Wagner Comin; Ferraz, Ágney Lopes Roth; Melo, André Elias; Noubir, Guevara; Júnior, Lourenço Alves Pereira  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.27604  
**URL**: http://arxiv.org/abs/2608.27604v1

## Abstract

Beyond Visual Line of Sight (BVLOS) Uncrewed Aerial Systems (UAS) operating over 5G Standalone (SA) networks use a shared User Plane for both command-and-control (C2) data and video feedback. Operators assess link quality through latency and availability, relying on soft isolation between network slices. However, the risk that an authorized co-tenant could make the Ground Control Station (GCS) state outdated without disrupting the connection remains underexplored. This work introduces FlyBlind, a timeliness attack in which an authorized co-tenant on a neighboring slice maintains legitimate uplink demand, causing state aging at the GCS without a rogue gNB or direct interference with C2 traffic. Our key insight is that, under soft isolation, sharing idle resources turns authorized competition for grants into state aging that conventional link monitors fail to detect. We formalize this effect, termed Silent State Staleness, as a falsifiable false-healthy predicate. On a dedicated testbed, telemetry age at the GCS saturates at approximately 12 seconds, with discrepancies of tens of meters between the GCS position estimate and ground truth, while the one-way delay (OWD) p99 remains in the tens of milliseconds, availability exceeds 99.9%, and the vehicle keeps operating in GUIDED mode without triggering failsafe mechanisms. These findings indicate that, in deployments with asymmetric uplink enforcement, verifying state freshness at the destination is essential rather than relying solely on link health.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
