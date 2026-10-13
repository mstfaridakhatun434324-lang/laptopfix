---
title: "FAULTY_HARDWARE_CORRUPTED_PAGE: Fixes That Actually Worked (Reddit Roundup)"
slug: how-to-fix-faulty-hardware-corrupted-page-reddit
date: 2026-09-03
categories: ["windows-errors"]
tags: ["bsod", "faulty hardware corrupted page", "ram", "reddit"]
description: "FAULTY_HARDWARE_CORRUPTED_PAGE driving you mad? These are the fixes Reddit users confirm actually solved it — tested, ranked, and explained."
thumbnail: "/images/thumbs/how-to-fix-faulty-hardware-corrupted-page-reddit.webp"
faqs:
  - q: "What fix do Reddit users recommend most for this error?"
    a: "Testing RAM with MemTest86 and replacing the bad stick — it's the most-reported successful fix by far. Second place goes to clean-installing graphics drivers. The community consensus is clear: this error is bad RAM more often than anything else."
  - q: "Is MemTest86 really better than Windows Memory Diagnostic?"
    a: "Yes, according to overwhelming community experience. Windows Memory Diagnostic misses subtle faults that MemTest86 catches. Multiple users report passing the Windows test, then finding errors on MemTest86 within one pass."
  - q: "Can this error be fixed without buying new RAM?"
    a: "Sometimes. Reseating the RAM, disabling XMP, updating graphics drivers, and repairing system files have all fixed it for users whose RAM turned out to be fine. But if MemTest86 shows errors, there's no software workaround — the stick needs replacing."
  - q: "How long does MemTest86 take?"
    a: "One full pass takes 30 minutes to a few hours depending on RAM size and speed. The community recommendation is at least 2-4 passes for confidence. Run it overnight — it's the most reliable way to rule RAM in or out."
---

If you've been searching Reddit threads about `FAULTY_HARDWARE_CORRUPTED_PAGE`, you've seen the pattern: dozens of suggestions, conflicting advice, and no clear winner. This article distills what actually worked for real users — the fixes that show up again and again in "this fixed it for me" replies — organized into a sensible order so you're not trying random things for a week.

The community consensus is remarkably consistent on this one: it's the RAM, until proven otherwise. But "proven otherwise" matters, because drivers and settings cause the identical error. The order below follows the community's most successful diagnostic path. For the full technical deep-dive on this stop code, see our main [FAULTY_HARDWARE_CORRUPTED_PAGE guide](/articles/fix-faulty-hardware-corrupted-page-on-windows-11/) — this article focuses on what's worked in practice.

## Why this happens

- **Failing RAM** (the community's #1 answer): Degraded memory cells corrupt pages. Users consistently report this as the root cause — often on RAM that "worked fine for years." Components age; yesterday's good stick is today's bad one.
- **Unstable XMP/DOCP memory profiles**: A hugely common thread theme. RAM running at its advertised XMP speed isn't guaranteed stable on every motherboard/CPU combo, and the fix is simply turning XMP off.
- **Buggy graphics drivers corrupting memory**: Multiple users traced their crashes to a specific GPU driver version — rolling back or clean-installing fixed it with no hardware changes.
- **Loose or poorly seated RAM**: Several "fixed it" stories end with reseating the sticks. Thermal cycling slowly works contacts loose over years.
- **Failing SSD corrupting the page file**: Less common but real — users whose MemTest86 passed eventually found dying drives.
- **Windows update breaking a storage or chipset driver**: A recurring thread pattern: crashes start the day after Patch Tuesday, fixed by rolling back the update or updating the chipset driver.
- **Overheating**: Mostly on laptops — dust-clogged cooling causing memory errors under load.

## How to fix it

Work through these in order — this is the community's most successful diagnostic sequence.

### Fix 1: Disable XMP/DOCP in the BIOS

The fastest free fix, and the one Redditors suggest trying first because it takes two minutes.

1. Restart and enter the BIOS/UEFI setup (**Del** or **F2** during boot).
2. Find the memory settings — look for **XMP**, **DOCP**, **EXPO**, or **A-XMP** (name depends on your motherboard).
3. Set it to **Disabled** or **Auto** (stock JEDEC speeds).
4. Save and exit, then use the PC normally for a few days.

A surprising number of "fixed it" replies end here. If your RAM is only stable at stock speeds, that's a RAM quality issue — but running at stock is a perfectly fine permanent solution.

### Fix 2: Reseat the RAM

The classic "it was just loose" fix that shows up in thread after thread.

1. Power off completely, unplug, and ground yourself (touch the metal case).
2. Open the case, release the clips, and remove each RAM stick.
3. Blow out the slots with compressed air. Wipe the stick contacts gently with a dry microfiber cloth — no liquids.
4. Reseat firmly until both clips snap shut on their own. The stick should be perfectly level.
5. Boot and test.

If you have two sticks, try booting with just one, then just the other — several users found their crashes followed one specific stick, which is faster than a full MemTest86 run for identifying the culprit.

### Fix 3: Clean-install your graphics driver

The most-reported software fix. Use Display Driver Uninstaller (DDU) for a truly clean slate — the community swears by it.

1. Download **Display Driver Uninstaller** and the latest GPU driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) (don't install the driver yet).
2. Boot into **Safe Mode** (**Settings** > **System** > **Recovery** > **Advanced startup** > **Troubleshoot** > **Advanced options** > **Startup Settings**).
3. Run DDU, select your GPU brand, and click **Clean and restart**.
4. After reboot, install the fresh driver you downloaded.
5. Test with the workload that triggered crashes — gaming, video rendering, whatever it was.

Multiple users specifically report that a *particular driver version* was the problem, so if the latest driver still crashes, try one or two versions older.

### Fix 4: Run MemTest86 — the definitive test

When the quick fixes don't work, this is the test the community trusts. Windows Memory Diagnostic isn't enough — too many users passed it and still had bad RAM.

1. Download **MemTest86** (free) and make a bootable USB with its tool.
2. Boot from the USB and let it run **at least 2 full passes** — overnight for 4 passes if you can.
3. **Any error = bad RAM.** No exceptions, no "maybe it's fine." One error is enough.
4. Test sticks individually to find the bad one.

If MemTest86 is clean after 4 passes, your RAM is fine — stop suspecting it and look at drivers and the drive.

### Fix 5: Roll back the recent Windows update

The "it started after Patch Tuesday" pattern is unmistakable when it's yours.

1. **Settings** > **Windows Update** > **Update history** > **Uninstall updates**.
2. Remove the most recent update, restart, and test for a few days.
3. If the crashes stop, the update (or a driver it delivered) was the cause. Update your **chipset** driver from your motherboard/laptop maker's site before letting the update reinstall.

### Fix 6: Check the drive health

For the users whose RAM tested fine, the drive was the next most common find.

1. Open **Terminal (Admin)** and run `chkdsk C: /f /r`.
2. Check SMART data with your drive manufacturer's utility (Samsung Magician, WD Dashboard, Crucial Storage Executive).
3. Reallocated sectors, CRC errors, or a failed manufacturer test = replace the drive and reinstall Windows. Back up first.

### Fix 7: Run SFC and DISM

The standard repair pass — occasionally the fix, always worth doing before a reinstall.

1. Open **Terminal (Admin)**.
2. `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
3. Restart and test.

## Closing

The Reddit consensus on FAULTY_HARDWARE_CORRUPTED_PAGE is unusually clear: test the RAM with MemTest86, and believe the result. The threads are full of people who skipped the memory test, spent days updating drivers, and eventually found the bad stick anyway. Do the two-minute fixes first (XMP off, reseat, clean GPU driver), then commit to the overnight MemTest86 run — it's the single highest-value diagnostic step for this error. And whatever you find, back up your data early: corrupted memory pages can corrupt files being written, which is the one consequence worth preventing no matter the cause. For the related memory crash family, our [MEMORY_MANAGEMENT guide](/articles/memory-management-bsod-windows-11-fix/) covers the sibling stop code.
