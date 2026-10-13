---
title: "How to Fix Windows Update Error 0x80070570 on a Lenovo Laptop"
slug: "how-to-fix-windows-update-error-0x80070570-on-lenovo-laptop"
date: 2026-09-05
categories: ["windows-update"]
tags: ["error 0x80070570", "windows update", "lenovo laptop", "file corrupt", "windows 11"]
description: "Error 0x80070570 on a Lenovo laptop means corrupted files — possibly a failing disk or RAM. Seven fixes, from cache resets and chkdsk to memory testing."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070570-on-lenovo-laptop.webp"
faqs:
  - q: "What does error 0x80070570 mean?"
    a: "It means ERROR_FILE_CORRUPT: a file Windows Update needs is damaged and unreadable. The damage can enter at any point in the chain — a bad download, a corrupted cache, file system damage, or failing hardware corrupting data during writes or transfers. One occurrence usually means a bad download; recurrence across different updates strongly suggests the disk or RAM is failing and needs testing."
  - q: "How do I know if it is the disk or the RAM?"
    a: "Run both tests — each is quick and conclusive. chkdsk /f /r finds bad sectors and file system damage; the Windows Memory Diagnostic, mdsched.exe, finds faulty RAM. Bad sectors reported by chkdsk make the drive the prime suspect, while memory errors point at RAM corrupting data in transit. Both can coexist on aging laptops, so do not stop after the first positive result."
  - q: "Should I back up my data immediately?"
    a: "Yes — right now, before any further troubleshooting, if you have not already. Recurring 0x80070570 is one of the classic early warnings of drive failure, and drives can slide from occasional corruption to unreadable quickly. Copy irreplaceable files to external storage or a cloud backup first, then run diagnostics knowing your data is safe whatever they find."
  - q: "Can overheating cause file corruption?"
    a: "Indirectly, yes. Sustained heat can make storage controllers and memory error under load — exactly the conditions of a large update installing inside a poorly ventilated laptop. If corruption appears only during heavy operations and the machine runs hot, improve cooling by cleaning the vents, using a stand, and avoiding soft surfaces, then see whether the errors stop before condemning the hardware."
---

Error 0x80070570 means "the file or directory is corrupted and unreadable." Windows Update found its materials structurally damaged — not merely mismatched, but broken. On a Lenovo laptop the range runs from a single bad download to the early warning of a failing drive or faulty RAM.

Treat this error with respect when it repeats: one corrupted download is bad luck, but recurring corruption across different updates is the hardware speaking. If a single operation was cancelled rather than corrupted, the [0x800704C7 cancelled-operation guide](/articles/how-to-fix-windows-update-error-0x800704c7-on-lenovo-laptop/) covers that different code.

The inspection below climbs deliberately from software to hardware. Clear the bad material first; if corruption returns, the disk and memory tests at the end identify the real structural fault.

## Why this happens

- **A drive reaching the end of its life:** Dying storage corrupts whatever it touches, and large, numerous update payloads are the canaries for drive failure.
- **Faulty RAM:** Bad memory corrupts data in transit — downloads arrive intact and are damaged before they ever reach the disk.
- **A single bad download:** One corrupt transfer can produce this error once, with no hardware involvement at all.
- **File system damage:** A damaged NTFS structure makes healthy files unreadable, raising corruption errors for data that is actually fine.
- **An overheating storage controller:** Thermal stress in a cramped laptop chassis can cause write errors under the sustained load of a large update.
- **Unstable overclock or undervolt:** Aggressive tuning on Legion machines can introduce the bit-errors that corrupt files during writes.
- **Power loss mid-write:** Battery depletion or forced shutdowns during writes leave files half-written and unreadable.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Demolish and rebuild the update working folders

The cache may be holding the very corrupted copies that keep failing validation. Services stopped and folders renamed, Windows regenerates the pair untouched by the old corruption. The fresh copies arrive with sound permissions and an empty pending queue.

1. Fire up an elevated Command Prompt (use right-click on Start, then Terminal (Admin)).
2. Stop all four services: net stop wuauserv, net stop cryptSvc, net stop bits, net stop msiserver.
3. Swap in new names for the two folders: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Bring the services back with net start, then scan for updates again.

### Fix 2: Load-test the drive with chkdsk

When files keep arriving corrupted, inspect the foundation they are written to. Bad sectors damage data as it lands on the platters or flash, and the symptom is indistinguishable from mysterious file corruption. A full scan maps out the defective regions and moves data off them, stopping the corruption at its source. Run chkdsk with /r whenever corruption recurs — Microsoft's [official Windows support hub](https://support.microsoft.com/en-us/windows) recommends it for exactly this pattern.

1. Open an elevated Command Prompt.
2. Start chkdsk C: /f /r and confirm it for the next restart.
3. Restart and let the scan finish completely — large drives may take an hour.
4. Retry the update after the disk check comes back clean.

### Fix 3: Stress-test the memory with Windows Memory Diagnostic

Faulty RAM corrupts data in transit, and update packages are large enough that a marginal memory module will damage them during download or extraction. When corruption errors keep recurring across different updates, the memory — not the network — is the likely culprit. The Windows Memory Diagnostic catches the RAM faults hiding behind mysterious repeated corruption.

1. Open the Run dialog with Win + R, enter mdsched.exe, and press Enter.
2. Select Restart now and check for problems.
3. Let the full test run to completion and note any errors it reports.
4. When errors show up, reseat or replace the bad memory module before updating.

### Fix 4: Inspect protected system files with SFC

Corrupted Windows system files can undermine the update installer in subtle ways, and the System File Checker exists to find and replace them. It audits every protected file against its known-good original and repairs the casualties — wiping out a whole category of installer failures in one pass.

1. Open an admin-level Command Prompt or Terminal.
2. Launch sfc /scannow from the prompt and let the scan run through.
3. If the scan reports repaired files, restart the laptop.
4. Attempt the update install again after restarting.

### Fix 5: Install the package directly from the Update Catalog

Even on healthy hardware, the automatic delivery path can stay broken. Fetching the failing update as a standalone .msu bypasses the entire pipeline — a detour that often succeeds where Windows Update keeps stalling, and a clean manual install proves the delivery path was the problem.

1. Get the KB number of the failing update from Settings, Windows Update, then Update history.
2. Search the Microsoft Update Catalog for that KB number and open the match.
3. Choose the x64 file for the current Windows 11 build.
4. Open the .msu, run the installer to the end, and restart when prompted.

### Fix 6: Rebuild the component store with DISM

The WinSxS store is the materials library the installer draws from, and a damaged index makes updates fail even when every visible file looks fine. DISM's RestoreHealth audits the store against healthy online sources and repairs the damage that SFC cannot reach on its own.

1. Open an elevated Command Prompt.
2. Kick off DISM /Online /Cleanup-Image /RestoreHealth and wait it out — the run takes 15 to 30 minutes.
3. Once it wraps up, run sfc /scannow again to mop up.
4. Restart and try the update again.

### Fix 7: Rebuild the structure with an in-place upgrade

If every inspection passes and corruption still returns, rebuild the entire structure. An in-place upgrade reinstalls Windows around the files and apps, installing fresh copies of every system file, service, and update component — resolving deep corruption that no individual tool could reach. Back up first either way; repairs are safe, not risk-free.

1. Grab the Windows 11 media creation tool via Microsoft's official page.
2. Fire up the tool, choose Upgrade this PC now, and keep your personal files and apps.
3. Let the installer run to completion through its several restarts.
4. When setup ends, run Windows Update once for anything newer than the repair image.

## Closing

0x80070570 demands respect: fix the software causes quickly, but believe the hardware tests when corruption keeps coming back. A drive or RAM module caught early by this error is a data-loss disaster prevented — replace failing hardware before it takes the files with it. If the corruption signature is specifically CRC failures, the [0x80070017 CRC-error guide](/articles/how-to-fix-windows-update-error-0x80070017-on-lenovo-laptop/) dives deeper.
