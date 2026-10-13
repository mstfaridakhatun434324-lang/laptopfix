---
title: "How to Fix PFN_LIST_CORRUPT After a Windows 11 Update"
slug: how-to-fix-pfn-list-corrupt-after-windows-11-update
date: 2026-09-15
categories: ["windows-errors"]
tags: ["bsod", "memory", "windows update"]
description: "PFN_LIST_CORRUPT blue screen after a Windows 11 update? The page frame database is damaged. Here's how to fix it."
thumbnail: "/images/thumbs/how-to-fix-pfn-list-corrupt-after-windows-11-update.webp"
faqs:
  - q: "What does PFN_LIST_CORRUPT mean?"
    a: "The Page Frame Number list — Windows' database tracking every physical memory page — is corrupted (stop code 0x4E). Causes include bad RAM, drivers corrupting the list, a corrupt pagefile, or a Windows update that damaged memory-management components."
  - q: "Why did this start right after a Windows update?"
    a: "The update likely installed an incompatible storage or memory-related driver, or partially corrupted system files. Updates also change memory manager behavior, exposing driver bugs that were previously harmless. Rolling back the update or its drivers is the logical first step."
  - q: "Is PFN_LIST_CORRUPT always bad RAM?"
    a: "No — despite the memory-sounding name, drivers are a very common cause. The PFN list lives in kernel memory, and any driver writing out of bounds can corrupt it. Test RAM, but investigate drivers with equal seriousness."
  - q: "Can this error damage my files?"
    a: "The crash itself doesn't delete files, but the underlying cause might: a failing drive corrupting the pagefile, or repeated crashes interrupting writes. Back up important data before extensive troubleshooting."
---

`PFN_LIST_CORRUPT` (stop code 0x4E) means Windows' Page Frame Number database — the master ledger of every physical RAM page, who owns it, and what state it's in — has been corrupted. Without a trustworthy ledger, the memory manager can't function, so Windows stops.

When this appears right after a Windows 11 update, the timeline is your best diagnostic clue: something the update changed — a driver, a system file, a memory-management behavior — is corrupting the list. The fixes below start with undoing the update's damage, then cover the hardware suspects.

## Why this happens

- **Incompatible driver from the update**: Storage, chipset, or filter drivers that corrupt the PFN list under the new build.
- **Bad RAM**: Failing memory corrupts the PFN database directly — a top cause regardless of updates.
- **Corrupt pagefile**: A damaged pagefile.sys feeds corrupt data back into PFN-tracked pages.
- **Failing storage drive**: Bad sectors corrupting the pagefile or hibernation file.
- **Overclocked/XMP memory**: Unstable memory timings corrupt PFN entries under load.
- **Corrupted system files**: Update-damaged memory manager components.

## How to fix it

Work through these in order — update rollback first, then hardware.

### Fix 1: Uninstall the recent update

If the crashes started with the update, remove it.

1. Open **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Remove the most recent update matching the crash timeline. Restart and test for a day.
3. Can't boot? Use recovery: Automatic Repair > **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
4. Pause updates for 2-3 weeks afterward (**Settings** > **Windows Update** > **Pause updates**).
5. Our [blue screen after Windows 11 update guide](/articles/blue-screen-after-windows-11-update-troubleshooting/) covers the full rollback workflow including driver-level rollbacks.

### Fix 2: Roll back storage and chipset drivers

The update's bundled drivers are prime suspects for PFN corruption.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Under **IDE ATA/ATAPI controllers**, **Storage controllers**, and **System devices**, right-click each > **Properties** > **Driver** tab > **Roll Back Driver** where available.
3. If roll-back is greyed out, uninstall the device (check **Delete the driver software**), restart, and install the manufacturer's version from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
4. Use Microsoft's **Show or hide updates** troubleshooter to block the bad driver version.
5. For Intel platforms, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) provides validated chipset drivers.

### Fix 3: Test your RAM

PFN corruption is a classic bad-RAM symptom — test regardless of the update timeline.

1. Press **Win + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. Any error = bad RAM. Confirm borderline cases with MemTest86 overnight (4+ passes from a bootable USB).
3. Reseat modules if accessible; test sticks individually.
4. Reset XMP/DOCP to stock speeds in BIOS — unstable memory overclocks corrupt PFN entries exactly like failing RAM does.
5. Full memory-testing methodology: our [MEMORY_MANAGEMENT stop code guide](/articles/how-to-fix-stop-code-memory-management-step-by-step/).

### Fix 4: Rebuild the pagefile

A corrupt pagefile is a software cause that perfectly mimics hardware.

1. Press **Win + R**, type `sysdm.cpl` > **Advanced** tab > **Performance Settings** > **Advanced** tab > **Virtual memory Change**.
2. Uncheck **Automatically manage**, set **No paging file**, click **Set**, restart.
3. Re-enable **Automatically manage paging file size for all drives**, click **Set**, restart again.
4. Also rebuild hibernation data: elevated Command Prompt > `powercfg /hibernate off`, restart, `powercfg /hibernate on`.
5. If crashes stop, disk errors likely corrupted the old pagefile — run Fix 5 to check the drive.

### Fix 5: Check drive health and repair system files

The update may have landed on — or revealed — a failing drive.

1. Elevated Command Prompt: `chkdsk C: /f /r` (schedule and reboot for the full surface scan).
2. Check SMART data with CrystalDiskInfo — replace the drive on anything but "Good."
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` to repair update-damaged system files.
4. If the drive is failing, back up immediately with `robocopy C:\Users\YourName E:\Backup /E` and replace the drive — no software fix holds on dying storage.

### Fix 6: Run Driver Verifier to catch the corrupting driver

If RAM and drive test clean, a driver is corrupting the PFN list.

1. Press **Win + R**, type `verifier` > **Create standard settings** > **Automatically select unsigned drivers** > **Finish**. Restart.
2. Use the laptop normally until it crashes — Verifier's dump names the driver.
3. Boot to Safe Mode, run `verifier`, **Delete existing settings**, then update or remove the named driver.
4. Temporarily uninstall third-party antivirus first — its filter drivers are frequent PFN corruptors.
5. Related Verifier workflow: our [DRIVER_VERIFIER_IOMANAGER_VIOLATION guide](/articles/best-way-to-fix-driver-verifier-iomanager-violation/).

### Fix 7: Update BIOS and consider an in-place upgrade

Finish with firmware and a system refresh.

1. Update BIOS from the manufacturer's support site — memory-controller fixes in firmware changelogs directly address PFN corruption.
2. If crashes persist after all of the above, run an in-place upgrade from [Windows 11 installation media](https://www.microsoft.com/en-us/software-download/windows11) (keep files and apps) to replace every system component the update may have damaged.
3. After the upgrade, install chipset and storage drivers from the manufacturer before running Windows Update.
4. If MemTest86 definitively failed and RAM is soldered, professional board repair is the remaining path — get a quote and check warranty status.
5. One more check worth doing: disable **Memory Integrity** temporarily (**Windows Security** > **Device security** > **Core isolation**) and test. On some 24H2 systems, HVCI interacts badly with older storage drivers in ways that present as PFN corruption — if disabling it stops the crashes, you've narrowed it to a driver/HVCI conflict rather than hardware.

## Closing

PFN_LIST_CORRUPT after a Windows update sits at the intersection of software and hardware: the update's drivers are the first suspects, but bad RAM corrupts the same database. Roll back the update and its drivers, test memory properly with MemTest86, rebuild the pagefile, and let Driver Verifier name any driver still corrupting the list. The timeline tells you where to start; the tests tell you where to finish.
