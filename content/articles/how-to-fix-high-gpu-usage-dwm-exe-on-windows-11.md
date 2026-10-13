---
title: "How to Fix High GPU Usage by DWM.exe on Windows 11"
slug: how-to-fix-high-gpu-usage-dwm-exe-on-windows-11
date: 2026-09-29
categories: ["performance"]
tags: ["dwm.exe", "gpu usage", "desktop window manager", "windows 11"]
description: "DWM.exe (Desktop Window Manager) eating your GPU on Windows 11? Fix driver issues, HDR/multi-monitor quirks, and runaway visual effects."
thumbnail: "/images/thumbs/how-to-fix-high-gpu-usage-dwm-exe-on-windows-11.webp"
faqs:
  - q: "What is dwm.exe and why does it use the GPU?"
    a: "DWM.exe is the Desktop Window Manager — it composites everything you see: windows, transparency, animations, and the taskbar, using the GPU to do it efficiently. Some GPU usage is normal, especially with multiple monitors, high refresh rates, or HDR. Abnormal is sustained high GPU (30%+) at idle with nothing visually demanding happening — that signals a driver bug, a stuck animation, or a misbehaving app forcing constant redraws."
  - q: "Can I disable or end dwm.exe to stop GPU usage?"
    a: "No — DWM is mandatory since Windows 8; you can't disable it and ending it just makes Windows restart it (or glitches your display). It's also not the enemy: DWM using the GPU is by design and far more efficient than the old CPU-based rendering. The fix is never disabling DWM — it's finding what's making DWM work overtime, which is usually a driver, a display setting, or a specific app."
  - q: "Why does DWM use more GPU with multiple monitors?"
    a: "Each additional monitor multiplies DWM's compositing workload — more pixels to composite, and mixed refresh rates (e.g., 60Hz + 144Hz) force extra synchronization work. HDR on one monitor and SDR on another adds tone-mapping overhead. If DWM GPU spikes appeared when you added a monitor, try matching refresh rates where possible and check for driver updates before assuming a hardware problem."
  - q: "Does Hardware-Accelerated GPU Scheduling help DWM usage?"
    a: "It can. Hardware-Accelerated GPU Scheduling (HAGS) lets the GPU manage its own memory scheduling instead of the CPU/DWM doing it, which reduces DWM overhead in some configurations — particularly with multiple high-refresh monitors. It's in Settings > System > Display > Graphics > Change default graphics settings. Results vary by GPU and driver version, so test it on and off rather than assuming."
---

`DWM.exe` — Desktop Window Manager — is supposed to use *some* GPU. It's the compositor that draws everything on your screen, and using the GPU for that is efficient by design. The problem is when Task Manager's GPU column shows DWM pinned at 30%, 50%, or higher while you're doing nothing visually demanding. That's not compositing — that's DWM working overtime because of a driver bug, a display configuration quirk, or an app forcing constant screen redraws. Here's how to find which one. For per-app GPU control, see [setting GPU preference per app](/articles/how-to-set-gpu-preference-per-app-on-windows-11/); for enabling [hardware-accelerated GPU scheduling](/articles/how-to-enable-hardware-accelerated-gpu-scheduling-in-windows-11-24h2/), which can reduce DWM overhead.

## Why this happens

- **Buggy or outdated GPU drivers**: The #1 cause — bad drivers make DWM's compositing path inefficient.
- **Mixed refresh-rate multi-monitor setups**: 60Hz + 144Hz forces extra synchronization work.
- **HDR enabled**: Tone mapping adds compositing cost, especially mixed HDR/SDR monitors.
- **An app forcing constant redraws**: Animated wallpapers, overlays, and buggy apps keep DWM compositing nonstop.
- **Stuck transparency/animation effects**: A hung animation keeps the compositor busy indefinitely.
- **Hardware-accelerated GPU scheduling off or buggy**: Depending on driver, either state can inflate DWM.
- **Integrated + discrete GPU confusion**: DWM on the wrong GPU, or constant handoff between them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm DWM is the real GPU consumer

Verify before changing drivers.

1. Open **Task Manager** > **Performance** tab > **GPU** and note overall utilization, then the **Processes** tab sorted by **GPU** — confirm **Desktop Window Manager** is the top consumer.
2. Check the **GPU Engine** column: DWM should use **GPU 0 – 3D** or **Copy** lightly at idle (a few percent). Sustained 30%+ at idle is abnormal.
3. Close all apps and watch for 5 minutes: if DWM GPU drops to near zero, an app was driving it (Fix 4). If it stays high with nothing open, it's driver/display-level (Fixes 2–3).
4. Note your display setup: count monitors, their refresh rates, and HDR status — multi-monitor and HDR are the big DWM multipliers.
5. Check **Settings** > **System** > **Display** > **Advanced display** for each monitor's refresh rate — mismatches are worth noting for Fix 3.

### Fix 2: Clean-install the GPU driver

The fix for the majority of DWM GPU cases.

1. Download the latest driver for your GPU: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel via the [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. For the thorough approach, use **DDU (Display Driver Uninstaller)** in Safe Mode to remove the old driver completely, then install the fresh one — this clears corrupted driver state that normal installs leave behind.
3. During NVIDIA/AMD install, choose **Custom** > check **Clean installation** if you'd rather not use DDU.
4. After installing, reboot and re-test DWM at idle before reinstalling GeForce Experience/Adrenalin extras — sometimes the extras (overlays, recording) are the actual trigger.
5. If the newest driver caused the problem, roll back: **Device Manager** > Display adapters > your GPU > **Properties** > **Driver** > **Roll Back Driver**.

### Fix 3: Simplify the display configuration

Reduce what DWM has to composite.

1. If you run mixed refresh rates (e.g., 144Hz gaming monitor + 60Hz secondary), try setting both to **60Hz** temporarily — if DWM GPU collapses, the mixed-rate sync cost was the cause; then decide your preferred tradeoff.
2. Turn off **HDR**: **Settings** > **System** > **Display** > **HDR** — test with it off, especially with mixed HDR/SDR monitors.
3. Disconnect secondary monitors one at a time to isolate whether a specific monitor/cable triggers it — a bad cable forcing constant re-negotiation shows up as DWM work.
4. Set a static desktop background instead of **Slideshow** or animated wallpaper — slideshow transitions and live wallpapers keep DWM compositing continuously.
5. In **Settings** > **Personalization** > **Colors**, turn off **Transparency effects** as a test — if DWM GPU drops sharply, a stuck transparency animation was likely.

### Fix 4: Find the app driving DWM

Some app is making DWM redraw constantly.

1. With DWM high, close apps one by one (especially: browsers with hardware acceleration, Discord/Steam overlays, screen recorders, animated wallpaper apps, RGB control software).
2. After each close, wait 60 seconds and check DWM's GPU — the drop identifies the trigger.
3. For browsers: toggle **hardware acceleration** off/on in the browser's settings (Chrome: Settings > System) — a bad interaction between browser compositing and DWM is common.
4. Disable **in-game/ desktop overlays** (GeForce Experience, Discord, Xbox Game Bar: Settings > Gaming > Xbox Game Bar > Off) — overlays inject into the compositing path.
5. Once identified, update that app, disable its overlay/animations, or replace it — don't blame DWM for an app's bad behavior.

### Fix 5: Toggle Hardware-Accelerated GPU Scheduling

Worth testing both ways.

1. Go to **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings**.
2. Note the current state of **Hardware-accelerated GPU scheduling**, then toggle it and reboot.
3. Test DWM GPU at idle and during typical use for a day in each state — on some driver/GPU combos HAGS reduces DWM overhead; on others it increases it.
4. Keep whichever setting gives lower sustained DWM usage; there's no universally correct answer, it depends on your GPU and driver version.
5. Also test **Variable refresh rate** on the same page — on some setups it interacts with DWM compositing cost.

### Fix 6: Check for deeper system issues

When drivers and displays don't explain it.

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` — DWM depends on system components these repair.
2. Check **Windows Update** for pending updates, including **optional driver updates** — Microsoft sometimes ships DWM/compositor fixes.
3. Monitor GPU temperature: if the GPU is overheating, throttling makes normal DWM work look like high utilization — clean dust, verify fans.
4. Test with a **clean boot** (`msconfig` > hide Microsoft services > disable all) to rule out third-party services injecting into the display path.
5. On laptops with dual GPUs, check the BIOS for a **discrete-GPU-only (MUX)** option — forcing one GPU can eliminate handoff overhead that inflates DWM. Check your maker's support page for BIOS updates too.

## Closing

DWM high GPU is DWM doing someone else's heavy lifting — usually a bad GPU driver, a demanding multi-monitor/HDR setup, or an app forcing endless redraws. Clean-install the driver, simplify the display config to isolate the trigger, and find the app if one is driving it. DWM itself is never the problem to remove; it's the messenger telling you something else is wrong.
