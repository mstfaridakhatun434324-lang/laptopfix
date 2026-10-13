---
title: "How to Fix HDMI Not Working on a Laptop in Windows 11 24H2"
slug: how-to-fix-hdmi-not-working-on-laptop-in-windows-11-24h2
date: 2026-09-17
categories: ["drivers"]
tags: ["hdmi not working laptop", "hdmi no signal windows 11", "hdmi driver fix"]
description: "HDMI not working on your laptop after Windows 11 24H2? Fix no-signal, undetected displays, and HDMI audio with these driver and hardware checks."
thumbnail: "/images/thumbs/how-to-fix-hdmi-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why does my HDMI show no signal on Windows 11 24H2?"
    a: "No signal usually means the monitor is on the wrong input, the cable is faulty, or the graphics driver is not driving the HDMI port after the 24H2 update. Work through input, cable, and driver checks in that order — the cause is almost always one of those three."
  - q: "Should the HDMI work without installing any driver?"
    a: "Basic HDMI output works with Windows' built-in display driver, but full functionality — correct resolutions, refresh rates, and HDMI audio — needs the proper GPU driver. After 24H2, reinstalling the Intel, NVIDIA, or AMD driver fixes most HDMI failures. If HDMI worked before the 24H2 update and broke immediately after, skip straight to the driver reinstall — that timing is diagnostic."
  - q: "Why does HDMI video work but there is no sound?"
    a: "HDMI audio is a separate endpoint that Windows must select as the output device. Right-click the speaker icon, open sound output options, and choose the TV or monitor (often labeled with the display's name). Also check that the display's own volume is up."
  - q: "Can a Windows update really break a physical HDMI port?"
    a: "It cannot damage the port, but it can break the driver that controls it — which looks identical from the outside. If HDMI died immediately after the 24H2 update and the port worked before, the driver is overwhelmingly the likely cause."
---

HDMI is supposed to be plug-and-play: cable in, picture appears. When it does not — "no signal" on the TV, Windows oblivious to the display, or video without audio — the failure hides in one of three places: the physical chain (port, cable, input), the display settings, or the graphics driver that 24H2 just replaced. On Windows 11 24H2, the driver is the prime suspect when HDMI worked before the update and died after.

This guide runs the full HDMI diagnostic in the order that wastes the least time: physical checks first (they are free), then Windows settings, then the driver repairs that fix update-broken HDMI ports.

## Why this happens

- **Wrong input on the display:** The TV or monitor listens on HDMI 1 while the cable sits in HDMI 2.
- **Faulty HDMI cable:** Damaged or out-of-spec cables fail the handshake, especially at 4K or high refresh rates.
- **24H2 graphics driver regression:** The update's driver does not initialize the HDMI output correctly.
- **Display not detected by Windows:** The driver fails EDID enumeration, so Windows never sees the display.
- **HDMI audio endpoint not selected:** Video works but sound routes to laptop speakers because the HDMI audio device is not the default.
- **Port disabled in BIOS:** Firmware toggles for the discrete GPU or external outputs affect HDMI on some laptops.
- **HDMI port hardware failure:** Worn or damaged ports lose pin contact — the genuine hardware case.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the display input and reseat the cable

The free fixes that resolve a large share of "no signal" reports.

1. Use the TV/monitor remote or buttons to cycle through **all** HDMI inputs — HDMI 1, 2, 3, and any ARC-labeled port.
2. Unplug the HDMI cable at both ends, inspect for bent pins or debris, and firmly reseat it.
3. Power-cycle the display: unplug its power for 30 seconds, then plug back in.
4. Try a different HDMI port on the display if one exists.

Test the cable and display with another device (game console, another laptop) if possible — that single test splits the problem into "laptop side" or "display side" instantly.

### Fix 2: Try a known-good cable

HDMI cables fail silently and often.

1. Swap in a different HDMI cable, preferably a certified High Speed or Ultra High Speed cable.
2. For 4K or 144Hz+ output, cable quality genuinely matters — cheap cables that worked at 1080p fail at higher bandwidths.
3. Keep cable length reasonable; passive cables beyond ~3 meters are suspect at high resolutions.

If the display springs to life with another cable, replace the old one rather than fighting it. For broader multi-display issues, our [second-monitor detection guide](/articles/best-way-to-fix-second-monitor-not-detected-windows-11/) covers the Windows side in depth.

### Fix 3: Force Windows to detect the display

Windows sometimes needs an explicit push, especially after updates.

1. Press **Win + P** and select **Duplicate** or **Extend**.
2. Go to **Settings > System > Display** and click **Detect** — click it two or three times.
3. Scroll to **Advanced display** and check whether the HDMI display appears as an option.

If **Win + P** offers only "PC screen only," the graphics driver is not exposing the HDMI output — proceed to the driver fixes.

### Fix 4: Clean-reinstall the graphics driver

The definitive fix for 24H2-broken HDMI.

1. Identify which GPU drives your HDMI port: on most laptops it is the **Intel** integrated GPU; on gaming laptops in dGPU mode it may be **NVIDIA**.
2. Download the driver: [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA drivers](https://www.nvidia.com/Download/index.aspx), or [AMD drivers](https://www.amd.com/en/support/download/drivers.html) — or the validated driver from your laptop maker's support page.
3. Install with the **Clean installation** option (or DDU in Safe Mode for stubborn cases) and restart.
4. Reconnect the HDMI cable and test.

On hybrid-graphics laptops, update the Intel driver first — it owns display output multiplexing even when the NVIDIA GPU renders the frames. Related port issues are covered in our [HDMI troubleshooting hub](/articles/best-way-to-fix-hdmi-not-working-on-laptop/).

### Fix 5: Fix HDMI audio separately

Video working but no sound is an audio-routing problem, not an HDMI failure.

1. Click the speaker icon in the taskbar and open the sound output selector.
2. Choose the TV/monitor entry (usually named after the display, e.g., "SAMSUNG" or "LG TV").
3. Go to **Settings > System > Sound**, select the HDMI device, and confirm its volume is up.
4. Check the display's own volume and mute state with its remote.

If the HDMI audio device does not appear, the graphics driver install in Fix 4 was incomplete — the GPU driver package includes the HDMI audio driver, so reinstalling it restores both.

### Fix 6: Check BIOS display output settings

Firmware controls which GPU drives the HDMI port on some laptops.

1. Reboot into BIOS/UEFI setup.
2. Look for **Graphics**, **Display**, or **Hybrid graphics** options. Ensure external display outputs are enabled.
3. On gaming laptops, try switching between **Hybrid** and **Discrete GPU only** modes — some HDMI ports are wired to the NVIDIA GPU and only activate in dGPU mode.
4. Save, boot into Windows, and retest.

Remember the original setting; dGPU-only mode fixes HDMI at the cost of battery life.

### Fix 7: Test the port hardware

The final determination for a port that survives all software fixes.

1. Boot a Linux live USB and test HDMI there — if it works in Linux, Windows software is still the problem; if it fails there too, the port hardware is suspect.
2. Inspect the laptop's HDMI port with a flashlight for bent pins, debris, or looseness.
3. Try the same cable and display on another laptop to triple-confirm the display side.
4. A physically damaged port needs professional repair — HDMI ports are soldered to the motherboard.

The Linux live-USB test is the gold standard for separating software from hardware: it uses completely different drivers, so whatever happens there is about the hardware.

## Closing

HDMI failures on Windows 11 24H2 follow a clear pattern: verify the display input and cable first, force Windows detection second, and clean-reinstall the graphics driver third — that sequence resolves the no-signal and undetected-display cases on the vast majority of laptops. Handle HDMI audio as its own routing step, and only suspect the physical port after the Linux live-USB test says so.
