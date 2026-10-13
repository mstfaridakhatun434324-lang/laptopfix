---
title: "Fix 'Display Driver Stopped Responding' on an ASUS Laptop"
slug: how-to-fix-display-driver-stopped-responding-on-asus-laptop
date: 2026-10-09
categories: ["drivers"]
tags: ["display driver stopped responding", "asus", "nvlddmkm", "tdr error", "gpu crash"]
description: "Fix the 'display driver stopped responding and has recovered' error on ASUS laptops: TDR tuning, clean GPU driver install, and thermal checks."
thumbnail: "/images/thumbs/how-to-fix-display-driver-stopped-responding-on-asus-laptop.webp"
faqs:
  - q: "What does 'display driver stopped responding' mean?"
    a: "Windows caught the GPU driver hanging and restarted it — the Timeout Detection and Recovery mechanism. The screen flickers or goes black for a few seconds, then recovers, often with a notification. Occasional TDRs are a nuisance; repeated ones every few minutes point to driver corruption, overheating, or an unstable GPU clock."
  - q: "Is the TDR error a sign my ASUS GPU is dying?"
    a: "Usually not. Most TDR loops come from corrupted drivers, dust-clogged cooling, or unstable factory overclock profiles — all fixable. Hardware failure is the diagnosis of last resort, reached only when clean drivers, normal thermals, and stock clocks still produce crashes, especially crashes accompanied by visual artifacts."
  - q: "Will increasing the TDR delay fix the crashes?"
    a: "It can stop the recovery loop by giving the GPU more time to complete heavy operations before Windows declares a hang. Raising TdrDelay from 2 to 8 seconds in the registry is a legitimate stabilization step, but treat it as a bandage — still pursue the underlying driver, thermal, or clock cause afterward."
  - q: "Why does it only happen in games on my ASUS laptop?"
    a: "Games sustain full GPU load for long periods, exposing marginal drivers, overheating, and unstable overclocks that idle desktop use never triggers. ASUS Armoury Crate Turbo profiles in particular can set GPU clocks the silicon cannot sustain, which is why the error appears in games but never while browsing."
---

"Display driver stopped responding and has recovered" — the TDR error — is Windows restarting your GPU driver after it hung. The screen goes black for a few seconds, maybe flickers, then comes back, often with the notification to prove it happened. On ASUS laptops it clusters around gaming, video editing, and external monitors: exactly the workloads that stress the GPU. Occasional TDRs after a driver update are annoying; repeated TDRs every few minutes make the machine unusable.

The TDR mechanism itself is protective — it prevents a full system freeze. Your job is to find why the driver keeps hanging: corrupted driver files, GPU overheating, an unstable overclock from Armoury Crate, or a genuinely failing GPU. The order below runs from most common and easiest to rarest and hardest.

## Why this happens

- **Corrupted GPU driver:** Partially updated or damaged driver files cause the hangs TDR was designed to catch.
- **GPU overheating:** Dust-clogged fans and dried thermal paste push the GPU past its stability point under load.
- **Unstable factory overclock:** ASUS Armoury Crate Turbo/Manual profiles push GPU clocks or voltage curves the silicon cannot sustain.
- **TDR timeout too aggressive:** The default 2-second TdrDelay can be too short for heavy compute workloads, triggering recoveries on operations that would have finished.
- **Conflicting Intel + NVIDIA/AMD drivers:** On Optimus/hybrid ASUS laptops, a broken iGPU driver destabilizes the dGPU handoff.
- **Failing GPU hardware:** Degrading VRAM or power delivery causes hangs no driver can fix — the last resort diagnosis.
- **Windows Update driver mismatch:** Windows pushes a driver version that conflicts with ASUS's customized GPU firmware or power tables.
- **Background overlays hooking the driver:** Discord overlay, GeForce Experience overlay, and screen recorders inject into the graphics pipeline and trigger hangs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Do a clean GPU driver reinstall with DDU

1. Download Display Driver Uninstaller and the latest notebook GPU driver for your ASUS model — from the official ASUS driver download page for your exact model, or [NVIDIA](https://www.nvidia.com/Download/index.aspx) / [AMD](https://www.amd.com/en/support/download/drivers.html) notebook drivers.
2. Boot into Safe Mode and run DDU: **Clean and restart** for your GPU brand.
3. Install the fresh driver with the **clean install** option, then reboot.
4. Test with the workload that triggered TDRs. Corrupted drivers cause the majority of TDR loops, and DDU is the definitive reset. For NVIDIA-specific crash patterns beyond TDR recoveries, the [NVIDIA driver crash guide](/articles/nvidia-driver-keeps-crashing-windows-11/) covers additional scenarios.

### Fix 2: Check thermals and clean the cooling system

1. Install HWiNFO64 and log GPU temperature during the triggering workload. Sustained temperatures above 87–90°C on a laptop GPU invite instability.
2. Blow out the intake/exhaust vents with compressed air (laptop off, battery removed if possible).
3. Elevate the rear of the laptop for airflow and retest.
4. If temperatures remain high, the thermal paste or pads likely need replacement — a service job on most ASUS models, but the single most effective hardware fix for load-triggered TDRs.

### Fix 3: Reset Armoury Crate to stock GPU settings

1. Open **Armoury Crate → System → GPU Power Saver / Operating Mode** and switch from Turbo to **Performance** or **Silent**.
2. If you set a manual overclock or custom fan/GPU curve, reset everything to defaults.
3. Disable **GPU overclock** features entirely and retest. Factory Turbo profiles are a known TDR source on some ASUS models — the silicon lottery means your unit may not sustain the profile's clocks.

### Fix 4: Increase the TDR delay in the registry

1. Open **regedit** → `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`.
2. Create a DWORD (32-bit) named **TdrDelay** with value `8` (seconds), and optionally **TdrDdiDelay** = `8`.
3. Reboot. The GPU gets 8 seconds instead of 2 before Windows declares a hang, eliminating recoveries on merely-slow operations.
4. Treat this as stabilization, not a cure — continue with driver and thermal fixes. Microsoft documents TDR behavior in [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Repair the Intel iGPU driver on hybrid models

1. On Optimus laptops the display pipeline runs through Intel graphics even when the NVIDIA/AMD GPU renders.
2. Update the Intel graphics driver via the [Intel driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) or ASUS support.
3. In **Armoury Crate → GPU Mode**, try switching between **Standard/Optimus** and **Ultimate** (dGPU direct) to see if one path is stable.
4. A broken iGPU driver producing TDRs blamed on the discrete GPU is a classic misdiagnosis — the [clean-install driver guide](/articles/how-to-update-nvidia-drivers-clean-install-in-windows-11-24h2/) covers the dGPU side thoroughly.

### Fix 6: Disable overlays and background GPU hooks

1. Turn off the Discord overlay (**Settings → Game Overlay**), GeForce Experience in-game overlay, and Xbox Game Bar (**Settings → Gaming**).
2. Close screen recording software (OBS, etc.) during testing.
3. Disable hardware acceleration in browsers temporarily to isolate the trigger.
4. If TDRs stop, re-enable overlays one at a time to find the offender.

### Fix 7: Stress-test to confirm or rule out hardware failure

1. Run FurMark or a demanding game for 30 minutes while logging temperatures and watching for TDRs or artifacts (colored blocks, texture corruption).
2. Artifacts plus TDRs at normal temperatures point to failing VRAM or GPU power delivery.
3. Run ASUS's built-in diagnostics (MyASUS → System Diagnostics) targeting the GPU.
4. If clean drivers, normal thermals, stock clocks, and no overlays still produce TDRs with artifacts, the GPU is failing — contact ASUS support while under warranty. Laptop GPUs are soldered, so this means board-level service.

## Closing

TDR errors look scary but resolve to a short list: corrupted driver, overheating, unstable overclock, or — rarely — dying hardware. Clean-install the GPU driver with DDU, verify thermals under load, reset Armoury Crate to stock clocks, and only then consider the TDR delay tweak or hardware failure. Work the list in order and the recoveries stop; skip steps and you will chase the symptom in circles.
