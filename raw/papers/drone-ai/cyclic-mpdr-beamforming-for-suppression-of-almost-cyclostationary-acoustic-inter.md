---
title: "Cyclic MPDR Beamforming for Suppression of Almost-Cyclostationary Acoustic Interference"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: preprint
authors: "Bologni, Giovanni; M\u00f8ller, Martin Bo; Heusdens, Richard; Hendriks, Richard C."
year: "2025"
doi: "10.48550/arXiv.2510.18391"
url: "http://arxiv.org/abs/2510.18391v3"
zotero_key: 6M4G5DNG
tags: ["auto:2nd-brain"]
sha256: 477415c810a71c80
---

# Cyclic MPDR Beamforming for Suppression of Almost-Cyclostationary Acoustic Interference

**Authors**: Bologni, Giovanni; Møller, Martin Bo; Heusdens, Richard; Hendriks, Richard C.  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2510.18391  
**URL**: http://arxiv.org/abs/2510.18391v3

## Abstract

Conventional acoustic beamformers typically assume short-time stationarity and process frequency bins independently, ignoring inter-frequency correlations. This is suboptimal for almost-periodic noise sources such as engines, fans, and musical instruments: these signals are better modeled as (almost) cyclostationary (ACS) processes with statistically correlated spectral components. This paper introduces the cyclic minimum power distortionless response (cMPDR) beamformer, which extends the conventional MPDR to jointly exploit spatial and spectral correlations. Building on frequency-shifted (FRESH) filtering, it suppresses noise components that are coherent across harmonically related frequencies, reducing residual noise beyond what spatial filtering alone can achieve. To address inharmonicity, where partials deviate from exact integer multiples of a fundamental frequency, we estimate resonant frequencies from a periodogram and derive frequency shifts from their pairwise spacing. Theoretical analysis yields closed-form expressions for residual noise and proves that output power decreases monotonically with the number of cyclic components. Experiments on synthetic harmonic noise and real UAV motor recordings confirm these findings: in low-SNR scenarios, the cMPDR achieves up to 5 dB improvement in SI-SDR over the MPDR, yields consistent STOI gains, and remains effective with a single microphone. When spectral correlation is absent, the method reduces to conventional MPDR and does not degrade performance. These results suggest that cyclic processing is a viable direction for acoustic noise reduction that deserves further investigation. Code and audio samples are available at https://github.com/Screeen/cMPDR.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
