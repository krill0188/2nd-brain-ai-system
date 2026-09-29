---
title: "yolo v8.4.161 Release Notes"
created: 2026-09-24
captured: 2026-09-24
type: release-note
tag: v8.4.161
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.161
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.161 Release Notes (2026-09-23)

## 🌟 Summary
**Ultralytics 8.4.161 is a reliability and usability release:** it fixes several training, inference, plotting, and upload bugs, while improving dataset handling and clarifying export and Platform documentation.

## 📊 Key Changes
- 🛠️ **Fixed six package issues in PR #26301**, the release’s main change:
  - RT-DETR decoder tensors now move correctly between devices, helping prevent validation or prediction device-mismatch errors.
  - Resuming older Adam/AdamW checkpoints now preserves the optimizer’s runtime fused setting.
  - Empty image files no longer crash prediction runs.
  - Training results can be read from paths containing bracket characters, and plots handle odd numbers of result panels correctly.
  - Platform uploads can fall back to `last.pt` when `save=False` means no `best.pt` was created.
- 🗂️ **Improved dataset and training utilities:** `.tgz` archives now extract correctly, semantic segmentation can skip unnecessary polygon processing, and fuzz testing better recognizes expected missing-split errors.
- 🍎 **Made CoreML export failures clearer:** removed an invalid fallback that could hide the original save error behind a misleading file-extension error.
- 📘 **Expanded export guidance:** documented the `device` option for Hailo and Ascend, and explained why static exports may produce different predictions on non-square images.
- ☁️ **Refreshed Platform documentation** for dataset image copying and face blurring, annotation providers, deployment pages and monitoring, and related API and billing details.

## 🎯 Purpose & Impact
- ✅ More dependable prediction and training-resume workflows, especially with RT-DETR, older checkpoints, and imperfect image datasets.
- 📈 Fewer failures when reading results or generating plots, including with unusual file paths and uneven metric layouts.
- ⚡ Less unnecessary processing for semantic datasets where polygon data is not used.
- 🔍 More actionable CoreML errors and clearer export settings help users diagnose problems and choose deployment options.
- 🧭 Updated Platform guidance makes dataset, annotation, billing, and deployment workflows easier to understand.

## What's Changed
* Document `device` export argument for OpenVINO, Hailo and Ascend by @raimbekovm in https://github.com/ultralytics/ultralytics/pull/26286
* Tighten export mode docs and explain static export prediction differences by @Vaishnavi220506 in https://github.com/ultralytics/ultralytics/pull/26285
* Align Platform docs with deployment pages, image copy, face blurring and new annotation providers by @raimbekovm in https://github.com/ultralytics/ultralytics/pull/26297
* Classify wrapped dataset split errors as expected in CLI fuzzing by @aswanth-07 in https://github.com/ultralytics/ultralytics/pull/26299
* Remove invalid CoreML .mlmodel save fallback by @amanharshx in https://github.com/ultralytics/ultralytics/pull/26298
* Fix extraction of .tgz dataset archives by @aswanth-07 in https://github.com/ultralytics/ultralytics
