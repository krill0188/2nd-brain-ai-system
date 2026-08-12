---
title: "yolo v8.4.118 Release Notes"
created: 2026-08-12
captured: 2026-08-12
type: release-note
tag: v8.4.118
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.118
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.118 Release Notes (2026-08-11)

## 🌟 Summary

Ultralytics v8.4.118 introduces a standalone OpenAI-compatible `LLM` interface alongside `YOLO`, while improving OBB training, dataset handling, model training reliability, and documentation workflows. 🚀

## 📊 Key Changes

- 🤖 **New standalone `LLM` model interface** by @glenn-jocher
  - Add `from ultralytics import LLM` for text and image-based language-model requests.
  - Supports OpenAI Responses and Chat Completions APIs, including synchronous and asynchronous calls.
  - Accepts images from local paths, URLs, data URLs, NumPy arrays, and PIL images.
  - Supports reusable prompts, request overrides, conversation state, API keys, and OpenAI-compatible service endpoints.
  - Uses the optional `openai` dependency and remains independent of Ultralytics Platform and workflow-runtime components.

- 📐 **Improved oriented bounding box training**
  - Mosaic, CutMix, and RandomPerspective now preserve OBB orientation when objects are clipped by image boundaries.
  - Prevents clipped objects from receiving incorrect rotation angles during training.

- ⚡ **Faster CopyPaste augmentation**
  - Batches instance concatenation instead of repeatedly copying growing arrays.
  - Reduces unnecessary processing overhead, especially when many objects are copied.

- 🧠 **More reliable YOLOE behavior**
  - Validates visual prompts before modifying model state.
  - Accepts flat prompts for supported batched image sources.
  - Rejects invalid string class labels and mismatched vocabularies earlier with clearer errors.
  - Preserves gradient settings when converting YOLOE convolution layers to linear layers.

- 🏋️ **Training and inference stability fixes**
  - Correctly resets dataloader workers when resuming after Mosaic augmentation is closed.
  - Allows repeated `train()` and `tune()` calls on the same model object.
  - Prevents duplicate World model callbacks across multi-dataset training.
  - Fixes classification prediction for models without predefined transforms.
  - Ensures classification validation loaders do not discard samples when compiling.
  - Fixes SAM and related predictor models being created with incompatible inference-only tensors.

- 🗂️ **Dataset and prediction improvements**
  - Classification auto-splitting now recognizes all supported image formats, including JPEG, BMP, WebP, TIFF, AVIF, HEIC, and uppercase extensions.
  - Missing classification images now raise a clear `FileNotFoundError` instead of failing later with an unrelated directory error.
  - Preserves original filenames when loading images after EXIF correction.
  - Keeps bounding-box fallbacks for malformed grounding segmentation labels.

- 📚 **Documentation and deployment updates**
  - Standardizes strict documentation validation on Zensical and updates contributor instructions.
  - Documentation redeployment now detects Python docstring and all configuration-file changes.
  - Restores model benchmark chart placeholders, including for YOLO26, while moving production site f
