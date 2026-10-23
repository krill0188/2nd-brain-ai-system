---
title: "yolo v8.4.184 Release Notes"
created: 2026-10-23
captured: 2026-10-23
type: release-note
tag: v8.4.184
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.184
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.184 Release Notes (2026-10-22)

## 🌟 Summary
A reliability-focused release with an important TIFF-reading fix, plus improvements to segmentation prompts, model loading, validation, integrations, and Platform workflows—without introducing a new model architecture.

## 📊 Key Changes
- **Multi-page TIFF handling (PR #26842):** By default, grayscale TIFF scans now load as their first page instead of incorrectly combining pages into image channels. Only `cv2.IMREAD_UNCHANGED` stacks same-size pages, preserving the option for multispectral workflows.
- **More reliable YOLOE and YOLO-World loading:** Checkpoint type now determines the correct model wrapper, so specialized models continue to work when saved under generic filenames such as `best.pt`. Changing class names on a text-fused YOLOE model now raises a clear error instead of silently relabeling predictions or failing later.
- **More faithful SAM mask refinement:** Floating-point prompt masks retain negative and fractional values, avoiding unintended changes to mask-refinement inputs.
- **Improved data and metric handling:** Fixes cover multipart polygon connections, confusion-matrix matching, classification prediction with rectangular image sizes, and validation on datasets without labels. Dataset downloads also recognize archive URLs with query strings.
- **Smoother integrations and runtime behavior:** Weights & Biases now supports training inside a user-started run, preserving its settings and leaving it open afterward. Additional fixes improve Platform training resume behavior and OpenVINO/LiteRT device handling.
- **Updated CI and documentation:** CPU runners gain SSH, `rsync`, and libraries needed to import GUI OpenCV. Documentation clarifies Platform dataset workflows and training features, corrects export examples, and refreshes several guides and screenshots.

## 🎯 Purpose & Impact
- **Prevents TIFF-related training failures:** Scanned documents are no longer mistaken for multi-channel images or allowed to produce images with excessive channel counts. Users who intentionally need TIFF pages as bands should use `cv2.IMREAD_UNCHANGED`.
- **Makes model and data workflows more predictable:** Correct model selection, clearer YOLOE class-change errors, and more accurate mask and polygon handling reduce confusing failures and incorrect results.
- **Improves validation and experiment tracking:** Label-free validation avoids unnecessary warnings, confusion-matrix matching is more consistent, and existing W&B runs retain their history and remain available for further logging.
- **Reduces setup friction:** More complete CPU runners and clearer Platform and export documentation make common CI and training tasks easier to run.

## What's Changed
* Add rsync to the CPU GitHub runner image by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26796
* Include OpenSSH in the CPU GitHub runner image by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26797
* Use YOLO11n example model name for IMX500 in expor
