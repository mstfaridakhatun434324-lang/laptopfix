---
title: "How to Fix DWM High GPU Usage on an ASUS Laptop"
slug: how-to-fix-dwm-high-gpu-usage-on-asus-laptop
date: 2026-09-07
categories: ["performance"]
tags: ["dwm", "desktop window manager", "high gpu", "asus laptop", "gpu usage"]
description: "Desktop Window Manager eating GPU on your ASUS laptop? Fix dwm.exe high GPU usage with driver, Armoury Crate, and display-setting steps."
thumbnail: "/images/thumbs/how-to-fix-dwm-high-gpu-usage-on-asus-laptop.webp"
faqs:
  - q: "What is dwm.exe and why does it use the GPU?"
    a: "The Desktop Window Manager (dwm.exe) composites everything you see — windows, taskbar, transparency, animations — using the GPU. Some GPU usage (1–10%) is normal. High sustained usage (30%+) means the compositor is struggling: too many GPU-accelerated apps competing, a driver bug, a refresh-rate conflict, or the discrete GPU being forced on for desktop work it shouldn't handle."
  - q: "Is high DWM GPU usage dangerous?"
    a: "No — it's a performance problem, not a hardware threat. DWM can't damage your GPU. But it steals GPU time from games and creative apps (causing stutter), keeps the discrete GPU awake (draining battery), and spins up fans. On ASUS laptops with dual GPUs, it often signals the NVIDIA/AMD discrete GPU is active when the integrated GPU should be compositing."
  - q: "Why is DWM GPU usage high on ASUS laptops specifically?"
    a: "ASUS's Armoury Crate profiles and GPU modes (Eco/Standard/Ultimate) directly control which GPU drives the display. In Ultimate mode the discrete GPU handles everything including the desktop, so DWM's GPU usage appears on the NVIDIA/AMD GPU at higher levels. Misconfigured modes, outdated Armoury Crate, or a stuck discrete GPU are the ASUS-specific triggers."
  - q: "Can I disable the Desktop Window Manager?"
    a: "No — not on Windows 10/11. DWM is a core, mandatory component; killing dwm.exe just makes Windows restart it, and there's no supported off switch. Old guides about disabling it date from Windows 7. The fix is always reducing its workload or fixing the driver/mode configuration that makes it struggle."
---

Seeing `dwm.exe` — Desktop Window Manager — sitting at 30%, 50%, or higher GPU usage in Task Manager feels wrong. The thing that draws your windows shouldn't be working that hard just to draw windows. On ASUS laptops the story usually has a specific twist: dual-GPU switching. Your machine has both power-sipping integrated graphics and a discrete NVIDIA or AMD GPU, and DWM's GPU usage spikes when the wrong GPU is doing the compositing — or when the discrete GPU gets stuck awake.

Before touching anything, note which GPU shows the load: Task Manager > **Performance** > **GPU 0 / GPU 1**. DWM hammering the discrete GPU at idle is the classic ASUS misconfiguration. For the general (non-ASUS) deep dive see [Desktop Window Manager high GPU troubleshooting](/articles/desktop-window-manager-high-gpu-troubleshooting/); for the step-by-step variant see [fixing DWM high GPU usage step by step](/articles/how-to-fix-dwm-high-gpu-usage-step-by-step/).

## Why this happens

- **Wrong GPU mode in Armoury Crate**: Ultimate mode forces the discrete GPU to composite the desktop, inflating DWM's GPU numbers.
- **Discrete GPU stuck awake**: A background app holding the NVIDIA/AMD GPU active so DWM runs on it instead of integrated.
- **Outdated GPU drivers**: Driver bugs in the compositing path, especially after Windows feature updates.
- **Too many GPU-accelerated apps**: Browsers, Discord, Spotify, wallpaper engines saturating video memory DWM needs.
- **Refresh-rate/multi-monitor conflicts**: Mixed rates forcing DWM to work harder to composite.
- **Hardware-accelerated GPU scheduling bugs**: The HAGS toggle conflicting with certain driver versions.
- **Corrupt DWM/system state**: Damaged system files or a compositor stuck in a bad state after sleep/resume.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check which GPU DWM is actually using

The diagnosis that directs everything else.

1. Open Task Manager > **Performance** and identify **GPU 0** and **GPU 1** — note which is Intel/AMD integrated and which is NVIDIA/AMD discrete.
2. Go to **Processes**, enable the **GPU** column (right-click headers), find **Desktop Window Manager**, and see which GPU engine it's using.
3. Normal: DWM on the integrated GPU at low single digits. Problem: DWM on the discrete GPU at 20%+ while you're just on the desktop.
4. Also check the discrete GPU's overall utilization — if it's active at idle with DWM plus a few stray processes, something is keeping it awake.
5. Open **Armoury Crate** > **GPU Power Saving** (or **GPU Mode**) and note the current mode — Eco, Standard, or Ultimate. This is usually the whole story.

### Fix 2: Set the correct ASUS GPU mode

The ASUS-specific fix that resolves most cases.

1. In **Armoury Crate**, set GPU mode to **Standard** (dynamic switching) for daily use — the integrated GPU handles the desktop, the discrete GPU wakes only for games and heavy apps.
2. Use **Eco Mode** when on battery and doing light work — it fully disables the discrete GPU, guaranteeing DWM composites on integrated.
3. Reserve **Ultimate Mode** for gaming sessions only — it routes everything through the discrete GPU (by design), which is why DWM's GPU usage looks high there. It's not a bug in Ultimate mode; it's the mode doing what it says.
4. After switching modes, restart (Armoury Crate prompts for the mode change restart) — GPU mode switches need a reboot to fully take effect.
5. Verify in Task Manager: DWM should now show minimal usage on the integrated GPU, and the discrete GPU should idle at 0%.

### Fix 3: Find what's keeping the discrete GPU awake

Something is pinning the big GPU on.

1. In **Armoury Crate** or **NVIDIA Control Panel** > **Desktop** > **Display GPU Activity Icon in Notification Area** — the tray icon lists exactly which processes are using the discrete GPU.
2. Usual culprits: browsers with hardware acceleration, Discord/Spotify, wallpaper engine apps, and updaters that briefly touch the GPU and never let go.
3. Close suspects one by one and watch the GPU activity icon — when the discrete GPU goes idle, you've found it.
4. For browsers: **Settings** > **System** > toggle hardware acceleration and test both ways — or set the browser to the integrated GPU in **Windows Settings** > **System** > **Display** > **Graphics** > per-app GPU preference.
5. Update Armoury Crate itself from the Microsoft Store or ASUS support — old Crate versions mismanage GPU switching and leave the discrete GPU stranded awake.

### Fix 4: Update both GPU drivers properly

Dual-GPU laptops need both drivers healthy.

1. Update the **integrated** GPU driver via [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) (or AMD's page for AMD integrated) — this is the driver DWM should be using.
2. Update the **discrete** GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or AMD — do a **clean install** to remove remnants.
3. Prefer ASUS's own validated GPU drivers from the laptop maker's official support site if the generic vendor drivers cause switching glitches — ASUS customizes power behavior and their validated drivers sometimes switch more reliably.
4. After updating, re-test in Standard mode: DWM low on integrated, discrete at 0% idle.
5. If a new driver made it worse, roll back in **Device Manager** > GPU > **Properties** > **Driver** > **Roll Back Driver**.

### Fix 5: Reduce the compositing workload

Give DWM less to chew on.

1. **Settings** > **Personalization** > **Colors** > turn off **Transparency effects** — acrylic blur is the most expensive thing DWM does.
2. `sysdm.cpl` > **Advanced** > **Performance Settings** > uncheck animation entries (minimize/maximize animations, taskbar animations, menu fades).
3. Close GPU-hungry background apps while testing — every Electron app and browser window consumes VRAM DWM wants.
4. Disconnect external monitors temporarily — mixed refresh rates multiply DWM's compositing work; test on the laptop panel alone.
5. Toggle **Hardware-accelerated GPU scheduling** (**Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings**) — test both on and off; some driver versions stutter with it on.

### Fix 6: Reset the graphics stack and system files

For DWM stuck in a bad state.

1. Press **Win+Ctrl+Shift+B** to restart the graphics driver — screen blinks, DWM restarts fresh. Check usage immediately after.
2. Sign out and back in — this fully restarts the DWM session, clearing corruption that survives driver restarts.
3. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` from an elevated terminal — DWM depends on system files these repair.
4. If high DWM usage appears specifically after sleep/resume, update the BIOS from ASUS support — resume-time GPU reinitialization bugs are fixed in BIOS updates.
5. Check [Microsoft's Windows support](https://support.microsoft.com/en-us/windows) for known DWM issues in your build (`winver`) — some builds ship compositor regressions fixed by cumulative updates.

## Closing

On ASUS laptops, DWM high GPU usage is usually a GPU-mode story, not a Windows bug: Ultimate mode or a stuck discrete GPU puts desktop compositing on the wrong chip. Set Standard/Eco for daily use, evict whatever's keeping the discrete GPU awake, keep both GPU drivers current, and DWM drops back to the background whisper it's supposed to be. Check the GPU activity icon first — it names the culprit in seconds.
