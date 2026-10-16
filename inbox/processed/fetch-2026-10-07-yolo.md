---
title: "yolo v8.4.174 Release Notes"
created: 2026-10-07
captured: 2026-10-07
type: release-note
tag: v8.4.174
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.174
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.174 Release Notes (2026-10-06)

## 🌟 Summary
Release **8.4.174** fixes AutoBatch’s backward-pass profiling for YOLO26 and speeds up prediction summaries, alongside improvements to exports, inference, tracking, and data handling.

## 📊 Key Changes
- **AutoBatch profiling — the main change:** The profiler now finds tensors inside nested model outputs, so backward profiling works with YOLO26 detection heads and other task heads. Prediction summaries also avoid unnecessary tensor conversions, making their logs faster.
- **More reliable inference and exports:** Dynamic CoreML models can handle batches larger than their exported batch size by processing them in chunks. Hailo INT8 optimization now receives reusable calibration images, fixing calibration methods that need to revisit the data.
- **Correct edge-case behavior:** Fast-NMS now keeps detections when the IoU threshold is zero. Tracking hides unconfirmed tracks when appropriate without dropping first-frame detections. INT8 calibration warnings are limited to export formats that support calibration data.
- **Improved data handling:** Dataset splitting preserves the caller’s random state, DOTA splitting accepts images without label files, and image loading and shape calculations better handle EXIF rotations and Unicode paths. Saved crops also retain dotted source names.
- **More dependable model setup:** Predictors and trackers are rebuilt when relevant setup arguments change; model-format detection handles compound filenames more reliably. YouTube inputs no longer require a stream of at least 1080p.
- **Documentation and packaging updates:** Guides cover per-object depth estimates and newer Platform workflows, including image search and live-camera inference. Docker images can cache Python bytecode, while CI and Conda guidance were updated for more compatible dependency resolution.

## 🎯 Purpose & Impact
- **AutoBatch can now measure YOLO26 training memory more accurately.** Because backward profiling runs successfully, automatic batch-size selections may change; fixed-batch training and prediction are unaffected.
- **Exported models are more practical across deployment targets.** CoreML handles larger prediction batches, and Hailo calibration methods that revisit their input data can work as intended.
- **Predictions and datasets are more consistent in edge cases,** reducing unexpected missing detections, failed dataset splits, or crop files that are hard to match to their sources.
- **No model architecture, checkpoint, or default changes are introduced.**

## What's Changed
* Fix misleading INT8 calibration warning for CoreML and MNN by @amanharshx in https://github.com/ultralytics/ultralytics/pull/26528
* Fix zero-threshold OBB suppression in Fast-NMS by @aswanth-07 in https://github.com/ultralytics/ultralytics/pull/26522
* Fix model.track leaking unconfirmed detections when no tracks are active by @wizzseen in https://github.com/ultralytics/ultralytics/pull/26525
* Keep dotted image and video names in `save_crop` file names
