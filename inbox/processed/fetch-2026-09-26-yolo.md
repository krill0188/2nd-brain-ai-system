---
title: "yolo v8.4.163 Release Notes"
created: 2026-09-26
captured: 2026-09-26
type: release-note
tag: v8.4.163
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.163
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.163 Release Notes (2026-09-25)

## 🌟 Summary
YOLO models can now be exported to Apple Core AI format from x86_64 Linux, making Linux servers and CI environments useful for preparing models for Apple devices.

## 📊 Key Changes
- 🍎 **Core AI export on Linux:** Export `.aimodel` files on x86_64 Linux as well as Apple silicon Macs running macOS 26 or later. The exported models target iOS 27 and macOS 27; **running them still requires Apple hardware**.
- 🔧 **Updated Core AI compatibility:** Supports `coreai-torch` 0.4.3, which performs optimization during conversion. The dependency now supports Python 3.11–3.14.
- 📈 **Clearer benchmarks:** Linux can report Core AI export results, while inference is correctly skipped because it requires macOS.
- 🛠️ **More reliable exports:** PyTorch functions patched for certain ONNX exports are now restored even when an export fails, preventing unexpected effects on later operations in the same process.
- 🐳 **Lean­er Docker images:** Docker builds avoid retaining package-install caches and remove bundled PyTorch test files, reducing image contents without removing needed runtime tools.

## 🎯 Purpose & Impact
- 🌐 Teams can build Apple-targeted models in Linux-based cloud, server, and CI workflows instead of needing a Mac for export.
- 📱 Apple hardware is still required to run `.aimodel` files, and Core ML remains a separate option.
- ✅ Export failures are less likely to leave a Python process in a modified state, while smaller Docker images use less storage and are quicker to distribute.

## What's Changed
* Skip the uv cache and torch test files in Docker images, and fix Core AI export by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26326
* Support coreai-torch 0.4.3, which removed `AIProgram.optimize()` by @cdeil in https://github.com/ultralytics/ultralytics/pull/26327
* Restore PyTorch functions after failed exports by @Nikhi00718 in https://github.com/ultralytics/ultralytics/pull/26325
* `ultralytics 8.4.163` Export Apple Core AI models on Linux by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26333


**Full Changelog**: https://github.com/ultralytics/ultralytics/compare/v8.4.162...v8.4.163
