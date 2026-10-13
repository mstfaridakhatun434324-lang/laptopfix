---
title: "How to Fix PAGE_FAULT_IN_NONPAGED_AREA on Windows 11"
slug: how-to-fix-page-fault-in-nonpaged-area-on-windows-11
date: 2026-10-07
categories: ["windows-errors"]
tags: ["blue screen", "page fault in nonpaged area", "bsod fix", "windows 11"]
description: "PAGE_FAULT_IN_NONPAGED_AREA keeps blue-screening your Windows 11 laptop? Learn what it means and fix it with RAM tests, driver updates, and disk checks."
thumbnail: "/images/thumbs/how-to-fix-page-fault-in-nonpaged-area-on-windows-11.webp"
faqs:
  - q: "What does PAGE_FAULT_IN_NONPAGED_AREA mean?"
    a: "It means Windows tried to read data from a memory region marked as nonpaged — memory that must always be resident in RAM — and the data wasn't there. Stop code 0x50 usually traces back to faulty RAM, a bad driver referencing freed memory, or disk corruption in the paging path. Because nonpaged memory is critical kernel memory, Windows has no safe recovery and blue-screens immediately."
  - q: "Can a Windows update cause this error?"
    a: "Yes. A feature or driver update can install a buggy driver or change memory management behavior in a way that exposes an existing weakness. If crashes started right after an update, roll back the most recent driver or uninstall the latest quality update first. Our [page fault after Windows 11 update](/articles/how-to-fix-page-fault-in-nonpaged-area-after-windows-11-update/) guide covers the update-specific angle in detail."
  - q: "Is PAGE_FAULT_IN_NONPAGED_AREA always a RAM problem?"
    a: "No, but RAM is the prime suspect. Drivers — especially antivirus filter drivers and storage controller drivers — are the other major cause. Run a full memory test and update storage and security drivers before buying new RAM. If the memory test is clean and crashes continue, the driver stack is where to look next."
  - q: "How do I find which driver caused the crash?"
    a: "Open the minidump in WinDbg or a free dump analyzer; the faulting module is usually named directly. Without that, check **Event Viewer > Windows Logs > System** around the crash time for driver warnings. Update or remove whatever driver appears repeatedly just before each crash."
---

PAGE_FAULT_IN_NONPAGED_AREA is one of the oldest and most common blue screens in Windows, and it still shows up regularly on Windows 11 laptops. One moment you're working, the next you're staring at a sad face and a stop code, and after the reboot there's no obvious explanation.

The technical meaning is simpler than it sounds: Windows reached for something in a protected memory region that is never supposed to be paged out to disk — and it wasn't there. That gap usually comes from failing RAM, a driver reading memory it already freed, or disk corruption. Here's how to pin down which one it is and fix it for good.

## Why this happens

- **Failing RAM sticks.** A bad cell in nonpaged pool memory is the single most common cause; the data Windows expects simply isn't where it should be.
- **Buggy storage or chipset drivers.** NVMe, SATA AHCI, and RAID controller drivers manage the boundary between memory and disk — a bug there triggers exactly this fault.
- **Antivirus filter drivers.** Security products hook deep into the memory manager, and an outdated filter driver referencing freed pool memory is a classic trigger.
- **Corrupted page file.** If the page file itself is damaged, the memory manager can lose track of what's resident and what isn't.
- **Disk errors on the system drive.** Bad sectors or a failing SSD in areas Windows uses for paging produce the same symptom as bad RAM.
- **Faulty hardware recently added.** A new RAM stick, a replacement SSD, or even a dock with a flaky controller can introduce the fault.
- **Corrupted system files.** Damaged kernel components can break the bookkeeping that keeps nonpaged memory consistent.

## How to fix it

Work through these in order, starting with memory — because if the RAM is bad, nothing else you do will stick.

### Fix 1: Run a full memory diagnostic

This is step one for a reason: stop code 0x50 loves bad RAM.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. On the blue test screen, press **F1**, choose **Extended**, and set the pass count to at least **2**. A single quick pass misses intermittent faults.
4. If errors appear, power down, remove one stick at a time (if your laptop allows it), and retest to identify the bad module. Replace it — RAM is cheap compared to the hours this error steals.

### Fix 2: Update storage and chipset drivers

The drivers sitting between memory and disk are the next most likely culprits.

1. Open **Device Manager** via **Win + X**.
2. Expand **IDE ATA/ATAPI controllers** and **Storage controllers**. Right-click each entry and choose **Update driver > Search automatically for drivers**.
3. Visit your laptop maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or Lenovo's official support portal — and install the latest chipset and storage driver package for your exact model.
4. If your SSD maker offers a firmware updater (Samsung Magician, WD Dashboard, Crucial Storage Executive), check for SSD firmware updates too.

### Fix 3: Update or temporarily remove your antivirus

Filter drivers are notorious for this exact stop code.

1. Open your antivirus and check for program updates — not just definition updates, the actual engine.
2. If crashes persist, uninstall the third-party antivirus completely and rely on Windows Security for a few days as a test. Use the vendor's dedicated removal tool to clear leftover filter drivers.
3. If the blue screens stop, the antivirus was the cause. Reinstall the latest version from the vendor, or stick with Windows Security, which is genuinely solid on Windows 11 now.

### Fix 4: Check the disk for errors

Rule out the storage side of the equation.

1. Open **Terminal (Admin)** from **Win + X**.
2. Run `chkdsk C: /f /r`. Type **Y** when asked to schedule the check, then restart.
3. Let the full scan finish — `/r` locates bad sectors and recovers readable data, which takes time on large drives.
4. After the scan, check your SSD's health with the manufacturer's tool or CrystalDiskInfo (look at the SMART "health status" percentage). A drive under 70% health is living on borrowed time.

### Fix 5: Reset the page file

A corrupted page file confuses the memory manager's bookkeeping.

1. Open **Settings > System > About**, click **Advanced system settings**.
2. Under **Performance**, click **Settings**, go to the **Advanced** tab, and click **Change** under Virtual memory.
3. Uncheck **Automatically manage paging file size for all drives**, select **No paging file**, and click **Set**.
4. Restart, then go back and re-enable **Automatically manage paging file size for all drives**. This rebuilds the page file from scratch.

### Fix 6: Repair system files

Damaged kernel files can break nonpaged memory accounting.

1. In **Terminal (Admin)**, run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store SFC draws from.
3. Restart and monitor. If SFC reports unfixable corruption even after DISM, an in-place upgrade (see Fix 8) is the cleaner path than fighting it file by file.

### Fix 7: Roll back the last Windows update or driver

If the crashes have a clear "started on Tuesday" story, trust the timeline.

1. Go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the most recent quality update and restart.
3. If a driver update coincided with the crashes, open **Device Manager**, find the device, open **Properties > Driver**, and click **Roll Back Driver**.
4. Then pause updates for a week (**Settings > Windows Update > Pause updates**) so the bad update doesn't reinstall before a fixed version ships.

### Fix 8: Do an in-place upgrade repair

When everything checks out individually but crashes continue, refresh Windows without losing your files.

1. Download the Windows 11 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount the ISO, run **setup.exe**, and choose **Keep personal files and apps**.
3. Let the repair install complete. It reinstalls every system file and driver framework component while leaving your data and programs in place.
4. Afterward, reinstall only essential drivers from your laptop manufacturer's site rather than letting Windows Update grab everything at once.

If the memory test keeps failing on known-good sticks, or crashes persist across a clean Windows install, you're looking at a motherboard-level memory controller fault — that's a warranty or board-replacement conversation. Related stop codes share a lot of the same root causes, so if you're seeing memory-flavored crashes generally, our [MEMORY_MANAGEMENT BSOD guide](/articles/how-to-fix-stop-code-memory-management-on-windows-11/) and the [general blue screen of death walkthrough](/articles/how-to-fix-blue-screen-of-death-windows-11/) are worth a read too.

## Closing

PAGE_FAULT_IN_NONPAGED_AREA is Windows telling you that something it trusted in memory betrayed that trust. Nine times out of ten the betrayal comes from a RAM stick or a storage driver, and the fixes above find it methodically. Work the list, test your memory honestly, and this stop code becomes a solved problem instead of a recurring nightmare.
