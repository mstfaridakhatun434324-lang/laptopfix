---
title: "How to Fix AnythingLLM NPU Not Detected on Windows 11"
slug: anythingllm-npu-not-detected
date: 2026-10-23
categories: ["ai-pc"]
tags: ["anythingllm", "npu", "local ai", "windows 11", "copilot+ pc", "llm"]
description: "Fix AnythingLLM not detecting your NPU on Windows 11: step-by-step driver checks, provider settings, app updates, and fallback options for Copilot+ PCs."
thumbnail: "/images/thumbs/anythingllm-npu-not-detected.webp"
faqs:
  - q: "Why doesn't AnythingLLM see my NPU?"
    a: "The app can only use the NPU through Windows' AI stack, so a missing or generic NPU driver, an outdated AnythingLLM build, or the wrong provider selected in settings will all hide it. Confirm the NPU appears in Device Manager first, then check the app's provider settings."
  - q: "Does AnythingLLM require a specific model for NPU use?"
    a: "Yes. The local model must be in a format the NPU backend supports; an incompatible quantization makes the app silently fall back to CPU. Re-download a supported model from inside the app's model picker after updating."
  - q: "Can battery saver hide the NPU from apps?"
    a: "It can. Aggressive power modes park the NPU to save battery, and apps reading the hardware list at that moment see it as unavailable. Plug in the charger and set the power mode to Best performance before rechecking."
  - q: "Is my NPU broken if no app detects it?"
    a: "Almost certainly not. If the NPU is missing from Device Manager entirely, the driver package is the problem — reinstall the chipset and NPU drivers from your laptop maker. Hardware failure is rare; driver failure is common."
---

You installed AnythingLLM to chat with your documents privately on your Copilot+ PC, opened the settings expecting the NPU as a compute option, and found nothing — CPU only, maybe a grayed-out GPU entry. The 40-plus TOPS NPU your laptop was marketed for is invisible to the app, and every local model crawls on the processor instead.

On Windows 11 AI PCs, an application can only reach the NPU through the platform's AI stack. The NPU must appear in Device Manager under Neural processors, its driver must expose the Windows AI runtime, and AnythingLLM must be new enough to query that path with a local provider configured. Break any one of those links — a stale driver, an app defaulting to CPU, an incompatible model — and you get exactly this symptom: no NPU detected.

This guide walks through six fixes in order: confirming the NPU exists at the OS level, repairing its driver, updating AnythingLLM and choosing the right local provider, and setting a sane fallback. The same driver-first discipline also fixes [Miracast on Snapdragon laptops](/articles/miracast-not-working-snapdragon-laptop/), which depends on the same platform driver stack — when one piece goes stale, several features fail together.

## Why this happens

- **NPU driver missing or generic:** Windows loaded a basic driver that does not expose the AI runtime; the NPU may show a warning icon or not appear at all.
- **AnythingLLM build too old:** NPU hardware detection arrived in later releases; older versions only offer CPU.
- **Wrong provider selected:** the app points at a cloud provider or CPU-only local provider instead of the local model path the NPU can use.
- **Model incompatible with the NPU backend:** the downloaded model or quantization is not supported by the NPU path, so the app silently falls back to CPU.
- **Windows AI components outdated:** the OS-side ML runtime predates NPU support, or the enabling feature update was never installed.
- **Power mode parking the NPU:** battery saver or best-efficiency modes can park the NPU, so apps reading the hardware list see it as unavailable.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the NPU exists at the OS level

Before blaming AnythingLLM, prove the hardware is visible to Windows — if the OS cannot see the NPU, no application ever will. Open Device Manager and look for a "Neural processors" category: Hexagon on Qualcomm, AI Boost on Intel, Ryzen AI on AMD. Also check Task Manager's Performance tab, where a healthy NPU gets its own graph. If it is missing here, the next two fixes are where your problem lives — app settings are a distraction until the hardware shows up.

1. Open Device Manager and expand **Neural processors**; the NPU should list with no warning icon.
2. Open Task Manager > **Performance** and look for the **NPU** graph.
3. If the NPU is absent from both, note your model in **Settings > System > About** first.
4. On a warning icon, open Properties — the device status names the missing driver.
5. Change no AnythingLLM setting until the NPU is visible here.

### Fix 2: Reinstall the NPU and chipset drivers

A visible-but-broken NPU is a driver problem, and NPU drivers ship inside the platform package from your laptop maker or chip vendor — never through AnythingLLM itself. On Intel machines the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the AI Boost driver; on AMD the [AMD driver page](https://www.amd.com/en/support/download/drivers.html) covers Ryzen AI; on Snapdragon the OEM package is the only source. Install the full chipset package, not just the NPU entry, because the runtime libraries that expose the NPU to apps travel with it.

1. Download the latest chipset and NPU package for your exact model, or run the Intel/AMD detector above.
2. Install as administrator without sleep or interruption.
3. Restart, then recheck Device Manager — the warning icon should be gone.
4. Confirm the NPU graph appears in Task Manager > Performance.
5. If Windows Update later downgrades it, check [Microsoft’s Windows support pages](https://support.microsoft.com/en-us/windows) for how to pin the working version.

### Fix 3: Update AnythingLLM and select the local provider

With the NPU healthy at the OS level, turn to the app itself. AnythingLLM’s NPU awareness arrived in newer builds, and the provider setting decides which compute path the app even attempts — a workspace pointed at a cloud provider will never touch your NPU no matter how healthy it is. Update to the latest release first, then make sure the workspace uses the local provider and the hardware preference names the NPU. Save the settings, quit the app fully, and relaunch so the new provider initializes from scratch.

1. In AnythingLLM **Settings**, check for updates; install the latest release and restart.
2. Set the model provider to the **local** provider option, not any cloud provider.
3. In the local-model settings, set the hardware preference to NPU (or Auto).
4. Save, fully quit the app, and relaunch.
5. Reopen settings and verify the NPU appears as an available device.

### Fix 4: Download an NPU-compatible model

Even with the NPU detected, an incompatible model silently drops you back to CPU — the most misleading failure in this chain, because everything looks configured correctly. The NPU backend supports specific model formats and quantizations, and a model downloaded for generic CPU use may not qualify. Remove the current local model and re-download one explicitly marked as NPU-compatible from inside the app’s model picker, starting with a smaller model to validate quickly. Watch the app’s status or logs during load — it should name the NPU as the execution device.

1. In model settings, note the current model, then remove it.
2. Open the model picker and choose one labeled NPU-compatible for your platform.
3. Prefer a smaller model first (3B/7B) to validate the pipeline quickly.
4. Let the download finish completely; partial downloads can also force CPU fallback.
5. Load the model; the app’s status should name the NPU as execution device.

### Fix 5: Check power mode and Windows updates

Two environmental traps remain. Battery saver and best-efficiency power modes park the NPU, and an app that enumerates hardware while it is parked concludes there is no NPU. Separately, the Windows AI runtime components that expose the NPU to apps arrive through Windows Update — a machine months behind on updates may simply lack the OS side of the contract. Note that local-model NPU issues are unrelated to cloud streaming performance; if your cloud apps stutter too, that is a different fix, covered in [Xbox Cloud Gaming lag on ARM laptops](/articles/xbox-cloud-gaming-arm-laptop-lag/).

1. Plug in the charger; set **Power & battery > Power mode** to **Best performance**.
2. Turn off Battery saver, including its automatic threshold.
3. Run Windows Update, install everything offered, then restart.
4. Relaunch AnythingLLM and recheck the device list on AC power.
5. NPU visible on AC but not battery is power policy — treat it as by design.

### Fix 6: Reset the app and set a sane fallback

If the NPU is healthy in Device Manager, the app is current, the model is compatible, and power is fine — yet detection still fails — the app's own configuration is corrupt. AnythingLLM keeps provider and device state in its local data folder, and a stale entry there can pin the app to CPU forever. A clean reset is faster than auditing the config file by file, and it also lets you deliberately choose the best fallback: GPU first, CPU last.

1. Back up documents and chat history (locations are in the app’s settings).
2. Uninstall AnythingLLM, then delete its leftover data folder.
3. Reinstall the latest build; launch once before changing any setting.
4. Configure the local provider from scratch before restoring documents.
5. If the NPU still refuses, set the device to GPU — a capable fallback on most Copilot+ PCs.

## Closing

An undetected NPU in AnythingLLM is a chain problem — OS visibility, driver, app version, provider choice, model compatibility, power — and the fix is whichever link is broken. Verify the NPU in Device Manager first, repair the driver second, and only then touch the app’s settings. If Windows’ own AI entry points are missing too — say the [Copilot app is missing from Start menu search](/articles/copilot-app-missing-start-menu-search/) — the Windows AI component install itself is the problem.
