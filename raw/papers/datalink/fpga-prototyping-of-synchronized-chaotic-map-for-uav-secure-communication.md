---
title: "FPGA prototyping of synchronized chaotic map for UAV secure communication"
created: 2026-08-20
updated: 2026-08-20
type: paper
item_type: preprint
authors: "Nwachioma, Christian; Ezuma, Martins; Medaiyese, Olusiji . O."
year: "2020"
doi: "10.48550/arXiv.2101.03880"
url: "http://arxiv.org/abs/2101.03880v1"
zotero_key: AF8XIWAQ
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/datalink/fpga-prototyping-of-synchronized-chaotic-map-for-uav-secure-communication.pdf
attachment_sha256: a80b3dd16f4df07a999c03fa076cd3e1b25a810dd7356ea91365ac2f8ab8a39f
sha256: 37c6efe11a0c2e76
---

# FPGA prototyping of synchronized chaotic map for UAV secure communication

**Authors**: Nwachioma, Christian; Ezuma, Martins; Medaiyese, Olusiji . O.  
**Year**: 2020  
**DOI**: 10.48550/arXiv.2101.03880  
**URL**: http://arxiv.org/abs/2101.03880v1

## Abstract

We propose a design that uses the principle of chaos for UAV secure communication. A UAV identified as an aerial base station communicates with a ground base station over an RF channel. The communication units have dynamics based on the logistic map. The map is chaotic in the appropriate parameter space. Its states are non-periodic, broadband, and noise-like in the frequency domain. They are useful for spreading information during transmission, making it difficult for an eavesdropper to recover the modulated message since state prediction is ultimately impossible. To retrieve it, we propose a variable feedback controller. It asymptotically stabilizes the error dynamics when the information source is off. During transmission, the controller synchronizes the units such that the error contains signatures of the information signal. Therefore, the information signal is retrievable by a suitable detection mechanism. Security depends on the confidentiality of the map, the variable feedback controller, including its scale factor and bounded feedback gain, and the designer`s choice of invertible function for use in the scrambling and descrambling process. Also, the method is less prone to jamming attacks and multipath effects as the broadband spectrum can be used to randomly select RF channels. It uses only a few simple algorithms, including a correlation summation and a detection mechanism. The algorithms collect subsamples of the received signal sequences and averages over each subsample length. The method requires minimal programming efforts and low hardware resource utilization. It is energy-efficient, which is a vital consideration for any UAV security model. Moreover, we realize a prototype of the communication system on field-programmable gate arrays. We presented a digital design of the secure communication system involving the transmission of bitstreams between the ABS and GBS.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
