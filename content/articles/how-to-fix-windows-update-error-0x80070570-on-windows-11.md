---
title: "Windows 11 Error 0x80070570: Fix the Corrupt Update Files"
slug: how-to-fix-windows-update-error-0x80070570-on-windows-11
date: 2026-09-06
categories: ["windows-update"]
tags: ["windows update", "0x80070570", "windows 11", "file corrupt", "corrupt files"]
description: "Error 0x80070570 means update files arrived damaged or unreadable. Trace the corruption to its source — cache, disk, or memory — and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070570-on-windows-11.webp"
faqs:
  - q: "What does Windows Update error 0x80070570 mean?"
    a: "It is the file-corrupt error: a file the update needed was damaged or unreadable. The corruption can originate in the download (bad transfer), in the local cache, on the disk itself (bad sectors), or even in RAM flipping bits during the operation."
  - q: "Why does 0x80070570 keep coming back after I retry?"
    a: "Because retrying reuses the same corrupt source. If the damage is in the local cache, every retry reads the same bad files; if it is on the disk or in RAM, every new download gets corrupted the same way. You must clear the cache and then test the hardware."
  - q: "Can bad RAM really cause update errors?"
    a: "Yes. Memory errors corrupt data as it is written, so downloads and extracted files end up damaged with no network fault involved. If multiple different updates fail with corruption codes, RAM is a prime suspect worth testing. Run the memory diagnostic before buying any replacement hardware."
  - q: "Should I worry about my SSD if I see this error?"
    a: "A single occurrence after a bad download is usually innocent. Repeated 0x80070570 errors across different updates, especially with chkdsk finding bad sectors, point at a failing drive — back up promptly. If a stuck rollback accompanied it, see our [undoing changes guide](/articles/best-way-to-fix-undoing-changes-made-to-your-computer-stuck/)."
---

Error 0x80070570 is Windows 11's file-corrupt verdict: somewhere between Microsoft's servers and your disk, a file the update needed arrived damaged — or was damaged after arrival. The update engine verifies what it downloads, finds the damage, and refuses to install rather than risk a broken system. That refusal is correct behavior; the repair is finding where the damage happens.

Corruption has exactly four usual sources, and the fix depends entirely on which one you have. A bad download corrupts in transit. A bad cache corrupts at rest on your disk. Bad sectors corrupt everything written to one spot. Bad RAM corrupts everything, everywhere, intermittently. The steps below eliminate them in that order — cheapest to check first — so you stop treating the symptom and start treating the cause.

Do not just keep retrying. Each retry from the same corrupt cache fails identically, and each retry onto a failing drive risks more damage.

## Why this happens

- **Corrupt download**: Transfer damage producing files that fail integrity checks.
- **Damaged update cache**: Corruption in SoftwareDistribution persisting across retries.
- **Bad disk sectors**: Failing storage damaging files written to weak areas.
- **Faulty RAM**: Memory errors flipping bits during download, extraction, or install.
- **Interrupted writes**: Power loss or crashes during a previous update leaving half-written files.
- **Overheating storage**: Thermal throttling and errors on hot NVMe drives during long updates.
- **Filesystem damage**: Logical corruption making good files unreadable.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Purge the corrupt cache completely

The cache is the most common corruption reservoir: one bad download poisons it, and every retry then reads the same damaged files. A full purge forces everything to be fetched fresh.

1. Open an elevated Command Prompt.
2. Run net stop wuauserv, net stop cryptSvc, net stop bits, and net stop msiserver.
3. Delete the entire contents of C:\Windows\SoftwareDistribution\Download.
4. Restart the four services, reboot, and retry the update from a clean slate.

### Fix 2: Run SFC and DISM to repair system files

If the corruption extends to files already on the system, the update's integrity checks will keep failing no matter how clean the new downloads are. These tools repair the on-disk baseline.

1. In an elevated Command Prompt, run DISM /Online /Cleanup-Image /RestoreHealth.
2. Follow with sfc /scannow and let it complete.
3. Reboot the laptop.
4. Retry the update — the repaired baseline may be all it needed.

### Fix 3: Check the disk with chkdsk

Bad sectors are a hardware source of exactly this error: files written to dying areas come back damaged. Chkdsk finds and quarantines them, and its report tells you whether the drive is merely bruised or actually failing.

1. In an elevated Command Prompt, run chkdsk C: /f /r and confirm the scan at next reboot.
2. Restart and let the full scan run — it can take an hour or more on large drives.
3. Review the summary: a few repaired sectors is fine; many bad sectors means replace the drive soon.
4. Retry updates only after the scan completes.

### Fix 4: Test the memory

RAM errors are the sneaky cause: they corrupt data invisibly, so downloads, extractions, and installs all produce damaged files with no disk or network fault. Windows includes a memory tester for exactly this.

1. Press Windows + R, type mdsched.exe, and press Enter.
2. Choose Restart now and check for problems.
3. Let the full test complete — do not skip it short.
4. If errors are reported, reseat the RAM (or have it serviced on soldered-memory ultrabooks) and retest before updating.

### Fix 5: Free space and cool the drive

Updates on nearly-full or overheating drives corrupt more often: the filesystem struggles to place large files, and hot NAND makes more errors. Both are easy to improve.

1. Ensure at least 20 GB free on C: using Disk Cleanup as administrator.
2. During the update, keep the laptop on a hard flat surface with vents clear — not on a bed or couch.
3. If the laptop runs hot, point a fan at it or use a cooling stand for the update session.
4. Retry the update in the cooler, roomier conditions.

### Fix 6: Install the update manually from the catalog

A manual install from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) bypasses the damaged automated pipeline: you download the package with the browser and install it directly, sidestepping cache and transfer quirks.

1. Find the KB number in Update history.
2. Download the x64 .msu from the Update Catalog.
3. Run the installer and reboot when prompted.
4. If the manual install also reports corruption, the hardware tests above become urgent — the problem is below the software layer.

### Fix 7: Check drive health with the manufacturer tool

When corruption recurs across different updates, get a professional verdict on the drive. Manufacturer diagnostics read the SMART data that chkdsk cannot fully interpret.

1. Boot into your manufacturer's diagnostics (F12 on Dell, F2 on HP, F10/F12 on Lenovo) and run the storage test.
2. Alternatively, check SMART status with the drive maker's Windows utility.
3. If the drive is failing, back up immediately and replace it before doing anything else — no update is worth risking your data.
4. After replacement, reinstall Windows fresh rather than cloning a corrupt system; Microsoft's [support hub](https://support.microsoft.com/en-us/windows) covers clean installation.

### Fix 8: Read the drive's SMART health data

When corruption recurs, ask the drive itself how it feels. SMART attributes — reallocated sectors, uncorrectable errors, wear leveling counts — reveal deterioration long before total failure, and the manufacturer's free utility reads them in plain language.

1. Install your SSD or HDD maker's diagnostic utility.
2. Review the health status, focusing on reallocated and pending sector counts.
3. Any caution or failure status means back up now and replace the drive — no update is worth risking data.
4. After replacing, clean-install Windows rather than cloning, so no corruption carries over.
## Closing

Error 0x80070570 is a corruption story, and corruption stories end when you find the source: bad download, bad cache, bad sectors, or bad RAM. The cache purge fixes the common case in minutes; the disk and memory tests protect you in the serious ones. Whatever you do, do not normalize recurring corruption errors — a drive or RAM stick that corrupts updates today corrupts your documents tomorrow. Related: the [Windows 10 0x80070570 guide](/articles/how-to-fix-windows-update-error-0x80070570-on-windows-10/) and our [undoing changes stuck guide](/articles/best-way-to-fix-undoing-changes-made-to-your-computer-stuck/) if corruption came with a stuck rollback.
