---
title: "How to Fix UNEXPECTED_STORE_EXCEPTION on an HP Laptop"
slug: how-to-fix-unexpected-store-exception-on-hp-laptop
date: 2026-09-21
categories: ["windows-errors"]
tags: ["bsod", "storage", "hp"]
description: "UNEXPECTED_STORE_EXCEPTION blue screen on your HP laptop? The memory store manager hit a fault. Here's the fix."
thumbnail: "/images/thumbs/how-to-fix-unexpected-store-exception-on-hp-laptop.webp"
faqs:
  - q: "What does UNEXPECTED_STORE_EXCEPTION mean?"
    a: "The kernel's memory store manager (which handles the pagefile and memory compression store) hit an unexpected exception — usually because the underlying storage faulted (stop code 0x154). It's most often a failing SSD/HDD, bad storage driver, or corrupt pagefile."
  - q: "Is my hard drive dying?"
    a: "Possibly — this stop code is strongly associated with storage faults. Check SMART health immediately with CrystalDiskInfo or HP's diagnostics. But don't panic yet: corrupt pagefiles and bad storage drivers cause the identical crash with a healthy drive."
  - q: "Why does it happen when the laptop wakes from sleep?"
    a: "The store manager is heavily involved in hibernation and sleep resume — it pages memory contents back from the hiberfile/pagefile. If the drive is slow to spin up or the storage driver mishandles resume, the store operation faults."
  - q: "Will I lose data?"
    a: "The crash itself doesn't delete files, but a failing drive behind it absolutely can. Back up your important data before troubleshooting further — this is the stop code where backup urgency is highest."
---

`UNEXPECTED_STORE_EXCEPTION` (stop code 0x154) comes from Windows' store manager — the component managing the pagefile-backed memory store and memory compression. When it hits an exception it didn't expect, it almost always means the storage underneath it misbehaved: the drive faulted, the driver glitched, or the pagefile is corrupt.

On HP laptops, this often shows up alongside HP's storage driver configurations and after Windows updates that replace them. The diagnostic order matters here: check the drive first (because a dying drive is urgent), then drivers and the pagefile.

## Why this happens

- **Failing SSD or hard drive**: The top cause — the drive faults during store operations.
- **Outdated or corrupt storage driver**: AHCI/NVMe controller drivers mishandling I/O.
- **Corrupt pagefile or hibernation file**: Damaged pagefile.sys or hiberfil.sys.
- **Antivirus filter drivers**: Kernel filters interfering with store I/O.
- **Failing RAM**: Bad memory corrupting store data before it's written.
- **Windows update storage driver swap**: Update-installed generic storage driver replacing HP's tuned one.

## How to fix it

Work through these in order — drive health first, because it's urgent.

### Fix 1: Back up your data immediately

Do this before anything else — if the drive is failing, every hour counts.

1. Boot into Windows (or Safe Mode if normal boot crashes).
2. Copy critical files to an external drive or cloud storage now — Documents, photos, work files first.
3. If Windows won't stay up long enough, boot from Windows installation media > **Repair your computer** > **Command Prompt** and use `robocopy C:\Users\YourName E:\Backup /E`.
4. Don't run intensive disk scans before backing up — a dying drive can fail completely under scan load. Backup first, diagnostics second.
5. Once backed up, proceed without fear — the remaining fixes are non-destructive.

### Fix 2: Check drive health with HP diagnostics

HP provides built-in diagnostics — use them.

1. Power off, then power on and immediately press **F2** (or **Esc** > **F2**) to enter **HP PC Hardware Diagnostics**.
2. Run the **Storage** / hard drive tests — both the quick and extensive tests.
3. Alternatively in Windows, install CrystalDiskInfo (free) and check **Health Status** — anything but "Good" means replace the drive.
4. You can also download HP's diagnostic tools from [HP support](https://support.hp.com/us-en).
5. If diagnostics fail, replace the drive — no software fix will hold. If they pass, continue: the cause is software.

### Fix 3: Update the storage controller driver

HP-tuned storage drivers matter — get the right one.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Expand **IDE ATA/ATAPI controllers** and **Storage controllers**.
3. Right-click each > **Update driver** > **Search automatically for drivers**.
4. Then install HP's official chipset/storage driver from [HP support](https://support.hp.com/us-en) for your exact model — this is the important step, since Windows Update's generic driver is a common trigger.
5. For Intel-based HP laptops, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) catches storage driver updates too.
6. Restart and test, especially sleep/wake cycles.
7. If the crashes began right after a Windows update, roll the storage driver back instead of updating forward: **Device Manager** > right-click the controller > **Properties** > **Driver** tab > **Roll Back Driver**. Then block the bad version with Microsoft's **Show or hide updates** troubleshooter so the update doesn't reinstall it overnight.

### Fix 4: Rebuild the pagefile and hibernation file

Corrupt store backing files cause this exact crash with a healthy drive.

1. Press **Win + R**, type `sysdm.cpl` > **Advanced** tab > **Performance Settings** > **Advanced** tab > **Virtual memory Change**.
2. Uncheck **Automatically manage**, set **No paging file**, **Set**, restart.
3. Re-enable **Automatically manage paging file size for all drives**, **Set**, restart.
4. Rebuild hibernation: elevated Command Prompt > `powercfg /hibernate off`, restart, `powercfg /hibernate on`.
5. Test sleep, hibernate, and wake cycles specifically — these exercise the store manager hardest.

### Fix 5: Run chkdsk and system file repairs

Fix file-system and system-file damage contributing to store faults.

1. Elevated Command Prompt: `chkdsk C: /f /r` — schedule and reboot for the full scan.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow`.
3. If chkdsk finds bad sectors in the pagefile region, the Fix 4 rebuild already relocated it — but recurring bad sectors mean the drive is degrading (back to Fix 2).
4. Microsoft documents these repair tools on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Remove antivirus filter interference

Filter drivers sit in the store I/O path and can fault it.

1. Temporarily uninstall third-party antivirus (disabling isn't enough — the filter driver stays loaded).
2. Restart and test for a day or two with Windows Defender active.
3. If crashes stop, the AV filter was the cause — reinstall only a version explicitly supporting your Windows build.
4. Also check for other filter drivers: disk encryption, backup tools with volume filters — uninstall or update them.

### Fix 7: Test RAM and update BIOS

The remaining hardware and firmware suspects.

1. Run `mdsched.exe` (**Win + R**) > **Restart now and check for problems**. Bad RAM corrupts store data.
2. Update the BIOS from [HP support](https://support.hp.com/us-en) — storage controller firmware fixes are common in HP BIOS changelogs.
3. If RAM fails and is removable, replace the stick; if soldered, professional service.
4. Related store-adjacent crashes: [PAGE_FAULT_IN_NONPAGED_AREA](/articles/how-to-fix-page-fault-in-nonpaged-area-step-by-step/) and our [HP-specific blue screen after update guide](/articles/how-to-fix-blue-screen-after-windows-11-update-on-hp-laptop/).

## Closing

UNEXPECTED_STORE_EXCEPTION on an HP laptop is the store manager telling you its storage faulted — so back up first, check the drive with HP's diagnostics, update HP's storage drivers, and rebuild the pagefile. Most cases end at a bad driver or corrupt pagefile, but the ones that end at a failing drive are why the backup comes first. Either way, the order above keeps your data safe while you find out which it is.
