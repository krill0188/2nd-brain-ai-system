---
title: "UAVD-Mamba: Deformable Token Fusion Vision Mamba for Multimodal UAV Detection"
created: 2026-09-01
updated: 2026-09-01
type: paper
item_type: preprint
authors: "Li, Wei; Tang, Jiaman; Li, Yang; Xia, Beihao; Tan, Ligang; Qin, Hongmao"
year: "2025"
doi: "10.48550/arXiv.2507.00849"
url: "http://arxiv.org/abs/2507.00849v1"
zotero_key: W6E9RPVJ
tags: ["auto:2nd-brain"]
attachment_path: raw/papers/files/drone-ai/uavd-mamba-deformable-token-fusion-vision-mamba-for-multimodal-uav-detection.pdf
attachment_sha256: 746fa577d24d7c11616f5057bc00df80a7d8dcbc520eefd2ef7082cf0500195f
sha256: f69ba1a90d82d00b
---

# UAVD-Mamba: Deformable Token Fusion Vision Mamba for Multimodal UAV Detection

**Authors**: Li, Wei; Tang, Jiaman; Li, Yang; Xia, Beihao; Tan, Ligang; Qin, Hongmao  
**Year**: 2025  
**DOI**: 10.48550/arXiv.2507.00849  
**URL**: http://arxiv.org/abs/2507.00849v1

## Abstract

Unmanned Aerial Vehicle (UAV) object detection has been widely used in traffic management, agriculture, emergency rescue, etc. However, it faces significant challenges, including occlusions, small object sizes, and irregular shapes. These challenges highlight the necessity for a robust and efficient multimodal UAV object detection method. Mamba has demonstrated considerable potential in multimodal image fusion. Leveraging this, we propose UAVD-Mamba, a multimodal UAV object detection framework based on Mamba architectures. To improve geometric adaptability, we propose the Deformable Token Mamba Block (DTMB) to generate deformable tokens by incorporating adaptive patches from deformable convolutions alongside normal patches from normal convolutions, which serve as the inputs to the Mamba Block. To optimize the multimodal feature complementarity, we design two separate DTMBs for the RGB and infrared (IR) modalities, with the outputs from both DTMBs integrated into the Mamba Block for feature extraction and into the Fusion Mamba Block for feature fusion. Additionally, to improve multiscale object detection, especially for small objects, we stack four DTMBs at different scales to produce multiscale feature representations, which are then sent to the Detection Neck for Mamba (DNM). The DNM module, inspired by the YOLO series, includes modifications to the SPPF and C3K2 of YOLOv11 to better handle the multiscale features. In particular, we employ cross-enhanced spatial attention before the DTMB and cross-channel attention after the Fusion Mamba Block to extract more discriminative features. Experimental results on the DroneVehicle dataset show that our method outperforms the baseline OAFA method by 3.6% in the mAP metric. Codes will be released at https://github.com/GreatPlum-hnu/UAVD-Mamba.git.

## Notes

<!-- 여기에 핵심 인사이트, 메모, 인용문을 추가하세요 -->
