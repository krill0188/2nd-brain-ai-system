---
title: "yolo v8.4.177 Release Notes"
created: 2026-10-14
captured: 2026-10-14
type: release-note
tag: v8.4.177
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.177
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.177 Release Notes (2026-10-13)

## 🌟 Summary
**Ultralytics 8.4.177 makes SAM prompts work consistently across image directories and video frames, alongside fixes that improve export reliability, training resumes, and prediction inputs.**

## 📊 Key Changes
- **SAM prompts now persist across a source:** Prompts supplied for a directory or video are applied to every image or frame, rather than just the first. Prompt coordinates are also scaled without changing caller-owned NumPy arrays or tensors.
- **More reliable model exports and inference:** Dynamic OpenVINO exports are pinned to the requested image size on Intel NPUs, which require fixed input dimensions. ONNX GPU inference now falls back to a compatible execution path when output shapes contain symbolic dimensions.
- **Safer training and checkpoint recovery:** Short training runs now take an optimizer step instead of potentially ending without updating the model. RMSprop checkpoints preserve small gradient-history values, helping resumed training avoid unexpectedly large updates.
- **More consistent prediction inputs:** PIL images now respect EXIF orientation, and source lists download only actual HTTP(S) URLs—so local paths beginning with `http` are not mistaken for links.
- **Improved experiment tracking and integrations:** Integration settings are read for each training run. W&B fixes improve final plot logging, offline resume IDs, project/run naming, and cleanup after interrupted or failed runs.
- **Documentation and workflow updates:** Guides clarify validation image geometry, W&B usage, Platform export options, and contribution testing advice. CI failure alerts are centralized, and runner images regain dependencies needed for Codecov signature checks.

## 🎯 Purpose & Impact
- **SAM users** can provide prompts once and get the intended segmentation behavior throughout a folder or video, whether using Python, streaming, or the CLI.
- **Training and deployment users** should see fewer failures on Intel NPUs and dynamic-output ONNX models, while checkpoint resumes and very short runs behave more reliably.
- **Everyday prediction workflows** handle phone-camera images and mixed source lists more predictably.
- **No new model architecture is introduced** in this release; the emphasis is on more dependable prediction, training, export, integrations, and documentation.

## What's Changed
* Name Platform export options and update the contributing guide's test advice by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26659
* Fix dynamic OpenVINO exports failing to compile on the Intel NPU by @onuralpszr in https://github.com/ultralytics/ultralytics/pull/26656
* Centralize workflow failure alerts in the GitHub App by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26661
* Restore Codecov signature dependencies in runner images by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26662
* Add https://youtu.be/TBEPfu2IMXE to docs by @RizwanMunawar in https://github.com/ultralytics/ult
