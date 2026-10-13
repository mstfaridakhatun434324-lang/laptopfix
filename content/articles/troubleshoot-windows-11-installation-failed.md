---
title: "Windows 11 Installation Failed? How to Troubleshoot It"
slug: troubleshoot-windows-11-installation-failed
date: 2026-10-13
categories: ["windows-errors"]
tags: ["windows-11-installation", "setup-error", "upgrade"]
description: "Windows 11 installation failed with an error code? Read the code, fix the underlying cause, and get the install to complete with this guide."
thumbnail: "/images/thumbs/troubleshoot-windows-11-installation-failed.webp"
faqs:
  - q: "What do Windows 11 setup error codes like 0x80070002 mean?"
    a: "Setup error codes point at the failure stage. 0x80070002 is missing files (corrupt media or download), 0xC1900101 is a driver blocking the upgrade, 0x800F081F is missing source files for a component, and 0x8007042B-0x4000D is a second-boot migration failure. The code plus the phase tells you where to look."
  - q: "How much free space does Windows 11 setup really need?"
    a: "Microsoft says 64 GB, but upgrades go smoother with at least 20-30 GB free on top of that for staging. Low disk space causes some of the most cryptic setup failures — free space first, troubleshoot second."
  - q: "Should I use Windows Update, the Installation Assistant, or a USB?"
    a: "For a failing upgrade, switch methods: if Windows Update fails, try the Installation Assistant; if that fails, do a USB-based upgrade keeping files. Different methods hit different code paths, and a failure in one often succeeds in another."
  - q: "Can antivirus block a Windows 11 installation?"
    a: "Yes — third-party antivirus is a leading cause of 0xC1900101 upgrade failures. Uninstall it (not just disable it) before retrying the upgrade, and reinstall afterward. Windows Security protects you during the gap."
---
A failed Windows 11 installation is frustrating because the error codes look like serial numbers and the rollback leaves you exactly where you started. But those codes are actually specific: each one names a failure stage, and each stage has a known set of causes. A failed Windows 11 installation is frustrating because the error codes look like serial numbers and the rollback leaves you exactly where you started. But those codes are actually specific: each one names a failure stage, and each stage has a known set of causes.

This guide shows how to read what the installer is telling you, fix the underlying problem, and get the installation across the finish line — whether you are upgrading or installing clean. This guide shows how to read what the installer is telling you, fix the underlying problem, and get the installation across the finish line — whether you are upgrading or installing clean.

## Why this happens

- **Insufficient disk space.** The installer needs room to stage files; tight drives fail with misleading codes.
- **A blocking driver.** Old storage, antivirus filter, or peripheral drivers halt the upgrade (the 0xC1900101 family).
- **Corrupted installation media or download.** Damaged ISO/USB files fail checksum-style with 0x80070002-type errors.
- **Third-party antivirus.** Its filter drivers and locked files are the single most common upgrade blocker.
- **Incompatible hardware or BIOS settings.** TPM, Secure Boot, or old BIOS versions stop Windows 11 setup cold.
- **Peripheral interference.** USB devices with bad drivers hang the device-migration phase.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Read the error code and phase properly

The code tells you the what; the phase tells you the where. The code tells you the what; the phase tells you the where — and setuperr.log usually names the exact blocking component in plain text.

1. Note the full error code from the setup failure screen or **Settings > Windows Update** history.
2. Check `C:\$Windows.~BT\Sources\Panther\setuperr.log` — the last errors before failure name the blocking component.
3. Look up the code's family: 0xC1900101 means driver, 0x80070002/0x80070003 means missing files, 0x800F081F means source files. That decides which fix below to prioritize.

### Fix 2: Free disk space and clean the staging area

The cheapest fix for a whole class of failures. The cheapest fix for a whole class of failures — low disk space produces some of the most misleading error codes in all of Windows setup.

1. Free at least 30 GB on C: — empty Recycle Bin, run **Disk Cleanup** (**cleanmgr**) including **Clean up system files**.
2. Delete the failed attempt's staging folders: `C:\$Windows.~BT` and `C:\$Windows.~WS` (you may need to take ownership).
3. Retry the installation. If it was a space or staging-corruption issue, this alone fixes it.

### Fix 3: Uninstall third-party antivirus and disconnect peripherals

Removes the most common upgrade blockers in one move. Removes the most common upgrade blockers in one move: antivirus filter drivers and USB peripherals with bad drivers.

1. Uninstall (not just disable) any third-party antivirus — its filter drivers survive disabling.
2. Unplug every USB device except keyboard and mouse: printers, docks, external drives, webcams.
3. Disable VPN clients and disk-encryption tools temporarily.
4. Retry the upgrade with this minimal configuration.

### Fix 4: Update drivers and BIOS before retrying

An old storage or chipset driver is the classic 0xC1900101 cause. An old storage or chipset driver is the classic 0xC1900101 cause — and the BIOS updates that fix upgrade blocks are easy to overlook.

1. Update chipset, storage controller, and graphics drivers from your laptop maker's support site.
2. Update the BIOS — several vendors fixed Windows 11 upgrade blocks in BIOS updates.
3. Verify TPM 2.0 and Secure Boot are enabled: run `tpm.msc` and check **Secure Boot State** in `msinfo32`.
4. If a specific driver is named in setuperr.log, update or remove exactly that driver. Our [driver-focused BSOD walkthrough](/articles/driver-power-state-failure-windows-11-fix/) covers hunting bad drivers in depth.

### Fix 5: Re-download and rebuild clean installation media

Eliminates corrupted downloads as a variable. Eliminates corrupted downloads as a variable — a fresh ISO from Microsoft plus the Media Creation Tool removes two suspects at once.

1. Download a fresh ISO from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Create the USB with the Media Creation Tool — not a third-party tool — to avoid media quirks.
3. If upgrading, run `setup.exe` from the USB while in Windows and choose **Keep personal files and apps**.
4. For a truly stubborn failure, boot the USB and do a clean install (back up first — this erases everything).

### Fix 6: Run the Windows Update troubleshooter and reset components

For failures coming through Windows Update specifically. For failures coming through Windows Update specifically, the troubleshooter plus a servicing-stack repair clears the most common Update-side blocks.

1. Run **Settings > System > Troubleshoot > Other troubleshooters > Windows Update > Run**.
2. In an elevated **Command Prompt**, run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` to repair the servicing stack.
3. Retry via the Installation Assistant from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) instead of Windows Update — different code path, often succeeds where Update failed.

### Fix 7: Check hardware compatibility directly

When all else fails, verify the machine actually qualifies. When all else fails, verify the machine actually qualifies — PC Health Check gives you a straight answer instead of another cryptic code.

1. Run Microsoft's PC Health Check from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) to confirm TPM, Secure Boot, CPU, and RAM requirements.
2. For borderline-old CPUs, the installer may simply refuse — that is a hardware wall, not a bug.
3. Check your SSD health too (`wmic diskdrive get status`); a failing drive corrupts staged setup files. For Safe Mode-based repairs of a half-upgraded system, see our [Safe Mode guide](/articles/how-to-boot-windows-11-in-safe-mode/).

## Closing

Windows 11 installation failures are almost never random — the error code and setuperr.log always point at a cause, usually disk space, a blocking driver, antivirus, or bad media. Read the code, remove the blocker, switch install methods if needed, and the setup that failed three times will usually sail through on the fourth. Write down the error code and the fix that worked — if you ever set up another machine, that note turns a repeat failure into a five-minute job.
