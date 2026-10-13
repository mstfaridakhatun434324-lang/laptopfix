---
title: "Display Driver Stopped Responding? Troubleshooting Guide"
slug: display-driver-stopped-responding-troubleshooting
date: 2026-09-17
categories: ["drivers"]
tags: ["display driver", "driver crash", "tdr", "screen freeze", "gpu driver"]
description: "Getting 'display driver stopped responding and has recovered'? Troubleshoot TDR crashes with driver reinstalls, TDR tweaks, temperature checks, and hardware tests."
thumbnail: "/images/thumbs/display-driver-stopped-responding-troubleshooting.webp"
faqs:
  - q: "What does 'display driver stopped responding and has recovered' mean?"
    a: "It means Windows' Timeout Detection and Recovery (TDR) caught the GPU hanging and restarted the graphics driver instead of blue-screening. You see a brief freeze or black flash, then a notification. Occasional TDRs are annoying; frequent ones signal a driver, heat, or hardware problem."
  - q: "Is a TDR crash a sign my GPU is dying?"
    a: "Not necessarily. Most TDRs are caused by buggy drivers, overheating, or unstable overclocks — all fixable. Hardware failure is the diagnosis only after clean drivers, stock clocks, and normal temperatures still produce crashes under light load. Work through this guide's software fixes before fearing the worst."
  - q: "Can overclocking cause display driver crashes?"
    a: "Yes — it is one of the top causes. Even factory overclocks on some cards can be marginally unstable with certain driver versions. Reset all GPU and CPU overclocks to stock as a diagnostic step; if crashes stop, the overclock was the trigger."
  - q: "How often is occasional driver recovery normal?"
    a: "Rarely — perhaps once after a major driver update while shaders rebuild. If you see the message weekly or more, something is wrong. Daily or per-gaming-session TDRs always warrant the full troubleshooting sequence in this guide. Track the frequency in a note — patterns help diagnose the trigger."
---

The screen freezes for two seconds, goes black, and comes back with a bubble: 'Display driver stopped responding and has recovered.' Your game crashed, your video call glitched, or your work just stuttered. Once is an annoyance; every day is a problem demanding a fix.

That message is Windows' Timeout Detection and Recovery — TDR — doing its job. When the GPU stops answering within about two seconds, Windows kills and restarts the graphics driver rather than crashing the whole system. The restart is the recovery you see; the hang is the disease you need to cure.

TDR hangs have a clear suspect list: the graphics driver itself, overheating, unstable clocks, power delivery, and finally failing hardware. This guide works that list in order, from the five-minute driver fix to the definitive hardware verdict.

## Why this happens


- **Buggy graphics driver version:** Certain driver releases are notorious for TDRs on specific GPU and laptop combinations.
- **GPU overheating:** Heat-induced instability is the top hardware cause — dust-clogged fans push GPUs past safe temperatures under load.
- **Unstable overclock:** GPU, VRAM, or CPU overclocks (including factory ones) can cross the stability line with a new driver.
- **Insufficient power delivery:** Aging chargers or batteries that cannot sustain peak GPU draw cause voltage droop and hangs.
- **TDR timeout too aggressive:** The default two-second timeout can false-trigger on heavy but legitimate workloads.
- **Corrupt shader caches:** Damaged cached shaders make the driver hang on specific games or applications repeatedly.
- **Background overlays conflicting:** Capture and overlay software hooks the graphics pipeline and can trigger hangs.
- **Failing GPU hardware:** Degrading VRAM or GPU silicon produces TDRs that survive every software fix — the last-resort diagnosis.

## How to fix it


Work through these in order — diagnose first, then act.

### Fix 1: Clean-reinstall the graphics driver


The first and most effective step. A truly clean install — not an update over the top — eliminates driver corruption and version-specific TDR bugs in one move.

1. Download the graphics driver for your exact laptop model from your maker's support site (or [NVIDIA](https://www.nvidia.com/Download/index.aspx)/[AMD](https://www.amd.com/en/support/download/drivers.html) for newer releases).
2. Boot into Safe Mode and run Display Driver Uninstaller (DDU) to wipe the old driver completely.
3. Restart normally and install the fresh driver.
4. If TDRs started with a specific driver version, install the previous known-good version instead of the latest.
5. Test with the application that crashed most reliably.
6. For version-specific guidance, see our [Windows 11 display driver recovery](/articles/how-to-fix-display-driver-stopped-responding-on-windows-11/).

### Fix 2: Check temperatures and clean cooling


Heat is the leading hardware cause of TDRs. If the GPU is thermal-throttling, no driver version will save it — the cooling system needs attention first.

1. Install HWiNFO64 or HWMonitor and log GPU temperature during the workload that crashes.
2. Sustained temperatures above 90°C on a laptop GPU indicate a cooling problem.
3. Blow compressed air through the vents (short bursts, fans held still) to clear dust.
4. Elevate the laptop or use a cooling pad to improve airflow during testing.
5. If temperatures stay high after cleaning, the thermal paste may need replacement — a shop job for most users.
6. Retest: TDRs that vanish with temperatures under control were heat-caused.

### Fix 3: Reset all overclocks to stock


Overclocks — yours or the factory's — are a prime TDR trigger. Returning everything to stock clocks is a fast, free diagnostic that either fixes the crashes or eliminates a major suspect.

1. Open MSI Afterburner, Intel XTU, or your maker's tuning utility and reset all GPU/CPU clocks and voltages to default.
2. Disable any 'performance' or 'turbo' modes in BIOS that raise clocks beyond stock.
3. If the laptop has a factory overclocked GPU, try the maker's 'quiet' or 'balanced' power profile which often runs stock clocks.
4. Test the crashing workload for at least an hour.
5. If crashes stop, reintroduce overclocks gradually — or leave stock for stability.

### Fix 4: Increase the TDR timeout


For heavy legitimate workloads (long shader compiles, huge renders), the default two-second TDR timeout can fire prematurely. Extending it gives the GPU room to finish without Windows declaring a hang.

1. Press Windows + R, type regedit, and press Enter.
2. Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers.
3. Create a DWORD (32-bit) named TdrDelay and set it to 10 (decimal) — ten seconds instead of two.
4. Optionally create TdrDdiDelay set to 10 as well.
5. Restart and test. This is a workaround for legitimate heavy loads, not a fix for genuinely hanging drivers.
6. Revert these values if crashes continue — masking a real hang only delays the diagnosis.

### Fix 5: Eliminate power and overlay suspects


Two often-overlooked triggers: marginal power delivery under peak GPU load, and overlay software hooking the graphics pipeline. Both are quick to test.

1. Run the crashing workload on AC power with the original high-wattage charger — not a smaller USB-C charger.
2. Check battery health; a severely degraded battery can destabilize power delivery on some models.
3. Disable all overlays: GeForce Experience, Discord, Xbox Game Bar, OBS — test with everything off.
4. Close background GPU users (browsers with hardware acceleration, video editors) during testing.
5. If crashes only happen on battery or with a weak charger, power delivery is the cause.

### Fix 6: Run the hardware verdict tests


When clean drivers, stock clocks, cool temperatures, and stable power still produce TDRs, the GPU hardware itself is suspect. These tests deliver the verdict.

1. Run a GPU stress test (FurMark or 3DMark) and watch for TDRs under pure load — crashes here with good temps point to silicon/VRAM.
2. Test with an external monitor: identical crashes rule out the internal display path.
3. Boot a Linux live USB and run a GPU workload — TDR-equivalent hangs there confirm hardware.
4. Check Windows Event Viewer, System log, for nvlddmkm/amdkmdap errors correlating with crashes.
5. Persistent failures across OSes mean failing GPU hardware — contact your maker's support for repair options.
6. For flickering that accompanies the crashes, our [second monitor flickering guide](/articles/how-to-fix-second-monitor-flickering-step-by-step/) covers the display-side fixes.

## Closing


Display driver TDRs are Windows catching the GPU red-handed — the recovery message is the symptom, the hang is the disease. Clean drivers, cool temperatures, stock clocks, and solid power cure the overwhelming majority of cases. Only when all four check out and crashes persist should you pronounce the hardware guilty.
