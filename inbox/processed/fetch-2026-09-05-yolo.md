---
title: "yolo v8.4.139 Release Notes"
created: 2026-09-05
captured: 2026-09-05
type: release-note
tag: v8.4.139
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.139
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.139 Release Notes (2026-09-04)

## 🌟 Summary

**v8.4.139** improves training efficiency and reliability—especially by reducing validation memory usage—while refreshing model statistics, dataset handling, optimizer performance, and documentation. 🚀

## 📊 Key Changes

- **Lower validation dataloader memory usage** by @glenn-jocher:
  - Validation workers now prefetch **2 batches instead of 4**.
  - Training loaders continue using a prefetch factor of 4.
  - This reduces queued validation data and shared-memory usage without slowing validation startup. 💾

- **Faster Muon/MuSGD optimizer updates**:
  - Updates are now grouped by column count and flattened according to their memory layout.
  - This avoids unnecessary tensor copies for channels-last convolution weights and preserves fused parameter updates.
  - The standalone `Muon` optimizer and related dead code were removed; `MuSGD` remains available. ⚡

- **More reliable EMA checkpoints**:
  - EMA attributes such as class names, class counts, strides, and class weights are now copied from the unwrapped model.
  - This fixes missing or stale metadata when using distributed training or `torch.compile`.
  - EMA is initialized after class weights are calculated, improving checkpoint consistency. ✅

- **Correct semantic segmentation dataset detection**:
  - A default `masks/` directory is now recognized as PNG-mask semantic segmentation when no `masks_dir` entry is specified.
  - Prevents incorrect class counts and phantom background classes in affected datasets. 🎯

- **Improved FP16 behavior documentation**:
  - Documentation now clearly warns that `quantize=16` can cast a retained PyTorch model in place.
  - A later FP32 call on the same model object may therefore use FP16-rounded weights.
  - This clarification applies to prediction and validation, including shared model objects. ⚠️

- **Refreshed FLOPs and parameter reporting**:
  - Published model statistics were synchronized with the current profiler.
  - Updated values cover YOLO26, YOLO11, YOLO12, YOLOv8, YOLOv5u, and other documented models.
  - Accuracy and speed benchmark values were not changed. 📊

- **More robust and maintainable internals**:
  - Batch-normalization fusion now uses PyTorch’s official fusion utilities.
  - SAM positional embeddings avoid nondeterministic cumulative-sum operations.
  - Temporary module aliases are now thread-safe and restore modified attributes correctly.
  - NumPy-to-tensor conversion can share CPU memory and perform a single device transfer.
  - ONNX export opset selection was simplified and made more compatible with current runtimes.

- **Expanded task visibility and documentation**:
  - Depth estimation is now listed consistently across the README, package description, docstrings, tutorials, and task detection messages.
  - Documentation validation now requires Zensical 0.0.58 or newer.
  - Several model benchmark tables and page frontmatter entries were corrected. 📚

## 🎯 Purpose & Impact

- **Users training with limited system or shar
