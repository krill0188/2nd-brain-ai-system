---
title: "yolo v8.4.155 Release Notes"
created: 2026-09-18
captured: 2026-09-18
type: release-note
tag: v8.4.155
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.155
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.155 Release Notes (2026-09-17)

## 🌟 Summary

**Ultralytics 8.4.155 improves dataset-cache safety, export reliability, training validation, and platform compatibility—helping YOLO26 workflows fail less often and provide clearer feedback.** 🚀

## 📊 Key Changes

- **🧹 Prevented stale `labels.cache` reuse after dataset configuration changes** *(PR #26207, the primary release change)*  
  Dataset cache validation now includes important scan settings such as:
  - Number of classes
  - Keypoint configuration
  - Detection versus pose usage
  - Single-class mode  
  This ensures changes to `data.yaml` trigger a fresh label scan instead of reusing incompatible cached labels.

- **⛔ Invalid epoch values are now rejected early**  
  Training configurations with `epochs=0` or negative values now raise a validation error instead of silently running 100 epochs or producing invalid training outputs.

- **🖥️ Improved Windows OpenVINO inference**  
  Windows CPU inference now explicitly requests FP32 precision to avoid reduced-precision kernel failures on affected systems.

- **📦 Better control over automatic dependency installation**  
  Setting `YOLO_AUTOINSTALL=False` now also prevents automatic `apt` installations and Edge TPU compiler setup. Missing dependencies produce a warning or actionable error instead of modifying the environment unexpectedly.

- **📱 Fixed YOLO26 pose training on Apple MPS**  
  The RLE pose-loss weights now use the correct `float32` type, allowing YOLO26 pose training to run on MPS devices.

- **⚡ Faster font checking**  
  Font lookup uses Matplotlib’s cached font list before rescanning the operating system, significantly reducing startup time on systems such as macOS.

- **📤 Improved export and inference paths**
  - LiteRT conversion now explicitly uses evaluation mode.
  - MNN examples no longer clamp pixel-coordinate boxes to `[0, 1]`, fixing collapsed bounding boxes and producing correct detections.
  - OBB angle data is passed directly during decoding, avoiding unnecessary model attributes and export warnings.

- **🔧 Updated distributed training compatibility**  
  DDP now uses the appropriate buffer-synchronization option for newer PyTorch versions, reducing deprecation warnings while preserving behavior.

- **☁️ Updated Platform SDK documentation**  
  Documentation now recommends `ultralytics-platform>=0.1.45` and explains how training metrics, checkpoints, arguments, and host information synchronize with the Ultralytics Platform.

- **🌐 Expanded repository mirroring infrastructure**  
  A scheduled workflow now mirrors public Ultralytics repositories to GitLab daily, including branches, tags, Git LFS objects, metadata, and repository avatars.

- **📚 Refreshed heatmaps documentation**  
  The heatmaps guide now features an updated YOLO26 tutorial video.

## 🎯 Purpose & Impact

- **More reliable dataset changes:** Users can safely modify class counts, keypoint settings, or task configuration without unknowingly training from incompatible cached labels. Erro
