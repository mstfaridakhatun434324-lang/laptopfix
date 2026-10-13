---
title: "Windows 11 Animations Lagging on Lenovo Laptop? Smooth Them Out"
slug: "how-to-fix-windows-11-animations-lagging-on-lenovo-laptop"
date: "2026-09-01"
categories: ["performance"]
tags: ["animations lagging", "windows 11", "lenovo laptop", "ui lag", "dwm"]
description: "Window animations, Alt-Tab, and Start menu transitions stuttering on your Lenovo Windows 11 laptop? Here's how to diagnose UI lag and restore buttery-smooth animations."
thumbnail: "/images/thumbs/how-to-fix-windows-11-animations-lagging-on-lenovo-laptop.webp"
faqs:
- q: "Why are Windows 11 animations laggy on my laptop?"
  a: "Animation lag is usually caused by the GPU not handling desktop compositing properly — outdated graphics drivers, the system falling back to software rendering, Desktop Window Manager (DWM) under load, or power settings throttling the GPU. On Lenovo laptops, outdated Intel or NVIDIA drivers and aggressive battery-saver GPU throttling are the most common causes."
- q: "Will turning off animations make my laptop faster?"
  a: "Turning off animations makes the system *feel* snappier because windows appear instantly instead of animating, and it slightly reduces GPU load. But it masks the problem rather than fixing it — on a healthy system with proper drivers, animations should run at a smooth 60fps. Fix the underlying cause first, then decide if you prefer animations on or off."
- q: "What is Desktop Window Manager and does it affect animations?"
  a: "Desktop Window Manager (dwm.exe) is the compositing engine that renders all windows, transparency, and animations in Windows 11. Every animation you see passes through DWM, so when DWM is starved of GPU resources or bugged, animations stutter system-wide. High DWM GPU usage in Task Manager is the telltale sign."
- q: "Can a high refresh rate display cause animation lag?"
  a: "Ironically, yes — if the GPU can't sustain the display's refresh rate during compositing, animations look worse at 120Hz than at 60Hz. Mismatched refresh rates between internal and external displays can also cause stutter. If animations lag on a high-refresh panel, test at 60Hz to see if the GPU is the bottleneck."
---

Choppy minimize/maximize animations, a stuttering Task View, a Start menu that fades in like a slideshow — when Windows 11's UI stops being smooth, the whole laptop feels cheap and broken, even if apps themselves run fine. This is a compositing problem, not a CPU problem: your processor can be nearly idle while animations stutter, because the GPU pipeline that renders them is struggling.

On Lenovo laptops, the usual suspects are graphics drivers (Intel iGPU drivers especially), DWM getting starved, or power settings quietly throttling the GPU. The fixes are quick and the improvement is immediately visible.

## Why this happens

- **Outdated Intel/NVIDIA graphics drivers** — the compositor depends on the GPU driver; old drivers stutter on Windows 11's effects.
- **GPU throttled by power settings** — Battery Saver or balanced plans cap GPU clocks, starving DWM.
- **Desktop Window Manager overloaded** — too many GPU-hungry background apps (browsers with hardware acceleration, overlays) compete with the compositor.
- **Software rendering fallback** — if the GPU driver fails, Windows falls back to CPU rendering (WARP), which is dramatically slower.
- **High refresh rate the GPU can't sustain** — 120Hz+ panels demand more compositing power than weak iGPUs deliver under throttling.
- **Corrupt DWM state** — the compositor can get into a degraded state that persists until reset.
- **External display mismatch** — different refresh rates or scaling between displays confuses the compositor.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's the compositor, not the CPU

Verify the GPU pipeline is the bottleneck before changing drivers.

Steps:

1. Open Task Manager → Performance → GPU and watch GPU utilization while triggering animations (Win+Tab, minimize/maximize windows).
2. Check the "3D" or "Copy" engine — spikes during animations are normal; sustained 90%+ means the GPU is saturated.
3. Look at **Desktop Window Manager** in Processes → if its GPU usage is high, the compositor is struggling.
4. Also check CPU — if CPU is low while animations stutter, it's definitively a GPU/compositor issue.
5. Note your display refresh rate (Settings → System → Display → Advanced display) for Fix 6.

### Fix 2: Update graphics drivers from Lenovo

Lenovo validates GPU drivers for your exact model — use theirs first. Get them from [Lenovo support](https://support.lenovo.com/us/en/).

Steps:

1. Find your exact model and download the latest **Intel** (or AMD) graphics driver plus **NVIDIA** driver if you have discrete graphics.
2. Install the integrated graphics driver first, restart, then the discrete driver, restart.
3. For Intel-only systems, Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is a reliable alternative.
4. Avoid letting Windows Update downgrade you afterward — check the driver date in Device Manager after the next update cycle.
5. Test animations immediately — driver fixes show results instantly.

### Fix 3: Set GPU to maximum performance while plugged in

Stop power management from throttling the compositor's GPU.

Steps:

1. Settings → System → Power & battery → Power mode → **Best performance** (plugged in).
2. NVIDIA users: NVIDIA Control Panel → Manage 3D settings → Power management mode → **Prefer maximum performance**.
3. AMD users: AMD Adrenalin → Gaming → Graphics → similar power/performance preference.
4. Intel users: Intel Graphics Command Center → System → Power → set Plugged In plan to **Maximum Performance**, and disable Panel Self-Refresh if animations stutter (it can cause micro-hitches).
5. In Lenovo Vantage, set the thermal/performance mode to Performance.

### Fix 4: Reduce GPU competition from background apps

Free up the GPU so DWM isn't fighting for resources.

Steps:

1. In Task Manager → Processes, sort by GPU and identify non-essential heavy users (browsers with many tabs, Discord/Spotify overlays, wallpaper engines).
2. Close or limit them and retest animations.
3. In Chrome/Edge Settings → System, try toggling hardware acceleration — on weak iGPUs, browser GPU usage can starve the compositor.
4. Disable animated wallpaper engines and desktop overlay widgets while testing.
5. If animations smooth out, you've found your competition — keep those apps closed or limited.

### Fix 5: Reset DWM and toggle compositing features

Clear a degraded compositor state and test Windows' visual effects settings.

Steps:

1. Open Task Manager → find **Desktop Window Manager** → End task (it restarts automatically; screen will flicker).
2. Test animations after the restart.
3. Search "performance" → "Adjust the appearance and performance of Windows."
4. Ensure **"Animate windows when minimizing and maximizing"** and **"Animations in the taskbar"** are checked (unchecking hides the problem rather than fixing it — but note the difference).
5. Toggle **Transparency effects** off in Settings → Personalization → Colors — transparency is GPU-expensive; if this fixes it, your GPU was borderline.

### Fix 6: Match refresh rate to what the GPU can sustain

A 120Hz panel is only smooth if the compositor can deliver 120 frames.

Steps:

1. Settings → System → Display → Advanced display → try **60Hz** temporarily.
2. If animations become smooth at 60Hz, the GPU can't sustain the higher rate under current conditions (usually throttling-related — revisit Fix 3).
3. If using an external monitor, set both displays to the same refresh rate if possible.
4. Check scaling: mismatched scale factors (125% laptop + 100% external) force extra compositing work — try matching them.
5. For persistent DWM-specific high GPU problems, see our [DWM high GPU guide](/articles/how-to-fix-desktop-window-manager-high-gpu-in-windows-11-24h2/) for deeper fixes.

### Fix 7: Enable Hardware-Accelerated GPU Scheduling

HAGS lets the GPU manage its own memory scheduling, reducing compositor latency.

Steps:

1. Settings → System → Display → Graphics → Default graphics settings.
2. Turn **On** "Hardware-accelerated GPU scheduling."
3. Restart the laptop (required for the change to take effect).
4. Test animations — improvement is usually subtle but real on supported hardware.
5. If things get worse (rare, on very old iGPUs), turn it back off.

## Closing

Animation lag on a Lenovo Windows 11 laptop is a GPU-pipeline problem with a short suspect list: drivers, throttling, DWM contention. Fixes 2 and 3 resolve the large majority of cases, and you'll see the difference the moment you Win+Tab. Don't just disable animations and call it done — smooth compositing is the sign of a healthy graphics stack, and it's worth the fifteen minutes to get it right. If the whole system (not just animations) feels slow, our [Windows 11 speed-up guide](/articles/how-to-speed-up-windows-11-laptop/) is the next stop.
