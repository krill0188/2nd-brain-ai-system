---
title: "A Novel Cipher for Enhancing MAVLink Security: Design, Security Analysis, and Performance Evaluation Using a Drone Testbed"
created: 2026-08-23
captured: 2026-08-23
type: paper
domain: gcs-software
source: http://arxiv.org/abs/2504.20626v1
authors: "Bhavya Dixit, Ananthapadmanabhan A., Adheeba Thahsin, Saketh Pathak, Gaurav S. Kasbekar, Arnab Maity"
published: "2025-04-29"
tags: [drone, gcs-software, paper, arxiv]
---

# A Novel Cipher for Enhancing MAVLink Security: Design, Security Analysis, and Performance Evaluation Using a Drone Testbed

**Authors**: Bhavya Dixit, Ananthapadmanabhan A., Adheeba Thahsin, Saketh Pathak, Gaurav S. Kasbekar, Arnab Maity
**Published**: 2025-04-29
**arXiv**: http://arxiv.org/abs/2504.20626v1

## Abstract

We present MAVShield, a novel lightweight cipher designed to secure communications in Unmanned Aerial Vehicles (UAVs) using the MAVLink protocol, which by default transmits unencrypted messages between UAVs and Ground Control Stations (GCS). While existing studies propose encryption for MAVLink, most remain theoretical or simulation-based. We implement MAVShield alongside AES-CTR, ChaCha20, Speck-CTR, and Rabbit, and evaluate them on a real drone testbed. A comprehensive security analysis using statistical test suites (NIST and Diehard) demonstrates strong resistance of the novel cipher to cryptanalysis. Performance evaluation across key metrics including memory usage, CPU load, and battery power consumption, demonstrates that MAVShield outperforms existing algorithms and offers an efficient, real-world solution for securing MAVLink communications in UAVs.
