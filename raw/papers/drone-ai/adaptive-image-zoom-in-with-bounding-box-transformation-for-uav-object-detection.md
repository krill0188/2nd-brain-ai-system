---
title: "Adaptive Image Zoom-in with Bounding Box Transformation for UAV Object Detection"
created: 2026-08-20
updated: 2026-08-20
type: paper
item_type: preprint
authors: "Wang, Tao; Lin, Chenyu; Tang, Chenwei; Zhou, Jizhe; Xiong, Deng; Li, Jianan; Zhao, Jian; Lv, Jiancheng"
year: "2026"
doi: "10.48550/arXiv.2602.07512"
url: "http://arxiv.org/abs/2602.07512v2"
zotero_key: 28TUMNV4
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/adaptive-image-zoom-in-with-bounding-box-transformation-for-uav-object-detection.pdf
attachment_sha256: a7f6ffb1c906a45fdba335251db88d9c2191463afa845a765e90c007344b701f
sha256: 5938c5e3a80d56fb
---

# Adaptive Image Zoom-in with Bounding Box Transformation for UAV Object Detection

**Authors**: Wang, Tao; Lin, Chenyu; Tang, Chenwei; Zhou, Jizhe; Xiong, Deng; Li, Jianan; Zhao, Jian; Lv, Jiancheng  
**Year**: 2026  
**DOI**: 10.48550/arXiv.2602.07512  
**URL**: http://arxiv.org/abs/2602.07512v2

## Abstract

Detecting objects from UAV-captured images is challenging due to the small object size. In this work, a simple and efficient adaptive zoom-in framework is explored for object detection on UAV images. The main motivation is that the foreground objects are generally smaller and sparser than those in common scene images, which hinders the optimization of effective object detectors. We thus aim to zoom in adaptively on the objects to better capture object features for the detection task. To achieve the goal, two core designs are required: \textcolor{black}{i) How to conduct non-uniform zooming on each image efficiently? ii) How to enable object detection training and inference with the zoomed image space?} Correspondingly, a lightweight offset prediction scheme coupled with a novel box-based zooming objective is introduced to learn non-uniform zooming on the input image. Based on the learned zooming transformation, a corner-aligned bounding box transformation method is proposed. The method warps the ground-truth bounding boxes to the zoomed space to learn object detection, and warps the predicted bounding boxes back to the original space during inference. We conduct extensive experiments on three representative UAV object detection datasets, including VisDrone, UAVDT, and SeaDronesSee. The proposed ZoomDet is architecture-independent and can be applied to an arbitrary object detection architecture. Remarkably, on the SeaDronesSee dataset, ZoomDet offers more than 8.4 absolute gain of mAP with a Faster R-CNN model, with only about 3 ms additional latency. The code is available at https://github.com/twangnh/zoomdet_code.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
