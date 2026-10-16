---
title: "yolo v8.4.175 Release Notes"
created: 2026-10-10
captured: 2026-10-10
type: release-note
tag: v8.4.175
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.175
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.175 Release Notes (2026-10-09)

## 🌟 Summary
**v8.4.175 focuses on making training, validation, inference, and deployment more reliable across existing Ultralytics models—without introducing a new model architecture.** The headline fix prevents classification images from appearing in both training and validation splits after a split ratio changes.

## 📊 Key Changes
- **🗂️ Safer classification splits (current PR):** When an image is reassigned after changing the train/validation ratio, its old split copy is removed. Nested class folders retain their paths, and cached data and split directories are preserved.
- **🧠 More dependable model loading:** Pretrained class names are transferred when appropriate, grayscale models make better use of RGB weights, and fine-tuning for fewer classes can retain more learned features. YAML-built pose models also receive the keypoint metadata they need for prediction.
- **📈 More complete and accurate validation:** Compiled validation no longer skips the final partial batch. The release also fixes large semantic-segmentation pixel counts and makes pose evaluation ignore unlabeled COCO keypoints as expected.
- **🖼️ More robust image and stream handling:** Fixes cover 16-bit image inputs, stale image caches, multi-page TIFFs, extensionless image URLs, and RTSP/RTMP/TCP sources that include video-like suffixes.
- **📦 Better export and runtime compatibility:** Fixes address larger inference batches for exports with embedded NMS, empty-frame CoreML handling, dynamic YOLOE CoreML exports, and defaults for exported models’ input sizes.
- **🎥 Tracking and depth improvements:** Tracker IDs are now isolated per tracker, and depth prediction uses the same image stretching approach as validation and calibration.
- **📚 Documentation and tooling updates:** Documentation clarifies Platform workflows, security and compliance, agent skills, depth calibration, and Hailo benchmarks. CI workflows also adopt shared `uv` setup and failure alerts, and the CUDA Docker image updates to PyTorch 2.14.1.

## 🎯 Purpose & Impact
- **Avoid split leakage:** Classification images should no longer be evaluated on images that also appear in training after a ratio change, making validation results more trustworthy.
- **Reduce unexpected failures:** Model loading, image inputs, exported-model inference, and multi-stream tracking should behave more consistently across common configurations.
- **Improve evaluation reliability:** Keeping partial validation batches and handling edge cases correctly can prevent missing samples or misleading metrics.
- **Make workflows easier to follow:** Expanded Platform and integration guidance helps users understand dataset management, calibration, security, and deployment options.

## What's Changed
* Add compliance and certifications to the security help page by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26552
* Use setup-uv defaults for Python and the venv by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26557
