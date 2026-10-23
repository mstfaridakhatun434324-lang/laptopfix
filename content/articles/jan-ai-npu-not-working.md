---
title: "How to Fix Jan AI NPU Not Working on Windows 11"
slug: jan-ai-npu-not-working
date: 2026-10-23
categories: ["ai-pc"]
tags: ["jan ai", "npu", "windows 11", "local llm", "copilot+ pc", "offline ai"]
description: "Fix Jan AI NPU acceleration not working on Windows 11 with driver verification, engine settings, clean reinstall steps, and model compatibility checks."
thumbnail: "/images/thumbs/jan-ai-npu-not-working.webp"
faqs:
  - q: "Why doesn't Jan detect my NPU on Windows 11?"
    a: "Jan reaches the NPU through the Windows AI stack, so a missing or generic NPU driver, an outdated Jan build, or the wrong local engine selected in settings will all hide it. Verify the NPU in Device Manager before adjusting the app."
  - q: "Which Jan engine should I use for NPU acceleration?"
    a: "Use the local engine build that supports your platform's NPU path, with a model in a compatible format. If the engine keeps falling back to CPU, re-download a supported model and check the hardware settings after updating Jan."
  - q: "Does Jan work on battery power with the NPU?"
    a: "Often poorly. Battery saver and best-efficiency power modes park the NPU, so Jan may fall back to CPU or report the NPU as unavailable. Plug in the charger and set Best performance mode when testing NPU acceleration."
  - q: "Should I reinstall Jan if the NPU still won't engage?"
    a: "Yes, as a later step. A clean reinstall clears stale engine and device configuration that can pin Jan to CPU. Back up your models and threads first, then reinstall the latest build and configure the hardware settings from scratch."
---

Jan is the open-source, offline-first ChatGPT alternative that runs language models entirely on your machine — no account, no cloud. On a Copilot+ PC that should mean the NPU handling inference while your documents stay local. Instead, many users find Jan ignoring the NPU completely: the hardware setting shows CPU, downloads crawl through the processor, and Task Manager's NPU graph never moves.

The reason is a chain of dependencies. Jan's local engine can only use the NPU that Windows exposes through its AI runtime — which requires a healthy NPU in Device Manager and a current driver — and then the right engine build, a compatible model format, and a clean hardware setting have to line up inside the app. Any broken link quietly drops you to CPU inference, and Jan does not always say which link failed.

This guide works through six fixes in order: verifying the NPU at the OS level, repairing the driver, updating Jan and configuring its engine, and handling models and power. Jan relies on OS-level hardware access the way other third-party hardware integrations do — [Wacom tablet drivers on ARM Windows](/articles/wacom-tablet-driver-arm-windows/) show the same pattern of driver-version sensitivity — so driver hygiene comes before app tweaks.

## Why this happens

- **NPU driver missing or generic:** Windows loaded a basic driver that does not expose the AI runtime, so Jan's hardware scan finds no NPU to offer.
- **Jan build too old:** NPU hardware support arrived in later releases; older builds only enumerate CPU and GPU.
- **Wrong local engine selected:** Jan supports multiple local engines, and only the current engine build for your platform queries the NPU path.
- **Incompatible model format:** the downloaded model's quantization is not supported by the NPU backend, forcing a silent fallback to CPU.
- **Stale hardware setting:** a previous CPU selection stored in Jan's configuration keeps applying even after the NPU becomes available.
- **Power mode parking the NPU:** battery saver can park the NPU, and Jan reading the hardware list at that moment sees it as unavailable.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the NPU is visible to Windows

Jan cannot use hardware that Windows does not expose, so start below the app. Open Device Manager and confirm the “Neural processors” category lists your NPU — Hexagon on Snapdragon, AI Boost on Intel, Ryzen AI on AMD — with no warning icon. Then check Task Manager’s Performance tab for the NPU graph. If either check fails, the driver is your fix, and every Jan setting is a distraction until the hardware shows up in both places. Verify first, configure later.

1. In Device Manager, expand **Neural processors**; confirm the NPU lists with no warning icon.
2. In Task Manager > **Performance**, look for the **NPU** graph.
3. If the NPU is missing, note your model from **Settings > System > About** first.
4. On a warning icon, open Properties and read the device status message.
5. Change no Jan setting until the NPU passes both checks.

### Fix 2: Reinstall the NPU and chipset drivers

NPU drivers arrive inside the platform package from your laptop maker or chip vendor, and Jan is particularly sensitive to the driver version because it queries the hardware path directly. On Intel, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the AI Boost driver; on AMD, the [AMD driver page](https://www.amd.com/en/support/download/drivers.html) covers Ryzen AI; on Snapdragon, only the OEM package applies. This is the same platform-driver discipline that fixes [spatial audio on Windows 11 ARM](/articles/spatial-audio-not-working-windows-11-arm/) — one stale package, several broken features.

1. Download the latest chipset and NPU package for your exact model, or run the Intel/AMD detector above.
2. Install as administrator; let it finish without sleep or interruption.
3. Restart, then recheck Device Manager for a clean NPU entry.
4. Confirm the NPU graph appears in Task Manager > Performance.
5. If Windows Update later downgrades it, check [Microsoft’s Windows support pages](https://support.microsoft.com/en-us/windows) for how to pin the working version.

### Fix 3: Update Jan and configure the local engine

With the hardware healthy, update the app and point it at the right engine. Jan’s NPU support lives in current builds and in the local engine configuration — an outdated app or a mismatched engine selection keeps offering CPU regardless of the driver. Update first, then open the hardware settings and explicitly choose the NPU-capable engine and device instead of trusting the defaults to sort it out. Save, quit Jan completely, and relaunch so the engine initializes against the new setting.

1. In Jan, check for updates; install the latest release, then fully quit and relaunch.
2. Open **Settings** and choose the current local engine build for your platform.
3. Set the hardware or device preference to **NPU** explicitly, not Auto or CPU.
4. Save, quit Jan completely, and relaunch so the engine initializes fresh.
5. Reopen settings and confirm the NPU selection persisted.

### Fix 4: Download a model the NPU backend supports

The most misleading failure: the NPU is detected and selected, yet inference runs on CPU because the model’s quantization is not supported by the NPU backend. Jan will not always warn you — it just does the safe thing and computes on the processor. Remove the current model and download one explicitly marked as NPU-compatible from inside Jan’s model hub, starting small to validate the pipeline before committing to a large download. Then start a chat and watch the NPU graph — it should show activity during generation.

1. In Jan’s model hub, note the current model, then remove it.
2. Download a model labeled NPU-compatible for your platform.
3. Start with a smaller model so the download and first load are quick tests.
4. Wait for the download to finish completely — partial files can force CPU fallback.
5. Start a chat and watch Task Manager’s NPU graph during generation.

### Fix 5: Rule out power and thermal throttling

Two environmental factors can keep a healthy NPU idle. Battery saver and best-efficiency modes park the NPU, and sustained thermal throttling on a thin laptop can do the same under load — Jan then reads “unavailable” and falls back to CPU. On company-managed machines there is a third possibility: device policy restricting hardware access, the same class of restriction behind [Autopilot provisioning failures on ARM laptops](/articles/autopilot-arm-laptop-provisioning-failed/). Test on AC power first to isolate the variable. If the NPU works plugged in but not on battery, that is power policy rather than a defect.

1. Plug in the charger; set **Power & battery > Power mode** to **Best performance**.
2. Turn off Battery saver entirely, including its automatic threshold.
3. Keep vents clear and the laptop on a hard surface — throttling mimics a missing NPU.
4. Run Windows Update, install everything offered, then restart.
5. Retest Jan on AC power before investigating further.

### Fix 6: Clean-reinstall Jan and rebuild the configuration

If the NPU is healthy, Jan is current, the engine is right, the model is compatible, and power is fine — yet the NPU still will not engage — the app’s stored configuration is corrupt. Jan keeps engine, device, and model state in its per-user data, and a stale entry can pin it to CPU permanently. A clean reinstall is faster than auditing those files by hand, and it forces every hardware choice to be made fresh against the now-healthy driver.

1. Back up your threads; note downloaded models and settings.
2. Uninstall Jan, then delete its leftover per-user data folder.
3. Install the latest build; launch once before changing anything.
4. Configure the engine and NPU device explicitly, download a compatible model, and test.
5. Reintroduce old models one at a time — the one that breaks NPU use was incompatible.

## Closing

Jan ignoring your NPU is a chain problem — OS visibility, driver version, app build, engine selection, model compatibility, power, and stored configuration, in that order. Verify the NPU in Device Manager first, repair the driver second, and only then configure the app. Work the chain methodically and the NPU graph finally moves.
