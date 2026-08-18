---
title: "yolo v8.4.120 Release Notes"
created: 2026-08-15
captured: 2026-08-15
type: release-note
tag: v8.4.120
domain: ai-autonomy
source: https://github.com/ultralytics/ultralytics/releases/tag/v8.4.120
tags: [drone, ai-autonomy, yolo]
---

# yolo v8.4.120 Release Notes (2026-08-13)

## 🌟 Summary

Ultralytics **8.4.120** improves CUDA training determinism and TensorFlow export reliability, while expanding documentation for LLM workflows and AI coding-agent integrations. 🚀

## 📊 Key Changes

- **Deterministic CUDA anchor generation** by @glenn-jocher
  - Replaced CUDA cumulative-sum operations with deterministic `arange`-based generation when creating detection anchors.
  - Removes recurring `cumsum_cuda_kernel` warnings during deterministic training.
  - Preserves runtime device handling for traced and TorchScript GPU models, avoiding device information being incorrectly fixed during tracing.

- **More reliable TensorFlow exports** 🛠️
  - Removed the obsolete NVIDIA package index from TensorFlow and non-YOLO export dependency installation.
  - `onnx-graphsurgeon` can now be installed directly from PyPI, reducing DNS and connectivity issues—especially in CPU-based CI environments and isolated export setups.

- **New Ultralytics LLM documentation** 🤖
  - Documents the OpenAI-compatible `LLM` interface for text, image, streaming, asynchronous, provider-specific, and YOLO-combined workflows.
  - Provides examples for OpenAI-compatible services such as DeepSeek, Kimi, Z.AI GLM, OpenRouter, and local servers.
  - Updates the default documented and runtime model to `gpt-5.6-luna`.

- **New Agent Skills integration guide** 🧩
  - Documents the official [`ultralytics/skills` repository](https://github.com/ultralytics/skills).
  - Covers AI-agent skills for model selection, datasets, training, tuning, inference, and export.
  - Includes installation guidance for Claude Code, Codex, and other compatible agents.

- **Version update**
  - Bumped the Ultralytics package version from `8.4.119` to `8.4.120`.

## 🎯 Purpose & Impact

- ✅ **Cleaner deterministic training logs:** Users no longer see repeated CUDA cumsum warnings that can obscure important training messages.
- ✅ **More predictable model tracing:** TorchScript and traced GPU models retain runtime device behavior without sacrificing the deterministic anchor-generation fix.
- ✅ **Smoother TensorFlow export setup:** Fewer external package-index dependencies should improve export reliability in restricted networks, CI pipelines, and CPU-only environments.
- ✅ **Better LLM discoverability:** Developers can more easily connect YOLO detection results with language and vision models through a consistent interface.
- ✅ **Improved AI-assisted development:** Agent Skills provide structured, workflow-specific guidance for using Ultralytics tools with supported coding agents.
- ℹ️ **No major model architecture changes were introduced in this release**; the primary technical improvement is improved determinism and export robustness.

## What's Changed
* Document the OpenAI-compatible LLM interface by @onuralpszr in https://github.com/ultralytics/ultralytics/pull/25789
* Document Ultralytics Agent Skills by @JaviChulvi in https://github.com/ultralytics/ultralytics/pull/25787
* Avoid nondeterminis
