---
title: "Secure Command, Control and Communications Systems (C3) for Army UxVs"
created: 2026-08-20
updated: 2026-08-20
type: paper
item_type: preprint
authors: "Rebolo, T.; Grilo, A.; Ribeiro, C."
year: "2025"
doi: "10.48550/arXiv.2511.21936"
url: "http://arxiv.org/abs/2511.21936v1"
zotero_key: ZB7Q77AT
tags: ["auto:2nd-brain"]
sha256: 5d2e7d94e80544bd
---

# Secure Command, Control and Communications Systems (C3) for Army UxVs

**Authors**: Rebolo, T.; Grilo, A.; Ribeiro, C.  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2511.21936  
**URL**: http://arxiv.org/abs/2511.21936v1

## Abstract

Unmanned Vehicles (UxVs) are increasingly used in modern military operations for reconnaissance, surveillance, and strike missions, enhancing situational awareness while reducing risk to personnel. Their affordability and rapid deployment have encouraged the adoption of commercial solutions. However, many rely on insecure protocols such as MAVLink, which lack authentication and encryption mechanisms. This paper designed, implemented, and evaluated a new secure command-and-control architecture that ensures confidentiality, integrity, and authentication (CIA) while supporting real-time control delegation between Ground Control Stations (GCSs). The proposed solution, named New Command and Control System (NC2S), enforces a zero-trust model integrating hierarchical credential-based privileges to regulate access and control among Tactical Commanders (TC), GCSs, and UxVs. It employs mutual Transport Layer Security (mTLS) with Elliptic Curve Digital Signature Algorithm (ECDSA) certificates and Elliptic Curve Diffie-Hellman (ECDH) key exchange, while message integrity is ensured through Hash-based Message Authentication Codes (HMAC). Multiple lightweight protocols were developed for credential management, key renewal, and control handover. The NC2S prototype was experimentally validated over Wi-Fi and Rohde&Schwarz HR-5000H tactical radios. Results showed that HR-5000H links introduce latencies roughly two orders of magnitude higher than broadband technologies (e.g., Wi-Fi or 5G&Beyond technologies) but are still able to maintain stable communication with minimal message loss, making them suitable for the NC2S links among TC terminals and GCSs.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
