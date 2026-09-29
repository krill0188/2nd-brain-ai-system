---
title: "yolo v8.4.164 Release Notes"
created: 2026-09-28
captured: 2026-09-28
type: release-note
tag: v8.4.164
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.164
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.164 Release Notes (2026-09-27)

## 🌟 Summary
**v8.4.164 makes FLOPs reporting more efficient and improves export, video inference, dataset validation, and reliability—without changing model architectures or predictions.**

## 📊 Key Changes
- **Faster FLOPs counting (PR #26373):** Delegates FLOPs estimation to THOP 2.2.0, which supports attention operations and profiles at smaller strides. This replaces full-size profiling for attention-based models such as YOLO11, YOLO12, and YOLO26, as well as RT-DETR. The PR depends on `ultralytics-thop` 2.2.0.
- **More efficient exports:** CoreML export skips redundant trace checking, with reported trace times around 2.8–3× faster. The exporter also removes a duplicate setup forward pass.
- **Improved video prediction:** CUDA prediction can prefetch video frames while the GPU processes the current batch. Batches now stay within one video, also fixing an FPS mix-up when processing videos with different frame rates.
- **More reliable data handling:** Dataset scans now catch malformed OBB labels and fractional class IDs earlier. They also accept pose datasets for detection training and correctly parse multi-row prediction CSV files.
- **Bug fixes and stability:** Fixes include memory growth in PIL-based annotation, cleanup when prediction streams end early, tracker callbacks affecting plain prediction, and YOLOv9 distillation across different head layouts.
- **Clearer deployment guidance:** Documentation adds and updates guidance for Core AI, Rust inference options, export formats, datasets, and deployment workflows.

## 🎯 Purpose & Impact
- **Less overhead when checking model information or starting training:** FLOPs reporting no longer needs a full-resolution forward pass for the affected models, which can make `model.info()` and training startup logging lighter.
- **Faster and smoother deployment workflows:** Export setup does less redundant work, and CUDA video prediction can overlap frame loading with GPU inference.
- **Earlier, clearer feedback on dataset problems:** Invalid labels are more likely to produce helpful errors during scanning rather than confusing failures later in training or validation.
- **More dependable runs:** Fixes reduce resource leaks, incorrect tracker behavior, and failures in distillation and prediction-source handling.

## What's Changed
* Ride out PyPI outages when publishing and alert Slack once by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26340
* Speed up CoreML export by disabling redundant trace checking by @amanharshx in https://github.com/ultralytics/ultralytics/pull/26337
* Update Platform docs to 21 export formats by @glenn-jocher in https://github.com/ultralytics/ultralytics/pull/26344
* Update ultralytics-inference version to 0.0.48 and add quantize in documentation by @onuralpszr in https://github.com/ultralytics/ultralytics/pull/26345
* Fix memory growth in `Annotator(pil=True)` from a font reference cycle by @Y-T-G in https://github.com/ultralytics/ultralytics/pull/26346
* Ret
