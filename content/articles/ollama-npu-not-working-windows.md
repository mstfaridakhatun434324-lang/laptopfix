---
title: "How to Fix Ollama NPU Not Working on Windows 11"
slug: ollama-npu-not-working-windows
date: 2026-10-23
categories: ["ai-pc"]
tags: ["ollama", "npu", "windows 11", "llm", "copilot+ pc", "troubleshooting"]
description: "Fix Ollama not using your NPU on Windows 11 with step-by-step checks for NPU drivers, runtime support, model configuration, and hardware compatibility."
thumbnail: "/images/thumbs/ollama-npu-not-working-windows.webp"
faqs:
  - q: "Does Ollama support NPUs on Windows 11?"
    a: "Out of the box, Ollama primarily targets CPU and GPU (CUDA/ROCm) execution — NPU offload on Windows depends on your chip vendor's runtime and experimental builds. Check Ollama's release notes for your specific NPU before assuming support exists."
  - q: "Why does Ollama only use my CPU on a Copilot+ PC?"
    a: "Because Ollama defaults to CPU execution when it cannot find a supported GPU or NPU backend. On Snapdragon, Intel Core Ultra, and AMD Ryzen AI laptops, you need the vendor's NPU driver stack and a compatible Ollama build for anything other than CPU inference."
  - q: "Which NPU works best with Ollama on Windows?"
    a: "Support varies by vendor and changes fast. Intel Core Ultra (via OpenVINO) and Qualcomm Snapdragon (via the Qualcomm AI Stack) have the most documented paths; AMD Ryzen AI support trails. Always verify against the current Ollama documentation for your exact chip."
  - q: "Is running LLMs on the NPU faster than CPU?"
    a: "For supported models and precisions, NPU offload can be significantly more power-efficient and sometimes faster than CPU inference, especially for sustained chat sessions on battery. But an unsupported configuration silently falling back to CPU is the most common 'not working' report."
---

You installed Ollama on your shiny Copilot+ PC expecting local LLMs to fly on the 40+ TOPS NPU — but `ollama run` pins the CPU at 100%, the NPU sits at 0% in Task Manager, and tokens trickle out at CPU speed. The NPU is right there in Device Manager, Windows itself uses it for Recall and Live Captions, yet Ollama ignores it completely.

Ollama was built around CPU and discrete-GPU execution, and NPU support on Windows is a patchwork of vendor runtimes, experimental builds, and model-format constraints. "Not working" usually means the NPU backend was never available — Ollama just fell back to CPU silently.

This guide gives you six fixes in technician order: verify what your hardware can actually do, fix the driver and runtime layer, then configure Ollama correctly. Work through them in sequence and check Task Manager's NPU graph after each change.

## Why this happens

- **Ollama defaults to CPU when no supported accelerator is found:** If the NPU backend is missing or incompatible, Ollama silently runs on CPU — there is no error, just slow tokens and a idle NPU.
- **Missing or outdated NPU driver stack:** Each vendor needs its own stack — Intel's NPU driver, AMD's Ryzen AI software, or Qualcomm's AI Stack. Without it, no application can touch the NPU.
- **No NPU execution provider in your Ollama build:** Standard Ollama releases target CUDA/ROCm/CPU. NPU execution needs vendor-specific builds or plugins (such as OpenVINO-based paths) that you must install deliberately.
- **Model format incompatible with the NPU:** NPUs typically need quantized models in specific formats. A GGUF model tuned for CPU will not magically run on the NPU even with the right drivers.
- **Windows AI component mismatch:** Features like the Windows Copilot Runtime mediate NPU access for some apps; a broken or outdated runtime can block third-party NPU access too.
- **Wrong expectations about which chip does what:** On laptops with both an NPU and a discrete GPU, Ollama may target the GPU backend and ignore the NPU entirely — "NPU not working" sometimes means "Ollama chose the GPU instead."

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your NPU is healthy in Windows first

Before blaming Ollama, prove the NPU itself works. If Windows cannot see or use the NPU, no application-level fix will help — and the repair path is drivers, not Ollama settings.

1. Open **Task Manager > Performance** and look for an **NPU** tab — its absence means Windows does not see the hardware at all.
2. Open **Device Manager > Neural processors** (or System devices) and confirm your NPU appears with no warning icon.
3. Run a built-in NPU workload — open **Settings > Bluetooth & devices > Cameras** and enable a Studio Effect, or turn on Live Captions — and watch the NPU graph move in Task Manager.
4. If the NPU tab is missing or the device shows an error, update the NPU/chipset driver from your laptop maker's support page (Dell, HP, or Lenovo) before continuing.
5. Only proceed once a Windows-native NPU workload demonstrably uses the hardware — as [Game Pass install failures on ARM laptops](/articles/game-pass-arm-laptop-install-failed/) show, the fix often lives below the app layer.

### Fix 2: Install the vendor NPU runtime Ollama needs

The bare driver is not enough — Ollama's NPU paths go through vendor SDKs, and this missing layer causes most "NPU not working" reports. Identify your chip and install its AI software stack.

1. Identify your chip: **Snapdragon X** (Qualcomm), **Intel Core Ultra** (Intel AI Boost NPU), or **AMD Ryzen AI** (XDNA NPU) via **Settings > System > About**.
2. For Intel, install the latest NPU driver and the OpenVINO runtime from [Intel's driver support page](https://www.intel.com/content/www/us/en/support/detect.html).
3. For AMD, install the Ryzen AI Software from [AMD's driver download page](https://www.amd.com/en/support/download/drivers.html).
4. For Snapdragon, install the Qualcomm AI Stack / neural processing SDK components from your laptop maker's support page, since Qualcomm distributes through OEMs.
5. Restart after installation and re-run the Task Manager NPU check from Fix 1 — the runtime install sometimes enables the Performance-tab graph itself.

### Fix 3: Use an Ollama build with NPU support

The standard Ollama installer from the website may not include an NPU execution path for your chip. Running the default build and expecting NPU offload is the most common configuration mistake.

1. Check Ollama's official documentation and GitHub releases for NPU support statements covering your exact chip — support lands per vendor, not all at once.
2. If a vendor-specific or experimental build exists for your NPU (for example, OpenVINO-enabled builds for Intel), install it instead of the default release.
3. Verify the installed version with `ollama --version` and compare against the release notes that mention NPU support.
4. Without an NPU backend, `ollama run` always uses CPU (or GPU) — no environment variable conjures NPU support the binary lacks.
5. NPU support moves fast — the build lacking it today may gain it next release, just as [HDR issues on ARM laptops](/articles/hdr-not-working-arm-laptop/) were fixed by a driver version alone.

### Fix 4: Configure the model and runtime for NPU execution

Even with the right build and drivers, the model itself must be NPU-friendly. A model in the wrong format or precision will fall back to CPU without any warning in the Ollama output.

1. Check the documentation for your NPU-enabled Ollama build to learn which model formats it accepts for NPU offload (quantization level and format matter).
2. Pull a model explicitly documented as NPU-compatible for your chip rather than assuming your existing GGUF library will transfer over.
3. Set any required environment variables or configuration flags the build documents for enabling the NPU execution provider — defaults usually mean CPU.
4. Run the model and watch **Task Manager > Performance > NPU** during generation: sustained NPU activity with lower CPU usage confirms offload is working.
5. If the NPU graph stays flat, check Ollama's server logs for execution-provider lines — they reveal whether the NPU backend loaded or was skipped.

### Fix 5: Rule out GPU-backend hijacking and resource contention

On machines with a discrete or integrated GPU alongside the NPU, Ollama may prefer the GPU backend — and Windows may reserve NPU capacity for its own features. Both look like "NPU not working" from the user's chair.

1. In Task Manager, check whether the **GPU** graph spikes during `ollama run` — if it does, Ollama chose the GPU backend, not the NPU.
2. Consult your build's docs for flags that force NPU execution or disable the GPU backend for testing.
3. Close other NPU workloads (Recall indexing, Live Captions, Studio Effects) while testing, since concurrent NPU users can throttle or block new sessions.
4. Windows AI features share the NPU with third-party apps — heavy Recall indexing during your test skews results, as with [Live Captions vs Teams captions](/articles/live-captions-vs-teams-captions/).
5. Re-test with a clean boot (minimal startup apps) if contention is suspected, then reintroduce apps one by one.

### Fix 6: Update Windows AI components and reset the stack

When drivers, runtime, build, and model are all correct but the NPU still idles, the Windows AI middleware itself may be broken. A servicing update plus a clean reinstall of Ollama clears the last layer of stale state.

1. Run **Settings > Windows Update** and install all pending updates, including optional driver updates — the Windows Copilot Runtime ships through servicing.
2. Uninstall Ollama completely, delete its model cache under your user profile if you want a truly clean slate (re-download models afterward), and reinstall the NPU-capable build.
3. Reinstall the vendor NPU runtime from Fix 2 on top, then restart — order matters, with the runtime going in before final testing.
4. Test with the smallest documented NPU-compatible model first; if the tiny model uses the NPU but your large one does not, the issue is model size or format, not the stack.
5. If nothing works, file an issue with Ollama including your chip model, driver versions, and logs — and check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for known NPU servicing issues on your Windows build.

## Closing

Ollama ignoring your NPU is almost always a missing layer, not a broken chip: the vendor runtime, an NPU-capable build, or an NPU-compatible model. Verify the NPU works in Windows first, install the right stack for your chip, match the build and model to it, and the tokens will finally flow through the silicon you paid for.
