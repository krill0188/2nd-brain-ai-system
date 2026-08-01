---
title: "yolo v8.4.114 Release Notes"
created: 2026-08-01
captured: 2026-08-01
type: release-note
tag: v8.4.114
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.114
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.114 Release Notes (2026-07-31)

## 🌟 Summary

**v8.4.114 improves reliability across Platform workflows, exported models, validation, edge inference, and advanced vision tasks—while delivering clearer errors and faster, more robust execution.** 🚀

## 📊 Key Changes

- **Clearer Ultralytics Platform errors and quieter retries** — PR #25581 by @glenn-jocher:
  - Platform URI resolution now uses `GET` instead of `HEAD`, preserving the detailed error messages returned by the Platform.
  - API errors such as invalid credentials, inaccessible datasets, and malformed pose labels now include actionable details.
  - Console-output upload failures no longer create a feedback loop where logged retry warnings trigger additional failed uploads.
  - Platform requests now stop early when no API key is available, and invalid credentials disable further attempts.

- **Improved exported-model validation**:
  - Static ONNX, TensorRT, OpenVINO, and similar models now automatically reuse the image size stored in export metadata.
  - Users no longer need to manually provide the exact export `imgsz` during validation. ✅

- **More reliable model export and deployment**:
  - Fixed GPU device mismatches during TorchScript inference by ensuring generated anchors follow the runtime device.
  - Prompt-free YOLOE exports now work correctly with NCNN and Paddle formats.
  - Loading a TorchScript archive as if it were a PyTorch checkpoint now produces a clearer error message.
  - Paddle export compatibility was improved for newer Python and x2paddle environments.

- **Faster LiteRT CPU inference**:
  - LiteRT now uses the configured number of CPU threads, enabling multi-core inference.
  - Raspberry Pi 5 LiteRT benchmarks were corrected for YOLO26n and YOLO26s, showing substantially lower latency than previously reported. ⚡

- **Fixes for SAM3, visualization, and pose rendering**:
  - SAM3 semantic prediction now defines the required mask threshold and avoids an `AttributeError`.
  - Class activation maps safely handle class IDs outside a model’s output range.
  - Pose keypoints and limbs located exactly on image borders are now rendered correctly instead of being silently dropped.

- **Improved training and data pipelines**:
  - BGR augmentation now applies correctly to semantic segmentation and depth training.
  - Distributed validation no longer crashes when the total batch size exceeds the number of validation images.
  - Dataset YAML validation handles empty `names` fields more safely.
  - Analytics line charts now accumulate counts across the configured update window instead of resetting every frame.

- **Documentation and maintenance updates**:
  - Added missing validation documentation for `channels_last`.
  - Documented class remapping and depth-loss training parameters.
  - Updated augmentation support tables for semantic and depth tasks.
  - Fixed Intel DL Streamer installation links and similarity-search examples.
  - Removed several redundant regression tests to reduce test-suite maintenance overh
