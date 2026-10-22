---
title: "UAV-Based 3D Spectrum Sensing: Insights on Altitude, Bandwidth, Trajectory, and Effective Antenna Patterns on REM Reconstruction"
created: 2026-10-22
updated: 2026-10-22
type: paper
item_type: preprint
authors: "Rahman, Mushfiqur; Maeng, Sung Joon; Guvenc, Ismail; Wong, Chau-Wai; Sichitiu, Mihail; Abrahamson, Jason A.; Bhuyan, Arupjyoti"
year: "2026"
doi: "10.48550/arXiv.2603.10362"
url: "http://arxiv.org/abs/2603.10362v2"
zotero_key: 7HDIN2GS
tags: ["auto:2nd-brain"]
sha256: 8f3782b7187c9582
---

# UAV-Based 3D Spectrum Sensing: Insights on Altitude, Bandwidth, Trajectory, and Effective Antenna Patterns on REM Reconstruction

**Authors**: Rahman, Mushfiqur; Maeng, Sung Joon; Guvenc, Ismail; Wong, Chau-Wai; Sichitiu, Mihail; Abrahamson, Jason A.; Bhuyan, Arupjyoti  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2603.10362  
**URL**: http://arxiv.org/abs/2603.10362v2

## Abstract

Spectrum sensing and the generation of 3D Radio Environment Maps (REMs) are essential for enabling spectrum sharing within cognitive radio networks. While Uncrewed Aerial Vehicles (UAVs) offer high-mobility 3D sensing, REM accuracy is challenged by dynamic flight behaviors, where fluctuations in UAV speed and direction introduce measurement inconsistencies. Furthermore, the airframe itself impacts the onboard antenna's radiation characteristics. In this paper, using real-world data, we systematically analyze how REM reconstruction accuracy is shaped by three key pillars: physical sensing parameters like altitude and bandwidth, environmental shadowing, and distortions caused by the UAV airframe. First, we benchmark diverse spatial prediction models, including simple Kriging (SK), ordinary Kriging (OK), trans-Gaussian Kriging, and Gaussian process regression (GPR). We demonstrate that while SK and its trans-Gaussian variant are highly accurate at extreme sample sparsity, OK improves as sample size increases, and GPR serves as the most stable overall baseline. Building on this, we propose a novel matrix completion (MC)-assisted GPR framework that enhances REM reconstruction in the presence of non-uniform spatial smoothness. The method operates by decomposing the REM into two distinct layers: a global smooth component and a highly varying local component. Our analysis based on real-world measurements reveals three key findings: 1) REM accuracy and shadowing variance follow a distinct tri-phasic trend as the UAV altitude increases; 2) REM accuracy significantly improves with increased spectrum bandwidth; and 3) antenna pattern calibration from in-field measurements significantly enhances REM accuracy by accounting for the effect of the UAV airframe.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
