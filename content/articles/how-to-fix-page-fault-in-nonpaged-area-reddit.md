---
title: "How to Fix PAGE_FAULT_IN_NONPAGED_AREA on Windows"
slug: how-to-fix-page-fault-in-nonpaged-area-reddit
date: 2026-09-08
categories: ["windows-errors"]
tags: ["page fault", "nonpaged area", "blue screen", "RAM", "driver error"]
description: "PAGE_FAULT_IN_NONPAGED_AREA blue screen? Usually bad RAM or a faulty driver. Test memory, update drivers, and fix it step by step."
thumbnail: "/images/thumbs/how-to-fix-page-fault-in-nonpaged-area-reddit.webp"
faqs:
  - q: "What does PAGE_FAULT_IN_NONPAGED_AREA mean?"
    a: "Windows tried to read data from the 'nonpaged' memory area — memory that must always stay in RAM — and the data wasn't there. This happens when RAM is faulty, a driver references freed memory, or the page file/disk corrupts the data."
  - q: "Is this always a RAM problem?"
    a: "No — it's about 50/50 between faulty RAM and buggy drivers (especially antivirus filter drivers and storage drivers). Test both: update/remove suspect drivers first since it's fast, then run MemTest86 for the definitive RAM verdict."
  - q: "Why does it happen during gaming or heavy use?"
    a: "Heavy workloads stress RAM, thermals, and drivers simultaneously. If it only happens under load, suspect overheating, an unstable RAM overclock/XMP profile, or the graphics driver — test with XMP disabled and temperatures monitored."
  - q: "Can a Windows update cause PAGE_FAULT_IN_NONPAGED_AREA?"
    a: "Yes. Updates frequently deliver new driver versions, and a buggy storage or network driver from Windows Update is a classic trigger. If crashes started after an update, roll back recent drivers first."
---

**PAGE_FAULT_IN_NONPAGED_AREA** is one of the most-discussed blue screens in PC help forums, and for good reason — it sits exactly on the fence between "bad RAM" and "bad driver," and the internet will confidently tell you it's always one or the other. The truth: it's genuinely about 50/50, so you need a method that checks both without wasting a weekend.

The nonpaged area is memory Windows never swaps to disk — drivers and the kernel live there. When something references data that should be pinned in RAM and it isn't, you get this stop code. Here's how to find out which side of the fence you're on. For the pure step-by-step variant, see [page fault fix, step by step](/articles/how-to-fix-page-fault-in-nonpaged-area-step-by-step/).

One more thing before you start: note whether the crashes mention a driver file on the blue screen. A named file like `ntoskrnl.exe` (points toward RAM) versus a third-party `.sys` file (points toward that driver) is the single most useful clue this stop code gives you — photograph the screen if it flashes by too fast.

## Why this happens

- **Faulty RAM module:** Bad memory cells losing data that should stay resident.
- **Buggy driver referencing freed memory:** A driver using memory after freeing it — antivirus filters and storage drivers are frequent offenders.
- **Corrupted page file:** Damaged virtual memory corrupting data structures.
- **Disk errors:** Bad sectors corrupting paged data the system expects to be intact.
- **Unstable RAM overclock/XMP:** Memory running beyond stable speeds under load.
- **Corrupted system files:** Damaged kernel memory-management components.
- **Bad virtual-memory configuration:** A manually set page file that's too small or on a failing secondary drive.
- **Aggressive BIOS memory settings:** Over-tightened memory timings or voltages in BIOS/UEFI destabilizing RAM.

## How to fix it

Work through these in order — drivers first (fast), RAM second (definitive).

### Fix 1: Identify the faulting driver from the dump

The stop code often names a file (e.g., `Ntfs.sys`, `ndis.sys`, a `.sys` driver). That filename is gold — it collapses the whole investigation to a single driver. Always check the screen and the dump before doing anything else.

1. Note any driver filename shown on the blue screen itself.
2. For detail, open the latest dump in `C:\Windows\Minidump` with **WinDbg Preview** (Microsoft Store) and run `!analyze -v`.
3. If a specific third-party `.sys` file is blamed, update or remove that driver first — you've just saved yourself hours.

### Fix 2: Update or roll back drivers

Cover the usual suspects in one pass.

1. Update **chipset, storage, and network drivers** from your laptop manufacturer's support site.
2. Clean-install the **graphics driver** with DDU in Safe Mode if crashes happen during gaming or video.
3. If crashes began after a Windows update, roll back recently updated drivers in **Device Manager** (**Properties > Driver > Roll Back Driver**).

### Fix 3: Remove antivirus filter drivers temporarily

Antivirus kernel drivers are disproportionately represented in this stop code.

1. Uninstall your third-party antivirus completely (Windows Security takes over).
2. Also temporarily remove VPN clients with network filter drivers.
3. Test for 24–48 hours of normal use before drawing conclusions.

### Fix 4: Reset the page file

A corrupted pagefile.sys can produce exactly this error. Deleting and recreating it is a two-minute job that eliminates an entire category of cause, so do it early rather than after hours of driver work.

1. **Settings > System > About > Advanced system settings > Performance Settings > Advanced tab > Change** (Virtual memory).
2. Uncheck automatic management, select **No paging file**, **Set**, restart.
3. Re-enable **Automatically manage paging file size**, restart again.
4. Run `chkdsk C: /f` in an admin terminal to check the underlying disk.

### Fix 5: Run Windows Memory Diagnostic

Quick RAM screen before the deep test.

1. **Win + R** > `mdsched.exe` > **Restart now and check for problems**.
2. Check results in **Event Viewer > Windows Logs > System** (source **MemoryDiagnostics-Results**).
3. Errors here mean bad RAM — proceed to Fix 7. A pass means continue to Fix 6 for certainty. For the broader memory-BSOD family, see our [memory management BSOD guide](/articles/how-to-fix-memory-management-bsod-in-windows-11-24h2/).

### Fix 6: Run MemTest86 for the definitive answer

This is the definitive test — the one that ends all debate about whether your RAM is good. Block out a few hours; it's worth it for a final answer.

1. Create a bootable **MemTest86** USB on another PC.
2. Boot from it, run at least one full pass (1–3 hours).
3. **Zero errors = RAM is fine; it's a driver problem** — go back to dump analysis (Fix 1) and Driver Verifier (`verifier.exe` with standard settings on third-party drivers, then `verifier /reset` in Safe Mode).
4. Any errors = bad RAM — proceed to Fix 7.

### Fix 7: Reseat or replace the faulty RAM

1. Power off, unplug, open the bottom panel (per your model's service manual).
2. Reseat each SODIMM firmly, then retest — poor seating causes genuine errors.
3. If a specific stick fails, replace it with matching DDR generation/speed.
4. Soldered RAM that's failing = manufacturer warranty/board repair.

### Fix 8: Disable XMP, check thermals, repair system files

The cleanup pass for stubborn cases. If you've reached this point, the cause is something environmental (timings, thermals) or a deeply buried driver issue — these steps cover both.

1. Enter BIOS/UEFI, disable **XMP/EXPO**, reset to optimized defaults.
2. Monitor with **HWiNFO64** — clean fans/vents if running hot.
3. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in an admin terminal.
4. If crashes only occur under specific loads after all this, test with a different GPU driver version from the [manufacturer's archive](https://www.nvidia.com/Download/index.aspx) or the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).

## Closing

PAGE_FAULT_IN_NONPAGED_AREA demands both halves of the investigation: the driver half (dumps, updates, filter-driver removal) and the RAM half (MemTest86's definitive verdict). Do the fast driver work first, then let MemTest86 settle the hardware question once and for all. Whichever side it lands on, you'll have evidence instead of guesses — and that's what separates a permanent fix from a week of random driver reinstalls. And remember the 50/50 rule: if you've only investigated one side (drivers or RAM), you haven't finished. The cases that drag on for weeks are almost always the ones where someone was sure it was the RAM and never checked the drivers — or vice versa.
