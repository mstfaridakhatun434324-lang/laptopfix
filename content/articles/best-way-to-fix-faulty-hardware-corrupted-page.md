---
title: "The Best Way to Fix FAULTY_HARDWARE_CORRUPTED_PAGE"
slug: best-way-to-fix-faulty-hardware-corrupted-page
date: 2026-10-13
categories: ["windows-errors"]
tags: ["blue screen", "faulty hardware", "memory corruption", "RAM test", "driver fix"]
description: "FAULTY_HARDWARE_CORRUPTED_PAGE blue screen? The definitive fix order: driver cleanup, page file reset, MemTest86, then RAM replacement if needed."
thumbnail: "/images/thumbs/best-way-to-fix-faulty-hardware-corrupted-page.webp"
faqs:
  - q: "What's the fastest way to fix FAULTY_HARDWARE_CORRUPTED_PAGE?"
    a: "Update your chipset, storage, and network drivers, then remove third-party antivirus and VPN filter drivers. That resolves the driver-caused majority of cases in under an hour. Only if crashes persist should you spend time on full RAM testing with MemTest86."
  - q: "How do I know if it's the RAM or a driver?"
    a: "Run MemTest86 for one full pass. Zero errors means the RAM is fine and a driver is corrupting memory — check your minidumps with WinDbg to identify it. Any errors at all means the RAM is defective, since good memory must be 100% error-free."
  - q: "Can I fix this without opening my laptop?"
    a: "Yes, in most cases. Driver updates, removing kernel-mode software, resetting the page file, and running SFC/DISM are all software fixes. You only need to open the laptop if MemTest86 proves a RAM stick is bad and your model has replaceable SODIMM modules."
  - q: "Does this error mean my hard drive is failing?"
    a: "Rarely, but it's possible — a dying drive can corrupt paged memory contents. Run chkdsk and check the drive's SMART health. If the drive is healthy and MemTest86 passes, the drive isn't your problem."
---

**FAULTY_HARDWARE_CORRUPTED_PAGE** is one of those stop codes where the name sends people down the wrong path. Yes, it *can* mean bad RAM — but it just as often means a driver is scribbling over memory it doesn't own, and Windows caught it. The "best way" to fix it isn't a single trick; it's a specific order that avoids wasting money on RAM you don't need.

Think of it as a process of elimination: eliminate the drivers (cheap, fast), then prove the RAM guilty or innocent (definitive, slow), then act on the verdict. If you want the Windows 11–specific version of this walkthrough, see our [Windows 11 edition](/articles/faulty-hardware-corrupted-page-bsod-windows-11/).

A word on mindset: treat this like an investigation, not a guessing game. Each fix below rules out one category — drivers, third-party software, page file, RAM, thermals. Skip steps and you'll end up going in circles; follow the order and you'll converge on the answer.

## Why this happens

- **Buggy kernel-mode driver:** Storage, network, and antivirus filter drivers that write past their memory buffers — the most common cause overall.
- **Defective RAM:** Bad memory cells corrupting whatever Windows stores in them.
- **Unstable memory overclock/XMP:** RAM pushed past its stable speed produces intermittent corruption.
- **Corrupted page file:** A damaged pagefile.sys makes paged memory come back corrupted.
- **Overheating:** Thermal stress causing bit errors in RAM, especially in thin laptops under sustained load.
- **Failing storage:** A dying SSD/HDD corrupting data as virtual memory pages are written and read back.

## How to fix it

Work through these in order — each step eliminates a category of cause.

### Fix 1: Update the drivers that touch memory most

Memory corruption almost always comes from low-level drivers, so start with those.

1. Download the latest **chipset**, **storage controller**, and **network** drivers from your laptop manufacturer's support site (not just Windows Update). Intel users can also run the [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) to detect the right chipset driver automatically.
2. Install chipset first, restart; then storage, restart; then network, restart.
3. Update the **BIOS/UEFI firmware** too — firmware updates include memory-controller and microcode fixes.
4. Use the PC normally and note whether crashes stop.

### Fix 2: Strip out kernel-mode third-party software

This single step fixes a remarkable number of cases.

1. Uninstall third-party antivirus suites, VPN clients, "RAM optimizers," and disk utility tools that install drivers.
2. Check **Device Manager > View > Show hidden devices** for leftover filter drivers from uninstalled software and remove them.
3. Restart and test for 24–48 hours. Windows Security handles protection fine in the meantime.

### Fix 3: Analyze the minidump to name the suspect

If crashes continue, let the dump point the finger. The minidump is a snapshot of the crime scene — the faulting module, the call stack, the corrupted address. Ten minutes here beats ten driver reinstalls.

1. Install **WinDbg Preview** from the Microsoft Store.
2. Open the latest `.dmp` from `C:\Windows\Minidump` and run `!analyze -v`.
3. Look for the faulting module — if a specific `.sys` file appears across multiple dumps, that's your corrupting driver. Update, roll back, or replace it accordingly; the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) is the best source for alternate driver versions.

Our [dump file analysis guide](/articles/how-to-analyze-bsod-dump-files-in-windows-11-24h2/) walks through this in detail if WinDbg feels intimidating.

### Fix 4: Reset the page file and verify the disk

Rule out virtual-memory corruption before blaming physical RAM.

1. Open **System Properties**: **Settings > System > About > Advanced system settings > Performance Settings > Advanced > Change** (Virtual memory).
2. Uncheck automatic management, set **No paging file**, click **Set**, restart.
3. Re-enable **Automatically manage paging file size** and restart again — pagefile.sys is now rebuilt from scratch.
4. Run `chkdsk C: /f` in an admin terminal and check SMART health with your manufacturer's diagnostic.

### Fix 5: Run MemTest86 — the definitive RAM test

This is the step that gives you a final answer on the hardware.

1. Create a bootable **MemTest86** USB on another computer.
2. Boot from it and run at least **one complete pass** (1–3 hours for typical laptop RAM).
3. Interpret strictly: **zero errors = RAM is innocent** (go back to drivers, Fix 6). **Any error = bad RAM** (go to Fix 7).
4. With two sticks, test individually to isolate the bad one.

### Fix 6: Driver purge when RAM tests clean

MemTest86 passed but crashes continue? A driver is definitely the culprit.

1. Boot into **Safe Mode** and use **DDU** for a clean graphics driver install.
2. In **Device Manager**, uninstall the storage controller and network adapter drivers, then reinstall fresh copies from the manufacturer.
3. Use **Driver Verifier** (`verifier.exe` in Run dialog) with standard settings on third-party drivers to catch the corrupter red-handed — be ready for it to intentionally BSOD the guilty driver, then boot to Safe Mode to disable Verifier with `verifier /reset`.

### Fix 7: Replace the bad RAM

Only reach this step with a failed MemTest86 in hand.

1. If your laptop has removable SODIMM slots, power off, unplug, open the bottom panel, and reseat the modules first — then retest, since poor seating causes real errors.
2. Replace the failing stick with a matching module (same DDR generation and speed).
3. If RAM is soldered, contact the manufacturer — it's a board-level warranty repair.
4. After replacement, run MemTest86 once more to confirm zero errors.

### Fix 8: Check thermals and power

The last-mile check for intermittent cases.

1. Monitor with **HWiNFO64** under load — thermal throttling plus this stop code means cleaning vents/fans and possibly repasting.
2. Test on AC power with the battery removed if possible (on models that allow it) to rule out power-delivery instability.
3. If crashes only happen on battery or only on AC, the power circuitry is suspect — a repair shop diagnosis is warranted.

## Closing

The best fix for FAULTY_HARDWARE_CORRUPTED_PAGE is a disciplined elimination: drivers first (Fix 1–2), then evidence from dumps (Fix 3), then the definitive MemTest86 verdict (Fix 5), then act on it. Most people who jump straight to buying RAM waste money; most people who reinstall Windows repeatedly waste time. Follow the order, trust the test results, and you'll land on the real cause — whether it's a $0 driver fix or a RAM stick that genuinely needs replacing. The most expensive mistake with this stop code is replacing RAM that was never bad. The second most expensive is reinstalling Windows five times for a driver problem. The elimination order above avoids both.
