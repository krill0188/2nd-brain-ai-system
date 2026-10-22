---
title: "yolo v8.4.183 Release Notes"
created: 2026-10-21
captured: 2026-10-21
type: release-note
tag: v8.4.183
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.183
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.183 Release Notes (2026-10-20)

## 🌟 Summary
**Ultralytics 8.4.183 expands hardware deployment and improves reliability across training, prediction, data handling, and evaluation.** 🚀

## 📊 Key Changes
- **Axelera Metis support for every YOLO26 task:** With Voyager SDK 1.9.0, detection, instance and semantic segmentation, depth estimation, pose, OBB, and classification models can all export, predict, and validate through `yolo`. The NMS-free detection path is used by default. SDK 1.8 exports remain compatible; the updated setup requires `metis-dkms` 1.7.0 or newer and supports PyTorch versions below 2.15.
- **Higher Axelera throughput:** In the documented COCO128 benchmark, SDK 1.9 reached **109 images per second at batch 32**, compared with 40 images per second on SDK 1.8. Larger prediction batches can improve throughput; batch size 1 remains useful when per-image latency matters.
- **Intel acceleration for LiteRT models:** LiteRT exports can now run on Intel CPUs and NPUs, including support for YOLO26 task types such as detection, segmentation, depth, pose, OBB, and classification.
- **More reliable training and depth calibration:** Fixes address warmup and gradient accumulation edge cases, MPS memory growth during training, and depth calibration replacing an already-good calibration with a worse one. Interrupted runs can also resume under the same Ultralytics Platform model, and W&B resuming works on Windows.
- **More accurate and robust data workflows:** Fixes improve ImageNet-subset classifier validation, accept UTF-8 labels with a byte-order mark, preserve non-ASCII grounding annotations, convert COCO RLE masks for segmentation, and align 16-bit NumPy images with image-file prediction behavior.
- **Prediction, export, and visualization fixes:** Negative FastSAM points now reliably exclude masks regardless of prompt order. Other fixes cover very thin images, rectangular INT8 calibration, grayscale LiteRT models, semantic overlay colors, depth-map saving, and several additional edge cases.
- **Platform and documentation updates:** Platform documentation now includes Gemma 4 and Nemotron as hosted annotation models and explains new visibility controls and workflows. Benchmark instructions were also clarified for NMS-free evaluation.

## 🎯 Purpose & Impact
- **Deploy YOLO26 on more hardware and tasks:** Axelera users can use one integrated workflow across all seven YOLO26 tasks, while Intel LiteRT users gain CPU and NPU inference options.
- **Get better throughput when processing batches:** Axelera SDK 1.9 can substantially increase prediction throughput for larger batches, though actual results depend on hardware and workload.
- **Trust training, validation, and predictions more:** The fixes reduce avoidable failures and make reported results better reflect the supplied data and model—for example, correcting classifier label alignment changes ImageNette validation accuracy from **9.45% to 70.37%** in the reported test.
- **Keep existing workflows working:** Many changes are 
