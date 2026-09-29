---
title: "yolo v8.4.162 Release Notes"
created: 2026-09-25
captured: 2026-09-25
type: release-note
tag: v8.4.162
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.162
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.162 Release Notes (2026-09-24)

## 🌟 Summary
YOLO prediction can now load the next batch of images while CUDA processes the current one, alongside performance, export, dataset, and Ultralytics Platform improvements. No model architectures or weights changed.

## 📊 Key Changes
- 🚀 **Faster CUDA prediction:** For multi-batch, image-only detection using PyTorch weights, prediction prefetches the next batch on a worker thread while the GPU handles the current batch. Other devices, tasks, backends, and mixed image/video sources keep the existing behavior.
- ⚡ **Faster training data preparation:** Optimized copy-paste augmentation and semantic-mask target generation while preserving their expected outputs.
- 🧠 **Lower memory use during TensorFlow INT8 export:** Calibration images are collected into a preallocated array instead of building several large intermediate copies.
- ☁️ **More Platform annotation and dataset features:** Added hosted text-prompted SAM 3 and SAM 3.1 options, expanded cloud-storage imports to 500,000 objects, and enabled image search by annotated class name.
- 🛠️ **More robust workflows:** Fixed Windows OpenVINO crashes and GPU ONNX inference silently falling back to CPU; improved dataset archive and `.yml` support, OOM recovery, and tracking when source files share a name.

## 🎯 Purpose & Impact
- ⏱️ **Better GPU utilization:** Overlapping image loading with inference can reduce idle time during eligible CUDA prediction runs. It complements existing work that speeds up decoding within a batch.
- 📈 **Smoother data workflows:** Faster augmentation and reduced calibration memory use can help improve training and export efficiency, especially on constrained systems.
- 🔍 **Easier annotation and dataset management:** Text-prompted SAM, larger cloud imports, and class-name search make it simpler to label and browse larger datasets.
- ✅ **Fewer surprises:** Export, Windows inference, archive loading, tracking, and training recovery fixes improve reliability without changing model behavior.

## What's Changed
* Reduce peak memory during INT8 TensorFlow calibration by @cainiao33 in https://github.com/ultralytics/ultralytics/pull/26288
* Point the validator at the rebuilt dataloader after OOM auto-reduce by @cainiao33 in https://github.com/ultralytics/ultralytics/pull/26296
* Simplify tar download handling and remove redundant regression fixtures by @cainiao33 in https://github.com/ultralytics/ultralytics/pull/26287
* fix incorrect dataset in OBB loss error message by @lmycross in https://github.com/ultralytics/ultralytics/pull/26314
* Fix Windows OpenVINO crashes and CI runtime warnings by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26317
* Remove headless-unsafe destroyAllWindows from Streamlit Inference by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26320
* Annotate CI test failures and xdist worker crashes on GitHub Actions by @Y-T-G in https://github.com/ultralytics/ultralytics/pull/26318
* Speed up overlap_mask=False semanti
