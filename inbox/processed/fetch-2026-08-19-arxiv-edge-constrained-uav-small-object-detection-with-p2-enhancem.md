---
title: "Edge-Constrained UAV Small-Object Detection with P2 Enhancement and Quantum-Inspired Lightweight Structure Search"
created: 2026-08-19
captured: 2026-08-19
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2606.09081v1
authors: "Wuming Lei, Yanbin Gao, Mingyan Sun, Xiaobin Li, Xuechen Liang"
published: "2026-06-08"
tags: [drone, ai-autonomy, paper, arxiv]
---

# Edge-Constrained UAV Small-Object Detection with P2 Enhancement and Quantum-Inspired Lightweight Structure Search

**Authors**: Wuming Lei, Yanbin Gao, Mingyan Sun, Xiaobin Li, Xuechen Liang
**Published**: 2026-06-08
**arXiv**: http://arxiv.org/abs/2606.09081v1

## Abstract

Unmanned aerial vehicle (UAV) object detection requires compact detectors that retain small-object details under onboard computation and memory constraints. Repeated downsampling inlightweight networks weakens shallow spatial information, while manually adding attention orfusion modules may increase cost without stable gains. This study analyzes YOLOX-Nano underedge-deployment constraints by combining a P2 high-resolution detection branch with a quantum-inspired evolutionary algorithm (QIEA) for lightweight structure screening. The search space isdefined by lightweight priority and task specificity, and the evaluation jointly considers accuracy,floating-point operations (FLOPs), latency, memory consumption, and recall. On VisDrone, theP2 branch increases APamall by 31.10% over the YOLOX-Nano baseline. Compared with NanoDet-Plus with similar model size, YOLOX-Nano+-P2 improves APs0.ss by 17.5% and APamal by 44.9%.The QIEA-selected candidate obtains the highest Recallso, but +P2 remains the strongest AP-oriented variant after full training. Full 100-epoch verification of Random-best, GA-best, andSA/QUBO-best candidates further shows that proxy rankings do not necessarily transfer to finalAPse9s. These results support using P2 as the main small-object enhancement path and QIEA as alightweight tool for candidate screening and accuracy-cost analysis. The source code, configurationfiles, diagnostic scripts, and summarized results are available at https://github.com/Ming23233/UAV-QIEA-Edge-Detection
