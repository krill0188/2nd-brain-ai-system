---
title: "yolo v8.4.172 Release Notes"
created: 2026-10-04
captured: 2026-10-04
type: release-note
tag: v8.4.172
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.172
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.172 Release Notes (2026-10-03)

## 🌟 Summary
**v8.4.172 makes oriented-box cropping work as expected and improves reliability across model training, export, dataset handling, and deployment.**

## 📊 Key Changes
- **Rotation-aligned OBB crops:** `save_crop=True` and `ObjectCropper` now save crops upright and aligned to each oriented bounding box. Areas extending beyond the image are filled with black.
- **Model correctness fixes:** AIFI positional embeddings now match non-square feature maps, and RT-DETR computes matching costs in float32 to avoid AMP precision errors affecting training assignments.
- **More reliable training and resume:** NaN recovery now correctly restarts the recovered epoch, while resumed runs preserve the selected optimizer and early-stopping progress.
- **Improved dataset and export handling:** Corrupted dataset caches trigger a rescan; classification datasets recognize more supported image formats; and static INT8 exports can calibrate even when the dataset is smaller than the requested batch.
- **Broader Python support:** Python 3.14 is added to package support and several Docker and export environments. The Python export image remains on Python 3.13 for dependencies that do not yet support 3.14.
- **Platform documentation refreshed:** Docs now describe current Platform behavior and APIs, including Agents management, dataset version comparisons, and direct LabelMe imports.

## 🎯 Purpose & Impact
- OBB users can now get useful, tightly aligned crops instead of no crops or axis-aligned approximations.
- Training and validation should be more dependable, particularly when using AMP, recovering from NaNs, or resuming an interrupted run.
- Dataset and export workflows are more resilient to damaged caches, varied image formats, and small calibration datasets.
- Updated Python support and clearer Platform documentation make it easier to choose compatible environments and follow current workflows.

## What's Changed
* Fix NaN conv outputs in JetPack5 Docker image from OpenBLAS 0.3.8 by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26473
* Bump Prettier from 3.8.5 to 3.9.9 by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26472
* Remove `cloudpickle` and `filelock` base dependencies and disallow new ones by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26471
* Remove redundant Lost-state checks in ByteTrack and FastTracker second association by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26481
* Use pre-cached assets in COCO-eval and CLI solutions tests by @JaviChulvi in https://github.com/ultralytics/ultralytics/pull/26476
* Align validation, Edge TPU export, and Platform dataset, Agents API, and billing docs with current behavior by @raimbekovm in https://github.com/ultralytics/ultralytics/pull/26467
* Fix AIFI position embedding for non-square feature maps by @ArgoHA in https://github.com/ultralytics/ultralytics/pull/26483
* Align Ultralytics Platform docs with current Platform behavi
