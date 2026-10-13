---
title: "Enabling Hardware-Accelerated GPU Scheduling in Windows 11"
slug: how-to-enable-hardware-accelerated-gpu-scheduling
date: 2026-09-22
categories: ["performance"]
tags: ["gpu scheduling", "hardware acceleration", "windows 11", "gaming performance", "graphics"]
description: "Enable Hardware-Accelerated GPU Scheduling on Windows 11 to cut latency and CPU overhead: requirements, steps, and what to do if the option is missing."
thumbnail: "/images/thumbs/how-to-enable-hardware-accelerated-gpu-scheduling.webp"
faqs:
  - q: "What does Hardware-Accelerated GPU Scheduling actually do?"
    a: "Normally the CPU manages GPU memory scheduling; HAGS lets the GPU's own dedicated scheduling processor handle it directly. This cuts scheduling latency and reduces CPU overhead in GPU-heavy workloads like gaming and video rendering. Gains are typically modest — a few percent — but it's free performance with no downside on supported hardware."
  - q: "Why don't I see the Hardware Scheduling option in Settings?"
    a: "Three requirements must all be met: Windows 10 May 2020 Update (2004) or newer, a GPU with a WDDM 2.7+ driver that supports HAGS (most NVIDIA GTX 10-series and newer, AMD RX 5000-series and newer, Intel integrated from recent generations), and a current GPU driver. Update the driver first — an old driver is the most common reason the toggle is missing."
  - q: "Can HAGS cause problems or should I turn it off?"
    a: "On supported hardware with current drivers it's stable, but early driver versions had stuttering and compatibility issues with some games and apps. If you enabled it and notice new stuttering, crashes, or visual glitches, turn it off and retest — it's a one-toggle change. When in doubt, current drivers plus HAGS on is the recommended combination."
  - q: "Does HAGS help on laptops with integrated graphics?"
    a: "Modestly. Integrated GPUs share system memory, so the scheduling win is smaller than on discrete GPUs, but the CPU overhead reduction still helps in games and GPU-accelerated apps. The battery impact is negligible either way. If the toggle is available on your iGPU, there's no reason not to enable it."
---

Hardware-Accelerated GPU Scheduling (HAGS) is one of Windows' quiet free-performance features: it lets your GPU manage its own memory scheduling instead of making the CPU do it, cutting latency and CPU overhead in games and GPU-heavy apps. The gains are modest — typically a few percent — but it's a single toggle with no cost on supported hardware.

The catch is the requirements: the option only appears when your Windows build, GPU, and driver all support it. This guide covers enabling it, what to do when the toggle is missing, and how to verify it's working.

## Why this happens

- **CPU-bottlenecked scheduling:** Without HAGS, the CPU spends cycles managing GPU memory queues.
- **Added latency:** CPU-mediated scheduling inserts delay into the render pipeline.
- **Missing toggle:** Outdated GPU drivers are the top reason the option doesn't appear.
- **Unsupported hardware:** Older GPUs lack the WDDM 2.7+ scheduling processor support.
- **Windows build too old:** HAGS needs Windows 10 2004 or newer.
- **Driver conflicts:** Corrupted GPU driver installs hiding the capability.
- **Disabled after updates:** Major Windows updates occasionally reset the toggle.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Enable the toggle in Graphics settings

Go to **Settings → System → Display → Graphics → Change default graphics settings** and turn on **Hardware-accelerated GPU scheduling**. Reboot when prompted — the change requires a restart to take effect. After rebooting, return to the same page to confirm the toggle stayed on. That's the entire enablement on supported hardware. If the toggle isn't there at all, don't force it — continue to Fix 2 to meet the requirements. The [24H2-specific HAGS guide](/articles/how-to-enable-hardware-accelerated-gpu-scheduling-in-windows-11-24h2/) covers the newest Settings layout.

1. Open **Settings → System → Display → Graphics**.
2. Click **Change default graphics settings**.
3. Turn on **Hardware-accelerated GPU scheduling**.
4. Reboot and confirm the toggle persisted.

### Fix 2: Update the GPU driver to unlock the option

A missing toggle almost always means an old driver. Get the current driver from your GPU vendor: NVIDIA users from [NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx), AMD users from [AMD's driver support page](https://www.amd.com/en/support/download/drivers.html), Intel users via Intel's Driver & Support Assistant tool. Do a clean install if the option still doesn't appear after updating — corrupted installs can hide capabilities. Reboot, then re-check the Graphics settings page; the toggle appears once a WDDM 2.7+ driver is properly installed.

1. Identify your GPU in Device Manager → Display adapters.
2. Download the current driver from the GPU vendor.
3. Perform a clean installation and reboot.
4. Re-check for the HAGS toggle in Graphics settings.

### Fix 3: Verify Windows build and hardware support

Confirm the other two requirements. Press Win+R → `winver` — you need Windows 10 version 2004 or newer (any Windows 11 qualifies). For hardware: NVIDIA GTX 10-series or newer, AMD RX 5000-series or newer, or recent Intel integrated graphics. If your GPU predates these, HAGS simply isn't available — no setting or hack enables hardware that lacks the scheduling processor. In that case, the best performance moves are driver updates and the [laptop HAGS guide](/articles/how-to-enable-hardware-accelerated-gpu-scheduling-on-laptop/) for squeezing performance from older GPUs another way.

1. Run `winver` to confirm your Windows build.
2. Check your GPU model against the support list.
3. If unsupported, focus on driver updates instead.
4. Don't chase registry hacks for missing hardware support.

### Fix 4: Verify HAGS is actually active

The toggle being on doesn't always mean it's working — verify. After enabling and rebooting, the most reliable check is the Settings page itself showing the toggle on. For deeper confirmation, GPU monitoring tools report the scheduling mode, and in games you can compare frame-time consistency before and after. If the toggle keeps turning itself off after reboots, a driver or Windows Update is resetting it — update the driver (Fix 2) and check Windows Update for a newer build. Persistent resets usually end with a clean driver install.

1. Confirm the toggle shows On after reboot.
2. Test in a GPU-heavy game or app for stability.
3. If it resets, clean-install the GPU driver.
4. Check Windows Update for a newer build if resets persist.

### Fix 5: Troubleshoot stuttering or glitches after enabling

If games stutter or apps glitch after enabling HAGS, the feature is exposing a driver bug, not creating one. First update to the absolute latest GPU driver — vendors continuously fix HAGS-related issues. Test with HAGS off to confirm it's the trigger (toggle off, reboot, retest). If off fixes it, leave it off and retry after the next driver release; some game/driver combinations genuinely conflict. Report the issue to the GPU vendor with your driver version — these reports drive the fixes. Stability always beats a theoretical few percent.

1. Update to the latest GPU driver first.
2. Toggle HAGS off, reboot, and retest to confirm the trigger.
3. Leave it off if the conflict is confirmed.
4. Retry after future driver releases.

### Fix 6: Pair HAGS with complementary settings

HAGS is one piece of the latency puzzle. In the same **Graphics settings** area, set your games' **GPU preference** to High performance so they use the discrete GPU on dual-GPU laptops. Enable **Game Mode** (Settings → Gaming → Game Mode) to prioritize game processes. And keep **Variable refresh rate** on if your display supports it. These stack with HAGS for the smoothest experience — each is a small win, and together they're noticeable. Microsoft documents the graphics settings in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Set per-game GPU preference to High performance.
2. Enable Game Mode in Gaming settings.
3. Enable variable refresh rate if supported.
4. Test the combined setup in your most-played game.

## Closing

Hardware-Accelerated GPU Scheduling is free performance hiding behind a toggle — enable it in Graphics settings, update the driver if the toggle is missing, and verify it sticks. It's not a dramatic upgrade, but stacked with proper GPU preferences and Game Mode, it's part of getting everything your hardware can give. And if it ever causes trouble, it's one toggle back to safety.
