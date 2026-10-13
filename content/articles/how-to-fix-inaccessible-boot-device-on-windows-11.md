---
title: "How to Fix INACCESSIBLE_BOOT_DEVICE on Windows 11"
slug: how-to-fix-inaccessible-boot-device-on-windows-11
date: 2026-09-24
categories: ["windows-errors"]
tags: ["blue screen", "windows 11", "boot issues"]
description: "INACCESSIBLE_BOOT_DEVICE blue screen blocking Windows 11 from starting? Fix the storage driver or boot configuration with these steps."
thumbnail: "/images/thumbs/how-to-fix-inaccessible-boot-device-on-windows-11.webp"
faqs:
  - q: "What does INACCESSIBLE_BOOT_DEVICE mean?"
    a: "Windows started to boot but lost access to the system drive partway through. The usual cause is a storage driver problem: Windows loaded the wrong driver, or an update replaced the working one. Boot configuration damage and failing SSDs are the other common causes."
  - q: "Why did this happen right after a Windows 11 update?"
    a: "Updates sometimes install a new storage controller driver that does not match your hardware, or they change the disk mode the BIOS expects. The system booted fine with the old driver and cannot reach the disk with the new one."
  - q: "Will I lose my files?"
    a: "Usually not. The error means Windows cannot reach the drive, not that the data is gone. In most cases the files are intact and become accessible again once the driver or boot configuration is fixed."
  - q: "Can a BIOS setting cause this blue screen?"
    a: "Yes. If the SATA mode was changed between AHCI and RAID, or from legacy to UEFI boot, Windows looks for the drive using the wrong method. Restoring the original setting often fixes it instantly."
---

INACCESSIBLE_BOOT_DEVICE is the blue screen that appears when Windows 11 begins to start and then realizes it cannot talk to the drive it is booting from. The laptop may loop on this screen forever, never reaching the desktop. It is alarming, but the data on the drive is usually fine; Windows has simply lost the instructions for reaching it.

The most common story is a storage driver that changed: a Windows update installed the wrong one, or a BIOS setting flipped the disk mode. The fixes below start in the recovery environment, since Windows will not boot, and walk you from the simplest driver fixes to boot configuration repair.

## Why this happens

- **Wrong storage driver after an update.** Windows Update replaced the working AHCI or RAID driver with an incompatible one.
- **Changed BIOS disk mode.** Switching between AHCI and RAID, or between UEFI and legacy boot, breaks the driver's expectations.
- **Corrupted boot configuration data.** The BCD store that tells Windows where the system drive is gets damaged.
- **Failing SSD.** A drive that drops offline intermittently produces exactly this error.
- **Disk corruption.** Filesystem damage on the boot partition blocks access during startup.
- **Recent hardware change.** Adding or removing a drive can reorder disks so the boot entry points at the wrong one.
- **BitLocker complications.** Encryption driver issues after updates can block access to an encrypted system drive.

## How to fix it

Work through these in order, starting with the quickest fixes first.

### Fix 1: Reach the recovery environment

You need the recovery tools since Windows will not start.

1. Power the laptop on and force it off by holding the **power button** during the Windows logo. Repeat three times.
2. On the fourth boot, Windows should open the **Choose an option** screen automatically.
3. Select **Troubleshoot** > **Advanced options**. This is your base camp for every fix below.
4. If the recovery environment never appears, boot from a Windows 11 installation USB and choose **Repair your computer** instead. You can create one on another PC from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

### Fix 2: Check the BIOS disk mode

A flipped setting is the fastest fix when it applies.

1. From **Advanced options**, choose **UEFI Firmware Settings** and restart into the BIOS.
2. Find the storage or SATA configuration section. Note whether it says **AHCI** or **RAID**/**Intel RST**.
3. If you recently changed this, or a BIOS update reset it, set it back to what it was when Windows worked. For most laptops that is **AHCI**.
4. Also confirm the boot mode is **UEFI**, not Legacy, if that is how Windows was installed.
5. Save with **F10** and exit. If Windows boots, you are done.

### Fix 3: Boot into Safe Mode to bypass the bad driver

1. In **Advanced options**, go to **Startup Settings** and click **Restart**.
2. Press **4** for Safe Mode. Safe Mode uses a minimal storage driver set and often boots where normal mode cannot.
3. If Safe Mode works, open **Device Manager**, expand **Storage controllers** and **IDE ATA/ATAPI controllers**, and roll back or update the storage driver.
4. Restart normally.

### Fix 4: Run Startup Repair

1. In **Advanced options**, choose **Startup Repair**.
2. Select your Windows installation and let it run. It automatically fixes common boot configuration problems.
3. If it reports it could not repair, continue to the manual BCD rebuild below. Startup Repair fixes the easy cases; the manual steps handle the rest.

### Fix 5: Rebuild the boot configuration data

1. In **Advanced options**, open **Command Prompt**.
2. Run these commands one at a time: `bootrec /fixmbr`, then `bootrec /fixboot`. If fixboot reports access denied, continue anyway.
3. Run `bootrec /scanos` to find Windows installations, then `bootrec /rebuildbcd` to rebuild the boot store. Type **Y** when asked to add each installation found.
4. For UEFI systems, you may need the longer sequence: `diskpart`, then `list vol`, identify the EFI partition, assign it a letter with `assign letter=Z:`, exit diskpart, then run `bcdboot C:\Windows /s Z: /f UEFI`. Adjust the drive letters to match what diskpart showed.
5. Close the prompt and choose **Continue** to restart.

### Fix 6: Run disk checks from the recovery prompt

1. Open **Command Prompt** from **Advanced options** again.
2. Run `chkdsk C: /f /r`. The drive letter may differ in recovery; use `diskpart` then `list vol` to confirm which letter holds Windows.
3. Let the scan complete. It can take a long time on large drives, but bad sectors on the boot partition are a real cause of this error.
4. Restart and test.

### Fix 7: Restore the storage driver from a restore point

1. In **Advanced options**, choose **System Restore**.
2. Pick a restore point from before the problem started.
3. Let it complete. System Restore reverts drivers and system files without touching your personal files, which makes it ideal for update-caused boot failures.
4. If no restore points exist, enable System Protection once you are back in Windows so you have this safety net next time.

### Fix 8: Test the SSD and reinstall as a last resort

1. From the recovery command prompt, run `wmic diskdrive get status`. Anything other than **OK** means the drive is failing.
2. If the drive is healthy but nothing else worked, back up your files using the command prompt or a live USB, then reinstall Windows from the installation media.
3. If the drive is failing, replace it. No software fix can keep a dying SSD reachable.
4. Related boot failures: [inaccessible boot device after a Windows 11 update](/articles/how-to-fix-inaccessible-boot-device-after-windows-11-update/) and the [Srttrail.txt blue screen guide](/articles/how-to-fix-srttrail-txt-blue-screen-error-after-windows-11-update/). Microsoft's recovery documentation is on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

INACCESSIBLE_BOOT_DEVICE looks catastrophic because Windows will not start, but it is usually a driver or configuration problem with your files sitting safely on the other side. Check the BIOS disk mode first, since that is a thirty-second fix when it applies, then work through Startup Repair and the BCD rebuild. Keep System Protection enabled going forward, and a bad storage driver update becomes a five-minute rollback instead of a boot crisis.
