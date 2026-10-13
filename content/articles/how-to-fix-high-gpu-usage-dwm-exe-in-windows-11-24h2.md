---
title: "DWM.exe High GPU Usage in Windows 11 24H2? Fix It"
slug: how-to-fix-high-gpu-usage-dwm-exe-in-windows-11-24h2
date: 2026-10-06
categories: ["performance"]
tags: ["dwm.exe high gpu", "desktop window manager", "windows 11 24h2", "gpu usage fix"]
description: "Desktop Window Manager (dwm.exe) eating your GPU in Windows 11 24H2? Diagnose why and apply proven fixes to bring GPU usage back to normal."
thumbnail: "/images/thumbs/how-to-fix-high-gpu-usage-dwm-exe-in-windows-11-24h2.webp"
faqs:
  - q: "What is dwm.exe and why is it using my GPU?"
    a: "Desktop Window Manager (dwm.exe) is the Windows process that draws everything you see: windows, transparency, animations, and the desktop itself. It legitimately uses the GPU because compositing the screen is graphics work. Normal usage is low — typically 1 to 5 percent. When it climbs to 20, 40, or higher and stays there, something is forcing it to constantly redraw the screen, such as a misbehaving app, a bad driver, or a stuck visual effect."
  - q: "Is high dwm.exe GPU usage dangerous?"
    a: "It is not dangerous in the sense of damaging hardware — GPUs are designed to run at full load. The real costs are heat, fan noise, and battery drain on laptops, plus stuttering in games and apps because dwm.exe is competing for GPU time. If your laptop gets hot and loud while doing nothing, dwm.exe GPU abuse is a likely suspect. Fixing it restores quiet operation and frees the GPU for work that actually needs it."
  - q: "Can I just end dwm.exe in Task Manager?"
    a: "You can, but Windows restarts it immediately — and killing it causes the screen to flicker or briefly go black as the compositor restarts. It is a diagnostic move at best, not a fix: if GPU usage drops after the restart but climbs back within minutes, you have confirmed something is driving it rather than dwm.exe itself being broken. The permanent fixes below target those drivers instead."
  - q: "Does disabling visual effects really help dwm.exe GPU usage?"
    a: "Yes, measurably. Transparency, animations, and shadows are exactly the work dwm.exe does on the GPU, so turning them off directly reduces its load. On systems where dwm.exe is misbehaving, disabling transparency effects alone can cut its GPU usage in half. You lose some visual polish, but on a laptop where battery life and quiet fans matter more than acrylic blur, it is a worthwhile trade."
---

You are not gaming, not editing video, not doing anything graphical — yet Task Manager shows dwm.exe (Desktop Window Manager) consuming 20, 40, even 70 percent of your GPU. The fans spin, the battery drains, and games stutter because the desktop compositor is hogging the graphics card. On Windows 11 24H2 this complaint has become notably more common, often appearing right after the feature update.

Dwm.exe is supposed to use the GPU — compositing your screen is graphics work. The problem is when it never stops. The usual drivers: outdated or mismatched GPU drivers from the 24H2 upgrade, a misbehaving app forcing constant screen redraws, or Windows visual effects piled onto a struggling driver. For related graphics tuning, see [enabling hardware-accelerated GPU scheduling](/articles/how-to-enable-hardware-accelerated-gpu-scheduling-in-windows-11-24h2/) and our [DWM high GPU after update guide](/articles/how-to-fix-desktop-window-manager-high-gpu-in-windows-11-24h2/).

## Why this happens

- **Outdated GPU drivers after the 24H2 update**: Feature updates frequently replace manufacturer graphics drivers with older generic ones that mishandle the compositor's workload.

- **A misbehaving app forcing redraws**: Apps with broken hardware acceleration or runaway animations make dwm.exe recomposite the screen dozens of times per second.

- **Visual effects overload**: Transparency, animations, and shadows multiply the per-frame work dwm.exe must do on the GPU.

- **Multiple displays at mismatched refresh rates**: Mixed 60Hz/144Hz monitor setups force the compositor into expensive synchronization work, especially on laptops with external displays.

- **Hardware-accelerated GPU scheduling issues**: HAGS changes how the GPU scheduler works; on some driver versions it increases dwm.exe overhead instead of reducing it.

- **Corrupt graphics driver installation**: A driver that installed halfway — common during feature updates — produces exactly this kind of constant low-level GPU churn.

- **HDR or variable refresh rate conflicts**: HDR and VRR handshakes that never settle keep the compositor re-negotiating display state in a loop.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm dwm.exe is the real GPU consumer

Task Manager's GPU column can mislead; verify properly before changing drivers.

1. Open **Task Manager > Performance > GPU** and note overall GPU utilization and temperature.
2. Switch to the **Processes** tab, right-click the column headers, and enable the **GPU** column if hidden; sort by it.
3. Confirm dwm.exe is genuinely the top consumer and note whether the usage is constant or spiking.
4. Check which GPU it is using on multi-GPU laptops (integrated vs discrete) — dwm.exe should normally sit on the integrated GPU.
5. If a game or browser is actually the top consumer and dwm.exe is second, fix that app first; the compositor is often just collateral.

### Fix 2: Update GPU drivers cleanly

This single step resolves the majority of dwm.exe GPU cases, especially post-24H2.

1. Identify your GPU: **Device Manager > Display adapters** (Intel, NVIDIA, AMD, or a combination).
2. Download the latest driver: NVIDIA from [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx), AMD from [AMD's driver support](https://www.amd.com/en/support/download/drivers.html), Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) — or your laptop maker's support site for OEM-tuned versions.
3. Choose **Custom/Advanced install** and check **Clean installation** (NVIDIA) or use DDU in Safe Mode for a truly fresh start on stubborn cases.
4. Restart and recheck Task Manager: dwm.exe GPU should drop to low single digits at idle.
5. If the newest driver is worse (it happens), roll back: **Device Manager > Display adapters > Properties > Driver > Roll Back Driver**.

### Fix 3: Trim Windows visual effects

Every transparency and animation is GPU work dwm.exe must perform; reducing them cuts its load directly.

1. Go to **Settings > Personalization > Colors** and turn off **Transparency effects**.
2. Open **Settings > Accessibility > Visual effects** and turn off **Animation effects**.
3. For the full treatment: search **Adjust the appearance and performance of Windows**, select **Adjust for best performance**, then re-enable only **Smooth edges of screen fonts**.
4. Restart dwm.exe to apply cleanly: in Task Manager's **Details** tab, right-click **dwm.exe > End task** (screen flickers briefly; it restarts automatically).
5. Compare GPU usage before and after — on affected systems this alone can halve dwm.exe's load.

### Fix 4: Hunt down the app forcing redraws

Dwm.exe often works hard because some application keeps invalidating the screen.

1. In Task Manager, sort processes by GPU and look for non-system apps with constant GPU activity — browsers, chat apps, and overlays are frequent offenders.
2. Close candidate apps one at a time and watch dwm.exe's GPU column for 30 seconds after each.
3. Pay special attention to apps with hardware acceleration settings (Discord, Slack, Chrome, Spotify) — toggle their hardware acceleration off as a test.
4. Disable overlays: NVIDIA GeForce Experience overlay, Discord overlay, Xbox Game Bar (**Settings > Gaming > Xbox Game Bar > Off**).
5. When you find the app, update it or leave its acceleration disabled; the app was the problem all along.

### Fix 5: Toggle Hardware-Accelerated GPU Scheduling

HAGS changes GPU scheduling behavior; on some 24H2 driver combinations it inflames dwm.exe instead of helping.

1. Go to **Settings > System > Display > Graphics > Change default graphics settings**.
2. Toggle **Hardware-accelerated GPU scheduling** to the opposite of its current state.
3. Restart the laptop (required for the change to take effect).
4. Check dwm.exe GPU at idle for several minutes; keep whichever setting gives lower usage.
5. Note the winning setting — after future driver updates, retest, since the ideal value can flip with new drivers.

### Fix 6: Fix multi-display and HDR conflicts

External monitors are a classic dwm.exe GPU trigger on laptops.

1. Disconnect external displays temporarily and check whether dwm.exe GPU drops — if yes, the display configuration is involved.
2. In **Settings > System > Display > Advanced display**, set all monitors to the same refresh rate if possible (mismatched 60/144Hz is the worst case).
3. Turn off **HDR** (**Settings > System > Display > HDR**) as a test; re-enable only if it proves innocent.
4. Update your monitor's color profile and try a different cable/port (a flaky DisplayPort handshake causes renegotiation loops).
5. If you use variable refresh rate, test with it off in both Windows settings and the monitor's OSD.

### Fix 7: Repair or reinstall Windows graphics components

For dwm.exe GPU abuse that survives driver updates, the OS graphics stack itself may be damaged.

1. Run **DISM /Online /Cleanup-Image /RestoreHealth** then **sfc /scannow** in an elevated terminal and restart.
2. Reinstall the GPU driver using DDU (Display Driver Uninstaller) in Safe Mode for a completely clean slate, then install the latest stable driver.
3. Check **Settings > Windows Update** for optional driver updates that may carry compositor-related fixes.
4. As a final measure, an in-place upgrade (reinstalling Windows 11 while keeping files and apps, via Microsoft's official Windows 11 download page) rebuilds the graphics stack cleanly.
5. If a clean Windows still shows runaway dwm.exe GPU at idle, suspect hardware — a failing GPU or display cable — and contact your laptop maker's support.

## Closing

Dwm.exe using your GPU is normal; dwm.exe abusing your GPU is a driver, app, or settings problem. Update graphics drivers cleanly, trim the visual effects, find the app forcing constant redraws, and sort out multi-display conflicts. In that order, these steps resolve nearly every case of runaway Desktop Window Manager GPU usage on 24H2.
