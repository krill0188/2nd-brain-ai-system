---
title: "Edge-Constrained UAV Small-Object Detection with P2 Enhancement and Quantum-Inspired Lightweight Structure Search"
created: 2026-08-12
updated: 2026-08-12
type: paper
item_type: preprint
authors: "Lei, Wuming; Gao, Yanbin; Sun, Mingyan; Li, Xiaobin; Liang, Xuechen"
year: "2026"
doi: "10.48550/arXiv.2606.09081"
url: "http://arxiv.org/abs/2606.09081v1"
zotero_key: 9S66I8N6
tags: ["auto:2nd-brain", "drone-ai"]
attachment_path: raw/papers/files/drone-ai/edge-constrained-uav-small-object-detection-with-p2-enhancement-and-quantum-insp.pdf
attachment_sha256: b51445fceb783cb4fa6e160c137f9cd49ae63fc0f7bb18c03bdf6caeebef2554
sha256: 2aae1b59e94a4dfb
---

# Edge-Constrained UAV Small-Object Detection with P2 Enhancement and Quantum-Inspired Lightweight Structure Search

**Authors**: Lei, Wuming; Gao, Yanbin; Sun, Mingyan; Li, Xiaobin; Liang, Xuechen  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2606.09081  
**URL**: http://arxiv.org/abs/2606.09081v1

## Abstract

Unmanned aerial vehicle (UAV) object detection requires compact detectors that retain small-object details under onboard computation and memory constraints. Repeated downsampling inlightweight networks weakens shallow spatial information, while manually adding attention orfusion modules may increase cost without stable gains. This study analyzes YOLOX-Nano underedge-deployment constraints by combining a P2 high-resolution detection branch with a quantum-inspired evolutionary algorithm (QIEA) for lightweight structure screening. The search space isdefined by lightweight priority and task specificity, and the evaluation jointly considers accuracy,floating-point operations (FLOPs), latency, memory consumption, and recall. On VisDrone, theP2 branch increases APamall by 31.10% over the YOLOX-Nano baseline. Compared with NanoDet-Plus with similar model size, YOLOX-Nano+-P2 improves APs0.ss by 17.5% and APamal by 44.9%.The QIEA-selected candidate obtains the highest Recallso, but +P2 remains the strongest AP-oriented variant after full training. Full 100-epoch verification of Random-best, GA-best, andSA/QUBO-best candidates further shows that proxy rankings do not necessarily transfer to finalAPse9s. These results support using P2 as the main small-object enhancement path and QIEA as alightweight tool for candidate screening and accuracy-cost analysis. The source code, configurationfiles, diagnostic scripts, and summarized results are available at https://github.com/Ming23233/UAV-QIEA-Edge-Detection

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
