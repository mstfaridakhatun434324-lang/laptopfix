---
title: "Phi Silica Not Working on Windows 11? How to Fix It"
slug: phi-silica-not-working-windows-11
date: 2026-10-21
categories: ["ai-pc"]
tags: ["phi silica", "on-device ai", "small language model", "npu", "ai pc", "troubleshooting"]
description: "Phi Silica not working on Windows 11? Discover why Microsoft's on-device small language model won't run and fix it with six proven step-by-step methods."
thumbnail: "/images/thumbs/phi-silica-not-working-windows-11.webp"
faqs:
  - q: "What is Phi Silica?"
    a: >
      Phi Silica is Microsoft's small language model designed to run entirely on your device's NPU. It powers on-device text features — rewriting, summarization, and similar tasks — without sending your data to the cloud. If it won't run, those features fall back to slower CPU processing or fail outright.
  - q: "Does Phi Silica require a specific NPU?"
    a: >
      It targets NPUs meeting Microsoft's Copilot+ performance bar — roughly 40+ TOPS. First check [your NPU's TOPS rating](/articles/how-to-check-npu-tops-windows-11/); hardware below the bar may not be offered the model at all.
  - q: "Is my data sent to Microsoft when Phi Silica runs?"
    a: >
      No — that's the point of on-device inference. The model runs locally on your NPU, so your text never leaves the machine for these features. A broken local model doesn't silently switch to cloud processing; the feature just fails.
  - q: "How big is the Phi Silica download?"
    a: >
      Several gigabytes, varying by version. The model must fully download and verify before anything works — an interrupted download is one of the most common reasons it "doesn't work" despite everything else looking fine.
---

Phi Silica is supposed to be invisible: Microsoft's small language model lives on your NPU, and apps just call it for on-device rewriting, summarization, and text smarts. But on some Windows 11 machines the magic never starts — the feature errors out, hangs, or quietly does nothing, and you're left wondering whether the model is missing, broken, or simply unsupported on your hardware.

The failure modes cluster into a few buckets: the model never downloaded, the NPU can't run it, the Windows build doesn't support it, or the app calling it is misconfigured. The symptom looks the same from the outside, so guessing wastes time.

This guide diagnoses properly with six fixes in technician order: verify your hardware qualifies, get the model onto the disk, repair the NPU layer, and fix the software calling it. Work them in sequence.

## Why this happens

- **Your NPU doesn't meet the bar:** Phi Silica targets Copilot+ class NPUs (around 40+ TOPS). Older or weaker NPUs may never be offered the model — the feature fails rather than running badly.
- **The model never finished downloading:** Multi-gigabyte model downloads interrupt easily. A partial download fails verification, and the feature reports a generic error instead of "download incomplete."
- **The NPU driver is unhealthy:** Phi Silica needs a working NPU driver. Warnings in Device Manager, or a driver that needs [an update before AI features work](/articles/studio-effects-driver-update-required/), will block the model from initializing.
- **Windows build too old:** On-device model support is tied to recent Windows 11 builds. An outdated build lacks the runtime the model needs.
- **Insufficient disk space or RAM:** The model needs gigabytes of disk for storage plus working memory at inference time. Constrained systems fail at load.
- **The calling app is misconfigured:** Sometimes Phi Silica itself is fine but the app's settings, permissions, or feature flags prevent it from invoking the model.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify your hardware actually qualifies

Don't troubleshoot software for a hardware shortfall. Confirm the NPU meets the requirement first.

1. [Check your NPU's TOPS rating](/articles/how-to-check-npu-tops-windows-11/) and confirm it's in Copilot+ territory (roughly 40+ TOPS).
2. In **Settings > System > About**, confirm you're running Windows 11 on a supported build — check with **winver**.
3. Look for your model on your maker's Copilot+ compatibility list; some "AI PCs" shipped before the Copilot+ program with weaker NPUs.
4. If the hardware qualifies, continue. If it doesn't, no software fix will conjure the model — the honest answer is that this feature needs Copilot+ class hardware.

### Fix 2: Confirm the model is fully downloaded and intact

A surprising number of "not working" cases are really "never finished downloading." Verify before touching drivers.

1. Open **Settings > System > Storage** and ensure at least 10 GB free on the system drive.
2. Trigger the feature that uses Phi Silica and let the machine sit on an unmetered connection — model downloads happen in the background and can take a while on slow links.
3. Check **Settings > Windows Update** for pending AI or optional updates; model delivery sometimes rides along with them.
4. If a previous attempt was interrupted, clear temporary and delivery-optimization files (**Settings > System > Storage > Temporary files**), restart, and let the download run to completion uninterrupted.

### Fix 3: Repair the NPU driver

Phi Silica initializes against the NPU driver. Any driver-level problem — warnings, stale versions, failed loads — stops the model cold.

1. In Device Manager, expand **Neural processors** and confirm the NPU shows no warning.
2. If there's a warning, fix it according to its code before continuing — a broken driver poisons everything above it.
3. Even without a warning, install the latest OEM NPU driver for your exact model; [driver updates are a routine prerequisite for AI features](/articles/studio-effects-driver-update-required/).
4. Verify with a quick NPU workload (Studio Effects background blur) that the driver genuinely works, not just that the warning cleared.

### Fix 4: Update Windows to a build that supports on-device models

The runtime Phi Silica needs ships with Windows itself. Running an older build is like having the engine but not the fuel lines.

1. Open **Settings > Windows Update**, install everything pending, and check **Advanced options > Optional updates**.
2. Restart and verify the new build with **winver**.
3. Retry the Phi Silica feature after the update completes — model downloads often trigger automatically on supported builds.
4. If you're already current, check [Microsoft's Windows support page](https://support.microsoft.com/en-us/windows) for any known issues with on-device AI on your specific build before going deeper.

### Fix 5: Check RAM, power, and thermal headroom

Inference needs working memory and a healthy power environment. Starved resources produce hangs and silent failures that look like model bugs.

1. Open Task Manager during a Phi Silica attempt and watch memory: if the system is paging heavily, close memory-hungry apps and retry.
2. Plug in the charger and set the power plan to **Best performance** temporarily — aggressive power saving can throttle the NPU mid-inference.
3. Ensure vents are clear; sustained AI workloads on a hot, throttled machine fail in confusing ways.
4. If [Recall's snapshot frequency settings](/articles/recall-snapshot-frequency-settings/) or other background AI features are maxed out, dial them back during testing — they compete for the same NPU.

### Fix 6: Repair the app and re-register the AI platform

When hardware, model, driver, and OS all check out, the fault is in the calling app or the platform registration — the last layer.

1. Open **Settings > Apps > Installed apps**, find the app using Phi Silica, open **Advanced options**, and use **Repair**; try **Reset** if Repair changes nothing.
2. In an elevated terminal, run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store the AI runtime depends on.
3. Check the app's own settings for AI or on-device toggles — some apps gate local models behind a setting that's off by default. [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) can also confirm your AI Boost driver is current on Core Ultra systems.
4. Restart, trigger the feature once more on a clean boot, and if it still fails, report it via **Feedback Hub** with your NPU model, driver version, Windows build, and the exact error text.

## Closing

Phi Silica failures are almost always one of four things: hardware below the bar, an incomplete model download, an unhealthy NPU driver, or an outdated Windows build. Verify qualification first, then work the stack from disk to driver to OS to app. When each layer checks out, the model initializes, inference stays on your device, and the feature works the way Microsoft advertised — fast, private, and offline-capable.
