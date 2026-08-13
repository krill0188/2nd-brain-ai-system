---
title: "yolo v8.4.119 Release Notes"
created: 2026-08-14
captured: 2026-08-14
type: release-note
tag: v8.4.119
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.119
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.119 Release Notes (2026-08-13)

## 🌟 Summary

**v8.4.119** improves Intel NPU classification performance with OpenVINO, strengthens detection and tracking reliability, expands Platform integration, and refreshes documentation and developer tooling. 🚀

## 📊 Key Changes

- ⚡ **OpenVINO NPU_TURBO for classification**
  - Enables `NPU_TURBO` automatically for classification models running on supported Intel NPU devices.
  - Applies only when the device advertises support, preserving existing behavior for other tasks, devices, and drivers.
  - Measured classification latency improvements of approximately **42–52%** on an Intel Core Ultra 9 185H, with bit-identical accuracy across tested configurations.
  - Turbo mode is intentionally limited to classification because larger image sizes showed little benefit and could consume unnecessary power.

- 🔌 **Platform SDK exposed from `ultralytics`**
  - Python 3.11+ users can access `Platform`, `AsyncPlatform`, `APIError`, and `APIConnectionError` directly from the main package.
  - Imports are lazy, so the SDK is loaded only when needed.
  - Python 3.8–3.10 users receive a clear compatibility message when requesting Platform exports.

- 🛰️ **More efficient Platform training callbacks**
  - Subsequent metrics, telemetry, and model uploads now reuse the registered model ID instead of repeatedly resolving project and model names.
  - Reduces internal Platform traffic and improves reliability during long training runs.

- 🛡️ **Improved tracking robustness**
  - BYTETracker now ignores detections with zero or negative width or height before creating tracks, preventing invalid Kalman filter states.
  - Kalman filter operations were simplified to use direct slicing instead of unnecessary matrix operations.
  - Removed redundant array copies in multi-object tracking paths.

- 🎯 **Safer detection export postprocessing**
  - Detection top-k selection is now limited to the number of available anchors.
  - Prevents export failures on very small input sizes while preserving normal behavior for standard inputs.

- 🧩 **Corrected CopyPaste augmentation probability**
  - The `CopyPaste` transform now respects its configured probability in flip mode.
  - Previously, eligible images could receive the augmentation unconditionally.

- 📚 **Documentation and usability updates**
  - Updated supported-task banners to cover all seven supported tasks, including semantic segmentation and depth estimation.
  - Added the `Cmd/Ctrl+Delete` image-deletion shortcut to the Platform annotation guide.
  - Added a YOLO26 LiteRT export and mobile deployment tutorial video.
  - Restored light, dark, and system theme controls in the documentation.
  - Removed documentation embeds that did not render correctly on the live site.
  - Improved ASCII string checks using Python’s built-in string operation for faster annotation rendering.

- 🧰 **CI maintenance**
  - Updated the self-hosted runner cleanup action used across several CI jobs.

## 🎯 Purpose & Impact

- 🚀 **Faster edge infe
