---
title: "yolo v8.4.176 Release Notes"
created: 2026-10-13
captured: 2026-10-13
type: release-note
tag: v8.4.176
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.176
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.176 Release Notes (2026-10-12)

## 🌟 Summary
YOLO 8.4.176 makes YOLO-World checkpoints much smaller after setting custom classes, while improving reliability across validation, fine-tuning, segmentation, tracking, and model deployment.

## 📊 Key Changes
- **YOLO-World checkpoints are dramatically smaller:** Setting classes no longer caches the CLIP text encoder by default. For `yolov8s-worldv2.pt`, a saved checkpoint shrank from **328.5 MB to 25.8 MB**, with identical predictions after reload. Caching remains available when explicitly requested.
- **More reliable validation and fine-tuning:** Detection validation now matches predictions to eligible targets in confidence order, reducing missed matches. YOLOE fine-tuning and resume also preserve trained classification heads instead of reinitializing them.
- **Fixes for segmentation and SAM:** MobileSAM FP16 inference no longer produces empty masks. Reused SAM predictors now reset state for new images and videos. A mask-thresholding change was reverted after it reduced YOLO26 segmentation mAP.
- **Improved deployment and input handling:** ONNX GPU inference now supports custom input names and strided tensors; OpenVINO NPU inference handles batches and depth outputs more reliably. Floating-point NumPy images also work with grayscale models.
- **Smoother video, tracking, and benchmarking:** Saved videos preserve fractional frame rates, high-FPS streams are handled correctly, and trackers can be copied or pickled on newer Python versions. Several benchmark workflow issues were fixed.
- **Documentation and Platform updates:** Docs clarify fine-tuning, inference, and precision behavior; Platform documentation covers relevance-based dataset sorting, email changes, and AI-assisted model comparison.

## 🎯 Purpose & Impact
- **Save storage and simplify sharing:** YOLO-World users can save and move custom-vocabulary checkpoints without carrying an unnecessary CLIP encoder.
- **Trust results and continue training safely:** Validation matching and YOLOE resume fixes reduce misleading evaluation results and prevent trained heads from being lost.
- **Get more dependable inference across devices:** SAM, ONNX, OpenVINO, image inputs, and video handling work more consistently across common workflows.
- **Keep segmentation metrics stable:** Reverting the mask threshold avoids the measured mAP regression introduced by the earlier change.

## What's Changed
* Threshold rescaled segment val masks and keep saved video duration with vid_stride by @Nicholas022400701 in https://github.com/ultralytics/ultralytics/pull/26416
* Add Hailo-8 benchmarks picture to doc by @lakshanthad in https://github.com/ultralytics/ultralytics/pull/26615
* Fix confidence-ordered validation matching for alternate targets by @Nikhi00718 in https://github.com/ultralytics/ultralytics/pull/26616
* Preserve ONNX input names and values in GPU binding by @aswanth-07 in https://github.com/ultralytics/ultralytics/pull/26618
* Fix empty MobileSAM masks in FP16 by computing LayerNorm2d w
