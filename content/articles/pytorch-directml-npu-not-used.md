---
title: "How to Get PyTorch to Actually Use the NPU with DirectML on Windows"
slug: pytorch-directml-npu-not-used
date: 2026-10-23
categories: ["ai-pc"]
tags: ["pytorch", "directml", "npu", "torch-directml", "copilot+ pc", "onnx"]
description: "PyTorch running on CPU instead of your NPU? Install torch-directml, select the NPU device explicitly, and convert models for clean NPU execution on Windows."
thumbnail: "/images/thumbs/pytorch-directml-npu-not-used.webp"
faqs:
  - q: "Why does PyTorch ignore my NPU even with DirectML installed?"
    a: >
      Plain PyTorch defaults to CPU, and torch-directml enumerates every DirectX device — your integrated GPU is usually listed first, so vague device selection lands on the GPU or falls back to CPU. Explicitly pick the NPU's device index, and make sure the model uses only ops the NPU supports.
  - q: "Do I need a special Python build for NPU inference on Snapdragon?"
    a: >
      Yes. Use a native ARM64 Python build, not x64 Python under Prism emulation. Emulated Python adds overhead and can break torch-directml's device binding, so NPU acceleration stays unreliable until you switch to the native interpreter and matching ARM64 packages.
  - q: "Can every PyTorch model run on the NPU?"
    a: >
      No. The NPU supports a subset of operators — exotic layers, custom CUDA ops, and some dynamic-shape patterns fall back to CPU or fail. Exporting the model to ONNX and simplifying the graph is the standard way to get clean, fully-NPU execution.
  - q: "Is torch-directml slower than CPU for small models?"
    a: >
      Often, yes. The NPU pays a fixed cost to move data and compile the graph, so tiny models can finish faster on the CPU. The NPU wins on sustained, batched inference — always benchmark your real workload rather than a single forward pass.
---

You installed torch-directml, moved your model to the DML device — and inference is still slow, Task Manager shows the CPU doing all the work, and the NPU sits at 0%. Nothing errored out, which makes it worse: PyTorch silently fell back to CPU (or parked your model on the integrated GPU) and never told you. On Windows AI PCs this is the normal failure mode, not an exception.

The reason is that PyTorch has no native NPU backend on Windows. The NPU is reached through DirectML, which exposes every DirectX-capable device — NPU included — as a generic compute target. That abstraction is convenient but lossy: device selection is by index, not by name, and your iGPU is almost always enumerated first. Add unsupported operators, a mismatched Python architecture, or a stale DirectML runtime, and the framework quietly routes work anywhere except the neural processor.

This guide gives you six fixes in order: get the right Python and torch-directml build, enumerate devices and pin the NPU explicitly, verify the binding, clean up the model graph, remove system-level interference, and benchmark correctly so you know the NPU is genuinely doing the work.

## Why this happens

- **torch-directml missing or wrong build:** Without the matching package, the DML device silently resolves to CPU.
- **Wrong DirectX device index:** The iGPU is enumerated first on most laptops, so unqualified selection lands on the GPU, not the NPU.
- **Unsupported operators fall back to CPU:** Custom ops and dynamic shapes have no NPU kernel — the runtime quietly runs them on the CPU.
- **x64 Python under emulation:** Emulated interpreters on Snapdragon machines add overhead and can break DirectML binding entirely.
- **Stale DirectML runtime:** An outdated DirectML stack can fail NPU binding with no clear error message.
- **Background interference:** Antivirus scans and background AI workloads skew timings so badly a working NPU looks broken.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install native ARM64 Python and the matching torch-directml

Most NPU failures start at install time. On Snapdragon Copilot+ PCs, x64 Python runs under Prism emulation, and while torch-directml may import, its device binding through the emulated layer is unreliable — enumeration can miss the NPU or crash mid-session. The fix is a native ARM64 Python with ARM64 wheels of torch and torch-directml whose versions match. A version mismatch is the second classic trap: the DirectML plugin is built against specific torch ABIs, and a mismatch produces import errors or silent CPU fallback. Pin both explicitly.

1. On Snapdragon, replace x64 Python with a native ARM64 Python 3.10+ build.
2. Create a fresh virtual environment so no stale x64 packages leak in.
3. Install torch, then the torch-directml build matching your torch version exactly.
4. Run `python -c "import torch_directml; print(torch_directml.device_count())"` — expect 2+.
5. If the import fails, check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for DirectML requirements.

### Fix 2: Enumerate devices and pin the NPU explicitly

Never trust the default device. torch-directml numbers every DirectX device from 0, and on virtually all AI-PC laptops the integrated GPU is device 0 while the NPU is device 1 or later. Code that grabs device 0 "because DirectML is installed" runs on the iGPU — faster than CPU, but not the NPU. Explicit enumeration takes five lines and removes all ambiguity: print each device's name, find the NPU, and bind your model to that index only. Skipping this step is the most common reason NPU benchmarks accidentally measure the iGPU instead.

1. Loop `torch_directml.device(i)` per index and print `torch_directml.device_name(i)`.
2. Find the index whose name contains NPU — commonly 1, but verify.
3. Create the device with that exact index in your code.
4. Move both model and inputs with `.to(dml_device)` — inputs left on CPU force copies.
5. Log the active device name at startup so silent fallback can't hide.

### Fix 3: Verify the binding with a real probe

A device name in a log line is not proof of NPU execution — the runtime can still spill unsupported ops to the CPU behind your back. Verify with two independent signals: Task Manager's NPU utilization graph during inference, and timing comparisons across devices. Run the same forward pass on CPU, iGPU, and NPU with proper warmup. If the NPU run matches the CPU run's speed, the graph is falling back. Cross-check with dedicated [NPU benchmark tools for Windows](/articles/npu-benchmark-tools-windows/): if a purpose-built benchmark lights up the NPU but your script doesn't, the problem is your code.

1. Watch Task Manager's NPU graph while your script runs.
2. Time 50 warmed-up forward passes on CPU, then 50 on the NPU device.
3. Confirm sustained NPU activity during the NPU runs.
4. If utilization is zero, simplify the model (Fix 4).
5. Record the numbers — you'll need this baseline for Fix 6.

### Fix 4: Clean the model graph for NPU-compatible ops

The NPU executes a subset of operators. Custom CUDA extensions, dynamic-shape patterns, and exotic normalization layers have no NPU kernels, so the runtime either errors or silently runs those subgraphs on the CPU — dragging performance back to CPU levels. The professional fix is exporting to ONNX and running through ONNX Runtime with the DirectML provider: the exporter surfaces unsupported ops as explicit errors at conversion time rather than silent fallbacks at runtime, and the resulting graph is exactly what the NPU executes.

1. Export with `torch.onnx.export` using a fixed input shape and recent opset.
2. Read the export log — every unsupported-op warning is a CPU trap.
3. Replace flagged layers with standard equivalents (standard LayerNorm, static shapes).
4. Validate the ONNX graph with onnxruntime and the DML provider.
5. Keep the export script — rerun it every time the model changes.

### Fix 5: Remove system-level interference

Sometimes the NPU works and the measurements lie. Real-time antivirus scanning of your Python environment and model files can add hundreds of milliseconds per run — enough to make NPU and CPU timings indistinguishable — so exclude your project folders or follow the [Defender performance tuning steps for ARM laptops](/articles/defender-arm-laptop-performance/). I/O misleads too: loading multi-gigabyte weights from an external SSD over a flaky link makes every run look slow regardless of device, and [Thunderbolt 5 connection issues on Intel AI PCs](/articles/thunderbolt-5-not-working-intel-ai-pc/) cause exactly that. Isolate compute from I/O before concluding anything.

1. Add your venv and model directories to the antivirus exclusion list.
2. Copy weights to the internal SSD and rerun timings.
3. Close background apps, especially anything doing its own AI inference.
4. Set Best performance power mode and plug in the charger.
5. Re-run the Fix 3 probe against your earlier baseline.

### Fix 6: Benchmark correctly and accept the NPU's real profile

The final trap is methodology. The NPU pays fixed costs — graph compilation on first run, host-to-device transfers — that dominate short benchmarks, so a single forward pass "proves" the CPU is faster. Correct benchmarking means warmup runs, realistic batch sizes, and sustained throughput measurement, where the NPU's efficiency advantage appears. Set expectations honestly: for tiny models and batch-size-1 latency, the CPU or iGPU may genuinely win. On Intel systems, [Intel's driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) can confirm the driver stack — then trust the numbers.

1. Add at least 10 warmup iterations before timing.
2. Measure sustained throughput over 60+ seconds, not single-pass latency.
3. Test batch sizes 1, 8, and 32 — the NPU's edge grows with batch size.
4. Compare NPU vs CPU vs iGPU on the identical workload.
5. Document the winning setup in your README for next time.

## Closing

PyTorch ignores the NPU for boring, fixable reasons: the wrong Python build, an unpinned device index, unsupported ops silently falling back, or interference skewing measurements. Install native, pin the NPU explicitly, clean the graph via ONNX, and benchmark honestly — then the NPU does the work you bought it for.
