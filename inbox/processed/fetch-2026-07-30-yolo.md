---
title: "yolo v8.4.112 Release Notes"
created: 2026-07-30
captured: 2026-07-30
type: release-note
tag: v8.4.112
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.112
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.112 Release Notes (2026-07-29)

## 🌟 Summary

Release `v8.4.112` makes model export support much clearer and more reliable, with comprehensive task documentation across formats and a fix enabling DEEPX classification exports. 📦✅

## 📊 Key Changes

- **Documented supported tasks for every export format** 📚
  - Added consistent **Supported Tasks** tables to 20 integration pages.
  - Clearly lists support for all seven Ultralytics tasks:
    - Object detection
    - Instance segmentation
    - Semantic segmentation
    - Pose estimation
    - OBB detection
    - Classification
    - Depth estimation
  - Documents model-family limitations, such as semantic segmentation and depth estimation being YOLO26-only for many formats.
  - Explicitly identifies unsupported combinations, including:
    - Axelera depth estimation
    - Hailo YOLO26 instance segmentation, pose, and OBB
    - Sony IMX500 semantic segmentation, OBB, and depth estimation

- **Verified export coverage across formats** 🔍
  - Completed 77 local export and inference checks across seven tasks.
  - Coverage was verified for TorchScript, ONNX, OpenVINO, CoreML, TensorFlow formats, PaddlePaddle, MNN, NCNN, ExecuTorch, and LiteRT.
  - TensorRT and RKNN support was confirmed through existing CI test matrices.

- **Fixed DEEPX classification export** 🛠️
  - Corrected calibration dataset discovery for classification models.
  - Classification datasets store their image directory as `root`, rather than `img_path`; the exporter now handles this correctly.
  - Updated DEEPX smoke tests to cover every task-specific default model instead of only YOLO26 detection.

- **Removed outdated GraphDef benchmark restrictions** ⚡
  - TensorFlow GraphDef benchmarks no longer reject OBB or pose models based on obsolete limitations.

- **Minor documentation and release updates** ✨
  - Updated the package version to `8.4.112`.
  - Improved wording around Huawei Ascend, TensorFlow GraphDef, NCNN, RKNN, and Hailo support.
  - Clarified that Edge TPU task support may still involve CPU execution for unsupported operations.

## 🎯 Purpose & Impact

- **Easier format selection:** Users can now quickly determine whether their task and model family are compatible with a target export format. 🧭
- **Fewer failed deployments:** Explicit support tables reduce confusion caused by previously undocumented or implied limitations.
- **Improved classification deployment:** DEEPX users can now export classification models successfully, including through automated smoke testing.
- **Better confidence in task support:** Broad empirical validation helps ensure documentation reflects actual export and inference behavior.
- **More accurate benchmarking:** Removing outdated GraphDef checks allows supported OBB and pose workflows to be benchmarked properly.
- **Important practical note:** A task marked as supported does not always mean the entire model runs on the accelerator; formats such as Edge TPU may execute some operations on the CPU.

## What's Changed
* Document s
