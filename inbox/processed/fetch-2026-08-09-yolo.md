---
title: "yolo v8.4.116 Release Notes"
created: 2026-08-09
captured: 2026-08-09
type: release-note
tag: v8.4.116
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.116
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.116 Release Notes (2026-08-07)

## 🌟 Summary

🚀 **v8.4.116** improves installation reliability, expands YOLOE and Platform workflows, strengthens tracking and export support, and refreshes YOLO26 documentation.

## 📊 Key Changes

- **🔧 OpenCV compatibility fix — current PR #25702 by @Y-T-G**
  - Raises the minimum `opencv-python` version from `4.6.0` to `4.7.0`.
  - Keeps the exclusion for `4.13.0.90`, which is affected by a FIPS self-test crash.
  - Removes an outdated ONNX DNN backend requirement check.
  - This aligns the dependency with `cv2.imdecodemulti`, which Ultralytics uses internally.

- **🧠 Reusable YOLOE prompt embeddings**
  - Adds `save_prompt_embeddings()` and `load_prompt_embeddings()` for storing text or visual prompt configurations in NPZ files.
  - Profiles are validated against the source YOLOE model and can be reused before exporting to formats such as ONNX, OpenVINO, TensorRT, CoreML, LiteRT, and RKNN.
  - Exported models remain standard single-input models and do not require the NPZ file at runtime.

- **📚 Improved model guidance**
  - Reworks the model index into a task-and-mode comparison table.
  - Positions **[YOLO26](https://docs.ultralytics.com/models/yolo26/)** as the recommended model for new projects, with YOLO11 as a mature production alternative.
  - Clarifies support for YOLO12, OBB, SAM models, YOLOE, YOLO-World, RT-DETR, and other model families.
  - Adds a YOLO26 custom-dataset training video and highlights monocular depth estimation.

- **🎯 Broader and safer tracking support**
  - Documents and supports OBB tracking alongside detection, segmentation, and pose.
  - Rejects unsupported semantic and depth tracking tasks with a clear error before processing begins.
  - Skips unnecessary camera-motion compensation work when `gmc_method: none`.
  - Keeps OC-SORT observation history bounded on all track lifecycle paths.

- **📦 More efficient model export**
  - Streams ONNX and QNN calibration data instead of retaining all transformed images in memory.
  - Reduces calibration memory usage substantially for large datasets.
  - Updates anchor creation to use CoreML-friendly tensor operations, improving dynamic CoreML export compatibility.

- **🧪 Depth and segmentation fixes**
  - Excludes ground-truth depth values outside the configured valid range during calibration, keeping calibration consistent with validation metrics.
  - Fixes FP16 segmentation with class-agnostic NMS.
  - Preserves YOLOE one-to-one classifier weights during linear probing, preventing a severe accuracy drop.
  - Makes pose activation-map gradients compatible with autograd and `torch.compile`.

- **🖼️ Visualization and analytics improvements**
  - Restores percentage labels in analytics pie charts.
  - Speeds up semantic-mask overlay rendering by replacing repeated full-image scans with a palette lookup.

- **☁️ Expanded Ultralytics Platform workflows**
  - Adds documented custom metadata support for datasets, images, projects, and models.
  - Supports nested metadata, metadat
