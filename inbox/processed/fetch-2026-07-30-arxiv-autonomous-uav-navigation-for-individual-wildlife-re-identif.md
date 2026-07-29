---
title: "Autonomous UAV Navigation for Individual Wildlife Re-Identification"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2606.31772v1
authors: "Claire Sun, Tanya Berger-Wolf, Jenna Kline"
published: "2026-06-30"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Autonomous UAV Navigation for Individual Wildlife Re-Identification

**Authors**: Claire Sun, Tanya Berger-Wolf, Jenna Kline
**Published**: 2026-06-30
**arXiv**: http://arxiv.org/abs/2606.31772v1

## Abstract

Reliable individual re-identification (re-ID) of wildlife is essential for population monitoring, behavioral tracking, and conservation policy evaluation, yet large-scale data collection remains labor-intensive, relying on manual efforts by ecologists or citizen scientists. We propose an autonomous drone navigation system that actively optimizes image capture for downstream re-ID, moving beyond passive aerial sensing. The system combines YOLOv11 object detection with a DINOv2-based pose classifier to guide real-time flight decisions: detecting animals, orienting to expose the lateral flank (the surface of interest for pattern-based re-ID), and approaching until the subject meets a minimum bounding-box threshold. Unlike prior drone systems that optimize for group-level behavioral video, ours targets the specific image-quality requirements of individual-identification models. We demonstrate feasibility through a case study on zebra using footage collected in Kenya, and show the approach generalizes to other species with diagnostic surface patterns, including giraffes, tigers, and elephants. Our work establishes a framework for task-aware embodied AI for ecological data collection, in which downstream re-ID requirements drive real-time perception and control.
