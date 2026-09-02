---
title: "Generalizable Multi-Agent Planning from Signal Temporal Logic Specifications via Diffusion"
created: 2026-09-02
updated: 2026-09-02
type: paper
item_type: preprint
authors: "Eappen, Joe; Xiong, Zikang; Iyengar, Shreyash S.; Jagannathan, Suresh"
year: "2026"
doi: "10.48550/arXiv.2608.29490"
url: "http://arxiv.org/abs/2608.29490v1"
zotero_key: 6KGEHQGJ
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/swarm/generalizable-multi-agent-planning-from-signal-temporal-logic-specifications-via.pdf
attachment_sha256: 53c0f319bb791333feef69827ad49a23d4ab86c6ad798648835ffbf2fd90925c
sha256: 5cf5fd2ba827bc81
---

# Generalizable Multi-Agent Planning from Signal Temporal Logic Specifications via Diffusion

**Authors**: Eappen, Joe; Xiong, Zikang; Iyengar, Shreyash S.; Jagannathan, Suresh  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.29490  
**URL**: http://arxiv.org/abs/2608.29490v1

## Abstract

Multi-agent systems in the real-world (e.g., drone swarms, autonomous cars, warehouse robots) must satisfy rich, temporal tasks while avoiding collisions. Signal Temporal Logic (STL) elegantly encodes such objectives, but current STL planning methods face critical limitations. State-of-the-art optimization-based approaches can handle arbitrary STL specifications but struggle with scalability, becoming computationally impractical as the number of agents grows. Learning-based methods efficiently handle a large number of agents with rapid planning times but fare poorly when deployment-time objectives differ from those used during training, and do not support planning tasks that require different specifications to be ascribed to different agents (i.e., heterogeneity) or team-level specifications requiring coordination of multiple agents. This fundamental trade-off between generalizability and scalability presents a challenge for realizing multi-agent STL planning algorithms in practice. To overcome this challenge, we introduce a new diffusion method for multi-agent planning with STL specifications. Using a differentiable approximation of STL, we integrate the STL gradient in the denoising process, making our approach generalizable to novel formulas whose predicates are placed anywhere within the goal region covered during training, while achieving the same scalability as existing learning-based methods. Our method supports heterogeneous specifications, and by using diffusion models, naturally enhances plan diversity, thereby significantly reducing safety-related violations (e.g., collisions) among agents. A detailed evaluation study justifies the utility of STL-guided diffusion-based multi-agent planners for constructing generalizable, scalable, and diverse plans. Videos and code are available at https://www.jeappen.com/diff-ma-stl/ and https://github.com/jeappen/diff-ma-stl .

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
