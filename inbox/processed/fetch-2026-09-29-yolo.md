---
title: "yolo v8.4.165 Release Notes"
created: 2026-09-29
captured: 2026-09-29
type: release-note
tag: v8.4.165
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.165
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.165 Release Notes (2026-09-28)

## 🌟 Summary
**v8.4.165 improves package compatibility, export and inference reliability, and dataset handling, with several targeted fixes for model outputs and vision workflows.**

## 📊 Key Changes
- 📦 **Cleaner Python wheel installation (current PR #26408):** Test files are no longer installed as a top-level `tests` package, avoiding conflicts with other projects. Tests remain in the source distribution so Conda builds can still run them.
- 🚀 **More reliable exports and inference:** ONNX export now checks that the requested opset is high enough for the model and reports a clear error if it is not. Windows OpenVINO inference also avoids a CPU instruction path that could crash on some machines.
- 📐 **Improved depth and semantic outputs:** Depth resizing now follows the same alignment convention used during training and validation. Saved semantic prediction masks are restored to the original image size without letterbox padding, and invalid semantic class IDs are flagged during dataset scanning.
- 🧹 **Safer, more consistent dataset processing:** Fixes cover whitespace-only labels, distinct segmentation polygons that share a bounding box, repeatable classification dataset splits, older Albumentations versions, and nested paths in COCO/LVIS conversion. Multispectral conversion now keeps source images if outputs collide or fail to write.
- 🎯 **More accurate vision utilities:** Corrected flips for left-top-width-height boxes, kept tracked pose keypoints colored by track ID, improved distance-calculation selection, and fixed class histories in analytics charts.
- 🛠️ **Documentation and CI updates:** Clarified Platform annotation and image-search guidance, corrected Ascend device mappings, and updated runner versions and test behavior.

## 🎯 Purpose & Impact
- ✅ **Fewer installation surprises:** The wheel no longer shadows other packages’ `tests` imports, while source-based Conda builds retain the tests they need.
- 🧪 **Clearer failure feedback and more dependable deployment:** Unsupported ONNX opsets fail early with an actionable message, and Windows OpenVINO is less prone to native crashes.
- 📊 **More trustworthy training and evaluation:** Dataset issues are caught earlier, repeated classification splits stay consistent, and saved semantic masks and depth outputs better match their intended image geometry.
- 🛡️ **Reduced risk of losing data:** Failed or colliding multispectral conversions no longer silently delete original images.

## What's Changed
* Fix Windows OpenVINO crashes and CI runtime warnings by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26317
* Update GitHub Actions runner to 2.337.0 in runner images by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26375
* Refresh AGENTS.md: stale docformatter claim and workflow guidance by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26381
* Treat unreadable paths as missing in check_file by @glenn-jocher in https://github.com/ultralytics/ultra
