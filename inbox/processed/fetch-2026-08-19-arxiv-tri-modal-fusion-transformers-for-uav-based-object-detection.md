---
title: "Tri-Modal Fusion Transformers for UAV-based Object Detection"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2604.16630v1
authors: "Craig Iaboni, Pramod Abichandani"
published: "2026-04-17"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Tri-Modal Fusion Transformers for UAV-based Object Detection

**Authors**: Craig Iaboni, Pramod Abichandani
**Published**: 2026-04-17
**arXiv**: http://arxiv.org/abs/2604.16630v1

## Abstract

Reliable UAV object detection requires robustness to illumination changes, motion blur, and scene dynamics that suppress RGB cues. Thermal long-wave infrared (LWIR) sensing preserves contrast in low light, and event cameras retain microsecond-level temporal edges, but integrating all three modalities in a unified detector has not been systematically studied. We present a tri-modal framework that processes RGB, thermal, and event data with a dual-stream hierarchical vision transformer. At selected encoder depths, a Modality-Aware Gated Exchange (MAGE) applies inter-sensor channel and spatial gating, and a Bidirectional Token Exchange (BiTE) module performs bidirectional token-level attention with depthwise-pointwise refinement, producing resolution-preserving fused maps for a standard feature pyramid and two-stage detector. We introduce a 10,489-frame UAV dataset with synchronized and pre-aligned RGB-thermal-event streams and 24,223 annotated vehicles across day and night flights. Through 61 controlled ablations, we evaluate fusion placement, mechanism (baseline MAGE+BiTE, CSSA, GAFF), modality subsets, and backbone capacity. Tri-modal fusion improves over all dual-modal baselines, with fusion depth having a significant effect and a lightweight CSSA variant recovering most of the benefit at minimal cost. This work provides the first systematic benchmark and modular backbone for tri-modal UAV-based object detection.
