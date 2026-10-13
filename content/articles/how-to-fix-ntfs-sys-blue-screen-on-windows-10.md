---
title: "How to Fix the Ntfs.sys Blue Screen on Windows 10"
slug: how-to-fix-ntfs-sys-blue-screen-on-windows-10
date: 2026-09-09
categories: ["windows-errors"]
tags: ["ntfs.sys", "blue screen", "disk error", "file system", "windows 10"]
description: "Ntfs.sys blue screen on Windows 10 means file system trouble. Run chkdsk, test the drive, update storage drivers, and fix it properly."
thumbnail: "/images/thumbs/how-to-fix-ntfs-sys-blue-screen-on-windows-10.webp"
faqs:
  - q: "What does an Ntfs.sys blue screen mean?"
    a: "The NTFS file system driver crashed while reading or writing to your drive. That points to disk errors, bad sectors, a failing drive, corrupted file system structures, or a buggy storage driver — not to Ntfs.sys itself being broken."
  - q: "Is Ntfs.sys crash a sign my hard drive is dying?"
    a: "It can be, but don't assume it. Run chkdsk /r and check the drive's SMART health first. If the drive is healthy, the cause is usually file system corruption or a storage driver issue — both fixable in software."
  - q: "Will chkdsk delete my files?"
    a: "Chkdsk repairs file system structures; it doesn't delete your personal files. In rare cases it may move corrupted file fragments to found.000 folders, but your documents, photos, and apps are preserved."
  - q: "Why does it happen after a Windows 10 update?"
    a: "Updates can install a new storage controller driver that conflicts with your hardware, or the update process itself can hit existing disk errors and leave the file system inconsistent. Rolling back the storage driver or running chkdsk usually resolves it."
---

When the blue screen names **Ntfs.sys**, beginners assume that file is broken. It isn't — Ntfs.sys is the driver Windows uses to talk to NTFS-formatted drives, and it's crashing because something *underneath* it went wrong: the disk, the file system structures on it, or the storage driver feeding it bad data.

So the fix isn't "repair Ntfs.sys" — it's investigating the storage stack from the disk up. On Windows 10, this error most commonly traces to disk errors or a storage driver mismatch, both very fixable. (On Windows 11, see our [Ntfs.sys Windows 11 guide](/articles/how-to-fix-ntfs-sys-blue-screen-in-windows-11-24h2/).)

Before running anything, back up your most important files if you can still boot — Ntfs.sys crashes sometimes precede drive failure, and a backup takes minutes while data recovery takes days. Then work the storage stack from the bottom up: physical disk health, file system integrity, the driver layer, and finally memory, since bad RAM can corrupt file system data in transit.

## Why this happens

- **Disk errors / bad sectors:** The top cause — physical defects or logical corruption where NTFS structures live.
- **Failing drive:** An SSD or HDD developing faults that corrupt reads.
- **Buggy storage controller driver:** Especially after Windows Update replaces a working driver.
- **Corrupted file system:** From power losses, forced shutdowns, or interrupted updates.
- **Bad RAM corrupting cached writes:** Faulty memory corrupting file system data in transit.
- **Loose drive connection:** On laptops with 2.5" SATA drives, a loose connector causes intermittent I/O errors that crash Ntfs.sys.
- **Third-party disk tools:** Defragmenters, "SSD optimizers," and encryption drivers that hook the file system can destabilize it.
- **Overheating drive:** NVMe SSDs that overheat can produce transient read errors.

## How to fix it

Work through these in order.

### Fix 1: Run chkdsk with surface scan

This is the single most effective fix for Ntfs.sys crashes. The `/r` flag locates bad sectors and recovers readable information while fixing logical file system errors — it's the closest thing to a one-shot repair for this stop code.

1. Open **Command Prompt (Admin)** — right-click **Start**, choose **Windows Terminal (Admin)** or **Command Prompt (Admin)**.
2. Type `chkdsk C: /r` and press Enter. If prompted to schedule at restart, type **Y** and reboot.
3. Let the full scan complete — all 5 stages. On large drives this takes a while; don't interrupt it.
4. When Windows boots, check the results in **Event Viewer > Windows Logs > Application**, filtering for **Wininit** as the source.
5. If chkdsk repaired errors, use the PC normally and watch for recurrences. Microsoft's [disk error checking guide](https://support.microsoft.com/en-us/windows) explains what chkdsk's stages mean.

### Fix 2: Check the drive's SMART health

Chkdsk fixes logical damage; SMART tells you about physical health. Run both — they answer different questions, and you need both answers before deciding whether this is a software repair or a drive replacement.

1. Open an admin terminal and run `wmic diskdrive get status` — you want "OK" for each drive.
2. For detail, install **CrystalDiskInfo** (free) and check the health status and reallocated/pending sector counts.
3. Better yet, run your manufacturer's boot diagnostics (Dell **F12** > Diagnostics, HP **Esc** > **F2**, Lenovo **F10**).
4. If SMART shows warnings or growing bad sectors, back up immediately and replace the drive — software can't fix dying hardware.

### Fix 3: Update or roll back the storage driver

The driver layer between Windows and the disk.

1. Open **Device Manager**, expand **Storage controllers** and **IDE ATA/ATAPI controllers**.
2. If crashes started after an update: right-click the controller > **Properties > Driver > Roll Back Driver**.
3. Otherwise, download the latest storage/chipset driver from your laptop maker's support site and install it.
4. Also check **Disk drives** in Device Manager — update those drivers too.

### Fix 4: Run SFC and DISM

File system driver crashes can cascade from corrupted Windows files.

1. In an admin terminal: `sfc /scannow`.
2. Then: `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart and test.

### Fix 5: Test the RAM

Bad memory corrupts file system data cached in RAM, producing Ntfs.sys crashes with a perfectly healthy disk. This is the sneaky cause: everything about the disk checks out, yet crashes continue, because the corruption happens in RAM before data ever reaches the drive.

1. **Win + R** > `mdsched.exe` > **Restart now and check for problems**.
2. For certainty, run **MemTest86** from USB for one full pass.
3. Replace or reseat any failing modules.

### Fix 6: Check for overheating (especially NVMe SSDs)

1. Install **HWiNFO64** or **CrystalDiskInfo** and check drive temperatures under load. NVMe drives throttling above ~70–75°C can throw errors.
2. Clean vents and fans, ensure the laptop sits on a hard surface.
3. If the SSD runs hot consistently, a thermal pad replacement (or a shop visit) helps.

### Fix 7: Disable problematic startup software and test in Safe Mode

If the disk and drivers check out, a third-party program loading at boot may be crashing the file system driver. Safe Mode strips those away for a clean test.

1. Boot into **Safe Mode** (Shift + Restart > **Troubleshoot > Advanced options > Startup Settings**).
2. If crashes stop in Safe Mode, a third-party driver or service is involved — use **msconfig** to disable non-Microsoft services in halves until you isolate it.
3. Pay special attention to disk utilities, encryption tools, and backup software with file system filter drivers.

### Fix 8: Back up and replace the drive if errors recur

If chkdsk keeps finding new errors or SMART keeps degrading:

1. Back up everything to an external drive (use **File History** or a full image with **Macrium Reflect Free**).
2. Replace the SSD/HDD — on most laptops this is a straightforward bottom-panel job; check your model's manual.
3. Reinstall Windows 10 from USB media and restore your files. A fresh drive with a fresh file system ends Ntfs.sys crashes permanently.

## Closing

Ntfs.sys crashes are the storage stack telling you something below it is wrong — work upward from the disk: chkdsk first, SMART health second, storage drivers third. That order catches the real cause in the vast majority of cases, whether it's logical corruption (fixable in an hour) or a dying drive (fixable with a replacement). Don't waste time "repairing" Ntfs.sys itself; it's the messenger, not the problem. One last note: if chkdsk found bad sectors but SMART looks fine, keep an eye on the drive for a few weeks — run CrystalDiskInfo monthly. A drive that developed bad sectors once often develops more, and the next Ntfs.sys crash might be the warning you act on before data loss. If your crashes point at the storage subsystem more broadly, see our [unexpected store exception fix](/articles/best-way-to-fix-unexpected-store-exception/).
