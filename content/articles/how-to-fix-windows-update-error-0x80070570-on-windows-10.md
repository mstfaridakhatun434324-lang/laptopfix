---
title: "Fix Windows Update Error 0x80070570 on Windows 10: Replace the Bad Files"
slug: how-to-fix-windows-update-error-0x80070570-on-windows-10
date: 2026-09-07
categories: ["windows-update"]
tags: ["windows update", "0x80070570", "windows 10", "corrupt files", "chkdsk"]
description: "Windows 10 error 0x80070570 flags damaged update files. Clear the corrupt cache, verify disk and memory, and install cleanly with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070570-on-windows-10.webp"
faqs:
  - q: "What causes error 0x80070570 on Windows 10?"
    a: "A file needed by the update is corrupt or unreadable. The damage can come from a bad download, a poisoned local update cache, bad disk sectors, faulty RAM, or an interrupted write from an earlier crashed update. The repair order in this guide follows that exact list of suspects."
  - q: "Why do I get 0x80070570 on different updates each time?"
    a: "Different updates failing with the same corruption code points below the software layer — at the disk or RAM corrupting whatever passes through. Run chkdsk and the memory diagnostic promptly instead of retrying updates. One failing update is a download problem; many is a hardware problem."
  - q: "Will Disk Cleanup fix 0x80070570?"
    a: "It can help: removing old update files and temporary data clears some corruption reservoirs and frees the space updates need. But it does not repair bad sectors or bad RAM, so treat it as a first step, not the whole fix."
  - q: "How do I know if my hard drive is dying?"
    a: "Repeated corruption errors, chkdsk reporting bad sectors, SMART warnings, and unusual noises (on spinning drives) are the classic signs. Back up immediately if several appear together. For the companion symptom of updates failing to install at all, see our [driver update failure guide](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/)."
---

Windows 10 meets error 0x80070570 the same way every time: an update downloads, the installer starts its integrity checks, and one file fails — corrupt, unreadable, unusable. The installer stops rather than build your system on damaged goods, which is the right call. Your job is to figure out where the damage entered the picture, because the same code covers four very different problems.

The investigation runs from the most likely to the most serious. First, the download and the cache — the everyday sources of corrupt files. Then the filesystem and the disk surface, where bad sectors silently damage whatever lands on them. Finally RAM, the invisible corruptor that damages data in flight. Each layer has a definitive test, so you will know rather than guess.

One rule for the whole repair: stop retrying the same update from the same cache. It cannot succeed until the corrupt source is gone.

## Why this happens

- **Bad transfer**: Network damage to the downloaded package.
- **Poisoned cache**: Corrupt files in SoftwareDistribution reused by every retry.
- **Bad sectors**: Dying disk areas damaging written files.
- **RAM faults**: Bit flips during processing corrupting good data.
- **Interrupted previous update**: Half-written files from a crashed earlier install.
- **Low disk space**: Filesystem unable to place large update files cleanly.
- **Filesystem corruption**: Logical errors making intact files unreadable.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run Disk Cleanup as administrator

Start by clearing the known reservoirs of damaged update debris and making room. It is quick, safe, and occasionally sufficient on its own when the corruption was a one-off.

1. Search Disk Cleanup, right-click it, and choose Run as administrator.
2. Select C:, then tick Temporary files, Windows Update Cleanup, Previous Windows installations, and Delivery Optimization Files.
3. Click OK and let it finish — this can take several minutes.
4. Restart the laptop before retrying the update.

### Fix 2: Empty the download cache manually

Disk Cleanup does not always reach everything. Manually emptying the download folder guarantees no damaged fragment survives to poison the next attempt.

1. In an elevated Command Prompt, run net stop wuauserv and net stop bits.
2. Delete all contents of C:\Windows\SoftwareDistribution\Download.
3. Run net start wuauserv and net start bits.
4. Check for updates and let it download completely fresh.

### Fix 3: Repair the component store and system files

Corruption in the on-disk Windows image makes every update's integrity checks fail. DISM restores the store, SFC repairs files against it — the standard one-two for file-level damage.

1. Run DISM /Online /Cleanup-Image /RestoreHealth in an elevated Command Prompt.
2. When finished, run sfc /scannow.
3. Reboot after both complete.
4. Retry the update on the repaired baseline.

### Fix 4: Scan the disk surface with chkdsk

This is the definitive test for the bad-sector hypothesis. The /r flag finds weak sectors, recovers readable data, and marks them unusable so nothing important lands there again.

1. In an elevated Command Prompt, run chkdsk C: /f /r and approve the reboot scan.
2. Restart and let it run to completion — large drives can take over an hour.
3. Read the final summary carefully for bad sector counts.
4. A handful is wear; dozens is a dying drive — back up and replace before continuing updates.

### Fix 5: Test system memory

If the disk is clean but corruption persists, RAM is next. Faulty memory corrupts data silently during the exact operations updates perform, and the built-in tester catches most faults.

1. Press Windows + R, type mdsched.exe, and press Enter.
2. Select Restart now and check for problems, and let the standard test finish.
3. If errors appear, power down, reseat the memory modules, and retest.
4. On laptops with soldered RAM showing errors, contact the manufacturer — the board needs service.

### Fix 6: Install from the Update Catalog manually

Bypassing the automated pipeline with a manual install from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) isolates whether the corruption lives in the download path or deeper in the system.

1. Note the failing update's KB number from Update history.
2. Download the x64 .msu package from the Update Catalog.
3. Install it directly and reboot as prompted.
4. If the manual package also fails integrity checks, the disk or RAM findings above are confirmed — act on them.

### Fix 7: Refresh the installation if corruption is systemic

When SFC cannot repair files, chkdsk keeps finding damage, or corruption appears in daily use beyond updates, the installation itself is compromised. A repair install rebuilds it while keeping your files.

1. Back up your important files first — systemic corruption is exactly when backups matter most.
2. Download the Windows 10 ISO from Microsoft, mount it, and run setup.exe.
3. Choose Keep personal files and apps.
4. After the refresh, verify with one more SFC scan, then update normally. Microsoft's [support hub](https://support.microsoft.com/en-us/windows) has the full clean-install procedure if the refresh is not enough.

### Fix 8: Verify drive health and keep it cool

Recurring corruption puts the drive itself under suspicion, and drives deserve two kinds of care: a health verdict from SMART data, and thermal kindness during heavy workloads. This fix covers both, because a hot, deteriorating drive corrupts more than a cool, healthy one.

1. Download your SSD or HDD maker's health utility and review the overall SMART status, focusing on reallocated and pending sector counts.
2. Any caution or failure status means back up immediately and plan replacement — do not trust important files to a flagged drive.
3. For the update session, place the laptop on a hard, flat surface with vents unobstructed and the rear slightly elevated.
4. Close heavy applications so the CPU and SSD share less heat, then retry the update in the cooler conditions.

## Closing

Windows 10's 0x80070570 always means the same thing — damaged files — but the fix depends on the layer: cache, disk, or memory. Clear the cache first because it is fast, test the disk and RAM because they matter, and take recurring corruption seriously as a hardware warning. An update error is an annoyance; the failing drive behind it is an emergency. Tell them apart with the tests above, and act accordingly. Related: the [Windows 11 0x80070570 guide](/articles/how-to-fix-windows-update-error-0x80070570-on-windows-11/) and our [driver update failure guide](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) for corruption isolated to driver packages.
