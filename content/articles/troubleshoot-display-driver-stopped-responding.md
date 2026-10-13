---
title: "Troubleshoot 'Display Driver Stopped Responding' Errors"
slug: troubleshoot-display-driver-stopped-responding
date: 2026-10-07
categories: ["drivers"]
tags: ["display driver", "tdr", "gpu timeout", "driver crash", "nvlddmkm stopped"]
description: "Troubleshoot display driver timeout crashes: diagnose TDR causes, clean-install GPU drivers, and stabilize an unstable graphics driver."
thumbnail: "/images/thumbs/troubleshoot-display-driver-stopped-responding.webp"
faqs:
  - q: "What is TDR and why does it crash my display driver?"
    a: "TDR stands for Timeout Detection and Recovery, Windows' watchdog for the GPU. If the graphics driver doesn't respond within about two seconds, Windows resets it to avoid a full system crash. The screen flickers black and recovers. Frequent TDRs mean the GPU is repeatedly hanging, which points to driver corruption, overheating, unstable clocks, or failing hardware."
  - q: "How is troubleshooting TDR different from a quick driver reinstall?"
    a: "A quick reinstall fixes simple corruption, but persistent TDRs need systematic diagnosis: confirming temperatures, testing stock clocks, checking power delivery, and isolating software conflicts. This guide treats TDR as a symptom to diagnose rather than a driver to replace, so you find the actual cause instead of reinstalling drivers repeatedly and hoping."
  - q: "Can RAM cause display driver TDR errors?"
    a: "Yes, though it's underappreciated. Unstable system RAM — especially overclocked or XMP memory — corrupts data the GPU driver works with, producing TDR-pattern crashes that look exactly like GPU problems. If TDRs survive GPU driver reinstalls and temperature fixes, run MemTest86. Faulty RAM is a real and testable cause."
  - q: "When should I suspect the GPU hardware is dying?"
    a: "Suspect hardware when TDRs persist across multiple driver versions, at stock clocks, with temperatures under control, in Safe Mode, and in a second operating system like Linux. Artifacts (colored blocks, lines, texture corruption) alongside TDRs strengthen the hardware case. No software fix repairs degrading VRAM or a failing GPU core."
---

This is the diagnostic companion to the quick-fix TDR guide: instead of jumping to solutions, we systematically isolate the cause of "display driver stopped responding" crashes. TDR (Timeout Detection and Recovery) is Windows resetting a hung GPU driver — the screen blacks out for seconds, then recovers. Occasional TDRs are noise. Patterned, repeatable TDRs are a symptom with a findable cause.

The method: reproduce reliably, then eliminate variables one at a time — temperature, clocks, drivers, power, RAM, software conflicts — until the trigger reveals itself. If you haven't tried the basic clean driver reinstall yet, start with the [quick TDR fix guide](/articles/how-do-i-fix-display-driver-stopped-responding/) first; this guide is for crashes that survive it.

## Why this happens

- **Driver corruption or bugs:** The most common cause — damaged files, conflicting remnants, or a genuinely buggy driver release.
- **GPU overheating:** Thermal instability hangs the GPU under load; TDR fires as designed.
- **Unstable core/memory clocks:** Factory or manual overclocks that are marginally stable trip TDR in demanding workloads.
- **Unstable system RAM:** Bad or overclocked RAM corrupts GPU driver data, mimicking GPU failure.
- **Power delivery problems:** Failing adapters, aggressive power states, or overloaded circuits starve the GPU mid-render.
- **TDR timeout too short:** The default 2-second limit can fire on legitimate heavy compute or complex scenes.
- **Software conflicts:** Overlays, capture tools, and driver-hooking utilities destabilizing the graphics pipeline.
- **Degrading GPU hardware:** Failing VRAM or GPU cores produce TDRs no software fix resolves.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Establish a reliable reproduction case

1. Identify exactly what triggers the TDR: a specific game, a scene, a benchmark, video rendering, or idle desktop use. Write it down.
2. Note the timing: immediate on load, after 20 minutes (heat soak pattern), or random.
3. Test whether it happens at the Windows desktop with no 3D load — idle TDRs point at drivers or power states rather than heat or clocks.
4. A reproducible trigger turns every subsequent fix into a clean experiment: apply fix, run trigger, observe.
5. Without reproduction, you're guessing. With it, each step below gives a definitive yes/no answer.

### Fix 2: Monitor temperatures during the trigger

1. Run HWiNFO64 with logging enabled, then execute your reproduction case until the TDR fires.
2. Check the log: GPU core, hotspot, and VRAM temperatures in the seconds before the crash.
3. Sustained readings above 90°C (core) or 100°C+ (hotspot/VRAM) indicate thermal triggering.
4. If heat is implicated: clean vents, elevate the laptop, replace dried thermal paste, and retest — TDRs that vanish with 10°C lower temperatures were thermal all along.
5. Cool-running TDRs (under 80°C) eliminate heat and point to drivers, clocks, power, or RAM. Thermal behavior also overlaps with [general display driver instability](/articles/best-way-to-fix-display-driver-stopped-responding/).

### Fix 3: Test at guaranteed stock settings

1. Reset the GPU to stock clocks (MSI Afterburner reset, or the vendor tool's default profile).
2. Disable XMP/DOCP memory overclocking in BIOS — run RAM at JEDEC stock speeds as a test.
3. Disable CPU overclocking/undervolting temporarily.
4. Run your reproduction case. Stability at full stock proves an overclock or undervolt was the trigger.
5. Reintroduce tweaks one at a time afterward if you want them — but know that marginal stability is the classic source of "it worked for months then started TDRing" as silicon and thermals drift.

### Fix 4: Clean-install drivers with DDU in Safe Mode

1. Download the target driver version first ([NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), [Intel](https://www.intel.com/content/www/us/en/support/detect.html)), plus DDU.
2. Boot into Safe Mode, run DDU to remove all GPU driver traces (select "clean and restart").
3. Install the downloaded driver fresh — not over the top, but onto the DDU-cleaned system.
4. Test your reproduction case before installing GeForce Experience, overlays, or tuning tools.
5. If TDRs persist across a DDU-clean install of both the current and a previous known-good driver version, the driver itself is likely not the cause — continue down the list.

### Fix 5: Test system RAM

1. Create a MemTest86 USB drive and run at least 2 full passes (several hours).
2. Any error — even one — means the RAM is unstable and a suspect in TDR crashes.
3. If errors appear with XMP enabled but not at stock speeds, the memory overclock is the problem; run at stock or replace the kit.
4. Reseat RAM modules (on laptops with socketed RAM) and retest — poor contact causes intermittent errors.
5. RAM-induced TDRs are the great mimics: everything points at the GPU, but the corruption originates in system memory feeding the driver bad data.

### Fix 6: Stabilize power delivery

1. Test on the original manufacturer charger — underrated third-party chargers starve the GPU under load.
2. In the GPU control panel, set **power management to maximum performance** to eliminate power-state transition hangs.
3. Disable **PCI Express Link State Power Management** in Windows Power Options.
4. If TDRs correlate with other high-draw devices (external drives, docks), test with them disconnected — total system power budget matters on laptops.
5. Power-related TDRs often show a pattern: fine in light games, crashing in heavy ones, worse on battery than on AC.

### Fix 7: Extend the TDR timeout and observe

1. In regedit, go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers` (export the key first as backup).
2. Create QWORD `TdrDelay` = **8** (decimal) and optionally `TdrDdiDelay` = **10**.
3. Restart and run your reproduction case.
4. If TDRs stop: the GPU was stalling but recovering — investigate what's slow (heavy scene, shader compilation, background load) rather than treating the timeout as the fix.
5. If TDRs continue at 8 seconds, the GPU is hard-hanging, not just slow — this strengthens the hardware-failure hypothesis. Either way, revert the registry change once diagnosis is complete unless you need it as a workaround.

### Fix 8: Eliminate software conflicts, then judge hardware

1. Disable ALL overlays (Steam, Discord, GeForce Experience, Xbox Game Bar) and close capture/recording software.
2. Uninstall system optimizers, driver updaters, and RGB tools that hook the graphics stack.
3. Test your reproduction case in this minimal state.
4. Boot a Linux live USB and run a GPU stress test there — TDR-equivalent hangs in Linux across driver versions = hardware.
5. The hardware verdict requires the full elimination: multiple driver versions, stock clocks, cool temperatures, tested RAM, stable power, no conflicting software, crashes in two operating systems. When that bar is met, the GPU (usually VRAM) is failing — on laptops, that's a board-level repair decision.

## Closing

TDR troubleshooting is elimination science: reproduce reliably, then remove variables — heat, clocks, drivers, RAM, power, software — until the crash stops or every variable is cleared. Most cases resolve at the driver or temperature step. The ones that survive the full gauntlet have earned the hardware diagnosis, and you'll know it with evidence rather than suspicion.
