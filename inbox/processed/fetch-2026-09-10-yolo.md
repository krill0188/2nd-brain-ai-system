---
title: "yolo v8.4.146 Release Notes"
created: 2026-09-10
captured: 2026-09-10
type: release-note
tag: v8.4.146
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.146
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.146 Release Notes (2026-09-09)

## 🌟 Summary

Ultralytics **v8.4.146** improves RT-DETR reliability across small inputs, dynamic exports, and tracking, while updating export portability, Windows training behavior, data downloads, and GPU container environments. 🚀

## 📊 Key Changes

- **🛠️ RT-DETR inference fixes**
  - Prevents failures when small images produce fewer anchors than the configured query count.
  - Keeps query counts, denoising masks, and learned query embeddings consistent.
  - Preserves the correct detection limit in dynamic ONNX and OpenVINO exports.
  - Makes RT-DETR tracking compatible with TrackTrack by avoiding an unsupported NMS recovery argument.
  - Validated across image sizes from 32 to 640 pixels, TorchScript, CoreML, ONNX, OpenVINO, training, validation, and tracking.

- **📦 More device-agnostic TorchScript exports**
  - Removes hard-coded device assumptions from export-time tensor creation.
  - TorchScript models exported on CUDA or Apple MPS can now be loaded and used on other devices, such as CPU.
  - Fixes dynamic RT-DETR export behavior so bounding boxes remain correct at sizes different from the export size.

- **🎯 Improved FP16 embedded-NMS inference**
  - Converts end-to-end NMS output rows to float32.
  - Prevents segmentation, pose, and OBB FP16 exports from failing during mask or box processing.

- **🪟 Better Windows CUDA training defaults**
  - Stops automatically enabling `channels_last` memory format on Windows, where it could significantly reduce performance.
  - Users can still explicitly enable it with `channels_last=True`.

- **🌐 More reliable NDJSON image downloads**
  - Replaces the previous 30-second total timeout with connection and socket-inactivity timeouts.
  - Large images on slow or shared connections are less likely to fail while downloading.

- **🐳 Updated GPU and export environments**
  - AMD64 GPU images now use PyTorch 2.14 with CUDA 13.2.
  - NVIDIA ARM64 images move to NVIDIA PyTorch 26.08 with CUDA 13.4 and updated ONNX Runtime GPU support.
  - GPU runner images now include `g++` for compiled training workflows and TensorRT for CUDA 13.
  - LiteRT remains in the Python export image because its current dependencies are not compatible with PyTorch 2.14.
  - Conda Docker builds now use conda-forge PyTorch 2.13, torchvision 0.28, and CUDA 13.0.

- **🧪 CI and maintenance updates**
  - Restores the GPU CI workflow while keeping it temporarily disabled through an explicit condition.
  - Adds disk cleanup before isolated export setup.
  - Updates documentation for CUDA 13, JetPack, TensorRT, DLA, Conda images, and export compatibility.
  - Bumps the package version from **8.4.145 to 8.4.146**.

## 🎯 Purpose & Impact

- **Greater RT-DETR stability:** Small images and dynamically sized inputs should no longer trigger query or anchor-related inference failures. ✅
- **More dependable deployment:** Models exported on one accelerator can be used on another device more reliably, reducing device-specific TorchScript issues.
- **Safe
