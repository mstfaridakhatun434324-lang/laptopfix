---
title: "KERNEL_SECURITY_CHECK_FAILURE in Windows 11 24H2: 7 Fixes That Work"
slug: how-to-fix-kernel-security-check-failure-in-windows-11-24h2
date: 2026-09-23
categories: ["windows-errors"]
tags: ["windows-11", "bsod", "kernel-security-check"]
description: "KERNEL_SECURITY_CHECK_FAILURE on Windows 11 24H2? Usually bad RAM or a corrupt driver. Diagnose it correctly with these 7 ordered fixes."
thumbnail: "/images/thumbs/how-to-fix-kernel-security-check-failure-in-windows-11-24h2.webp"
faqs:
  - q: "What does KERNEL_SECURITY_CHECK_FAILURE mean?"
    a: "Windows runs constant integrity checks on its own kernel data structures — linked lists, pool allocations, and security cookies. When one of those checks fails, Windows crashes immediately with this stop code rather than continue running on corrupted foundations. The usual causes are faulty RAM corrupting kernel data, a buggy driver writing where it should not, or corrupted system files."
  - q: "Is KERNEL_SECURITY_CHECK_FAILURE caused by a virus?"
    a: "Rarely, but it is worth ruling out — kernel-level malware can trip these integrity checks, which is exactly what they are designed to catch. In practice, though, the cause is bad RAM or a bad driver in the overwhelming majority of cases. Run a Defender Offline scan once to clear the question, then focus on memory and drivers."
  - q: "Why did it start after updating to 24H2?"
    a: "The 24H2 update replaced a large portion of the kernel and driver stack. If your RAM had a marginal fault that previous builds tolerated, 24H2's stricter integrity checks may now catch it on every boot. Likewise, drivers that worked on 23H2 can corrupt the new kernel structures. The update did not break your hardware — it exposed a weakness that was already there."
  - q: "Should I run a malware scan before trying the other fixes?"
    a: "Yes, it is worth 20 minutes. KERNEL_SECURITY_CHECK_FAILURE can be caused by rootkits or corrupt security components, so run a full scan with Windows Security first, then follow up with the free Microsoft Safety Scanner for a second opinion. If both come back clean, you can confidently move on to driver and memory troubleshooting without wondering about infection."
---

KERNEL_SECURITY_CHECK_FAILURE is Windows catching its own kernel data in a corrupted state and refusing to continue. On Windows 11 24H2 it often appears after the feature update, which makes people blame the update — but the update usually just exposed a RAM fault or driver bug that was quietly present before.

This guide diagnoses it properly: memory first, drivers second, system files third.

## Why this happens

- **Faulty RAM.** The single most common cause. Bad memory corrupts the kernel's linked lists and pool structures, failing the integrity checks.
- **A buggy driver corrupting kernel memory.** Storage, network, and antivirus filter drivers are the usual suspects on 24H2.
- **Corrupted system files from the 24H2 upgrade.** An interrupted or conflicted feature update damages kernel components.
- **Unstable overclocking or XMP profiles.** Aggressive memory timings cause intermittent corruption that fails integrity checks under load.
- **A failing SSD.** Corruption in paged-out kernel data read back from bad flash.
- **Kernel-level malware.** Rootkits modifying kernel structures trip the checks by design — uncommon but real.
- **Incompatible BIOS/firmware.** Old firmware misreporting hardware capabilities can lead drivers to corrupt kernel state.

## How to fix it

Work through these in order. The memory test comes early because it is the most likely answer.

### Fix 1: Run Windows Memory Diagnostic immediately

Do not skip this — bad RAM is the top cause and the test is free.

1. Save your work, press **Win + R**, type `mdsched.exe`, press **Enter** → **Restart now and check for problems**.
2. Let the full pass complete. After reboot, check results in **Event Viewer** → **Windows Logs** → **System**, filtering for **MemoryDiagnostics-Results**.
3. If errors are reported, skip to Fix 5 — you have found your cause.
4. If it passes, continue: a single pass can miss intermittent faults, so keep RAM on the suspect list until Fix 5's deeper test.

### Fix 2: Install all pending Windows and driver updates

Clear known 24H2 issues before deeper diagnosis.

1. Go to **Settings** → **Windows Update** → **Check for updates**; install everything including **Advanced options** → **Optional updates**.
2. Then update drivers from your laptop manufacturer's support site — **chipset**, **storage**, **network**, **graphics** — rather than relying solely on Windows Update.
3. Intel-based laptops can use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to detect the correct driver versions automatically.
4. Restart and test for a day under normal workload before continuing.

### Fix 3: Run a Defender Offline malware scan

Rule out kernel-level malware since this stop code is designed to catch it.

1. Open **Windows Security** → **Virus & threat protection** → **Scan options** → **Microsoft Defender Offline scan** → **Scan now**.
2. The laptop reboots into a clean offline environment and scans — this catches rootkits that hide from normal scans.
3. If threats are found and removed, retest stability for several days; reinfection suggests a compromised installer or download source worth investigating.
4. A clean scan means you can focus on hardware and drivers with confidence.

### Fix 4: Update or remove third-party kernel software

Antivirus and disk tools operating at kernel level are frequent integrity-check violators.

1. Open **Settings** → **Apps** → **Installed apps** and look for third-party antivirus, disk encryption, backup tools with kernel drivers, and "system optimizers."
2. Uninstall anything you do not actively need, using vendor removal tools for antivirus products to clear filter drivers completely.
3. Update anything you keep to the latest version — vendors continuously fix kernel-compatibility issues.
4. Confirm Microsoft Defender is active (**Settings** → **Privacy & security** → **Windows Security**) as your baseline.

### Fix 5: Deep-test the RAM and reset memory settings

The built-in test is a screen; MemTest86 is the diagnosis.

1. Create a MemTest86 USB drive (free download, run from another PC if needed) and boot from it.
2. Let it run at least 4 full passes — overnight is ideal. Even a single error means bad RAM.
3. If errors appear: power off, reseat the modules, and retest. Test sticks individually to isolate the bad one, then replace it with matching specs.
4. Enter the BIOS and disable XMP/EXPO or any memory overclocking, loading **Optimized Defaults** — then retest. If errors vanish at stock speeds, the overclock was the entire problem and your RAM is fine.
5. Laptops with soldered RAM showing errors need manufacturer service — back up immediately.

### Fix 6: Repair system files and check the drive

Fix corrupted kernel files and rule out the storage layer.

1. In **Terminal (Admin)**: `sfc /scannow` → `DISM /Online /Cleanup-Image /RestoreHealth` → `sfc /scannow` again.
2. Run `chkdsk C: /f /r` (type `Y`, restart, let it finish completely).
3. Check SMART: `wmic diskdrive get status` — every drive should report **OK**.
4. Microsoft documents these repair tools in their [Windows support resources](https://support.microsoft.com/en-us/windows).

### Fix 7: Check Driver Verifier status and update the BIOS

Clear the last configuration-level suspects.

1. Run `verifier /query` in an admin terminal. If Driver Verifier is enabled, run `verifier /reset` and restart — Verifier turns minor driver quirks into fatal integrity failures.
2. Update the BIOS/UEFI from your manufacturer's support site (AC power, do not interrupt) — firmware updates frequently include memory-compatibility and stability fixes relevant to this exact error.
3. If crashes survive all seven fixes, you are looking at a failing motherboard component or a deeply defective driver version — try rolling back recent drivers (**Device Manager** → device → **Properties** → **Driver** → **Roll Back Driver**) before seeking professional diagnosis.

## Closing

KERNEL_SECURITY_CHECK_FAILURE on 24H2 is a "trust but verify" error: Windows caught corruption in its own foundations, and your job is to find the source — usually RAM, sometimes a driver, rarely anything exotic. The memory diagnostic up front saves hours of misdirected driver work, so do not skip it. And if the 24H2 update was the trigger, remember it exposed the weakness rather than creating it; fixing the RAM or driver properly ends the crashes for good. For the closely related corruption error, see [CRITICAL_STRUCTURE_CORRUPTION in 24H2](/articles/how-to-fix-critical-structure-corruption-in-windows-11-24h2/); for the pre-24H2 variant, [KERNEL_SECURITY_CHECK_FAILURE after a Windows 11 update](/articles/how-to-fix-kernel-security-check-failure-after-windows-11-update/).
