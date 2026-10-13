---
title: "How to Fix High DPC Latency in Windows 11: A Step-by-Step Guide"
slug: "how-to-fix-dpc-latency-high-windows-11-step-by-step"
date: "2026-10-01"
categories: ["performance"]
tags: ["dpc latency windows 11", "fix audio crackling", "latencymon guide", "stuttering fix windows 11", "driver latency"]
description: "Step-by-step DPC latency troubleshooting for Windows 11: measure with LatencyMon, identify the bad driver, and apply fixes in the right order."
thumbnail: "/images/thumbs/how-to-fix-dpc-latency-high-windows-11-step-by-step.webp"
faqs:
  - q: "How long should I run LatencyMon for a reliable result?"
    a: "At least 5 to 10 minutes of normal use, including the activity that triggers your symptoms (audio playback, gaming, video calls). Shorter runs miss intermittent spikes; the drivers that cause real-world glitches often spike in bursts minutes apart. For sleep/wake-related issues, include a full sleep and wake cycle inside the measurement window."
  - q: "LatencyMon says my system is unsuitable — should I panic?"
    a: "No. The red ‘unsuitable for real-time audio’ verdict is common on laptops and simply means some driver occasionally exceeds ideal thresholds. What matters is the magnitude and frequency: occasional 1000µs spikes are a minor annoyance, while sustained multi-millisecond spikes from one driver cause the audible/visible glitches worth fixing with this guide."
  - q: "Can Windows updates cause DPC latency to get worse?"
    a: "Yes, occasionally. Feature updates can replace your tuned manufacturer drivers with generic Windows Update versions that handle interrupts worse — a classic regression pattern. If latency spiked right after a Windows update, check Device Manager for driver dates: re-installing the manufacturer's driver over the newer-but-worse generic one usually restores the old behavior."
  - q: "Is disabling devices in Device Manager a valid fix?"
    a: "As a diagnostic step, yes — disabling a suspect device and re-testing proves causation quickly. As a permanent fix, only if you genuinely do not need the device (an unused discrete GPU or a broken webcam, for example). For devices you need, the permanent fix is an updated or reconfigured driver, not a disabled device."
---

When Windows 11 stutters — audio crackles, the mouse hitches, video frames drop — but Task Manager shows low CPU, the culprit is usually DPC latency: drivers taking too long to finish high-priority interrupt work, starving everything else of CPU time in microsecond bursts. It is invisible to normal monitoring and maddening to troubleshoot blind.

This guide is the methodical version: measure with the right tool, identify the exact driver, fix that driver, and verify the improvement — each step building on the last. No shotgun driver reinstalls, no registry voodoo, just diagnosis followed by targeted action.

## Why this happens

- **Outdated or buggy device drivers:** Audio, network, and storage drivers are the classic DPC offenders.
- **Generic Windows drivers instead of manufacturer ones:** Windows Update drivers often lack the tuning of vendor releases.
- **Power management conflicts:** Devices entering/exiting low-power states generate latency spikes.
- **USB device problems:** Faulty USB hardware or drivers poll excessively.
- **BIOS/firmware interrupt issues:** Fixed by updates on many laptop models.
- **Background software polling hardware:** Monitoring tools and RGB software hammering sensors.
- **Thermal throttling:** Heat slows interrupt handling across the board.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Establish a baseline with LatencyMon

Every fix in this guide is verified against LatencyMon measurements. Without a baseline you cannot tell whether a change helped, hurt, or did nothing — so measure first, carefully.

1. Download LatencyMon, run as administrator, and click Start.
2. Use the PC normally for 10 minutes: play audio, browse, move windows.
3. Record: the Main-tab verdict, highest DPC routine time, and the top 3 drivers by DPC count.
4. Save a screenshot — you will compare every later measurement against it.

### Fix 2: Identify the worst driver and research it

The Drivers tab names filenames like ndis.sys, dxgkrnl.sys, or HDAudBus.sys. The filename tells you the subsystem; Device Manager tells you the actual hardware behind it. Precision here prevents wasted effort.

1. Sort LatencyMon's Drivers tab by DPC count and Total execution time.
2. Note the top driver's filename and its reported driver (right-click > Properties).
3. Map it: ndis.sys = network, HDAudBus/audio = sound, storport = storage, dxgkrnl = graphics.
4. Search the filename plus your laptop model for known issues.

### Fix 3: Update that specific driver from the manufacturer

Now update exactly the implicated driver — from your laptop or motherboard manufacturer's support site, not Windows Update. Vendor drivers carry interrupt-handling fixes that generic builds lack. [Microsoft documents manual driver updates](https://support.microsoft.com/en-us/windows) if you need the official procedure.

1. Download the newest driver for the implicated device from the manufacturer.
2. In Device Manager, update the device using the downloaded driver (or run its installer).
3. Restart, then re-run the identical 10-minute LatencyMon test.
4. Compare numbers: a real fix shows the driver's DPC count and max time collapsing.

### Fix 4: Disable device power management for the suspect

If the offender is a network or USB device, its power-state transitions are likely generating the spikes. Disabling its power saving is a two-minute test with immediate verdict.

1. In Device Manager, open the suspect device's Properties.
2. On Power Management, untick ‘Allow the computer to turn off this device to save power.’
3. Check the Advanced tab for power-saving features and set them to Maximum Performance.
4. Re-run LatencyMon, including an idle-to-active transition in the test window.

### Fix 5: Isolate USB and background software

Two common amplifiers: bad USB hardware and software that polls hardware constantly (monitoring overlays, RGB controllers, old VPNs). Isolate both with a clean boot plus physical USB removal.

1. Unplug all non-essential USB devices and re-test with LatencyMon.
2. Then perform a clean boot (msconfig > hide Microsoft services > disable all; disable startup items).
3. If latency normalizes, re-enable software in halves to find the poller.
4. Remove or update whatever triggers the spikes.

### Fix 6: Update BIOS, chipset, and storage drivers

When no single driver stands out but baseline latency is uniformly high, the platform layer — BIOS interrupt routing, chipset drivers, storage controller — is the suspect. Updates here fix whole classes of latency at once.

1. Check for a BIOS update from your manufacturer; flash per their instructions exactly.
2. Install the latest chipset and storage (AHCI/NVMe) drivers.
3. Load BIOS defaults after flashing, then reapply your settings.
4. Run the full 10-minute LatencyMon comparison again.

### Fix 7: Verify the fix under real load

The final step is proof, not hope: re-run your exact baseline test and confirm the numbers improved, then stress the specific symptom (audio playback, gaming, video calls) that brought you here.

1. Repeat the identical 10-minute LatencyMon run from Fix 1.
2. Confirm the verdict improved and the worst driver's numbers dropped.
3. Test your actual symptom: play audio for 30 minutes, game for an hour.
4. If symptoms persist despite good numbers, the cause may be application-level — investigate the app, not drivers.

### Fix 8: Document your fix and monitor long-term

DPC latency regressions are common: a Windows update replaces your tuned driver, or a new peripheral introduces a chatty driver. Keeping notes turns the next incident from a day of detective work into a ten-minute driver reinstall. If the numbers ever degrade again, the [System Interrupts troubleshooting path](/articles/what-to-do-if-system-interrupts-high-cpu-windows-11/) uses the same LatencyMon evidence, and a general [performance baseline](/articles/laptop-running-slow-windows-11-how-to-speed-up/) helps spot wider slowdowns early.

1. Write down which driver was at fault and which version fixed it.
2. Save a LatencyMon screenshot of your healthy baseline numbers.
3. After each Windows feature update, spot-check latency for 5 minutes.
4. If latency returns, reinstall the known-good manufacturer driver first.

## Closing

DPC latency troubleshooting rewards method over speed: measure a baseline, name the driver, update that driver from the manufacturer, verify with the same test. Most cases resolve at step three — a single updated audio or network driver. The discipline of measuring before and after is what separates a permanent fix from weeks of random driver reinstalls.
