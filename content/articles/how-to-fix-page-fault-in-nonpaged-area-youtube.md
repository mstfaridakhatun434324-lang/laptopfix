---
title: "How to Fix PAGE_FAULT_IN_NONPAGED_AREA on a Windows Laptop"
slug: how-to-fix-page-fault-in-nonpaged-area-youtube
date: 2026-10-09
categories: ["windows-errors"]
tags: ["blue screen", "page fault", "memory error"]
description: "PAGE_FAULT_IN_NONPAGED_AREA blue screen? It means Windows touched memory that wasn't there. Here's how to test RAM, update drivers, and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-page-fault-in-nonpaged-area-youtube.webp"
faqs:
  - q: "What does PAGE_FAULT_IN_NONPAGED_AREA mean?"
    a: "Windows tried to read data from a memory region that was supposed to be locked in RAM (the 'nonpaged area') but found it missing or corrupted. The usual causes are faulty RAM, a buggy driver passing bad memory addresses, or disk corruption in the page file area."
  - q: "Is PAGE_FAULT_IN_NONPAGED_AREA always a RAM problem?"
    a: "No — despite the name, drivers cause it just as often. A driver referencing freed or invalid memory triggers the identical stop code. That's why the fix order is: test RAM first (it's definitive), then hunt drivers. If the memory test passes clean, shift focus to recently updated drivers."
  - q: "How long does Windows Memory Diagnostic take?"
    a: "The standard pass takes 15–30 minutes depending on your RAM size. For a thorough test, choose the Extended mode (press F1 at the blue test screen), which can take several hours but catches intermittent faults the quick pass misses."
  - q: "Can antivirus cause PAGE_FAULT_IN_NONPAGED_AREA?"
    a: "Yes. Antivirus filter drivers operate at a low level where memory mistakes crash the system. If crashes started after an AV update or install, temporarily uninstall it (keeping Windows Security on) as a test — it's a quick way to rule a major suspect in or out."
---
PAGE_FAULT_IN_NONPAGED_AREA sounds like pure hardware failure, and sometimes it is — but just as often it's a driver handing Windows a bad memory address. The name describes what Windows was doing when it crashed, not what's broken. So don't rush to buy new RAM: test first, then follow the evidence.

Work through these in order, starting with the memory test since it gives a definitive yes-or-no on the hardware. A closely related variant is covered in our [page fault in nonpaged area (Reddit cases) guide](/articles/how-to-fix-page-fault-in-nonpaged-area-reddit/), and memory-related crashes pair well with [faulty hardware corrupted page fixes](/articles/how-to-fix-faulty-hardware-corrupted-page/).

## Why this happens

- **Faulty RAM stick:** Bad memory cells in the nonpaged pool region — the most classic cause.
- **Buggy device driver:** A driver dereferencing invalid or freed memory, often after a driver update.
- **Corrupted page file:** Damage to pagefile.sys makes paged memory look like nonpaged faults.
- **Disk corruption:** Bad sectors where memory-mapped files live produce the same stop code.
- **Antivirus filter drivers:** Low-level AV drivers with memory bugs.
- **Overclocking or bad RAM timings:** Unstable memory from XMP/manual overclocks on some laptops.
- **Failing motherboard memory controller:** Rare, but the last suspect when RAM and drivers check out.
- **Loose RAM from drops or heat cycling:** Physical shocks and thermal expansion can weaken RAM seating over time, producing intermittent faults that pass quick tests but fail extended ones.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the blue screens stop appearing.

### Fix 1: Run Windows Memory Diagnostic

Definitive RAM test, built into Windows. Do this before anything else.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**.
3. The blue memory test screen appears. For a deeper test, press **F1**, select **Extended**, and press **F10** — this takes longer but catches intermittent faults.
4. Let it complete; the laptop reboots automatically.
5. Check results: open **Event Viewer** (**eventvwr.msc**) > **Windows Logs** > **System**, filter for source **MemoryDiagnostics-Results**.
6. If errors are reported, you've found it — proceed to Fix 2. If clean, skip to Fix 3.

### Fix 2: Reseat or replace the faulty RAM

Confirmed bad memory needs physical attention.

1. Power off, unplug, and (if your laptop allows) remove the bottom panel.
2. Release the RAM module clips, remove the stick, and firmly reseat it — a surprising number of "faults" are just poor contact.
3. If you have two sticks, test with one at a time to identify the bad one (run `mdsched.exe` again per stick).
4. Replace the faulty stick with matching specs (DDR4/DDR5, speed, voltage — check your laptop's manual).
5. If RAM is soldered (common on ultrabooks), this becomes a warranty/motherboard repair — contact the manufacturer.

### Fix 3: Update or roll back device drivers

With RAM cleared, drivers are suspect number one — especially anything updated just before crashes began.

1. Open **Device Manager** (**Win + X** > **Device Manager**).
2. Update **Display adapters**, **Network adapters**, and **System devices** via **Update driver** > **Search automatically for drivers**.
3. If a specific driver was recently updated, right-click it > **Properties** > **Driver** > **Roll Back Driver**.
4. Get the full tested set from your maker: [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
5. Restart and stress-test with normal use for a day.

### Fix 4: Run CHKDSK and repair system files

Rules out disk corruption masquerading as memory faults.

1. Open an **administrator Command Prompt**.
2. Run `chkdsk C: /f /r` (press **Y**, restart, let it finish).
3. Back in Windows, run `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and monitor.

### Fix 5: Reset the page file

A corrupted pagefile.sys is a lesser-known but real cause.

1. Press **Win + R**, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab > **Performance** > **Settings** > **Advanced** tab > **Virtual memory** > **Change**.
3. Uncheck **Automatically manage paging file size for all drives**.
4. Select **No paging file**, click **Set**, and restart (this deletes the old page file).
5. Return to the same dialog, re-check **Automatically manage**, click **Set**, and restart again.
6. Windows creates a fresh page file — test for stability.

### Fix 6: Temporarily remove third-party antivirus

Quick elimination test for filter-driver causes.

1. Uninstall your third-party antivirus via **Settings** > **Apps** > **Installed apps** (disabling often leaves the driver loaded).
2. Verify **Windows Security** is active.
3. Use the laptop normally for a day or two.
4. If crashes stop, the AV driver was at fault — reinstall the latest version or switch products.
5. If crashes continue, reinstall your AV; it wasn't the cause.

### Fix 7: Disable Fast Startup and check for overclocking

Stability settings that reduce memory-related crashes.

1. Open **Control Panel** > **Power Options** > **Choose what the power buttons do** > **Change settings that are currently unavailable**.
2. Uncheck **Turn on fast startup** and save — this forces clean memory initialization on every boot.
3. If you enabled XMP or any overclocking in BIOS, revert to stock memory settings.
4. Restart and test.

## Closing

PAGE_FAULT_IN_NONPAGED_AREA is a "test, don't guess" error. The memory diagnostic gives you a clean verdict on RAM in under an hour, and that verdict decides the whole repair path: bad RAM means reseat or replace; clean RAM means hunt drivers, starting with whatever changed most recently. Most people land in the second camp and are fixed by a driver update or rollback. Whatever you find, don't ignore recurring instances — memory faults, whether silicon or software, don't heal themselves, and the crash you postpone is the unsaved work you lose. Save your work frequently while troubleshooting, since these crashes give no warning. For deeper crash analysis, learn to [read dump files with WinDbg](/articles/how-to-read-dump-files-with-windbg-on-windows-11/) to see exactly which driver faulted.
