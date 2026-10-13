---
title: "What to Do If the Display Driver Stopped Responding"
slug: what-to-do-if-display-driver-stopped-responding
date: 2026-09-23
categories: ["drivers"]
tags: ["display driver stopped responding", "tdr error", "nvlddmkm", "amdkmdap", "gpu crash fix"]
description: "Display driver stopped responding and recovered? Understand TDR errors (nvlddmkm, amdkmdap, igfx) and apply seven fixes from clean reinstalls to TDR tuning."
thumbnail: "/images/thumbs/what-to-do-if-display-driver-stopped-responding.webp"
faqs:
  - q: "What does 'display driver stopped responding and has recovered' actually mean?"
    a: "It means Windows' Timeout Detection and Recovery (TDR) watchdog noticed the GPU driver had not responded within two seconds, so it reset the driver instead of letting the system freeze. The screen flickers black briefly and the application may crash, but Windows keeps running. Occasional TDRs under extreme load are benign; frequent ones signal a driver, overclock, thermal, power, or hardware problem worth diagnosing."
  - q: "Is it safe to change TdrDelay in the registry?"
    a: "Yes. Raising TdrDelay from 2 to 8 seconds only extends how long Windows waits before resetting an unresponsive GPU — it cannot damage hardware. If the GPU is truly hung, recovery just takes a few seconds longer. Create a System Restore point first, and do not set TdrLevel to 0 (that disables recovery entirely and converts stalls into hard freezes). Revert the values if they make no difference."
  - q: "Why do TDR errors happen more in some games than others?"
    a: "Different games stress different GPU subsystems — one may hammer VRAM bandwidth while another stresses shader compilation or video encode. A marginal overclock, a VRAM weakness, or a driver bug in a specific API path (DirectX 12 vs Vulkan) will therefore trigger TDRs in one title and run clean in another. Note which games trigger it: that pattern is valuable diagnostic evidence pointing at the stressed subsystem."
  - q: "Can RAM cause display driver TDR errors?"
    a: "Indirectly, yes. Unstable system RAM (bad XMP profile, failing DIMM) corrupts data the GPU driver is processing, producing TDRs that look exactly like GPU problems. If TDRs survive a clean driver install at stock clocks and safe temperatures, run MemTest86 or Windows Memory Diagnostic. RAM-caused TDRs often come with random app crashes and occasional blue screens outside graphics workloads — that broader instability is the tell."
---

'Display driver stopped responding and has recovered' is Windows' Timeout Detection and Recovery (TDR) system doing its job: the GPU driver took too long to answer, so Windows reset it instead of freezing the whole machine. You see a brief black flicker, maybe a frozen app, and life goes on — until it happens every ten minutes and 'recovered' starts feeling optimistic.

The three driver names in the error tell you which GPU is involved: nvlddmkm (NVIDIA), amdkmdap (AMD), or igfx (Intel integrated). The underlying causes are the same family as any GPU instability — corrupt driver installs, overclocks, heat, power, and an impatient watchdog timer — but the fix order here is tuned for the TDR pattern specifically rather than full crashes.

For vendor-specific deep dives, see our [NVIDIA crash guides](/articles/how-to-fix-nvidia-driver-crashing-on-windows-11/) and the [Windows 11 TDR walkthrough](/articles/how-to-fix-display-driver-stopped-responding-after-windows-11-update/); [ASUS-specific TDR cases](/articles/how-to-fix-display-driver-stopped-responding-on-asus-laptop/) are covered separately for that brand's quirks.

## Why this happens

- **Corrupt graphics driver installation** — Layered installs and interrupted updates leave the driver in a state that stalls under load.
- **TDR timeout too aggressive (default 2s)** — Heavy but legitimate workloads trip the two-second watchdog on slower or heavily loaded GPUs.
- **Unstable overclock / undervolt** — Marginal clocks that pass benchmarks can still stall the driver during specific workloads.
- **GPU overheating** — Thermal throttling creates the exact stalls the TDR watchdog punishes.
- **Insufficient power delivery** — Voltage droop under load stalls the GPU; laptops on battery saver are especially prone.
- **Conflicting overlays and capture hooks** — Injected overlays stall the render pipeline during mode switches.
- **Failing GPU hardware / VRAM** — Degrading silicon stalls unpredictably; the last suspect, not the first.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean-reinstall the graphics driver

The highest-yield TDR fix regardless of GPU brand. Remove everything, start fresh.

1. Download the latest driver for your GPU: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).
2. Boot into Safe Mode and run DDU (Display Driver Uninstaller) — Clean and restart.
3. Install the downloaded driver with the clean-install option ticked.
4. Block Windows Update from replacing it (Device Installation Settings > No). Retest the workload that triggered TDRs.

### Fix 2: Increase the TDR delay

When the driver recovers on its own every time, the watchdog is likely just impatient. Give it more room.

Create a System Restore point before editing the registry — it takes seconds and makes the change fully reversible. Note that TdrDelay helps only when the driver genuinely recovers on its own (Event ID 4101); if the machine blue-screens or hard-freezes instead, the GPU is not recovering at all and the watchdog timing is not your problem.

1. Open regedit and go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create DWORD (32-bit) **TdrDelay** = `8` (decimal) and **TdrDdiDelay** = `8`.
3. Optionally create **TdrLevel** = `3` to keep recovery enabled (do not set 0 — that disables recovery and turns stalls into freezes).
4. Restart. If TDRs stop, the GPU was simply slow, not broken. Revert if nothing changes.

### Fix 3: Reset clocks and test thermals

Separate silicon problems from software problems in under an hour.

Laptop owners should pay special attention to the 'plugged in vs battery' variable: many TDR loops happen only on battery, where the GPU is power-limited into instability. If your crashes vanish the moment you plug in, the fix is power policy (Best performance, plugged in while gaming), not drivers.

1. Reset any GPU/CPU overclock and undervolt to stock; close tuning utilities.
2. Monitor GPU temperature under the TDR-triggering workload — sustained 86°C+ means clean the cooling system.
3. On desktops, verify separate PCIe power cables per connector.
4. On laptops, test plugged in at Best performance — battery modes starve the GPU.

### Fix 4: Disable overlays and background injectors

TDRs that strike on alt-tab, resolution change, or game launch scream overlay conflict.

1. Disable in-game overlays in GeForce Experience / AMD Adrenalin / Discord.
2. Close FPS counters, RivaTuner, and RGB software that hooks into games.
3. Disable Windows Game Bar's background recording while testing.
4. Retest the exact trigger scenario for at least an hour.

### Fix 5: Test with hardware acceleration toggled

Browser and app hardware acceleration routes work through the same driver path that TDRs.

1. In Chrome/Edge, toggle Settings > System > 'Use hardware acceleration when available' to the opposite state.
2. In Discord and other Electron apps, toggle Hardware Acceleration similarly.
3. If TDRs only happen in one app, the app's acceleration path plus your driver is the conflict — keep it off there.
4. This is diagnostic: it narrows the trigger, not a permanent lifestyle choice.

### Fix 6: Check Event Viewer for the pattern

The TDR event details distinguish driver stalls from hardware faults.

1. Open Event Viewer > Windows Logs > System. Filter for source **nvlddmkm / amdkmdap / Display** around crash times.
2. Note Event ID 4101 (recovered) vs 4109/4111 patterns and any preceding disk/power warnings.
3. TDRs preceded by Kernel-Power 41 (unexpected shutdown) suggest power, not the driver.
4. Bring this log to support forums or warranty claims — it is the evidence technicians ask for. Microsoft's official Windows support documentation covers log-collection guidance if you need it.

### Fix 7: Stress-test VRAM and consider hardware fault

When software is exhausted and TDRs come with artifacts, test the silicon.

1. Run OCCT's VRAM test or FurMark for 20–30 minutes at stock clocks.
2. Artifacts (checkerboards, colored blocks) plus errors = failing GPU/VRAM.
3. No errors after extended testing = software-side; revisit Fixes 1–2 with an older known-stable driver version.
4. For failing hardware under warranty, RMA with the Event Viewer logs attached.

## Closing

The TDR message is Windows protecting you from a freeze, and the fix order follows the evidence: clean driver reinstall first, then give the watchdog more patience with TdrDelay, then rule out clocks, heat, power, and overlays. Genuine hardware failure is real but rare — most 'display driver stopped responding' loops end at Fix 1 or Fix 2.
