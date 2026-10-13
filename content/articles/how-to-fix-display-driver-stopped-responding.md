---
title: "Display Driver Stopped Responding? Fix TDR Crashes on Your Laptop"
slug: how-to-fix-display-driver-stopped-responding
date: 2026-09-30
categories: ["drivers"]
tags: ["display driver", "tdr error", "gpu crash", "nvidia", "screen freeze"]
description: "\"Display driver stopped responding and has recovered\" on your laptop? Learn what TDR errors mean and the exact fixes, from clean driver installs to TDR delay tweaks."
thumbnail: "/images/thumbs/how-to-fix-display-driver-stopped-responding.webp"
faqs:
  - q: "What does 'display driver stopped responding and has recovered' mean?"
    a: "It's Windows' Timeout Detection and Recovery (TDR) kicking in: the GPU took longer than two seconds to respond, so Windows reset the graphics driver instead of blue-screening. You see a brief freeze or black flash, then a notification. Occasional TDRs are harmless, but frequent ones point to driver bugs, overheating, or unstable GPU clocks that need fixing."
  - q: "Can overheating cause the display driver to stop responding?"
    a: "Absolutely — it's one of the top causes on laptops. When the GPU overheats, it throttles and can miss the TDR timeout, triggering a reset. If crashes happen during gaming or video rendering but never when idle, suspect thermals first: clean the vents, elevate the laptop for airflow, and monitor GPU temperatures with HWiNFO or the manufacturer's utility."
  - q: "Will increasing the TDR delay fix the crashes?"
    a: "It can stop the symptom but not the disease. Raising TdrDelay from 2 to 8 seconds gives a struggling GPU more time before Windows resets it, which helps with heavy workloads on marginal drivers. But if the root cause is a corrupt driver or overheating, the crashes will return — use the registry tweak as a complement to a proper fix, not a replacement."
  - q: "Should I use DDU before reinstalling my graphics driver?"
    a: "Yes, when standard reinstalls fail. Display Driver Uninstaller (DDU) removes every trace of the old driver — registry entries, folders, services — in Safe Mode, eliminating corrupted remnants that a normal reinstall leaves behind. It's the technician's standard step for recurring TDR errors, and takes about ten minutes including the reboot cycle."
---

The screen freezes for two seconds, goes black, and comes back with a little notification: 'Display driver stopped responding and has recovered.' That's Windows' Timeout Detection and Recovery — TDR — doing its job. Your GPU missed its deadline, Windows reset the driver, and you avoided a full blue screen. When it happens once a month, ignore it. When it happens every gaming session, something needs fixing.
TDR crashes on laptops come from a short list of usual suspects: a buggy or corrupted graphics driver, an overheating GPU squeezed into a thin chassis, unstable factory overclocks, or a Windows update that replaced your working driver. This guide works through them in diagnostic order, starting with the free and easy fixes. If your crashes involve an NVIDIA card specifically, our [NVIDIA driver crashing guide](/articles/nvidia-driver-keeps-crashing-windows-11/) goes deeper on that hardware.
The single most effective fix for recurring TDR errors is a true clean reinstall of the graphics driver — not the quick reinstall, but the scorched-earth version with Display Driver Uninstaller in Safe Mode. We'll get there, but first we'll rule out the simpler causes so you don't nuke a working setup unnecessarily. For the proper method, see our [clean NVIDIA install walkthrough](/articles/how-to-update-nvidia-drivers-clean-install-in-windows-11-24h2/) if you run GeForce hardware.

## Why this happens

- **Corrupted graphics driver installation.** Partial updates and interrupted installs leave mixed old/new driver files that trip the TDR watchdog.
- **Buggy driver release.** Some driver versions are simply unstable on certain GPU and laptop combinations — the release notes' 'known issues' section is worth reading.
- **GPU overheating.** Laptop GPUs throttle under heat; a throttled GPU can miss the two-second TDR deadline and get reset.
- **Unstable factory overclock.** Some gaming laptops ship with aggressive GPU clocks that aren't stable in all workloads.
- **Windows Update driver replacement.** Windows swaps your manufacturer-tuned GPU driver for a generic one that misbehaves under load.
- **Failing GPU hardware.** Less common, but artifacting alongside TDRs suggests the silicon itself is degrading.
- **Conflicting overlays and capture software.** Discord overlay, screen recorders, and some antivirus 'gaming modes' hook the graphics pipeline and trigger timeouts.
- **Insufficient power delivery.** On battery or with an underpowered charger, the GPU can't hold its clocks and stutters into a TDR.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Note the pattern before changing anything

Diagnosis first: when the crashes happen tells you where to look. Five minutes of observation prevents hours of wrong fixes.

1. Write down what you were doing each time: gaming, video editing, YouTube, or idle on the desktop.
2. Check whether crashes happen on battery, on AC power, or both — power-related TDRs only appear on battery.
3. Open Event Viewer (Windows + X → Event Viewer) → Windows Logs → System, and filter for source 'nvlddmkm' or 'amdkmdap' around the crash time.
4. Look for visual artifacts (colored squares, lines) before the freeze — artifacts point toward hardware or heat, clean freezes toward drivers.
5. If crashes started right after a driver or Windows update, you already know your prime suspect.

### Fix 2: Do a true clean reinstall with DDU

The number-one fix for recurring TDRs. Display Driver Uninstaller in Safe Mode removes every trace the standard uninstaller leaves behind.

1. Download DDU from its official source and the latest GPU driver from NVIDIA, AMD, or Intel — save the driver installer locally first.
2. Disconnect from the internet (unplug Ethernet / turn off WiFi) so Windows can't auto-install a driver mid-process.
3. Boot into Safe Mode (Settings → Recovery → Advanced startup → Troubleshoot → Startup Settings).
4. Run DDU, select your GPU brand, choose 'Clean and restart.'
5. After reboot, install the downloaded driver (choose Custom/Clean install if the installer offers it), reconnect to the internet, and test under load.

### Fix 3: Rule out overheating

If TDRs strike under load but never at idle, heat is the prime suspect — and laptops are thermal pressure cookers.

1. Install HWiNFO64 and log GPU temperature during the workload that triggers crashes; sustained temps above 85–90°C are a red flag.
2. Blast compressed air through the exhaust vents (laptop off) to clear dust from the heatsink fins.
3. Elevate the rear of the laptop an inch or two for airflow — a hard book works; avoid soft surfaces that block intakes.
4. In your GPU control panel, cap the frame rate or enable vsync to reduce sustained load as a test.
5. If the laptop is over two years old and runs hot at idle, the thermal paste may need replacement — a repair-shop job on most models.

### Fix 4: Roll back or try a different driver version

When the crashes started with a specific driver release, the release itself is the bug. Don't fight it — step back or sideways.

1. Open Device Manager → Display adapters → your GPU → Properties → Driver tab → Roll Back Driver (if available).
2. If rollback is grayed out, use DDU (Fix 2) and install the previous driver version from the vendor's archive.
3. Check the driver release notes for your exact symptom — vendors often list TDR fixes per version.
4. For NVIDIA, the 'Studio' driver branch is sometimes more stable than 'Game Ready' on laptops used for mixed work.
5. Once stable, consider pausing automatic driver updates so Windows doesn't re-install the bad version.

### Fix 5: Increase the TDR delay via the registry

This gives the GPU more time before Windows declares a timeout — helpful for heavy workloads on otherwise healthy hardware.

1. Press Windows + R, type regedit, and navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers.
2. Right-click → New → DWORD (32-bit) Value, name it TdrDelay, and set its value to 8 (decimal).
3. Optionally create TdrDdiDelay as a DWORD set to 10 for good measure.
4. Reboot and test the workload that was crashing.
5. If crashes persist unchanged, revert the values — the delay is a bandage, and the real cause still needs fixing.

### Fix 6: Disable overlays and background GPU hooks

Overlays inject themselves into the graphics pipeline; a buggy hook can stall the GPU just long enough to trip TDR.

1. Disable the Discord overlay (User Settings → Game Overlay → off) and test.
2. Turn off GeForce Experience / AMD Adrenalin in-game overlay temporarily.
3. Close screen-recording software (OBS, Xbox Game Bar capture) during testing.
4. Disable any antivirus 'game mode' or 'hardware acceleration' features one at a time.
5. Re-enable them one by one after stability returns to identify the culprit.

### Fix 7: Test on AC power with the original charger

Power starvation causes clock instability that looks exactly like a driver bug — especially on gaming laptops.

1. Plug in the laptop's original charger (not a weaker USB-C phone charger) and retest the crashing workload.
2. In Windows power settings, set the power mode to 'Best performance' while plugged in.
3. In NVIDIA Control Panel / AMD Adrenalin, set Power management mode to 'Prefer maximum performance' as a test.
4. If crashes vanish on AC power, your battery or charger can't sustain the GPU — replace the weak link.
5. Persistent crashes on AC power with clean drivers and good thermals point to hardware — check warranty status via [Dell's support site](https://www.dell.com/support) or your maker's equivalent.

## Closing

TDR errors are Windows telling you the GPU stumbled — your job is figuring out whether it tripped over a bad driver, heat, or hardware. Clean-reinstall the driver first, check thermals second, and you'll resolve the vast majority of cases without spending a cent.
