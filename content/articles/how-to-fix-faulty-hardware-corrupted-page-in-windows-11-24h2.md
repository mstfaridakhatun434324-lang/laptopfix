---
title: "FAULTY_HARDWARE_CORRUPTED_PAGE in Windows 11 24H2: Diagnosis and 7 Fixes"
slug: how-to-fix-faulty-hardware-corrupted-page-in-windows-11-24h2
date: 2026-09-06
categories: ["windows-errors"]
tags: ["windows-11", "bsod", "faulty-hardware-corrupted-page"]
description: "FAULTY_HARDWARE_CORRUPTED_PAGE crashing Windows 11 24H2? It usually means bad RAM or a failing drive. Here is how to diagnose and fix it."
thumbnail: "/images/thumbs/how-to-fix-faulty-hardware-corrupted-page-in-windows-11-24h2.webp"
faqs:
  - q: "Does FAULTY_HARDWARE_CORRUPTED_PAGE always mean my hardware is dying?"
    a: "Not always, despite the name. It means Windows found a corrupted memory page and blamed hardware, but the corruption can come from a buggy driver writing where it should not, an unstable overclock, or corrupted system files. Genuine hardware failure — usually RAM — is the most common cause, but rule out drivers and software first because those fixes are free."
  - q: "How can I tell if it is the RAM or the SSD?"
    a: "Run Windows Memory Diagnostic (mdsched.exe) first. If it reports errors, it is the RAM. If memory passes repeatedly but crashes continue, suspect the drive: run chkdsk /f /r, check SMART status with wmic diskdrive get status, and look at your SSD manufacturer's health tool. Crashes during heavy disk activity point at the drive; crashes during heavy multitasking point at RAM."
  - q: "Will updating to the latest 24H2 patches fix it?"
    a: "Sometimes. Early 24H2 builds had storage and memory-management bugs that Microsoft patched in later cumulative updates. If you are on an early 24H2 build, installing all pending updates is worth doing. But if the crashes are caused by failing hardware, no update will help — test the RAM and drive regardless."
  - q: "Can Windows Memory Diagnostic really catch a bad RAM stick?"
    a: "Usually, yes. Type mdsched in the Start search, restart, and let the full extended test run — it takes 30 to 60 minutes. If it reports errors, shut down, reseat the RAM modules, and retest each stick alone if your laptop allows access. A clean extended test strongly points the blame back at the SSD or its driver instead."
---

FAULTY_HARDWARE_CORRUPTED_PAGE is Windows telling you it caught corrupted data in memory and is pointing the finger at hardware. On Windows 11 24H2 this error worries people because the name sounds like a death sentence for the laptop. In reality, about half the cases I see are software or configuration problems wearing a hardware costume.

This guide helps you figure out which one you have, then fix it — starting with the free checks.

## Why this happens

- **Failing RAM.** The most common genuine cause. A dying memory module corrupts pages, Windows detects the corruption, and you get this stop code.
- **A buggy driver corrupting memory.** Faulty drivers — especially storage and network drivers in early 24H2 builds — can write to memory pages they do not own.
- **A failing SSD.** Bad flash cells corrupt data as pages are paged in and out, and Windows blames the hardware layer.
- **Unstable overclocking or XMP profiles.** Aggressive memory timings cause intermittent corruption that looks exactly like failing hardware.
- **Overheating.** RAM and SSDs that run too hot produce errors; thin laptops with clogged vents are prime candidates.
- **Corrupted page file.** A damaged pagefile.sys on a drive with bad sectors feeds corrupted pages back into memory.
- **Early 24H2 build bugs.** The first 24H2 releases had memory-management regressions that later cumulative updates fixed.

## How to fix it

Work through these in order. The goal of the first few fixes is diagnosis: find out whether your hardware is actually at fault before spending money.

### Fix 1: Install all pending Windows updates

Rule out the known 24H2 bugs first — it takes ten minutes.

1. Go to **Settings** → **Windows Update** and click **Check for updates**.
2. Install everything offered, including optional driver updates (click **Advanced options** → **Optional updates**).
3. Restart when prompted, even if it says a restart is not required.
4. Use the laptop for a day. If crashes stop, an early-24H2 bug was your problem. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the major 24H2 fixes by KB number if you want to confirm.

### Fix 2: Run Windows Memory Diagnostic

This is the definitive RAM test built into Windows. Run it before anything else hardware-related.

1. Save your work, then press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Let the standard test complete — do not skip it. Results appear after Windows boots back up (check **Event Viewer** → **Windows Logs** → **System**, filter for **MemoryDiagnostics-Results** if the notification does not appear).
4. If it reports hardware problems, you have bad RAM. Skip to Fix 6.

### Fix 3: Check the drive with chkdsk and SMART

If memory passes, the drive is suspect number two.

1. Open **Terminal (Admin)** and run `chkdsk C: /f /r`. Type `Y` when asked to schedule it, then restart and let it finish.
2. After booting, run `wmic diskdrive get status` in the terminal — you want **OK** for every drive.
3. Install your SSD manufacturer's toolbox (Samsung Magician, Crucial Storage Executive, WD Dashboard, Intel MAS) and check the drive health percentage and SMART warnings.
4. If chkdsk found and repaired bad sectors and crashes stop, the drive had fixable file-system damage. If SMART shows warnings, back up immediately — the drive is failing.

### Fix 4: Reset BIOS to defaults and disable XMP

Unstable memory settings cause corruption that mimics dying RAM.

1. Restart and enter the BIOS (usually **F2** or **Del** during the manufacturer's logo).
2. Find the option to **Load Optimized Defaults** or **Load Setup Defaults** and apply it.
3. If you see XMP, EXPO, or any memory overclocking profile enabled, disable it or set memory to standard speeds.
4. Save and exit, then use the laptop normally. If the crashes vanish, your RAM is fine — the overclock was the problem.

### Fix 5: Update storage and chipset drivers

Buggy storage drivers corrupt pages in transit, especially on 24H2.

1. Get the latest chipset and storage/AHCI/NVMe drivers from your laptop manufacturer's support site for your exact model.
2. Install chipset first, then storage, restarting between each.
3. Intel-based laptops can also use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to detect the correct drivers automatically.
4. In **Device Manager** (**Win + X** → **Device Manager**), verify no yellow warnings remain under **Storage controllers** and **IDE ATA/ATAPI controllers**.

### Fix 6: Reseat or replace the RAM

If the memory diagnostic found errors, act on it.

1. Power off completely, unplug, and (if your battery is removable) remove it. Hold the power button 10 seconds to drain residual charge.
2. Open the RAM compartment, remove each module, blow out dust, and reseat firmly until the clips click.
3. Run the memory diagnostic again. If errors persist, test one stick at a time to isolate the bad module.
4. Replace the faulty stick with matching specs (speed, voltage, CAS latency — check the working stick's label). For soldered-RAM ultrabooks with errors, it is a warranty or board-level repair.

### Fix 7: Rebuild the page file and run SFC/DISM

A corrupted page file on a damaged drive sector can keep feeding bad pages into memory.

1. Open **Settings** → **System** → **About** → **Advanced system settings** → **Performance** → **Settings** → **Advanced** → **Virtual memory** → **Change**.
2. Uncheck **Automatically manage paging file size**, select **No paging file**, click **Set**, and restart.
3. Delete `C:\pagefile.sys` if it still exists (you may need to show hidden system files), then go back and re-enable **Automatically manage paging file size** and restart again.
4. In **Terminal (Admin)**, run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` to repair any system files the corruption touched.

## Closing

FAULTY_HARDWARE_CORRUPTED_PAGE demands a diagnosis-first mindset: memory test, drive check, BIOS defaults — in that order — before you conclude anything is dying. I have seen this error "fixed" by a $0 XMP disable and also by a RAM replacement; the tests tell you which one you need. If your memory passes but crashes continue during heavy multitasking, also read our guide on [MEMORY_MANAGEMENT blue screens](/articles/memory-management-bsod-windows-11-fix/), and for the closely related post-update variant see [FAULTY_HARDWARE_CORRUPTED_PAGE after a Windows 11 update](/articles/how-to-fix-faulty-hardware-corrupted-page-after-windows-11-update/).
