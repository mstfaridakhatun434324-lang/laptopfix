---
title: "Update Fails With Error 0xC1900101 on Windows 10: A Driver-First Fix"
slug: how-to-fix-update-fails-with-error-0xc1900101-on-windows-10
date: 2026-09-07
categories: ["windows-update"]
tags: ["0xc1900101", "windows 10", "update failed", "driver error"]
description: "Error 0xC1900101 on Windows 10 almost always means a driver blocked the upgrade. Find the offending driver and get the update installing cleanly."
thumbnail: "/images/thumbs/how-to-fix-update-fails-with-error-0xc1900101-on-windows-10.webp"
faqs:
  - q: "What does 0xC1900101 mean on Windows 10?"
    a: "It is a generic rollback code that means a driver caused the upgrade to fail. The extended code after it (for example 0x30018 or 0x40017) tells you which phase failed, but in practice the cause is almost always the same: an incompatible, outdated, or buggy device driver that the new Windows build cannot work with. Updating or removing that driver fixes it."
  - q: "How do I find which driver caused 0xC1900101?"
    a: "Check the setup log files. The most useful are setupact.log and setuperr.log in the hidden $WINDOWS.~BT\\Sources\\Panther folder. Search for driver names mentioned near failure entries, or use Microsoft's SetupDiag tool, which parses the logs automatically and names the likely culprit driver."
  - q: "Can antivirus cause 0xC1900101?"
    a: "Yes — third-party antivirus and firewall drivers are among the most common triggers. Their filter drivers hook deep into the storage and network stacks, and the upgrade process cannot safely migrate them. Uninstalling third-party security software before the upgrade (keeping Windows Defender active) resolves a large share of these failures."
  - q: "Is 0xC1900101 the same on Windows 10 and 11?"
    a: "The code means the same thing on both — a driver-driven upgrade rollback — and the fix approach is identical. The main difference is which drivers tend to trigger it, since Windows 11 has stricter driver requirements. Our companion guide covers the [Windows 11 variant of this error](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/) if you are upgrading that OS instead."
---

Error 0xC1900101 is Windows 10's way of saying "a driver killed this upgrade." The code itself is generic — Microsoft uses it for any upgrade that rolls back because of a driver problem — but the fix pattern is remarkably consistent: find the bad driver, update it or remove it, and run the upgrade again.

The extended code that follows 0xC1900101 (like 0xC1900101–0x30018) tells you which upgrade phase failed, but you do not need to memorize the phases. What you need is the driver hunt described below, because in nine cases out of ten the culprit is one of a short list: storage drivers, display drivers, antivirus filter drivers, or an old peripheral driver that has not been updated in years. Work the list in order — most users are upgrading successfully by Fix 4.

## Why this happens

- **Incompatible storage driver:** Old AHCI, RAID, or NVMe drivers cannot handle the new build's storage stack.
- **Antivirus filter driver conflict:** Third-party security drivers hook the kernel in ways the upgrade cannot migrate.
- **Outdated display driver:** Ancient GPU drivers crash the upgrade during the display migration phase.
- **Problematic peripheral driver:** Old printer, scanner, or USB device drivers fail the driver's compatibility checks.
- **BIOS too old:** Firmware predating the target build lacks interfaces the new Windows expects.
- **Corrupted driver store:** Damaged entries in the driver repository confuse the upgrade's driver migration.
- **Insufficient disk space:** The upgrade needs room to stage drivers and rollback data; without it, driver migration fails.
- **Third-party disk tools:** Encryption or disk utility drivers block the partition operations the upgrade requires.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Remove third-party antivirus

This single step resolves more 0xC1900101 failures than everything else combined.

1. Open **Settings > Apps > Installed apps** and uninstall your third-party antivirus completely — disabling is not enough, because the filter driver stays loaded.
2. Make sure Windows Security (Defender) activates automatically after the uninstall.
3. Restart the laptop.
4. Run the Windows update again without reinstalling the antivirus.
5. Reinstall your preferred security software only after the upgrade succeeds.

### Fix 2: Update the critical drivers

Update the drivers most likely to block the upgrade before retrying. Intel's detection tool at [Intel DSA](https://www.intel.com/content/www/us/en/support/detect.html) finds current chipset and storage drivers automatically.

1. Update your storage controller driver from the laptop or motherboard manufacturer's site.
2. Update the display driver — use the GPU vendor's clean-install option (NVIDIA, AMD, or Intel).
3. Update the network drivers (both Wi-Fi and Ethernet).
4. Update the chipset driver package for your machine.
5. Restart and retry the upgrade with all critical drivers current.

### Fix 3: Disconnect all non-essential hardware

Every connected device is a driver the upgrade must migrate; fewer devices means fewer failure points.

1. Unplug everything USB except keyboard and mouse — printers, scanners, external drives, dongles, hubs.
2. If you use a docking station, undock and run the upgrade on the bare laptop.
3. Disable Bluetooth in Settings to sideline Bluetooth drivers.
4. Eject any SD cards or secondary storage.
5. Retry the upgrade in this minimal configuration.

### Fix 4: Run SetupDiag to name the culprit

When the generic fixes are not enough, let Microsoft's diagnostic read the logs. The [Windows support hub](https://support.microsoft.com/en-us/windows) documents the upgrade log locations.

1. Download SetupDiag from Microsoft's website on a working computer (or the same one).
2. Run it — it scans the Panther logs from the failed upgrade automatically.
3. Read its output: it names the driver or component most likely responsible.
4. Update, roll back, or uninstall that specific driver.
5. Retry the upgrade.

### Fix 5: Free disk space aggressively

Driver migration needs staging room, and cramped drives fail in misleading ways.

1. Open **Settings > System > Storage** and check free space.
2. Run Disk Cleanup on the system drive, including **system files** and **Windows Update Cleanup**.
3. Move personal files to external storage until at least 25 GB is free.
4. Uninstall large unused programs.
5. Retry the upgrade with the breathing room it needs.

### Fix 6: Update the BIOS

An outdated BIOS is a known 0xC1900101 trigger, especially on laptops more than a few years old.

1. Check your current BIOS version (run `msinfo32` and look at BIOS Version/Date).
2. Visit your laptop manufacturer's support site and compare with the latest release.
3. If an update exists, download it and follow the manufacturer's instructions exactly — keep the charger connected.
4. Do not interrupt the BIOS flash for any reason.
5. After the flash, retry the Windows upgrade.

### Fix 7: Clean the driver store

Remove ghost and damaged driver packages that confuse the migration.

1. Open Device Manager and enable **View > Show hidden devices**.
2. Look for grayed-out (non-present) devices, especially under storage and display — uninstall them.
3. Open an elevated Command Prompt and run `pnputil /enum-drivers` to list third-party driver packages.
4. Remove packages for hardware you no longer own with `pnputil /delete-driver oemXX.inf /uninstall` (use the exact published name shown).
5. Restart and retry the upgrade with a clean driver store. A clean store also helps when [downloads themselves keep stalling](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/) before the upgrade even begins.

### Fix 8: Perform the upgrade from installation media

If Windows Update keeps failing, the media-based upgrade often succeeds — it handles driver migration slightly differently. First make sure the [update service is healthy](/articles/how-to-fix-windows-update-service-not-running-in-windows-11-24h2/) so the media creation step itself works.

1. Download the Windows 10 Media Creation Tool from Microsoft.
2. Run it and choose **Upgrade this PC now**.
3. When prompted, choose to keep personal files and apps.
4. Let the upgrade run — with antivirus removed and drivers updated, it usually completes.
5. After success, reinstall your security software and reconnect your devices.

## Closing

0xC1900101 looks cryptic, but it is one of the most diagnosable update errors in Windows 10: a driver blocked the upgrade, and the fixes above find it. Antivirus removal and critical driver updates clear the majority of cases; SetupDiag names the culprit in the stubborn ones. Once you know the pattern, the code stops being intimidating — it is just Windows telling you, in its own terse way, to clean up your drivers before upgrading.
