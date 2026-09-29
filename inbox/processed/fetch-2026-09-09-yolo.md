---
title: "yolo v8.4.144 Release Notes"
created: 2026-09-09
captured: 2026-09-09
type: release-note
tag: v8.4.144
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.144
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.144 Release Notes (2026-09-08)

## 🌟 Summary

**v8.4.144 improves model reliability, numerical stability, inference precision, and deployment workflows without changing model architectures.** 🚀

## 📊 Key Changes

- **More reliable model YAML loading** 🧩  
  Explicitly requested files such as `custom26n.yaml` are now loaded before attempting a scale-unified fallback like `custom26.yaml`. This prevents custom model definitions from being silently replaced.

- **Safer training and assignment edge cases** 🛡️  
  Empty-label batches now return correctly typed boolean foreground masks, keeping task-aligned assigners consistent with their normal output contract.

- **Stable CIoU calculations for reduced precision** 🔢  
  The overlap calculation now avoids `NaN` values and invalid gradients for identical FP16 and BF16 boxes, improving training stability on lower-precision hardware.

- **More efficient repeated `model.to()` calls** ⚡  
  Cached predictors are preserved when a model is already on the requested device or precision. This avoids unnecessary rebuilding, reducing latency and memory use during repeated inference setup.

- **Improved Triton FP32 behavior** 🎯  
  Triton client tensors now remain in FP32 even when `quantize=16` is requested. This prevents unintended input rounding and output conversion on the client while leaving the server-side model precision unchanged.

- **Faster semantic segmentation mosaic loading** 🖼️  
  Semantic masks for buffered mosaic images are now retained in RAM instead of being decoded repeatedly. Benchmarks showed approximately **1.26× to 1.77× faster** data loading, depending on the configuration.

- **More flexible CLI configuration** 🛠️  
  Arguments provided before `cfg=<file>` are now preserved, and blank `data` values in copied configuration files correctly fall back to the task’s default dataset.

- **Broader OpenVINO/NNCF compatibility** 📦  
  The general upper version limit for NNCF has been removed, allowing newer NNCF 3.x releases with modern PyTorch and OpenVINO installations while retaining legacy restrictions where required.

- **More informative quantization documentation** 📚  
  QAT versus post-training quantization results are now documented for YOLO26 models. The examples show that QAT provides little benefit for the smallest model but can recover substantially more INT8 accuracy for larger models.

- **More robust CI and test infrastructure** ✅  
  CLA permissions were corrected, DEEPX export environments are skipped on machines with less than 15 GiB of RAM, and checkpoint corruption tests now work correctly with channels-last tensors.

- **Documentation maintenance** 🔗  
  The DL Streamer system requirements link was fixed, and the documentation license banner now uses a CDN-hosted asset.

## 🎯 Purpose & Impact

- **Users get more predictable model behavior**, especially when working with custom YAML files or unusual training batches.
- **Training with FP16 or BF16 is more robust**, reducing the risk of silent `NaN` values tha
