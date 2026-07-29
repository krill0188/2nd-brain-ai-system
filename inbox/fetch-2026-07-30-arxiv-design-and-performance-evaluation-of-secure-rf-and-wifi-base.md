---
title: "Design and Performance Evaluation of Secure RF and WiFi-Based Communication in Drone Swarms via Testbed Implementation"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2606.27028v1
authors: "Bhavya Dixit, Aayushi Rajgor, Subham Kumar, Rushikesh Patil, Ananthapadmanabhan A., Gaurav S. Kasbekar, Arnab Maity"
published: "2026-06-25"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Design and Performance Evaluation of Secure RF and WiFi-Based Communication in Drone Swarms via Testbed Implementation

**Authors**: Bhavya Dixit, Aayushi Rajgor, Subham Kumar, Rushikesh Patil, Ananthapadmanabhan A., Gaurav S. Kasbekar, Arnab Maity
**Published**: 2026-06-25
**arXiv**: http://arxiv.org/abs/2606.27028v1

## Abstract

Unmanned aerial vehicle (UAV) swarms rely on distributed coordination and cooperative communication to support scalable operations, extended coverage, and applications such as surveillance and real-time data exchange. Wireless technologies such as radio frequency (RF) and WiFi are widely used for UAV-to-UAV and UAV-to-ground control station (GCS) communication but introduce significant security challenges. MAVLink, the predominant communication protocol in UAV systems, provides message integrity and authentication but lacks built-in encryption, leaving telemetry traffic vulnerable to eavesdropping. In our previous work, we proposed MAVShield, a lightweight encryption framework for MAVLink communications. In this paper, MAVShield, AES-CTR, Speck-CTR, ChaCha20, and Rabbit are integrated into four custom-built UAVs to establish secure communication links over RF and WiFi channels. Their performance is evaluated through flight experiments using a UAV swarm testbed. Encrypted telemetry data enable autonomous formation control and collision avoidance during flight. For collision avoidance, we develop a modified artificial potential field (APF) algorithm that computes attractive and repulsive forces directly in geodetic coordinates, eliminating Cartesian transformations and reducing trajectory oscillations while avoiding local-minimum trapping. CPU utilization, memory consumption, and packet delivery ratio (PDR) are measured for each encryption scheme. Results show that MAVShield achieves performance comparable to unencrypted communication while outperforming AES-CTR, Speck-CTR, ChaCha20, and Rabbit in overall efficiency. Algebraic cryptanalysis and Wireshark-based traffic analysis demonstrate resistance to key-recovery attacks and protection of telemetry confidentiality. The results indicate that MAVShield is an efficient and secure solution for UAV swarm communication.
