---
title: "FAULTY_HARDWARE_CORRUPTED_PAGE: What to Do Next"
slug: what-to-do-if-faulty-hardware-corrupted-page
date: 2026-09-30
categories: ["windows-errors"]
tags: ["FAULTY_HARDWARE_CORRUPTED_PAGE", "RAM failure", "hardware diagnosis"]
description: "Seeing FAULTY_HARDWARE_CORRUPTED_PAGE? Don't panic: test your RAM and SSD, update drivers, and follow this guide to find whether hardware is truly at fault."
thumbnail: "/images/thumbs/what-to-do-if-faulty-hardware-corrupted-page.webp"
faqs:
  - q: "Does FAULTY_HARDWARE_CORRUPTED_PAGE always mean my hardware is broken?"
    a: "No — despite the alarming name, this stop code is frequently caused by buggy drivers corrupting memory pages, not by dead hardware. Windows names the error for what it detected (a corrupted hardware page), not for the root cause. Always test drivers and run memory diagnostics before buying replacement parts."
  - q: "Which hardware component causes this error most often?"
    a: "System RAM is the prime suspect, followed by the SSD or hard drive, and occasionally the motherboard's memory controller. Start with Windows Memory Diagnostic to test RAM, then check your drive's SMART health. If both pass clean, the cause is almost certainly a driver rather than hardware."
  - q: "Can a Windows update cause FAULTY_HARDWARE_CORRUPTED_PAGE?"
    a: "Yes. Updates can expose latent bugs in older storage, chipset, or memory-adjacent drivers, and the resulting corruption triggers exactly this stop code. If crashes began right after an update, update your chipset and storage drivers first, and consider rolling back the update as a test."
  - q: "How do I test my RAM properly for this error?"
    a: "Run Windows Memory Diagnostic (mdsched.exe) for a quick check, but for a definitive answer use MemTest86 booted from a USB drive and let it complete at least 4 full passes — that takes several hours. A single error in MemTest86 means the RAM stick under test is faulty and should be replaced."
---

FAULTY_HARDWARE_CORRUPTED_PAGE (stop code `0x12B`) is Windows telling you it found a memory page whose contents don't match what hardware should have delivered. The name screams "broken hardware," and sometimes it is — but just as often, a driver corrupted the page in transit and the hardware is perfectly fine. Your job is to figure out which.

This guide runs the investigation in the right order: rule out the cheap software causes first, then test the hardware properly. It's closely related to the [MEMORY_MANAGEMENT](/articles/memory-management-bsod-blue-screen-error-fix/) stop code, and the diagnostic tools overlap — if you've already run [memory diagnostics](/articles/how-to-run-memory-diagnostic-tool-on-laptop/), you're halfway there.

## Why this happens

- Failing RAM sticks or slots delivering corrupted data to the memory controller.
- A dying SSD or hard drive corrupting paged-out memory contents.
- Buggy storage or chipset drivers corrupting memory pages during transfers.
- Overheating components (especially RAM or the chipset) causing bit errors.
- Unstable overclocks or undervolts on CPU, RAM, or cache.
- Corrupted page file or hibernation file feeding bad data back on resume.

## How to fix it

Work through these in order: software first, then quick hardware tests, then deep hardware testing.

### Fix 1: Run Windows Memory Diagnostic

Start with the built-in RAM test — it's fast and catches obvious failures.

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems (recommended)**.
3. Let the **Standard** test finish without interrupting.
4. After reboot, open **Event Viewer > Windows Logs > System** and find the **MemoryDiagnostics-Results** entry.
5. Hardware errors here mean RAM is suspect — continue to Fix 6 for confirmation.

### Fix 2: Update chipset and storage drivers

Storage and chipset drivers move every byte of paged memory, so stale versions are prime suspects.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Expand **IDE ATA/ATAPI controllers** and **Storage controllers**; update each driver.
3. Download the latest chipset driver from your laptop maker's support site (Dell, HP, Lenovo, or ASUS) for your exact model.
4. If you have an Intel system, [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the right chipset package automatically.
5. Restart and use the laptop normally for a day to check for recurrences.

### Fix 3: Check drive health with SMART

A failing drive corrupts the page file and hibernation data, producing exactly this error.

1. Open an elevated **Command Prompt** and run `wmic diskdrive get status`.
2. Every drive should report **OK** — anything else means replace the drive.
3. For detail, install your SSD maker's toolbox (Samsung Magician, Crucial Storage Executive, WD Dashboard).
4. Check the **health percentage** and **reallocated sector count**.
5. Back up immediately if health is below 80% or warnings appear — then replace the drive.

### Fix 4: Disable hibernation and rebuild the page file

Corrupted hibernation or page-file data can trigger this error on every resume or under memory pressure.

1. In an elevated Command Prompt, run `powercfg /hibernate off` to disable hibernation.
2. Open **System Properties** (`sysdm.cpl`) > **Advanced** > **Performance Settings** > **Advanced** > **Virtual memory > Change**.
3. Uncheck **Automatically manage**, select **No paging file**, click **Set**, and restart.
4. Return to the same dialog, re-enable **Automatically manage paging file size**, and restart again.
5. This forces Windows to create a fresh, clean page file.

### Fix 5: Repair system files and roll back recent updates

Rule out OS-level corruption and update-triggered driver bugs before blaming hardware.

1. In an elevated Command Prompt, run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` and restart.
3. If crashes started after an update, go to **Settings > Windows Update > Update history > Uninstall updates** and remove it.
4. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) lists known issues per update if you want to verify first.
5. Monitor for a few days — stable means software was the cause.

### Fix 6: Run MemTest86 for a definitive RAM verdict

If quick tests were inconclusive but crashes continue, MemTest86 gives the final word on RAM.

1. On another PC, download MemTest86 and create a bootable USB with its installer.
2. Boot your laptop from the USB (use the **F12**/boot menu key for your brand).
3. Let it run at least **4 full passes** — expect several hours; don't interrupt.
4. Any red error line means the installed RAM is faulty.
5. Test sticks individually to identify which one fails, then replace it.

### Fix 7: Reseat components and reset the BIOS

Loose modules and aggressive firmware settings cause intermittent corruption that mimics failing hardware.

1. Power off, unplug, and remove the bottom panel.
2. Reseat the RAM modules and the SSD firmly in their slots.
3. Enter the BIOS and load **Setup Defaults** (usually **F9**), disabling any XMP or manual timings.
4. Clean dust from vents and fans — overheating RAM throws exactly these errors.
5. Reassemble, boot, and stress-test with normal heavy use.

### Fix 8: Stress-test and monitor temperatures

Intermittent heat-related corruption only shows up under load, so finish with a controlled stress test.

1. Install **HWiNFO64** and watch RAM-adjacent temperatures (chipset, SSD, CPU package) during heavy use.
2. Run a memory-heavy workload — large photo edits, video renders, or several virtual machines — for an hour.
3. If crashes only happen when hot, improve cooling: clean vents, replace dried thermal paste, or use a cooling pad.
4. Laptop RAM rarely has its own heatsink, so chipset and SSD heat are the usual culprits.
5. Stable under stress with clean thermals means your fix held — close the case on this one.

## Closing

FAULTY_HARDWARE_CORRUPTED_PAGE demands a verdict, not a guess: test the RAM, check the drive, update the drivers that move memory around, and only then consider replacement parts. In practice, drivers and corrupted page files cause more of these crashes than dead hardware does — so the software-first order in this guide saves most people from buying RAM they didn't need.
