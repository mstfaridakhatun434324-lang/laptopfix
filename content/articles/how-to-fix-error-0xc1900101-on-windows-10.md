---
title: "How to Fix Windows 10 Update Error 0xC1900101"
slug: how-to-fix-error-0xc1900101-on-windows-10
date: 2026-09-07
categories: ["windows-errors"]
tags: ["0xC1900101", "feature update", "driver conflict"]
description: "Error 0xC1900101 kills Windows 10 feature updates, usually due to a driver conflict. Identify the bad driver and get the update installed."
thumbnail: "/images/thumbs/how-to-fix-error-0xc1900101-on-windows-10.webp"
faqs:
  - q: "What does error 0xC1900101 mean during a Windows 10 update?"
    a: "It is a generic rollback code meaning the feature update failed and Windows reverted to the previous version. The extended code after it (like 0x20017 or 0x30018) hints at the phase that failed, but the underlying cause is almost always a driver — storage, display, network, or antivirus filter drivers are the usual suspects. Less often, low disk space or corrupted system files are responsible."
  - q: "How do I find which driver caused 0xC1900101?"
    a: "Check C:\\$Windows.~BT\\Sources\\Panther\\setuperr.log after the rollback — the last errors before the failure usually name the driver or device. You can also open Device Manager and look for devices with yellow warning icons. The most reliable method is updating or removing suspect drivers one category at a time: storage controllers first, then display, then network, then antivirus."
  - q: "How much free space do I need for a Windows 10 feature update?"
    a: "Microsoft recommends at least 20 GB of free space on the system drive for a feature update, though the installer can technically proceed with less. In practice, aim for 30 GB or more — the update needs room to download, extract, and stage files plus keep a rollback copy. If space is tight, run Disk Cleanup and move personal files to another drive first."
  - q: "Should I disconnect peripherals during the update?"
    a: "Yes, it genuinely helps with 0xC1900101. External drives, USB hubs, printers, and dongles load extra drivers during the update, and any one of them can conflict. Disconnect everything except the charger, keyboard, and mouse before retrying the feature update — this simple step resolves a surprising number of failures."
---

Error 0xC1900101 is the classic "update failed and rolled back" code on Windows 10. You run the feature update, it grinds through the percentage, reboots a few times, and then lands you back on your old version with a message that the installation failed. Sometimes you get an extended code like 0xC1900101-0x20017, which narrows down the phase — but either way, the story is the same: something on your system fought the update and won.

In the overwhelming majority of cases, that something is a driver. Storage controller drivers, graphics drivers, and antivirus filter drivers are the repeat offenders. The fixes below focus on clearing those conflicts out of the way so the update can complete. Set aside an hour; driver cleanup takes a little patience but beats staring at another rollback.

## Why this happens

- **Incompatible storage or chipset drivers.** Old AHCI, RAID, or NVMe drivers crash the update during the driver-migration phase.
- **Graphics driver conflicts.** Outdated or custom OEM graphics drivers fail the update's driver validation.
- **Antivirus filter drivers.** Third-party antivirus hooks deep into the system and blocks the update's file operations.
- **Insufficient disk space.** The update needs room to stage files and keep a rollback copy; tight drives cause mid-install failures.
- **Connected peripherals.** External devices load drivers during the update that can conflict with the new build.
- **Corrupted system files or update cache.** Damaged components cause the installer to fail integrity checks.

## How to fix it

Work through these in order, retrying the update after each major step.

### Fix 1: Free up disk space and disconnect peripherals

Give the installer room and remove variables.

1. Open **Settings > System > Storage** and check free space on C: — aim for at least 30 GB free.
2. Run **Disk Cleanup** (`cleanmgr.exe`): select C:, click **Clean up system files**, and check **Windows Update Cleanup**, **Temporary files**, and **Delivery Optimization Files**.
3. Move large personal files (videos, downloads) to an external drive or cloud storage.
4. Unplug everything except the charger, keyboard, and mouse — external drives, printers, USB hubs, and dongles all come out.
5. Retry the feature update from **Settings > Update & Security > Windows Update**.

### Fix 2: Uninstall third-party antivirus temporarily

Antivirus filter drivers are a top cause of 0xC1900101.

1. Open **Settings > Apps** and uninstall your third-party antivirus completely (disabling is often not enough — the filter driver stays loaded).
2. Confirm **Windows Security** (Defender) is active so you are still protected.
3. Restart the laptop.
4. Run the feature update.
5. Reinstall your antivirus afterward if you prefer it over Defender.

### Fix 3: Update storage, chipset, and graphics drivers

Old drivers are the most common root cause — bring them current before retrying.

1. Open **Device Manager** (`Win + X`).
2. Expand **IDE ATA/ATAPI controllers** and **Storage controllers**; update each driver via **Update driver > Search automatically for drivers**.
3. Get the proper chipset driver from your laptop maker's support site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
4. Update the graphics driver from the GPU maker: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [NVIDIA](https://www.nvidia.com/Download/index.aspx), or [AMD](https://www.amd.com/en/support/download/drivers.html).
5. Restart and retry the update.

### Fix 4: Check the setup logs to name the culprit

If it fails again, read the logs instead of guessing.

1. After a rollback, open **File Explorer** and go to `C:\$Windows.~BT\Sources\Panther\` (enable hidden items in the **View** menu if you cannot see it).
2. Open **setuperr.log** in Notepad and scroll to the bottom — the final errors usually name a driver file or device.
3. Search the web for the exact driver filename plus your laptop model to confirm.
4. Update, roll back, or uninstall that specific driver in **Device Manager**, then retry the update.

### Fix 5: Run SFC, DISM, and reset the update cache

Corruption in system files or the update store can fail integrity checks.

1. Open **Command Prompt (Admin)**.
2. Run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Stop update services: `net stop wuauserv` and `net stop bits`.
4. Rename the cache: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
5. Restart the services: `net start wuauserv` and `net start bits`.
6. Retry the update.

### Fix 6: Update the BIOS

An outdated BIOS can block the new build's hardware initialization.

1. Check your current BIOS version with `msinfo32` (look at **BIOS Version/Date**).
2. Compare it with the latest on your manufacturer's support site.
3. Install the update with the charger connected and do not interrupt it.
4. Retry the feature update afterward.

### Fix 7: Perform an in-place upgrade with the Media Creation Tool

When Windows Update keeps failing, the Media Creation Tool often succeeds where it does not.

1. Download the **Media Creation Tool** for Windows 10 from Microsoft's website (find the link through [Microsoft Support](https://support.microsoft.com/en-us/windows)).
2. Run it and choose **Upgrade this PC now**.
3. Select **Keep personal files and apps** when prompted.
4. Let it complete — this reinstalls Windows 10 with the latest build while preserving everything.

A related install failure with its own fixes is [Windows 11 install error 0x80070002](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/), and the Windows 11 variant of this exact code is covered in our [0xC1900101 on Windows 11](/articles/how-to-fix-error-0xc1900101-in-windows-11-24h2/) guide.

## Closing

Error 0xC1900101 is frustrating because the rollback erases your progress each time, but it is almost always a driver standing in the update's way. Clear disk space, unplug peripherals, remove the antivirus temporarily, and update your storage and chipset drivers — that combination gets the feature update through in most cases. When it still fails, the setup logs will name the exact culprit, and the Media Creation Tool's in-place upgrade is a reliable fallback that keeps your files and apps intact.
