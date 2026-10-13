---
title: "The Best Way to Fix the MEMORY_MANAGEMENT Stop Code"
slug: best-way-to-fix-stop-code-memory-management
date: 2026-10-06
categories: ["windows-errors"]
tags: ["memory-management", "bsod", "ram"]
description: "Stop code MEMORY_MANAGEMENT has a clear best fix order: test RAM, update drivers, repair files. Here is the sequence ranked by success rate."
thumbnail: "/images/thumbs/best-way-to-fix-stop-code-memory-management.webp"
faqs:
  - q: "What is the single most effective fix for MEMORY_MANAGEMENT?"
    a: "Testing and replacing faulty RAM. Stop code 0x1A is the memory manager catching corruption, and a dying RAM stick is the cause more often than all software causes combined. The Windows Memory Diagnostic takes under 30 minutes and gives you a definitive answer."
  - q: "Can outdated drivers really cause a memory stop code?"
    a: "Yes. Drivers that write outside their allocated memory corrupt the memory manager's bookkeeping, which triggers exactly this stop code. Graphics, storage controller, and network drivers are the usual offenders — which is why driver updates come right after the RAM test in the fix order."
  - q: "How long does it take to fix this error properly?"
    a: "Plan for an hour of active work plus one overnight test if needed. The RAM test takes 20-30 minutes, driver updates about 20 minutes, and SFC/DISM another 20. Only if the quick RAM test passes but crashes continue do you need the overnight MemTest86 run."
  - q: "Should I run MemTest86 or is the Windows tool enough?"
    a: "Start with the Windows Memory Diagnostic — it catches obviously bad sticks fast. If it passes but you still crash, run MemTest86 overnight; it is far more thorough and catches marginal sticks the built-in test misses. Two clean MemTest86 passes means your RAM is almost certainly fine."
---
MEMORY_MANAGEMENT (stop code 0x1A) is Windows catching its memory bookkeeping corrupted. The name makes everyone assume it is the RAM — and most of the time they are right — but drivers and system files can produce the identical crash. MEMORY_MANAGEMENT (stop code 0x1A) is Windows catching its memory bookkeeping corrupted. The name makes everyone assume it is the RAM — and most of the time they are right — but drivers and system files can produce the identical crash.

There is a well-established best order for fixing this, ranked by how often each step actually resolves it. Follow it top to bottom instead of trying things at random, and you will waste the least time. There is a well-established best order for fixing this, ranked by how often each step actually resolves it. Each step also tells you what a positive result means, so you are never left wondering whether to keep going.

## Why this happens

- **Failing RAM.** A stick flipping bits corrupts whatever Windows stored there — the most common cause by a wide margin.
- **A driver writing to memory it does not own.** Buggy graphics, storage, or network drivers corrupt the memory manager's structures.
- **Corrupted system files.** Damage to Windows' own memory management components triggers the stop code from normal operations.
- **Unstable RAM overclock or XMP profile.** Aggressive memory timings cause intermittent corruption that only shows under load.
- **Failing storage drive.** Corrupted data read from a dying drive poisons the memory pages Windows caches.
- **Damaged page file.** Corruption in pagefile.sys means data swapped to disk comes back wrong.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Test the RAM with Windows Memory Diagnostic

Highest success rate of any single step — do this first, not last. Schedule it when you can spare the reboot — the test takes over the machine completely, so save your work first.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. If it reports hardware problems, you have found it: reseat the RAM, test sticks individually if you have two, and replace the bad one.
4. If it passes, keep going — the built-in test is quick but not exhaustive.

### Fix 2: Update graphics, chipset, and storage drivers

The most common non-RAM cause, and a twenty-minute job. Do the graphics driver first if you must prioritize: on laptops it is the single driver most likely to corrupt memory behind the scenes.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Update drivers under **Display adapters**, **IDE ATA/ATAPI controllers**, **Storage controllers**, and **Network adapters** (right-click each > **Update driver > Search automatically for drivers**).
3. Then install the latest chipset and graphics drivers from your laptop maker's support site — for example [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
4. Restart and use the laptop for a full day before declaring it fixed.

### Fix 3: Repair system files with SFC and DISM

Eliminates Windows' own corruption as a suspect. DISM needs internet access to fetch clean copies — if you are offline it can fall back to local sources, but the online repair is more reliable.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow` and wait for it to finish.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart. If SFC found and fixed corruption, there is a good chance your crashes are done.

### Fix 4: Run the overnight MemTest86 test

The definitive RAM verdict for when the quick test passed but crashes continue. One pass is not enough — errors often appear only after the sticks heat up, which is why the overnight run matters.

1. Download MemTest86, create a bootable USB, and boot from it.
2. Let it run at least 4 passes — ideally overnight.
3. Any red errors mean bad RAM, even if Windows' own test passed. Replace the stick.
4. Two fully clean passes means RAM is cleared — the cause is software. Our [memory troubleshooting walkthrough](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/) covers what to check next.

### Fix 5: Check the drive and rebuild the page file

A dying drive or corrupted pagefile.sys feeds bad data into memory. The page-file rebuild sounds drastic but is harmless: Windows recreates it automatically, and a corrupted pagefile is a real (if uncommon) cause of 0x1A.

1. In an elevated **Command Prompt**, run `chkdsk C: /f /r` (press **Y** to schedule at restart) and reboot.
2. Check drive health: `wmic diskdrive get status` should report OK.
3. To rebuild the page file: **Win + R**, type `sysdm.cpl`, go to **Advanced > Performance Settings > Advanced > Virtual memory > Change**, uncheck automatic management, set **No paging file**, reboot, then re-enable automatic management and reboot again.

### Fix 6: Disable XMP and reset BIOS to defaults

Marginal RAM overclocks are a classic intermittent cause. Even factory XMP profiles can be marginal on specific CPU and motherboard combinations — 'it came that way' does not mean it is stable.

1. Enter BIOS/UEFI setup during boot (**F2** or **Del**).
2. Disable XMP/EXPO or any memory overclock profile.
3. Load optimized defaults, save, and exit.
4. If crashes stop, your RAM was not stable at its rated speed — run it at stock or replace it. For general blue screen reading skills, see our [BSOD fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 7: In-place Windows repair as the last resort

When hardware tests clean and drivers are current, refresh Windows itself. The in-place upgrade reinstalls tens of thousands of system files while leaving your programs alone — it is the highest-success software step precisely because it is so thorough.

1. Download the installer from Microsoft's Windows 11 download page.
2. Run setup and choose **Keep personal files and apps**.
3. After completion, reinstall graphics and chipset drivers fresh before anything else.

## Closing

The best way to fix MEMORY_MANAGEMENT is also the simplest: test the RAM first, update the drivers second, repair Windows third. That order resolves the vast majority of cases because it follows the actual probability of each cause. Skip the order and you will spend days fixing things that were never broken. And if the RAM test names a bad stick, replace it rather than removing it and limping along on half your memory — single-channel mode is a performance penalty you will feel every day.
