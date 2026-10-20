---
title: "How to Fix NPU Stuck at 0% Usage on Your AI PC Laptop"
slug: npu-stuck-at-zero-percent-usage
date: 2026-10-20
categories: ["ai-pc"]
tags: ["npu 0 percent usage", "npu not used", "npu stuck", "troubleshooting", "ai pc", "task manager"]
description: "Fix your NPU stuck at 0% usage on your AI PC laptop — find why apps ignore the neural processor and get AI workloads running on the right chip again today."
thumbnail: "/images/thumbs/npu-stuck-at-zero-percent-usage.webp"
faqs:
  - q: "Why is my NPU at 0% while AI features run?"
    a: "Usually no app is actually sending work to the NPU — many AI features silently fall back to the CPU or GPU. A flat 0% during a guaranteed NPU task, however, signals a routing problem: the driver, the app, or Windows is not dispatching work to the chip."
  - q: "Should the NPU show usage all the time?"
    a: "No. The NPU idles at 0% by design and only spikes during AI workloads like background blur, live captions, or Recall indexing. Worry only when usage stays at zero while you are actively using a feature that should use the NPU."
  - q: "How do I confirm an app is supposed to use the NPU?"
    a: "Check the app's documentation or settings for NPU, DirectML, or AI acceleration options. Windows Studio Effects, live captions, and Recall are the built-in features guaranteed to target the NPU when it is healthy."
  - q: "Can a driver reinstall fix 0% NPU usage?"
    a: "Yes, if the cause is a corrupt driver or a broken DirectML routing layer. A clean reinstall of the OEM NPU and chipset drivers restores the dispatch path. If usage stays flat afterward, the issue is usually app-side."
---

You bought an AI PC for its neural processor, you open Task Manager's Performance tab, and there it sits: NPU, 0% — while fans spin up running an AI workload on the CPU. That flatline is frustrating because the chip is present, the driver looks healthy, and yet nothing reaches it.

A stuck-at-zero NPU usually means one of two things: no workload is being sent to it (apps quietly falling back to CPU or GPU), or the dispatch path between Windows and the chip is broken (driver, DirectML, or scheduling issue). The fixes differ completely, so this guide starts with diagnosis.

Work through these six methods in order — diagnose first, then act — and you will know whether your NPU needs a driver fix, a settings change, or simply a workload that targets it.

## Why this happens

- **No NPU-aware workload running:** Most apps never touch the NPU. If nothing you run uses DirectML or the Windows AI APIs, 0% is the expected reading.
- **App falling back to CPU/GPU:** Many apps probe for the NPU once and silently fall back if the probe fails — one failed initialization can park the app on the CPU permanently.
- **Corrupt NPU or chipset driver:** A damaged driver can report healthy in Device Manager while its compute path is broken, so dispatch calls fail and usage never rises.
- **DirectML routing broken:** Windows routes AI work through DirectML. If that layer is misconfigured or its components are missing, work never reaches the NPU.
- **Power plan parking the NPU:** Aggressive power saving can keep the NPU in a deep idle state that workloads cannot wake it from, freezing usage at zero.
- **Background AI services disabled:** Recall indexing, Studio Effects processing, and similar services generate the steadiest NPU load. If they are off, the chip has little to do.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Generate a real NPU workload and watch Task Manager

Before changing anything, prove whether the problem is "no work sent" or "work sent but failing." A controlled test with a guaranteed NPU feature gives a clean signal instead of guessing.

1. Open Task Manager (**Ctrl + Shift + Esc**), go to the Performance tab, and select NPU so you can watch it live.
2. Start a certain NPU workload: enable **Studio Effects background blur** in your camera app, or turn on **live captions** (**Win + Ctrl + L**), and watch the graph for 30 seconds.
3. If it spikes, your NPU works — your earlier apps simply were not sending it work.
4. If it stays flat at 0%, the dispatch path is broken — continue with Fix 2.

### Fix 2: Check which chip your apps are actually using

When the NPU stays flat but the CPU or GPU spikes during AI tasks, confirm the fallback directly. Knowing where the work lands tells you whether to fix the app or the driver.

1. With Task Manager open on the Performance tab, run your AI workload again and compare the CPU, GPU, and NPU graphs.
2. If the GPU spikes instead of the NPU, the app prefers GPU DirectML — check the app's settings for an NPU or inference-device option and switch it.
3. If the CPU spikes, the app is not using hardware acceleration — update the app, since NPU support often arrives in newer versions.
4. If nothing spikes anywhere, the [NPU not used by apps guide](/articles/npu-not-used-by-apps-windows-11/) has deeper app-by-app routing checks.

### Fix 3: Reinstall the NPU and chipset drivers cleanly

A driver that looks healthy in Device Manager can still have a broken compute path. A true clean reinstall — delete the driver software, then install the OEM package fresh — rebuilds the dispatch layer.

1. In Device Manager, right-click the NPU, choose **Uninstall device**, check **"Attempt to remove the driver for this device"**, and restart.
2. Download the latest chipset driver for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support and install it as administrator, then install the NPU/AI Boost package and restart again.
3. Rerun the Fix 1 workload test — if usage now spikes, the old driver's compute path was corrupt.
4. If it is still flat, continue — the blockage is elsewhere.

### Fix 4: Stop power management from parking the NPU

When the NPU is parked in a deep idle state by aggressive power policy, workloads cannot wake it and usage freezes at zero. This is a common culprit on laptops running battery-saver profiles.

1. Open **Control Panel > Hardware and Sound > Power Options**, click **Change plan settings**, then **Change advanced power settings**, and set **PCI Express > Link State Power Management** to **Off** for both On battery and Plugged in.
2. Switch to **Best performance** power mode temporarily (**Settings > System > Power & battery > Power mode**).
3. Rerun the Fix 1 test on AC power — if the NPU wakes up, keep Link State off or use Moderate savings as a compromise.
4. Revisit this if the flatline returns on battery, which confirms power policy as the cause.

### Fix 5: Repair the DirectML and AI platform components

Windows dispatches NPU work through DirectML and the Windows AI platform. If those components are damaged, dispatch fails silently and usage never rises — even with a perfect driver.

1. Install all pending updates in **Settings > Windows Update**, including optional driver updates — DirectML components ship through Windows Update.
2. Open Terminal as administrator and run `sfc /scannow` to repair corrupted system files the AI platform depends on.
3. For driver errors here, check the [driver signature verification guide](/articles/npu-driver-signature-verification-failed/) — a signature failure on one NPU component can silently break dispatch.
4. Restart and rerun the Fix 1 workload test.

### Fix 6: Re-enable the background AI services that feed the NPU

The steadiest NPU load on an AI PC comes from background services — Recall indexing, Studio Effects, live captions. If these are disabled, the chip idles at 0% even when healthy.

1. In **Settings > Privacy & security > Recall & snapshots**, make sure Recall is enabled if you use it.
2. Turn on **live captions** (**Win + Ctrl + L**) during a video call or media playback.
3. Enable a Studio Effects feature (background blur or eye contact) in your camera app.
4. Watch Task Manager — sustained NPU activity proves the chip and dispatch path are healthy. If [Click to Do's summarize feature is missing](/articles/click-to-do-summarize-missing/), that is a separate app-availability issue.

## Closing

An NPU stuck at 0% is usually a workload-routing story, not a dead chip: either nothing is asking the NPU for work, or the dispatch path is broken. Test with a guaranteed NPU feature first, then work the driver and power layers.
