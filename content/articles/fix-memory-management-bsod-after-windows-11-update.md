---
title: "How to Fix the Memory Management BSOD After a Windows 11 Update"
slug: fix-memory-management-bsod-after-windows-11-update
date: 2026-10-06
categories: ["windows-errors"]
tags: ["bsod", "memory", "windows-update"]
description: "MEMORY_MANAGEMENT blue screen started after a Windows 11 update? Here's how to tell a driver problem from bad RAM — and fix whichever it is."
thumbnail: "/images/thumbs/fix-memory-management-bsod-after-windows-11-update.webp"
faqs:
  - q: "What does the MEMORY_MANAGEMENT stop code mean?"
    a: "Windows detected corruption in how memory is managed — a driver wrote to memory it didn't own, a system file handling memory got damaged, or physical RAM returned bad data. After a Windows update, the most common cause is a driver the update installed or a system file the update corrupted."
  - q: "How do I know if it's bad RAM or a bad driver?"
    a: "Run Windows Memory Diagnostic (mdsched.exe) or MemTest86. Clean passes point at drivers or system files; errors point at RAM. Timing also helps: crashes that began within hours of an update are usually driver-related, while random crashes over months lean toward hardware."
  - q: "Can a Windows update damage RAM?"
    a: "No — updates can't physically damage memory. But they can expose marginal RAM: new memory-management code paths or drivers may touch memory regions the old code never stressed, turning a latent hardware weakness into visible crashes. The RAM was already weak; the update just revealed it."
  - q: "Should I reinstall Windows for MEMORY_MANAGEMENT errors?"
    a: "Only as a last resort. Most cases resolve with driver updates/rollbacks, SFC/DISM repairs, or RAM reseating/replacement. Reinstall if you've eliminated drivers and RAM and crashes persist — a clean install rules out deep system corruption definitively."
---
The MEMORY_MANAGEMENT blue screen is Windows catching its own memory bookkeeping in a corrupted state. When it starts right after a Windows 11 update, the timing is your biggest clue — but it's also a little misleading, because the same stop code comes from two very different places: bad drivers (software) and bad RAM (hardware). An update can trigger either path.

This guide helps you figure out which one you're dealing with and fix it, without wasting a weekend on the wrong theory.

A practical tip before you start: pay attention to the crash pattern. If the blue screens happen during specific activities — gaming, video calls, large file copies — note them, because the pattern often implicates a particular driver (graphics, network, storage). If they're completely random, even at idle, lean toward RAM or system-file causes. Either way, work the list below in order and don't skip the memory test — it's the single step that most often changes the diagnosis.

## Why this happens

- **Driver replaced by the update** — network, storage, or graphics drivers with memory bugs, installed by Windows Update over working versions.
- **Corrupted system files** — the update damaged Windows' own memory-management components.
- **Marginal RAM exposed** — memory that was borderline before now faults under the update's changed code paths.
- **Antivirus filter drivers** — third-party security drivers incompatible with the new build's memory handling.
- **Corrupted page file** — the disk-backed virtual memory file damaged during the update.
- **Overclocked/XMP memory instability** — RAM tuning that the previous build tolerated but the new one doesn't.
- **Failing SSD** — bad sectors corrupting the page file or memory-mapped system files.

## How to fix it

Work through these in order — software first (it's the likely culprit after an update), hardware second.

### Fix 1: Roll back recently updated drivers

Start with what the update most likely changed.

1. Open **Device Manager** (**Windows + X** > **Device Manager**).
2. Check **Display adapters**, **Network adapters**, and **Storage controllers**: right-click each > **Properties** > **Driver** tab, and look at the **Driver Date**.
3. For any driver dated around the update, click **Roll Back Driver**.
4. Restart and use the laptop normally for a day. If crashes stop, you've found it — get the proper driver from your laptop maker's support site instead of letting Windows Update reinstall the bad one.

### Fix 2: Update drivers from the manufacturer

If rollbacks aren't available, go the other direction — proper current drivers.

1. Note your exact model (**Windows + R** > `msinfo32` > **System Model**).
2. Download chipset, graphics, network, and storage drivers from the manufacturer's support page.
3. Install chipset first, restart; then graphics, restart; then network. Test for stability after each — this isolates the culprit.
4. For Intel machines, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is a reliable source for chipset, Wi-Fi, and Bluetooth drivers.

### Fix 3: Repair system files with DISM and SFC

Fix what the update may have corrupted in Windows itself.

1. Open **Terminal (Admin)** (**Windows + X**) and run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
   Wait for it to complete — it downloads clean copies of damaged files.
2. Then run `sfc /scannow`.
3. Restart. If SFC reports unfixable corruption on repeated runs, note it — that's a sign pointing toward the disk or a deeper problem (see Fix 6).

### Fix 4: Reset the page file

A corrupted page file causes exactly this stop code.

1. Press **Windows + R**, type `sysdm.cpl`, press Enter. Go to the **Advanced** tab > **Performance** > **Settings** > **Advanced** tab > **Virtual memory** > **Change**.
2. Uncheck **Automatically manage paging file size for all drives**, select **No paging file**, click **Set**, then **OK**. Restart.
3. After reboot, return to the same dialog, re-check **Automatically manage paging file size for all drives**, click **Set** > **OK**, and restart again.
4. Windows rebuilds the page file from scratch — if it was corrupted, the crashes stop here.

### Fix 5: Test the RAM thoroughly

Now the hardware side — don't skip this.

1. Press **Windows + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. For a conclusive test, create a MemTest86 USB on another PC, boot from it, and run at least 2 full passes (overnight is ideal).
3. Errors? Power off, unplug, open the laptop, and reseat the RAM sticks firmly. Retest.
4. Still erroring? Test sticks individually to find the bad one and replace it. Also enter BIOS (**F2/Del** at boot) and disable XMP/DOCP memory profiles — run at stock speeds to confirm stability.

### Fix 6: Check the drive and remove filter drivers

Two remaining software-adjacent causes.

1. Run `chkdsk C: /f /r` in an admin Terminal (schedule at restart if prompted) to catch disk corruption affecting the page file.
2. Check SMART status: `wmic diskdrive get status` should return **OK**.
3. Uninstall third-party antivirus completely (**Settings** > **Apps** > **Installed apps**) — filter drivers are a known MEMORY_MANAGEMENT trigger after build updates. Test for several days on Microsoft Defender.
4. Uninstall VPN clients and disk utilities you don't need, for the same reason.

### Fix 7: Uninstall the update or reset Windows

When everything else passes but crashes continue.

1. **Settings** > **Windows Update** > **Update history** > **Uninstall updates** — remove the update that started the trouble, restart, test for a few days.
2. If stable, pause updates for a few weeks before letting it reinstall.
3. If crashes persist even without the update, do **Settings** > **System** > **Recovery** > **Reset PC** > **Keep my files** > **Cloud download**.
4. After the reset, install manufacturer drivers first, then update Windows — and watch for the crash's return to identify the trigger.

## Closing

After a Windows 11 update, MEMORY_MANAGEMENT is usually the update's driver shuffle or file damage — both fixable without new hardware. But because the same stop code comes from dying RAM, always run the memory test before declaring it a software problem; it's the step that prevents the most wasted effort. For the broader memory-related blue screen family, see [stop code MEMORY_MANAGEMENT step by step](/articles/how-to-fix-stop-code-memory-management-step-by-step/), the general [MEMORY_MANAGEMENT BSOD guide](/articles/memory-management-bsod-windows-11-fix/), and Microsoft's [blue screen help page](https://support.microsoft.com/en-us/windows) covers the official troubleshooting path for persistent cases.
