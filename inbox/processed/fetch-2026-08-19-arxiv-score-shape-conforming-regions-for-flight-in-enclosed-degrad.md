---
title: "SCORE: Shape-Conforming Regions for Flight in Enclosed, Degraded Environments"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2608.15289v1
authors: "Eric Minwoo Kim, Jong-Kook Kim"
published: "2026-08-15"
tags: [drone, ai-autonomy, paper, arxiv]
---

# SCORE: Shape-Conforming Regions for Flight in Enclosed, Degraded Environments

**Authors**: Eric Minwoo Kim, Jong-Kook Kim
**Published**: 2026-08-15
**arXiv**: http://arxiv.org/abs/2608.15289v1

## Abstract

Autonomous UAVs enter enclosed environments such as caves and collapsed structures that confine the vehicle and degrade perception. Conformal prediction provides a distribution-free guarantee by calibrating how far an obstacle keep-out must expand to absorb perception error at a target coverage level. However, existing keep-out regions use convex primitives whose bulges consume narrow passages and grow as perception degrades. Our main contribution defines the nonconformity score on a signed distance field (SDF). This produces a non-convex keep-out that tightly follows obstacle geometry and avoids the unnecessary bulging of equal-margin convex regions. Two supporting components keep this geometry usable as perception degrades. First, a voxelwise union of complementary sensor observations certifies voxels that any single sensor misses. Second, the margin around the obstacle adapts to measured visibility without weather labels or the online ground-truth feedback that single-pass flight cannot provide. Results on real subterranean data show that the resulting distribution-free, shape-conforming keep-out retains more usable free space than convex baselines at the same certified coverage, and produces safer closed-loop flight.
