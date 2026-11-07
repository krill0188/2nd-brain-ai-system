---
title: "KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL"
created: 2026-11-07
updated: 2026-11-07
type: paper
item_type: preprint
authors: "Ramachandran, Aswin; Schulz, Jona; Derungs, Maurus; Angelini, Carlo; Meier, Tobias; D'Andrea, Raffaello"
year: "2026"
doi: "10.48550/arXiv.2611.03138"
url: "http://arxiv.org/abs/2611.03138v1"
zotero_key: XJQX6585
tags: ["auto:2nd-brain"]
sha256: 073ae7b6ca75cdc2
---

# KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL

**Authors**: Ramachandran, Aswin; Schulz, Jona; Derungs, Maurus; Angelini, Carlo; Meier, Tobias; D'Andrea, Raffaello  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2611.03138  
**URL**: http://arxiv.org/abs/2611.03138v1

## Abstract

Progress in robot learning, particularly physical multi-agent reinforcement learning (MARL), is currently challenged by a limited availability of accessible, standardized benchmarks. While simulation-based MARL has produced remarkable emergent behaviors, from coordinated team play to complex tool use, translating these advances to physical systems remains difficult. A key barrier is infrastructural: physical platforms are often prohibitively expensive, require specialized facilities, or lack open mechanisms and designs for reproducibility. We introduce KlaskTron, an open-source, low-cost (<\$2500 USD), desktop-scale robotic testbed for adversarial MARL based on the dynamic tabletop game KLASK. The platform features dual CoreXY gantries with high-torque brushless motors, enabling the high-speed, precise manipulation required for competitive play. Crucially, we provide a complete ecosystem: hardware designs (CAD, BOM), a GPU-native digital twin in NVIDIA Isaac Lab for high-fidelity modeling and simulation, and a validated sim-to-real baseline using a learned neural actuator model. We demonstrate that this baseline enables zero-shot policy transfer, with trained agents exhibiting emergent adversarial behaviors. To ensure full reproducibility of our results, all project assets are released publicly: hardware CAD/BOM and assembly documentation at [https://idscethzurich.github.io/klask_hardware], inference software stack at [https://github.com/IDSCETHZurich/klask_software] and the simulation and MARL setup at [https://github.com/IDSCETHZurich/klask_rl].

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
