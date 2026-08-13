---
title: "Clustered Randomized Smoothing for Stochastic Prediction Functions"
created: 2026-08-13
updated: 2026-08-13
type: paper
item_type: preprint
authors: "Figueiredo, Eduardo; Mathiesen, Frederik; Schumann, Julian; Kober, Jens; Zgonnikov, Arkady; Laurenti, Luca"
year: "2026"
doi: "10.48550/arXiv.2608.12037"
url: "http://arxiv.org/abs/2608.12037v1"
zotero_key: AV5NSSI3
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/_unclassified/clustered-randomized-smoothing-for-stochastic-prediction-functions.pdf
attachment_sha256: 6475cd552cee045cd08f3775fc43bf4341166aea744471ae8a5c485be8805dc8
sha256: 4f4c3151ce274c62
---

# Clustered Randomized Smoothing for Stochastic Prediction Functions

**Authors**: Figueiredo, Eduardo; Mathiesen, Frederik; Schumann, Julian; Kober, Jens; Zgonnikov, Arkady; Laurenti, Luca  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2608.12037  
**URL**: http://arxiv.org/abs/2608.12037v1

## Abstract

Modern stochastic predictors can model rich, multi-modal outcome distributions. However, this expressive power comes with challenges in ensuring robust predictions $-$ a critical requirement in safety-critical domains. Randomized smoothing is a leading technique for improving robustness, particularly against adversarial perturbations. Yet, in stochastic multi-modal regression settings, randomized smoothing often fails due to mode collapse, yielding averaged predictions that do not reflect the underlying distribution. To address this limitation, we propose clustered $α$-smoothing, a framework that (1) partitions noisy samples using an arbitrary clustering algorithm, (2) applies $α$-smoothing locally within each cluster, and (3) combines the resulting predictions into a mixture distribution. By interpreting the smoothing distribution as a mixture of $α$-smoothers, we derive a lower bound on the probability that the smoothed prediction lies within a union of compact regions corresponding to distinct modes. We empirically evaluate our framework on two benchmarks, demonstrating substantial improvements over state-of-the-art methods. In stochastic trajectory prediction on a driving simulator dataset, our approach achieves, on average, a $27\%$ lower Wasserstein distance to the ground-truth distribution compared to $α$-smoothing. In quadrotor control, where modes correspond to distinct feasible paths to a target, our method reduces the collision rate by $81\%$ relative to the state-of-the-art randomized smoothing.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
