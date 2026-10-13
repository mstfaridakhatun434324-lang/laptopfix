---
title: "How to Fix FAULTY_HARDWARE_CORRUPTED_PAGE in Windows 11"
slug: faulty-hardware-corrupted-page-bsod-windows-11
date: 2026-10-11
categories: ["windows-errors"]
tags: ["blue screen", "faulty hardware", "RAM", "memory error", "windows 11"]
description: "FAULTY_HARDWARE_CORRUPTED_PAGE in Windows 11 points to bad RAM or a driver corrupting memory. Test memory, update drivers, fix it step by step."
thumbnail: "/images/thumbs/faulty-hardware-corrupted-page-bsod-windows-11.webp"
faqs:
  - q: "What does FAULTY_HARDWARE_CORRUPTED_PAGE mean?"
    a: "Windows' memory manager detected that a page of memory was corrupted — either by defective RAM hardware or by a driver writing where it shouldn't. Despite the name, it's a software/driver problem roughly half the time, so don't order new RAM until you've done the software checks."
  - q: "Is FAULTY_HARDWARE_CORRUPTED_PAGE always bad RAM?"
    a: "No. Drivers that corrupt memory (bad storage, network, or antivirus filter drivers) produce the identical stop code. The reliable way to tell: if Windows Memory Diagnostic and MemTest86 both pass clean, it's almost certainly a driver, not the RAM."
  - q: "Can a Windows 11 update cause this error?"
    a: "Yes — 24H2-era reports frequently trace it to a driver the update installed or to Intel/AMD chipset driver mismatches. If the crashes started right after an update, roll back recent driver changes before suspecting hardware."
  - q: "How long does MemTest86 need to run?"
    a: "One full pass (all tests, roughly 1–3 hours depending on RAM size) with zero errors is a solid clean bill of health. If you see even a single error, the RAM is bad — memory must be perfect, not 'mostly fine.'"
---

**FAULTY_HARDWARE_CORRUPTED_PAGE** is Windows 11's way of saying "something scribbled on memory that didn't belong to it." The name pushes you toward blaming the RAM, and sometimes that's right — but drivers that corrupt memory produce this exact same stop code. The trick is testing in the right order so you don't buy RAM you don't need or reinstall drivers for a hardware fault.

This guide is tuned for Windows 11 (including 24H2). For the version-agnostic walkthrough with a different fix order, see our [general faulty hardware corrupted page guide](/articles/best-way-to-fix-faulty-hardware-corrupted-page/).

## Why this happens

- **Defective RAM module:** The literal cause — a stick with bad cells corrupts whatever Windows stores there.
- **Driver corrupting memory:** Buggy storage, network, or filter drivers (antivirus, VPN) writing past their buffers; Windows 11 24H2 updates have triggered several waves of these.
- **Unstable RAM overclock/XMP:** Memory running faster than it's stable for produces intermittent corruption under load.
- **Overheating:** Heat-induced bit flips in RAM, common in thin laptops with clogged cooling.
- **Corrupted page file or disk errors:** A damaged pagefile.sys or bad sectors where virtual memory lives.
- **Failing SSD:** Less common, but a dying drive corrupting paged-out memory contents.

## How to fix it

Work through these in order — software first, hardware last.

### Fix 1: Update chipset and storage drivers

Memory-corrupting drivers are usually low-level ones, so start there. On Windows 11 — particularly 24H2 — chipset and storage driver mismatches after feature updates are a documented trigger for this exact stop code.

1. Go to your laptop maker's support site and download the latest **chipset** and **storage (SATA/NVMe)** drivers for your exact model.
2. Install the chipset driver first, restart, then the storage driver, restart again.
3. Also update the **network drivers** (Wi-Fi and Ethernet) — network filter drivers are notorious memory corruptors.
4. Use the laptop normally for a day and watch for crashes.

### Fix 2: Remove memory-corrupting third-party software

Antivirus filter drivers and "RAM optimizer" tools run in kernel mode and can corrupt memory.

1. Uninstall any third-party antivirus, "PC cleaner," or RAM-booster utilities. Windows Security is a fine replacement.
2. Uninstall VPN clients temporarily — their network filter drivers are a known trigger.
3. Restart and test for a day or two before reinstalling anything.

### Fix 3: Run Windows Memory Diagnostic

Quick first-pass RAM test, built into Windows.

1. Press **Win + R**, type `mdsched.exe`, press Enter.
2. Choose **Restart now and check for problems**.
3. After the reboot and test, check results in **Event Viewer > Windows Logs > System**, filtering for source **MemoryDiagnostics-Results**.
4. If it reports errors, skip to Fix 6 — you've found bad RAM.

### Fix 4: Reset the page file and check the disk

A corrupted pagefile can masquerade as RAM corruption.

1. Open **Settings > System > About > Advanced system settings**, then under Performance click **Settings**, go to the **Advanced** tab, and click **Change** under Virtual memory.
2. Uncheck **Automatically manage paging file size**, select **No paging file**, click **Set**, and restart.
3. After rebooting, go back and re-enable **Automatically manage paging file size** — this recreates pagefile.sys from scratch.
4. Open **Terminal (Admin)** and run `chkdsk C: /f` to rule out disk errors underneath it all.

### Fix 5: Run MemTest86 for a definitive RAM verdict

Windows Memory Diagnostic is a screening test; MemTest86 is the real thing. The built-in test misses subtle faults that MemTest86's pattern tests catch, so a "pass" from Windows doesn't close the hardware question.

1. On another PC, download **MemTest86** (free) and create a bootable USB.
2. Boot the laptop from the USB and let it run at least **one full pass** (1–3 hours).
3. **Zero errors = RAM is fine**, and your problem is a driver. Any errors at all = bad RAM, proceed to Fix 6.
4. If you have two sticks, test them one at a time to find the bad one.

### Fix 6: Reseat or replace the RAM

Only do this after MemTest86 shows errors (or Windows Memory Diagnostic does).

1. Power off, unplug, and remove the bottom panel (check your model's service manual — some RAM is soldered and not replaceable).
2. Remove each SODIMM, blow out dust, and reseat firmly until the clips click. Retest — bad seating causes real errors.
3. If errors persist on a specific stick, replace it with a matching module (same DDR generation, speed, and ideally timings).
4. If the RAM is soldered and failing, it's a motherboard/warranty repair.

### Fix 7: Disable XMP/overclocking and check thermals

If MemTest86 passes but crashes happen under load:

1. Enter BIOS/UEFI and disable **XMP/EXPO** memory profiles, returning RAM to stock speed.
2. Reset any CPU tuning in Intel XTU, Ryzen Master, or manufacturer utilities.
3. Monitor temperatures with **HWiNFO64** — sustained high temps plus this stop code means cleaning fans and vents, and possibly repasting on older machines.

### Fix 8: Clean-install the most suspicious drivers

When RAM tests clean but crashes continue, do a driver purge of the usual suspects.

1. In **Safe Mode**, use **DDU** to clean-install the graphics driver.
2. In **Device Manager**, uninstall the Wi-Fi and storage controller drivers (right-click > **Uninstall device**), then restart and let Windows reinstall, or install the manufacturer's versions fresh.
3. If a specific driver version is implicated (check minidumps with WinDbg — see [how to analyze dump files](/articles/how-to-analyze-bsod-dump-files-in-windows-11-24h2/)), install the last known-good version from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) instead of the newest.

## Closing

FAULTY_HARDWARE_CORRUPTED_PAGE demands a disciplined order: update the low-level drivers, strip out kernel-mode third-party tools, then prove the RAM guilty or innocent with MemTest86 before spending money. On Windows 11 — especially after 24H2 updates — the driver side of this error is more common than people expect, so don't skip the software steps just because the stop code says "hardware." If MemTest86 is clean and fresh drivers don't help, the minidump will usually name the corrupting driver — that's your final lead. Document what you find — if MemTest86 flagged a stick, note which slot; if a driver fixed it, note the version. Memory corruption issues love to resurface after the next driver update, and your notes turn a repeat into a five-minute fix.
