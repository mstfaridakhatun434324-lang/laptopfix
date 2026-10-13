---
title: "Enable Hardware-Accelerated GPU Scheduling in Windows 11 24H2"
slug: how-to-enable-hardware-accelerated-gpu-scheduling-in-windows-11-24h2
date: 2026-10-13
categories: ["performance"]
tags: ["gpu scheduling", "hags", "windows 11 24h2", "gaming", "graphics"]
description: "What is Hardware-Accelerated GPU Scheduling in Windows 11 24H2, how to enable it, which GPUs support it, and when it actually helps."
thumbnail: "/images/thumbs/how-to-enable-hardware-accelerated-gpu-scheduling-in-windows-11-24h2.webp"
faqs:
  - q: "What does Hardware-Accelerated GPU Scheduling actually do?"
    a: "Normally your CPU manages GPU memory and schedules GPU tasks. Hardware-accelerated GPU scheduling hands that scheduling work to a dedicated scheduling processor on the GPU itself, reducing CPU overhead and latency in the graphics pipeline. In practice this means slightly lower CPU usage during gaming and potentially smoother frame pacing, though the gains are modest — typically a few percent — and vary by game, GPU, and driver."
  - q: "Which GPUs support hardware-accelerated GPU scheduling?"
    a: "NVIDIA GeForce GTX 10 series and newer plus current drivers, AMD Radeon RX 5000 series and newer, and Intel integrated and Arc graphics with recent drivers all support it. The GPU needs a hardware scheduler, which is why older cards are excluded. If the toggle is missing from your graphics settings, your GPU or driver does not support it — updating to the latest driver from NVIDIA, AMD, or Intel is the first thing to check."
  - q: "Should I turn it on or leave it off?"
    a: "For most users on supported hardware, turning it on is reasonable — it is a stable, Microsoft-supported feature since Windows 10 version 2004. Gamers may see small latency and frame-consistency improvements. However, a minority of users report stuttering or instability in specific games with it enabled, so if you enable it and a particular game gets worse, toggle it back off and reboot. There is no universal right answer; test with your games."
  - q: "Do I need to restart after enabling it?"
    a: "Yes, Windows requires a restart for the change to take effect — the toggle itself will tell you so. The scheduling mode is established when the graphics stack initializes at boot, so without a restart nothing changes. After rebooting, you can verify it is active with Task Manager, Performance tab, GPU section, where supporting systems note the scheduling state, or simply confirm the toggle stayed on."
---

Hardware-Accelerated GPU Scheduling (HAGS) is one of those Windows settings that sounds like free performance — and mostly, it is a small, free improvement. Instead of your CPU micromanaging GPU memory and task scheduling, HAGS lets the GPU's own dedicated scheduler handle that work. The result: a bit less CPU overhead in the graphics pipeline, slightly lower latency, and in some games, smoother frame delivery. On Windows 11 24H2 the feature is mature, stable, and a single toggle away.

But "free performance" needs honest framing. Gains are typically in the low single-digit percentages, vary wildly by game and GPU, and a small minority of users see worse stuttering with it on. This guide covers what HAGS does, how to enable it on 24H2, how to verify it's working, and how to decide whether to keep it — plus what to do when the toggle is missing. If your games stutter for other reasons, also see [fixing game stuttering after a Windows update](/articles/how-to-fix-game-stuttering-after-windows-update-in-windows-11-24h2/) and [Desktop Window Manager high GPU](/articles/how-to-fix-desktop-window-manager-high-gpu-after-windows-11-update/).

## Why this happens

- **CPU-managed GPU scheduling is overhead**: Without HAGS, the CPU spends cycles scheduling GPU work — cycles games could use.
- **Latency in the graphics pipeline**: Extra CPU hops between frame submission and GPU execution add input latency.
- **The toggle is missing**: Older GPUs lack the hardware scheduler, or drivers are too old to expose it.
- **It was off by default**: Windows enables HAGS by default on fresh 24H2 installs with supported GPUs, but upgrades sometimes leave it off.
- **Driver updates reset it**: Major GPU driver reinstalls occasionally flip the toggle back off.
- **Conflicting overlays**: Some overlays and capture tools interact poorly with the hardware scheduler in specific games.
- **Expectation mismatch**: HAGS optimizes scheduling overhead — it can't fix stutter caused by shaders, thermals, or slow storage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether your GPU supports it

Don't hunt for a toggle your hardware can't use.

1. Open **Task Manager** > **Performance** > **GPU** and note your GPU model.
2. Supported: **NVIDIA** GeForce GTX 10 series / RTX 20, 30, 40, 50 series; **AMD** Radeon RX 5000 series and newer; **Intel** UHD/Iris Xe integrated and **Arc** discrete — all with recent drivers.
3. If your GPU is older than these, HAGS isn't available — no setting or hack enables a hardware scheduler that doesn't exist. Your performance tuning time is better spent on [game stuttering fixes](/articles/how-to-fix-game-stuttering-after-windows-update-in-windows-11-24h2/).
4. On laptops with dual GPUs (integrated + discrete), HAGS applies at the system level — the discrete GPU is what matters for gaming.
5. When in doubt, check your GPU vendor's specs page for "hardware scheduling" support rather than guessing.

### Fix 2: Update your GPU driver first

An old driver hides the toggle.

1. Identify your GPU vendor, then get the latest driver: [NVIDIA's driver download](https://www.nvidia.com/Download/index.aspx), [AMD's driver support](https://www.amd.com/en/support/download/drivers.html), or [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. Do a **clean install** of the driver (NVIDIA and AMD installers both offer this option) — it clears corrupted settings that can hide or break the toggle.
3. For laptops, prefer the driver from your laptop manufacturer's support site if the vendor-direct driver misbehaves — OEM-customized GPUs sometimes need OEM drivers.
4. Reboot after the driver install, even if not prompted.
5. Only after the driver is current should you look for the toggle — checking before updating wastes time.

### Fix 3: Enable the toggle in Windows 11 24H2

The actual one-minute change.

1. Open **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings** (at the top of the Graphics page).
2. Find **Hardware-accelerated GPU scheduling** and switch it **On**.
3. If the toggle is missing despite a supported GPU and current driver, your specific GPU/driver combination doesn't expose it — some mobile GPUs lag behind desktop support.
4. **Restart your laptop** — the change only takes effect at boot, when the graphics stack initializes. The Settings page will say so.
5. After rebooting, return to the same page and confirm the toggle is still On — if it flipped back, a driver or policy is overriding it (see Fix 5).

### Fix 4: Verify it's active and test with your games

Confirm, then measure.

1. Re-open **Task Manager** > **Performance** > **GPU** — on supporting systems the GPU details note the scheduling state.
2. Launch your most-played game and play for 15–20 minutes with HAGS on — note frame rates, 1% lows if you monitor them, and subjective smoothness.
3. Then toggle it **off**, reboot, and repeat the same session — compare honestly. A few percent improvement or slightly steadier frame pacing means keep it on.
4. Pay special attention to games that previously micro-stuttered — HAGS helps scheduling-related stutter specifically, not shader-compilation stutter.
5. Keep notes per game: HAGS is system-wide, but its effect is per-game, and knowing which of your games benefit settles the keep-or-remove question.

### Fix 5: Troubleshoot a missing or reverting toggle

When the setting won't cooperate.

1. Toggle missing: re-verify GPU support (Fix 1) and driver currency (Fix 2) — those cover 95% of missing-toggle cases.
2. Toggle reverts after reboot: check for group policies or "tweaker" utilities managing GPU settings — undo their GPU-related changes.
3. On some laptops, the toggle only appears when the discrete GPU is active — plug in AC power and set the power mode to **Best performance**, then re-check.
4. Try the registry path only as a diagnostic: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers` — `HwSchMode` = 2 means on, 1 means off. If Settings won't stick but the registry does, a policy is interfering.
5. If nothing exposes the toggle, accept it — your configuration doesn't support HAGS, and the gains wouldn't have been transformative anyway. Microsoft's Windows graphics documentation covers the feature's requirements.

### Fix 6: Decide per-game whether to keep it

The honest evaluation step most guides skip.

1. Keep HAGS **on** if your testing shows neutral-to-positive results across your games — it's the default for a reason on supported hardware.
2. If one specific game stutters worse with HAGS on while others are fine, you have two options: leave HAGS on and live with it, or turn it off system-wide — there's no per-game toggle, unfortunately.
3. For competitive or latency-sensitive games, test input latency specifically, not just FPS — HAGS's latency reduction is its most consistent benefit.
4. Re-test after major GPU driver updates — driver changes occasionally flip which games benefit.
5. Don't chase the toggle as a fix for stutter with an obvious other cause (thermal throttling, single-channel RAM, HDD game drive) — fix the actual bottleneck instead.

### Fix 7: Pair it with the settings that multiply the benefit

HAGS is one piece of a smooth-gaming setup.

1. Enable **Game Mode** (**Settings** > **Gaming** > **Game Mode**) — it deprioritizes background tasks while gaming, complementing HAGS's CPU-overhead reduction.
2. Set your laptop's power mode to **Best performance** and thermal profile to performance when gaming plugged in.
3. Keep GPU drivers current — HAGS's benefit grows as vendors optimize their schedulers.
4. Cap frame rates slightly below your display's refresh rate (in-game or via driver) to smooth frame pacing — this pairs well with HAGS's steadier scheduling.
5. Monitor with an overlay (RTSS or the driver overlay) for a session — seeing steadier frame times is more convincing than any benchmark number.

## Closing

Hardware-Accelerated GPU Scheduling on Windows 11 24H2 is a genuine, if modest, improvement: less CPU overhead in the graphics pipeline, a touch less latency, occasionally smoother frames — for the price of one toggle and a reboot. Enable it on supported hardware, test honestly with your own games, and keep it if it helps. It's not magic, but free performance is free performance.
