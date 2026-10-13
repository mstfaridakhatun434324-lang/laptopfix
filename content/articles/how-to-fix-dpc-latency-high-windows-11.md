---
title: "How to Fix High DPC Latency on Windows 11 (Audio Crackles & Stutters)"
slug: how-to-fix-dpc-latency-high-windows-11
date: 2026-09-27
categories: ["performance"]
tags: ["dpc latency", "high dpc latency", "audio crackling", "stuttering", "windows 11 drivers"]
description: "Audio crackling and micro-stutters on Windows 11? High DPC latency is usually the cause — here is how to find the bad driver and fix it."
thumbnail: "/images/thumbs/how-to-fix-dpc-latency-high-windows-11.webp"
faqs:
  - q: "What is DPC latency in simple terms?"
    a: "Drivers handle hardware interrupts through Deferred Procedure Calls. If one driver takes too long in its DPC routine, everything else — including audio playback — waits, producing crackles, pops, and stutters. LatencyMon measures these delays in microseconds; spikes above 1000–2000 microseconds during audio work indicate a problem driver."
  - q: "Is high DPC latency a hardware problem?"
    a: "Rarely at first. The overwhelming majority of cases are buggy drivers — network, Wi-Fi, storage, or GPU drivers hogging interrupt time. True hardware causes (failing devices, bad PCIe links) exist but are the minority. Always exhaust the driver fixes before suspecting hardware."
  - q: "Why does DPC latency affect audio more than video?"
    a: "Audio is uniquely sensitive because it plays from a tiny buffer that must be refilled on a strict deadline — typically every few milliseconds. A single 2-millisecond driver stall empties the buffer and you hear a pop. Video has much larger buffers and can absorb the same stall invisibly, which is why audio crackles while video looks fine."
  - q: "Can Windows updates cause DPC latency spikes?"
    a: "Yes — a driver delivered through Windows Update can introduce a latency regression overnight. If crackling started right after an update, check which drivers changed and roll back the network or audio driver first. Conversely, updates also fix latency bugs, so staying current on known-good driver versions matters."
---

You are listening to music or on a call when the audio starts crackling — tiny pops and dropouts that no volume knob fixes. Or games micro-stutter while the frame rate counter looks fine. On Windows 11 laptops, this signature almost always means **high DPC latency**: a misbehaving driver hogging the CPU interrupt path and starving time-sensitive work like audio.

Fixing it is detective work with a specific tool: LatencyMon, which names the exact driver with the worst execution times. Once you know the culprit — usually a network, Wi-Fi, or storage driver — the fix is updating, rolling back, or reconfiguring that one driver. No guesswork, no reinstalling Windows on a hunch.

This guide walks the full path: measure with LatencyMon, identify the offender, fix it, and verify the spikes are gone. If your stutters are game-specific rather than audio, the [game stuttering guide](/articles/how-to-fix-game-stuttering-after-windows-update-on-windows-11/) covers the gaming angle.

## Why this happens

- **Buggy network/Wi-Fi driver:** The single most common offender — NDIS drivers with long DPC routines stall the system every time packets arrive.
- **Outdated storage driver:** AHCI/NVMe drivers with poor interrupt handling spike during disk I/O, crackling audio during file copies.
- **GPU driver power management:** Aggressive GPU clock switching generates DPC spikes; the driver takes too long waking the hardware.
- **USB audio interface driver issues:** External DACs and headsets with bad drivers add their own latency on top of system DPC.
- **BIOS power management (C-states):** Deep CPU sleep states add wake latency that shows up as DPC spikes under light load.
- **Background driver polling:** RGB utilities, hardware monitors, and fan tools polling hardware constantly inflate latency.
- **Windows Update driver regressions:** A newly delivered driver version introducing worse interrupt behavior than its predecessor.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure with LatencyMon and name the culprit

Download LatencyMon (Resplendence, free) and let it run for ten minutes during normal use — play audio so dropouts occur while measuring. The Drivers tab sorts by highest DPC execution time; the top entries name your suspects. Also check the Main tab conclusion line. Write down the exact driver filenames (e.g. ndis.sys, storport.sys, nvlddmkm.sys) — everything below targets them specifically. Without this step you are guessing.

1. Download and install LatencyMon from the developer site.
2. Click Start, play audio, and use the laptop normally for ten minutes.
3. Open the Drivers tab and sort by "Highest execution (ms)".
4. Record the top two or three driver filenames — those are your targets.

### Fix 2: Update or roll back the offending driver

Match the culprit filename to its device: ndis.sys or a Wi-Fi driver file means the network adapter; storport.sys means storage; nvlddmkm.sys means NVIDIA graphics. Get the driver from the right source — laptop maker first for tuned builds, then the chip vendor. If the problem started after a recent update, roll back instead: Device Manager → device → Properties → Driver → Roll Back Driver. For Intel-based network and chipset drivers, the [Intel driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the correct builds.

1. Identify which device owns the worst driver file.
2. Download the latest driver from the laptop maker or chip vendor.
3. If recently updated, roll back the driver first as a test.
4. Re-run LatencyMon for ten minutes and compare the numbers.

### Fix 3: Tame network driver interrupt behavior

When the network driver is the culprit, two settings often calm it: in Device Manager → network adapter → Advanced, disable interrupt-heavy offloads you do not need and try disabling "Energy Efficient Ethernet"/power-saving modes that cause wake spikes. Also test with Wi-Fi off and Ethernet on (or vice versa) to split wireless-driver issues from wired ones. Gamers and audio workers sometimes pin the fix by using the laptop maker driver version instead of the newest generic.

1. Open the adapter Advanced tab and note the current offload settings.
2. Disable power-saving and energy-efficient modes on the adapter.
3. Test on the opposite connection type (wired vs wireless) to isolate.
4. Re-measure with LatencyMon after each change.

### Fix 4: Stabilize GPU power management

If the graphics driver tops the DPC list, its power-state switching is the likely mechanism. In the NVIDIA/AMD control panel, set Power management mode to "Prefer maximum performance" (NVIDIA) or disable aggressive power saving (AMD) as a test — if spikes vanish, you have confirmed it and can look for a driver version that behaves. Also update the GPU driver cleanly; DPC regressions in graphics drivers are common and commonly fixed. The [game stuttering walkthrough](/articles/how-to-fix-game-stuttering-after-windows-update-step-by-step/) covers GPU-side tuning in more depth.

1. Set the GPU control panel power mode to maximum performance as a test.
2. Re-run LatencyMon during audio playback.
3. Spikes gone: keep the setting or find a better-behaved driver version.
4. Do a clean GPU driver install if the driver itself is the offender.

### Fix 5: Adjust BIOS power settings and disable CPU deep sleep

Under light load, CPUs park in deep C-states, and waking from them adds latency that LatencyMon attributes to the system. As a diagnostic, disable C-states (or set to C1 only) in BIOS — if spikes collapse, power management was the amplifier. Also update the BIOS itself; vendors regularly fix interrupt and power-management behavior in BIOS updates. Keep the laptop plugged in during BIOS changes and follow the maker instructions exactly.

1. Enter BIOS and find CPU power/C-state settings.
2. Limit to C1 or disable C-states as a diagnostic test.
3. Check the maker site for a newer BIOS with latency fixes.
4. Re-measure; restore C-states if they were not the cause (battery life matters).

### Fix 6: Remove polling utilities and background interferers

Hardware monitors, RGB controllers, and fan utilities poll devices on tight loops, and their drivers show up as constant low-grade DPC load that spikes under activity. Uninstall or disable them one at a time, re-measuring after each. Also test with USB audio devices unplugged and Bluetooth off to rule out external-device drivers. The goal is the quietest possible driver stack during measurement.

1. Uninstall RGB, fan-control, and hardware-monitoring utilities temporarily.
2. Disconnect USB audio gear and disable Bluetooth for the test.
3. Re-run LatencyMon and compare against the earlier baseline.
4. Reintroduce tools one at a time to find any offender.

### Fix 7: Verify the fix under real workload

A fix that looks good in an idle ten-minute run can fail under load. Do a final verification: play audio, copy a large file, and run a video call simultaneously while LatencyMon records for fifteen minutes. Spikes should stay under roughly 500 microseconds with no audible glitches. Save a screenshot of the clean run — if the problem ever returns after an update, you will know exactly which driver to blame first.

1. Run audio + file copy + video call together for fifteen minutes.
2. Confirm LatencyMon shows no spikes above ~500µs and no audible pops.
3. Screenshot the clean Drivers tab for future reference.
4. If spikes return later, check Windows Update driver changes first.

## Closing

High DPC latency is one of the most diagnosable problems in Windows: LatencyMon names the driver, and the fix targets that driver — update, roll back, reconfigure its power behavior, or calm the BIOS settings around it. Measure first, change one thing at a time, and verify under real load; the crackles and stutters leave when the offending driver does.
