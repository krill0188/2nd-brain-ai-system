---
title: "yolo v8.4.152 Release Notes"
created: 2026-09-15
captured: 2026-09-15
type: release-note
tag: v8.4.152
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.152
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.152 Release Notes (2026-09-14)

## 🌟 Summary

**v8.4.152 improves system monitoring by adding cached NVIDIA driver and driver-supported CUDA version information to `SystemLogger`.**

## 📊 Key Changes

- 🖥️ Added top-level `driver_version` and `cuda_version` fields to system metrics collected on NVIDIA-enabled systems.
- ⚡ Version information is queried once when `SystemLogger` starts, avoiding repeated NVML calls during metric collection.
- 🛡️ GPU utilization monitoring continues to work even when version information is unavailable; missing fields are simply omitted.
- 📌 `cuda_version` represents the CUDA version supported by the installed NVIDIA driver, matching the value reported by `nvidia-smi`—not the installed CUDA toolkit or PyTorch build version.
- 📦 Bumped the package version from `8.4.151` to `8.4.152`.

## 🎯 Purpose & Impact

- 🔍 Monitoring systems can now receive NVIDIA driver and CUDA compatibility details directly from `SystemLogger`, without collecting them separately.
- 🚀 Caching keeps repeated metric collection efficient, with validation confirming only one query per version per logger instance.
- 🌍 Non-NVIDIA and macOS environments remain compatible, with NVIDIA-specific fields omitted when unavailable.
- ✅ Testing on an eight-GPU server confirmed accurate versions, reliable collection across cumulative and rate modes, and strong performance.

## What's Changed
* Report NVIDIA driver and CUDA versions in SystemLogger by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26173


**Full Changelog**: https://github.com/ultralytics/ultralytics/compare/v8.4.151...v8.4.152
