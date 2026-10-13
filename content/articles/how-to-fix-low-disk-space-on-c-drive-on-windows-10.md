---
title: "C: Drive Full on Windows 10? Reclaim Your Disk Space"
slug: how-to-fix-low-disk-space-on-c-drive-on-windows-10
date: 2026-09-27
categories: ["performance"]
tags: ["low disk space c drive", "windows 10 disk cleanup", "free up disk space", "c drive full"]
description: "Running out of space on C: in Windows 10? Find what's eating your disk and reclaim gigabytes with Disk Cleanup, Storage Sense, and safe manual trims."
thumbnail: "/images/thumbs/how-to-fix-low-disk-space-on-c-drive-on-windows-10.webp"
faqs:
  - q: "How much free space should I keep on my C: drive?"
    a: "Aim for at least 15-20% of the drive free, or a minimum of 20-30 GB on typical laptop SSDs. Below about 10% free, Windows can't defragment properly, updates may fail, virtual memory gets constrained, and SSD performance and lifespan both suffer. If you're under 10 GB free, treat it as urgent and work through the cleanup steps immediately."
  - q: "Is it safe to delete files in the Windows folder to free space?"
    a: "Generally no — don't hand-delete anything inside C:\\Windows. The safe exceptions are handled by built-in tools: Disk Cleanup's Windows Update Cleanup and Delivery Optimization Files options, which remove exactly the safe leftovers. Manual deletion in WinSxS or System32 can break updates or the whole OS. Use the tools; they're designed for this."
  - q: "Will Storage Sense delete my personal files?"
    a: "No. Storage Sense only removes categories you explicitly enable: temporary files, Recycle Bin contents older than your chosen age, and Downloads folder files older than your chosen age (off by default). It never touches Documents, Pictures, or Desktop unless you've moved them into OneDrive with Files On-Demand. Review its settings once so you know exactly what it cleans."
  - q: "Why does my C: drive keep filling up after I clean it?"
    a: "Something is actively writing: Windows Update downloading feature updates, a runaway log file from a crashing app, System Restore points accumulating, or hibernation and page files sized to your RAM. If space vanishes within days of a cleanup, check the largest folders with a disk analyzer and look for constantly-growing files — that's your culprit, and deleting without fixing it just repeats the cycle."
---

The red bar in File Explorer. The 'Low Disk Space' warnings. Updates failing with cryptic errors. A full C: drive on Windows 10 isn't just annoying — it slows the whole system down, because Windows needs free space for virtual memory, temporary files, and update staging. The fix isn't buying a bigger drive (yet); it's finding what's actually consuming the space and removing what's safe.

Windows 10 gives you solid built-in tools for this: Disk Cleanup with its system-files mode, Storage Sense for ongoing maintenance, and a few manual trims that reclaim gigabytes in minutes. The key is knowing what's safe to delete versus what just looks deletable. If disk pressure is part of broader slowness, [freeing up disk space on Windows 11](/articles/how-to-free-up-disk-space-on-windows-11/) covers the newer OS with transferable ideas, and [low disk space after the Windows 11 update](/articles/how-to-fix-low-disk-space-on-c-drive-after-windows-11-update/) tackles update leftovers specifically.

Work through these in order — the early fixes are the big wins, and the later ones are for stubborn cases.

## Why this happens

- **Windows Update leftovers**: Every feature update keeps a Windows.old folder and gigabytes of update backups so you can roll back — useful for ten days, dead weight after.
- **Temporary files piling up**: App installers, update staging, and crash dumps accumulate in Temp folders that nothing cleans automatically on Windows 10 by default.
- **Hibernation file**: hiberfil.sys reserves disk space equal to a large fraction of your RAM — on a 16 GB laptop, that's 6-12 GB sitting idle.
- **System Restore points**: Each restore point can be several GB, and Windows 10 keeps creating them before updates and installs.
- **Oversized Recycle Bin**: Deleted files aren't gone until the bin is emptied — large video projects and installers can sit there for months.
- **Downloads folder bloat**: Years of installers, ISOs, and attachments that were needed exactly once and never again.
- **App bloat and caches**: Unused programs, old game installs, and browser caches quietly consume tens of gigabytes.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run Disk Cleanup with system files

The single biggest win. The system-files mode unlocks Windows Update Cleanup and other categories the basic mode hides.

1. Press Win + R, type cleanmgr, press Enter, and select C:.
2. Click Clean up system files, select C: again, and wait for the scan.
3. Check Windows Update Cleanup, Delivery Optimization Files, Temporary files, and Recycle Bin.
4. Click OK, confirm, and let it run — this alone often frees 10-30 GB after a feature update.

### Fix 2: Delete the Windows.old folder

If you upgraded Windows 10 versions recently, this folder is a full copy of your old install — often 20+ GB.

1. Open Settings, System, Storage, then Temporary files.
2. Check Previous version of Windows and click Remove files.
3. Alternatively, Disk Cleanup's system-files mode lists it as Previous Windows installation(s).
4. Only do this once you're sure the new version works — deleting it removes the 10-day rollback option.

### Fix 3: Enable Storage Sense for ongoing cleanup

Storage Sense automates the boring part so the drive doesn't fill up again.

1. Open Settings, System, Storage, and turn on Storage Sense.
2. Click Configure Storage Sense and set it to run weekly.
3. Enable deletion of temporary files and set Recycle Bin cleanup to 30 days.
4. Leave Downloads folder cleanup off unless you're certain — that's the one that can surprise you.

### Fix 4: Shrink or disable hibernation

If you never hibernate (most laptop users just use Sleep), the hibernation file is pure overhead.

1. Open an admin Command Prompt (right-click Start, Command Prompt (Admin) or Windows PowerShell (Admin)).
2. Run powercfg /hibernate off to delete hiberfil.sys immediately.
3. Verify the space is back in File Explorer.
4. Re-enable anytime with powercfg /hibernate on if you miss the hibernate option.

### Fix 5: Trim restore points and move user folders

Restore points and user data are the two quietest space hogs.

1. Press Win + R, type sysdm.cpl, go to System Protection, select C:, and click Configure.
2. Lower Max Usage to 5% or delete all but the latest restore point.
3. For bulky libraries, right-click Documents or Pictures, Properties, Location tab, and move them to a D: partition or external drive.
4. Microsoft documents storage management at [Microsoft's Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 6: Uninstall what you don't use

Programs you installed in 2021 and forgot are still occupying real gigabytes.

1. Open Settings, Apps, Apps & features, and sort by Size.
2. Uninstall anything you don't recognize or haven't opened in a year — trial software, old toolbars, duplicate utilities.
3. Check for multiple versions of the same runtime or large games you finished.
4. Restart after bulk uninstalls so pending cleanup completes.

### Fix 7: Find the mystery hogs with a disk analyzer

When the big wins aren't enough, visualize the drive to find what's really eating it.

1. Install a free treemap analyzer like WinDirStat or WizTree (WizTree is dramatically faster on big drives).
2. Scan C: and look at the largest rectangles — often a single forgotten folder.
3. Common surprises: old phone backups, virtual machine disks, video render caches, and log files from a crashing service.
4. Delete or relocate what you identify, then re-scan to confirm the space is truly freed.

### Fix 8: Compact the OS and relocate the pagefile

Two advanced reclaims for when the standard cleanup isn't enough: Windows' built-in CompactOS compression and moving the pagefile off C:.

1. Open an admin Command Prompt and run compact.exe /CompactOS:always to compress Windows system files — typically saves 2-4 GB with negligible performance cost on modern CPUs.
2. To move the pagefile: press Win + R, type sysdm.cpl, go to Advanced, Performance Settings, Advanced tab, Virtual memory, Change.
3. Uncheck Automatically manage, select C:, choose No paging file, then select your D: drive (or another partition) and set System managed size.
4. Click Set, OK, and restart. This frees RAM-sized gigabytes from C: — on 16 GB systems, that's often 2-16 GB.
5. Only do this if you have a second partition or drive; never disable the pagefile entirely.

## Closing

A full C: drive on Windows 10 is almost always fixable without new hardware — update leftovers, temp files, and hibernation data account for the bulk of it on most laptops. Run Disk Cleanup in system-files mode first, turn on Storage Sense so it stays clean, and use a disk analyzer for whatever remains. Keep 15-20% free going forward and Windows will thank you with fewer failed updates and a snappier system.
