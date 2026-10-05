---
title: "yolo v8.4.173 Release Notes"
created: 2026-10-05
captured: 2026-10-05
type: release-note
tag: v8.4.173
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.173
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.173 Release Notes (2026-10-04)

## 🌟 Summary
Version **8.4.173** adds native AMD Xilinx export for **Versal AI Edge Series Gen 2 NPUs**, opening a new path to deploy Ultralytics models on AMD edge hardware.

## 📊 Key Changes
- 🚀 **New `xilinx` export format** — Export models through AMD Quark to a quantized ONNX model and Vitis AI configuration. The format also accepts `vitis`, `vitisai`, and `versal` as aliases.
- 🧠 **Mixed-precision deployment** — Most of the model is quantized to INT8, while the head is kept in floating point for the Vitis AI compiler to run in BF16. The export can be validated on a CPU before deployment; AMD’s Vitis AI tools compile it into a `.rai` model for the NPU.
- 🎯 **Specific hardware support** — The native export targets Versal AI Edge Gen 2 devices, including the VEK385. Older Zynq, Kria, and first-generation Versal devices still require their separate AMD workflows.
- 📚 **Expanded AMD guidance** — New documentation explains export and deployment, hardware compatibility, and which model operations may run on the NPU versus the CPU.
- 🐳 **Smaller Docker images** — Removed unnecessary OpenCV GUI and other system packages from several images. Reported root-filesystem savings range from about **184 MB to 305 MB**, depending on the image. GUI display remains possible by installing the GUI OpenCV build when needed.
- 🔧 **Additional maintenance** — PyTorch dependency support was broadened, and several documentation links and Markdown rendering issues were corrected.

## 🎯 Purpose & Impact
- ✅ Makes it easier to take Ultralytics models from export through validation to deployment on supported AMD Versal Gen 2 hardware.
- ⚙️ INT8 quantization can reduce the model’s deployment footprint, while keeping the head in BF16 helps preserve accuracy. Actual accuracy and speed depend on calibration data, compilation, and the target device.
- 📌 The new export is **not a universal Xilinx export**: deploying on older AMD Xilinx hardware requires the device-specific flows described in the guide.
- 💾 Leaner Docker images reduce storage and download costs; users who need graphical OpenCV features must install them explicitly.

## What's Changed
* Fix raw Markdown in the Vertex AI guide and metric docstrings by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26513
* Keep the docs home language links untranslated by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26515
* Drop unused OpenCV GUI libraries and gnupg from Docker images by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26514
* Fix broken ETH3D link and the Triton localhost reference link by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26516
* Add AMD Xilinx Vitis AI deployment guide by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26517
* Update torch requirement from <2.13.0,>=2.12.0 to >=2.12.0,<2.15.0 by @dependabot[bot] in https://github.com/ultralytics/ultralytics/pull/26463
* `ultralytics 8.4.173` Add AMD Xilinx Vitis
