---
title: "yolo v8.4.157 Release Notes"
created: 2026-09-21
captured: 2026-09-21
type: release-note
tag: v8.4.157
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.157
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.157 Release Notes (2026-09-20)

## 🌟 Summary

**Ultralytics v8.4.157 makes TensorRT inference faster—up to 20% for FP16 and INT8 engines—while improving YOLOE prompt-free support, Apple Silicon performance, validation reliability, and training stability. 🚀**

## 📊 Key Changes

- **⚡ Faster TensorRT engines (PR #26223, @Y-T-G)**
  - Calibrates FP16 conversion with a real image instead of random noise, allowing more layers to safely run in FP16.
  - Rewrites SiLU activations into a TensorRT-fusable form, reducing memory-bound activation kernels.
  - Adds CUDA Graph replay for supported static TensorRT engines, reducing per-inference launch overhead.
  - Expected impact: **up to 20% faster TensorRT FP16 and INT8 inference**, especially on static-shape engines. CUDA Graph acceleration is not used for dynamic engines, DLA execution, or engines with embedded NMS.

- **🎯 Expanded YOLOE-26 prompt-free inference (PR #26201)**
  - Supports checkpoints containing both one-to-many and one-to-one detection heads.
  - The `nms` setting can now select between standard NMS inference and NMS-free inference.
  - `set_vocab()` can regenerate both branches for custom prompt-free YOLOE models.

- **🍎 Improved Apple Silicon CPU and MPS performance**
  - Disables a slow NNPACK convolution path on Apple Silicon CPUs, improving larger-batch training and validation.
  - Reworks MPS box-IoU and task-assignment operations to avoid expensive reductions.
  - Replaces semantic segmentation `bincount` operations with MPS-friendly alternatives, addressing severe slowdowns and buffer-size failures.
  - Optimizes result export, plotting, and summaries by avoiding repeated per-detection conversions.

- **🧪 More reliable training and validation**
  - AutoBatch no longer treats an initial batch-size probe failure as an out-of-memory limit.
  - Mosaic augmentation now closes correctly during very short training runs.
  - Resume errors now report the actual checkpoint or configuration problem instead of incorrectly claiming the file is missing.
  - Invalid settings such as negative patience, non-positive image sizes, invalid worker counts, and non-finite values are rejected earlier.

- **📐 Improved export and dataset behavior**
  - Fixed-shape exported models consistently retain their exported image size across repeated `predict()` calls.
  - TAR dataset extraction now returns the dataset’s actual top-level directory, matching ZIP behavior.
  - Semantic mask caches correctly handle changes to `nc=1`, preserving foreground pixels in binary mask training.
  - Standalone validation skips labels for classes unsupported by the loaded model instead of crashing.
  - COCO size-specific metrics now remain associated with the correct task, including detection, segmentation, and pose.

- **📦 Smoother dependency installation**
  - Corrected Python-version markers and package conflicts for several export extras, improving `uv lock` and `uv sync` reliability.

## 🎯 Purpose & Impact

- **Faster deployment:** TensorRT users can expe
