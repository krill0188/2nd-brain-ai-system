---
title: "yolo v8.4.137 Release Notes"
created: 2026-09-01
captured: 2026-09-01
type: release-note
tag: v8.4.137
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.137
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.137 Release Notes (2026-08-31)

## 🌟 Summary

**v8.4.137 automatically enables the faster channels-last memory layout for CUDA training on PyTorch 1.11+, improving GPU training performance while preserving clear opt-out and compatibility options.** 🚀

## 📊 Key Changes

- **Automatic channels-last training:** The existing `channels_last=None` setting now automatically uses the NHWC memory format for CUDA training with **PyTorch 1.11 and newer**.
- **Explicit control remains available:**
  - `channels_last=None`: Automatically selects channels-last when supported.
  - `channels_last=False`: Explicitly keeps the traditional NCHW format.
  - `channels_last=True`: Explicitly requests channels-last, preserving previous behavior.
- **Safe compatibility behavior:** PyTorch 1.10 and older, CPU, and MPS training continue using NCHW by default.
- **Improved resume handling:** The `channels_last` setting is now included among the training options that can be updated when resuming a run.
- **Documentation updates:** Training guides and argument references now describe the automatic CUDA behavior.
- **No model architecture changes:** This release focuses on training performance and memory layout rather than changing model structure or outputs.

## 🎯 Purpose & Impact

- ⚡ **Potentially faster CUDA training:** Channels-last can improve convolution performance on compatible GPUs, particularly modern Tensor Core hardware.
- 🧠 **Better YOLO26 training defaults:** Users no longer need to manually enable the optimization when using a supported PyTorch and CUDA environment.
- 🛡️ **Reduced compatibility risk:** Automatic activation begins at PyTorch 1.11, the first validated version that avoids known channels-last failures in YOLO26 training.
- 🔧 **Full user control:** Workloads that require the traditional layout can disable the optimization with `channels_last=False`.
- 🌍 **Broad validation:** The change was tested across CUDA 11.1–13.2, PyTorch 1.8–2.12, Python 3.8–3.13, and a wide range of modern NVIDIA GPUs.
- 📦 **Minimal implementation impact:** The behavior is selected during trainer setup without adding new arguments, persistent state, helper utilities, or GPU-specific allowlists.

## What's Changed
* Auto-enable channels-last CUDA training by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26007


**Full Changelog**: https://github.com/ultralytics/ultralytics/compare/v8.4.136...v8.4.137
