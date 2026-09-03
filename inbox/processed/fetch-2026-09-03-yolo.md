---
title: "yolo v8.4.138 Release Notes"
created: 2026-09-03
captured: 2026-09-03
type: release-note
tag: v8.4.138
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.138
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.138 Release Notes (2026-09-01)

## 🌟 Summary

**Ultralytics v8.4.138** is a stability-focused release that restores compatibility with older checkpoints, fixes YOLO-World loading, and improves training, inference, tracking, tuning, and documentation reliability. 🛠️

## 📊 Key Changes

- **Legacy checkpoint loading fixed** 🎯  
  Restricted checkpoint loading now recognizes loss and assignment classes stored in checkpoints created before **8.4.95**, including detection, classification, pose, segmentation, rotated-box, and keypoint-related components.

- **YOLO-World loading fixed** 🌍  
  Corrects package loading issues affecting YOLO-World models and related checkpoints.

- **MuSGD with `channels_last` no longer crashes** ⚡  
  Replaces an incompatible tensor flattening operation with a layout-safe one, allowing CUDA training with the MuSGD optimizer and automatic `channels_last` support to run correctly.

- **SAM feature extraction optimized** 🧠  
  SAM, SAM2, and SAM3 image embeddings are computed in inference mode, preventing unnecessary autograd graphs from being retained and reducing memory overhead during repeated inference.

- **Distributed training made more robust** 🔧  
  - Prevents DDP failures when a mini-batch contains no assigned targets.  
  - Ensures detection, pose, OBB, and related model branches remain connected to the training graph even when there are no positive samples.

- **Tuning results corrected** 📈  
  Multi-dataset tuning now preserves dataset names and iteration order across distributed workers. Failed datasets are recorded with zero metrics instead of incomplete results, keeping tuning histories and fitness plots consistent.

- **Classification inference preprocessing improved** 🚀  
  More preprocessing work is moved to the inference device and performed in batches, which can reduce CPU overhead and improve classification throughput.

- **BoT-SORT tracking made faster** 🏃  
  Global motion compensation now caps corner detection at 400 points instead of 1,000, reducing optical-flow computation while retaining sufficient information for motion estimation.

- **Precision and quantization documentation clarified** 📚  
  Documentation now explains that `quantize` may select or request different runtime precisions depending on the export format. This avoids implying that every backend supports the same FP16, FP32, or INT8 behavior.

- **Documentation quality updates** ✨  
  Markdown tables were consistently formatted, the OBB navigation label was cleaned up, the TrackZone video was updated, and the YOLO26 CPU speed comparison now clearly identifies its YOLO26n-versus-YOLO11n ONNX baseline and hardware.

## 🎯 Purpose & Impact

- **More users can load existing models without retraining**, especially those using checkpoints created with older Ultralytics versions. ✅
- **YOLO-World workflows become more dependable** for users loading supported models and checkpoints.
- **Platform and cloud GPU training jobs are less likely to fail**, particularly MuSGD runs usi
