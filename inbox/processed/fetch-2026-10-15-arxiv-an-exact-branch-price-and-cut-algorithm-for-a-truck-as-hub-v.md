---
title: "An Exact Branch-Price-and-Cut Algorithm for a Truck-as-Hub Vehicle Routing Problem with Drones"
created: 2026-10-15
captured: 2026-10-15
type: paper
domain: comms-protocol
source: http://arxiv.org/abs/2610.15016v1
authors: "Fan Pu, Sivakumar Rathinam, Yunlong Zhang, Xiaopeng Li, Xiubin Wang, Yang Zhou"
published: "2026-10-10"
tags: [drone, comms-protocol, paper, arxiv]
attachment_path: raw/papers/files/comms-protocol/an-exact-branch-price-and-cut-algorithm-for-a-truck-as-hub-v.html
attachment_type: html
attachment_sha256: e248026b09ee293cdbf35b5e1cba5589d5aed09e8fafff52c59b531fc35b409c
---

# An Exact Branch-Price-and-Cut Algorithm for a Truck-as-Hub Vehicle Routing Problem with Drones

**Authors**: Fan Pu, Sivakumar Rathinam, Yunlong Zhang, Xiaopeng Li, Xiubin Wang, Yang Zhou
**Published**: 2026-10-10
**arXiv**: http://arxiv.org/abs/2610.15016v1

## Abstract

Rural last-mile logistics remains challenging because of sparse demand, limited road infrastructure, and long travel distances. We study a Truck-as-Hub Vehicle Routing Problem with Drones in Rural Areas, in which multiple trucks each carry a dedicated fleet of drones. Drone launch and retrieval are restricted to predesignated passive synchronization pads, where a visiting truck temporarily acts as a mobile hub, may dispatch multiple drones simultaneously, and must wait until all launched drones return before continuing its route. We formulate a mixed-integer quadratic programming model that jointly accounts for customer delivery delays, truck return times, and operating costs. To solve the problem exactly, we transform the original truck--drone network so that each feasible route can be represented as a single path and develop a branch-price-and-cut algorithm with tailored pricing, cutting, branching, and parallel-computing procedures. Computational experiments show that the proposed algorithm proves optimality for most large-scale test cases and achieves optimality gaps of no more than 4% for the remaining cases, whereas Gurobi reaches the 1,800-second time limit on all large-scale instances when applied directly to the compact formulation. Sensitivity analyses show that drone operating costs and managerial priorities substantially affect drone utilization and customer delays, providing practical guidance for balancing service quality and operating cost in rural delivery systems.
