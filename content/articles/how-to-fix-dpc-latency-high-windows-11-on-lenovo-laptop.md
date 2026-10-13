---
title: "Fix High DPC Latency on Your Lenovo Laptop in Windows 11"
slug: how-to-fix-dpc-latency-high-windows-11-on-lenovo-laptop
date: 2026-09-10
categories: ["performance"]
tags: ["dpc latency high", "lenovo laptop", "windows 11", "audio stutter", "latencymon"]
description: "Audio crackling and stutters from high DPC latency on your Lenovo? Identify the bad driver with LatencyMon and fix deferred procedure call spikes."
thumbnail: "/images/thumbs/how-to-fix-dpc-latency-high-windows-11-on-lenovo-laptop.webp"
faqs:
  - q: "What is DPC latency?"
    a: "Deferred Procedure Call latency measures how long drivers take to finish interrupt work. High DPC latency means a driver is hogging the CPU at a priority that blocks everything else — causing audio crackles, mouse stutter, and video glitches even when overall CPU usage looks low."
  - q: "How do I measure DPC latency?"
    a: "Download LatencyMon, a free tool from Resplendence. Close unnecessary apps, press Play, and let it run for 5 to 10 minutes while you reproduce the problem — play audio, move the mouse. Then open the Drivers tab and sort by DPC execution time. The driver at the top is your culprit, and the measured microseconds tell you how severe the problem is."
  - q: "What DPC latency is acceptable?"
    a: "For everyday use, sustained latency under 500 microseconds is fine and you will never notice it. For real-time audio production, aim under 200 microseconds to avoid crackles. Brief spikes to 1000 are tolerable on any system. Constant spikes above 2000 microseconds will cause audible glitches, mouse stutter, and dropped video frames — that is firmly fix-me territory."
  - q: "Can Wi-Fi drivers cause high DPC latency?"
    a: "Absolutely — they are among the most common offenders. Wi-Fi drivers with aggressive power saving constantly cycle the radio, and each cycle can stall the CPU at high priority. Updating the driver from your laptop maker's support site and disabling power-saving on the adapter in Device Manager resolves a large share of DPC latency cases."
---

High DPC latency is the ghost in the machine: your CPU usage looks fine, nothing is obviously wrong, yet audio crackles, the mouse micro-stutters, and video calls glitch. The culprit is a misbehaving driver holding the processor hostage in tiny, high-priority slices that Task Manager barely shows. On Lenovo laptops, the usual offenders are network, audio, and power-management drivers.

DPC — Deferred Procedure Call — is how Windows drivers finish interrupt work. When a driver takes too long, everything behind it waits: audio buffers underrun and you hear a pop, the mouse skips, a frame drops. The fix is detective work with the right tool, and the tool is free.

This guide walks you through measuring latency properly, identifying the guilty driver, and fixing it — in that order.

## Why this happens

- **Wi-Fi driver power saving:** The wireless driver constantly power-cycling is the single most common DPC latency source.

- **Outdated audio drivers:** Realtek/Conexant audio drivers with bad DPC behavior cause the crackling directly.

- **Lenovo power management drivers:** Aggressive CPU state switching (C-states) adds latency spikes.

- **Outdated chipset drivers:** The chipset driver governs interrupt routing for the whole system.

- **USB controller issues:** Problematic USB drivers spike latency, especially with audio interfaces attached.

- **NVIDIA/AMD GPU driver:** Graphics drivers occasionally introduce DPC regressions in specific versions.

- **Background network scanning:** Lenovo utilities or third-party tools polling the network stack. Related interrupt-storm issues are covered in [System Interrupts high CPU on Lenovo](/articles/how-to-fix-system-interrupts-high-cpu-windows-11-on-lenovo-laptop/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure with LatencyMon to find the culprit

Guessing at drivers wastes hours. LatencyMon identifies the exact driver file with the worst DPC times in minutes.

1. Download LatencyMon (free) from Resplendence and install it.
2. Close unnecessary apps, then press the Play button and let it run 5 to 10 minutes.
3. Reproduce the problem during the run — play audio, move the mouse, join a call.
4. Open the Drivers tab and sort by DPC count and execution time.
5. Note the top driver file name (e.g., ndis.sys, storport.sys, or a vendor driver) — that is your target.

### Fix 2: Fix Wi-Fi driver power management

If ndis.sys or your Wi-Fi driver tops the LatencyMon list, power-saving on the wireless adapter is the prime suspect.

1. Open Device Manager and expand Network adapters.
2. Right-click your Wi-Fi adapter, Properties, Power Management tab.
3. Uncheck 'Allow the computer to turn off this device to save power'.
4. On the Advanced tab, set Power Saving Mode or Roaming Aggressiveness to Maximum Performance.
5. Update the Wi-Fi driver from [Lenovo Support](https://support.lenovo.com/us/en/) for your exact model.
6. Re-run LatencyMon for 10 minutes to confirm the improvement.

### Fix 3: Update audio and chipset drivers

Audio drivers cause the symptom directly; chipset drivers govern the interrupt plumbing underneath. Update both.

1. In Device Manager, update the audio driver under Sound, video and game controllers.
2. Get the latest Realtek or Conexant driver from Lenovo Support rather than Windows Update.
3. Install the newest Lenovo chipset driver package for your model.
4. Restart and re-run LatencyMon.
5. If a specific driver version introduced the problem, roll back: Device Manager, driver Properties, Roll Back Driver.

### Fix 4: Tame CPU power-state switching

Aggressive C-state transitions add latency spikes. Limiting them trades a little battery life for smooth real-time performance.

1. Open Power Options, Change plan settings, Change advanced power settings.
2. Expand Processor power management.
3. Set Minimum processor state to 50 percent on Plugged in (keeps clocks from diving).
4. If your BIOS exposes C-state controls, try disabling the deepest C-states — check Lenovo's BIOS simulator for your model first.
5. Test with LatencyMon after each change.
6. For Intel systems, keep chipset drivers current via [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 5: Disable problematic devices one by one

When LatencyMon points at a device class rather than a clear driver, isolation testing finds the hardware trigger.

1. In Device Manager, disable non-essential devices one at a time: Bluetooth, webcam, fingerprint reader.
2. After each disable, run LatencyMon for 5 minutes.
3. When latency drops, you have found the device — update or replace its driver.
4. Check Lenovo Vantage for firmware updates for the identified device.
5. Re-enable everything else and confirm latency stays low.

### Fix 6: Clean-install the GPU driver if implicated

Graphics drivers are occasional DPC offenders, especially right after a major driver update. A clean install removes the regression.

1. If LatencyMon implicates nvlddmkm.sys or amdkmdag.sys, download the previous known-good driver version.
2. Run the installer with the clean-install option checked.
3. Restart and re-measure with LatencyMon.
4. Report the regression to the GPU vendor so it gets fixed upstream.
5. If latency persists across driver versions, the GPU is likely innocent — return to the network and audio suspects.

### Fix 7: Disable dynamic tick and retest

Windows' dynamic tick lets the system timer fire irregularly to save power, but on some Lenovo hardware it interacts badly with drivers and surfaces as DPC latency spikes. Disabling it forces a steady timer tick — a well-known tweak in the pro-audio world used against exactly this problem.

1. Open Command Prompt as administrator.
2. Run `bcdedit /set disabledynamictick yes` and press Enter.
3. Restart the laptop.
4. Run LatencyMon for 10 minutes and compare the worst DPC times with your earlier measurement.
5. If latency improved, keep the setting; if not, revert with `bcdedit /set disabledynamictick no`.
6. Also test with the High performance power plan temporarily to rule out power-saving interactions.

## Closing

High DPC latency is a driver detective story, and LatencyMon is your magnifying glass. On Lenovo laptops the trail usually ends at the Wi-Fi driver's power saving or an outdated audio driver — fix those, verify with a second measurement, and the crackles and stutters disappear. If Task Manager shows System Interrupts rather than a named driver eating CPU, read [System Interrupts high CPU after the Windows 11 update](/articles/how-to-fix-system-interrupts-high-cpu-after-windows-11-update/) next.
