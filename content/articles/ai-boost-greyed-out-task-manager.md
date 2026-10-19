---
title: "AI Boost Greyed Out in Task Manager? How to Enable It"
slug: ai-boost-greyed-out-task-manager
date: 2026-10-19
categories: ["ai-pc"]
tags: ["ai boost", "task manager", "greyed out", "npu", "windows 11"]
description: "AI Boost greyed out in Task Manager on Windows 11? Learn why the NPU monitor is disabled and how to re-enable NPU tracking in minutes."
thumbnail: "/images/thumbs/ai-boost-greyed-out-task-manager.webp"
faqs:
  - q: "What does a greyed-out NPU in Task Manager mean?"
    a: "It means Windows sees the NPU hardware entry but cannot communicate with it — usually a driver problem, a disabled device, or the NPU being turned off in BIOS. The chip is present but not operational."
  - q: "Is greyed out different from missing entirely?"
    a: "Yes. Missing means Windows sees no NPU at all; greyed out means it sees the device but cannot use it. Greyed out is actually the better problem — the hardware and enumeration are working, so the fix is usually driver-level."
  - q: "Can I still use AI features with a greyed-out NPU?"
    a: "No. A greyed-out NPU cannot process workloads, so Copilot+ features that need it will fail or fall back to slower CPU processing. Fix the underlying issue first."
  - q: "Does this affect battery life?"
    a: "Not directly — a non-functional NPU draws little power. But apps falling back to CPU for AI tasks can increase overall consumption, so fixing the NPU often improves efficiency too."
---

Task Manager shows the NPU entry, but it is greyed out — no live graph, no utilization, just a dimmed label where your AI accelerator should be. This is a distinct symptom from the NPU being [entirely undetected](/articles/npu-not-detected-windows-11/): Windows knows the hardware is there, but something is preventing it from talking to the chip. That "something" is fixable in most cases without touching hardware.

A greyed-out entry typically means the device is disabled, its driver failed to start, or firmware has the NPU in a low-power limbo. Work through these fixes in order.

## Why this happens

- **Device disabled in Device Manager:** The NPU may have been manually disabled or disabled by a failed update, and Task Manager reflects that state as greyed out.
- **Driver failed to start:** A broken or mismatched driver leaves the device present but non-functional.
- **NPU suspended by power policy:** Aggressive power saving can park the NPU so deeply that Task Manager cannot query it.
- **BIOS set to a limited mode:** Some firmware offers NPU "low power" modes that restrict OS access.
- **Driver/firmware version skew:** The driver loads but cannot initialize the chip, leaving it in a half-alive state.
- **Task Manager itself glitching:** Rarely, the Performance tab cache goes stale and shows a greyed entry for a working NPU — a refresh fixes it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Refresh Task Manager and reboot

Rule out a display glitch before doing real work.

1. Close Task Manager completely and reopen it (Ctrl + Shift + Esc).
2. Check the Performance tab again — look for the NPU entry lighting up.
3. If still grey, do a full shutdown (not restart), wait 10 seconds, power on.
4. Recheck. If the NPU is live now, it was a stale enumeration — done.
5. If still grey, the problem is real; continue.

### Fix 2: Enable the device in Device Manager

The most common actual cause.

1. Open Device Manager (Win + X), expand Neural processors.
2. If the NPU shows a down-arrow icon, right-click and choose Enable device.
3. If it shows a warning instead, note the error code — [code 43](/articles/npu-driver-error-code-43/) has its own fix path.
4. After enabling, reboot and check Task Manager.
5. If it disables itself again on reboot, a driver or policy is fighting you — continue to Fix 3.

### Fix 3: Reinstall the NPU driver

A driver that cannot start the chip produces exactly this symptom.

1. Get the OEM NPU driver from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. Device Manager: uninstall the NPU entry, ticking "Attempt to remove the driver."
3. Install the OEM package, reboot.
4. Check Task Manager — the NPU graph should now be live.
5. If the entry is still grey, the driver version may mismatch your firmware; try the next older or newer OEM release.

### Fix 4: Check BIOS NPU settings

Firmware can put the NPU in a restricted mode.

1. Reboot into BIOS (F2/Del/F10).
2. Find NPU / AI Boost settings — look for modes like "Enabled" vs "Low Power" or "Auto."
3. Set it to fully Enabled (not Auto or Low Power).
4. Save, exit, boot Windows, recheck Task Manager.
5. Our [BIOS NPU enablement guide](/articles/how-to-enable-npu-in-bios/) covers vendor-specific menu locations.

### Fix 5: Relax power management

Deep power states can hide a working NPU from Task Manager.

1. Settings, System, Power & battery — set power mode to Best performance temporarily.
2. Device Manager, NPU Properties, Power Management tab — uncheck "Allow the computer to turn off this device."
3. Advanced power settings: PCI Express Link State Power Management — Off (temporarily).
4. Reboot and check Task Manager. If the NPU lights up, power policy was the cause.
5. Restore balanced settings afterward, keeping just the NPU's own power-management checkbox off.

### Fix 6: Verify apps can actually use the NPU

A live Task Manager entry does not guarantee apps use the chip.

1. With the NPU graph active, run an AI feature (e.g., Windows Studio Effects on your camera).
2. Watch the NPU utilization — it should spike during the AI workload.
3. If it stays flat while the feature runs, apps are bypassing the NPU — see our guide on [NPU not used by apps](/articles/npu-not-used-by-apps-windows-11/).
4. Confirm in the app's settings that NPU/hardware acceleration is selected where applicable.
5. Persistent flatlines across all apps point back to a driver issue — revisit Fix 3 with a different driver version.

## Closing

A greyed-out NPU in Task Manager is Windows telling you the hardware is visible but unreachable — almost always a disabled device, a failed driver start, or a power policy parking the chip too deeply. Enable, reinstall, and check firmware in that order, and the graph comes alive. Once it does, confirm real workloads actually reach the silicon; a lit-up graph that never moves means the next problem is app routing, not detection.
