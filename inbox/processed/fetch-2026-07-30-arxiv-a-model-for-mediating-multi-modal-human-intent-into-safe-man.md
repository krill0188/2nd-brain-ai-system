---
title: "A Model for Mediating Multi-Modal Human Intent into Safe Maneuvers for UAVs"
created: 2026-07-30
captured: 2026-07-30
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2607.11654v1
authors: "Sofia Nelson, Dalal Alrajeh, Pedro Antonio Alarcon Granadeno, Jane Cleland-Huang"
published: "2026-07-13"
tags: [drone, ai-autonomy, paper, arxiv]
---

# A Model for Mediating Multi-Modal Human Intent into Safe Maneuvers for UAVs

**Authors**: Sofia Nelson, Dalal Alrajeh, Pedro Antonio Alarcon Granadeno, Jane Cleland-Huang
**Published**: 2026-07-13
**arXiv**: http://arxiv.org/abs/2607.11654v1

## Abstract

Direct human interaction with autonomous UAV systems can be enabled through modalities such as speech, gestures, and graphical interfaces. However, interpreting such inputs as directly executable commands introduces safety risks in dynamic environments. Operator requests may conflict with terrain constraints, inter-UAV separation requirements, or flight-envelope limitations. In this paper, we present a requirements-governed maneuver-response model that mediates multi-modal human intent into safe UAV maneuvers by treating operator inputs as bounded maneuver requests rather than direct commands. Requested maneuvers are mapped to constrained motion primitives and processed through a structured request-evaluate-execute pipeline. Each request is interpreted with associated confidence, validated against terrain, separation, workspace, and flight-envelope constraints, and either constrained, rejected, or executed under continuous runtime monitoring. We further formalize the approach as a requirements-based specification model in which maneuver primitives are associated with explicit preconditions, invariants, guard conditions, and postconditions governing admissibility, execution safety, and emergency handling. These requirements support runtime verification and future reactive synthesis approaches. We present an initial lab-based validation demonstrating that voice and GUI-based inputs can be reliably interpreted and safely executed as constrained maneuver requests.
