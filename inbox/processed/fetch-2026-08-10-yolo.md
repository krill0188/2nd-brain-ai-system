---
title: "yolo v8.4.117 Release Notes"
created: 2026-08-10
captured: 2026-08-10
type: release-note
tag: v8.4.117
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.117
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.117 Release Notes (2026-08-09)

## 🌟 Summary

**v8.4.117 improves augmentation correctness, model reliability, deployment safety, and documentation across Ultralytics YOLO and YOLO26.** 🚀

## 📊 Key Changes

- 🧩 **Albumentations now handles spatial transforms by type**
  - PR #25633 replaces the fragile hardcoded transform-name list with recursive type detection, so wrapped transforms such as `OneOf` correctly update annotations.
  - Spatial augmentations now carry **bounding boxes, polygons, masks, depth maps, and keypoints** through the pipeline.
  - Background-only images receive pixel-level augmentations even when they have no annotations.
  - Keypoint flipping respects the configured `flip_idx` mapping.
  - Probability handling now makes a zero probability a reliable off switch.
  - Unsupported topology-changing transforms, such as grid shuffling with polygons or keypoints, are detected instead of silently corrupting labels.

- 🔐 **Improved security for dependency installation**
  - `check_requirements()` now prevents untrusted requirement strings from being interpreted as shell commands.
  - This protects workflows that automatically install missing dependencies while loading model files.

- 🛡️ **More reliable dataset and mask processing**
  - Fixed Windows semantic-mask shape handling so grayscale masks remain two-dimensional and semantic training no longer fails during Mosaic augmentation.
  - COCO conversion now keeps one consistent label format per file, warns about unusable polygons, and falls back to box-shaped polygons when necessary.
  - Mixed detection and segmentation rows are rejected instead of being silently misread.
  - Grounding dataset caching and validation were improved, including clearer errors for empty or invalid annotation sets.
  - Degenerate polygon contours are skipped when exporting labels.

- 🧠 **Depth estimation improvements**
  - Depth postprocessing now aligns PyTorch, Hailo, and exported-model outputs before removing padding, producing more consistent results across inference backends.
  - Depth validation no longer inherits rectangular batching behavior that conflicts with its intentional square stretching.
  - The KITTI depth configuration now uses the canonical 652-frame left-camera evaluation split, avoiding test-set overlap and making reported results more reproducible.
  - Depth metrics and documentation were updated to reflect per-image evaluation behavior.

- ⚡ **Faster and more consistent inference**
  - YOLO26 end-to-end postprocessing uses grouped top-k selection, improving TensorRT FP16 latency by approximately **1.8% to 8.1%** without changing mAP.
  - RT-DETR FLOPs profiling is faster and now supports attention-based decoder architectures correctly.
  - SavedModel INT8 calibration avoids an unnecessary NumPy copy.
  - GMC tracking now handles textureless frames and incomplete feature matches without stopping, allowing tracking to recover cleanly.
  - SAM3 video masks use the model’s configured threshold consistently instead of a
