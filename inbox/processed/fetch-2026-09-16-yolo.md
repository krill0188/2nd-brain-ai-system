---
title: "yolo v8.4.153 Release Notes"
created: 2026-09-16
captured: 2026-09-16
type: release-note
tag: v8.4.153
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.153
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.153 Release Notes (2026-09-15)

## 🌟 Summary

**Ultralytics 8.4.153** delivers a critical SAM3 initialization fix, improves validation reliability, clarifies INT8 export behavior, and expands Ultralytics Platform documentation and annotation capabilities. 🚀

## 📊 Key Changes

- **🛠️ Fixed SAM3 `compile=False` handling — PR #26189 by @glenn-jocher**
  - Converts the predictor option correctly before passing it to the SAM3 builder:
    - `False` disables compilation.
    - `True` enables the default compilation mode.
    - Explicit compilation mode strings are preserved.
  - Prevents unintended `torch.compile` activation and the resulting PyTorch 2.14 Dynamo error during SAM3 initialization.
  - Validated across all six Platform SAM models for HTTP and WebSocket inference.
  - Package version bumped to **8.4.153**.

- **✅ Improved standalone semantic segmentation validation**
  - Polygon-based semantic datasets now receive their background class metadata during dataset construction.
  - Prevents background pixels from being incorrectly assigned to the final real class.
  - Makes standalone validation metrics such as mIoU and pixel accuracy meaningful again.

- **🖼️ Fixed standalone classification validation with extra classes**
  - Validation now filters samples whose class IDs are outside the model’s class range, matching existing training behavior.
  - Prevents `IndexError` crashes when the validation dataset contains more classes than the checkpoint supports.
  - Clear warnings identify skipped samples and mismatched classes.

- **🔄 Preserved explicit datasets when resuming training**
  - `train(resume=True, data="...")` now correctly honors the user-provided dataset instead of silently using the checkpoint’s original dataset.
  - Path-based resumes also avoid injecting an unintended task-default dataset.

- **⚙️ Improved INT8 export behavior and documentation**
  - Quantization-aware training checkpoints can export their stored INT8 ranges without calibration data for ONNX and TensorRT.
  - RKNN INT8 validation now correctly applies to detection models only, including INT8-only Rockchip targets.
  - RKNN examples now use a compatible detection model and dataset.
  - TensorRT documentation no longer claims that `dynamic` is automatically enabled for INT8 exports.

- **🎯 Preserved `conf=0.0` during IMX export**
  - An explicit zero confidence threshold is no longer replaced with `0.001`.
  - Added coverage for both `conf=0.0` and the default `conf=0.25` behavior.

- **🧩 Expanded Platform annotation and billing documentation**
  - Added documentation for dataset-wide batch annotation, class mapping, progress tracking, stopping runs, version snapshots, and billing.
  - YOLO smart annotation now includes pose datasets, while SAM remains available for detection, segmentation, semantic, and OBB tasks.
  - Documented the Platform referrals tab, endpoint uptime charges, batch annotation pricing, supported dataset licenses, and Python 3.11 requirement.
  - Agents documentation now refl
