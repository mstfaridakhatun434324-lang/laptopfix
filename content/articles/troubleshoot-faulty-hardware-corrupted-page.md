---
title: "Troubleshooting FAULTY_HARDWARE_CORRUPTED_PAGE Step by Step"
slug: troubleshoot-faulty-hardware-corrupted-page
date: 2026-09-16
categories: ["windows-errors"]
tags: ["blue screen", "faulty hardware corrupted page", "0x12b", "memory test", "troubleshooting"]
description: "A methodical step-by-step troubleshooting plan for FAULTY_HARDWARE_CORRUPTED_PAGE — isolate RAM, drivers, and SSD faults with certainty."
thumbnail: "/images/thumbs/troubleshoot-faulty-hardware-corrupted-page.webp"
faqs:
  - q: "How do I know if it's the RAM or a driver?"
    a: "Pattern is everything. Crashes that blame different drivers each time, or happen at random moments, point to RAM. Crashes that always name the same .sys file and happen during the same activity point to that driver. MemTest86 settles it definitively — clean passes mean it's almost certainly software."
  - q: "How long should I run MemTest86?"
    a: "At least 4 full passes, which takes several hours — overnight is ideal. Intermittent RAM faults often don't appear until pass 3 or later. One quick pass isn't enough to declare memory healthy."
  - q: "Can a Windows update cause FAULTY_HARDWARE_CORRUPTED_PAGE?"
    a: "Yes. Updates can install buggy storage or chipset drivers that corrupt memory pages, and they can enable memory settings your RAM can't handle. If crashes started right after an update, check our [post-update variant guide](/articles/how-to-fix-faulty-hardware-corrupted-page-after-windows-11-update/) before buying hardware."
  - q: "What if MemTest86 is clean but crashes continue?"
    a: "Then focus on drivers and the SSD. Update chipset and storage drivers, check the drive's SMART health, and run Driver Verifier to catch a driver writing out of bounds. Clean memory plus persistent 0x12B crashes is a software problem until proven otherwise."
---

FAULTY_HARDWARE_CORRUPTED_PAGE (0x12B) is a diagnosis disguised as an accusation: Windows found a corrupted memory page and is telling you about it. But "hardware" in the name is Windows' best guess, not a verdict. This guide is a true troubleshooting sequence — each step eliminates a suspect, so by the end you know exactly what's broken instead of guessing.

Grab a notebook (or a notes app on your phone) and record what each step shows. Patterns across steps are what solve this.

## Why this happens

- **Degrading RAM modules.** Memory cells weaken over time; single-bit errors corrupt pages unpredictably.
- **Unstable memory timings.** XMP/EXPO profiles or manual timings the modules can't quite sustain.
- **Drivers writing outside their memory.** A buggy driver corrupts pages belonging to other components.
- **SSD errors corrupting the page file.** Pages swapped to a failing drive return corrupted.
- **Motherboard or memory-controller faults.** Damaged slots or traces corrupt data in transit.
- **Heat-related memory instability.** Hot RAM or a hot memory controller produces transient errors.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Document the crash pattern

Good troubleshooting starts with data, not fixes.

1. For the next few crashes, note the time, what you were doing, and how long the laptop had been on.
2. Check each dump with BlueScreenView — record which driver (if any) is blamed each time.
3. Ask: same driver every time (driver suspect), different drivers (RAM suspect), or no driver named (deeper hardware suspect)?
4. Note whether crashes cluster after the laptop warms up — heat-related faults follow a warm-up curve.
5. This log guides every decision below and saves you from fixing the wrong thing.

### Fix 2: Establish a software baseline

Strip the system to known-good software before testing hardware.

1. Boot into Safe Mode and use the laptop for a while — if it's stable in Safe Mode, a third-party driver is corrupting memory.
2. Perform a clean boot (`msconfig` > hide Microsoft services > disable all, plus disable startup apps) and test normally.
3. Uninstall recently added drivers, especially storage, chipset, and "optimizer" tools.
4. Run `DISM /Online /Cleanup-Image /RestoreHealth` then `sfc /scannow` in **Terminal (Admin)**.
5. If the system is stable at baseline, reintroduce software in halves until crashes return. Our broader [Windows 11 blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers baseline techniques in more depth.

### Fix 3: Reset all clocks and voltages to stock

Remove overclocking from the suspect list definitively.

1. Enter BIOS/UEFI and disable XMP/EXPO, CPU overclock, undervolt, and memory timing tweaks.
2. Load optimized defaults, save, and exit.
3. Also check for manufacturer "performance" utilities in Windows (Armoury Crate, Lenovo Legion Toolkit, Dell Alienware Command Center) and reset those to stock.
4. Test for at least 48 hours of normal use at stock settings.
5. Only proceed to hardware testing after confirming stock settings still crash — otherwise you've already found it.

### Fix 4: Run the Windows Memory Diagnostic

Quick first-pass memory test.

1. Press **Windows + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**, pressing **F1** for **Extended** mode.
3. Let it complete without interruption.
4. After reboot, open **Event Viewer > Windows Logs > System** and find **MemoryDiagnostics-Results**.
5. Errors here are conclusive — replace the RAM. Clean results mean you need the deeper test next.

### Fix 5: Run MemTest86 overnight

The definitive memory test.

1. Create a bootable MemTest86 USB on another computer.
2. Boot the laptop from it and let it run at least 4 full passes (overnight recommended).
3. Zero errors across 4 passes means the RAM modules themselves are almost certainly fine.
4. If errors appear, test sticks individually and in different slots to separate bad sticks from bad slots.
5. Record exactly which stick/slot errors — this matters for warranty claims and targeted replacement.

### Fix 6: Stress the storage subsystem

Check the drive behind the page file.

1. Back in Windows, open **Terminal (Admin)** and run `chkdsk C: /f /r` (schedule at reboot if prompted).
2. Check SMART data with your SSD manufacturer's utility — look at reallocated sectors, media errors, and overall health percentage.
3. Run a disk benchmark (CrystalDiskMark) and watch for errors or hangs during the test.
4. If the drive shows warnings, clone it to a replacement SSD before it fails outright.
5. As a diagnostic, temporarily move the page file to a different drive via **Advanced system settings > Performance > Virtual memory** and see if crashes stop.

### Fix 7: Use Driver Verifier to catch corrupting drivers

If memory and storage test clean, hunt the driver.

1. Press **Windows + R**, type `verifier`, and press Enter.
2. Choose **Create custom settings**, enable **Special pool** and **Pool tracking**, then select third-party drivers from the list.
3. Restart and use the laptop — Verifier will crash the system quickly when a driver corrupts pool memory, naming the culprit.
4. Analyze the resulting dump, update or remove the named driver.
5. Boot to Safe Mode and run `verifier /reset` to disable Verifier when done.

### Fix 8: Decide on hardware repair or replacement

When all tests point at hardware, act on the evidence.

1. Bad RAM stick identified: replace with the exact spec (DDR generation, speed, voltage) from your laptop manual.
2. Bad slot but good sticks: the motherboard needs repair — weigh the cost on older laptops.
3. Clean RAM but persistent crashes: suspect the SSD or motherboard; professional diagnosis with known-good parts is fastest.
4. Get repair quotes before committing — on laptops over 4–5 years old, replacement often beats repair.
5. Microsoft's [blue screen troubleshooting hub](https://support.microsoft.com/en-us/windows) lists final recovery options.

## Closing

The step-by-step approach turns FAULTY_HARDWARE_CORRUPTED_PAGE from a scary accusation into a solvable puzzle: document the pattern, baseline the software, de-clock, test memory properly, check storage, and hunt drivers with Verifier. Most people find their answer by Fix 5. Whatever you find, you'll know it with evidence — not guesswork — and that's what separates a fix from a hope. If this stop code landed right after a Windows 11 update, the [post-update FAULTY_HARDWARE_CORRUPTED_PAGE guide](/articles/how-to-fix-faulty-hardware-corrupted-page-after-windows-11-update/) sorts out update-triggered driver faults from real hardware.
