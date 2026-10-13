---
title: "REFERENCE_BY_POINTER Blue Screen: Step-by-Step Fix"
slug: how-to-fix-reference-by-pointer-bsod-step-by-step
date: 2026-09-07
categories: ["windows-errors"]
tags: ["blue screen", "driver error", "bsod fix"]
description: "REFERENCE_BY_POINTER blue screen on Windows? Follow this step-by-step guide to find the bad driver and stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-reference-by-pointer-bsod-step-by-step.webp"
faqs:
  - q: "What does REFERENCE_BY_POINTER mean?"
    a: "Windows tracks how many parts of the system are using certain kernel objects with a reference count. This stop code (0x00000018) means a driver decremented a count too far — usually to zero while the object was still in use, or negative. It's a driver bug, caught by Windows' bookkeeping."
  - q: "Which drivers cause REFERENCE_BY_POINTER?"
    a: "Most often third-party antivirus/filter drivers, storage controller drivers, and network drivers — anything that hooks kernel objects. The crash dump usually names the exact .sys file, which is why analyzing the dump is Fix 1."
  - q: "Can RAM cause REFERENCE_BY_POINTER?"
    a: "Indirectly, yes. Faulty RAM can corrupt the reference counts stored in memory, producing this stop code with no single driver at fault. If the named driver keeps changing between crashes, test the memory with MemTest86 before chasing drivers further."
  - q: "Is it safe to just ignore it if it happens rarely?"
    a: "No. Each occurrence means a driver corrupted kernel bookkeeping, and while Windows caught it this time, the underlying bug can corrupt data silently on the occasions it doesn't crash. A rare REFERENCE_BY_POINTER still deserves the dump analysis in Fix 1."
---

REFERENCE_BY_POINTER (stop code 0x00000018) is one of the rarer blue screens, which also makes it one of the more confusing ones. In plain terms: Windows keeps a reference count for certain system objects, and a driver decremented one too many times — a classic driver bug, caught red-handed.

The good news about a specific driver bug is that it's fixable without hardware surgery. Our [REFERENCE_BY_POINTER reference](/articles/best-way-to-fix-reference-by-pointer-bsod/) has the technical background; this is the hands-on, step-by-step version. Start at Fix 1. Don't let the rarity of this stop code worry you — rare just means fewer people have documented it online, not that it's harder to fix than the common ones.

## Why this happens

- A buggy third-party driver mishandling object reference counts — the textbook cause.

- Antivirus or firewall drivers hooking kernel objects incorrectly.

- Outdated storage or network drivers with known reference-count bugs.

- Corrupted system files breaking the object manager's bookkeeping.

- Two security products installed at once, both hooking the same objects.

- Failing RAM corrupting the reference counts stored in memory.

- A corrupted driver installation mixing old and new driver files with different reference-counting behavior, confusing the object manager.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Identify the driver from the crash dump

This stop code is almost always one specific driver. The dump names it — read it before changing anything.

1. After rebooting, open **Event Viewer > Windows Logs > System** and find the **BugCheck** entry for any named **.sys** file.

2. For certainty, analyze the minidump with **WinDbg** — our [dump analysis guide](/articles/best-way-to-read-dump-files-with-windbg/) walks through `!analyze -v`.

3. Write down the driver name; every fix below targets it.

4. If dumps aren't being saved, enable minidumps in **Settings > System > About > Advanced system settings > Startup and Recovery**.

### Fix 2: Update or replace the named driver

A driver with a reference-count bug needs replacing, not tweaking. Get the manufacturer's current version.

1. Open **Device Manager** and find the device tied to the named driver.

2. Right-click, choose **Uninstall device**, and tick **Attempt to remove the driver for this device**.

3. Restart the laptop.

4. Install the latest driver from the manufacturer's official site — never from a driver-updater tool.

### Fix 3: Remove conflicting security software

Two antivirus products (or antivirus plus a 'system optimizer' with a driver) hooking the same kernel objects is a classic trigger for this stop code.

1. Open **Settings > Apps > Installed apps** and list every antivirus, firewall, VPN, and 'PC optimizer' installed.

2. Keep one antivirus; uninstall the rest using each vendor's official **removal tool** (normal uninstall leaves kernel drivers behind).

3. Restart and let **Windows Security** cover the gap during testing.

4. Reinstall only what you actually need, one at a time, testing stability between each.

### Fix 4: Run Driver Verifier on the suspect

If the dump is inconclusive, Driver Verifier can force the buggy driver to crash identifiably — but use it narrowly and carefully.

1. Press **Win + R**, type `verifier`, and choose **Create standard settings**.

2. Select **Select driver names from a list** and tick ONLY your suspect driver.

3. Restart and use the laptop; Verifier will crash it naming the violator if it's guilty.

4. Afterward, boot to Safe Mode and run `verifier /reset` to turn it off. Never leave Verifier on permanently.

### Fix 5: Repair system files

If the object manager's own files are corrupted, even good drivers crash against them. Repair the foundation.

1. Open **Terminal (Admin)** and run `sfc /scannow`.

2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.

3. Restart and test for a day or two.

4. Microsoft's documentation for both tools is on [their Windows support pages](https://support.microsoft.com/en-us/windows).

### Fix 6: Test the RAM

Corrupted reference counts in faulty memory mimic a driver bug perfectly. When dumps point everywhere, test the hardware.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.

2. For a thorough test, boot **MemTest86** from USB and run 2+ passes.

3. Replace any stick with errors.

4. If RAM is clean and one driver keeps getting named, that driver is definitively the problem — replace it and move on.

### Fix 7: Do an in-place upgrade repair

When driver replacements don't stick and the dumps keep implicating system components, an in-place upgrade reinstalls Windows over itself — rewriting the kernel and object-manager components this stop code is about — while keeping your files and programs.

1. Download the current Windows 11 ISO from the [official Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11).

2. Mount the ISO by double-clicking it and run **setup.exe**.

3. Choose **Keep personal files and apps** when asked.

4. Let setup complete — 30-90 minutes with several reboots; don't interrupt it.

5. Afterward, reinstall the suspect driver fresh from the manufacturer's site.

6. Monitor for a week. A clean kernel plus a clean driver ends the stubborn cases.

## Closing

REFERENCE_BY_POINTER is Windows catching a driver miscounting its references — annoying, but precise. Read the dump, name the driver, replace the driver; that three-step core fixes nearly every case. The traps to avoid are running two security products at once and trusting driver-updater tools, both of which manufacture exactly this kind of bug. Fix it once, properly, and this is one blue screen you won't see again. An in-place upgrade is the closest thing to a reinstall without the pain: it rewrites every Windows component while keeping your files and programs. When a driver replacement doesn't stick and dumps keep pointing at system components, this is the fix that ends it. Rare stop codes feel scarier than common ones, but they're often easier: fewer possible causes, and the dump usually names the culprit outright. You picked a good one to learn dump analysis on — the same !analyze -v workflow in our dump guide decodes the common stop codes too.
