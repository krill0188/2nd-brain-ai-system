---
title: "yolo v8.4.143 Release Notes"
created: 2026-09-08
captured: 2026-09-08
type: release-note
tag: v8.4.143
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.143
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.143 Release Notes (2026-09-07)

## 🌟 Summary

**v8.4.143 introduces INT8 quantization-aware training for YOLO26, improves deployment and evaluation workflows, and delivers a broad documentation and integration refresh.** 🚀

## 📊 Key Changes

- **🧠 INT8 quantization-aware training (QAT) — PR #26083**
  - Adds support for `quantize=8` during `train` mode.
  - Fine-tunes pretrained weights while simulating INT8 quantization, allowing the model to adapt before deployment rather than being quantized only after training.
  - Stores calibrated quantization ranges in the checkpoint and supports direct export to ONNX and TensorRT with Q/DQ nodes—without requiring calibration data during export.
  - Reuses the existing `quantize` argument and adds no new public API or dependency.
  - Particularly useful for deploying YOLO26 models to resource-constrained edge hardware.

- **📈 More complete validation metrics — PR #24489**
  - Adds per-class AP75 values to validation summaries, DataFrame outputs, CSV files, and JSON exports.
  - Applies consistently to detection, segmentation, pose, and OBB tasks.

- **🚀 Improved YOLO26 deployment workflows**
  - DeepStream documentation now uses the native Ultralytics exporter instead of a separate third-party script.
  - Clarifies when to use the NMS-free head with `nms=False` and updates Triton, DALI, SAM, and C++ examples accordingly.
  - Adds documentation for Apple’s Core AI export target and backend.
  - Corrects quantization guidance for formats that support only specific precisions.

- **🛠️ Training and model lifecycle fixes**
  - Corrects pretrained-model handling after `reset_weights()`, during resume operations, and in multi-dataset or distributed training.
  - Preserves Platform model URIs when training through Python.
  - Keeps prediction output directories when copying or converting `Results` objects.
  - Removes stale SAM3 decoder coordinate caches, improving reliability across device and precision changes.

- **🌍 Platform and authentication updates**
  - Uses the Ultralytics Platform SDK for login, model downloads, dataset exports, and training resource access.
  - Aligns Python 3.11+ installations with the shared-login SDK requirements while preserving local workflows on older Python versions.

- **📚 Extensive documentation improvements**
  - Reviews and corrects examples, CLI syntax, export details, tracker behavior, dataset layouts, image decoding, hardware integrations, and model descriptions.
  - Expands YOLO26 depth-estimation dataset documentation with new FAQs and dataset guidance.
  - Updates Ultralytics Platform links across dataset and training pages.
  - Documents improved Albumentations support for boxes, polygons, keypoints, depth maps, and semantic masks.
  - Refreshes DeepStream, OpenVINO, Core AI, Edge TPU, Ray Tune, Jetson, and other integration guides.

## 🎯 Purpose & Impact

- **⚡ Better edge performance:** QAT can help INT8-deployed models retain more accuracy while benefiting from lower memory usage, faster inference
