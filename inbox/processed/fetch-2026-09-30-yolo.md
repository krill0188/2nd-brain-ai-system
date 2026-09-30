---
title: "yolo v8.4.166 Release Notes"
created: 2026-09-30
captured: 2026-09-30
type: release-note
tag: v8.4.166
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.166
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.166 Release Notes (2026-09-29)

## 🌟 Summary
**Ultralytics 8.4.166 focuses on more reliable dataset handling and prediction outputs, alongside updated Platform and inference documentation.** No model architecture changes are included.

## 📊 Key Changes
- 🗂️ **Semantic masks and dataset conversion:** The release preserves class IDs in Pascal VOC-style palette PNG masks and retains pixel values from 16-bit masks. It also rebuilds older semantic-mask caches and includes LVIS images even when they have no annotations.
- 🎯 **More accurate segmentation outputs:** Fixes prevent resized instance masks from shrinking during validation and preserve the correct letterbox crop when saving semantic predictions.
- 🧰 **Dataset and training reliability:** Fixes address stale disk-cached images, relative directories and globs in prediction source lists, outdated classification split copies, and unsafe small-image training configurations.
- 🖼️ **Image and video handling:** Annotation visualization and image compression now account for EXIF orientation, and saved videos retain the expected duration when frames are skipped.
- 📚 **Documentation updates:** Inference guidance now reflects Rust inference 0.0.50, including device selection, video requirements, GPU preprocessing, and RT-DETR support. Platform docs also describe current annotation, dataset, inference, and deployment behavior.

## 🎯 Purpose & Impact
- ✅ **Better compatibility with real-world datasets:** Palette-based and 16-bit masks are less likely to be rejected or interpreted with incorrect class IDs.
- 📐 **More trustworthy segmentation results:** Validation masks and saved predictions better match the original image dimensions and content.
- 🛠️ **Fewer confusing failures:** Dataset loading, training checks, and prediction inputs behave more consistently, catching some issues earlier.
- 📖 **Clearer guidance for users:** Updated docs help users understand current Platform features and inference defaults, including the [Ultralytics Platform](https://platform.ultralytics.com).

## What's Changed
* Docs: document Platform image generation, similarity, and face blurring by @JaviChulvi in https://github.com/ultralytics/ultralytics/pull/26411
* Align Rust inference docs with ultralytics-inference 0.0.50 by @raimbekovm in https://github.com/ultralytics/ultralytics/pull/26431
* Sync platform docs and screenshots with annotation, inference, and deployment changes by @raimbekovm in https://github.com/ultralytics/ultralytics/pull/26419
* Classify unsupported onnx opset rejections as expected in fuzzing by @raimbekovm in https://github.com/ultralytics/ultralytics/pull/26430
* Include the multi_scale minimum size in the final batch=1 training check by @raimbekovm in https://github.com/ultralytics/ultralytics/pull/26429
* Clarify optimizer=auto learning rate behavior by @zkoymen in https://github.com/ultralytics/ultralytics/pull/26435
* Respect cache mode when loading existing .npy images by @aswanth-07 in https://github.com/ultralytics/ultralytics/p
