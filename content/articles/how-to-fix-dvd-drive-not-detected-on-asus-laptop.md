---
title: "DVD Drive Not Detected on ASUS Laptop? Fix It Here"
slug: how-to-fix-dvd-drive-not-detected-on-asus-laptop
date: 2026-09-26
categories: ["drivers"]
tags: ["dvd drive", "asus", "optical drive", "device manager", "troubleshooting"]
description: "ASUS laptop not detecting the DVD drive? Fix the missing optical drive with registry, driver, and BIOS steps specific to ASUS laptops."
thumbnail: "/images/thumbs/how-to-fix-dvd-drive-not-detected-on-asus-laptop.webp"
faqs:
  - q: "Why did my DVD drive disappear from File Explorer on my ASUS laptop?"
    a: "The drive usually disappears because Windows stopped loading its driver — often after a Windows update, a filter driver conflict from burning software, or a registry corruption in the CD-ROM class keys. The hardware is typically fine; the drive just needs its driver binding restored through Device Manager or a registry fix."
  - q: "Is the DVD drive failure a hardware problem on ASUS laptops?"
    a: "Rarely at first. If the drive tray still opens and the BIOS sees the drive, it's a Windows driver issue, not dead hardware. Suspect hardware only if the tray won't eject, the drive makes grinding noises, or it's missing from BIOS too — those point at the drive or its cable."
  - q: "Can third-party burning software hide my DVD drive?"
    a: "Yes. Disc burning and virtual-drive software installs filter drivers that hook into the optical drive stack. When those filters corrupt or conflict — especially after Windows updates — the real drive vanishes from Explorer. Removing the UpperFilters and LowerFilters registry values is the classic fix."
  - q: "Does ASUS have a specific driver for the DVD drive?"
    a: "Usually not — Windows' built-in cdrom.sys handles optical drives, and ASUS doesn't ship a separate DVD driver. The relevant ASUS-side pieces are the chipset driver and BIOS. If Windows' driver stack is the problem, the fix is in Device Manager and the registry, not an ASUS download."
---

Optical drives are fading from laptops, but plenty of ASUS machines still have them — and when the DVD drive vanishes from File Explorer, it's disorienting. The tray opens, the disc spins, but Windows acts like the drive doesn't exist. Before you assume the drive died, know this: on ASUS laptops, a missing DVD drive is a software problem far more often than a hardware one.

Windows talks to optical drives through a driver stack involving filter drivers from burning software, and that stack is fragile. Windows updates, iTunes, Daemon Tools, and old Nero installs can all knock it over. The fixes below go from the quick checks to the famous registry repair, in order.

## Why this happens

- **Corrupt filter drivers:** UpperFilters/LowerFilters registry values break the drive stack.
- **Windows update regression:** an update damaged the cdrom driver binding.
- **Burning software conflicts:** virtual drive tools hook the optical stack and fail.
- **Drive disabled in Device Manager:** accidentally or by a tuning utility.
- **BIOS/UEFI setting:** the SATA port for the optical bay got disabled.
- **Loose drive connection:** the slimline SATA connector works loose over time.
- **ATAPI driver corruption:** the underlying storage driver fails to enumerate the drive.
- **Drive letter conflict:** Windows lost the drive's letter assignment.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check BIOS and the physical drive

1. Restart the ASUS laptop and press **F2** (or Del) to enter BIOS.
2. Look for the DVD/optical drive in the SATA device list. If BIOS sees it, the hardware and cable are fine.
3. If BIOS doesn't list it, reseat the drive: power off, remove the battery if possible, and firmly push the drive back into its bay.
4. Test the eject button — a tray that won't open at all suggests power or hardware failure.
5. Only proceed with Windows fixes if BIOS detects the drive; otherwise you're chasing software for a hardware problem.

### Fix 2: Reveal and re-enable in Device Manager

1. Open Device Manager (**Win + X > Device Manager**) and click **View > Show hidden devices** — the drive may be hiding as a grayed entry.
2. Expand **DVD/CD-ROM drives**. If the drive appears with a down arrow, right-click and choose **Enable device**.
3. If it has a yellow warning, right-click and choose **Uninstall device**, then click **Action > Scan for hardware changes**.
4. Check the **Device status** on the Properties > General tab for error codes guiding the next step.
5. A related device-visibility walkthrough is [showing hidden devices in Device Manager](/articles/how-can-i-enable-hidden-devices-in-device-manager/) if the drive won't appear at all.

### Fix 3: Delete the UpperFilters and LowerFilters values

1. This is the classic, most effective fix. Press **Win + R**, type `regedit`, and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e965-e325-11ce-bfc1-08002be10318}`.
2. In the right pane, look for **UpperFilters** and **LowerFilters** values.
3. Right-click each and delete them. (Export the key first via File > Export as a backup — takes ten seconds.)
4. Close Registry Editor and restart the laptop.
5. Windows rebuilds the filter stack cleanly, and the DVD drive typically reappears in File Explorer.
6. If the values return after installing burning software, that software is the conflict source — update or replace it.

### Fix 4: Reinstall the ATAPI/IDE controller driver

1. In Device Manager, expand **IDE ATA/ATAPI controllers**.
2. Right-click each channel/controller and choose **Uninstall device** (don't check driver deletion).
3. Restart — Windows redetects the storage controllers and re-enumerates attached drives including the DVD.
4. This fixes cases where the controller itself stopped reporting the optical drive.
5. Also update the ASUS chipset driver from ASUS support if you haven't — the SATA controller depends on it.

### Fix 5: Check ASUS BIOS settings for the optical bay

1. Enter BIOS (F2) and look under **Advanced > SATA Configuration**.
2. Ensure the SATA port for the optical drive is **Enabled** — some BIOS updates reset port settings.
3. Check for any "ODD" (optical disc drive) specific options and enable them.
4. While there, confirm the SATA mode is **AHCI** (not IDE/RAID changes you didn't make).
5. Save and exit, then check File Explorer. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) covers general hardware detection if the drive still hides.

### Fix 6: Assign or restore the drive letter

1. Press **Win + X** and choose **Disk Management**.
2. Look for the CD-ROM entry — it may be present but letterless.
3. Right-click it and choose **Change Drive Letter and Paths**, then assign a free letter like E:.
4. If the drive doesn't appear in Disk Management either, the problem is lower in the stack — return to Fix 3.
5. Letter conflicts happen when USB drives or network mappings grab the optical drive's old letter.

### Fix 7: Test in a clean boot and consider hardware

1. Perform a clean boot (**msconfig** > Services > Hide Microsoft services > Disable all) to rule out third-party filter software.
2. If the drive appears in clean boot, re-enable services in halves to find the conflicting program — usually disc-burning or virtual-drive software.
3. Uninstall the offending software properly (not just disable) since its filters persist.
4. If nothing brings the drive back and BIOS sees it fine, try a Linux live USB — drive visible there means Windows is definitely the problem.
5. The same logic applies across brands; compare with [DVD drive not detected on Acer laptops](/articles/how-to-fix-dvd-drive-not-detected-on-acer-laptop/) for the parallel walkthrough.

## Closing

A missing DVD drive on an ASUS laptop is one of the most fixable problems in this whole category — the registry filter fix alone resolves a huge share of cases, and it takes five minutes including the backup. The important discipline is checking BIOS first so you don't waste an hour on registry edits for a drive that isn't electrically connected. Work the stack from hardware up: BIOS detection, Device Manager, filters, controllers, drive letters. The drive was working before; something in that stack changed, and these steps find it.
