---
title: "How to Fix Display Driver Stopped Responding in Windows 11 24H2"
slug: how-to-fix-display-driver-stopped-responding-in-windows-11-24h2
date: 2026-09-08
categories: ["drivers"]
tags: ["display driver stopped responding", "tdr error", "gpu crash", "windows 11 24h2"]
description: "Getting 'Display driver stopped responding and has recovered' on Windows 11 24H2? Six fixes for TDR crashes, from clean driver reinstalls to TDR delay tuning."
thumbnail: "/images/thumbs/how-to-fix-display-driver-stopped-responding-in-windows-11-24h2.webp"
faqs:
  - q: "What does 'display driver stopped responding and has recovered' actually mean?"
    a: "It's a Timeout Detection and Recovery (TDR) event: the GPU didn't answer Windows within about two seconds, so Windows reset the graphics driver instead of blue-screening. You see a brief black flicker and then the desktop returns. A one-off TDR after a driver update is harmless; repeated TDRs mean the driver, GPU scheduling, or hardware is genuinely struggling and needs the fixes in this guide."
  - q: "Can this error damage my graphics card?"
    a: "The TDR mechanism itself is protective — it resets the driver precisely to avoid a crash that could corrupt state. However, the underlying cause can matter: chronic overheating that triggers TDRs will shorten the GPU's life, and an unstable overclock behind the errors stresses the chip. Fix the cause rather than the symptom, and check temperatures while you troubleshoot."
  - q: "Why does it only happen in one game or app?"
    a: "Some applications push the GPU in ways that expose driver bugs — specific shader paths, rapid context switches, or heavy compute loads that the driver's scheduler mishandles. If TDRs are app-specific, update that app, toggle its graphics settings (especially hardware acceleration), and check the vendor's forums for known issues with your exact driver version before reinstalling the driver."
  - q: "Should I increase the TDR delay in the registry?"
    a: "Increasing TdrDelay can stop the resets if your GPU is simply slow to finish heavy work rather than truly hung — it's a legitimate fix for workstation and rendering workloads. But it's a mask, not a cure: if the GPU is genuinely crashing, a longer delay just postpones the reset. Apply it only after a clean driver reinstall and temperature check haven't helped."
---

The screen goes black for two seconds, the desktop stutters back, and a notification tells you the display driver stopped responding and has recovered. Once is a fluke. Twice a day is a pattern. Every time you open a game or a video call is a problem that needs fixing — and on Windows 11 24H2, this classic TDR (Timeout Detection and Recovery) error has some new twists, from hardware GPU scheduling conflicts to driver builds that don't play well with the 24H2 kernel.

Here's the technician's mental model: Windows gives the GPU roughly two seconds to complete its work. If the driver doesn't respond in time, Windows kills and restarts the graphics driver instead of crashing the whole system. That reset is the "recovered" part. The failure to respond, though, has a cause — a buggy driver build, the GPU being starved or overheated, a scheduling conflict, or (least often) a dying card. We'll isolate which one it is, in order of likelihood. If the driver is an NVIDIA card and installers are also failing, the [NVIDIA clean install guide](/articles/how-to-update-nvidia-drivers-clean-install-in-windows-11-24h2/) pairs well with this one.

## Why this happens

- **A buggy or corrupted graphics driver build.** The most common cause: the installed driver has a scheduling bug, or its files were corrupted during the 24H2 upgrade, so the GPU stops answering under load.
- **Hardware GPU scheduling conflicts.** 24H2 leans harder on hardware-accelerated GPU scheduling; on some driver builds this feature destabilizes the scheduler and triggers TDRs.
- **The GPU is overheating.** Dust-clogged fans or dried thermal paste push the GPU past its thermal limit, it throttles mid-task, misses the two-second window, and Windows resets the driver.
- **An unstable overclock or undervolt.** Factory or user overclocks that were stable on older drivers can become unstable on a new driver build's different voltage curves.
- **Conflicting overlays and capture software.** Screen recorders, Discord overlays, and monitoring tools inject into the graphics pipeline and can stall the driver.
- **Failing VRAM or GPU hardware.** Least common but real: degraded video memory causes the GPU to hang on specific operations, producing TDRs that no driver change fixes.
- **Power delivery problems.** An underpowered or failing charger/battery on a laptop can starve the discrete GPU during boost, causing exactly these resets.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Perform a clean reinstall of the graphics driver

Don't just update over the top — purge and reinstall.

1. Download the latest driver for your GPU: [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx), [AMD drivers](https://www.amd.com/en/support/download/drivers.html), or Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. During NVIDIA/AMD setup, choose **Custom** and check **Perform a clean installation** (NVIDIA) or **Factory Reset** (AMD).
3. For Intel or stubborn cases, use DDU (Display Driver Uninstaller) in Safe Mode first, then install fresh.
4. Restart and stress-test with the app that triggered the TDRs. This resolves the majority of cases.

### Fix 2: Toggle hardware-accelerated GPU scheduling

A 24H2-specific fix worth trying early.

1. Go to **Settings** > **System** > **Display** > **Graphics** > **Change default graphics settings**.
2. Toggle **Hardware-accelerated GPU scheduling** to the opposite of its current state.
3. Restart the laptop (the change requires a reboot).
4. Test for a day. If TDRs stop, leave it in the stable position — some driver builds only misbehave with one setting.

### Fix 3: Check GPU temperatures

Rule out heat before you blame software.

1. Install HWiNFO or use Task Manager's **Performance** > **GPU** tab to watch temperature under load.
2. Sustained temperatures above ~85–90°C on a laptop GPU during the triggering workload point to thermal throttling.
3. Clean the vents with compressed air, ensure the laptop sits on a hard flat surface, and consider a cooling pad.
4. If temps are fine, heat isn't your cause — move on. If they're high and cleaning doesn't help, the thermal paste or fans need professional service.

### Fix 4: Disable overlays and background capture

Strip the graphics pipeline down to isolate interference.

1. Turn off the Xbox Game Bar: **Settings** > **Gaming** > **Xbox Game Bar** > Off.
2. Disable Discord/Steam/NVIDIA overlays and any screen-recording software, at least temporarily.
3. In your browser, toggle hardware acceleration off and on to test (**Settings** > **System** in Edge/Chrome).
4. If TDRs stop with overlays off, re-enable them one at a time to find the offender.

### Fix 5: Increase the TDR delay (registry)

Give a slow-but-working GPU more time before Windows declares it hung.

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a DWORD (32-bit) named **TdrDelay** (if absent) and set it to **8** (decimal, = 8 seconds).
3. Optionally create **TdrDdiDelay** = **8** as well.
4. Restart. This helps workstation/rendering workloads where the GPU is legitimately busy, not hung.

### Fix 6: Reset overclocks and test the hardware

Eliminate instability at the silicon level.

1. Reset any GPU overclock/undervolt to stock (MSI Afterburner > reset, or vendor control panel defaults).
2. Run the triggering workload at stock clocks for a full day.
3. If TDRs persist across multiple clean driver versions at stock clocks with good temperatures, run your vendor's GPU diagnostics or a VRAM stress test.
4. Hardware-level TDRs that survive everything above mean the GPU needs warranty service — and the [Lenovo-specific display driver guide](/articles/how-to-fix-display-driver-stopped-responding-on-lenovo-laptop/) covers vendor diagnostics if you're on a Lenovo machine.

## Closing

TDR errors look scary but the fix is methodical: clean-reinstall the driver, toggle GPU scheduling, check heat, strip overlays, adjust the TDR delay, and finally suspect hardware. In that order, you'll find the cause instead of guessing at it. And once the resets stop, resist the urge to immediately reinstall the overlay stack or reapply the overclock — change one thing at a time so you know what actually fixed it.
