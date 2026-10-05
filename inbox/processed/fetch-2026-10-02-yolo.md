---
title: "yolo v8.4.171 Release Notes"
created: 2026-10-02
captured: 2026-10-02
type: release-note
tag: v8.4.171
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.171
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.171 Release Notes (2026-10-01)

## 🌟 Summary
**v8.4.171 adds end-to-end AMD GPU support for Ultralytics workflows, alongside fixes to dataset handling, model export, and several task-specific behaviors.**

## 📊 Key Changes
- **AMD ROCm and MIGraphX support (PR #24137):** Train and run native PyTorch models on supported AMD GPUs with ROCm, and run exported ONNX models using the MIGraphX execution provider. Provider selection is automatic on supported systems, with CPU fallback if MIGraphX is unavailable.
- **AMD deployment options:** Adds a ROCm-based `latest-amd` Docker image, AMD GPU CI testing, and setup and usage guidance. MIGraphX support targets Linux x86_64 with Python 3.11 or newer.
- **Faster repeat ONNX startup:** MIGraphX compiled models are cached, avoiding recompilation on later loads. Published Radeon 8060S benchmarks show matching accuracy and faster inference for ONNX/MIGraphX than PyTorch ROCm in the tested configurations; the first run still incurs compilation time.
- **Dataset and training fixes:** Restores reading existing image caches across cache modes, preserves archive timestamps to avoid unnecessary label rescans, and corrects RT-DETR denoising query matching during training.
- **Export and task fixes:** Reduces temporary storage used by Core ML NMS exports, improves pose keypoint scaling in LiteRT/RKNN, and fixes several mask and analytics behaviors.
- **Documentation and CI improvements:** Adds Apple M4 Core AI/Core ML latency results and suppresses expected tracer warnings in pytest logs.

## 🎯 Purpose & Impact
- **More hardware choice:** AMD users can train with ROCm and deploy ONNX models with GPU acceleration through MIGraphX, without changing their usual prediction calls.
- **Smoother deployment:** The AMD Docker image and dedicated setup documentation make it easier to get started, while hardware CI helps verify the ROCm path.
- **More reliable workflows:** Cache and training fixes help avoid wasted disk space, repeated dataset processing, and incorrect RT-DETR denoising matches.
- **No new model architecture is introduced:** The headline change is broader AMD hardware support, with additional bug fixes and clearer performance guidance.

## What's Changed
* Fix regressions found in third-party PR audits by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26461
* Add Core ML and Core AI latency benchmarks on Apple M4 to the Core AI docs by @onuralpszr in https://github.com/ultralytics/ultralytics/pull/26459
* Remove extra temporary weights copy from CoreML NMS export by @amanharshx in https://github.com/ultralytics/ultralytics/pull/26466
* Fix RT-DETR contrastive denoising group indices by @Nikhi00718 in https://github.com/ultralytics/ultralytics/pull/26465
* Ignore benign TracerWarnings in pytest like the package does by @UltralyticsAssistant in https://github.com/ultralytics/ultralytics/pull/26462
* Add AMD ROCm and MIGraphX support by @itikhono in https://github.com/ultralytics/ultralytics/pull/24137

## New Contributors
* @itik
