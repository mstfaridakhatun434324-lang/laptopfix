---
title: "High DPC Latency on Windows 11? Fix Audio Stutters and Dropouts"
slug: what-to-do-if-dpc-latency-high-windows-11
date: 2026-10-08
categories: ["performance"]
tags: ["dpc latency", "latency", "audio stutter", "drivers", "windows 11"]
description: "Audio crackling, mouse stuttering, video hitching? High DPC latency means a driver is hogging the kernel. Here's how to find it and fix it."
thumbnail: "/images/thumbs/what-to-do-if-dpc-latency-high-windows-11.webp"
faqs:
  - q: "What is DPC latency and why does it cause stuttering?"
    a: "Deferred Procedure Calls are kernel-level tasks drivers schedule; high DPC latency means a driver is holding the CPU at kernel priority too long, delaying everything else — audio buffers underrun (crackles), the mouse stutters, video hitches. It is measured in microseconds with tools like LatencyMon. Spikes above 1000µs cause audible glitches; sustained high latency makes the whole system feel broken."
  - q: "Which drivers most commonly cause high DPC latency?"
    a: "The usual suspects: network drivers (Wi-Fi and Ethernet, especially power-saving features), storage controller drivers (storport, NVMe), GPU drivers, and USB drivers. On laptops, the Wi-Fi driver is the number-one offender — its power management constantly interrupts. Audio interface drivers and badly written peripheral drivers (RGB software, capture cards) are frequent runners-up."
  - q: "Is LatencyMon safe to use for diagnosing this?"
    a: "Yes, LatencyMon by Resplendence is the standard diagnostic tool — it only measures, changing nothing. Run it for 5 to 10 minutes during normal use (including the stuttering activity), then check the Drivers tab sorted by DPC count and execution time. The driver at the top is your prime suspect. It's free for this diagnostic use."
  - q: "Can Windows updates cause DPC latency spikes?"
    a: "Yes — Windows Update frequently replaces vendor-tuned network, storage, or GPU drivers with generic or newer-but-buggier versions, and latency problems often start the day after. If your stuttering began right after an update, the driver rollback path (Device Manager, Roll Back Driver) is the first fix to try, before any deeper investigation."
---

High DPC latency is the ghost in the machine: Task Manager shows low CPU, yet audio crackles, the cursor micro-stutters, and video hitches every few seconds. The system isn't overloaded — it's being interrupted. A misbehaving driver is holding the kernel too long on each pass, and everything time-sensitive starves. Gamers, musicians, and video-callers feel it first, but once you know the signature, you recognize it everywhere.

The fix is a driver hunt, and there's a standard tool for it. This guide walks the full path: measure, identify the driver, and fix or replace it.

## Why this happens

- **Wi-Fi driver power management:** The top offender — aggressive power-saving in wireless drivers generates constant high-priority interrupts.
- **Storage driver issues:** NVMe/storport drivers with bugs or wrong versions stall the kernel on I/O completion.
- **GPU driver DPC spikes:** Certain GPU driver versions are notorious for millisecond-scale DPC execution during rendering.
- **USB driver and device chatter:** A malfunctioning USB device (or its driver) spamming interrupts — docks and audio interfaces are classic.
- **Network driver offload bugs:** Faulty TCP offload or interrupt moderation settings in Ethernet/Wi-Fi drivers.
- **RGB and peripheral bloatware:** Poorly written drivers from peripheral utilities (RGB control, macro software) poll hardware constantly.
- **BIOS/firmware bugs:** Interrupt routing or power-state bugs in firmware that no driver update can fix — only a BIOS update.
- **Windows Update driver replacements:** Vendor-tuned drivers overwritten by generic or regressed versions overnight.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure with LatencyMon and identify the driver

Download LatencyMon (Resplendence, free), run it as administrator, press Play, and use the laptop normally for 5–10 minutes — include the activity that stutters (play audio, move the mouse, stream video). Then check the Drivers tab sorted by DPC execution time: the driver with the highest total is your prime suspect. Note its exact filename (e.g., ndis.sys implicates network, storport.sys implicates storage, nvlddmkm.sys implicates NVIDIA). Everything after this targets that specific driver. For the related system-interrupts variant, see [System Interrupts high CPU](/articles/how-to-fix-system-interrupts-high-cpu-windows-11-step-by-step/).

1. Run LatencyMon as admin for 5–10 minutes of typical use.
2. Drivers tab → sort by DPC count/execution time.
3. Note the top driver's filename — it names the subsystem.
4. All further fixes target that driver's subsystem.

### Fix 2: Fix the Wi-Fi driver (the most common culprit)

If ndis.sys, tcpip.sys, or your Wi-Fi driver's .sys tops the list: Device Manager → Network adapters → your Wi-Fi card → Properties → Advanced tab → disable power-saving features (set "Power Saving Mode" to Maximum Performance, disable "U-APSD" / WMM power save if present). Also update the Wi-Fi driver from the laptop vendor's site (not just Windows Update — vendor versions are tuned for your exact card). Test latency again. On many laptops this single change drops DPC spikes from milliseconds to microseconds.

1. Device Manager → Wi-Fi adapter → Properties → Advanced.
2. Set Power Saving Mode to Maximum Performance; disable WMM power save.
3. Update the Wi-Fi driver from the laptop vendor's support site.
4. Re-run LatencyMon; compare spikes.

### Fix 3: Roll back or update the suspect driver

If the stuttering started after a Windows update, Device Manager → suspect device → Properties → Driver → Roll Back Driver. If no rollback is available (or the driver was always bad), update instead: GPU from NVIDIA/AMD/Intel directly, storage/chipset from the vendor or Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html). Change one driver at a time and re-measure with LatencyMon between changes — otherwise you won't know which change worked. Driver version numbers matter here; write them down.

1. Roll back the suspect driver if the problem started after an update.
2. Otherwise update it from the vendor (not generic Windows Update).
3. Change one driver at a time; re-measure with LatencyMon between.
4. Record version numbers that work — you'll need them if Windows "updates" again.

### Fix 4: Unplug USB devices one at a time

If USB-related drivers (usbport.sys, or a device-specific driver) top LatencyMon: disconnect all USB devices, re-measure, then reconnect one at a time with measurement between each. Docks, USB audio interfaces, capture cards, and RGB peripherals are the usual offenders. A device that spikes latency when connected has a bad driver or failing hardware — update its driver from the manufacturer, try a different port (USB 2.0 vs 3.0 changes the driver path), or replace it. Don't overlook the laptop's own built-in devices: disable the webcam or fingerprint reader in Device Manager as a test.

1. Disconnect all USB devices; re-measure latency.
2. Reconnect one at a time, measuring between each.
3. Identify the spiking device; update its driver or change ports.
4. Test disabling built-in devices (webcam, fingerprint) too.

### Fix 5: Disable interrupt-heavy bloatware drivers

RGB control software, fan controllers, macro tools, and "gaming" utilities install kernel drivers that poll hardware constantly. If LatencyMon implicates an unfamiliar .sys file, search its name — it's often from a utility you installed and forgot. Uninstall the utility (not just exit it — the driver loads at boot regardless), reboot, and re-measure. The related interrupts guide covers the [post-update variant](/articles/how-to-fix-system-interrupts-high-cpu-after-windows-11-update/) of this same class of problem.

1. Identify unfamiliar high-DPC .sys files via web search.
2. Uninstall the parent utility completely (not just exit).
3. Reboot; re-measure with LatencyMon.
4. Keep only utilities whose drivers behave.

### Fix 6: Tune power and interrupt settings

Control Panel → Power Options → Change plan settings → Change advanced power settings: set "PCI Express → Link State Power Management" to Off (a known DPC source on some laptops), and in Processor power management ensure minimum processor state isn't causing aggressive C-state transitions (try 5%→50% minimum as a test). In Device Manager, for the network adapter, experiment with "Interrupt Moderation" disabled. These are tradeoffs — slightly more power for smoother latency — and they're reversible, so test each with LatencyMon running.

1. PCI Express Link State Power Management → Off.
2. Raise minimum processor state as a C-state test.
3. Try Interrupt Moderation disabled on the network adapter.
4. Measure each change with LatencyMon; keep what helps.

### Fix 7: Update the BIOS

If a firmware-level driver (ACPI.sys high in LatencyMon) is implicated, or nothing else helped, check the laptop vendor's support site for a BIOS update — vendors fix interrupt routing and power-state bugs in BIOS releases regularly. Flash on AC power with a charged battery, following vendor instructions exactly. After updating, re-run LatencyMon for a full 10 minutes. BIOS-caused DPC issues are the hardest to diagnose and the simplest to fix once identified — one flash, problem gone. Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) documents the general update process.

1. Check the vendor support site for BIOS updates for your model.
2. Flash on AC power, battery charged, per instructions.
3. Re-run LatencyMon for 10 minutes afterward.
4. Confirm spikes are gone during your stutter-triggering activity.

## Closing

High DPC latency feels mysterious because Task Manager looks innocent — but LatencyMon names the guilty driver in minutes, and from there it's a standard driver fix: tune, roll back, update, or remove. Start with the Wi-Fi driver's power settings (the cause more often than not), change one thing at a time, and measure everything. Smooth audio and a steady cursor are the reward for an hour of methodical work.
