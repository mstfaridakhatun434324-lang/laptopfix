---
title: "INACCESSIBLE_BOOT_DEVICE: How to Fix It Step by Step"
slug: how-to-fix-inaccessible-boot-device-reddit
date: 2026-09-20
categories: ["windows-errors"]
tags: ["blue screen", "inaccessible_boot_device", "boot repair"]
description: "INACCESSIBLE_BOOT_DEVICE means Windows lost contact with your drive during boot. Fix BIOS storage settings, rebuild the boot files, and start up again."
thumbnail: "/images/thumbs/how-to-fix-inaccessible-boot-device-reddit.webp"
faqs:
  - q: "What does INACCESSIBLE_BOOT_DEVICE mean?"
    a: "It means Windows started loading but then couldn't communicate with the drive holding the operating system. The boot process got far enough to begin, then lost the disk. Common triggers are a BIOS storage mode change, a corrupted boot configuration, a failed Windows update touching storage drivers, or a drive that is physically failing or disconnected."
  - q: "Will I lose my files fixing this error?"
    a: "Usually not. The error is about Windows reaching the drive, not about your files being gone — your data is almost always intact on the disk. All the core fixes (BIOS settings, boot repair, driver rollback) leave your files alone. Only a clean reinstall would erase data, and that's the last resort after everything else fails."
  - q: "Can a Windows update cause INACCESSIBLE_BOOT_DEVICE?"
    a: "Yes, it's a classic pattern. An update can install a storage driver that doesn't match your BIOS storage mode, or corrupt the boot configuration data. That's why the error so often appears the morning after an update. Uninstalling the latest update from the recovery environment fixes these cases quickly."
  - q: "What if my drive doesn't show up in the BIOS?"
    a: "Then Windows never had a chance — this is hardware. Power off, and if it's a laptop with an accessible drive bay, reseat the SSD or hard drive. If it still doesn't appear in the BIOS, the drive has likely failed and needs replacing. At that point your priority shifts to data recovery, ideally by connecting the drive to another PC with a USB adapter."
---

INACCESSIBLE_BOOT_DEVICE is the blue screen you get when Windows can't find its own drive partway through starting up. It's especially common the morning after a Windows update or a BIOS change, and it's scary because the laptop looks completely dead.

Don't panic — your files are almost certainly still on the disk. The problem is the handoff between the BIOS, the storage driver, and Windows, and it can be repaired from the recovery environment in most cases.

## Why this happens

- **BIOS storage mode changed.** Switching between AHCI, RAID, and IDE modes makes the installed storage driver unable to talk to the drive.
- **Corrupted boot configuration data (BCD).** The BCD tells Windows where to find itself; if it's damaged, boot fails midway.
- **Bad storage driver from an update.** A Windows update can install a driver that doesn't match your storage controller.
- **Failing or loose drive.** A dying SSD/HDD or a drive that worked itself loose drops out mid-boot.
- **Corrupted system files on the boot partition.** Damage to the EFI partition or boot files stops the handoff.
- **Disk encryption issues.** BitLocker or third-party encryption with a damaged key or header can block access to the drive.

## How to fix it

Work through these in order, from Fix 1 onward, and stop as soon as Windows boots again.

### Fix 1: Check the BIOS storage mode

This is the number one cause, and the fix takes two minutes if you know where to look.

1. Restart and enter the BIOS/UEFI — usually **F2**, **Del**, or **F12** during the logo screen.
2. Find the storage or SATA configuration section (often under **Advanced** or **Main**).
3. Note the current mode: **AHCI**, **RAID** (sometimes called Intel RST Premium), or **IDE**.
4. If you or an update recently changed it, switch it back to what it was — most modern laptops should be on **AHCI** or **RAID** depending on factory setup.
5. Save and exit. If Windows boots, you're done — don't touch it again.

### Fix 2: Run Startup Repair from the recovery environment

Windows can often repair its own boot files if you give it the chance. Our [startup repair guide](/articles/how-to-use-startup-repair-windows-11-on-laptop/) has the full details.

1. If Windows won't start, power the laptop off and on three times in a row to trigger Automatic Repair.
2. On the recovery screen, go to **Troubleshoot > Advanced options > Startup Repair**.
3. Select your Windows installation and your administrator account.
4. Let it run — it takes 5 to 15 minutes and may restart the laptop.
5. If it reports it couldn't repair, continue to Fix 3 for the manual approach.

### Fix 3: Rebuild the boot configuration data manually

When Startup Repair can't fix the BCD, rebuilding it by hand usually can.

1. From the recovery screen, go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run these commands one at a time, pressing Enter after each:
   `bootrec /fixmbr`
   `bootrec /fixboot`
   `bootrec /rebuildbcd`
3. If `fixboot` returns "Access is denied," run these instead:
   `diskpart`, then `list vol`, identify the EFI partition, `sel vol 2` (use its number), `assign letter=Z:`, `exit`, then `bcdboot C:\Windows /s Z: /f UEFI`.
4. Type `exit` and choose **Continue** to restart.
5. If Windows boots, immediately create a restore point — you'll thank yourself later.

### Fix 4: Uninstall the latest update from recovery

If the error appeared right after an update, remove that update before doing anything drastic.

1. Go to **Troubleshoot > Advanced options > Uninstall Updates**.
2. Choose **Uninstall latest quality update** first.
3. Restart and test. If it still fails, go back and choose **Uninstall latest feature update**.
4. Once booted, pause updates for two weeks in **Settings > Windows Update** to prevent immediate reinstallation.
5. Report the problem via the Feedback Hub so Microsoft sees it — these driver mismatches get fixed when they're reported.

### Fix 5: Run CHKDSK and SFC from the recovery command prompt

Disk corruption on the system partition can cause this exact error.

1. Open **Command Prompt** from **Troubleshoot > Advanced options**.
2. First find your Windows drive letter — in recovery it may not be C:. Run `diskpart`, `list vol`, `exit` to check.
3. Run `chkdsk C: /f /r` (replace C: with the correct letter) and let it complete.
4. Then run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` with the correct letter.
5. Restart with **Continue** and see if Windows loads.

### Fix 6: Load the correct storage driver at boot

Sometimes the installed driver is wrong for the current BIOS mode, and you need to inject the right one.

1. On another PC, download the Intel RST or AMD RAID driver for your laptop model and extract it to a USB stick.
2. Boot your laptop to **Troubleshoot > Advanced options > Command Prompt**.
3. Use `drvload E:\path\to\driver.inf` (adjust the path) to load the driver.
4. Alternatively, boot into [Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) with networking and install the proper storage driver from Device Manager.
5. Once booted normally, install the full chipset and storage driver package so it survives future updates.

### Fix 7: Reseat or test the drive

If software repairs all fail, suspect the hardware — especially on laptops that travel a lot.

1. Power off completely and unplug the charger.
2. If your laptop has an accessible drive bay or bottom panel, open it and reseat the SSD or hard drive firmly in its slot.
3. Boot into the BIOS and check whether the drive appears in the storage list.
4. If it appears intermittently or not at all, the drive is failing — replace it.
5. If you need the data, connect the old drive to another PC with a USB-to-SATA/NVMe adapter before it dies completely.

### Fix 8: Reset Windows from the recovery environment

When the boot structure is too damaged to repair, a reset gives you a working system again.

1. Go to **Troubleshoot > Reset this PC**.
2. Choose **Keep my files** first — it reinstalls Windows while preserving your personal data.
3. If that fails, choose **Remove everything** for a fully clean slate (only after you've exhausted data recovery).
4. Prefer **Cloud download** if you have internet in recovery — it fetches an undamaged copy of Windows.
5. After the reset, install storage and chipset drivers from your laptop maker's site before running Windows Update.

## Closing

INACCESSIBLE_BOOT_DEVICE is almost never as bad as it looks. Check the BIOS storage mode first — that alone fixes a huge share of cases — then work through boot repair and update removal. Your files are usually safe throughout. For general boot-repair technique, keep the [startup repair walkthrough](/articles/how-to-use-startup-repair-windows-11-on-laptop/) handy, and Microsoft's [official recovery documentation](https://support.microsoft.com/en-us/windows) covers the advanced command-line options.
