---
title: "Low Disk Space on C: Drive? Free It Up (ASUS Laptop Guide)"
slug: how-to-fix-low-disk-space-on-c-drive-on-asus-laptop
date: 2026-09-06
categories: ["performance"]
tags: ["low disk space c drive", "asus laptop", "free up disk space", "c drive full"]
description: "C: drive almost full on your ASUS laptop? Find what's eating the space and reclaim gigabytes safely with this step-by-step cleanup guide."
thumbnail: "/images/thumbs/how-to-fix-low-disk-space-on-c-drive-on-asus-laptop.webp"
faqs:
  - q: "How much free space should I keep on my C: drive?"
    a: "Aim for at least 15-20% of the drive free, with an absolute minimum of 15-20GB on typical 256-512GB laptop SSDs. Below that threshold, Windows cannot stage updates, the page file cannot grow, search indexing degrades, and SSD performance itself drops because the controller lacks free blocks for wear leveling. The red bar in File Explorer is not just a warning color — it marks the point where Windows behavior genuinely degrades."
  - q: "Is it safe to delete files from the Windows folder to free space?"
    a: "No — never manually delete files from C:\\Windows. It is tempting because the folder is huge, but deleting the wrong file breaks Windows or future updates. The safe tools are Disk Cleanup (including Clean up system files), Storage Sense, and the Settings > System > Storage > Temporary files page, which know exactly which Windows files are safe to remove (old update backups, delivery optimization files, previous installations). Let the official tools do the surgery."
  - q: "Why does my C: drive fill up again after I clean it?"
    a: "Something is actively writing: Windows Update staging files, growing pagefile/hiberfil, runaway log files from a crashing app or driver, cloud sync tools downloading, or a misbehaving app writing temp files it never deletes. After cleaning, monitor with a disk-space visualizer (WizTree or WinDirStat) run a week apart and compare — the growing folder reveals the culprit. Recurring mystery growth is a symptom worth diagnosing, not just re-cleaning."
  - q: "Can I move programs to another drive to free C: space?"
    a: "For Microsoft Store apps, yes: Settings > Apps > Installed apps lets you move many Store apps to another drive. For traditional desktop programs, most must be uninstalled and reinstalled with a custom path — simply dragging program folders breaks them. Steam, Epic, and other game launchers let you move game libraries to another drive natively, which is the biggest single win for gamers. Future installs: choose the custom install path at setup time."
---

The red bar in File Explorer says it all: your ASUS laptop's C: drive is nearly full, Windows nags you about low disk space, updates fail for lack of room, and everything feels slower because the system has no breathing room. Laptop SSDs — often just 256GB or 512GB — fill up faster than anyone expects.

Freeing space safely is a priority-ordered hunt: the biggest wins come from Windows' own leftover files, then personal data, then applications. This guide works through them biggest-first so you reclaim gigabytes in minutes, not megabytes in hours. For the general Windows 11 version, see [freeing up disk space on Windows 11](/articles/how-to-free-up-disk-space-on-windows-11/); if the disk is also pinned at 100% activity, read [fixing 100% disk active time](/articles/how-to-fix-disk-active-time-100-percent-step-by-step/).

## Why this happens

- **Windows Update leftovers**: Previous installations, update cleanup files, and delivery optimization caches can consume 20-40GB.

- **Hibernation file (hiberfil.sys)**: Hibernation reserves disk equal to a large fraction of RAM — 8-16GB on typical laptops.

- **Bloated page file**: Pagefile.sys grows with RAM size and crash-dump settings, sometimes reaching 10GB+.

- **ASUS preinstalled software**: MyASUS, Armoury Crate caches, and bundled trials consume space and download updates silently.

- **Game libraries on C:**: Steam/Epic default installs on C: devour tens of gigabytes per title.

- **Cloud sync downloads**: OneDrive/Dropbox set to keep everything locally duplicate cloud storage onto the small SSD.

- **Temp and log accumulation**: Crashing apps and drivers can write gigabytes of logs; temp folders accumulate for years.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Map the disk with a visualizer

You cannot free space efficiently without knowing where it went; a treemap shows it in seconds.

1. Download **WizTree** (free, extremely fast) and run it as administrator on C:.
2. Sort by size and note the top 5 space consumers — typical leaders: Windows, Users, Program Files, pagefile.sys, hiberfil.sys.
3. Expand the biggest folders to find the specific subfolders responsible (e.g., C:\Windows\SoftwareDistribution, a game folder, a sync folder).
4. Take a screenshot or note the numbers — you will compare after cleanup to confirm the wins.
5. Do not delete anything yet; the next fixes handle each category safely.

### Fix 2: Remove Windows' own leftover files

The safest big win: Windows knows which of its files are disposable.

1. Open **Settings > System > Storage > Temporary files**, check **Previous Windows installations**, **Windows Update Cleanup**, **Delivery Optimization Files**, and **Temporary files**, then **Remove files** (15-30GB typical).
2. Run **Disk Cleanup** (cleanmgr) as administrator, click **Clean up system files**, and check the same categories for anything Settings missed.
3. In **Settings > System > Storage**, turn on **Storage Sense** and configure it to run automatically and clean the Recycle Bin and Downloads on a schedule.
4. Check **C:\Windows\SoftwareDistribution\Download** — if Disk Cleanup already handled updates, this should be small; never delete it manually while updates are pending.
5. Re-run WizTree afterward to confirm the reclaimed space.

### Fix 3: Shrink hiberfil.sys and pagefile.sys

These two hidden system files often total 15-25GB on laptops with 16GB RAM.

1. Decide on hibernation: if you never hibernate (most laptop users just sleep), disable it — elevated Command Prompt: **powercfg /hibernate off** — this deletes hiberfil.sys immediately.
2. If you use hibernation, shrink it instead: **powercfg /hibernate /size 50** cuts it to 50% of RAM.
3. For the page file: **System > Advanced system settings > Performance > Settings > Advanced > Virtual memory > Change** — keep it **System managed** (safest) unless you know you need custom sizing.
4. Do not disable the page file entirely — Windows and many apps expect it to exist, and crashes become harder to diagnose.
5. These changes take effect after a restart; verify with WizTree that the files shrank.

### Fix 4: Tame ASUS preloads and app data

ASUS laptops carry their own space consumers beyond Windows'.

1. Open **Settings > Apps > Installed apps** and uninstall ASUS-bundled trials and utilities you never use (keep MyASUS for driver updates if you rely on it).
2. In **MyASUS**, check for downloaded update packages cached locally and clear them after successful installs.
3. Clear Armoury Crate / ASUS app caches if present; game-service caches can grow to multiple gigabytes.
4. Check **C:\Users\<you>\AppData** in WizTree — app caches (browsers, Discord, Spotify) often hold gigabytes; clear them from within each app's settings rather than deleting blindly.
5. Empty the **Recycle Bin** — deleted files still occupy disk until it is emptied.

### Fix 5: Move games and large media off C:

For most users, this is where the tens of gigabytes hide.

1. In **Steam > Settings > Storage**, add a library folder on another drive (or external SSD) and move installed games there — no re-downloading needed.
2. Epic Games Launcher: uninstall the game, then reinstall choosing the new location (Epic lacks Steam's move feature).
3. Move personal media (videos, photos, ISOs) to an external drive or cloud; keep only active projects on C:.
4. For **OneDrive**: **Settings > Sync and backup > Advanced > Files On-Demand** on, then right-click big synced folders > **Free up space** to keep placeholders instead of full copies.
5. Uninstall desktop programs you no longer use via **Settings > Apps** — sort by size to find the heavyweights first.

### Fix 6: Hunt recurring growth and logs

If space vanishes again after cleaning, find the process doing the writing.

1. Run WizTree, clean, then run it again a week later and compare — the growing folder is your culprit.
2. Check **C:\Windows\Logs** and **C:\Users\<you>\AppData\Local\Temp** for runaway log files (some crashing drivers write gigabytes).
3. Open **Event Viewer > Windows Logs > System/Application** for apps logging errors thousands of times per hour — fix or update the offending app.
4. Use **Resource Monitor > Disk** tab sorted by Total to catch processes writing heavily in real time.
5. For chronic temp-file producers, a scheduled Storage Sense run (Fix 2) keeps them from accumulating again.

### Fix 7: Extend C: or upgrade storage when cleanup is not enough

Sometimes the drive is simply too small for the workload; solve the capacity problem structurally.

1. Check **Disk Management** (diskmgmt.msc): if unallocated space sits adjacent to C:, right-click C: > **Extend Volume**.
2. If another partition (like D:) has free space, you can shrink it and extend C: into the freed space (third-party partition tools make non-adjacent moves easier).
3. Consider a larger SSD: check your ASUS model's manual for M.2 slot availability — many ASUS laptops support adding a second SSD for data while keeping C: lean.
4. When reinstalling or resetting Windows, partition deliberately: give C: at least 150-200GB on a 512GB drive.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents Storage Sense and Disk Cleanup officially if you want the reference procedures.

## Closing

A full C: drive on an ASUS laptop is almost always Windows leftovers, hibernation/page files, and games or sync data in the wrong place — in that order. Map it with WizTree, clear Windows' disposable files, shrink the system files, move the big libraries, and automate the rest with Storage Sense. Do it once properly and the red bar stays away.
