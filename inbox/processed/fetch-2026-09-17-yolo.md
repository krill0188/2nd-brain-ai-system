---
title: "yolo v8.4.154 Release Notes"
created: 2026-09-17
captured: 2026-09-17
type: release-note
tag: v8.4.154
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.154
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.154 Release Notes (2026-09-16)

## 🌟 Summary

**v8.4.154 improves CoreML export and inference reliability, restores accurate RT-DETR INT8 deployment, reduces training overhead, and strengthens dataset and Platform workflows.** 🚀

## 📊 Key Changes

- **🛠️ CoreML dynamic export fixed — PR #26199**
  - YOLO detection, segmentation, pose, and OBB models can now export with `dynamic=True` without triggering a `coremltools` `arange` conversion error.
  - Static CoreML models now correctly process batches of multiple images instead of running inference only on the first image.
  - Supports proper output stacking for raw predictions, embedded NMS, segmentation, and classification models.
  - CoreML export documentation now clarifies restrictions for dynamic inputs, NMS, classification, RT-DETR, and batch sizes.

- **⚡ RT-DETR OpenVINO INT8 export repaired**
  - Keeps the RT-DETR decoder in floating point while applying NNCF transformer-aware quantization.
  - Reported RT-DETR-L accuracy improved from approximately **0.0002 to 0.6513 mAP50-95**, with nearly unchanged CPU inference speed.

- **🏎️ Faster training, especially on GPUs**
  - Avoids unnecessary memory initialization, activation copies, host-device synchronization, and repeated EMA state reconstruction.
  - Enables fused Adam and AdamW optimizers where supported.
  - A measured YOLO26x COCO training step on a B200 GPU improved from **228.9 ms to 183.5 ms**—about a **1.25× speedup** in that test environment.

- **🧠 More memory-efficient SAM3 mask processing**
  - Large semantic masks are upscaled in bounded chunks rather than all at once.
  - This prevents multi-gigabyte temporary allocations while preserving mask results.

- **🎯 Classification validation now prevents class-index mistakes**
  - Validation and training splits are aligned to the model’s class names instead of relying on each folder’s local alphabetical ordering.
  - Classes missing from the model are skipped with a warning, preventing silently incorrect accuracy and model-selection metrics.

- **📡 Platform training callbacks now use the Platform SDK**
  - Replaces duplicated raw HTTP and retry logic with the generated SDK.
  - Adds controlled POST retries while preserving authentication handling, cancellation, checkpoint signing, payload sanitization, and quiet console-error behavior.
  - Requires `ultralytics-platform>=0.1.45`.

- **✅ Clearer dataset and validation checks**
  - Segment datasets now reject box-only labels or mismatched polygon and box counts.
  - Pose validation reports an actionable error when `kpt_shape` is missing, including when stale label caches are present.
  - `save_json=True` now reports small-, medium-, and large-object mAP on detection datasets using `faster-coco-eval`.
  - Training resume behavior is documented: the checkpoint dataset is restored unless an explicit `data=` override is provided.

- **🌐 Platform workflow and documentation updates**
  - Documents semantic PNG mask imports, similar-image search, generated image variations
