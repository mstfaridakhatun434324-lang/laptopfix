---
title: "How to Fix Video TDR Failure in Windows 11 24H2"
slug: how-to-fix-video-tdr-failure-in-windows-11-24h2
date: 2026-10-11
categories: ["windows-errors"]
tags: ["video tdr failure", "windows 11 24h2", "gpu fix"]
description: "VIDEO_TDR_FAILURE blue screen after the Windows 11 24H2 update? Fix the GPU timeout behind it with this ordered driver and hardware guide."
thumbnail: "/images/thumbs/how-to-fix-video-tdr-failure-in-windows-11-24h2.webp"
faqs:
  - q: "What does VIDEO_TDR_FAILURE mean?"
    a: "TDR stands for Timeout Detection and Recovery. Windows noticed the graphics driver stopped responding, tried to reset it, and the reset failed — so the system crashed. The dump usually names the GPU driver file, like nvlddmkm.sys for NVIDIA or atikmpag.sys for AMD."
  - q: "Why did 24H2 start causing TDR failures?"
    a: "Major Windows builds change the graphics driver model and power management behavior. Drivers that worked on 23H2 can time out under 24H2's different scheduling, especially older GPU drivers. A clean install of a 24H2-aware driver version is the primary fix."
  - q: "Can overheating cause VIDEO_TDR_FAILURE?"
    a: "Yes. A GPU that overheats throttles or hangs instead of completing its work within the timeout window. If TDR crashes happen during gaming or video work but never at idle, check GPU temperatures — sustained readings above 90°C on a laptop GPU need attention."
  - q: "Should I increase the TDR delay in the registry?"
    a: "Only as a diagnostic step, not a fix. Raising TdrDelay gives a struggling GPU more time before Windows declares failure, which can confirm a marginal hardware or driver issue. But it masks the real problem — fix the driver, cooling, or power delivery instead of relying on a longer timeout."
---
VIDEO_TDR_FAILURE is Windows' graphics watchdog giving up. When your GPU driver stops responding, Windows first tries the polite approach — resetting the driver while keeping everything running (that's the TDR part). When the reset itself fails, you get the blue screen. On Windows 11 24H2, this error spiked because the update changed graphics scheduling enough to expose drivers that were already marginal.

The fix path is GPU-focused: clean driver reinstall first, then power and cooling, then hardware. Nearly all TDR failures resolve in the first three steps.

## Why this happens

- **Outdated GPU driver incompatible with 24H2.** The top cause — old drivers time out under the new build's scheduling.
- **Corrupted GPU driver installation.** Partial updates or conflicting remnants cause intermittent hangs.
- **GPU overheating.** A hot GPU stalls instead of finishing work inside the timeout window.
- **Unstable GPU overclock or undervolt.** Marginal clocks fail under 24H2's different load patterns.
- **Insufficient power delivery.** Aging batteries or weak adapters on laptops cause GPU power dips that look like hangs.
- **Failing GPU hardware.** Rare, but a dying GPU produces TDR failures no driver can fix.

## How to fix it

Work through these in order — driver fixes first, they're the cause nine times out of ten.

### Fix 1: Clean-reinstall the GPU driver with DDU

A standard driver update often isn't enough — strip the old driver completely.

1. Download the latest driver for your GPU: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html). Choose a 24H2-certified version, not a beta.
2. Download Display Driver Uninstaller (DDU) and boot into **Safe Mode**.
3. Run DDU, select your GPU brand, and choose **Clean and restart**.
4. After reboot, install the fresh driver you downloaded. Don't let Windows Update install a driver first — disconnect from the network during the DDU process if Windows keeps grabbing one.

### Fix 2: Roll back the 24H2 update if crashes started with it

If TDR failures began the day 24H2 installed, the build itself is implicated.

1. Go to **Settings > System > Recovery** and check whether **Go back** is available (within 10 days of the upgrade).
2. Alternatively, **Settings > Windows Update > Update history > Uninstall updates** for smaller culprits.
3. If you roll back, block the 24H2 reinstall temporarily via **Pause updates** while you wait for a fixed GPU driver.
4. Reattempt the upgrade after installing a known-good driver — the order matters: good driver first, then the build.

### Fix 3: Reset GPU clocks and check temperatures

Overclocks and heat are the next most common triggers.

1. Open your GPU tuning tool (MSI Afterburner, ASUS GPU Tweak, or the vendor control panel) and reset everything to stock clocks and voltages.
2. Monitor GPU temperature with HWMonitor during the workload that crashes — sustained temps above 90°C on a laptop GPU indicate a cooling problem.
3. Clean vents with compressed air and ensure the laptop sits on a hard surface.
4. If crashes only happen under load and temps are high, cooling is your fix — the same thermal discipline that prevents [CLOCK_WATCHDOG_TIMEOUT](/articles/how-to-fix-clock-watchdog-timeout-on-windows-11/) applies here.

### Fix 4: Fix laptop power delivery

GPUs hang when starved of power, and laptops have unique power constraints.

1. Always troubleshoot on the **original charger**, plugged into the wall — not a USB-C dock or third-party adapter unless it's rated for your laptop's wattage.
2. In **Settings > System > Power & battery**, set the power mode to **Best performance** while testing.
3. Check the battery's health: run `powercfg /batteryreport` in Command Prompt and look at design vs. full charge capacity — a heavily degraded battery can't smooth power dips.
4. Disable aggressive GPU power saving in the vendor control panel (NVIDIA Control Panel > Manage 3D settings > Power management mode > Prefer maximum performance) as a test.

### Fix 5: Adjust the TDR delay as a diagnostic

A longer timeout can confirm whether the GPU is marginal or the driver is at fault.

1. Open **Registry Editor** (`regedit`) and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a **DWORD (32-bit)** value named `TdrDelay` and set it to `10` (decimal) — up from the default 2 seconds.
3. Restart and test. If crashes stop, the GPU was timing out marginally — still fix the underlying driver or cooling issue.
4. If crashes continue even with a 10-second delay, the GPU is hanging hard, which points more toward hardware. Remember to treat this as diagnostic, not a permanent fix.

### Fix 6: Test with the integrated GPU

Isolate whether the discrete GPU is the problem.

1. In **Device Manager**, under **Display adapters**, disable the discrete NVIDIA/AMD GPU (right-click > Disable device).
2. Run on the integrated Intel/AMD graphics for a day of normal use.
3. If crashes vanish, the discrete GPU or its driver is confirmed as the source — focus all remaining effort there.
4. Re-enable when done testing. Persistent failures on integrated graphics too suggest a system-level issue rather than the discrete GPU.

### Fix 7: Check for hardware failure

When software is exhausted, verify the GPU itself.

1. Run your laptop maker's built-in diagnostics with a focus on video/GPU tests.
2. Run a GPU stress test (FurMark or similar) briefly while watching temperatures — artifacts or immediate crashes indicate hardware trouble.
3. On laptops, the GPU is soldered — a confirmed failure means a motherboard replacement, which is a manufacturer service matter.
4. Back up data before any service. If the laptop is out of warranty, get a repair quote and compare against replacement cost honestly.

## Closing

VIDEO_TDR_FAILURE in Windows 11 24H2 is a driver-compatibility problem far more often than a hardware problem. Clean-reinstall a 24H2-ready GPU driver with DDU, reset clocks, fix cooling and power delivery — that sequence ends the crashes for the overwhelming majority of laptops. The TDR mechanism itself is Windows protecting you from a hung GPU; once the driver stops hanging, the watchdog never needs to fire. If your dumps name a specific driver file, the [driver IRQL fix guide](/articles/how-to-fix-driver-irql-not-less-or-equal-reddit/) covers the same clean-replacement discipline for other driver crashes.
