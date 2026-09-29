---
title: "yolo v8.4.142 Release Notes"
created: 2026-09-07
captured: 2026-09-07
type: release-note
tag: v8.4.142
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.142
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.142 Release Notes (2026-09-05)

## 🌟 Summary

**Ultralytics v8.4.142** unifies YOLO inference and export behavior under the `nms` option, making it easier to choose between maximum accuracy and NMS-free speed while improving benchmark consistency and deployment documentation.

## 📊 Key Changes

- 🔄 **Unified `end2end` into `nms`**
  - `nms=None` *(default)* uses the one-to-many head with Ultralytics-managed NMS.
  - `nms=True` uses the one-to-many head and embeds NMS in supported exports.
  - `nms=False` selects the one-to-one NMS-free head when available.
  - The legacy `end2end` argument is deprecated:
    - `end2end=True` maps to `nms=False`.
    - `end2end=False` maps to `nms=None`, unless explicitly combined with `nms=True`.
  - Both YOLO26 heads remain trained, while validation, checkpoint selection, and early stopping now follow the selected inference head.

- 📦 **Improved model fusion and export handling**
  - Model fusion now removes the unused detection branch regardless of which inference head is selected.
  - Exported models preserve their native output behavior, while unsupported formats automatically fall back to compatible raw outputs.
  - NMS options are now documented consistently across ONNX, TensorRT, CoreML, OpenVINO, MNN, Ascend, Hailo, and other integrations.

- 📏 **More reliable cross-format benchmarks**
  - Benchmark validation now uses square inputs consistently across native and exported models.
  - This ensures accuracy and latency comparisons are based on the same preprocessing rather than mixing rectangular and square inputs.

- 🐛 **Training resume fix**
  - Resuming training with Albumentations transforms no longer fails when saving arguments to YAML.
  - The fix addresses argument normalization order without changing the training workflow.

- 🌐 **Expanded deployment documentation**
  - Added a new guide for deploying Ultralytics models on Luxonis OAK RVC2 and RVC4 cameras.
  - Improved Ambarella CVflow deployment guidance, including SDK compilation, host validation, and Cavalry device deployment.
  - Documented reliable DEEPX SDK installation using the vendor wheel repository.

- 🧪 **Broader test coverage and maintenance**
  - Updated prediction, validation, export, Hailo, and model-head tests for the new `nms` behavior.
  - Package version updated to `8.4.142`.

## 🎯 Purpose & Impact

- ✅ **Simpler API:** One `nms` setting now controls head selection and export-time NMS across prediction, validation, tracking, benchmarking, and export.
- 🎯 **Better default accuracy:** YOLO26 now defaults to the one-to-many head with NMS, which generally provides higher accuracy than the NMS-free one-to-one head.
- ⚡ **Optional lower-latency deployment:** Use `nms=False` when you want NMS-free predictions and a simpler post-processing pipeline.
- 🔧 **Easier migration:** Existing `end2end` configurations continue to work through compatibility mapping, but new code should use `nms`.
- 📊 **Fairer performance comparisons:** Cross-format benchmark results are now more 
