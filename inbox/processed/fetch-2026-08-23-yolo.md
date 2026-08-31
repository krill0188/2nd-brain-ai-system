---
title: "yolo v8.4.126 Release Notes"
created: 2026-08-23
captured: 2026-08-23
type: release-note
tag: v8.4.126
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.126
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.126 Release Notes (2026-08-21)

## 🌟 Summary

**v8.4.126 makes restricted checkpoint loading safer and up to 40% faster in concurrent environments, while simplifying RLE loss calculations and preserving backward compatibility.**

## 📊 Key Changes

- 🔒 **Thread-safe restricted checkpoint loading**
  - Fixed a race condition when multiple threads loaded PyTorch checkpoints with restricted loading enabled.
  - The shared allow-list is now registered for the process lifetime instead of being temporarily removed when one thread finishes.
  - Added a regression test covering 32 concurrent restricted loads.

- ⚡ **Faster restricted model loading**
  - Only checkpoint globals actually referenced by a file are registered, rather than rebuilding a large allow-list for every load.
  - This reduces restricted-loading overhead by approximately **40%** in affected cases.

- 🛡️ **Improved compatibility with secure loading**
  - Restricted loading now requires PyTorch functionality available from version 2.6 onward; older versions continue to fall back to standard loading behavior.
  - Normal, unrestricted loading remains unchanged.
  - Official **YOLO26** checkpoints, including YOLO26x, are protected from failures caused by concurrent loading.

- 🧠 **Simplified RLE prior calculation**
  - Replaced the runtime multivariate distribution object with a simpler closed-form implementation.
  - Retained existing checkpoint buffers so models saved before v8.4.126 can still resume correctly.
  - Improved numerical behavior under mixed-precision training.

- 🏷️ **Version update**
  - Updated the Ultralytics package version from **8.4.125** to **8.4.126**.

## 🎯 Purpose & Impact

- ✅ **More reliable production inference:** Multi-threaded services and Platform CPU workers can load models concurrently without intermittent checkpoint errors.
- 🚀 **Reduced startup and loading time:** Restricted checkpoint loading performs less unnecessary work, benefiting applications that frequently load models.
- 🔐 **Maintained security benefits:** Safe loading continues to limit checkpoint reconstruction to known, approved classes.
- 🔄 **Backward compatible:** Existing unrestricted workflows and older saved model checkpoints continue to work as before.
- 📉 **Cleaner internal implementation:** The RLE change removes unnecessary distribution-object overhead without changing the intended loss behavior.

## What's Changed
* Make restricted checkpoint loading thread-safe and 40% faster, simplify RLE prior by @pderrenger in https://github.com/ultralytics/ultralytics/pull/25885


**Full Changelog**: https://github.com/ultralytics/ultralytics/compare/v8.4.125...v8.4.126
