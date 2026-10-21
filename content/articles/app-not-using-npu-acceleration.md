---
title: "How to Fix an App Not Using NPU Acceleration"
slug: app-not-using-npu-acceleration
date: 2026-10-21
categories: ["ai-pc"]
tags: ["npu acceleration", "app not using npu", "directml", "npu usage zero", "ai pc", "windows 11"]
description: "Is an app ignoring your NPU? Follow step-by-step fixes to route AI workloads to the neural processor, verify NPU usage, and stop battery-draining CPU fallbacks."
thumbnail: "/images/thumbs/app-not-using-npu-acceleration.webp"
faqs:
  - q: "Why does my app run on the CPU instead of the NPU?"
    a: "Most apps default to the CPU or GPU unless they are written to target the NPU through DirectML or an NPU execution provider. An app that never mentions NPU support usually has no NPU code path at all — no setting can change that."
  - q: "How do I check whether an app is using the NPU?"
    a: "Open Task Manager > Performance > NPU while the app is running its AI workload. Sustained NPU activity during the task means it is accelerating; a flat zero while the CPU spikes means the app fell back to the CPU."
  - q: "Can I force any app to use the NPU?"
    a: "No. The app's developer must ship NPU support. What you can do is make sure the NPU is healthy, the app is updated, and any in-app AI or hardware-acceleration setting is enabled — then the app's own NPU path can engage."
  - q: "Does using the NPU save battery?"
    a: "Yes, significantly. NPUs deliver AI work at far lower power than a CPU doing the same math. An app stuck on the CPU for background AI tasks will drain your battery noticeably faster than the same workload on the NPU."
---

Your AI PC's NPU sits at zero while an app churns your CPU on an AI task — background blur, noise removal, image generation. Why?

Apps don't use the NPU automatically. A developer must write an explicit NPU code path — usually through DirectML or the chip vendor's execution provider. When that path is missing, outdated, or blocked by a driver problem, the app quietly falls back to the CPU.

Six fixes in order: verify the app supports the NPU, confirm the NPU is healthy, flip the right in-app and Windows settings, update the software stack, and confirm real NPU activity.

## Why this happens

- **The app has no NPU code path:** Many AI apps ship CPU/GPU-only builds. Unless the release notes or settings mention NPU, DirectML, or your chip (Intel AI Boost, AMD Ryzen AI, Snapdragon), the app simply cannot use the NPU.
- **NPU driver missing or broken:** Even NPU-aware apps fall back to the CPU when the driver is absent — the classic [code 28 drivers-not-installed state](/articles/directml-not-using-npu-windows-11/) — or when the device fails.
- **Outdated app version:** NPU support often arrives in a later release than the app's initial AI features. Running last year's build means running the pre-NPU code path.
- **AI/hardware acceleration disabled in settings:** Some apps gate their NPU path behind an "AI acceleration" or "hardware acceleration" toggle that ships off by default or gets reset by updates.
- **Windows graphics preference forcing the wrong processor:** Per-app GPU preferences and power policies can steer an app to the integrated GPU or CPU, bypassing the NPU provider entirely.
- **Stale DirectML or AI framework:** A mismatched or outdated framework version silently disables the NPU provider.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the app actually supports NPU acceleration

Chasing settings for an app without NPU support wastes an afternoon. Check the developer's documentation first — not the marketing.

1. Search the app's settings for "NPU", "AI acceleration", "hardware acceleration", or "DirectML". Absent options strongly suggest no NPU path exists.
2. Check the developer's release notes or support pages for your chip name (Intel AI Boost, AMD Ryzen AI XDNA, Snapdragon Hexagon).
3. If the app is NPU-aware but sluggish to start its AI features, the [Copilot app slow loading fix](/articles/copilot-app-slow-loading-fix/) covers a related startup problem with the same diagnostic mindset.
4. If no NPU support exists, your options are updating to a newer version that adds it or switching to an alternative app that does.

### Fix 2: Verify the NPU is healthy in Device Manager and Task Manager

An NPU-aware app cannot use hardware that Windows cannot see. Confirm the neural processor is present and started before touching the app. If the device is missing entirely, reinstall the chipset driver from your laptop maker or the [Intel](https://www.intel.com/content/www/us/en/support/detect.html) / [AMD](https://www.amd.com/en/support/download/drivers.html) driver pages.

1. Open Device Manager and confirm the NPU entry exists with no yellow warning. A broken or missing device must be fixed first — see the [DirectML NPU guide](/articles/directml-not-using-npu-windows-11/) for the driver-side repair.
2. Open Task Manager > Performance and check for an **NPU** tab. No tab means Windows does not see the NPU at all.
3. Run the app's AI workload and watch the NPU graph: flat zero with CPU spiking confirms fallback; sustained NPU activity confirms acceleration works.
4. If the NPU tab is missing entirely, stop here and fix the driver — no app setting substitutes for absent hardware.

### Fix 3: Enable AI and hardware acceleration inside the app

Developers often ship the NPU path behind a toggle that defaults off — the most common fix for apps that genuinely support the NPU.

1. Open the app's Settings or Preferences and look under Performance, Advanced, AI, or Hardware sections.
2. Enable anything labeled AI acceleration, hardware acceleration, NPU, or neural engine — and choose the NPU explicitly if the app offers a processor picker (NPU vs GPU vs CPU).
3. Restart the app fully — quit from the system tray, not just close the window — so the new execution provider loads.
4. Re-run the AI workload with Task Manager's NPU tab open to confirm the change took effect.

### Fix 4: Update the app and the Windows AI stack

A version skew between the app and the Windows ML stack is a classic silent-fallback cause.

1. Update the app to its latest version — via the Microsoft Store (Library > Get updates) or the developer's own updater.
2. Go to **Settings > Windows Update** and install everything pending, since DirectML and NPU driver components ship through Windows Update.
3. If the app plugs into Outlook or Office AI features that also ignore the NPU, the [Click to Do in Outlook fix](/articles/click-to-do-not-working-outlook/) walks through the same update-and-repair sequence.
4. Restart the PC after updating — execution providers load at process start, and a reboot guarantees clean load order.

### Fix 5: Set the app's graphics and power preference to favor efficiency

A wrong graphics or power preference can keep an app on a high-power path that never touches the NPU provider.

1. Go to **Settings > System > Display > Graphics**, find the app in the list (or add its .exe), click Options.
2. Choose **Let Windows decide** or the power-saving GPU option rather than forcing High performance — counterintuitively, the NPU path usually engages from the balanced profile.
3. In **Settings > System > Power & battery**, set Power mode to **Balanced** or **Best power efficiency** while testing.
4. Re-run the workload and check the NPU graph again. If the NPU shows activity, you found the steering problem.

### Fix 6: Reinstall the app cleanly to reset its execution provider

Corrupt caches or a botched update can leave the NPU provider half-registered — the app launches fine but acceleration never initializes. A clean reinstall rebuilds it.

1. Uninstall the app from **Settings > Apps > Installed apps**.
2. Delete its leftover data folders under `%localappdata%` and `%appdata%` — back up any projects or models first.
3. Reinstall the latest version from the official source, launch it, and re-enable the NPU/AI acceleration setting from Fix 3.
4. Verify the NPU now carries the workload in Task Manager — then leave the setting alone through future updates.

## Closing

An idle NPU is usually an app without an NPU path, a disabled toggle, or a driver the app can't see. Verify support exists, confirm the NPU is healthy, flip the acceleration settings, and keep everything updated. Once the NPU graph moves, you get the AI PC payoff: the same features at a fraction of the battery cost.
