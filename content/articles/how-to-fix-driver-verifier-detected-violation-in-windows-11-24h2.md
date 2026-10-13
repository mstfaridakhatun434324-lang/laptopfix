---
title: "Fix DRIVER_VERIFIER_DETECTED_VIOLATION in Windows 11 24H2"
slug: how-to-fix-driver-verifier-detected-violation-in-windows-11-24h2
date: 2026-10-10
categories: ["windows-errors"]
tags: ["bsod", "stop code 0xc4", "driver verifier", "windows 11 24h2"]
description: "End the DRIVER_VERIFIER_DETECTED_VIOLATION boot loop in Windows 11 24H2: disable Verifier safely and fix the driver it caught."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-detected-violation-in-windows-11-24h2.webp"
faqs:
  - q: "What is DRIVER_VERIFIER_DETECTED_VIOLATION?"
    a: "Stop code 0x000000C4 means Driver Verifier — Windows' built-in driver stress-test tool — caught a driver breaking the rules. Here's the twist: Verifier only runs if someone turned it on. Most people hitting this never enabled it deliberately; it was left on by a technician, a tutorial, or a previous troubleshooting session."
  - q: "Why does it keep crashing in a loop?"
    a: "Because Verifier loads at every boot and immediately stress-tests drivers again. Each boot triggers the same violation and the same blue screen. The loop breaks the moment you disable Verifier with verifier /reset from Safe Mode or WinRE."
  - q: "Should I just leave Driver Verifier on after fixing the driver?"
    a: "No. Verifier is a diagnostic instrument, not a protective feature — it makes crashes more likely by design and slows the system. Turn it off with verifier /reset as soon as you've identified and fixed the offending driver."
  - q: "Does 24H2 change anything about this error?"
    a: "Windows 11 24H2 tightened driver enforcement and updated several inbox drivers, so a driver that passed Verifier on 23H2 can newly fail on 24H2. The fix process is the same, but pay extra attention to drivers dated before the 24H2 upgrade."
---
DRIVER_VERIFIER_DETECTED_VIOLATION (stop code 0x000000C4) has a peculiar cause: the crash is the diagnostic tool working as intended. Driver Verifier is a Windows utility that deliberately stresses drivers to expose bugs — and when it catches one misbehaving, it blue-screens with this exact stop code. The catch is that Verifier doesn't turn itself on. If you're seeing this, Verifier is running, and it was probably left enabled by an earlier troubleshooting session, a repair shop visit, or a tutorial you followed months ago and forgot.

On Windows 11 24H2 this surfaces more often because the update refreshed inbox drivers and tightened enforcement, so borderline drivers that previously squeaked by now get flagged. The fix has two phases: first stop the crash loop by disabling Verifier, then deal with the driver it caught — because Verifier did find a real bug, even if the timing is inconvenient.

## Why this happens

- **Driver Verifier was left enabled.** The overwhelmingly common cause. It persists across reboots until explicitly reset, so one forgotten `verifier` session months ago produces today's boot loop.
- **A genuinely buggy third-party driver.** Verifier caught a real violation — a driver corrupting pool memory, mishandling IRPs, or breaking locking rules. The bug is real even though Verifier's aggression made it visible.
- **A driver that 24H2's stricter checks newly flag.** Drivers written against older WDK expectations can trip Verifier's updated checks after the 24H2 upgrade.
- **Verifier configured too aggressively.** Selecting "all drivers" or enabling Low Resource Simulation produces crashes that look like driver bugs but are really Verifier false positives under artificial stress.
- **Corrupted driver binaries.** A half-written driver file from an interrupted update fails Verifier's integrity checks immediately at load.
- **Leftover Verifier settings after a repair install.** Verifier configuration lives in the registry and can survive in-place upgrades, resurrecting the loop on a "fresh" system.

## How to fix it

Work through these in order. Phase one (Fixes 1–2) stops the bleeding; phase two fixes the underlying driver.

### Fix 1: Disable Driver Verifier from Safe Mode

This single command ends the crash loop for most people.

1. Interrupt boot three times (power off at the Windows logo) to reach **Automatic Repair**, then **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, press **4** for Safe Mode.
2. Open **Terminal (Admin)** and run `verifier /reset`.
3. Confirm it reports the settings were cleared, then reboot normally.
4. If Windows boots cleanly and stays up, Verifier was your whole problem — but don't stop here. Check Fix 3 to see what Verifier had been complaining about, because the underlying driver bug is still present. For general safe-mode entry alternatives, see [how to boot Windows 11 in safe mode](/articles/how-to-boot-windows-11-in-safe-mode/).

### Fix 2: Reset Verifier from WinRE when Safe Mode also crashes

If Verifier is configured aggressively enough to crash even Safe Mode, go around it.

1. Boot to **Automatic Repair** > **Advanced options** > **Troubleshoot** > **Advanced options** > **Command Prompt**.
2. Run `verifier /reset` and then `verifier /query` to confirm the settings are cleared.
3. Type `exit`, choose **Continue** to boot Windows normally.
4. Still crashing? From the same Command Prompt, run `reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v VerifyDrivers /f` and `reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v VerifyDriverLevel /f` to surgically remove Verifier's registry settings, then reboot.

### Fix 3: Find which driver Verifier caught

The crash dumps from the loop are evidence — read them before the trail goes cold.

1. Once stable, open `C:\Windows\Minidump` and install **WinDbg Preview** from the Microsoft Store.
2. Load the newest dump from the crash loop and run `!analyze -v`.
3. The **IMAGE_NAME** tells you the driver Verifier flagged. Also run `!verifier` in WinDbg — with Verifier dumps it lists exactly which rule was violated and by whom.
4. Write the driver name down. If the analysis is new to you, the [WinDbg dump-reading guide](/articles/best-way-to-read-dump-files-with-windbg/) covers these commands step by step.

### Fix 4: Update or replace the flagged driver

Verifier found a real bug — now fix the driver, not the messenger.

1. In **Device Manager** (`devmgmt.msc`), find the device, right-click > **Uninstall device**, ticking **Attempt to remove the driver for this device**.
2. Reboot, then install the newest driver from your laptop manufacturer's support site — Dell, HP, Lenovo, Acer, or ASUS, matched to your exact model.
3. For graphics drivers, prefer a clean install: NVIDIA users should download from [NVIDIA](https://www.nvidia.com/Download/index.aspx) and choose **Custom** > **Perform a clean installation**; AMD users from [AMD's driver page](https://www.amd.com/en/support/download/drivers.html).
4. Date-check the driver: anything predating your 24H2 upgrade deserves replacement even if it's "the latest" the vendor lists.

### Fix 5: Roll back if a recent driver update caused it

When the timeline shows a driver update right before the loop started:

1. **Device Manager** > device **Properties** > **Driver** tab > **Roll Back Driver**, and pick the reason.
2. If rollback is greyed out, uninstall as in Fix 4 and manually install the previous version from the vendor's driver archive.
3. Block Windows Update from re-pushing the bad version via **Settings** > **Windows Update** > **Advanced options** > **Optional updates** — uncheck driver updates there, or use the show/hide updates troubleshooter from [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 6: Repair system files and re-test with Verifier properly

Once the driver is replaced, verify the fix scientifically.

1. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in **Terminal (Admin)** to clean up any collateral damage from the crash loop.
2. Re-enable Verifier narrowly: `verifier`, custom settings, all checks except Low Resource Simulation, selecting **only the replaced driver**.
3. Reboot and use the PC normally for a few hours. No crash means the new driver is clean.
4. Run `verifier /reset` one final time and reboot. Confirm with `verifier /query` that nothing is selected. Verifier's job is done — leave it off.

### Fix 7: Uninstall the 24H2 update path as a fallback

If the flagged driver has no newer version and the vendor hasn't fixed it:

1. **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the 24H2 enablement/feature update if the loop began with it.
2. Pause updates for a few weeks while the vendor catches up.
3. This is a holding pattern, not a fix — revisit once an updated driver appears.

## Closing

DRIVER_VERIFIER_DETECTED_VIOLATION in 24H2 is almost anticlimactic once you know the secret: somebody left the diagnostic tool running, and `verifier /reset` ends the loop in under a minute. The real work is honoring what Verifier found — it flagged a genuine driver bug, and replacing that driver properly is what keeps the blue screen from coming back through some other stop code next month. Disable the tool, fix the driver, verify, then leave Verifier off until you actually need it again.
