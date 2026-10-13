---
title: "The Best Way to Fix Lagging Animations in Windows 11"
slug: best-way-to-fix-windows-11-animations-lagging
date: 2026-10-10
categories: ["performance"]
tags: ["animations lagging", "windows 11", "visual effects", "ui lag", "stuttering"]
description: "Windows 11 animations stuttering when you minimize, snap, or switch windows? Here's the proven order of fixes, from visual-effects tuning to GPU drivers."
thumbnail: "/images/thumbs/best-way-to-fix-windows-11-animations-lagging.webp"
faqs:
  - q: "Why do Windows 11 animations lag on a fast laptop?"
    a: "Lagging animations are usually a graphics pipeline problem, not a CPU problem. Outdated GPU drivers, the desktop window manager struggling with mismatched refresh rates, or visual effects rendering on the integrated GPU instead of the discrete one all cause stutter. Even powerful laptops stutter if the driver is old or Windows is compositing the desktop at the wrong refresh rate."
  - q: "Will turning off animations make my laptop faster?"
    a: "Disabling animations removes the visible stutter and slightly reduces GPU load, so the system feels snappier — but it doesn't fix the underlying cause. Think of it as treating the symptom. The better approach is to fix the driver or refresh-rate issue first, then decide whether you prefer animations on or off as a matter of taste."
  - q: "Do I need a discrete GPU for smooth Windows 11 animations?"
    a: "No. Modern integrated graphics (Intel Iris Xe, AMD Radeon 780M, Apple-silicon-era equivalents on the Windows side) handle desktop compositing effortlessly. If animations lag on integrated graphics, something is misconfigured — usually the driver, the display refresh rate setting, or a power plan throttling the GPU — not a lack of hardware."
  - q: "Can a Windows update cause animation lag?"
    a: "Yes, and it happens regularly. Feature updates sometimes replace a working GPU driver with an older inbox version, reset the display refresh rate to 60 Hz on a 120 Hz panel, or re-enable transparency effects you had disabled. After any update that introduces stutter, check the refresh rate setting and GPU driver version first — those two cover most cases."
---

Few things make a powerful laptop feel cheap like stuttering window animations. You minimize a window and it judders down to the taskbar. You snap two apps side by side and the transition tears. Alt-tabbing feels like wading through mud. The CPU is barely awake, the SSD is fast, yet the interface itself lags — because Windows 11's animations live and die on the graphics pipeline, and that pipeline has several fragile links.

The best fix order is: refresh rate, GPU driver, visual effects, power plan, then deeper causes. Most people fix it at step one or two and never need the rest. Related guides: [disabling visual effects in Windows 11](/articles/how-to-disable-visual-effects-in-windows-11-24h2/) and [fixing slow Alt-Tab](/articles/how-to-fix-alt-tab-slow-windows-11-step-by-step/).

## Why this happens

- **Wrong display refresh rate**: Windows resets high-refresh panels to 60 Hz after updates, making every animation visibly choppier.
- **Outdated or generic GPU driver**: The Microsoft Basic Display Adapter or an old vendor driver can't composite smoothly.
- **Animations rendering on the wrong GPU**: The desktop compositor stuck on power-saving integrated graphics with bad drivers.
- **Transparency and blur effects**: Acrylic blur is GPU-expensive; on throttled or misconfigured GPUs it stutters.
- **Power plan throttling the GPU**: Battery-saver and efficiency modes that starve the GPU of clocks during light UI work.
- **Desktop Window Manager (DWM) overload**: Too many GPU-accelerated apps (browsers, Electron apps) saturating video memory.
- **Variable refresh rate / multi-monitor mismatch**: Mixed refresh rates across monitors force DWM to composite at the lowest common denominator.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Set the correct refresh rate

The single most common cause — check it first.

1. Go to **Settings** > **System** > **Display** > **Advanced display**.
2. Under **Choose a refresh rate**, select the highest your panel supports (120 Hz, 144 Hz, etc.) — if it says 60 Hz on a high-refresh laptop, you've found the problem.
3. If the higher option is missing, your GPU driver is likely generic (see Fix 2) — Windows can't expose rates the driver doesn't report.
4. On multi-monitor setups, set each display individually and test animations with only the laptop screen enabled first.
5. Note: some laptops only offer high refresh rates when plugged in — check both on battery and on AC power.

### Fix 2: Install the proper GPU driver

Never trust the inbox driver for smooth compositing.

1. Open **Device Manager** > **Display adapters** — if you see "Microsoft Basic Display Adapter," Windows is using a fallback driver and animations will always stutter.
2. Install the vendor driver: [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel, [NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx) for GeForce, AMD's driver page for Radeon.
3. Choose a **clean installation** if the installer offers it — this removes old driver remnants that can conflict.
4. Restart, then re-check the refresh rate setting from Fix 1 — the full range of rates should now appear.
5. Test animations immediately: minimize/maximize windows, snap layouts, and Alt-Tab. The difference after a proper driver is usually night and day.

### Fix 3: Tune visual effects (the right way)

Reduce the compositing load without making Windows look broken.

1. Press **Win+R**, type `sysdm.cpl`, go to **Advanced** > **Performance** > **Settings**.
2. Select **Custom** and keep checked: **Smooth edges of screen fonts**, **Show thumbnails instead of icons**, and **Smooth-scroll list boxes** — uncheck the animation entries (**Animate windows when minimizing and maximizing**, **Animations in the taskbar**, **Fade or slide menus into view**).
3. Go to **Settings** > **Personalization** > **Colors** and turn off **Transparency effects** — acrylic blur is the single most expensive visual effect.
4. Go to **Settings** > **Accessibility** > **Visual effects** and review the toggles there too — Windows 11 duplicates some settings across pages.
5. This is the fix detailed in our guide to [disabling visual effects in Windows 11](/articles/how-to-disable-visual-effects-in-windows-11-24h2/) if you want the full walkthrough with screenshots.

### Fix 4: Stop the power plan from throttling the GPU

Efficiency modes can starve the compositor.

1. Click the battery icon and set the power mode slider to **Best performance** (plugged in) as a test — if animations smooth out, power throttling was the cause.
2. Go to **Settings** > **System** > **Power & battery** > **Power mode** and set **Best performance** for plugged-in use permanently if you mostly work docked.
3. For NVIDIA laptops, open **NVIDIA Control Panel** > **Manage 3D settings** > **Power management mode** and set it to **Prefer maximum performance** — then check whether DWM stutter disappears.
4. In your laptop vendor's control app ( Armoury Crate, Legion Zone, OMEN Hub), make sure the active profile isn't an extreme silent/eco mode that clamps GPU clocks.
5. On battery, accept some trade-off — but **Balanced** should still animate smoothly; if it doesn't, the issue is elsewhere.

### Fix 5: Reduce DWM's workload

Free up the video memory the compositor needs.

1. Close GPU-heavy background apps while testing: browsers with hardware acceleration, Discord, Spotify, and wallpaper engines all consume VRAM the compositor wants.
2. In your browser, try toggling **hardware acceleration** off and on (**Settings** > **System**) — a misbehaving browser can saturate the GPU and make the whole desktop stutter.
3. Lower the resolution scaling if it's extreme — 200%+ scaling on a 4K panel multiplies compositing work.
4. Disconnect external monitors one at a time to test whether a mixed-refresh-rate setup is the trigger (Fix: run both at the same rate or use only one while testing).
5. Open Task Manager's **Performance** > **GPU** tab and watch **3D** and **Video Encode** graphs while triggering animations — sustained 100% during simple window moves means something is hogging the GPU.

### Fix 6: Reset the graphics stack

When the compositor itself is in a bad state.

1. Press **Win+Ctrl+Shift+B** — the screen will blink as Windows restarts the graphics driver. This is safe and instant; test animations right after.
2. If stutter returns after sleep or reboot, the driver is crashing and recovering badly — do a full clean reinstall with DDU (Display Driver Uninstaller) in Safe Mode, then install the vendor driver fresh.
3. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated terminal — corrupted system files can break DWM's composition path.
4. Create a new local user account and test animations there — if they're smooth, your main profile's settings or startup apps are the cause, not the system.
5. As a last resort, check [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) for known animation issues with your specific build — some Insider and feature-update builds ship with compositor regressions that only a patch fixes.

## Closing

Lagging animations are a graphics pipeline issue with a graphics pipeline fix order: refresh rate first, proper GPU driver second, visual-effects tuning third. Nine times out of ten the culprit is a 120 Hz panel stuck at 60 Hz or a generic display driver after an update. Fix the pipeline and the interface goes back to feeling instant — no hardware upgrade required.
