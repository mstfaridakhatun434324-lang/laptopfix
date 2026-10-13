---
title: "DVD Drive Not Detected in Windows 11 24H2? Bring It Back"
slug: "how-to-fix-dvd-drive-not-detected-in-windows-11-24h2"
date: "2026-09-26"
categories: ["drivers"]
tags: ["dvd drive", "optical drive", "windows 11 24h2", "device manager", "drivers"]
description: "Your DVD or CD drive vanished after Windows 11 24H2? Learn why optical drives disappear and follow proven steps to make Windows detect yours again."
thumbnail: "/images/thumbs/how-to-fix-dvd-drive-not-detected-in-windows-11-24h2.webp"
faqs:
  - q: "Why did my DVD drive disappear after the Windows 11 24H2 update?"
    a: "The 24H2 update can corrupt the UpperFilters and LowerFilters registry values that Windows uses to load optical drive drivers, which makes the drive vanish from File Explorer and Device Manager. It can also replace the working SATA controller driver with an incompatible version. The drive hardware is almost always fine — the OS simply lost the software path to it."
  - q: "How do I check if Windows detects my DVD drive at all?"
    a: "Open Device Manager and expand DVD/CD-ROM drives. If the drive appears with a warning icon, it is a driver problem. If the section is missing entirely, restart into BIOS and check whether the drive appears there — BIOS detection means hardware is fine and Windows is at fault. Also check Disk Management, since a drive with a corrupted driver sometimes appears there without a letter."
  - q: "Can a registry fix restore a missing DVD drive?"
    a: "Yes, deleting the corrupted UpperFilters and LowerFilters values from the optical drive's registry key is the classic, Microsoft-documented fix for vanishing DVD drives. Those values tell Windows which filter drivers to load, and when they corrupt, the whole device fails to start. Removing them lets Windows load the drive with default handling, which restores detection immediately."
  - q: "Is my DVD drive dead if BIOS does not see it?"
    a: "Not necessarily, but it is a strong hardware signal. First check the drive's SATA and power connections if it is a desktop-style external unit or a removable laptop bay drive — reseat them. For internal laptop drives, a BIOS update can restore detection of drives the firmware stopped enumerating. If BIOS still shows nothing after reseating, the drive itself has likely failed."
---

Optical drives are fading from modern laptops, but plenty of machines still ship with them — and Windows 11 24H2 has an unfortunate habit of making them vanish. One day the drive is in File Explorer, the next it is gone from everywhere: no drive letter, no entry in Device Manager, as if it was never installed.

This particular disappearance is famous among technicians because the cause is so specific: corrupted filter-driver registry values. Windows loads optical drives through a chain of filter drivers, and when 24H2 damages that chain, the drive silently drops out. The hardware is innocent in the vast majority of cases, and the fix is refreshingly direct.

## Why this happens

- **Corrupted UpperFilters/LowerFilters registry values:** The classic cause — damaged filter entries prevent the optical driver stack from loading.
- **Incompatible SATA controller driver:** 24H2 replaces the working AHCI driver, breaking communication with the optical drive.
- **Drive disabled in BIOS:** Firmware updates can reset SATA port settings, hiding the drive from the OS.
- **ATAPI driver corruption:** The core cdrom.sys driver files can be damaged during the update.
- **Power management on the SATA link:** Aggressive link power management can leave the drive unresponsive after sleep.
- **Loose drive connection:** On laptops with removable bays, the drive can shift just enough to lose contact.
- **Failed drive hardware:** Laser or controller failure in the drive itself, the least common cause.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Delete the corrupted filter registry values
Open Registry Editor and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e965-e325-11ce-bfc1-08002be10318}`. In the right pane, delete the `UpperFilters` and `LowerFilters` values if present. Close the editor and restart. This is Microsoft's own documented fix for vanishing optical drives, and it resolves the 24H2-specific failure in most cases. If you are nervous about registry edits, export the key first as a backup. For related device-detection technique, see our guide on [enabling hidden devices](/articles/how-to-enable-hidden-devices-in-device-manager-on-windows-11/).

### Fix 2: Check BIOS detection to isolate hardware vs software
Restart into BIOS/UEFI setup and look at the storage or SATA device list. If the DVD drive appears in BIOS but not Windows, the problem is 100% software — continue with the fixes below confidently. If BIOS does not list it, reseat the drive (for removable-bay laptops, slide it out and back in firmly) and check again. BIOS-level absence after reseating points to a dead drive or failed SATA port, which no Windows fix can address.

### Fix 3: Reinstall the SATA/AHCI controller driver
In Device Manager, expand "IDE ATA/ATAPI controllers," right-click the SATA AHCI controller, and choose Uninstall device (do not delete the driver if Windows warns about boot). Restart — Windows reinstalls the controller driver fresh. Better yet, download the chipset driver for your model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) and install it, since the OEM AHCI driver handles optical drives more reliably than the generic one 24H2 may have installed.

### Fix 4: Force redetection and update the cdrom driver
In Device Manager, click Action and "Scan for hardware changes." If the DVD drive appears with a warning, right-click it, choose Update driver, then "Browse my computer" and "Let me pick" — select the standard CD-ROM driver. You can also uninstall the DVD/CD-ROM entry and rescan to force a clean driver load. Check Disk Management too: occasionally the drive appears there without a letter, and assigning one restores File Explorer visibility. Our [DVD detection walkthrough](/articles/how-to-fix-dvd-drive-not-detected-step-by-step/) covers these steps with screenshots.

### Fix 5: Disable SATA link power management
Open Power Options, advanced settings, and expand "PCI Express" then "Link State Power Management" — set it to Off. Also check for a SATA or AHCI power setting and disable aggressive power saving. After sleep or hibernation, link power management can leave the optical drive in a state Windows cannot wake, which looks exactly like a vanished drive. A full shutdown and cold boot after changing this confirms whether power management was the trigger.

### Fix 6: Repair system files and check the ATAPI stack
Open an elevated Command Prompt and run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth`. The 24H2 update process itself can damage the cdrom.sys driver or its supporting files, and this repair pass restores them from known-good copies. Reboot after the repair and rescan for hardware changes. Microsoft documents optical drive troubleshooting at Windows support if you need the official flow.

### Fix 7: Test the drive as external hardware
If the internal drive remains invisible, remove it (on bay-style laptops) and test it in an inexpensive USB optical drive enclosure, or test a known-good drive in the laptop's bay. This definitively separates a dead drive from a dead SATA port. Replacement internal DVD drives are cheap for models that still use them, and a USB DVD drive is a practical alternative that sidesteps the internal bus entirely. If BIOS never saw the drive and reseating failed, replacement is the answer.

## Closing
A DVD drive that vanishes after Windows 11 24H2 is a registry and driver problem far more often than a hardware death. Deleting the corrupted filter values, refreshing the SATA controller driver, and confirming BIOS-level detection brings the drive back in the great majority of cases — no new hardware required. Optical drives need little maintenance, but two habits prevent a repeat: after each Windows feature update, glance at File Explorer to confirm the drive is still listed — catching a filter corruption early means a thirty-second registry fix instead of a rediscovery project. Avoid registry cleaners and aggressive "system optimizer" tools, which are notorious for damaging the very filter values that keep optical drives working. If you use the drive for ripping or burning, keep the lens clean with a proper lens-cleaning disc; read errors from a dirty lens mimic driver problems and send people down the wrong path. For laptops where the internal drive has failed outright, a USB DVD drive is often the pragmatic permanent replacement — it sidesteps the internal SATA bus entirely and works through the same software. And if you rarely use optical media, consider whether the bay is better repurposed: many laptops accept a hard-drive caddy in the optical bay, turning dead weight into extra storage.
