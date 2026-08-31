---
title: "Weighted strategies to guide a multi-objective evolutionary algorithm for multi-UAV mission planning"
created: 2026-08-31
captured: 2026-08-31
type: paper
domain: gcs-software
source: http://arxiv.org/abs/2402.18749v1
authors: "Cristian Ramirez-Atencia, Javier Del Ser, David Camacho"
published: "2024-02-28"
tags: [drone, gcs-software, paper, arxiv]
---

# Weighted strategies to guide a multi-objective evolutionary algorithm for multi-UAV mission planning

**Authors**: Cristian Ramirez-Atencia, Javier Del Ser, David Camacho
**Published**: 2024-02-28
**arXiv**: http://arxiv.org/abs/2402.18749v1

## Abstract

Management and mission planning over a swarm of unmanned aerial vehicle (UAV) remains to date as a challenging research trend in what regards to this particular type of aircrafts. These vehicles are controlled by a number of ground control station (GCS), from which they are commanded to cooperatively perform different tasks in specific geographic areas of interest. Mathematically the problem of coordinating and assigning tasks to a swarm of UAV can be modeled as a constraint satisfaction problem, whose complexity and multiple conflicting criteria has hitherto motivated the adoption of multi-objective solvers such as multi-objective evolutionary algorithm (MOEA). The encoding approach consists of different alleles representing the decision variables, whereas the fitness function checks that all constraints are fulfilled, minimizing the optimization criteria of the problem. In problems of high complexity involving several tasks, UAV and GCS, where the space of search is huge compared to the space of valid solutions, the convergence rate of the algorithm increases significantly. To overcome this issue, this work proposes a weighted random generator for the creation and mutation of new individuals. The main objective of this work is to reduce the convergence rate of the MOEA solver for multi-UAV mission planning using weighted random strategies that focus the search on potentially better regions of the solution space. Extensive experimental results over a diverse range of scenarios evince the benefits of the proposed approach, which notably improves this convergence rate with respect to a naïve MOEA approach.
