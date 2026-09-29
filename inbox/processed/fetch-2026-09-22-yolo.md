---
title: "yolo v8.4.158 Release Notes"
created: 2026-09-22
captured: 2026-09-22
type: release-note
tag: v8.4.158
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.158
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.158 Release Notes (2026-09-21)

## 🌟 Summary

**Ultralytics 8.4.158 improves YOLO26 training reliability, model export compatibility, data handling, inference backends, and Ultralytics Platform workflows.** 🚀

## 📊 Key Changes

- **🔄 Mosaic augmentation now stays closed after OOM recovery**
  - Fixed a training issue where automatic batch-size reduction rebuilt the dataloader and unintentionally re-enabled Mosaic augmentation.
  - The trainer now re-arms the mosaic-closing logic after rebuilding the pipeline, ensuring the augmentation state matches the training log and configuration.

- **⚙️ More reliable AutoBatch sizing**
  - AutoBatch no longer treats a failed batch-one probe caused by BatchNorm at very small image sizes as a GPU memory limit.
  - Added CUDA coverage for small image sizes to prevent regressions.

- **🧠 Improved data loading and caching**
  - RAM image caches can now be shared more efficiently with `spawn` and `forkserver` DataLoader workers.
  - Linux DataLoader workers start lazily, reducing the risk of image-decoder deadlocks during initialization.
  - Dataset hyperparameters are copied before transforms modify them, preventing one dataset from changing settings used by later datasets.
  - Disk caching now uses a smaller safety margin and handles failed cache writes more safely.

- **📦 Stronger download and dataset handling**
  - `safe_download()` can resume interrupted downloads with HTTP Range requests, handle encoded responses, and better tolerate temporary server errors.
  - Invalid files named as archives are now returned as files instead of being mistaken for extracted datasets.
  - NDJSON conversion keeps at least one image when a valid nonzero fraction would otherwise select none.

- **📤 More accurate model exports**
  - Exported models with missing or invalid class names now infer the correct class count from the model head instead of defaulting to 999 names.
  - This improves metadata consistency for legacy detection and classification checkpoints.
  - TorchScript inference is stabilized on older PyTorch versions by avoiding a repeated-inference crash.
  - TensorRT now raises clear errors when dynamic shapes are rejected or inference execution fails.

- **🎭 Better SAM2 video masks**
  - SAM2 video predictions now correctly enforce non-overlapping masks before thresholding.
  - The highest-scoring object owns each pixel, preventing tracked objects from incorrectly covering one another.
  - CPU semantic segmentation postprocessing is also faster through improved class-index selection.

- **🍎 Expanded Apple deployment support**
  - Core AI assets now include model descriptions and are documented as an opt-in path in the Ultralytics iOS SDK and Flutter plugin.
  - Core ML remains the default and recommended Apple deployment format, especially for broader device compatibility.
  - Core AI remains limited to newer Apple operating systems and Apple silicon export environments.

- **🛠️ Ultralytics Platform improvements**
  - Added class-prompted annotati
