---
title: "Troubleshoot NVIDIA Driver Crashing: Advanced Repair Workflow"
slug: troubleshoot-nvidia-driver-crashing
date: 2026-10-11
categories: ["drivers"]
tags: ["nvidia", "driver crash", "tdr", "gpu troubleshooting", "nvlddmkm"]
description: "Advanced troubleshooting for NVIDIA driver crashes: read crash dumps, isolate driver vs. heat vs. power faults, and stabilize a crashing GPU."
thumbnail: "/images/thumbs/troubleshoot-nvidia-driver-crashing.webp"
faqs:
  - q: "How do I know whether my NVIDIA crashes are caused by the driver or by heat?"
    a: "Correlate crashes with temperature logs. If crashes happen only above 85°C or after long sessions, heat is the cause. If they happen on a cool GPU within minutes of boot or on the desktop, the driver is the cause. Logging both with HWiNFO during the crashing workload gives you a definitive answer instead of a guess."
  - q: "What is nvlddmkm.sys and why does it appear in crash reports?"
    a: "Nvlddmkm.sys is the NVIDIA Windows kernel-mode driver itself. When a blue screen or Event Viewer entry names it, that means the NVIDIA driver was executing when the fault occurred. It does not automatically mean the driver is buggy — overheating and power faults also crash inside the driver — but it confirms the GPU subsystem is where to investigate."
  - q: "Should I increase the TDR delay to stop the crashes?"
    a: "Only as a diagnostic step, not a fix. Raising TdrDelay gives a slow GPU more time before Windows declares it hung, which helps identify whether the watchdog is tripping prematurely. If crashes continue with a longer delay, the underlying instability — driver, heat, or power — still needs the real fixes in this guide."
  - q: "Can a Windows update break a previously stable NVIDIA driver?"
    a: "Yes. Feature updates can replace your NVIDIA driver with an older inbox version, reset power plans, or change the TDR behavior. After any major Windows update, verify your NVIDIA driver version is still the one you installed and reinstall it cleanly if crashes begin. This is one of the most common triggers of sudden new crashes."
---

Basic NVIDIA fixes — update the driver, hope for the best — fail often enough that a deeper workflow is worth having. This guide is that workflow: a structured troubleshoot for recurring NVIDIA driver crashes that treats the driver, the thermals, and the power delivery as three suspects to be eliminated with evidence. It is written for crashes that survived the simple fixes, the ones that keep coming back.

The core technique is isolation. Change one variable at a time, measure, and record. By the end you will know which subsystem is at fault instead of cycling drivers at random.

## Why this happens

- **Layered driver corruption:** Years of installs leave conflicting binaries that no in-place update fully clears.
- **Regression in a specific release:** A driver version can be unstable only on certain laptop GPU and chipset combinations.
- **Thermal instability:** Heat-induced errors crash inside the driver, masquerading as driver bugs.
- **Power starvation under load:** Weak adapters or degraded batteries cannot sustain GPU boost clocks.
- **TDR watchdog tripping early:** The default two-second hang detection fires on GPUs that are slow but not hung.
- **Hook conflicts from overlays:** Injected overlay code destabilizes the driver pipeline after updates.
- **Failing GPU hardware:** VRAM or core degradation produces crashes that no software fix touches.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Capture the crash signature

Open Event Viewer (Win + X), go to Windows Logs, System, and filter for the nvlddmkm error around each crash — note the exact timestamp and any bugcheck code. Then install HWiNFO, enable logging, and run the workload that crashes; when it does, check the log for GPU temperature, clock speed, and power draw in the seconds before the crash. A crash at 90°C+ with maxed clocks is thermal. A crash at 65°C on the desktop is driver. A crash coinciding with a power-draw spike on a third-party charger is power. Write the pattern down. Every later step is judged against this baseline — "did the crash signature change?" is how you know a fix worked.

### Fix 2: Strip the driver to bare metal with DDU

Download DDU and your target driver — start with your laptop maker's NVIDIA package. Disconnect from the internet to stop Windows Update interfering, boot into Safe Mode, and run DDU with the "remove GeForce Experience" option too — GFE's overlay and services are independent crash contributors. Reboot into normal mode and install the downloaded driver with Custom install and "Perform a clean installation." Reconnect and test the exact crashing workload. Our step-by-step [NVIDIA clean-install guide](/articles/how-to-update-nvidia-drivers-clean-install-on-windows-11/) covers the installer options that prevent leftover-file conflicts. If the crash signature is unchanged, the driver files were never the problem — move to thermals and power with confidence instead of trying a fourth driver version.

### Fix 3: Eliminate thermals as a variable

With the clean driver in place, run the crashing workload with the laptop on a cooling pad, vents unobstructed, room as cool as you can make it. Log temperatures. If crashes vanish in the cool test, heat is confirmed: clean the fans and heatsink fins with compressed air, and on machines over two years old, consider repasting the GPU — dried thermal paste is the classic cause of "it used to be stable." Also verify the fans actually ramp under load; a fan stuck quiet (see our cooling guides) produces exactly this crash pattern. Do not skip this step because the laptop "doesn't feel that hot" — internal GPU hotspots exceed what the chassis tells your hand.

### Fix 4: Eliminate power as a variable

Test exclusively on the original manufacturer charger with its full wattage — check the brick's label against the laptop's requirement. Disconnect USB-C docks and hubs during the test, since some negotiate lower power delivery than the barrel charger provides. If the battery is swollen or heavily degraded, test with it removed on AC power if the design allows. Log GPU power draw in HWiNFO: crashes that coincide with the card failing to sustain its boost power point to delivery, not the driver. An underpowered or dying adapter is a cheap fix for a problem that looks exactly like a driver bug.

### Fix 5: Bisect driver versions methodically

If thermals and power are cleared, the driver version is genuinely suspect. Using DDU each time, test three points: the laptop OEM's driver, the current NVIDIA release from [NVIDIA's download page](https://www.nvidia.com/Download/index.aspx), and one release two to three versions older. Test the identical workload for the same duration on each, logging crashes. This bisection finds the stable island instead of wandering. Record which versions pass — driver regressions cluster around specific releases, and knowing your stable version ends the update lottery permanently. Keep notes; "the March release was stable, the May one crashed" is actionable intelligence.

### Fix 6: Remove all injected software and test clean-booted

Disable every overlay: GeForce Experience, Discord, Xbox Game Bar, OBS, screen recorders, and GPU tweaking tools. Then run `msconfig`, hide Microsoft services, disable the rest, and restart into a clean boot. Test the workload. If crashes stop, re-enable software in halves until the offender returns — this binary search is faster than guessing. Pay special attention to anything that updated around the time crashes began; overlay hooks break silently with their own updates. For persistent display-driver-level issues beyond NVIDIA-specific ones, our guide to [display driver crashes](/articles/how-to-fix-display-driver-stopped-responding-on-windows-11/) covers the shared Windows mechanisms.

### Fix 7: Test the TDR delay and accept a hardware verdict

Create the `TdrDelay` DWORD set to 8 under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers` and restart. If crashes stop, the watchdog was tripping on a slow-but-healthy GPU — keep the tweak and monitor. If crashes continue identically through clean drivers, cool thermals, solid power, no overlays, multiple driver versions, and a longer TDR delay, the GPU hardware is failing: degraded VRAM or core. Run the manufacturer's diagnostics GPU test for confirmation. A confirmed hardware fault on a laptop usually means board-level repair or replacement — get a quote before deciding, and back up your data regardless.

## Closing

Stubborn NVIDIA crashes surrender to isolation: capture the signature, clean the driver completely, clear thermals, clear power, bisect versions, evict injected software, and only then judge the hardware. Each step eliminates a suspect with evidence, so you never go in circles. Most crashing GPUs are saved at step two or three; the ones that are not have earned an honest hardware verdict instead of another hopeful driver install.
