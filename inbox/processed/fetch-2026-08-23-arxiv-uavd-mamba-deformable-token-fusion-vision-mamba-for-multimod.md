---
title: "UAVD-Mamba: Deformable Token Fusion Vision Mamba for Multimodal UAV Detection"
created: 2026-08-23
captured: 2026-08-23
type: paper
domain: ai-autonomy
source: http://arxiv.org/abs/2507.00849v1
authors: "Wei Li, Jiaman Tang, Yang Li, Beihao Xia, Ligang Tan, Hongmao Qin"
published: "2025-07-01"
tags: [drone, ai-autonomy, paper, arxiv]
---

# UAVD-Mamba: Deformable Token Fusion Vision Mamba for Multimodal UAV Detection

**Authors**: Wei Li, Jiaman Tang, Yang Li, Beihao Xia, Ligang Tan, Hongmao Qin
**Published**: 2025-07-01
**arXiv**: http://arxiv.org/abs/2507.00849v1

## Abstract

Unmanned Aerial Vehicle (UAV) object detection has been widely used in traffic management, agriculture, emergency rescue, etc. However, it faces significant challenges, including occlusions, small object sizes, and irregular shapes. These challenges highlight the necessity for a robust and efficient multimodal UAV object detection method. Mamba has demonstrated considerable potential in multimodal image fusion. Leveraging this, we propose UAVD-Mamba, a multimodal UAV object detection framework based on Mamba architectures. To improve geometric adaptability, we propose the Deformable Token Mamba Block (DTMB) to generate deformable tokens by incorporating adaptive patches from deformable convolutions alongside normal patches from normal convolutions, which serve as the inputs to the Mamba Block. To optimize the multimodal feature complementarity, we design two separate DTMBs for the RGB and infrared (IR) modalities, with the outputs from both DTMBs integrated into the Mamba Block for feature extraction and into the Fusion Mamba Block for feature fusion. Additionally, to improve multiscale object detection, especially for small objects, we stack four DTMBs at different scales to produce multiscale feature representations, which are then sent to the Detection Neck for Mamba (DNM). The DNM module, inspired by the YOLO series, includes modifications to the SPPF and C3K2 of YOLOv11 to better handle the multiscale features. In particular, we employ cross-enhanced spatial attention before the DTMB and cross-channel attention after the Fusion Mamba Block to extract more discriminative features. Experimental results on the DroneVehicle dataset show that our method outperforms the baseline OAFA method by 3.6% in the mAP metric. Codes will be released at https://github.com/GreatPlum-hnu/UAVD-Mamba.git.
