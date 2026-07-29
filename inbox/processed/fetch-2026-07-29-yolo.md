---
title: "yolo v8.4.110 Release Notes"
created: 2026-07-29
captured: 2026-07-29
type: release-note
tag: v8.4.110
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.110
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.110 Release Notes (2026-07-29)

## 🌟 Summary

🚀 Version **8.4.110** expands RKNN export to every supported YOLO task and improves GPU-friendly tensor image plotting, making Rockchip deployment more versatile and visualization more efficient.

## 📊 Key Changes

- **Expanded RKNN export support** by @glenn-jocher:
  - RKNN models can now be exported for:
    - Object detection
    - Instance segmentation
    - Classification
    - Pose estimation
    - Oriented bounding boxes (OBB)
    - Semantic segmentation
    - Depth estimation
  - Export smoke tests now cover all current task models using `rknn-toolkit2`.
  - Documentation and export tables now show task-specific model names and artifacts.
  - Package version bumped to **8.4.110**.

- **More efficient tensor-based plotting**:
  - `Results.plot()` and `Annotator` now accept contiguous HWC BGR `torch.Tensor` images.
  - Tensor images can remain on their original device during mask compositing, avoiding unnecessary CPU transfers.
  - Conversion to NumPy is delayed until required by OpenCV, PIL, display, saving, or the returned result.

- **Documentation improvements**:
  - Corrected “setup” to “set up” in the DeepSparse tutorial.
  - Updated plotting API documentation to include tensor image support.
  - Added task-specific export configuration to classification, depth, OBB, pose, segmentation, and semantic segmentation pages.

## 🎯 Purpose & Impact

- **Broader Rockchip NPU deployment** 📱: Users can deploy more types of YOLO26 models on RKNN-compatible Rockchip hardware, rather than being limited to detection models.
- **Simpler export workflows** 🛠️: Task-specific documentation and artifact names make it clearer which model to export and how to use the resulting RKNN file.
- **Improved visualization performance** ⚡: GPU-backed tensor images can avoid an unnecessary image copy to the host during mask plotting, which may improve performance for accelerated pipelines.
- **Better reliability** ✅: Expanded validation confirms RKNN conversion and basic inference coverage across all seven supported tasks.
- **No major behavior changes for existing users**: NumPy image workflows remain supported, while tensor-based workflows gain improved device efficiency.

## What's Changed
* Keep tensor images on-device during mask plotting by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/25487
* Fix grammar in DeepSparse tutorial by @gizembm in https://github.com/ultralytics/ultralytics/pull/25488
* Expand RKNN export support to all tasks by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/25490

## New Contributors
* @gizembm made their first contribution in https://github.com/ultralytics/ultralytics/pull/25488

**Full Changelog**: https://github.com/ultralytics/ultralytics/compare/v8.4.109...v8.4.110
