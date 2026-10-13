---
title: "PAGE_FAULT_IN_NONPAGED_AREA: A Troubleshooter's Walkthrough"
slug: page-fault-in-nonpaged-area-troubleshooting
date: 2026-09-06
categories: ["windows-errors"]
tags: ["page-fault-in-nonpaged-area", "troubleshooting", "bsod"]
description: "Troubleshoot PAGE_FAULT_IN_NONPAGED_AREA methodically: read the dump, separate driver faults from RAM faults, and fix the real cause for good."
thumbnail: "/images/thumbs/page-fault-in-nonpaged-area-troubleshooting.webp"
faqs:
  - q: "What is the first thing to check for this stop code?"
    a: "Whether the blue screen named a driver file. A named .sys file means a specific driver faulted — chase that driver. No named file, or a different file every crash, means suspect the RAM or drive first. That single observation splits the entire troubleshooting tree."
  - q: "How do I read a minidump for PAGE_FAULT_IN_NONPAGED_AREA?"
    a: "Install WinDbg Preview from the Microsoft Store, open the newest dump in C:\\Windows\\Minidump, and run !analyze -v. For 0x50, the faulting address and IMAGE_NAME matter most — they tell you which driver touched the bad address and what it was doing."
  - q: "Why do the dumps name a different driver every time?"
    a: "Because the real fault is underneath the drivers — almost always bad RAM or a failing drive corrupting whatever happens to be in memory. Each crash catches a different innocent driver holding corrupted data. Stop chasing drivers and test the hardware."
  - q: "Can paging file settings cause this error?"
    a: "A corrupted pagefile.sys can, yes — data swapped out comes back wrong and faults when referenced. Deleting and recreating the page file (via System Properties > Performance > Virtual memory) is a legitimate troubleshooting step, though it is rarely the whole story."
---
Troubleshooting PAGE_FAULT_IN_NONPAGED_AREA (stop code 0x50) well means doing diagnosis before repair. This crash has three distinct families of causes — bad drivers, bad RAM, bad drives — and the fix for one does nothing for the others. Guessing wastes days. Troubleshooting PAGE_FAULT_IN_NONPAGED_AREA (stop code 0x50) well means doing diagnosis before repair. This crash has three distinct families of causes — bad drivers, bad RAM, bad drives — and the fix for one does nothing for the others. Guessing wastes days.

This walkthrough is the diagnostic sequence: gather evidence from the dumps, classify the fault, then apply the fix that matches. Every step narrows the field. This walkthrough is the diagnostic sequence: gather evidence from the dumps, classify the fault, then apply the fix that matches. Every step narrows the field.

## Why this happens

- **A driver touching invalid memory.** The classic software cause — the dump usually names it.
- **Failing RAM.** Corrupts data structures so that valid addresses hold garbage.
- **A dying drive.** Returns corrupted data that faults when the memory manager references it.
- **Corrupted page file.** Swapped-out data returns damaged and trips the fault on read-back.
- **Antivirus filter drivers.** Their deep hooks make their bugs surface as page faults in innocent processes.
- **Faulty RAM timings.** XMP profiles that are not quite stable fault intermittently under load.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Classify the fault from the blue screen and dumps

Diagnosis first: the pattern decides the entire repair path. Diagnosis first: the pattern decides the entire repair path — same driver means software, scattered drivers mean hardware.

1. Write down any `.sys` file named on the blue screen (disable auto-restart via our [auto-restart guide](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/) if it vanishes too fast).
2. Open the last three dumps in `C:\Windows\Minidump` with WinDbg Preview, running `!analyze -v` on each.
3. Same driver in all three: driver fault — go to Fix 2. Different drivers each time, or no driver: hardware fault — go to Fix 3.

### Fix 2: Fix the driver fault

For the consistent-single-driver pattern. For the consistent-single-driver pattern — update it, roll it back if recently updated, or remove the product that installed it.

1. Update the named driver from the manufacturer's website — graphics, storage, and network drivers first.
2. If it was recently updated, roll back: **Device Manager > Properties > Driver > Roll Back Driver**.
3. For filter drivers (antivirus, VPN), clean-reinstall the product or uninstall to test.
4. Verify by reproducing the original crash scenario; one driver change at a time.

### Fix 3: Test the RAM thoroughly

For the inconsistent-dump pattern — this is the definitive hardware check. For the inconsistent-dump pattern — the quick test screens, the overnight MemTest86 test convicts, and one error is enough.

1. Run `mdsched.exe` > **Restart now and check for problems**.
2. If clean but suspicion remains, run MemTest86 overnight for at least 4 passes.
3. Test sticks individually to isolate the bad one. On soldered-RAM ultrabooks, a failure here means a warranty or board-level repair — document the MemTest86 errors with photos.

### Fix 4: Check the drive and rebuild the page file

The second hardware suspect, plus the page-file wildcard. The second hardware suspect, plus the page-file wildcard — rebuild the page file while you are here, since it is harmless and occasionally the whole cause.

1. Run `chkdsk C: /f /r` from an elevated prompt and reboot for the full scan.
2. Check `wmic diskdrive get status` and the maker's SMART toolbox.
3. Rebuild the page file: `sysdm.cpl` > **Advanced > Performance Settings > Advanced > Virtual memory > Change** — set **No paging file**, reboot, re-enable **Automatically manage**, reboot again.
4. If chkdsk finds growing bad sectors, prioritize replacing the drive over further software troubleshooting.

### Fix 5: Eliminate filter-driver suspects with a clean boot

Catches the antivirus/VPN filter drivers that dumps sometimes miss. Catches the antivirus and VPN filter drivers that dumps sometimes miss — clean boot isolates them by elimination.

1. Run `msconfig`, tick **Hide all Microsoft services**, **Disable all**.
2. Disable all startup items in Task Manager and restart.
3. If stable, re-enable in halves. Filter drivers that corrupt memory reveal themselves here when dumps are ambiguous.

### Fix 6: Repair Windows' own files

The final software sweep — [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) has more on the built-in repair tools used here. The final software sweep — and give intermittent 0x50 faults a longer observation window than most crashes before declaring victory.

1. Elevated prompt: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Restart and monitor for several days — intermittent 0x50 faults need a longer observation window than most crashes.
3. If the faulting module was a Windows driver and SFC repaired it, you are likely done. Our [IRQL troubleshooting guide](/articles/irql-not-less-or-equal-windows-11-fix/) covers the closely related driver-fault stop code.

### Fix 7: Test with one RAM stick at a time

When MemTest86 shows errors but you have two sticks, this identifies which one is bad so you replace one, not both.

1. Power off, unplug, and remove one RAM stick (ground yourself first; check your manual for access).
2. Run MemTest86 or the Windows diagnostic on the remaining stick alone.
3. Swap and repeat — the stick that errors alone is the bad one.
4. Also test the suspect stick in the other slot: errors that follow the slot, not the stick, mean a bad motherboard slot.

## Closing

The troubleshooter's edge on PAGE_FAULT_IN_NONPAGED_AREA is classification: three dumps tell you whether you are hunting a driver or hunting hardware, and everything after that is execution. Diagnose first, fix second, and this stop code resolves in hours instead of weeks. Classification is a habit, not just a step — apply the same 'what does the pattern say' discipline to every blue screen and your troubleshooting time will collapse.
