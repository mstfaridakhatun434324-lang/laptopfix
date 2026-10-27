---
title: "How to Fix Stable Diffusion DirectML Not Using Your NPU"
slug: stable-diffusion-directml-npu-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["stable diffusion", "directml", "npu", "ai image generation", "windows 11", "troubleshooting"]
description: "Fix Stable Diffusion DirectML not using your NPU with steps for DirectML setup, driver updates, model compatibility, and fallback to GPU or CPU execution."
thumbnail: "/images/thumbs/stable-diffusion-directml-npu-fix.webp"
faqs:
  - q: "Can Stable Diffusion run on an NPU?"
    a: >
      NPU support for Stable Diffusion is limited and experimental. Most Stable Diffusion setups use the GPU through DirectML or CUDA, and NPU execution is only available in specific builds and runtimes that expose the NPU through DirectML. For most users, GPU execution is the practical path.
  - q: "What is DirectML?"
    a: >
      DirectML is Microsoft's machine-learning API that lets frameworks run models on Windows hardware — GPU or, where supported, NPU — without vendor-specific code. Stable Diffusion frontends that support DirectML can use it instead of CUDA.
  - q: "Why does my NPU not appear as a DirectML device?"
    a: >
      The NPU appears only if the NPU driver registers it with DirectML and the runtime version supports it. An outdated NPU driver, an old DirectML runtime, or a frontend that only queries GPUs will all hide the NPU.
  - q: "Is NPU image generation faster than GPU?"
    a: >
      Usually not for Stable Diffusion today. Laptop NPUs are optimized for small, efficient models, while Stable Diffusion is a large model that runs faster on a discrete or strong integrated GPU. The NPU advantage is power efficiency, not raw speed.
---

You installed Stable Diffusion hoping your AI laptop's NPU would generate images, but the NPU never appears as a device, generation falls back to the CPU at a crawl, or DirectML errors out entirely. The honest starting point is that NPU execution for Stable Diffusion is experimental and narrow — most setups are designed for GPUs, and the NPU path only works in specific combinations of driver, runtime, and frontend.

That does not mean you are stuck. This guide separates the realistic paths: getting DirectML working on your GPU, checking whether your NPU can genuinely be used, and choosing the right execution provider for your hardware. Chasing NPU execution when your stack only supports GPU wastes hours; picking the working provider gets you generating images today.

## Why this happens

- **NPU not exposed through DirectML:** Most NPU drivers do not register the NPU as a general DirectML device, so frontends that enumerate DirectML devices see only the GPU.
- **Frontend only supports GPU providers:** Many Stable Diffusion frontends query for CUDA or DirectML GPU devices and never ask about NPUs, regardless of driver support.
- **Outdated NPU or graphics driver:** DirectML device enumeration depends on current drivers. Stale NPU or GPU drivers can hide devices or produce incompatible versions.
- **Model too large or unsupported on NPU:** Even when an NPU is visible, Stable Diffusion models may exceed NPU memory or use operators the NPU runtime does not support, causing fallback or failure.
- **Missing ONNX or DirectML runtime components:** NPU execution usually goes through ONNX Runtime with a DirectML execution provider. Missing or mismatched runtime versions break the chain.
- **Wrong Python environment or package versions:** Mixed package versions — torch, onnxruntime, diffusers — can silently disable DirectML or NPU providers even when the hardware is ready.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set expectations and check what devices DirectML actually sees

Before changing anything, find out which devices your stack can use. This prevents chasing an NPU path that does not exist on your machine.

1. Open your Stable Diffusion frontend's settings or logs and look for the execution provider and device list it reports.
2. If it lists a GPU via DirectML, GPU execution is available — that is your reliable path, covered in the next fix.
3. If it lists no device or CPU only, the DirectML runtime or driver is the problem, not the model.
4. Check your NPU driver's presence in Device Manager under **Neural processors** or **System devices**.
5. If no NPU device appears in Device Manager either, update the NPU driver from your maker before going further. For related NPU driver work, see [TensorFlow DirectML on AI laptops](/articles/tensorflow-directml-ai-laptop-fix/).

### Fix 2: Get DirectML GPU execution working first

GPU via DirectML is the well-supported path on AI laptops, and it should be your baseline before any NPU experiment.

1. Update the graphics driver from your laptop maker's support page or [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics.
2. In your frontend, select the DirectML execution provider explicitly rather than leaving it on auto.
3. Start with a small model, such as a distilled or turbo variant, to confirm generation works at all.
4. If generation succeeds on GPU, you have a working baseline — NPU experiments are now optional, not blocking.
5. If GPU DirectML also fails, the runtime or Python environment is the problem — move to the environment fix below.

### Fix 3: Repair the Python environment and runtime packages

Mixed or stale packages are the most common reason DirectML silently falls back to CPU. A clean environment fixes them.

1. Create a fresh Python virtual environment for Stable Diffusion rather than reusing a mixed one.
2. Install the versions your frontend documents for torch, onnxruntime, and diffusers — do not mix latest-everything with a pinned frontend.
3. Install the DirectML-specific onnxruntime build if your frontend requires it, following its documentation exactly.
4. Run a small test generation and check the logs for which provider actually executed — "CPUExecutionProvider" in the logs means DirectML did not engage.
5. If logs show DirectML errors, copy the exact error message and search your frontend's issue tracker — DirectML errors are usually version mismatches with known fixes.

### Fix 4: Check NPU support honestly for your specific stack

Only pursue NPU execution if your stack documents it. Otherwise you are fighting the frontend's design.

1. Check your frontend's documentation for NPU or DirectML NPU support statements.
2. Check your NPU maker's documentation for DirectML NPU support on your processor family.
3. If neither documents NPU execution, accept GPU execution — the NPU on your laptop is designed for Windows AI features, not for Stable Diffusion.
4. If both document it, update the NPU driver, the DirectML runtime, and the frontend to the documented compatible versions.
5. Test with the smallest supported model first, since NPU memory limits reject large models outright.

### Fix 5: Handle model size, memory, and operator failures

NPU and integrated GPU execution both fail on models that exceed available memory or use unsupported operators. Shrinking the workload is often the fix.

1. Try a smaller model variant — distilled, turbo, or quantized — before a full-size model.
2. Reduce the image resolution for the first test, since memory scales with resolution.
3. Enable attention slicing or model offloading options if your frontend offers them.
4. Close other apps competing for GPU or NPU memory during generation.
5. If a specific model always fails while smaller models succeed, the model itself is the limiter, not your setup.

### Fix 6: Use the right fallback and keep the working setup

A working GPU setup beats a broken NPU experiment. Lock in the configuration that generates images reliably.

1. Record the driver versions, package versions, and settings of your working configuration.
2. Use GPU DirectML as your daily execution provider on AI laptops.
3. Revisit NPU execution only when a new frontend release or driver update explicitly adds support.
4. For cloud or API alternatives when local generation is too slow, use a hosted image service rather than fighting local hardware limits.
5. For further Windows AI guidance, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows). Related local-AI setup issues are covered in [Fooocus install fixes](/articles/fooocus-ai-laptop-install-fix/) and [Automatic1111 on ARM](/articles/automatic1111-arm-windows-install-fix/).

## Closing

Stable Diffusion on an AI laptop works best through DirectML on the GPU — that is the supported, tested path. NPU execution is experimental, narrow, and undocumented for most frontends, so check whether your stack even supports it before investing hours. Get GPU generation working first, keep that configuration stable, and treat NPU support as a future upgrade, not a prerequisite for generating images today. If this fix did not fully resolve the issue, related troubleshooting for [Asus Zenbook 14 Oled Ai Issues](/articles/asus-zenbook-14-oled-ai-issues-fix/) and [Click To Do Snipping Tool Not Working](/articles/click-to-do-snipping-tool-not-working/) covers neighboring causes that can produce the same symptom on AI laptops.
