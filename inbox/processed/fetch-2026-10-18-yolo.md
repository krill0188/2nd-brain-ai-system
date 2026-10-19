---
title: "yolo v8.4.181 Release Notes"
created: 2026-10-18
captured: 2026-10-18
type: release-note
tag: v8.4.181
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.181
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.181 Release Notes (2026-10-17)

## 🌟 Summary
Version 8.4.181 focuses on making dataset loading, annotation, tracking, and inference more reliable, with several performance and compatibility improvements. No model architecture changes are included.

## 📊 Key Changes
- **Fixed data-pipeline edge cases:** Dataset discovery now prioritizes `.yaml` files before `.yml` files, preventing unrelated YAML files from breaking dataset loading. `.txt` and `.csv` prediction-source lists work regardless of filename capitalization, and dataset hashing now supports filenames with non-UTF-8 characters.
- **Improved automatic annotation:** `auto_annotate` now names label files using the detector’s prediction output path, helping keep labels matched to images with the same filename stem.
- **Made rotated-box tracking steadier:** Tracked object angles now stay consistent between frames instead of unexpectedly flipping, making angle-based tracking output easier to use.
- **Reduced segmentation memory overhead:** Native mask processing writes results into a preallocated output stack, avoiding extra full-size copies. A related filtering change also avoids repeated GPU-to-CPU synchronization.
- **Fixed small-image depth output:** Depth maps for one-row, one-column, and 1×1 images now retain their expected two-dimensional shape.
- **Improved training metrics on shared GPU hosts:** Platform system metrics report the GPUs used by the training run, rather than including unrelated GPUs on the same machine.
- **Updated compatibility checks and guidance:** PyTorch–Torchvision checks cover newer releases, JetPack detection includes JetPack 7.2, and TensorRT 11 DLA limitations are clarified. CI also tests newer Python versions with recent PyTorch releases.
- **KPTTracker is not part of this release:** Its earlier addition was reverted.

## 🎯 Purpose & Impact
- Dataset setup and prediction workflows should fail less often on common filename and file-format edge cases.
- Tracking, depth prediction, and segmentation results are more consistent, including for unusual image sizes and rotated objects.
- Segmentation may use less temporary memory, while Platform GPU charts more accurately reflect each run.
- Updated compatibility checks and documentation should make it easier to identify supported software and hardware combinations.

## What's Changed
* Refresh stale version lookups: torchvision pairing, JetPack 7.2, TensorRT 11 DLA by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26728
* Simplify is_jetson JetPack lookup and run each SlowTests torch shard on its newest Python by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26733
* Report only the training run's GPUs in Platform system metrics by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26734
* Add KPTTracker: keypoint-based tracking for Pose models by @FelixTx in https://github.com/ultralytics/ultralytics/pull/26530
* Revert "Add KPTTracker: keypoint-based tracking for Pose models (#26530)" by @glenn-joch
