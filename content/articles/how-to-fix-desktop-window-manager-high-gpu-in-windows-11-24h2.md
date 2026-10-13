---
title: "Desktop Window Manager High GPU in Windows 11 24H2? Fix It"
slug: how-to-fix-desktop-window-manager-high-gpu-in-windows-11-24h2
date: 2026-10-02
categories: ["performance"]
tags: ["dwm.exe", "desktop window manager", "high gpu", "windows 11 24h2"]
description: "dwm.exe hogging your GPU in Windows 11 24H2? Fix Desktop Window Manager's high GPU usage — drivers, effects, and app culprits explained."
thumbnail: "/images/thumbs/how-to-fix-desktop-window-manager-high-gpu-in-windows-11-24h2.webp"
faqs:
  - q: "What is Desktop Window Manager (dwm.exe)?"
    a: "Desktop Window Manager is the Windows compositing engine — it draws every window, the taskbar, transparency, animations, and thumbnails to the screen via the GPU. It's essential; Windows can't run its modern interface without it. Normal GPU usage is 0–5%, spiking briefly when you move windows or trigger animations. Sustained high GPU from dwm.exe means something is forcing it to recompose constantly — usually a misbehaving app, a driver bug, or excessive visual effects."
  - q: "Is dwm.exe a virus?"
    a: "The legitimate dwm.exe lives in C:\\Windows\\System32 and is a core Windows component. Malware occasionally disguises itself with the same name in other locations. Verify: in Task Manager, right-click Desktop Window Manager > Open file location — it must resolve to System32. If it's anywhere else, run a Microsoft Defender Offline scan immediately. In 99% of high-GPU cases, though, it's the real dwm.exe being overworked, not malware."
  - q: "Can I just disable Desktop Window Manager?"
    a: "No — not on Windows 11. DWM is mandatory for the entire modern UI; disabling it was possible back in Windows 7 with Aero off, but Windows 10/11 have no supported way to turn it off, and killing the process just makes Windows restart it. The correct approach is reducing its workload: fewer transparency/animations, updated drivers, and finding the app that's forcing constant recomposition."
  - q: "Why did dwm.exe GPU usage spike after the 24H2 update?"
    a: "Feature updates reset visual-effect settings, replace GPU drivers with older builds, and re-enable background apps — all of which raise DWM's workload. 24H2 also introduced changes to the compositing stack that exposed bugs in some older GPU drivers. The standard post-update pattern: a driver that's now mismatched with the compositor. Updating to the latest vendor GPU driver resolves most 24H2-era dwm.exe spikes."
---

`dwm.exe` — Desktop Window Manager — sitting at 30%, 60%, even 90% GPU in Task Manager while you're just staring at the desktop is wrong. DWM is the compositor that draws your windows, and at idle it should barely sip GPU. When it doesn't, something is making it redraw the screen thousands of times a second: a flickering app, a driver bug, HDR misbehaving, or a stack of visual effects the update re-enabled.

You can't kill DWM (Windows just restarts it), so the fix is reducing what drives it: update the graphics driver, calm the visual effects, find the app forcing recomposition, and check the known 24H2-specific triggers. For CPU-side compositor-adjacent issues, see [Antimalware Service Executable high CPU](/articles/antimalware-service-executable-high-cpu-windows-11/); for graphics scheduling, [enabling HAGS](/articles/how-to-enable-hardware-accelerated-gpu-scheduling-on-windows-11/).

## Why this happens

- **Outdated or mismatched GPU driver**: The #1 cause — especially after 24H2 replaced your vendor driver.
- **App forcing constant redraws**: A flickering widget, animated wallpaper engine, or buggy overlay makes DWM recompose endlessly.
- **Excessive visual effects**: Transparency, animations, and blur all cost compositing work; updates re-enable them.
- **HDR or multi-monitor mismatch**: HDR toggling, mixed refresh rates, or resolution scaling bugs spike DWM load.
- **Hardware-accelerated app overlays**: Discord overlay, GeForce Experience overlay, or screen recorders hook the compositor.
- **Corrupt driver or compositor state**: Occasionally the driver stack itself wedges and needs a clean reinstall.
- **Second GPU confusion on hybrids**: DWM bouncing between iGPU and dGPU on laptops with dual graphics.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify it's the real dwm.exe and check the pattern

Rule out malware and understand the load.

1. In **Task Manager**, right-click **Desktop Window Manager** > **Open file location** — it must be `C:\Windows\System32\dwm.exe`. Anywhere else = malware; run a Defender Offline scan.
2. Switch Task Manager to the **Performance** > **GPU** tab and watch which engine dwm.exe uses (3D, Video Decode, Copy) — this hints at the workload type.
3. Note the pattern: constant high GPU vs. spikes when moving the mouse or switching windows vs. high only with a specific app open.
4. If it's high only with one app open, that app is the trigger — skip to Fix 4.
5. Check **Settings** > **Windows Update** > **Update history** — if a recent update precedes the spike, suspect the driver swap (Fix 2).

### Fix 2: Clean-install the latest GPU driver

The fix for most 24H2 dwm.exe spikes.

1. Identify your GPU (Task Manager > Performance > GPU, or `dxdiag`).
2. Download the latest: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html).
3. Install with **clean installation** (NVIDIA) or factory reset (AMD) — critical, because the goal is removing the update-installed driver completely.
4. For the deepest clean, use **DDU (Display Driver Uninstaller)** in Safe Mode before installing the fresh driver — this wipes every remnant.
5. Reboot and watch dwm.exe at idle for 10 minutes — driver-caused spikes usually vanish immediately.

### Fix 3: Reduce compositing workload (visual effects)

Less for DWM to draw, less GPU it needs.

1. **Settings** > **Personalization** > **Colors** — turn off **Transparency effects**.
2. **Settings** > **Accessibility** > **Visual effects** — turn off **Animation effects**.
3. **Settings** > **System** > **About** > **Advanced system settings** > **Performance** > **Settings** > choose **Adjust for best performance** (or Custom with animations/shadows off).
4. Right-click desktop > **Personalize** > **Background** — if using **Slideshow**, switch to **Picture**; slideshows force periodic full recomposition.
5. Uninstall or disable animated wallpaper engines (Wallpaper Engine, Lively) as a test — they're constant DWM workload by design.

### Fix 4: Find the app forcing recomposition

One bad app can drive the whole compositor.

1. Close apps one by one while watching dwm.exe GPU in Task Manager — when it drops, you've found it.
2. Usual suspects: desktop widgets (rainmeter-style), overlay apps (Discord overlay, FPS counters), screen-recording tools left running, buggy Electron apps with animations, and browsers with hardware acceleration glitching.
3. For the suspect app: update it, disable its overlay/animations, or toggle its hardware acceleration setting off.
4. Check **Startup apps** and kill the suspect's auto-start if it's something you don't need resident.
5. Browsers: test with hardware acceleration toggled the other way (**Settings** > **System** in Chrome/Edge) — a glitching GPU process forces DWM to work overtime.

### Fix 5: Fix HDR and multi-monitor triggers

Display configuration is a classic DWM stressor.

1. **Settings** > **System** > **Display** > **HDR** — if HDR is on and dwm.exe is high, toggle it off as a test; HDR compositing bugs in some driver versions spike DWM.
2. For multi-monitor: set all displays to their **native resolution** and try matching refresh rates where possible — mixed 60Hz/144Hz setups have caused DWM bugs historically.
3. **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings** — toggle **Hardware-accelerated GPU scheduling** and test both states (reboot between).
4. Disconnect secondary monitors one at a time as a diagnostic — if DWM calms with one display, it's a multi-monitor compositing bug; update drivers and retest.
5. Check monitor cables too — a flaky DisplayPort/HDMI connection causing repeated re-detection forces DWM re-initialization loops.

### Fix 6: Disable problematic overlays and hooks

Overlays inject into the compositing path.

1. Turn off the **Xbox Game Bar** (**Settings** > **Gaming** > **Xbox Game Bar**) if you don't use it.
2. Disable **Discord overlay** (Discord > Settings > Game Overlay), **GeForce Experience/AMD Adrenalin in-game overlay**, and any FPS-overlay tools as a test.
3. Disable screen-recording utilities' background hooks (OBS virtual camera left on, etc.).
4. Third-party "window manager" or "desktop enhancement" tools (fancy window snapping, transparency tools) hook DWM directly — disable as a test.
5. Re-enable one at a time after DWM calms to identify the specific offender.

### Fix 7: Reset the graphics stack

When nothing targeted works.

1. In **Device Manager** > **Display adapters**, right-click your GPU > **Disable device**, wait 10 seconds, **Enable device** — this restarts the driver stack without a reboot.
2. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Terminal — compositor files are protected system files.
3. As a final software step, do an in-place Windows repair install from Microsoft's official Windows 11 download page, keeping files and apps.
4. On hybrid laptops, also update the *other* GPU's driver (iGPU if you updated dGPU and vice versa) — DWM uses both.
5. If dwm.exe still hogs GPU after all this on a clean driver, test with a different monitor/cable — and consider that the GPU itself may be failing.

## Closing

Desktop Window Manager high GPU in 24H2 is a workload problem, not a DWM problem: something — usually a replaced GPU driver, a flickering app, an overlay, or a stack of re-enabled visual effects — is forcing the compositor to redraw constantly. Clean-install the vendor driver, strip the effects, hunt the triggering app by elimination, and check HDR/multi-monitor configs. DWM itself is innocent; it's just doing what it's told, very expensively.
