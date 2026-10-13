---
title: "Display Driver Stopped Responding: Step-by-Step Fix Guide"
slug: how-to-fix-display-driver-stopped-responding-step-by-step
date: 2026-09-05
categories: ["drivers"]
tags: ["display driver stopped responding", "tdr error fix", "gpu driver reinstall"]
description: "Fix the \"display driver stopped responding and has recovered\" error step by step — clean driver reinstalls, TDR tweaks, and stability checks for any laptop."
thumbnail: "/images/thumbs/how-to-fix-display-driver-stopped-responding-step-by-step.webp"
faqs:
  - q: "What is the TDR error in simple terms?"
    a: "TDR stands for Timeout Detection and Recovery. Windows watches the graphics driver, and if it stops responding for about two seconds, Windows restarts the driver instead of crashing the whole system. You see a brief freeze or black screen, then everything comes back with a notification."
  - q: "How do I know if it is a driver problem or bad hardware?"
    a: "Driver problems are workload-specific and started after a software change; hardware problems show visual artifacts, happen in the BIOS screen, or occur even at idle. Run the manufacturer's hardware diagnostics — if the GPU passes, the problem is software and these steps will fix it."
  - q: "Which driver should I install to fix TDR errors?"
    a: "Start with the driver from your laptop manufacturer's support page, since it is validated for your exact hardware. If TDRs persist, try the latest driver from the GPU vendor (Intel, NVIDIA, or AMD). Keep track of which version is stable for your machine."
  - q: "Can overheating really cause the display driver to stop responding?"
    a: "Yes, it is one of the top causes. When the GPU overheats, it throttles and misses the driver's response deadlines, triggering TDR. If freezes happen after minutes of gaming or rendering and the fans are loud, suspect heat before software."
---

"Display driver stopped responding and has recovered." The screen freezes, flickers black, and returns — sometimes once a day, sometimes every ten minutes in a game. This is Windows' TDR mechanism doing its job: rather than blue-screening when the graphics driver hangs, it restarts the driver and tells you about it.

Because TDR is a symptom rather than a single disease, the fix depends on what is hanging the driver: corrupt driver files, overheating, an unstable overclock, a misbehaving app, or an over-aggressive timeout. This step-by-step guide walks the full diagnostic path in the order a technician would follow it.

## Why this happens

- **Corrupt GPU driver installation:** Failed or partial updates leave driver components that hang under load.
- **GPU overheating:** Thermal throttling makes the driver miss its two-second response deadline.
- **Unstable overclock/undervolt:** Marginal GPU or memory clocks crash the driver when stressed.
- **Driver regression:** A new driver version introduces hangs on specific hardware that the old version did not have.
- **Hardware acceleration conflicts:** Browsers and chat apps with GPU acceleration trigger hangs on certain drivers.
- **TDR timeout too short:** Legitimate heavy operations (shader compilation, large renders) exceed the default two-second limit.
- **Unstable power delivery:** Weak chargers or degraded batteries cause voltage droops that hang the GPU.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify when and where it happens

Diagnosis first: the pattern tells you which fix to prioritize.

1. Note exactly what you were doing when the freeze occurred — gaming, video call, browsing, or idle.
2. Check **Event Viewer > Windows Logs > System** for events from source `nvlddmkm`, `amdkmdap`, or `igfx` around the freeze time. The faulting module name tells you which driver hung.
3. If it only happens in one app, skip to Fix 5. If it happens across everything under load, start with Fix 2 and Fix 4.

Five minutes of pattern-noting here saves you from reinstalling drivers for a problem that is actually heat — or vice versa.

### Fix 2: Perform a clean GPU driver reinstall with DDU

The most reliable single fix for TDR loops.

1. Download **Display Driver Uninstaller (DDU)** and the new driver for your GPU from Intel, NVIDIA, or AMD — or your laptop maker's support page for a validated version.
2. Disconnect from the internet to block Windows from installing its own driver mid-process.
3. Boot into **Safe Mode** and run DDU: select your GPU brand and choose **Clean and restart**.
4. After rebooting (still offline), install the downloaded driver with its **Clean installation** option, then reconnect.

Before any driver surgery, consider [backing up your current drivers](/articles/best-way-to-backup-drivers-before-update/) so you can restore the exact working set if the new version misbehaves.

### Fix 3: Test the previous driver version

If the TDRs began right after a driver update, the update is guilty until proven innocent.

1. Download the prior driver version from the vendor's driver archive.
2. Install it using the DDU-clean method from Fix 2.
3. Use the machine normally for a day or two before judging stability.

Driver regressions are common enough that many experienced users keep a "known good" version noted down. Do not update GPU drivers reflexively — update when you have a reason.

### Fix 4: Check temperatures and cooling

Heat-induced TDRs follow a recognizable pattern: fine when cold, freezing after minutes of load.

1. Run **HWiNFO64** sensors-only mode and watch GPU temperature during the triggering workload.
2. Sustained temperatures above ~85–90°C with loud fans point to cooling problems: clean vents with compressed air, use a hard flat surface, and consider a cooling pad.
3. On older laptops, dried thermal paste is a prime suspect — a repaste by a technician often drops temperatures 10–15°C.
4. As an immediate relief, cap frame rates (NVIDIA/AMD control panels or in-game settings) to reduce heat output.

If freezes correlate with temperature spikes, you have found your cause — no driver version fixes a GPU that is cooking itself.

### Fix 5: Disable hardware acceleration in everyday apps

Many TDR reports trace to browsers and chat apps, not games.

1. Disable **Use hardware acceleration** in Chrome/Edge (**Settings > System**), Discord, Slack, and Teams.
2. Restart each app and test for a day.
3. Re-enable one app at a time to identify the trigger if the freezes stop.

This is especially worth trying when TDRs happen during video calls or while scrolling media-heavy pages — classic hardware-acceleration trigger scenarios.

### Fix 6: Adjust the TDR delay and GPU scheduling

Two Windows-level tweaks for borderline cases.

1. In the registry at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`, create DWORD `TdrDelay` set to **8** (decimal) to give the GPU eight seconds before Windows declares a hang. Restart afterward.
2. Go to **Settings > System > Display > Graphics > Change default graphics settings** and try **Hardware-accelerated GPU scheduling** both on and off, testing stability in each state.

The TDR delay helps legitimate long operations; the scheduling toggle resolves driver-specific conflicts. Neither replaces a broken driver, so do these after Fix 2, not instead of it. Microsoft documents display troubleshooting basics on the [Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 7: Verify power delivery and run hardware diagnostics

The last software-adjacent checks before suspecting the GPU itself.

1. Test on the original manufacturer charger with the battery installed — third-party chargers with wrong wattage cause voltage droops under GPU load.
2. Reset any GPU overclock or undervolt to factory defaults (MSI Afterburner, vendor utilities).
3. Run your laptop maker's built-in hardware diagnostics (Dell, HP, and Lenovo all include GPU tests) to confirm the hardware passes.
4. If diagnostics fail or you see visual artifacts even in the BIOS, the GPU hardware is failing — contact support while under warranty.

A GPU that passes diagnostics, stays cool, and still TDRs on a clean driver install across versions is rare — but that combination is the genuine signal for a hardware fault. For brand-specific angles, see our [HP-focused TDR guide](/articles/how-to-fix-display-driver-stopped-responding-on-hp-laptop/).

## Closing

TDR errors look scary but are Windows protecting you from a full crash while the graphics driver hangs. Diagnose the pattern first, then clean-reinstall the driver, check thermals, and tame hardware acceleration — in that order. Worked through methodically, these steps resolve the "display driver stopped responding" loop on nearly every laptop where the GPU hardware is healthy.
