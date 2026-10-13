---
title: "C: Drive Low on Space in Windows 11? Reclaim Gigabytes Fast"
slug: how-to-fix-low-disk-space-on-c-drive-on-windows-11
date: 2026-09-05
categories: ["performance"]
tags: ["low disk space", "c drive full", "windows 11", "disk cleanup", "storage"]
description: "Windows 11 warning about low disk space on C:? Find what's eating your drive and reclaim tens of gigabytes with safe, proven cleanup steps."
thumbnail: "/images/thumbs/how-to-fix-low-disk-space-on-c-drive-on-windows-11.webp"
faqs:
  - q: "How much free space should I keep on my C: drive?"
    a: "Aim for at least 15–20% of the drive free, with an absolute minimum of 15–20 GB on modern Windows 11 systems. Below that, Windows Update can't stage updates, virtual memory can't expand, apps can't write temp files, and the whole system slows down noticeably. SSDs also wear faster and perform worse when nearly full, so free space is both a performance and longevity issue."
  - q: "Is it safe to delete the Windows.old folder?"
    a: "Yes, once you're confident you won't roll back to the previous Windows build — Windows.old is the backup of your old installation kept for 10 days after a feature update precisely for rollbacks. After that window, or if you're happy with the new build, delete it via Disk Cleanup (Clean up system files > Previous Windows installations). Never delete it manually with Shift+Delete; the proper tool handles permissions correctly."
  - q: "Why does my C: drive keep filling up by itself?"
    a: "The usual self-filling culprits: Windows Update staging files, restore points accumulating, the Delivery Optimization cache, browser caches, temp files from installers, hibernation file (hiberfil.sys, often several GB), and apps like Teams/OneDrive caching data. If the drive fills rapidly with no explanation, check for a runaway log file — some buggy apps write gigabytes of logs — using a disk analyzer like WinDirStat or WizTree to find the exact folder."
  - q: "Can I move programs from C: to another drive?"
    a: "Some Microsoft Store apps can be moved via Settings > Apps > Installed apps > Move, but traditional desktop programs generally can't be moved after installation — they must be uninstalled and reinstalled to the new location. The practical approach: change default save locations for documents/downloads to another drive, move your user folders (Documents, Downloads, Pictures), and install large new programs to the secondary drive from the start."
---

The red bar in File Explorer. The "Low Disk Space" warnings. Windows Update failing with cryptic errors. A C: drive gasping for air makes everything worse — updates fail, apps crash on save, virtual memory can't expand, and the whole system feels sluggish. On laptops with 256GB SSDs (still extremely common), it's almost a rite of passage.

The good news: on most systems, 20–50GB of reclaimable space is sitting in plain sight — old update files, temp data, caches, and forgotten downloads. The key is knowing what's safe to delete (a lot) versus what isn't (a few critical things). This guide walks the safe path first, then the advanced options, so you reclaim maximum space with zero risk to your system.

Pair this with [scheduling automatic Disk Cleanup](/articles/how-to-schedule-disk-cleanup-in-windows-11-24h2/) so the drive stays clean, and [freeing up disk space generally](/articles/how-to-free-up-disk-space-on-windows-11/) for the companion overview.

## Why this happens

- **Windows Update staging and rollback files**: Update caches, delivery optimization data, and Windows.old can consume 20–40GB.
- **Temp files accumulating**: Installer leftovers, app caches, and Windows temp folders grow silently for months.
- **Restore points and shadow copies**: System Protection storing many restore points eats gigabytes invisibly.
- **Hibernation file**: hiberfil.sys reserves RAM-sized disk space (8–32GB) even if you never hibernate.
- **User data creep**: Downloads, Desktop, and Documents folders ballooning with forgotten large files.
- **App caches**: Browsers, Teams, OneDrive, and creative apps caching gigabytes of data.
- **Small SSD from the factory**: 128–256GB drives simply fill fast under Windows 11's footprint plus apps.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Find out what's actually eating the space

Don't delete blindly — get a map first.

1. Go to **Settings** > **System** > **Storage** — Windows 11's built-in breakdown shows exactly how much space goes to Apps, Temporary files, Documents, and Other. Click each category for details.
2. In the Storage page, click **Temporary files** — check every safe box (Temporary files, Thumbnails, Delivery Optimization Files, Recycle Bin, Previous Windows installations) and note the total before removing.
3. For a deeper view, install **WizTree** (free, extremely fast) — run it on C: and sort by size. It reveals the exact folders hogging space in seconds.
4. Common surprises people find: `C:\Windows\SoftwareDistribution` (update cache), `C:\$Recycle.Bin`, forgotten VM images, game installers in Downloads, and iPhone backups in AppData.
5. Write down your top 5 space hogs — you'll target them specifically in the fixes below.

### Fix 2: Run Disk Cleanup like a professional

The built-in tool, used properly, reclaims the most space safely.

1. Press **Win + R**, type `cleanmgr.exe`, press Enter, select **C:**, and click **Clean up system files** (this restarts the tool with admin rights and unlocks the big categories).
2. Check: **Windows Update Cleanup** (often 5–15GB), **Previous Windows installations** (Windows.old, 15–30GB — only if you won't roll back), **Temporary files**, **Recycle Bin**, **Thumbnails**, **Delivery Optimization Files**, and **Device driver packages**.
3. Click OK > **Delete Files** and let it run — the Windows Update Cleanup phase can take 10–20 minutes; that's normal.
4. After it finishes, check **Settings** > **System** > **Storage** again to measure what you reclaimed.
5. Repeat this monthly, or automate it — see our guide on [scheduling Disk Cleanup](/articles/how-to-schedule-disk-cleanup-in-windows-11-24h2/).

### Fix 3: Tame System Restore and shadow copies

Restore points are useful, but unbounded ones are expensive.

1. Press **Win + R**, type `sysdm.cpl` > **System Protection** tab > select **C:** > **Configure**.
2. Note the **Current Usage** — on some systems it's 20–50GB of restore points. Reduce **Max Usage** to 5–10% (or about 5GB on a 256GB drive).
3. Click **Delete** to remove all but the most recent restore point — this is safe; you keep one good fallback.
4. Alternatively, run `vssadmin delete shadows /for=C: /oldest` in an elevated terminal to trim old shadow copies without touching settings.
5. Don't disable System Protection entirely — one recent restore point has saved countless systems. Just cap its appetite.

### Fix 4: Disable hibernation if you don't use it

Instant multi-gigabyte win on most laptops.

1. Open **Terminal (Admin)** and run `powercfg /hibernate off` — this deletes hiberfil.sys immediately, freeing RAM-sized space (8GB on 8GB machines, 16GB on 16GB machines, etc.).
2. Verify: check C: root — hiberfil.sys should be gone, and Storage settings should show the reclaimed space.
3. Understand the trade-off: you lose **Hibernate** from the power menu (Sleep still works fine). Most laptop users never hibernate — Sleep plus modern standby covers it.
4. If you actually use Hibernate, skip this — instead reduce its size: `powercfg /hibernate /size 50` shrinks the file to 50% of RAM.
5. Re-enable anytime with `powercfg /hibernate on` if you change your mind.

### Fix 5: Move user folders and clean Downloads

Your files, not Windows, are often the real hog.

1. Open File Explorer, right-click **Downloads** > **Properties** > **Location** > **Move** — point it to a folder on another drive (or an external drive). Do the same for **Documents**, **Pictures**, and **Videos** if they're large.
2. Sort Downloads by size and delete installers you'll never run again — old setup executables, ISOs, and zip files are classic space wasters.
3. Check **Desktop** — files on the Desktop live on C: and people forget they're there. Move large files elsewhere.
4. Empty the **Recycle Bin** properly — right-click > **Empty Recycle Bin**. "Deleted" files still occupy space until you do.
5. For cloud storage: in OneDrive/Dropbox settings, use **Files On-Demand** so cloud files don't all sync locally — this alone can free tens of GB.

### Fix 6: Clear app caches surgically

Target the worst offenders without nuking anything important.

1. Browsers: **Chrome/Edge** > Settings > **Privacy** > **Clear browsing data** > **Cached images and files** (keep cookies/history unless you want a full reset) — often 1–5GB.
2. **Teams**: clear `%appdata%\Microsoft\Teams\Cache` and the GPUCache folders — Teams' cache notoriously grows to multiple GB.
3. **Windows Temp**: press **Win + R** > `%temp%` > **Ctrl + A** > Delete (skip files in use) — safe; these are regenerable temp files.
4. **Delivery Optimization**: **Settings** > **Windows Update** > **Advanced options** > **Delivery Optimization** > clear the cache, and consider limiting its cache size.
5. Check Microsoft's official [Windows support page](https://support.microsoft.com/en-us/windows) for guidance on storage management if you're unsure about any category — when in doubt, leave it.

### Fix 7: Advanced moves — compact OS and storage sense

The final layer for stubbornly full drives.

1. Enable **Storage Sense**: **Settings** > **System** > **Storage** > **Storage Sense** > On, configured to run automatically and clean the Recycle Bin and Downloads folder on a schedule.
2. Consider **CompactOS**: in elevated Terminal, run `compact.exe /compactOS:query` to check status, then `compact.exe /compactOS:always` to compress Windows system files — typically saves 2–4GB with negligible performance impact on modern CPUs.
3. Move the **pagefile** if you have a second drive: `sysdm.cpl` > **Advanced** > **Performance Settings** > **Advanced** > **Virtual memory** > **Change** — set C: to "No paging file" and create a system-managed pagefile on the other drive. (Only with a second internal drive; never put it on a slow USB stick.)
4. Uninstall apps you don't use: **Settings** > **Apps** > **Installed apps**, sort by size, and remove the big ones you forgot about.
5. If the drive is still critically full after all this, it's time to face reality: clone to a larger SSD. A 512GB or 1TB SSD upgrade is cheap, and migration tools make it painless — no amount of cleanup fixes a drive that's simply too small for your needs.

## Closing

Low disk space on C: is a maintenance problem, not a mystery — Windows accumulates cruft, and the fixes are all built into the system. Map what's eating space, run a proper Disk Cleanup, cap restore points, ditch hibernation if you don't use it, and move your big folders. Then turn on Storage Sense so you never have to do emergency cleanup again.
