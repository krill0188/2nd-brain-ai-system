---
title: "SCORE: Shape-Conforming Regions for Flight in Enclosed, Degraded Environments"
created: 2026-08-19
updated: 2026-08-19
type: paper
item_type: preprint
authors: "Kim, Eric Minwoo; Kim, Jong-Kook"
year: "2026"
doi: "10.48550/arXiv.2608.15289"
url: "http://arxiv.org/abs/2608.15289v1"
zotero_key: FGQJFNQ4
tags: ["auto:2nd-brain"]
sha256: 23024aa2070a0178
---

# SCORE: Shape-Conforming Regions for Flight in Enclosed, Degraded Environments

**Authors**: Kim, Eric Minwoo; Kim, Jong-Kook  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.15289  
**URL**: http://arxiv.org/abs/2608.15289v1

## Abstract

Autonomous UAVs enter enclosed environments such as caves and collapsed structures that confine the vehicle and degrade perception. Conformal prediction provides a distribution-free guarantee by calibrating how far an obstacle keep-out must expand to absorb perception error at a target coverage level. However, existing keep-out regions use convex primitives whose bulges consume narrow passages and grow as perception degrades. Our main contribution defines the nonconformity score on a signed distance field (SDF). This produces a non-convex keep-out that tightly follows obstacle geometry and avoids the unnecessary bulging of equal-margin convex regions. Two supporting components keep this geometry usable as perception degrades. First, a voxelwise union of complementary sensor observations certifies voxels that any single sensor misses. Second, the margin around the obstacle adapts to measured visibility without weather labels or the online ground-truth feedback that single-pass flight cannot provide. Results on real subterranean data show that the resulting distribution-free, shape-conforming keep-out retains more usable free space than convex baselines at the same certified coverage, and produces safer closed-loop flight.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
