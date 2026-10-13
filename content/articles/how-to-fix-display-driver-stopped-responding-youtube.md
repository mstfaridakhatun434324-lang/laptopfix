---
title: "\"Display Driver Stopped Responding\" Error: Fix It for Good"
slug: "how-to-fix-display-driver-stopped-responding-youtube"
date: "2026-09-29"
categories: ["drivers"]
tags: ["display driver", "tdr error", "gpu crash", "nvidia", "amd"]
description: "Seeing 'display driver stopped responding and has recovered'? Learn what the TDR error means and apply permanent fixes for NVIDIA, AMD, and Intel graphics."
thumbnail: "/images/thumbs/how-to-fix-display-driver-stopped-responding-youtube.webp"
faqs:
  - q: "What does 'display driver stopped responding' actually mean?"
    a: "It means Windows' Timeout Detection and Recovery system decided the GPU took too long to respond — over two seconds by default — so it reset the graphics driver instead of letting the system hang. The screen goes black briefly, then returns. It is a protective mechanism, and its appearance tells you the GPU stalled, whether from driver bugs, overheating, unstable clocks, or hardware faults."
  - q: "Is the TDR error caused by my graphics card dying?"
    a: "Rarely at first. The overwhelming majority of TDR errors come from driver corruption, overheating, unstable overclocks, or software conflicts. Hardware failure is the diagnosis only after crashes persist across multiple clean driver installs, stock clocks, verified cooling, and a fresh Windows install. Do the software fixes first — they resolve most cases."
  - q: "Can increasing the TDR delay fix the crashes?"
    a: "It can stop the symptom when the GPU legitimately needs more than two seconds for heavy workloads, such as complex renders or large machine-learning tasks. Setting TdrDelay to 8 or 10 seconds gives the GPU room to finish. But if the GPU is truly hung, a longer delay just postpones the reset — use it as a workaround for heavy workloads, not as a fix for random crashes."
  - q: "Why does the error only happen in one specific game?"
    a: "A single-game pattern points to that game's shader compilation, a corrupted shader cache, or an engine quirk interacting with your driver version. Clear the game's shader cache, verify game files, and try a different driver version. If every other game is stable, the driver is fine in general and the problem is the specific game-driver interaction."
---

The screen freezes, goes black for a few seconds, then comes back with the bubble: "Display driver stopped responding and has recovered." It might happen in games, during video playback, or seemingly at random on the desktop. This is Windows' TDR — Timeout Detection and Recovery — doing its job: rather than letting a stalled GPU hang the whole system, it resets the driver.

TDR is a symptom, not a disease, and it is admirably honest: something made your GPU stop answering for more than two seconds. The causes range from a corrupted driver install to a GPU gasping for cool air to an overclock that was never truly stable. Because the reset "recovers," people tolerate it for months — but each crash risks data loss in creative work and ruins competitive gaming. The fixes below go after the stall causes permanently.

## Why this happens

- **Corrupted graphics driver installation:** Leftover files and registry damage make the driver stall under load.
- **GPU overheating:** Thermal stress causes the GPU to stop responding before throttling can save it.
- **Unstable overclock or undervolt:** Clocks that pass quick tests fail during sustained real-world loads.
- **Failing GPU hardware:** Degrading VRAM or power delivery stalls the chip intermittently.
- **Corrupted shader caches:** Damaged cached shaders hang the driver when specific content loads.
- **Conflicting overlays and capture software:** Injected hooks stall the rendering pipeline.
- **Insufficient or unstable power:** On laptops, aggressive power limits can starve the GPU mid-task.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Clean-install the graphics driver with DDU
Download Display Driver Uninstaller and the latest driver for your GPU — [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html). Disconnect from the internet, boot to Safe Mode, run DDU's "Clean and restart," then install the new driver with its clean-install option. Corrupted installs are the top TDR cause, and only a true wipe removes the damage that in-place updates preserve. Test with your most crash-prone workload for at least an hour.

### Fix 2: Reset all overclocks to stock
Open MSI Afterburner, your manufacturer's control app, or the GPU vendor's tuning panel, and reset core clock, memory clock, voltage, and fan curves to defaults. Disable any "auto overclock" or "performance boost" features. Many TDR cases trace to overclocks that were stable in benchmarks but fail in specific games after driver updates changed power behavior. Run at stock for several days; if crashes vanish, any future tuning must be validated much more conservatively.

### Fix 3: Check temperatures under load
Install HWiNFO64 and log GPU temperature during gaming or a stress test. Sustained readings above 85–87°C on a laptop GPU invite TDR crashes. Clean dust from vents with compressed air, elevate the rear of the laptop for airflow, and verify fans actually spin up under load. If temperatures are high and the laptop is a few years old, dried thermal paste is likely — a professional repaste typically drops temps dramatically. Cooling fixes a large share of "random" TDR errors. See our [laptop fan troubleshooting](/articles/how-to-fix-laptop-fan-not-working-in-windows-11-24h2/) for cooling diagnostics.

### Fix 4: Clear shader caches and verify game files
Delete the GPU shader caches (NVIDIA's DXCache/GLCache, or use Disk Cleanup's DirectX Shader Cache option), and in your game launcher verify the integrity of game files. Corrupted shaders stall the driver at the exact moment specific content loads — which is why some TDR crashes happen at the same game location every time. Fresh caches rebuild cleanly on next launch. If crashes are game-specific, also try the game's forums for known driver-version conflicts.

### Fix 5: Disable overlays and background GPU hooks
Turn off the GeForce Experience/AMD Adrenalin overlay, Discord overlay, Xbox Game Bar, and any screen recording or FPS-monitoring tools. Test after each. These apps inject code into the graphics pipeline, and a hook that stalls for two seconds triggers exactly the TDR you're seeing. Re-enable them one at a time to identify the offender. For NVIDIA-specific crash patterns, our [NVIDIA driver crash guide](/articles/how-to-fix-nvidia-driver-crashing-step-by-step/) goes deeper.

### Fix 6: Increase the TDR timeout via registry
If crashes happen during legitimately heavy workloads (rendering, large models), give the GPU more time: open Registry Editor, go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`, create DWORD (32-bit) `TdrDelay` set to `10`, and reboot. This extends the patience window from 2 to 10 seconds. Treat it as a workaround for heavy tasks, not a cure for random desktop crashes — if the GPU truly hangs, you'll still get the reset, just later.

### Fix 7: Test power delivery and consider hardware fault
On laptops, set the power plan to Best Performance and test with the AC adapter connected — battery-only power limits can starve the GPU. Try an external monitor to rule out panel-specific issues. If TDR crashes persist across multiple clean driver versions, at stock clocks, with good temperatures, on a fresh Windows install, the GPU hardware itself is likely failing. Document the pattern with logs for a warranty claim; intermittent VRAM faults are the classic end-stage cause. Microsoft's graphics diagnostics at Windows support can help capture the failure.

## Closing
"Display driver stopped responding" is Windows telling you the GPU stalled, and stalls have findable causes: corrupted drivers, heat, unstable clocks, bad caches, or hostile overlays. A DDU clean install plus temperature verification resolves most cases outright — and the cases that survive that treatment have earned a hardware diagnosis. TDR errors that stay fixed share a common aftercare: leave overclocks at stock unless you have a specific, validated reason — most "stable" overclocks are only stable until a driver update changes power behavior underneath them. Clean your vents on a schedule, because the gradual return of heat is the gradual return of crashes, and people forget the cleaning that fixed it a year ago. Keep DDU and a known-good driver installer archived together so any future driver corruption gets the full-wipe treatment immediately instead of three rounds of hopeful in-place reinstalls. If you do creative work, save frequently regardless — TDR resets can take unsaved work with them, and no driver fix changes that risk to zero. And treat a TDR that survives a DDU wipe, stock clocks, verified cooling, and a fresh OS as hardware until proven otherwise; at that point further software attempts just waste the warranty window.
