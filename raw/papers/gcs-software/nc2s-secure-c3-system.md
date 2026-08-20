---
title: "Secure Command, Control and Communications Systems (C3) for Army UxVs"
created: 2026-08-20
captured: 2026-08-20
type: paper
domain: gcs-software
source: http://arxiv.org/abs/2511.21936v1
authors: "T. Rebolo, A. Grilo, C. Ribeiro"
published: "2025-11-26"
tags: [drone, gcs-software, paper, arxiv]
---

# Secure Command, Control and Communications Systems (C3) for Army UxVs

**Authors**: T. Rebolo, A. Grilo, C. Ribeiro
**Published**: 2025-11-26
**arXiv**: http://arxiv.org/abs/2511.21936v1

## Abstract

Unmanned Vehicles (UxVs) are increasingly used in modern military operations for reconnaissance, surveillance, and strike missions, enhancing situational awareness while reducing risk to personnel. Their affordability and rapid deployment have encouraged the adoption of commercial solutions. However, many rely on insecure protocols such as MAVLink, which lack authentication and encryption mechanisms. This paper designed, implemented, and evaluated a new secure command-and-control architecture that ensures confidentiality, integrity, and authentication (CIA) while supporting real-time control delegation between Ground Control Stations (GCSs). The proposed solution, named New Command and Control System (NC2S), enforces a zero-trust model integrating hierarchical credential-based privileges to regulate access and control among Tactical Commanders (TC), GCSs, and UxVs. It employs mutual Transport Layer Security (mTLS) with Elliptic Curve Digital Signature Algorithm (ECDSA) certificates and Elliptic Curve Diffie-Hellman (ECDH) key exchange, while message integrity is ensured through Hash-based Message Authentication Codes (HMAC). Multiple lightweight protocols were developed for credential management, key renewal, and control handover. The NC2S prototype was experimentally validated over Wi-Fi and Rohde&Schwarz HR-5000H tactical radios. Results showed that HR-5000H links introduce latencies roughly two orders of magnitude higher than broadband technologies (e.g., Wi-Fi or 5G&Beyond technologies) but are still able to maintain stable communication with minimal message loss, making them suitable for the NC2S links among TC terminals and GCSs.
