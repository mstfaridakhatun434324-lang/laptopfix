---
title: "ONNX Runtime DirectML Falls Back to CPU: Force NPU Execution on Windows 11"
slug: onnxruntime-directml-fallback-cpu
date: 2026-10-22
categories: ["ai-pc"]
tags: ["onnx","directml","npu","cpu-fallback","windows-11","troubleshooting"]
description: "ONNX Runtime keeps falling back to CPU instead of using DirectML with your NPU? Diagnose the fallback and force NPU execution with these proven fixes."
thumbnail: "/images/thumbs/onnxruntime-directml-fallback-cpu.webp"
faqs:
  - q: "What does DirectML fallback to CPU mean?"
    a: >
      ONNX Runtime tries execution providers in priority order. When the
      DirectML provider cannot run a model on the NPU or GPU — missing
      driver, unsupported operator, or provider load failure — it silently
      falls back to the CPU provider. Inference still works, but much more
      slowly and with higher power draw.
  - q: "How can I tell which provider ONNX Runtime is actually using?"
    a: >
      Enable verbose logging in your app or check its logs for the
      provider list. Many apps print lines like "Using DMLExecutionProvider"
      or fall back messages. Profiling tools and Task Manager (NPU/GPU
      activity during inference) also reveal where the work runs.
  - q: "Does fallback happen because my model is incompatible?"
    a: >
      Sometimes. Operators the DirectML provider does not support force
      those nodes — or the whole model — onto the CPU. But driver
      problems, an outdated DirectML runtime, or a misconfigured provider
      list cause fallback even for fully supported models.
  - q: "Will forcing the NPU break my application?"
    a: >
      If the model genuinely needs unsupported operators, forcing NPU-only
      execution can throw errors instead of silently slowing down. The
      right approach is diagnosing why fallback happens, then fixing the
      driver or model — not blindly disabling the CPU provider.
---

You built or installed an AI app that should fly on your laptop's NPU, but inference is slow, the fan spins up, and Task Manager shows the CPU doing all the work while the NPU sits idle. Somewhere in the stack, ONNX Runtime tried the DirectML execution provider, failed, and quietly fell back to the CPU. The app still produces correct results, which makes this failure mode insidious: everything "works", just five to twenty times slower than it should, and your battery pays the difference.

ONNX Runtime's provider fallback is by design — it prefers a slow correct answer over a crash. But chronic fallback means your AI PC is not actually an AI PC for that workload. The causes split into three buckets: the DirectML provider cannot load at all (driver or runtime problems), the provider loads but rejects the model (unsupported operators or shapes), or the app never asked for DirectML properly in the first place. Readers who hit the [ONNX Runtime NPU execution provider error](/articles/onnx-runtime-npu-execution-provider-error/) saw the loud version of this; fallback is the quiet version. Related reading on [DirectML not using the NPU at all](/articles/directml-not-using-npu-windows-11/) and [OpenVINO failing to detect the NPU](/articles/openvino-npu-not-detected-windows/) covers the neighboring stacks.

Fixing fallback restores the performance your hardware was bought for — and the features built on local inference, from [Studio Effects on external webcams](/articles/studio-effects-external-webcam-issues/) to the [Click to Do sparkle icon pipeline](/articles/click-to-do-sparkle-icon-missing/), all assume the NPU path actually works. Diagnose first, then act.

## Why this happens

- **NPU driver broken or missing:** If the NPU driver fails to load, DirectML has no device to target and ONNX Runtime falls back to CPU.
- **Outdated DirectML runtime:** Old DirectML versions lack NPU operator support or the device enumeration logic newer drivers expect.
- **Unsupported operators in the model:** Nodes using operators DirectML cannot execute force per-node or whole-graph fallback to CPU.
- **Provider priority misconfiguration:** Apps that list providers in the wrong order, or omit the DirectML provider entirely, never attempt NPU execution.
- **Wrong ONNX Runtime build:** The DirectML execution provider ships in specific builds; a CPU-only package cannot use DirectML no matter the hardware.
- **GPU/NPU contention or power state:** If the target device is asleep, busy, or in a low-power state, session creation can fail and trigger fallback.
- **Mismatched DirectX/DirectML versions:** A stale DirectX runtime or missing platform update can break the DirectML device creation path.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Confirm fallback is actually happening

Do not optimize blindly. Prove the CPU is doing the work and the NPU is idle before changing anything.

1. Run your AI workload and open Task Manager > Performance; watch the CPU, GPU, and NPU tiles during inference.
2. If the CPU spikes while NPU stays at 0%, fallback is confirmed; note the CPU utilization percentage as your baseline.
3. Check the application's logs or console output for provider messages mentioning DMLExecutionProvider, CPUExecutionProvider, or fallback warnings.
4. If the app has a settings page, look for an inference device or execution provider option and note its current value.
5. Record model name, ONNX Runtime version, and timing per inference — you will compare against these after each fix.

### Fix 2: Repair the NPU driver underneath DirectML

DirectML talks to the NPU through the driver. A driver that Device Manager shows as healthy can still fail DirectML device creation, so reinstall it cleanly.

1. Open Device Manager and check the NPU entry for warnings; note the driver version.
2. Download the latest NPU driver from your laptop maker or the chip vendor ([Intel](https://www.intel.com/content/www/us/en/support/detect.html), [AMD](https://www.amd.com/en/support/download/drivers.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx) for GPU DirectML paths).
3. Uninstall the current NPU device with "Attempt to remove the driver" checked, restart, then install the fresh package.
4. Verify the NPU appears in Task Manager > Performance after reboot.
5. Rerun the workload and check whether the NPU tile now shows activity during inference.

### Fix 3: Update ONNX Runtime and the DirectML provider package

Provider fallback is frequently fixed by newer builds — operator coverage expands every release, and NPU enumeration bugs get patched.

1. Check which ONNX Runtime version your app bundles (often in About, logs, or the Python package list via `pip show onnxruntime-directml`).
2. If you control the environment, upgrade to the latest `onnxruntime-directml` release matching your Python and OS.
3. Ensure the DirectML provider package is actually installed — the plain `onnxruntime` CPU package cannot use DirectML.
4. After upgrading, rerun the workload and compare inference timing against your Fix 1 baseline.
5. If the app bundles its own runtime and cannot be upgraded, check the vendor's release notes for a version that fixes NPU fallback.

### Fix 4: Set the provider list explicitly in code or config

Many fallback cases are simply misconfiguration: the app never requests DirectML, or requests it after the CPU provider. Put DirectML first.

1. In your code, pass providers explicitly: `ort.InferenceSession(model, providers=['DmlExecutionProvider', 'CPUExecutionProvider'])`.
2. Verify the provider order — ONNX Runtime tries them left to right, so DirectML must come before CPU.
3. For apps you did not write, look for a config file, environment variable, or settings UI controlling the inference provider.
4. Test with verbose logging enabled (`ort.set_default_logger_severity(0)`) to see exactly which provider each node uses.
5. Confirm in the logs that the session reports DmlExecutionProvider active and NPU activity appears in Task Manager.

### Fix 5: Identify and work around unsupported operators

If the provider loads but the model still falls back, unsupported operators are the likely cause. Find them and handle them deliberately.

1. Run the model through ONNX Runtime with verbose logging and look for messages about unsupported ops or nodes assigned to CPU.
2. Use Netron or the ONNX checker to inspect which operators the model uses, especially custom or very new ones.
3. Options: replace unsupported ops with equivalent supported ones, split the model so only supported subgraphs run on NPU, or accept partial fallback for a few nodes.
4. Consider converting or re-exporting the model targeting opset versions with better DirectML coverage.
5. Re-test after each model change and measure how much of the graph now executes on the NPU versus CPU.

### Fix 6: Update Windows, DirectX, and platform components

The DirectML device path depends on OS-level pieces. A fully updated Windows 11 has the newest DirectML runtime and NPU enumeration support.

1. Open Settings > Windows Update, install all updates including optional driver updates, and restart.
2. Visit [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) to confirm you are on a supported build; upgrade if you are far behind.
3. Reinstall the NPU driver once more after major OS updates, since build upgrades can reset driver state.
4. Rerun the workload end-to-end and compare timing and NPU utilization against your original baseline.
5. If fallback persists only for one specific app, report it to the app vendor with your logs — the bug may be in their provider configuration, and features like [Studio Effects on external webcams](/articles/studio-effects-external-webcam-issues/) or the [Click to Do sparkle icon](/articles/click-to-do-sparkle-icon-missing/) can help confirm whether system-wide NPU inference is healthy.

## Closing

ONNX Runtime falls back to the CPU when DirectML cannot load, cannot handle the model, or was never asked properly. Work the diagnosis chain: confirm the fallback, repair the NPU driver, update the runtime, set provider priority explicitly, handle unsupported operators, and keep Windows itself current. Each step either fixes the problem or narrows it to the next layer. Once DirectML holds onto the NPU, inference speeds up dramatically, the fan calms down, and everything built on local models — including [Studio Effects with external webcams](/articles/studio-effects-external-webcam-issues/) and [Click to Do's sparkle icon features](/articles/click-to-do-sparkle-icon-missing/) — finally runs on the hardware it was designed for.
