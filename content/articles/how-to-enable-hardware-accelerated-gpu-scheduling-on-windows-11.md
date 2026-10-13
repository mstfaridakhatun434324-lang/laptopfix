---
title: "How to Enable Hardware-Accelerated GPU Scheduling on Windows 11"
slug: how-to-enable-hardware-accelerated-gpu-scheduling-on-windows-11
date: 2026-09-18
categories: ["performance"]
tags: ["gpu scheduling", "hags", "windows 11 graphics", "gaming performance"]
description: "Enable Hardware-Accelerated GPU Scheduling (HAGS) on Windows 11 to cut latency and boost gaming smoothness — requirements, steps, and troubleshooting."
thumbnail: "/images/thumbs/how-to-enable-hardware-accelerated-gpu-scheduling-on-windows-11.webp"
faqs:
  - q: "What does Hardware-Accelerated GPU Scheduling do?"
    a: "Normally Windows manages GPU memory through the CPU, which adds scheduling overhead and latency. HAGS lets the GPU's own dedicated scheduling processor manage its memory directly, bypassing the CPU for these decisions. The result is lower latency, slightly higher and more consistent frame rates in games, and less CPU overhead during GPU-heavy work like video rendering or 3D tasks."
  - q: "Which GPUs support Hardware-Accelerated GPU Scheduling?"
    a: "You need a GPU with a hardware scheduler: NVIDIA GeForce GTX 10-series and newer (Pascal onward) with driver 451.48+, or AMD Radeon RX 5600/5700-series and newer with Adrenalin 20.5.1+. Intel integrated graphics on 11th-gen Core and newer also support it. Older GPUs lack the required scheduler hardware, so the toggle simply won't appear for them."
  - q: "Will enabling HAGS make a big difference in games?"
    a: "Expect modest gains: typically 1–5% higher average FPS and, more importantly, smoother frame pacing with fewer micro-stutters. The benefit is largest on systems where the CPU is the bottleneck or in games with heavy draw-call loads. It's a free improvement with no downside on supported hardware, so there's no reason not to enable it — but don't expect miracles."
  - q: "Why is the HAGS toggle missing on my Windows 11 laptop?"
    a: "The toggle only appears when three conditions are met: Windows 11 with WDDM 2.7+ driver model, a GPU with hardware scheduling support, and a current graphics driver. Update your GPU driver from NVIDIA, AMD, or Intel first. On laptops with hybrid graphics, check that the discrete GPU driver is current — an outdated iGPU or dGPU driver can hide the option."
---

Hardware-Accelerated GPU Scheduling (HAGS) is one of those rare free performance upgrades: a single toggle that hands GPU memory management from the CPU to a dedicated scheduler on the graphics card itself. The payoff is lower latency and smoother frame delivery in games and GPU-heavy apps. Microsoft introduced it in Windows 10 version 2004 and refined it in Windows 11, where it's better supported across drivers.

Enabling it takes about a minute — but only if your hardware qualifies. This guide covers the requirements, the two ways to enable it (Settings and Registry), how to verify it's actually active, and what to do when the toggle is missing or causes issues. If you're chasing broader gaming smoothness, also see [fixing game stuttering after a Windows update](/articles/how-to-fix-game-stuttering-after-windows-update-on-dell-laptop/); for general GPU load issues, [Desktop Window Manager high GPU](/articles/how-to-fix-desktop-window-manager-high-gpu-in-windows-11-24h2/).

## Why this happens

- **CPU-managed GPU scheduling adds latency**: The default path routes every GPU memory decision through the CPU, adding overhead.
- **Frame pacing suffers under CPU bottlenecks**: When the CPU is busy, GPU scheduling waits — causing micro-stutters HAGS eliminates.
- **Driver overhead in draw-call-heavy games**: Games issuing thousands of draw calls pay scheduling tax on every frame.
- **Windows 11 refines the WDDM scheduler**: The newer driver model makes hardware scheduling more stable than the early Windows 10 implementation.
- **Laptop hybrid graphics complicate scheduling**: iGPU/dGPU switching adds another scheduling layer that benefits from hardware offload.
- **Outdated drivers hide the feature**: The toggle requires WDDM 2.7+; old drivers report an older model and the option vanishes.
- **Some apps behave better with direct GPU control**: Video editors and 3D renderers with heavy VRAM churn see the most consistent gains.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm your hardware supports HAGS

Don't hunt for a toggle your GPU can't show.

1. Press Win + R, type `dxdiag`, and check the **Display** tab — note your GPU model and the **Driver Model** (needs WDDM 2.7 or higher).
2. NVIDIA: you need a GTX 10-series or newer. AMD: RX 5600/5700-series or newer. Intel: 11th-gen Core iGPU or newer, or Arc graphics.
3. If your GPU is older than these, stop here — the hardware scheduler doesn't exist on your card and no setting can enable it.
4. On hybrid-graphics laptops, check **both** display tabs in dxdiag — the toggle keys off the driver model reported.
5. If hardware qualifies but the toggle is missing, the driver is the problem — continue to Fix 2.

### Fix 2: Update your graphics driver

The most common reason for a missing HAGS toggle.

1. Identify your GPU vendor, then get the latest driver: [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx), [AMD drivers](https://www.amd.com/en/support/download/drivers.html), or [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. Do a clean install: NVIDIA offers "Custom > Perform a clean installation"; AMD has a factory-reset option in its installer.
3. On laptops, prefer the laptop manufacturer's driver (Dell, HP, Lenovo, ASUS) if the generic one causes issues — but try the vendor driver first for the newest WDDM support.
4. Restart after installation and re-check dxdiag — confirm the Driver Model now reads WDDM 3.x.
5. If the toggle still doesn't appear, continue to the Registry method in Fix 4, which can force it on supported hardware.

### Fix 3: Enable HAGS in Settings (the normal way)

The one-minute toggle.

1. Open **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings** (at the top of the Graphics page).
2. Turn on **Hardware-accelerated GPU scheduling**.
3. Also enable **Optimizations for windowed games** on the same page — it reduces latency for borderless-windowed games.
4. Restart your laptop — the change only takes effect after a reboot.
5. After rebooting, return to the same page to confirm the toggle stayed on (on some systems with outdated drivers it silently reverts).

### Fix 4: Enable HAGS via the Registry

For systems where the Settings toggle is missing but hardware qualifies.

1. Press Win + R, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Find the **HwSchMode** DWORD — double-click it and set its value to `2` (enabled). If it doesn't exist, right-click > **New** > **DWORD (32-bit) Value**, name it `HwSchMode`, and set it to `2`.
3. Value `1` means disabled; `2` means enabled. (Back up the key first: right-click GraphicsDrivers > Export.)
4. Restart the laptop — this is mandatory for the change to apply.
5. Verify with dxdiag or GPU-Z afterward; if games crash or stutter more, set it back to `1` — a small number of driver/hardware combos don't like it.

### Fix 5: Verify it's actually active and helping

Confirm the change did something measurable.

1. Reopen **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings** — toggle should read On.
2. Run a quick before/after test in a demanding game with its built-in benchmark or an FPS overlay (GeForce Experience, Radeon Software, or RTSS).
3. Look for improved 1% lows and smoother frame times rather than just average FPS — that's where HAGS shows up.
4. Check **Task Manager** > **Performance** > **GPU** during gaming — CPU-side scheduling overhead should be marginally lower.
5. Give it a few gaming sessions before judging; driver shader caches rebuild after driver updates and can temporarily skew results.

### Fix 6: Roll back if you get instability

Rare, but some configurations regress.

1. If you see new stuttering, driver crashes, or black screens after enabling HAGS, turn the toggle off (or set `HwSchMode` back to `1`) and reboot.
2. Known-sensitive setups: very old games, certain VR titles, and some laptop dGPU drivers — update the driver again before concluding HAGS is at fault.
3. Also test with **Optimizations for windowed games** toggled separately — occasionally that setting, not HAGS, is the culprit.
4. File feedback via the GPU vendor's driver feedback if a current driver breaks with HAGS on — it helps get it fixed.
5. Revisit after the next driver update; HAGS support improves steadily and a future driver may resolve the conflict.

## Closing

Hardware-Accelerated GPU Scheduling is a genuine, free improvement on supported hardware: lower latency, smoother frame pacing, and less CPU overhead for GPU work. Check your GPU qualifies, update the driver so the toggle appears, flip it on, reboot, and verify with real games. If your hardware is too old for it, the best alternative is simply keeping drivers current and trimming background load while gaming.
