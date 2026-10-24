---
title: "Outage Analysis and Bilevel Resource Optimization in RIS-Assisted Clustered UAV-NOMA Networks"
created: 2026-10-24
captured: 2026-10-24
type: paper
domain: comms-protocol
source: http://arxiv.org/abs/2610.30410v1
authors: "Masoud Ghazikor, Ly V. Nguyen, Morteza Hashemi"
published: "2026-10-21"
tags: [drone, comms-protocol, paper, arxiv]
attachment_path: raw/papers/files/comms-protocol/outage-analysis-and-bilevel-resource-optimization-in-ris-ass.html
attachment_type: html
attachment_sha256: 3393f6c390af92b91d72fb9e4de81c70e11fc5af01a08b2ed099de098c3a3965
---

# Outage Analysis and Bilevel Resource Optimization in RIS-Assisted Clustered UAV-NOMA Networks

**Authors**: Masoud Ghazikor, Ly V. Nguyen, Morteza Hashemi
**Published**: 2026-10-21
**arXiv**: http://arxiv.org/abs/2610.30410v1

## Abstract

This paper investigates RIS-assisted downlink UAV communications based on NOMA. Since conventional NOMA becomes difficult to scale as the number of UAVs grows, we develop a cluster-based UAV-NOMA framework in which a BS serves multiple UAV groups with the aid of partitionable RISs. Within this framework, we consider direct, RIS-only indirect, and composite links, and develop an analytical model for the received SNR and outage performance under Nakagami-$m$ and double Nakagami-$m$ fading with imperfect SIC. To enable scalable transmission, we introduce a greedy RIS-aware (GRIS) clustering method, which groups UAVs according to spatial and channel-related features. Based on the resulting clusters and RIS assignment, we formulate an efficiency-reliability bilevel optimization problem that jointly optimizes inter-cluster BS power allocation, intra-cluster NOMA power coefficients, and RIS element assignment. Specifically, the outer efficiency problem maximizes the average throughput across clusters, while the inner reliability problem minimizes the worst-UAV outage probability within each cluster. To solve the formulated problem, we propose a two-level iterative framework consisting of an inter-cluster outer-efficiency solver (IOS) and an intra-cluster inner-reliability solver (I2S), where I2S combines a grid-based progressive search (GPS) for NOMA power refinement with reliability-guided RIS element reassignment, and IOS updates the BS power weights. Numerical results demonstrate the effectiveness of GRIS clustering, while pre-optimization analysis reveals efficiency-reliability trade-offs in power allocation. Baseline comparisons illustrate the ability of IOS-I2S to balance efficiency and reliability, while ablation studies highlight the importance of joint optimization.
