---
title: "System Interrupts High CPU: Troubleshooting Walkthrough"
slug: system-interrupts-high-cpu-troubleshooting
date: 2026-09-29
categories: ["performance"]
tags: ["system interrupts", "high cpu", "troubleshooting", "dpc latency", "hardware"]
description: "A full troubleshooting walkthrough for System Interrupts CPU spikes: measure DPC latency, interrogate drivers, and isolate failing hardware."
thumbnail: "/images/thumbs/system-interrupts-high-cpu-troubleshooting.webp"
faqs:
  - q: "What's the difference between System Interrupts and a normal high-CPU process?"
    a: "A normal high-CPU process is a program you can see, end, or uninstall. System Interrupts is kernel accounting for time spent handling hardware signals — there's no executable to kill. That difference changes the entire troubleshooting approach: instead of managing programs, you're investigating drivers and hardware. The tools are different (LatencyMon, Device Manager, Safe Mode) and the fixes are driver updates, device replacements, or BIOS updates."
  - q: "How do I use LatencyMon to find the problem driver?"
    a: "Run LatencyMon as administrator for 5-10 minutes while the issue is active. Open the Drivers tab and sort by DPC count — the driver with the highest count and longest execution times is keeping the CPU in interrupt handling. Note its file name (like ndis.sys or storport.sys), then trace it to the actual device driver underneath via Device Manager or a driver database. That device is your investigation target."
  - q: "Can Windows Update fix System Interrupts high CPU?"
    a: "Sometimes, when the fix is a driver Microsoft distributes — network and audio driver updates do arrive via Windows Update. But Windows Update also causes these problems by replacing working vendor drivers with generic ones. Check Update history against the symptom timeline: if the spike started right after an update, the update's driver is suspect number one, and the fix is the vendor driver, not another update."
  - q: "When is it hardware failure rather than a driver bug?"
    a: "When every driver is current and correct yet the interrupts persist, when the problem survives Safe Mode and clean driver reinstalls, or when it correlates with a specific device regardless of driver version. Failing drives, dying network cards, and bad USB devices generate interrupt storms no software can fix. The elimination tests in this walkthrough — Safe Mode, device removal, port changes — are how you prove it's the hardware."
---

System Interrupts high CPU is a troubleshooting problem in the truest sense: the symptom is clear, the cause is hidden behind a kernel abstraction, and the fix depends entirely on what you find. This walkthrough is the complete investigation — from first measurement to final verdict — organized so each phase either identifies the culprit or eliminates a category.

Unlike the [best-way fix guide](/articles/best-way-to-fix-system-interrupts-high-cpu/), which prioritizes the fastest resolution path, this walkthrough is exhaustive. Use it when the quick path didn't find the answer, or when you want to understand the full picture before changing anything.

## Why this happens

- **DPC latency in a single driver:** One driver's deferred procedure calls running too long, dominating interrupt time.
- **Interrupt storms from failing hardware:** A device retrying failed operations generates interrupts at orders of magnitude above normal.
- **Misconfigured interrupt moderation:** Network adapters firing per-packet interrupts instead of batching.
- **Shared IRQ conflicts:** Legacy interrupt line sharing forcing the CPU to poll multiple devices per interrupt.
- **Power management bugs:** Drivers mishandling sleep/wake transitions, leaving devices in interrupt-generating states.
- **BIOS interrupt routing issues:** Firmware assigning interrupt resources badly, fixed in later BIOS versions.
- **USB controller driver defects:** The USB stack generating excessive interrupts under specific device combinations.
- **Storage driver completion bugs:** AHCI/NVMe drivers mishandling command completions.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Characterize the symptom precisely

Before touching anything, document: the exact CPU percentage range, whether it's constant or bursty, whether it correlates with network activity, disk activity, audio playback, or USB devices, and when it started (which update? which new device?). Boot into Safe Mode and compare — calm in Safe Mode means a third-party driver; still high means a core Windows driver, BIOS issue, or hardware. This characterization is your case file; every later step references it.

1. Record System Interrupts CPU % over 10 minutes (range and pattern).
2. Test correlations: network load, disk load, audio, USB devices.
3. Note the start date; check it against updates and new hardware.
4. Boot into Safe Mode and compare the reading.

### Fix 2: Run the LatencyMon investigation

Download LatencyMon, run as administrator, and collect 10 minutes of data during active symptoms. Examine three tabs: **Main** (is the system suitable for real-time audio? — a general latency verdict), **Drivers** (sorted by DPC count — your prime suspect list), and **Processes** (to rule out a process driving the interrupts). The top DPC driver is your lead. Common signatures: ndis.sys → network driver underneath; storport.sys → storage driver; HDAudBus.sys → audio; usbport.sys → USB stack. Write down the top three — sometimes the culprit is a combination.

1. Run LatencyMon as administrator for 10 minutes during symptoms.
2. Check the Drivers tab sorted by DPC count; note the top three.
3. Check the Main tab for the overall latency verdict.
4. Map each suspect driver file to its device.

### Fix 3: Interrogate the suspect driver

For the top suspect: check its version and date in Device Manager (driver file properties), compare against the vendor's latest, and check the timeline — did this driver update recently? Search the driver version plus "DPC latency" to find known-bad versions; some driver releases are infamous for this. If a known-bad version is installed, the fix is a specific version change (newer or older), not just "update." Precision beats currency here — the newest driver isn't always the best driver for your hardware.

1. Identify the suspect driver's version and date.
2. Compare against the vendor's current release.
3. Search the version number with "DPC latency" for known issues.
4. Plan a targeted version change (not blind updating).

### Fix 4: Test driver changes methodically

Change one driver at a time and measure after each change: update to vendor-latest, or roll back to the previous version, or try the Microsoft inbox driver (Update driver → Browse → Let me pick → choose the generic). After each change, reboot and run the same 10-minute observation as Fix 1. Only one variable per test — changing three drivers at once teaches you nothing about which one mattered. Keep a log: version, date, result. This discipline is what separates troubleshooting from flailing.

1. Change exactly one driver (update, roll back, or try inbox driver).
2. Reboot; repeat the 10-minute observation.
3. Log the version and the result.
4. Revert changes that didn't help before trying the next.

### Fix 5: Investigate the hardware layer

If drivers are exonerated, go physical. Reseat RAM and any removable cards (desktops). Try different USB ports and cables for suspect peripherals. Test the drive with manufacturer diagnostics. Check temperatures — overheating components generate error interrupts. For laptops, test on battery vs. AC (power delivery issues cause interrupt anomalies), and with the dock/station disconnected. If a specific hardware configuration change resolves it, you've found a hardware fault that no driver update will fix.

1. Reseat RAM and removable cards; check all cable connections.
2. Test suspect USB devices on different ports and cables.
3. Run manufacturer drive diagnostics.
4. Test on battery vs. AC; with and without dock.

### Fix 6: Update BIOS and reset firmware settings

Check for a BIOS update newer than yours on the manufacturer's support site — interrupt routing fixes are common in BIOS changelogs (look for "IRQ," "interrupt," "DPC," or "stability" mentions). Apply it carefully on AC power. Then load BIOS defaults (note your custom settings first) to clear any misconfigured interrupt or power setting. Firmware is the layer most people forget, and it's the layer that controls how interrupts reach the CPU in the first place.

1. Check the BIOS changelog for interrupt-related fixes.
2. Apply the BIOS update on AC power, uninterrupted.
3. Load BIOS defaults (record custom settings first).
4. Re-observe System Interrupts after the firmware update.

### Fix 7: Reach the verdict and act on it

By now you have evidence pointing at a driver version, a device, or the firmware. Act on the verdict: pin the working driver version (use the show/hide updates troubleshooter to block Windows from "fixing" it), replace the failing device, or disable a non-essential device in Device Manager. If the verdict is a core Windows driver with no alternative and current BIOS, escalate: it's either a Windows bug needing a patch (check the [Update Catalog](https://www.catalog.update.microsoft.com/) for hotfixes) or hardware needing professional diagnosis. Document everything — the next person (or future you) will thank you. For related interrupt-adjacent CPU issues, the [Defender high CPU guide](/articles/how-to-fix-windows-defender-high-cpu-usage/) covers the process-side counterpart.

1. State the verdict: which driver/device/firmware is responsible.
2. Pin working driver versions against unwanted updates.
3. Replace or disable the faulty hardware.
4. Document the full investigation for future reference.

## Closing

Troubleshooting System Interrupts is detective work with good tools: characterize, measure with LatencyMon, interrogate drivers one at a time, test the hardware layer, check the firmware, and render a verdict. The process feels slow, but it's faster than the alternative — months of random tweaks that never address the actual driver or device. The interrupts stop when the shouting hardware goes quiet, and now you know how to find who's shouting.
