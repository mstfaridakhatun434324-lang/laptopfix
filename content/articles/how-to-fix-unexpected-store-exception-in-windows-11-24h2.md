---
title: "UNEXPECTED_STORE_EXCEPTION on Windows 11 24H2: How to Fix It"
slug: how-to-fix-unexpected-store-exception-in-windows-11-24h2
date: 2026-09-11
categories: ["windows-errors"]
tags: ["windows 11", "blue screen", "store exception", "ssd"]
description: "UNEXPECTED_STORE_EXCEPTION crashing your Windows 11 24H2 laptop? It's usually your SSD or its driver — here's how to diagnose and fix it."
thumbnail: "/images/thumbs/how-to-fix-unexpected-store-exception-in-windows-11-24h2.webp"
faqs:
  - q: "What does UNEXPECTED_STORE_EXCEPTION mean?"
    a: "The 'store' is Windows' memory manager component that handles paging data between RAM and disk. This error means that component hit an unexpected failure — most often because the storage drive or its driver misbehaved during a page operation. It's a storage problem far more often than a memory problem."
  - q: "Is my SSD dying if I get this error?"
    a: "Possibly, but don't assume it yet. Outdated storage drivers, corrupted system files, and antivirus filter drivers cause this error on perfectly healthy SSDs. Check the drive's SMART health first — if it's clean, the cause is almost certainly software."
  - q: "Why did it start after the 24H2 update?"
    a: "The 24H2 update changed storage stack behavior and delivered new storage drivers. An older SSD firmware or driver that worked under 23H2 can fault under 24H2's timing. Updating the storage driver and SSD firmware resolves most post-update cases."
  - q: "Can antivirus cause UNEXPECTED_STORE_EXCEPTION?"
    a: "Yes. Antivirus filter drivers sit in the storage I/O path, and a buggy or outdated filter can crash the store component. If crashes started after an AV update, try disabling its real-time protection temporarily or updating it — and make sure Windows Security isn't fighting a second AV."
---

UNEXPECTED_STORE_EXCEPTION on Windows 11 24H2: How to Fix It

UNEXPECTED_STORE_EXCEPTION is Windows' storage subsystem raising its hand and saying something went wrong while moving data between RAM and your drive. The name is opaque, but the practical meaning is clear: look at your SSD and its driver first. Since the 24H2 update, this error has spiked — 24H2 reworked parts of the storage stack, and older SSD firmware and drivers are feeling it.

Don't panic about your data: the error is about the paging path, not your files, and the fixes below start with the easy software causes before anyone suggests replacing hardware. If your crashes point at memory rather than storage, our [memory management BSOD guide](/articles/memory-management-bsod-windows-11-fix/) is the parallel track.

## Why this happens

- **The storage driver is buggy or outdated.** NVMe and Intel RST drivers that predate 24H2 are the top cause of post-update cases.
- **SSD firmware is old.** Firmware bugs in the drive itself can fault under 24H2's changed I/O patterns.
- **Antivirus filter drivers interfere.** AV products hook every disk read/write; a bad filter crashes the store component.
- **The drive is actually failing.** Bad NAND blocks in the paging area produce exactly this error — SMART data will show it.
- **Corrupted system files.** Damage to the memory manager's own components triggers the exception from the software side.
- **Fast Startup + driver mismatch.** A hibernated storage driver state from before the update can wedge the I/O path.

## How to fix it

Work through these in order — software causes first, hardware verdict last.

### Fix 1: Update the storage drivers

The single most effective fix for post-24H2 cases.

1. Open **Device Manager**, expand **Storage controllers** and **IDE ATA/ATAPI controllers**.
2. Right-click each controller (Intel RST, NVMe controller, Standard SATA AHCI Controller) and choose **Update driver > Search automatically for drivers**.
3. Then get the maker's tested version: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/) — enter your model/serial and install their storage/chipset driver.
4. Reboot and use the laptop for a day, including sleep/wake cycles — storage crashes often strike on resume.

### Fix 2: Update the SSD firmware

Firmware fixes for 24H2-era I/O bugs are common.

1. Identify your SSD: open **Device Manager > Disk drives** and note the model, or run `Get-PhysicalDisk | Select FriendlyName, FirmwareVersion` in PowerShell.
2. Visit the SSD maker's site (Samsung Magician, Crucial Storage Executive, WD Dashboard, Intel MAS) and check for firmware updates.
3. Apply the update following the tool's instructions — keep the laptop on AC power throughout.
4. Recheck stability for a few days; firmware updates resolve whole classes of these crashes at once.

### Fix 3: Check drive health with SMART

Get a verdict on the hardware before going further.

1. Install CrystalDiskInfo (free) or your SSD maker's tool and look at **Health Status**.
2. **Good/Caution/Bad**: "Good" means keep troubleshooting software. "Caution" or "Bad" — especially with reallocated sectors, CRC errors, or a falling health percentage — means the drive is the problem.
3. Also run `chkdsk C: /f /r` from an elevated Command Prompt (reboot to scan) to fix file-system-level damage.
4. If SMART shows failure: back up immediately and replace the drive. No driver update fixes dying NAND.

### Fix 4: Disable Fast Startup

Clear the hibernated driver state that may be wedging the storage path.

1. Press **Win + R**, type `powercfg.cpl`, press **Enter**.
2. Click **Choose what the power buttons do**, then **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup** and **Save changes**.
4. Shut down fully (not restart), power back on, and test for a day.

### Fix 5: Investigate the antivirus filter

AV drivers live in the exact I/O path that's crashing.

1. If crashes started after an antivirus update, open the AV and temporarily disable real-time protection — test for stability.
2. Make sure you're not running two antivirus products (e.g., a third-party AV plus Windows Security's real-time protection fighting it).
3. Update the AV to its latest version, or use the vendor's clean-removal tool and rely on Windows Security for a while as a test.
4. If removing the AV ends the crashes, try a different vendor or stick with Windows Security — a crashing filter driver isn't worth any feature set.

### Fix 6: Repair system files

Rule out corruption in the store component itself.

1. Open an elevated **Terminal** and run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Reboot and monitor. If SFC finds corruption in `stornvme.sys` or related files that DISM can't repair, an in-place repair install using Microsoft's official Windows 11 installation media refreshes them while keeping files and apps.
4. Related storage-adjacent crashes like [DRIVER_POWER_STATE_FAILURE](/articles/driver-power-state-failure-windows-11-fix/) share some of these same driver suspects.

### Fix 7: Clean-install the storage driver / reset Windows

The last software steps before blaming hardware.

1. In **Device Manager**, uninstall the storage controller (tick **Attempt to remove the driver**), then reboot — Windows installs its inbox driver, which is often more stable than a bad vendor one.
2. If crashes persist with a healthy SMART report and clean drivers, run **Reset this PC** (keep files) to eliminate deep software causes.
3. Still crashing after a reset with good SMART? Test with a different SSD if possible — some failures only show under specific I/O patterns that SMART doesn't capture.
4. Microsoft tracks storage-related known issues in its Windows support documentation — check for your SSD model and 24H2.

## Closing

UNEXPECTED_STORE_EXCEPTION is the storage subsystem asking for help, and on 24H2 the answer is usually a storage driver or SSD firmware that's behind the times. Update both, verify the drive's health with SMART, and clear the usual suspects (Fast Startup, AV filters) — and the exception becomes unexpected in the good way: as in, it never happens again.
