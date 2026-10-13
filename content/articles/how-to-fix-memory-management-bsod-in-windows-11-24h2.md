---
title: "Fix MEMORY_MANAGEMENT BSOD After the Windows 11 24H2 Update"
slug: how-to-fix-memory-management-bsod-in-windows-11-24h2
date: 2026-10-12
categories: ["windows-errors"]
tags: ["blue screen", "memory management", "windows 11 24h2", "bsod fix"]
description: "MEMORY_MANAGEMENT blue screens after the Windows 11 24H2 update? Fix it with RAM tests, driver rollbacks, and update-specific repairs that work."
thumbnail: "/images/thumbs/how-to-fix-memory-management-bsod-in-windows-11-24h2.webp"
faqs:
  - q: "Why did the 24H2 update cause MEMORY_MANAGEMENT crashes?"
    a: "Feature updates replace core memory-management components and update dozens of drivers at once. If a driver was already borderline — especially storage, chipset, or antivirus filter drivers — the new memory manager can expose the bug as a crash. In some cases the update itself installs a buggy driver version. The timing is the clue: crashes that begin within days of 24H2 point at the update, not sudden hardware failure."
  - q: "Should I roll back the 24H2 update?"
    a: "Only as a diagnostic step, not the first fix. Try updating drivers, testing RAM, and repairing system files first — these resolve most cases while keeping you on the supported build. If crashes clearly started with 24H2 and nothing else helps, rolling back within the 10-day window is reasonable, then update again once fixed drivers ship."
  - q: "How is this different from a regular MEMORY_MANAGEMENT BSOD?"
    a: "The stop code and root causes are the same — bad RAM, bad drivers, disk issues — but the trigger is the update itself. That changes the fix order: update-related fixes (driver rollbacks, uninstalling the update, DISM repair of the new component store) come before hardware suspicion. Our general [MEMORY_MANAGEMENT stop code guide](/articles/how-to-fix-stop-code-memory-management-on-windows-11/) covers the hardware-first angle."
  - q: "Can I prevent this on the next feature update?"
    a: "Mostly, yes. Update your chipset, storage, and BIOS drivers from the manufacturer before installing a feature update, temporarily uninstall third-party antivirus, and make sure you have 20GB+ free on the system drive. After the update, verify drivers again — Windows often swaps in its own versions during the upgrade."
---

The Windows 11 24H2 update brought a lot of improvements — and for some laptops, a nasty side effect: recurring MEMORY_MANAGEMENT blue screens. If your machine was rock-solid before the update and started crashing after it, the update is the prime suspect, and the fix order is different from a generic memory crash.

This guide is tuned for exactly that scenario: crashes that began with 24H2. We'll start with update-specific fixes, then fall back to the standard memory diagnostics if the update angle doesn't pan out.

## Why this happens

- **A driver the update installed is buggy.** 24H2 refreshes storage, chipset, and display drivers; a bad one in the mix triggers memory-management crashes.
- **An old driver conflicts with the new memory manager.** 24H2 changed kernel memory handling, and drivers written against older behavior can now fault.
- **Antivirus filter drivers break under the new build.** Security products hook the memory manager deeply; outdated engines crash after feature updates.
- **The update itself is partially corrupt.** Interrupted or low-disk-space upgrades leave the component store damaged.
- **Pre-existing marginal RAM gets exposed.** Tighter memory checking in the new build can surface RAM that was silently borderline before.
- **BIOS/firmware incompatibility.** Older BIOS versions sometimes mishandle the power and memory states 24H2 expects.
- **Third-party disk tools conflicting.** Disk encryption, backup, or defrag utilities with kernel drivers may not be 24H2-ready.

## How to fix it

Work through these in order — update-specific fixes first, hardware checks after.

### Fix 1: Update chipset and storage drivers for 24H2

The update often leaves you with generic drivers where you need manufacturer ones.

1. Open **Device Manager** (**Win + X**) and check **IDE ATA/ATAPI controllers**, **Storage controllers**, and **System devices** for anything with a warning icon.
2. Download the latest chipset and storage drivers for your exact model making sure the package lists Windows 11 24H2 support. (Check Dell's, HP's, or Lenovo's support site for your exact model.)
3. Install the chipset package first, then storage drivers, restarting between them.
4. Check your SSD manufacturer's tool for a firmware update too; 24H2-era firmware fixes are common.

### Fix 2: Update or remove third-party antivirus

This is the single most common 24H2-specific trigger.

1. Open your antivirus and force a program update (not just definitions).
2. Check the vendor's site for an explicit "Windows 11 24H2 compatible" version — install it.
3. If crashes continue, uninstall the antivirus completely using the vendor's removal tool, and run on Windows Security for a few days. If the BSODs stop, the antivirus was the cause; reinstall only the 24H2-certified version.

### Fix 3: Roll back recently updated drivers

If Device Manager shows drivers dated to your 24H2 install, they may be the problem.

1. In **Device Manager**, open **Properties** on display, network, and storage devices.
2. On the **Driver** tab, check the driver date. If it matches the update window and **Roll Back Driver** is available, click it.
3. Prioritize rolling back the display driver and any storage controller driver.
4. After rolling back, use the manufacturer's site to install the last known-good version rather than letting Windows Update pick.

### Fix 4: Repair the component store

Feature updates can leave the component store damaged, especially if disk space ran low.

1. Open **Terminal (Admin)** and run `DISM /Online /Cleanup-Image /RestoreHealth`. On 24H2 this can take 15–30 minutes; let it finish.
2. Then run `sfc /scannow`.
3. Restart. If DISM reports it repaired the store, there's a good chance the crashes were update corruption rather than hardware.

### Fix 5: Uninstall the 24H2 update (diagnostic rollback)

If crashes began the day 24H2 installed, prove the connection.

1. Go to **Settings > System > Recovery**.
2. Under **Recovery options**, if **Go back** is available (10-day window), use it to return to the previous build.
3. Test stability for a few days. If crashes stop, 24H2 was the trigger — update all drivers and the BIOS, then reinstall 24H2 from the [Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11) rather than Windows Update.
4. If **Go back** is gone, use **Settings > Windows Update > Update history > Uninstall updates** to remove the most recent cumulative update as a partial test.

### Fix 6: Test the RAM

If update fixes don't help, verify the hardware the new build is stressing.

1. Run `mdsched.exe`, choose **Restart now and check for problems**, and use **Extended** mode with 2 passes (press **F1** on the test screen).
2. For certainty, run MemTest86 overnight.
3. Also disable **XMP/EXPO** in the BIOS temporarily — 24H2's memory handling can expose a marginal overclock that older builds tolerated.

### Fix 7: Check disk health and free space

24H2 needs breathing room, and a struggling drive corrupts the paging path.

1. Free up at least 20GB on C: — use **Settings > System > Storage > Temporary files** and **Cleanup recommendations**.
2. Run `chkdsk C: /f /r` in an elevated prompt and let it complete at next boot.
3. Check SSD health with the manufacturer's utility. A drive with declining health plus a major update is a crash waiting to happen.

### Fix 8: Update the BIOS

Manufacturers ship 24H2-compatibility BIOS updates that fix memory and power-state handling.

1. Check your version with `msinfo32` under **BIOS Version/Date**.
2. Compare with the latest for your model on the manufacturer's support page, looking for release notes mentioning 24H2 or memory stability.
3. Flash with the charger connected, following instructions exactly.

If you've done all eight and crashes persist, analyze a minidump with WinDbg (`!analyze -v`) to name the faulting driver — at that point it's a specific driver bug, not the update in general. Related reading: our [page fault in nonpaged area guide](/articles/how-to-fix-page-fault-in-nonpaged-area-on-windows-11/) for the sibling stop code, and the [general blue screen of death walkthrough](/articles/how-to-fix-blue-screen-of-death-windows-11/) for dump-analysis basics.

## Closing

When MEMORY_MANAGEMENT crashes start with the 24H2 update, the update is guilty until proven innocent — but "the update" almost always means a driver the update brought along. Refresh the chipset and storage drivers, sort out the antivirus, repair the component store, and most 24H2-triggered crashes disappear without ever touching the RAM.
