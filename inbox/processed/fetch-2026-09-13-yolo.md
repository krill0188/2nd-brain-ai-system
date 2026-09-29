---
title: "yolo v8.4.150 Release Notes"
created: 2026-09-13
captured: 2026-09-13
type: release-note
tag: v8.4.150
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.150
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.150 Release Notes (2026-09-12)

## 🌟 Summary

**v8.4.150 improves secure checkpoint loading, restores compatibility with fused YOLOE models, and adds performance and documentation updates across Ultralytics.** 🚀

## 📊 Key Changes

- **⚡ Faster restricted checkpoint loading — PR #26155 by @glenn-jocher**
  - Resolves only the model classes actually referenced by a checkpoint instead of importing and scanning every supported model module.
  - Preserves existing trusted namespaces, aliases, registration locks, and allow-list behavior.
  - Restores the safe `forward` and `forward_fuse` bindings required by fused YOLOE checkpoints.
  - Improves error reporting by showing the rejected object type without calling `repr()` on partially reconstructed modules.
  - Adds support for legacy NumPy metadata and embedded Ultralytics CLIP objects during restricted loading.
  - Extends tests to cover legacy checkpoints, fused models, NumPy fitness values, and inference-output consistency.

- **🛡️ Safer diagnostics and Ray Tune compatibility — PR #26151**
  - Prevents Sentry from capturing command-line arguments and local variables that may contain credentials.
  - Enforces Ray version `2.41.0` or newer and removes obsolete compatibility code for older Ray releases.

- **📈 More efficient RT-DETR training on dense datasets — PR #26150**
  - Avoids calculating matching costs between predictions and targets from different images.
  - Reduces unnecessary cost storage and padding overhead, with the greatest benefits expected on datasets containing many objects per image, such as SKU-110K.
  - Keeps the assignment solver, losses, precision, and training configuration unchanged.

- **📚 YOLO27 preview documentation**
  - Publishes a clearly labeled **YOLO27 Coming Soon** model page with planned architecture details, supported tasks, preliminary benchmarks, and future usage examples.
  - Adds discovery links throughout the README and documentation.
  - Clarifies that YOLO27 weights, package support, and a launch date are not currently available; **YOLO26 remains the recommended released model**.

- **☁️ Expanded Ultralytics Platform deployment documentation**
  - Documents configurable CPU and memory resources, uptime billing, scale-to-zero behavior, and lightweight monitoring for eligible paid endpoints.
  - Explains that prediction examples and statistics are temporary and may be lost after stopping, restarting, redeploying, resizing, or replacing an endpoint.
  - Describes saving useful prediction examples to datasets for persistent storage.

- **🏆 Clearer model benchmark tables**
  - Standardizes bold highlighting for best accuracy, speed, latency, size, parameter count, and computational-cost values across model documentation.
  - Updates benchmark tables for YOLO26, YOLO11, YOLOv8, YOLOv9, YOLO12, YOLOE, SAM, YOLO-NAS, and other supported families without changing the underlying results.

## 🎯 Purpose & Impact

- **More reliable production loading:** Fused YOLOE checkpoints and older Platform checkp
